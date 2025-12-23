# T-496: Lebanon — add events ROI tracker dataset (cost → starts)

Status: done
Type: data
Priority: P2
Dependencies: T-446 (recommended)
Claimed-by: evoticketresolver_8onefiye
Claimed-at: 2025-12-22T20:43:23Z
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Add a structured ROI tracker so the Lebanon team can evaluate fairs/events consistently (cost per qualified lead, cost per start) and make repeat/skip decisions each season.

---

## Context

- Event content exists in:
  - `countries/lebanon/entities/fairs-events/calendar-2025-2026.md`
  - `countries/lebanon/entities/fairs-events/profiles/*.md`
- `countries/lebanon/data/entities/fairs-events.csv` should be populated first (T-446) so this ROI table can reference `event_id`.

---

## Allowed write paths

- `tickets/T-496-lebanon-events-roi-tracker-data.md`
- `countries/lebanon/data/operations/event-roi.csv`
- `countries/lebanon/data/operations/event-roi-dictionary.md`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**` (global)
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- `countries/**` (except `countries/lebanon/**`)

---

## Required outputs

- `countries/lebanon/data/operations/event-roi.csv` created with headers and (optionally) one example row.
- `countries/lebanon/data/operations/event-roi-dictionary.md` created defining fields (event_id, season, cost, leads, apps, offers, deposits, starts) and calculation notes.

---

## Acceptance criteria

- [x] Dictionary defines required fields and explicitly distinguishes “leads scanned” vs “qualified leads”.
- [x] No files outside `Allowed write paths` were modified.

## What changed

- What changed (2025-12-22): Added `countries/lebanon/data/operations/event-roi.csv` and `countries/lebanon/data/operations/event-roi-dictionary.md` to standardize fair/event ROI tracking (cost → qualified leads → starts).
