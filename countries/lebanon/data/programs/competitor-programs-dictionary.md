# Competitor programs data dictionary

Schema reference for `competitor-programs.csv`. Use `field-standards.md` for currency and date conventions.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| competitor | Competitor institution name. | string | `European University Cyprus` | Should match `competitors.csv` `name`; consider linking via IDs when available. |
| program_name | Program title. | string | `MD Medicine` | Official program name. |
| degree_level | Degree level. | enum | `bachelor` | Suggested: `bachelor`, `master`, `doctoral`, `certificate`, `other`. |
| delivery | Delivery mode. | enum | `on-campus` | Use `on-campus`, `online`, `hybrid`. |
| tuition_eur | Annual tuition in EUR. | decimal | `9000` | Numeric only. |
| location | Campus city/country. | string | `Nicosia, CY` | Free text but include country code. |
| language | Primary instruction language. | string | `English` | Free text. |
| intake_months | Months with intakes. | multi-enum | `February;September` | Semicolon-separated month names (Title case). |
| notes | Positioning or admissions notes. | string | `Scholarships up to 30%` | Concise. |
| as_of | Snapshot date. | date (YYYY-MM-DD) | `2025-12-20` | Required. |
