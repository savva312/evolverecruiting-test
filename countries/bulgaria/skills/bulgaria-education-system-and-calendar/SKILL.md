---
name: bulgaria-education-system-and-calendar
description: Document Bulgaria’s education system and yearly school/exam calendar in a recruiting-usable way (windows, blackout dates, credential/grading context). Use for Bulgaria-specific scheduling of school visits, fairs, webinars, paid campaigns, deadlines, and for interpreting Bulgarian secondary credentials (incl. DZI/NVO, IB, Cambridge overlaps).
metadata:
  owner: evobuilder
  version: "1.1"
  scope: bulgaria
---

# Bulgaria education system and calendar

## Use the global workflow

Follow the end-to-end process in the global skill: `/skills/education-system-and-calendar/SKILL.md`.  
This Bulgaria file only adds **country-specific source lists, path conventions, and data nuances.**

---

## Country-specific scope

- Keep the focus on **Bulgaria** (no generic EU practices).
- Apply the global steps to the **current + next academic years** unless the ticket narrows the horizon.

---

## Recommended output locations (if the ticket allows)

- `/countries/bulgaria/market/education-system.md`
- `/countries/bulgaria/market/exams-and-calendar.md`
- Optional structured rows (only if a ticket explicitly allows adding/updating data): `countries/bulgaria/data/operations/`

Use the global defaults unless the ticket or existing repo structure requires an alternate path.

---

## Bulgaria source checklist

- **Ministry of Education and Science** (school year calendar, official breaks).
- **Regional education directorates** when calendars differ locally (note the region in `notes`).
- **State Matura (DZI) and NVO exam schedules** from official communiqués.
- **Official public holiday decrees** (Council of Ministers) for long weekends/bridges.
- **IB/Cambridge** official timetables if Bulgarian feeders use those curricula.

Record `source_url`, publisher, and `last_verified` for every event.

---

## Data conventions (Bulgaria)

- Include `event_name_bg` in addition to `event_name_en` when sources provide Bulgarian names (copy exact casing; do not translate).
- Keep stable `event_id` patterns such as `dzi-may-exams`, `nvo-grade-7`, `winter-break`, `spring-break`.
- Mark `impact_on_recruiting` as `blackout` for DZI/NVO prep and exam weeks; most schools restrict access.
- Note whether dates are **national** or **region-specific** in `notes`.

---

## Operational reminders

- **Visit planning:** best windows are typically after the start-of-year settling period and post-DZI (late May–June), but validate against the current calendar.
- **Messaging:** reference Bulgarian credential terms (e.g., “Държавни зрелостни изпити”, “ДЗИ”) rather than generic “national exam.”
- **Updates:** when dates shift mid-year, append a short update log to the Markdown outputs and refresh `last_verified` in the CSV.
