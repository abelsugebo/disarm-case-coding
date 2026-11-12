"""Validate a DISARM case folder (evidence_log.csv + disarm_mapping.csv).

Usage:
    python scripts/validate.py examples/gerd-assab-2025

Uses only the Python standard library.
"""

import csv
import re
import sys
from pathlib import Path

EVIDENCE_ID = re.compile(r"^E\d{2}$")
ROW_ID = re.compile(r"^M\d{2}$")
TACTIC_ID = re.compile(r"^TA(0[1-9]|1[0-8])$")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
PHASES = {"Plan", "Prepare", "Execute", "Assess", "Context"}
CONFIDENCE = {"High", "Medium", "Low to Medium", "Low"}


def read_rows(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def split_ids(value):
    return [v.strip() for v in (value or "").split(";") if v.strip()]


def validate(folder):
    folder = Path(folder)
    errors = []

    evidence = read_rows(folder / "evidence_log.csv")
    known = set()
    for n, row in enumerate(evidence, start=2):
        eid = row["evidence_id"]
        if not EVIDENCE_ID.match(eid):
            errors.append(f"evidence_log.csv line {n}: bad evidence_id '{eid}'")
        if eid in known:
            errors.append(f"evidence_log.csv line {n}: duplicate evidence_id '{eid}'")
        known.add(eid)
        if row["date"] and not DATE.match(row["date"]):
            errors.append(f"evidence_log.csv line {n}: date must be YYYY-MM-DD")
        if not row["description"].strip():
            errors.append(f"evidence_log.csv line {n}: description is empty")

    for n, row in enumerate(evidence, start=2):
        for ref in split_ids(row["linked_ids"]):
            if ref not in known:
                errors.append(f"evidence_log.csv line {n}: linked_ids refers to unknown '{ref}'")

    mapping = read_rows(folder / "disarm_mapping.csv")
    cited = set()
    for n, row in enumerate(mapping, start=2):
        if not ROW_ID.match(row["row_id"]):
            errors.append(f"disarm_mapping.csv line {n}: bad row_id '{row['row_id']}'")
        if row["disarm_phase"] not in PHASES:
            errors.append(f"disarm_mapping.csv line {n}: unknown phase '{row['disarm_phase']}'")
        tid = row["disarm_tactic_id"]
        if row["disarm_phase"] == "Context":
            if tid:
                errors.append(f"disarm_mapping.csv line {n}: context rows take no tactic ID")
        elif not TACTIC_ID.match(tid):
            errors.append(f"disarm_mapping.csv line {n}: bad tactic ID '{tid}'")
        if row["confidence"] not in CONFIDENCE:
            errors.append(f"disarm_mapping.csv line {n}: unknown confidence '{row['confidence']}'")
        refs = split_ids(row["evidence_ids"])
        if not refs:
            errors.append(f"disarm_mapping.csv line {n}: no evidence_ids cited")
        for ref in refs:
            cited.add(ref)
            if ref not in known:
                errors.append(f"disarm_mapping.csv line {n}: unknown evidence ID '{ref}'")

    uncited = sorted(known - cited)
    return errors, len(evidence), len(mapping), uncited


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    errors, n_evidence, n_mapping, uncited = validate(sys.argv[1])
    print(f"{n_evidence} evidence items, {n_mapping} mapping rows")
    if uncited:
        print("Evidence not cited in any mapping row (fine for context or anchors): " + ", ".join(uncited))
    if errors:
        print(f"{len(errors)} problem(s):")
        for e in errors:
            print("  - " + e)
        sys.exit(1)
    print("OK")


if __name__ == "__main__":
    main()
