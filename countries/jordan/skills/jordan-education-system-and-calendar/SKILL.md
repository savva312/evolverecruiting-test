---
name: jordan-education-system-and-calendar
description: Document Jordan’s education system and yearly school/exam calendar in a recruiting-usable way (windows, blackout dates, credential/grading context). Use for Jordan-specific scheduling of school visits, fairs, webinars, paid campaigns, deadlines, and for interpreting Jordanian secondary credentials (incl. DZI/NVO, IB, Cambridge overlaps).
metadata:
  owner: evobuilder
  version: "1.1"
  scope: jordan
---

# Jordan education system and calendar

## Use the global workflow

Follow the end-to-end process in the global skill: `/skills/education-system-and-calendar/SKILL.md`.  
This Jordan file only adds **country-specific source lists, path defaults, and data conventions.**

---

## Recommended output locations (if the ticket allows)

- `/countries/jordan/market/education-system.md`
- `/countries/jordan/market/education-calendar.md`
- `/countries/jordan/data/calendar/jordan-academic-calendar.csv`

Use these unless the ticket or existing repo structure requires different paths.

---

## Jordan source checklist

- **Ministry of Education (وزارة التربية والتعليم)** for official school calendars and term/break schedules.
- **Tawjihi (General Secondary) exam timetables** from ministry bulletins and result release notices.
- **Public holiday decrees** (e.g., Eid al-Fitr/Adha, Independence Day, Christmas/New Year as applicable).
- **Regional directorates or school circulars** if term calendars differ locally; note the governorate in `notes`.
- **IB/Cambridge** timetables where international schools operate those curricula.

Capture `source_url`, publisher, and `last_verified` for every event.

---

## Data conventions (Jordan)

- Use `event_name_ar` when Arabic titles exist; otherwise keep `event_name_en`.
- Keep stable `event_id` patterns such as `tawjihi-winter`, `tawjihi-summer`, `first-term`, `second-term`, `eid-al-fitr`, `eid-al-adha`, `winter-break`.
- Mark `impact_on_recruiting` as `blackout` for Tawjihi prep/exam weeks and Eid breaks; schools typically restrict access.
- If dates are provisional pending Gazette confirmation, flag the uncertainty in `notes` and refresh when confirmed.

---

## Operational reminders

- **Blackouts:** Tawjihi prep/exams (winter and summer sessions) and Eid periods limit outreach and visits.
- **Best windows:** early term weeks after resumption and post-results periods (when counselors engage on next steps).
- **Messaging:** use official terminology (e.g., “التوجيهي”) and note grading/stream distinctions in the education system note.
- **Updates:** refresh CSV/Markdown when ministry bulletins shift dates; keep a brief update log in the Markdown outputs.

---

## Common pitfalls

- Mixing Jordan-specific dates with generic EU timelines.
- Copying last year’s exam dates without verifying changes.
- Writing long narratives but failing to produce a structured dataset.
- Using unofficial blogs as the source of truth when primary sources exist.
- Inventing Jordanian translations or abbreviations.

---

## “Done” checklist

- [ ] CSV exists/updated and passes basic sanity checks (ISO dates, ranges valid, sources present)
- [ ] Calendar note includes clear blackout windows + best windows
- [ ] Education system note covers: structure, school types, credentials, grading, exam relevance
- [ ] All outputs are within ticket-approved write paths
- [ ] Each artifact has an update/verification stamp
