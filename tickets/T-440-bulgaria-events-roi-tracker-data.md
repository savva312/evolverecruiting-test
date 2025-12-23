# T-440: Bulgaria — add events ROI tracker dataset (cost → starts)

Status: done
Type: data
Priority: P2
Dependencies: T-420 (recommended)
Claimed-by: evoticketresolver_nkc5drr6
Claimed-at: 2025-12-22T17:53:34Z
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Add a structured ROI tracker so the Bulgaria team can evaluate fairs/events consistently (cost per qualified lead, cost per start) and make repeat/skip decisions each season.

---

## Context

- Event content exists in:
  - `countries/bulgaria/entities/fairs-events/calendar-2025-2026.md`
  - `countries/bulgaria/entities/fairs-events/profiles/*.md`
- A structured `fairs-events.csv` is planned (T-420). This ROI table can reference `event_id` once available.

---

## Allowed write paths

- `tickets/T-440-bulgaria-events-roi-tracker-data.md`
- `countries/bulgaria/data/operations/event-roi.csv`
- `countries/bulgaria/data/operations/event-roi-dictionary.md`

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

- `countries/bulgaria/data/operations/event-roi.csv` created with headers and (optionally) one example row.
- `countries/bulgaria/data/operations/event-roi-dictionary.md` created defining fields (event_id, season, cost, leads, apps, offers, deposits, starts) and calculation notes.

---

## Acceptance criteria

- [x] Dictionary defines required fields and explicitly distinguishes “leads scanned” vs “qualified leads”.
- [x] No files outside `Allowed write paths` were modified.

## What changed

- What changed (2025-12-22): Added `countries/bulgaria/data/operations/event-roi.csv` and `countries/bulgaria/data/operations/event-roi-dictionary.md` to standardize fair/event ROI tracking (cost → qualified leads → starts).
