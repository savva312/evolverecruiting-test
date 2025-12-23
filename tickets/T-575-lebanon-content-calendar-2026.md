# T-575: Lebanon — build `content-calendar.csv` (12-month plan aligned to Lebanon calendar)

Status: open
Type: data
Priority: P2
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

Populate `countries/lebanon/data/operations/content-calendar.csv` with a 12-month Lebanon content plan aligned to:
- Lebanon exam/holiday rhythms (Lebanese Bac, IB, French Bac)
- intake conversion windows (post-results July/August)
- campus split (Athens vs Nicosia) and hero program clusters

---

## Context

- Calendar constraints: `countries/lebanon/market/exams-and-calendar.md`
- Digital channel guidance: `countries/lebanon/go-to-market/digital-playbook/channel-strategy.md`
- Empty file: `countries/lebanon/data/operations/content-calendar.csv`
- Dictionary: `countries/lebanon/data/operations/content-calendar-dictionary.md`

---

## Allowed write paths

- `tickets/T-467-lebanon-content-calendar-2026.md`
- `countries/lebanon/data/operations/content-calendar.csv`
- `countries/lebanon/data/operations/content-calendar-dictionary.md` (only if minor clarifications are needed)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- `countries/**` (except `countries/lebanon/**`)

---

## Required outputs

- `countries/lebanon/data/operations/content-calendar.csv` populated with **≥24 rows** (at least 2 per month) for `2026-01` through `2026-12`.

---

## Acceptance criteria

- [ ] Every row has `month`, `theme`, `primary_channel`, `asset_type`, `owner`, `status`, and `as_of`.
- [ ] Lebanon Bac-heavy windows (late Jun–mid Jul) use lighter-touch content themes (reassurance, checklists) vs hard conversion pushes.
- [ ] No files outside `Allowed write paths` were modified.

