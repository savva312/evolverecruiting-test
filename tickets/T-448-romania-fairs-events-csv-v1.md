# T-448: Romania — populate `countries/romania/data/entities/fairs-events.csv` (v1) + dictionary

Status: done
Type: data
Priority: P1
Dependencies: T-148
Claimed-by: codex-gpt5
Claimed-at: 2025-12-22
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Populate `countries/romania/data/entities/fairs-events.csv` so the team can:
- filter the Romania event calendar by priority, city, and audience
- track planning status (targeted/booked/attended) in a structured way
- link events to their narrative profiles

Also update `countries/romania/data/entities/fairs-events-dictionary.md` to match the schema.

---

## Context

Existing in-repo inputs:
- Calendar: `countries/romania/entities/fairs-events/calendar-2025-2026.md`
- Profiles: `countries/romania/entities/fairs-events/profiles/*.md`
- CSV scaffold: `countries/romania/data/entities/fairs-events.csv`
- Dictionary scaffold: `countries/romania/data/entities/fairs-events-dictionary.md`

Keep this dataset **time-bounded** and practical: include the core “must-do / consider / monitor” set with dates when known and timing patterns otherwise.

---

## Allowed write paths

- `tickets/T-448-romania-fairs-events-csv-v1.md`
- `countries/romania/data/entities/fairs-events.csv`
- `countries/romania/data/entities/fairs-events-dictionary.md`
- `executions/**` (optional for notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `.github/**`
- `scripts/**`
- `tickets/**` (except this ticket file)
- `countries/**` (except `countries/romania/data/**`)

---

## Required outputs

- Updated `countries/romania/data/entities/fairs-events.csv` (minimum: events already documented under `entities/fairs-events/`)
- Updated `countries/romania/data/entities/fairs-events-dictionary.md`

---

## Acceptance criteria

- [x] Every documented event profile in `countries/romania/entities/fairs-events/profiles/` has a corresponding CSV row with a stable `event_id` and working `profile_path`.
- [x] The CSV includes priority and planning status fields (define exact names in dictionary).
- [x] Dictionary matches the dataset exactly.
- [x] No edits outside allowed paths.

## What changed

- Added a Romania fairs/events schema (priority, planning status, cadence, lead goals, profile links) and populated the data dictionary.
- Filled `countries/romania/data/entities/fairs-events.csv` with seven priority/consider/monitor events covering every existing narrative profile plus organizer, cadence, cost, lead goal, and planning status metadata.
