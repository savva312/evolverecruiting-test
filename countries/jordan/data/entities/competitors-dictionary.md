# Competitors data dictionary

Schema reference for `competitors.csv`. Follow `field-standards.md` for shared fields.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| competitor_id | Stable unique identifier for the competitor. | string | `comp-jo-amman-001` | Lowercase, ASCII. |
| name | Institution/provider name. | string | `German Jordanian University` | Full brand name. |
| home_country | Home country code. | string (ISO 3166-1 alpha-2) | `JO` | Uppercase codes. |
| target_programs | Programs/fields they market in Jordan. | multi-enum | `engineering;business` | Semicolon-separated list. |
| jo_presence | Presence footprint in Jordan. | enum | `campus` | Suggested: `none`, `local_agent`, `rep_office`, `campus`, `alumni_network`, `digital_only`, `other`. |
| notes | Positioning, pricing cues, source links. | string | `Applied-sciences positioning with German industry links` | Concise. |
| as_of | Snapshot date. | date (YYYY-MM-DD) | `2026-02-04` | Required. |
