# T-538: Nigeria — Fairs/events: CSV build + calendar refresh (2025–2026)

Status: open
Type: data
Priority: P1
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

Operationalize Nigeria events planning by (1) populating `fairs-events.csv` and (2) refreshing the narrative calendar with confirmed/updated dates and participation guidance.

---

## Context

- Narrative calendar exists: `countries/nigeria/entities/fairs-events/calendar-2025-2026.md` (last updated 2025-03-09; partially estimate-based)
- Structured dataset is header-only: `countries/nigeria/data/entities/fairs-events.csv`
- Schema: `countries/nigeria/data/entities/fairs-events-dictionary.md`

---

## Allowed write paths

- `countries/nigeria/data/entities/fairs-events.csv`
- `countries/nigeria/entities/fairs-events/calendar-2025-2026.md`
- `executions/T-458-nigeria-fairs-events-csv-and-calendar-refresh/**` (optional notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket for status updates)
- `countries/**` (except `countries/nigeria/**`)

---

## Required outputs

- `countries/nigeria/data/entities/fairs-events.csv` with **≥ 12 rows** covering the highest-ROI Nigeria fairs/events
- `countries/nigeria/entities/fairs-events/calendar-2025-2026.md` updated with:
  - `Last updated:` date refreshed
  - any confirmed dates/packages added (with sources or “unconfirmed” labels)

---

## Acceptance criteria

- [ ] `fairs-events.csv` includes required fields and valid `event_id` + `as_of` for every row
- [ ] Calendar page clearly labels which dates are confirmed vs estimated, with links to organizers
- [ ] No PII is added; organizer contacts should be role-based or omitted

