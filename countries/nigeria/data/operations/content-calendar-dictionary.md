# Content calendar data dictionary

Schema reference for `content-calendar.csv`.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| content_id | Unique identifier. | string | `cnt-ng-2025-jan-001` | Lowercase, ASCII. |
| title | Content title. | string | `Why UNIC for Nigerian CS students` | Concise. |
| channel | Channel. | enum | `blog` | Example: `blog`, `email`, `social`, `webinar`. |
| publish_date | Planned publish date. | date | `2025-01-15` | `YYYY-MM-DD`. |
| owner | Content owner. | string | `Marketing` | Team/person. |
| status | Status. | enum | `planned` | Example: `planned`, `draft`, `live`, `retired`. |
| notes | Context or links. | string | `Align with Lagos school visits.` | Concise. |
| as_of | Snapshot date. | date (YYYY-MM-DD) | `2025-12-20` | Required for all rows. |
