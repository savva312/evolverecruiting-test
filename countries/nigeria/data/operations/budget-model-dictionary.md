# Budget model data dictionary

Schema reference for `budget-model.csv`.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| line_item | Budget line item. | string | `Meta prospecting` | Free text. |
| category | Budget category. | enum | `paid_media` | Example: `paid_media`, `events`, `travel`, `production`, `agency`. |
| planned_amount_eur | Planned amount in EUR. | number | `5000` | Use EUR unless specified. |
| actual_amount_eur | Actual spend in EUR. | number | `4200` | Use EUR unless specified. |
| timeframe | Time period for the spend. | string | `2025-Q1` | Month/quarter as text. |
| notes | Additional context. | string | `Nigeria launch test; adjust after CPL review.` | Concise. |
| as_of | Snapshot date. | date (YYYY-MM-DD) | `2025-12-20` | Required for all rows. |
