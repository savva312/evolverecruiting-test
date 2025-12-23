# Competitors data dictionary

Schema reference for `competitors.csv`. Follow `field-standards.md` for shared fields.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| competitor_id | Stable unique identifier for the competitor. | string | `comp-gr-athens-001` | Lowercase, ASCII. |
| name | Institution/provider name. | string | `European University Cyprus` | Full brand name. |
| home_country | Home country code. | string (ISO 3166-1 alpha-2) | `CY` | Uppercase codes. |
| target_programs | Programs/fields they market in Serbia. | multi-enum | `medicine;business` | Semicolon-separated list. |
| rs_presence | Presence footprint in Serbia. | enum | `local_agent` | Suggested: `none`, `local_agent`, `rep_office`, `alumni_network`, `digital_only`, `other`. |
| notes | Positioning, pricing cues, source links. | string | `Strong scholarship offers; runs Belgrade fairs` | Concise. |
| as_of | Snapshot date. | date (YYYY-MM-DD) | `2025-12-20` | Required. |
