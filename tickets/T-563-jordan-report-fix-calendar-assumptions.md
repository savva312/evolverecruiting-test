# T-563: Jordan report — correct calendar/exam/travel assumptions and remove Bulgaria artifacts

Status: open
Type: qa
Priority: P0
Dependencies: (none)
Claimed-by:
Claimed-at:
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Correct the Jordan recruitment plan report where it contains non-Jordan calendar/exam/travel assumptions (e.g., “Matura”, “Sofia”) by:
- Replacing with Jordan-correct exam terminology and windows (Tawjihi + IB/A-Level).
- Removing Bulgaria-only travel framing (e.g., “Sofia to Athens”).
- Linking the report’s timing guidance to the Jordan calendar doc in this repo.

---

## Context

Report needing cleanup:
- `countries/jordan/reports/2025-12-20 - UNIC Athens Jordan Recruitment Plan.md`

Jordan calendar anchor:
- `countries/jordan/market/exams-and-calendar.md`

---

## Allowed write paths

- `tickets/T-464-jordan-report-fix-calendar-assumptions.md`
- `countries/jordan/reports/2025-12-20 - UNIC Athens Jordan Recruitment Plan.md`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**` (global)
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- `countries/**` (except `countries/jordan/**`)

---

## Required outputs

- `countries/jordan/reports/2025-12-20 - UNIC Athens Jordan Recruitment Plan.md` updated to remove Bulgaria artifacts and correct Jordan exam/calendar references.

---

## Acceptance criteria

- [ ] The report contains **no** references to Bulgaria exam terms/cities (at minimum: “Matura”, “Sofia”, “Plovdiv”, “Varna”).
- [ ] Timing guidance aligns with `countries/jordan/market/exams-and-calendar.md` (links included).
- [ ] Any specific travel-time claims are either sourced or rephrased conservatively (avoid invented numbers).

