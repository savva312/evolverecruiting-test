---
name: lebanon-education-system-and-calendar
description: Document Lebanon’s education system and yearly school/exam calendar in a recruiting-usable way (windows, blackout dates, credential/grading context). Use for Lebanon-specific scheduling of school visits, fairs, webinars, paid campaigns, deadlines, and for interpreting Lebanese secondary credentials (e.g., Brevet, Lebanese Baccalaureate, IB, Cambridge overlaps).
metadata:
  owner: evobuilder
  version: "1.1"
  scope: lebanon
---

# Lebanon education system and calendar

## Use the global workflow

Follow the end-to-end process in the global skill: `/skills/education-system-and-calendar/SKILL.md`.  
This Lebanon file only adds **country-specific sources, path defaults, and data conventions.**

---

## Recommended output locations (if the ticket allows)

- `/countries/lebanon/market/education-system.md`
- `/countries/lebanon/market/education-calendar.md`
- `/countries/lebanon/data/calendar/lebanon-academic-calendar.csv`

Use these unless the ticket or existing repo structure requires different paths.

---

## Lebanon source checklist

- **Ministry of Education and Higher Education** for official calendars and exam announcements.
- **Brevet and Lebanese Baccalaureate** exam schedules and results releases from official communiqués.
- **Public holiday decrees** (Council of Ministers) including religious holidays that create long breaks.
- **Regional/school circulars** if calendars vary; note the governorate or school network in `notes`.
- **IB/Cambridge** timetables for international schools operating those programs.

Record `source_url`, publisher, and `last_verified` for every event.

---

## Data conventions (Lebanon)

- Use `event_name_ar` when Arabic titles are available; otherwise keep `event_name_en`.
- Keep stable `event_id` patterns such as `brevet-exams`, `baccalaureate-exams`, `first-term`, `second-term`, `eid-al-fitr`, `eid-al-adha`, `winter-break`.
- Mark `impact_on_recruiting` as `blackout` for Brevet/Baccalaureate exam prep and religious holiday breaks.
- If dates differ by region or school network, capture that in `notes` and avoid mixing multiple regions in one row.

---

## Operational reminders

- **Blackouts:** Brevet/Baccalaureate exam periods and Eid breaks restrict access; shift to light-touch nurture.
- **Visit windows:** early term weeks and post-results periods are best for counselor meetings and conversion pushes.
- **Messaging:** reference credential names exactly (e.g., “البكالوريا اللبنانية”) and clarify language-of-instruction norms in the system note.
- **Updates:** refresh CSV/Markdown when ministry circulars shift dates; keep a brief update log in the Markdown outputs.

---

## Common pitfalls

- Mixing Lebanon-specific dates with generic EU timelines.
- Copying last year’s exam dates without verifying changes.
- Writing long narratives but failing to produce a structured dataset.
- Using unofficial blogs as the source of truth when primary sources exist.
- Inventing Lebanese translations or abbreviations.

---

## “Done” checklist

- [ ] CSV exists/updated and passes basic sanity checks (ISO dates, ranges valid, sources present)
- [ ] Calendar note includes clear blackout windows + best windows
- [ ] Education system note covers: structure, school types, credentials, grading, exam relevance
- [ ] All outputs are within ticket-approved write paths
- [ ] Each artifact has an update/verification stamp
