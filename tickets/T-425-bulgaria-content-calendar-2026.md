# T-425: Bulgaria — build `content-calendar.csv` (12-month plan aligned to BG calendar)

Status: done
Type: data
Priority: P1
Dependencies: (none)
Claimed-by: evoticketresolver_oh0bya6j
Claimed-at: 2025-12-22T17:50:52Z
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Populate `countries/bulgaria/data/operations/content-calendar.csv` with a 12-month Bulgaria content plan aligned to:
- Bulgarian exam/holiday rhythms (Matura, school breaks)
- intake conversion windows (pre-May, post-results June/July)
- campus split (Athens vs Nicosia) and hero program clusters

---

## Context

- Calendar constraints: `countries/bulgaria/market/exams-and-calendar.md`
- Digital channel guidance: `countries/bulgaria/go-to-market/digital-playbook/channel-strategy.md`
- Empty file: `countries/bulgaria/data/operations/content-calendar.csv`
- Dictionary: `countries/bulgaria/data/operations/content-calendar-dictionary.md`

---

## Allowed write paths

- `tickets/T-425-bulgaria-content-calendar-2026.md`
- `countries/bulgaria/data/operations/content-calendar.csv`
- `countries/bulgaria/data/operations/content-calendar-dictionary.md` (only if minor clarifications are needed)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- `countries/**` (except `countries/bulgaria/**`)

---

## Required outputs

- `countries/bulgaria/data/operations/content-calendar.csv` populated with **≥24 rows** (at least 2 per month) for `2026-01` through `2026-12`.

---

## Acceptance criteria

- [ ] Every row has `month`, `theme`, `primary_channel`, `asset_type`, `owner`, `status`, and `as_of`.
- [ ] Matura-heavy periods (late May–mid June) use lighter-touch content themes (reassurance, checklists) vs hard conversion pushes.
- [ ] No files outside `Allowed write paths` were modified.

---

## What changed

- Populated `countries/bulgaria/data/operations/content-calendar.csv` with a 2026 (Jan–Dec) plan of 36 rows aligned to the Bulgaria school/exam cycle, with explicit Athens vs Nicosia and hero program-cluster coverage.
