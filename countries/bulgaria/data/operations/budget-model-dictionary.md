# Budget model data dictionary

Schema reference for `budget-model.csv`. Use `field-standards.md` for currency and period conventions.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| category | Top-level budget category. | enum | `marketing` | Suggested: `marketing`, `events`, `travel`, `technology`, `scholarships_discounts`, `partners_agents`, `personnel`, `other`. Use `scholarships_discounts` for planned tuition discount envelopes (not cash actuals). Use `partners_agents` for commissions and partner enablement/co-marketing placeholders. |
| sub_category | More specific breakdown. | string | `paid_social` | Free text label. |
| period | Time period for the budget line. | period | `2025-Q1` | Use `YYYY`, `YYYY-Q#`, or `YYYY-MM`. |
| amount_eur | Budgeted amount in EUR. | decimal | `15000` | Numeric only. |
| assumptions | Key calculation notes. | string | `€5 CPL x 3,000 leads` | Short rationale. |
| owner | Responsible person/team. | string | `Marketing` | Free text. |
| notes | Additional context or links. | string | `Includes agency fees` | Concise. |
| as_of | Snapshot date. | date (YYYY-MM-DD) | `2025-12-20` | Required. |
