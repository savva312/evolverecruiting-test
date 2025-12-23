# Fairs and events data dictionary

Schema reference for `fairs-events.csv`. Use `field-standards.md` for IDs and dates.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| event_id | Stable unique identifier for the fair/event. | string | `event-lb-beirut-2025-edu` | Lowercase, ASCII. |
| name | Event name. | string | `Beirut International Education Fair` | Full event title. |
| city | Host city. | string | `Beirut` | Text. |
| country | Country code. | string (ISO 3166-1 alpha-2) | `LB` | Uppercase codes. |
| start_date | Event start date. | date (YYYY-MM-DD) | `2025-10-12` | Required if known. If only month/season is known, use `YYYY-MM-01` and note it as a placeholder in `notes`. If unknown, leave blank (no `TBD`). |
| end_date | Event end date. | date (YYYY-MM-DD) | `2025-10-13` | May match start if single-day. Leave blank if unknown (no `TBD`). |
| organizer | Hosting organization. | string | `Integral Educational Programs` | Company/association. |
| format | Delivery format. | enum | `in-person` | Use `in-person`, `virtual`, `hybrid`. |
| focus | Primary topic focus. | string | `International study` | Brief theme. |
| expected_attendance | Projected number of attendees. | integer | `2500` | Leave blank if unknown. |
| notes | Booth details, costs, source. | string | `Offers lead scans; early-bird by July` | Keep concise. |
| as_of | Snapshot date. | date (YYYY-MM-DD) | `2025-12-20` | Required. |
