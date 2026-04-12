# Scholarships and discounts data dictionary

Schema reference for `scholarships-discounts.csv`. Follow currency and date standards in `field-standards.md`.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| scholarship_id | Stable identifier for the offer. | string | `unic_nicosia_merit_cgpa` | Lowercase, ASCII; encode campus where useful (e.g., `unic_nicosia_*`, `unic_athens_*`). |
| name | Scholarship/discount name. | string | `UNIC Nicosia Academic Merit Scholarship (CGPA)` | Official label or counselor-facing shorthand; include campus in the name when helpful. |
| eligibility | Eligibility summary. | string | `Romanian (EU) admits with high school leaving certificate ≥18/20 or equivalent` | Short rule description; mention campus, study level (UG/PG), and any nationality/residency constraints. |
| amount_type | Type of amount offered. | enum | `percentage` | Use `percentage`, `fixed_amount`, `range`, `other`; for loans or work-study use `other`. |
| amount_value | Value of the benefit. | decimal / short range | `10-50` | Numeric where a single value is published; short ranges like `10-50` allowed when sources specify bands; leave blank if not published. |
| currency | Currency code when `amount_type=fixed_amount` or when the benefit is expressed as a monetary range. | string (ISO 4217) | `EUR` | Uppercase ISO 4217 code; use `EUR` for UNIC monetary amounts and leave blank for percentage-style awards or where no fixed currency amount is published. |
| deadline | Application deadline date. | date (YYYY-MM-DD) | `2026-04-01` | Leave blank if rolling; capture key scholarship cut-offs when they are published. |
| source | Source link or contact. | string | `https://www.unic.ac.cy/nicosia/scholarships-financial-aid/` | Public URL (UNIC page, EU programme, government portal) or a short repo citation when pointing to an internal summary. |
| notes | Additional terms, renewal rules, stacking. | string | `Applies after first year; not normally stackable with other UNIC scholarships—highest tuition reduction applies.` | Concise; include renewal GPA rules, stacking/exclusion notes, and any Romania-specific caveats (e.g., EU-only, Cyprus permanent residency). |
| as_of | Snapshot date. | date (YYYY-MM-DD) | `2026-04-12` | Required; ISO 8601 date representing when sources were last checked for this row. |
