# DISARM Case Coding Toolkit

A lightweight, spreadsheet-friendly method for documenting influence-operation behavior with the [DISARM Red Framework](https://github.com/DISARMFoundation/DISARMframeworks): an evidence log, a behavior-to-tactic mapping table, a codebook, and a validation script. It includes a fully coded worked example from a published case study.

**Author:** Abel W. Sugebo, information-integrity and OSINT researcher, Certified DISARM Analyst
**Companion guide:** [Using the DISARM Framework in Research](https://data-knowledge-hub.com/docs/data-analysis/04_04_disarm-framework/) (Data Knowledge Hub, 2025), which explains the framework this toolkit puts into practice.

## Why this exists

DISARM gives analysts a shared vocabulary for influence operations, but most case studies stop at a narrative description. This toolkit turns the method into two linked tables so that every claim in a report traces back to a logged, preserved artifact, and every artifact has a stated confidence level. It is designed for small research teams and fact-checkers who work in spreadsheets, not code.

Three rules govern the method:

1. **Map behavior, not intent.** A row records what was observed. It never asserts who coordinated it or why.
2. **No claim without evidence IDs.** Every mapping row cites one or more evidence-log IDs.
3. **Confidence is explicit.** Each mapping carries High, Medium, Low, or Low to Medium confidence, with the reasoning in the notes.

## Repository layout

```
codebook/
  CODEBOOK.md                 Field definitions, allowed values, coding rules
  evidence_log_template.csv   Empty evidence log
  disarm_mapping_template.csv Empty behavior-to-tactic mapping table
examples/gerd-assab-2025/
  README.md                   Case summary and how to read the example
  evidence_log.csv            E01 to E14, as described in the published report
  disarm_mapping.csv          Table 1 of the report, with DISARM tactic IDs added
scripts/
  validate.py                 Checks IDs, references, and allowed values (Python standard library only)
```

## Quick start

1. Copy the two templates in `codebook/` into a spreadsheet or keep them as CSV.
2. Log each artifact in `evidence_log_template.csv` as you collect it. Preserve a screenshot or archive link before you code anything.
3. Map observed behaviors in `disarm_mapping_template.csv`, citing evidence IDs.
4. Check the files:

```bash
python scripts/validate.py examples/gerd-assab-2025
```

## Worked example

[`examples/gerd-assab-2025`](examples/gerd-assab-2025) codes a 2025 case study of AI-generated and visual propaganda that linked pride in the Grand Ethiopian Renaissance Dam (GERD) to "Assab / sea access" narratives on X and YouTube. It shows synthetic visuals, a long-form-to-short-clip amplification chain, multilingual resonance, and counter-messaging mapped to five DISARM tactics.

Source report: *DISARM Case Study: AI-Generated Propaganda Linking GERD Pride to "Assab/Sea Access" Narratives* (Inform Africa / HaqCheck, 2025), [PDF](https://informafrica.net/wp-content/uploads/2025/12/Disarm-Case-Study_-AI-Generated-Propaganda-Linking-GERD-Pride-To-_Assab_Sea-Access_-Narratives_final_inform_africa.pdf).

## Ethics

The example contains no account names, handles, URLs to the original posts, or reproduced content. It records only what the published report states. Apply the same restraint in new cases: log artifacts privately with full provenance, and publish behavior-level descriptions.

## Related work

- [checked-fact-checking-method](https://github.com/abelsugebo/checked-fact-checking-method): the HaqCheck CHECKED workflow for verifying individual claims. This toolkit covers the campaign behavior behind them.

## License

[CC BY 4.0](LICENSE.md). Reuse and adapt freely with attribution.

## Contact

[abelsugebo.com](https://abelsugebo.com) · [LinkedIn](https://www.linkedin.com/in/abel-wabella-sugebo/)
