# Schools data dictionary

Schema reference for `schools.csv`. Follow shared rules in `../field-standards.md` for IDs, dates, and encoding.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| school_id | Stable unique identifier for the school. | string | `ng-lagos-aisl` | Lowercase, ASCII; hyphenated; do not reuse. |
| name | Official school name (English). | string | `American International School of Lagos` | Keep full legal/brand name. |
| city | City where the school is located. | string | `Lagos` | Use Nigerian spelling in English. |
| region | Nigerian state/region. | string | `Lagos State` | Free text; align with national regions list when possible. |
| area | Sub-city area or corridor. | string | `Victoria Island` | Helps target travel planning. |
| priority_tier | Affordability tier from the source report. | enum | `Tier1` | Use `Tier1`, `Tier2A`, `Tier2B`, `Tier3-proxy`. |
| evidence_level | Strength of fee/pathway evidence. | enum | `high` | `high`, `medium`, `proxy`, `opaque`. |
| day_boarding | Operating model. | enum | `day+boarding` | `day`, `boarding`, `day+boarding`, `unknown`. |
| curricula | Curricula or leaving qualifications. | multi-enum | `cambridge-igcse; a-levels` | Semicolon-separated; use lowercase descriptors. |
| international_pathway | Short text on pathway/qualification signals. | string | `American curriculum with IB DP signal` | Keep concise. |
| fee_basis | Currency basis for cited fees. | enum | `USD` | `USD`, `GBP`, `EUR`, `NGN`, `on-request`, `not-published`. |
| fee_note | Brief fee evidence or note. | string | `USD 28k–32k tuition reported for 2025` | Include term/annual clarity when known. |
| affordability_fit | Recruiting fit shorthand. | enum | `very-strong` | `very-strong`, `strong`, `moderate`, `validate`. |
| program_fit_tags | Programs likely to fit (semicolon). | multi-enum | `medicine;business;cs-data-ai` | Semicolon-separated; keep lowercase. |
| notes_short | Context or operational note. | string | `Hard-currency fees; confirm current sheet directly.` | Keep concise; no PII. |
| sources | URLs or repo references. | multi-enum | `report-20251220` | Semicolon-separated; cite the Nigeria premium pipeline report or public links. |
| last_verified | Snapshot date for this row. | date (YYYY-MM-DD) | `2025-12-20` | See `field-standards.md`. |
