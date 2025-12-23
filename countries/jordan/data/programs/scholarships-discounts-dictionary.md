# Scholarships and discounts data dictionary

Schema reference for `scholarships-discounts.csv`. Follow currency and date standards in `field-standards.md`.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| scholarship_id | Stable identifier for the offer. | string | `sch-jo-athens-early-apply` | Lowercase, ASCII. |
| name | Scholarship/discount name. | string | `Jordan Athens Early Application Grant` | Official label. |
| eligibility | Eligibility summary. | string | `Jordan applicants with Tawjihi ≥85% or IB 32+` | Short rule description. |
| amount_type | Type of amount offered. | enum | `percentage` | Use `percentage`, `fixed_amount`, `range`, `other`. |
| amount_value | Value of the benefit. | decimal | `25` | Numeric; interpret with `amount_type`. |
| currency | Currency code when `amount_type=fixed_amount`. | string (ISO 4217) | `EUR` | Uppercase; blank for percentage. |
| deadline | Application deadline date. | date (YYYY-MM-DD) | `2026-04-01` | Leave blank if rolling. |
| source | Source link or contact. | string | `https://www.unic.ac.cy/scholarships` | URL or short citation. |
| notes | Additional terms, renewal rules. | string | `Stackable with sibling discount; verify MoHESR approvals` | Concise. |
| as_of | Snapshot date. | date (YYYY-MM-DD) | `2026-02-04` | Required. |
