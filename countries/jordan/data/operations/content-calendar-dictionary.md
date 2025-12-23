# Content calendar data dictionary

Schema reference for `content-calendar.csv`. Apply shared standards in `field-standards.md`.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| content_id | Unique content item ID. | string | `cnt-jo-2026-ramadan-webinar` | Lowercase, ASCII. |
| title | Content or campaign title. | string | `Ramadan parent webinar: studying in Greece` | Concise label. |
| channel | Channel/format. | enum | `webinar` | Examples: `blog`, `email`, `webinar`, `social`, `press`, `event`. |
| target_audience | Intended audience. | string | `Parents in Amman` | Free text segment. |
| publish_date | Planned publish date. | date (YYYY-MM-DD) | `2026-03-10` | Required for scheduled items. |
| owner | Content owner. | string | `Jordan marketing` | Team or person. |
| status | Current status. | enum | `planned` | Use `planned`, `in-progress`, `scheduled`, `shipped`, `repurpose`. |
| notes | Supporting context or links. | string | `Align with QS Amman fair follow-up` | Concise. |
| as_of | Snapshot date. | date (YYYY-MM-DD) | `2026-02-04` | Required. |
