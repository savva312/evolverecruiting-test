# Scholarships and discounts data dictionary

Schema reference for `scholarships-discounts.csv`. Follow currency and date standards in `field-standards.md`.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| scholarship_id | Stable identifier for the offer. | string | `unic_athens_academic_excellence_gold` | Lowercase, ASCII. |
| campus | Campus that owns the policy. | enum | `unic_nicosia` | `unic_nicosia` or `unic_athens`. |
| name | Scholarship/discount name. | string | `Athens Academic Excellence – Gold` | Official label. |
| eligibility | Eligibility summary. | string | `RO applicants with GPA >5.3` | Short rule description. |
| amount_type | Type of amount offered. | enum | `percentage` | Use `percentage`, `fixed_amount`, `range`, `other`. `range` covers spreads like `10-40`; `other` is for qualitative awards with no numeric value. |
| amount_value | Value of the benefit. | decimal/string | `50` | Numeric; when `amount_type=range` store `min-max` (no symbols); leave blank when `amount_type=other`. |
| currency | Currency code when money is quoted. | string (ISO 4217) | `EUR` | Required for `fixed_amount` or monetary `range`; blank for percentages. |
| deadline | Application deadline date. | date (YYYY-MM-DD) | `2025-04-01` | Leave blank if rolling/continuous. |
| source | Source link or contact. | string | `https://unic.ac.cy/scholarships` | URL or repo path; prefer official campus sources. |
| notes | Additional terms, renewal rules. | string | `Applies first year only; stackable with merit` | Concise; capture Romania-specific constraints. |
| as_of | Snapshot (last verified) date. | date (YYYY-MM-DD) | `2025-12-23` | Required on every row. |
