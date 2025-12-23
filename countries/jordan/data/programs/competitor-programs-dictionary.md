# Competitor programs data dictionary

Schema reference for `competitor-programs.csv`. Use `field-standards.md` for currency and date conventions.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| competitor | Competitor institution name. | string | `German Jordanian University` | Should match `competitors.csv` `name`; consider linking via IDs when available. |
| program_name | Program title. | string | `BSc Computer Engineering` | Official program name. |
| degree_level | Degree level. | enum | `bachelor` | Suggested: `bachelor`, `master`, `doctoral`, `certificate`, `other`. |
| delivery | Delivery mode. | enum | `on-campus` | Use `on-campus`, `online`, `hybrid`. |
| tuition_eur | Annual tuition in EUR. | decimal | `6500` | Numeric only. |
| location | Campus city/country. | string | `Amman, JO` | Free text but include country code. |
| language | Primary instruction language. | string | `English` | Free text. |
| intake_months | Months with intakes. | multi-enum | `September;February` | Semicolon-separated month names (Title case). |
| notes | Positioning or admissions notes. | string | `Applied-sciences model; German industry placements` | Concise. |
| as_of | Snapshot date. | date (YYYY-MM-DD) | `2026-02-04` | Required. |
