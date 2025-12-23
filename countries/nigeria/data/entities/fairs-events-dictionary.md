# Fairs and events data dictionary

Schema reference for `fairs-events.csv`. Apply shared standards from `../field-standards.md`.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| event_id | Stable unique identifier for the fair/event. | string | `event-ng-lagos-2025-edu` | Lowercase, ASCII. |
| name | Event name. | string | `Lagos International Education Fair` | Full event title. |
| city | Host city. | string | `Lagos` | Text. |
| organizer | Organizer name. | string | `Example Fairs Ltd` | Company/organization. |
| timing | Event timing. | string | `Oct 2025` | Month/year or date range. |
| format | Event format. | enum | `in-person` | Use `in-person`, `virtual`, or `hybrid`. |
| notes | Participation notes or focus. | string | `Medicine-heavy audience; agents invited` | Keep concise. |
| as_of | Snapshot date. | date (YYYY-MM-DD) | `2025-12-20` | Required for all rows. |
