---
name: romania-education-system-and-calendar
description: Document Romania’s education system and yearly school/exam calendar in a recruiting-usable way (windows, blackout dates, credential/grading context). Use for Romania-specific scheduling of school visits, fairs, webinars, paid campaigns, deadlines, and for interpreting Romanian secondary credentials (incl. Bacalaureat, Evaluarea Nationala, IB, Cambridge overlaps).
metadata:
  owner: evobuilder
  version: "1.1"
  scope: romania
---

# Romania education system and calendar

## Use the global workflow

Follow the end-to-end process in the global skill: `/skills/education-system-and-calendar/SKILL.md`.  
This Romania file only adds **country-specific sources, path defaults, and data conventions.**

---

## Recommended output locations (if the ticket allows)

- `/countries/romania/market/education-system.md`
- `/countries/romania/market/education-calendar.md`
- `/countries/romania/data/calendar/romania-academic-calendar.csv`

Use these unless the ticket or existing repo structure requires different paths.

---

## Romania source checklist

- **Ministry of Education** (official school year structures, module calendars, holiday orders).
- **Bacalaureat** and **Evaluarea Națională** schedules and results releases from ministry communiqués.
- **Public holidays** from government decisions (note long weekends/bridge days).
- **Inspectorate/school circulars** if modules or breaks differ locally; record the county in `notes`.
- **IB/Cambridge** timetables where Romanian schools offer those programs.

Capture `source_url`, publisher, and `last_verified` for every event.

---

## Data conventions (Romania)

- Use `event_name_ro` when Romanian titles exist; otherwise keep `event_name_en`.
- Keep stable `event_id` patterns such as `bacalaureat-session-1`, `bacalaureat-session-2`, `evaluare-nationala`, `module-1`, `module-2`, `winter-break`, `spring-break`.
- Mark `impact_on_recruiting` as `blackout` for Bacalaureat/Evaluarea Națională prep and exam weeks.
- If dates are county-specific, capture the county in `notes` and avoid mixing multiple counties in one row.

---

## Operational reminders

- **Blackouts:** Bacalaureat and Evaluarea Națională exam weeks plus immediate prep periods constrain school access.
- **Visit windows:** early modules and post-results periods are best for school visits and counselor meetings; align messaging to exam outcomes.
- **Updates:** refresh CSV/Markdown when ministry orders adjust module dates or exam calendars; keep a short update log in the Markdown outputs.

---

## Common pitfalls

- Mixing Romania-specific dates with generic EU timelines.
- Copying last year’s exam dates without verifying changes.
- Writing long narratives but failing to produce a structured dataset.
- Using unofficial blogs as the source of truth when primary sources exist.
- Inventing Romanian translations or abbreviations.

---

## “Done” checklist

- [ ] CSV exists/updated and passes basic sanity checks (ISO dates, ranges valid, sources present)
- [ ] Calendar note includes clear blackout windows + best windows
- [ ] Education system note covers: structure, school types, credentials, grading, exam relevance
- [ ] All outputs are within ticket-approved write paths
- [ ] Each artifact has an update/verification stamp
