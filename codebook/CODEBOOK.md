# Codebook

## Evidence log (`evidence_log.csv`)

One row per collected artifact or context source.

| Field | Required | Description | Allowed values |
|---|---|---|---|
| `evidence_id` | Yes | Unique ID, assigned in collection order | `E` followed by two digits, e.g. `E01` |
| `date` | No | Publication date of the artifact, ISO format | `YYYY-MM-DD`, or blank if not recorded |
| `platform` | No | Where the artifact appeared | Free text, e.g. `X`, `YouTube`, `News site` |
| `artifact_type` | Yes | What kind of evidence it is | `post`, `video`, `image`, `clip`, `long-form video`, `article`, `context source`, `not described` |
| `language` | No | Language(s) of text or audio | Free text |
| `role` | Yes | The artifact's function in the case | `primary artifact`, `amplification`, `timeline anchor`, `context`, `counter-messaging`, `not described` |
| `description` | Yes | Neutral, behavior-level description. Do not reproduce slogans in full unless analytically necessary. | Free text |
| `linked_ids` | No | Other evidence this item derives from or feeds into | Semicolon-separated IDs, e.g. `E11;E10` |
| `preservation` | No | How the artifact was preserved (keep the actual archive links in a private log) | Free text, e.g. `screenshot; archive link` |

## DISARM mapping (`disarm_mapping.csv`)

One row per observed behavior mapped to a DISARM Red Framework tactic.

| Field | Required | Description | Allowed values |
|---|---|---|---|
| `row_id` | Yes | Unique mapping ID | `M` followed by two digits |
| `disarm_phase` | Yes | DISARM phase of the tactic | `Plan`, `Prepare`, `Execute`, `Assess`, `Context` |
| `disarm_tactic_id` | No | DISARM tactic ID | `TA01` to `TA18`, or blank for context rows |
| `disarm_tactic` | Yes | Tactic name as written in DISARM, or a context label | Free text |
| `observed_behavior` | Yes | What was observed, in one or two sentences | Free text |
| `evidence_ids` | Yes | Supporting evidence | Semicolon-separated IDs that exist in the evidence log |
| `confidence` | Yes | Strength of the evidence for this mapping | `High`, `Medium`, `Low to Medium`, `Low` |
| `notes` | No | Reasoning, caveats, or limits | Free text |

## Coding rules

1. **Behavior, not attribution.** Code what the artifact shows. Coordination, sponsorship, or intent require separate evidence and are out of scope for this table.
2. **Evidence before coding.** An artifact is logged and preserved before it appears in any mapping row.
3. **Confidence scale.**
   - **High:** several independent artifacts clearly show the behavior.
   - **Medium:** the behavior is visible, but evidence is limited in number or partly inferential.
   - **Low to Medium / Low:** a signal is present, but the evidence cannot support the stronger claim (for example, calls to offline action with no evidence of offline outcomes).
4. **Context is not proof.** Background reporting and counter-messaging are logged with the `context` or `counter-messaging` role and are not used to establish the facts of the incident.
5. **Counter-messaging rows.** DISARM's Red Framework describes the influence operation. Contestation by other actors is recorded with phase `Context` and no tactic ID.

## DISARM tactic reference (Red Framework)

| ID | Tactic | Phase |
|---|---|---|
| TA01 | Plan Strategy | Plan |
| TA02 | Plan Objectives | Plan |
| TA13 | Target Audience Analysis | Plan |
| TA05 | Microtarget | Prepare |
| TA06 | Develop Content | Prepare |
| TA07 | Select Channels and Affordances | Prepare |
| TA14 | Develop Narratives | Prepare |
| TA15 | Establish Assets | Prepare |
| TA16 | Establish Legitimacy | Prepare |
| TA08 | Conduct Pump Priming | Execute |
| TA09 | Deliver Content | Execute |
| TA10 | Drive Offline Activity | Execute |
| TA11 | Persist in the Information Environment | Execute |
| TA17 | Maximise Exposure | Execute |
| TA18 | Drive Online Harms | Execute |
| TA12 | Assess Effectiveness | Assess |

Check the [DISARM Foundation framework repository](https://github.com/DISARMFoundation/DISARMframeworks) for the current version before coding a new case.
