# Competitors data dictionary

Schema reference for `competitors.csv`. Apply shared standards from `../field-standards.md`.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| competitor_id | Stable unique ID. | string | `comp-ng-med-001` | Lowercase, ASCII. |
| name | Institution/provider name. | string | `Example International University` | Use official/brand name. |
| city | City where the competitor is based or marketed from. | string | `Lagos` | Free text. |
| markets_served | Main source markets. | multi-enum | `NG;GH;UK` | ISO country codes; semicolon-separated. |
| focus_cluster | Primary program cluster focus. | enum | `medicine-md` | Use cluster slugs from `program-clusters`. |
| notes | Positioning, pricing cues, source links. | string | `Strong scholarship offers; runs Lagos fairs` | Concise. |
| as_of | Snapshot date. | date (YYYY-MM-DD) | `2025-12-20` | Required for all rows. |
