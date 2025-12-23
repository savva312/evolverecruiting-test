# Fairs and events data dictionary

Schema reference for `fairs-events.csv`. Use `field-standards.md` for IDs and dates.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| event_id | Stable unique identifier for the fair/event. | string | `event-rs-belgrade-2025-edu` | Lowercase, ASCII. |
| name | Event name. | string | `Belgrade International Education Fair` | Full event title. |
| city | Host city. | string | `Belgrade` | Text. |
| country | Country code. | string (ISO 3166-1 alpha-2) | `RS` | Uppercase codes. |
| start_date | Event start date. | date (YYYY-MM-DD) | `2025-10-12` | Required. |
| end_date | Event end date. | date (YYYY-MM-DD) | `2025-10-13` | May match start if single-day. |
| organizer | Hosting organization. | string | `Integral Educational Programs` | Company/association. |
| format | Delivery format. | enum | `in-person` | Use `in-person`, `virtual`, `hybrid`. |
| focus | Primary topic focus. | string | `International study` | Brief theme. |
| expected_attendance | Projected number of attendees. | integer | `2500` | Leave blank if unknown. |
| notes | Booth details, costs, source. | string | `Offers lead scans; early-bird by July` | Keep concise. |
| as_of | Snapshot date. | date (YYYY-MM-DD) | `2025-12-20` | Required. |
