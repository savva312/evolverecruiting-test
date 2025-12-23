# Keywords data dictionary

Schema reference for `keywords.csv`.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| keyword | Search term. | string | `study medicine in cyprus` | Lowercase where possible. |
| intent_stage | Funnel stage. | enum | `high_intent` | Suggested: `discovery`, `consideration`, `high_intent`. |
| audience | Target audience description. | string | `HS seniors in Lagos` | Short segment description. |
| est_cpc_eur | Estimated CPC in EUR. | number | `0.45` | Leave blank if unknown. |
| search_volume_bg | Average monthly searches in Nigeria. | integer | `5400` | Leave blank if unknown. |
| priority | Priority flag. | enum | `p1` | Use `p0`, `p1`, `p2`, `p3`. |
| notes | Additional context or sources. | string | `Google Keyword Planner sample` | Keep concise. |
| as_of | Snapshot date. | date (YYYY-MM-DD) | `2025-12-20` | Required for all rows. |
