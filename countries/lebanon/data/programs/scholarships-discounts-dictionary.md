# Scholarships and discounts data dictionary

Schema reference for `scholarships-discounts.csv`. Follow currency and date standards in `field-standards.md`.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| scholarship_id | Stable identifier for the offer. | string | `sch-ath-early-apply` | Lowercase, ASCII. |
| name | Scholarship/discount name. | string | `Athens Early Application Grant` | Official label. |
| eligibility | Eligibility summary. | string | `LB applicants with GPA >5.3` | Short rule description. |
| amount_type | Type of amount offered. | enum | `percentage` | Use `percentage`, `fixed_amount`, `range`, `other`. |
| amount_value | Value of the benefit. | decimal | `25` | Numeric; interpret with `amount_type`. |
| currency | Currency code when `amount_type=fixed_amount`. | string (ISO 4217) | `EUR` | Uppercase; blank for percentage. |
| deadline | Application deadline date. | date (YYYY-MM-DD) | `2025-04-01` | Leave blank if rolling. |
| source | Source link or contact. | string | `https://unic.ac.cy/scholarships` | URL or short citation. |
| notes | Additional terms, renewal rules. | string | `Applies first year only; stackable with merit` | Concise. |
| as_of | Snapshot date. | date (YYYY-MM-DD) | `2025-12-20` | Required. |
