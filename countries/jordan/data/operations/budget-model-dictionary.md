# Budget model data dictionary

Schema reference for `budget-model.csv`. Use `field-standards.md` for currency and period conventions.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| category | Top-level budget category. | enum | `marketing` | Suggested: `marketing`, `events`, `personnel`, `travel`, `technology`, `other`. |
| sub_category | More specific breakdown. | string | `paid_social` | Free text label. |
| period | Time period for the budget line. | period | `2026-Q2` | Use `YYYY`, `YYYY-Q#`, or `YYYY-MM`. |
| amount_eur | Budgeted amount in EUR. | decimal | `12000` | Numeric only. |
| assumptions | Key calculation notes. | string | `€6 CPL x 2,000 leads for Jordan` | Short rationale. |
| owner | Responsible person/team. | string | `Jordan marketing pod` | Free text. |
| notes | Additional context or links. | string | `Includes Arabic copywriting and localization` | Concise. |
| as_of | Snapshot date. | date (YYYY-MM-DD) | `2026-02-04` | Required. |
