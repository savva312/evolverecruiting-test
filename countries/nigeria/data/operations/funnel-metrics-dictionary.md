# Funnel metrics data dictionary

Schema reference for `funnel-metrics.csv`.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| metric_id | Unique identifier. | string | `fn-ng-2025-q1` | Lowercase, ASCII. |
| stage | Funnel stage. | enum | `inquiries` | Example: `impressions`, `clicks`, `leads`, `inquiries`, `applications`, `offers`, `deposits`, `enrolled`. |
| value | Metric value. | number | `120` | Numeric. |
| period | Time period. | string | `2025-Q1` | Month/quarter as text. |
| source | Data source. | string | `CRM` | Free text. |
| notes | Context. | string | `Nigeria-only campaigns.` | Concise. |
| as_of | Snapshot date. | date (YYYY-MM-DD) | `2025-12-20` | Required for all rows. |
