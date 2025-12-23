# Event ROI data dictionary

Schema reference for `event-roi.csv`. Follow `countries/lebanon/data/field-standards.md` for null handling, currency conventions, and date formats.

## Definitions (why this exists)

This dataset is a lightweight ROI tracker for fairs/events so the Lebanon team can:
- compare events across seasons (repeat/skip decisions)
- measure *cost per qualified lead* and *cost per start*
- keep the methodology consistent even when organizers change lead delivery formats

## Field reference

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| event_roi_id | Primary key for this ROI row (usually one row per event stop/date/city). | string | `education_fair_beirut_2026_spring` | Stable ASCII string. Do not recycle. |
| event_id | Foreign key to the canonical event entity record in `countries/lebanon/data/entities/fairs-events.csv`. | string | `event-lb-beirut-2026-edu` | Optional until the Lebanon `fairs-events.csv` is populated; leave blank if unknown. |
| event_name | Human-readable event name. | string | `Beirut International Education Fair` | Use the organizer-facing name. |
| event_format | How the event was delivered. | enum | `in_person` | Suggested: `in_person`, `virtual`, `hybrid`. |
| event_city | City where the activity happened (blank for purely virtual). | string | `Beirut` | Free text. |
| country | ISO 3166-1 alpha-2 country code for the city/location. | string | `LB` | Use `LB` for Lebanon. |
| season | Recruiting season label for comparisons. | enum | `2026-spring` | Use `YYYY-spring` or `YYYY-fall`. If needed, use `YYYY-summer` / `YYYY-winter` and document in `notes`. |
| start_date | Start date of the event activity. | date (YYYY-MM-DD) | `2026-03-15` | Required if known. |
| end_date | End date of the event activity. | date (YYYY-MM-DD) | `2026-03-16` | If single-day, repeat `start_date`. |
| cost_currency | Currency code for `cost_total_local`. | string | `EUR` | ISO 4217 alpha-3. |
| cost_total_local | Total event cost in local currency (booth + sponsorship + travel + lodging + other direct costs). | decimal | `2500` | Numeric only; include *all* event-related costs you want reflected in ROI. |
| fx_to_eur | FX rate used to convert local cost into EUR (1 unit of `cost_currency` to EUR). | decimal | `1` | Use `1` when already in EUR. Keep the rate used for auditability. |
| cost_total_eur | Total event cost converted to EUR. | decimal | `2500` | Numeric only. If using EUR directly, `cost_total_eur = cost_total_local`. |
| leads_scanned | Count of raw leads captured (badge scans / QR scans / list uploads), before quality screening. | integer | `300` | **Do not** use this as “qualified leads”. Include duplicates if your capture method does. |
| leads_qualified | Count of leads that meet the team’s qualification definition (after de-dupe and screening). | integer | `180` | Explicitly distinct from `leads_scanned`. Define your qualification rule in `notes` if it changes. |
| applications | Applications attributable to this event within the attribution window. | integer | `25` | Attribution rules must be consistent (see calculation notes). |
| offers | Offers attributable to this event within the attribution window. | integer | `12` |  |
| deposits | Deposits (or equivalent enrollment commitment) attributable to this event. | integer | `6` | If a campus uses a different commitment step, document it in `notes`. |
| starts | Starts attributable to this event (students who actually begin). | integer | `4` | Final ROI output. |
| cost_per_qualified_lead_eur | Derived metric: cost per qualified lead. | decimal | `13.89` | Formula: `cost_total_eur / leads_qualified` (blank if `leads_qualified` is 0/blank). |
| cost_per_start_eur | Derived metric: cost per start. | decimal | `625` | Formula: `cost_total_eur / starts` (blank if `starts` is 0/blank). |
| campus | Campus attribution scope. | enum | `both` | Suggested: `nicosia`, `athens`, `both`. Use `both` if routing was mixed. |
| owner | Internal owner responsible for the record/methodology. | string | `Enrollment Ops` | Team or person. |
| data_source | How counts/costs were obtained. | string | `manual_entry` | Examples: `crm_report`, `event_organizer_list`, `manual_entry`. |
| notes | Methodology, attribution window, and any deviations (e.g., shared booth, co-marketing, partial lead lists). | string | `Attribution window: 60 days post-event` | Keep concise; avoid long narratives. |
| as_of | Snapshot date for this record. | date (YYYY-MM-DD) | `2025-12-22` | Required. |

## Calculation notes (standardize ROI)

Use these defaults unless you explicitly override them in `notes`:
- **Qualified lead definition:** lead has valid contact info + program/intake intent captured + consent logged; duplicates removed.
- **Attribution window:** count applications/offers/deposits/starts that occur within a consistent window post-event (e.g., 60–120 days), using CRM source/UTM tagging where possible.
- **Shared attribution:** if multiple channels touch the same lead, document the rule (e.g., “last touch within 14 days”, “first touch”, or “split credit”) in `notes`.
