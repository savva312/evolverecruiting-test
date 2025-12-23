# Scholarships and discounts data dictionary

Schema reference for `scholarships-discounts.csv`.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| scholarship_id | Stable unique identifier. | string | `schol-ng-2025-early` | Lowercase, ASCII. |
| name | Scholarship/discount name. | string | `Early payment Nigeria` | Clear, descriptive. |
| audience | Eligible audience. | string | `Nigerian undergraduates` | Free text. |
| type | Award type. | enum | `discount` | Example: `merit`, `need`, `discount`, `other`. |
| value | Award value. | string | `10% tuition` | Percent or amount; specify currency if not EUR. |
| stacking_rules | Stacking/combination rules. | string | `Stackable with sibling; not with merit tier 2.` | Concise. |
| notes | Additional guidance. | string | `Use for early-cycle deposits.` | Concise. |
| as_of | Snapshot date. | date (YYYY-MM-DD) | `2025-12-20` | Required for all rows. |
