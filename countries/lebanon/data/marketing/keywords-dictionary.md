# Keywords data dictionary

Schema reference for `keywords.csv`. Use `field-standards.md` for encoding, currency, and dates.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| keyword | Search term. | string | `study medicine in cyprus` | Lowercase text; avoid special characters beyond search intent. |
| intent_stage | Funnel intent stage. | enum | `consideration` | Use `awareness`, `consideration`, `decision`. |
| audience | Target audience description. | string | `HS seniors in Beirut` | Short segment description. |
| est_cpc_eur | Estimated cost-per-click in EUR. | decimal | `0.85` | Numeric only. |
| search_volume_lb | Average monthly searches in Lebanon. | integer | `5400` | Leave blank if unknown. |
| priority | Operational priority flag. | enum | `high` | Use `high`, `medium`, `low`, or blank. |
| notes | Source or targeting nuance. | string | `Based on Google KW Planner Oct 2025` | Concise. |
| as_of | Snapshot date. | date (YYYY-MM-DD) | `2025-12-20` | Required. |
