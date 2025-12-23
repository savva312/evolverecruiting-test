# T-513: Serbia — Refresh fairs/events calendar to cover 2026–2027 (planning-ready)

Status: open
Type: content
Priority: P1
Dependencies: (optional) T-451 (dataset can be built in parallel)
Claimed-by:
Claimed-at:
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Update Serbia’s fairs/events calendar so it is forward-looking from **Dec 2025** and operationally usable for planning the next 12–18 months (2026 cycle + early 2027).

---

## Context

- Primary file:
  - `countries/serbia/entities/fairs-events/calendar-2025-2026.md`
- Current issues:
  - Includes “Spring 2025” guidance that is now in the past (current date: 2025-12-22).
  - Some items look copied from other markets (organizer domains/labels) and need verification.
- Inputs to use:
  - `countries/serbia/entities/fairs-events/profiles/*.md`
  - Organizer official pages (primary sources)

---

## Allowed write paths

- `countries/serbia/entities/fairs-events/calendar-2025-2026.md`
- `executions/**` (optional; notes only)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket file for status updates)

---

## Required outputs

- `countries/serbia/entities/fairs-events/calendar-2025-2026.md`

---

## Acceptance criteria

- [ ] Rewrites the calendar so “next timing” is future-oriented (2026 dates where known; early 2027 placeholders allowed but must be clearly labeled).
- [ ] Each Must-do/Consider event includes:
  - [ ] booking lead time recommendation
  - [ ] expected lead capture method (badge scan vs QR form)
  - [ ] Serbia-specific staffing note (language, parent-heavy vs student-heavy)
- [ ] Removes or flags any copy/paste artifacts (e.g., non-Serbia organizer domains) unless verified.
- [ ] No edits outside allowed write paths.

