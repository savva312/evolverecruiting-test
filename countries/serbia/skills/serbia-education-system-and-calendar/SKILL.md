---
name: serbia-education-system-and-calendar
description: Document Serbia’s education system and yearly school/exam calendar in a recruiting-usable way (windows, blackout dates, credential/grading context). Use for Serbia-specific scheduling of school visits, fairs, webinars, paid campaigns, deadlines, and for interpreting Serbian secondary credentials (incl. DZI/NVO, IB, Cambridge overlaps).
metadata:
  owner: evobuilder
  version: "1.1"
  scope: serbia
---

# Serbia education system and calendar

## Use the global workflow

Follow the end-to-end process in the global skill: `/skills/education-system-and-calendar/SKILL.md`.  
This Serbia file only adds **country-specific sources, path defaults, and data conventions.**

---

## Recommended output locations (if the ticket allows)

- `/countries/serbia/market/education-system.md`
- `/countries/serbia/market/education-calendar.md`
- `/countries/serbia/data/calendar/serbia-academic-calendar.csv`

Use these unless the ticket or existing repo structure requires different paths.

---

## Serbia source checklist

- **Ministry of Education** official school-year calendar and holiday schedules.
- **Matriculation / final exam timetables** (state matura pilot or legacy graduation exams) from ministry announcements.
- **Entrance exam schedules** for specialized high schools if relevant to feeder targeting.
- **Public holidays** from government decrees (note Orthodox calendar shifts).
- **Regional/school circulars** if calendars differ by municipality; capture the region in `notes`.
- **IB/Cambridge** timetables where international schools operate those programs.

Record `source_url`, publisher, and `last_verified` for every event.

---

## Data conventions (Serbia)

- Use `event_name_sr` when Serbian titles are available; otherwise keep `event_name_en`.
- Keep stable `event_id` patterns such as `state-matura`, `graduation-exams`, `entrance-exams`, `winter-break`, `spring-break`, `orthodox-easter-break`, `first-term`.
- Mark `impact_on_recruiting` as `blackout` for graduation/state matura periods and Orthodox Easter break.
- If dates vary by municipality, capture the locality in `notes` and avoid mixing multiple regions in one row.

---

## Operational reminders

- **Blackouts:** graduation/state matura exam weeks and Orthodox Easter break significantly limit school access.
- **Visit windows:** early term weeks and post-exam periods are best for outreach; align messaging to exam outcomes and results release timing.
- **Updates:** refresh CSV/Markdown when ministry bulletins shift calendars or matura pilots; keep a brief update log in the Markdown outputs.

---

## Common pitfalls

- Mixing Serbia-specific dates with generic EU timelines.
- Copying last year’s exam dates without verifying changes.
- Writing long narratives but failing to produce a structured dataset.
- Using unofficial blogs as the source of truth when primary sources exist.
- Inventing Serbian translations or abbreviations.

---

## “Done” checklist

- [ ] CSV exists/updated and passes basic sanity checks (ISO dates, ranges valid, sources present)
- [ ] Calendar note includes clear blackout windows + best windows
- [ ] Education system note covers: structure, school types, credentials, grading, exam relevance
- [ ] All outputs are within ticket-approved write paths
- [ ] Each artifact has an update/verification stamp
