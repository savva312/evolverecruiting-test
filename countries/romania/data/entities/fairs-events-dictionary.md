# Fairs and events data dictionary

Schema reference for `fairs-events.csv`. Follow `skills/field-standards` for IDs, dates, and naming.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| event_id | Stable unique identifier for the fair/event. | string | `event-ro-riuf` | Lowercase, ASCII; do not reuse IDs for different events. |
| name | Event name. | string | `RIUF - Romanian International University Fair` | Full public-facing title. |
| cities | Primary host cities or `Virtual`. | string (semicolon-separated) | `Bucharest; Cluj-Napoca; Iasi; Timisoara` | Use `City; City` format or `Virtual (national)` for online-only events. |
| country | Country code. | string (ISO 3166-1 alpha-2) | `RO` | Uppercase codes. |
| priority | Commercial importance. | enum | `must-do` | Allowed: `must-do`, `consider`, `monitor`. |
| planning_status | Current internal status. | enum | `targeting` | Allowed: `booked`, `targeting`, `monitoring`, `attended`. |
| start_date | Next confirmed start date. | date (YYYY-MM-DD) or blank | `2025-03-15` | Leave blank if TBC and describe timing in `timing_pattern`. |
| end_date | Next confirmed end date. | date (YYYY-MM-DD) or blank | `2025-03-16` | Match `start_date` for single-day events; leave blank when TBC. |
| timing_pattern | Narrative on cadence/seasonality. | string | `Spring multi-city (Mar) + fall run (Oct)` | Include months, recurring windows, or specific multi-city legs. |
| organizer | Hosting organization. | string | `Educativa (RIUF)` | Company/association; include agency if applicable. |
| format | Delivery format. | enum | `in-person` | Use `in-person`, `virtual`, or `hybrid`. |
| audience_focus | Key attendee types. | string | `Students + parents + counselors` | Short list separated by `+`. |
| expected_attendance | Projected volume per edition. | string | `8000-12000 / season` | Use numerals with ranges; include units (`visitors`, `registrants`). |
| estimated_cost_eur | Anticipated booth/package spend. | string | `EUR 2.2k-3.8k per city` | Use `EUR` plus range or single value. |
| lead_goal | Target outcome (scans, meetings). | string | `600-1000 qualified scans per top city` | Capture the KPI UNIC tracks. |
| profile_path | Relative link to the narrative profile. | path | `countries/romania/entities/fairs-events/profiles/riuf-romanian-international-university-fair.md` | Must match existing profile path. |
| notes | Key fit/actions/risks. | string | `Book seminar + Romanian landing page before Jan.` | Keep concise; cite actions/risks across campuses. |
| as_of | Snapshot date for the row. | date (YYYY-MM-DD) | `2025-12-22` | Required for every row. |
