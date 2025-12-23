---
name: nigeria-education-system-and-calendar
description: Document Nigeria’s education system and yearly school/exam calendar in a recruiting-usable way (windows, blackout dates, credential/grading context). Use for Nigeria-specific scheduling of school visits, fairs, webinars, paid campaigns, deadlines, and for interpreting Nigerian secondary credentials (incl. Bacalaureat, Evaluarea Nationala, IB, Cambridge overlaps).
metadata:
  owner: evobuilder
  version: "1.1"
  scope: nigeria
---

# Nigeria education system and calendar

## Use the global workflow

Follow the end-to-end process in the global skill: `/skills/education-system-and-calendar/SKILL.md`.  
This Nigeria file only adds **country-specific sources, path defaults, and data conventions.**

---

## Recommended output locations (if the ticket allows)

- `/countries/nigeria/market/education-system.md`
- `/countries/nigeria/market/education-calendar.md`
- `/countries/nigeria/data/calendar/nigeria-academic-calendar.csv`

Use these unless the ticket or existing repo structure requires different paths.

---

## Nigeria source checklist

- **Federal Ministry of Education** (term dates, policy circulars).
- **State education boards** when term calendars differ by state; note the state in `notes`.
- **WAEC** and **NECO** exam timetables (May/June & Nov/Dec for WAEC; SSCE/BECE for NECO).
- **JAMB/UTME** schedule and results windows (critical for application timing).
- **Public holidays** from the Federal Government (add bridges/long weekends when official).
- **IB/Cambridge** timetables for international schools using those curricula.

Record `source_url`, publisher, and `last_verified` for every event.

---

## Data conventions (Nigeria)

- Keep `event_id` patterns stable: `waec-may-june`, `waec-nov-dec`, `neco-ssce`, `neco-bece`, `utme`, `first-term`, `easter-break`, `eid-al-fitr`, etc.
- Use `event_name_local` only when sources provide a non-English label (most will be English); otherwise leave it blank.
- Mark `impact_on_recruiting` as `blackout` for WAEC/NECO exam prep weeks and UTME exam days; many schools restrict access.
- If calendars are state-specific, capture the state in `notes` and avoid mixing multiple states in a single row.

---

## Operational reminders

- **Blackout risk:** WAEC/NECO exam windows and UTME are high-stress periods; prioritize nurture over visits.
- **Visit windows:** early term weeks after resumption and post-exam periods (after WAEC/NECO results) are strongest for conversion.
- **Messaging:** reference credential names accurately (WAEC SSCE, NECO SSCE/BECE, UTME score release) and align campaign pushes to results windows.
- **Updates:** refresh CSV/Markdown when WAEC/NECO/JAMB issue revised timetables; keep a short update log in the Markdown outputs.

---

## Common pitfalls

- Mixing Nigeria-specific dates with generic EU timelines.
- Copying last year’s exam dates without verifying changes.
- Writing long narratives but failing to produce a structured dataset.
- Using unofficial blogs as the source of truth when primary sources exist.
- Inventing Nigerian translations or abbreviations.

---

## “Done” checklist

- [ ] CSV exists/updated and passes basic sanity checks (ISO dates, ranges valid, sources present)
- [ ] Calendar note includes clear blackout windows + best windows
- [ ] Education system note covers: structure, school types, credentials, grading, exam relevance
- [ ] All outputs are within ticket-approved write paths
- [ ] Each artifact has an update/verification stamp
