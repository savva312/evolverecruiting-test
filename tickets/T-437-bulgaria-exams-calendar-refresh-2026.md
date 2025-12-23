# T-437: Bulgaria — refresh exams & academic calendar with exact 2025–26/2026–27 dates

Status: done
Type: content
Priority: P1
Dependencies: (none)
Claimed-by: evoticketresolver_udheph4m
Claimed-at: 2025-12-22T17:51:48Z
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Upgrade `countries/bulgaria/market/exams-and-calendar.md` from “typical month windows” to a recruiter-grade calendar with:
- exact dates for the next available cycles (2025–26 and/or 2026–27), sourced from official MoES releases
- clear “do / don’t” outreach windows derived from those dates

---

## Context

Current doc is month-window based and explicitly notes variability:
- `countries/bulgaria/market/exams-and-calendar.md`

This is high-leverage for Bulgaria because outreach effectiveness collapses during Matura/NAT windows.

---

## Allowed write paths

- `tickets/T-437-bulgaria-exams-calendar-refresh-2026.md`
- `countries/bulgaria/market/exams-and-calendar.md`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**` (global)
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- `countries/**` (except `countries/bulgaria/**`)

---

## Required outputs

- `countries/bulgaria/market/exams-and-calendar.md` updated with:
  - exact exam dates (DZI/Matura; NEA Grade 7/10) where published
  - updated month-by-month table for the relevant cycle(s)
  - sources list with “checked on” dates
  - a short “Recruiting implications” section translating dates into outreach/noise windows

---

## Acceptance criteria

- [x] Every exact date in the doc is supported by an official source link and a verification date.
- [x] If exact dates are not published for a cycle, the doc clearly states “not yet published” instead of guessing.
- [x] No files outside `Allowed write paths` were modified.

---

## What changed

- Updated `countries/bulgaria/market/exams-and-calendar.md` to a recruiter-grade 2025–26 exam calendar with exact DZI + NVO dates, explicit outreach “do/don’t” windows, and source links + verification date.
