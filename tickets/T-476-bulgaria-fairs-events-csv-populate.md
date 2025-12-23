# T-476: Bulgaria — populate `fairs-events.csv` (sync with calendar + profiles)

Status: done
Type: data
Priority: P1
Dependencies: (none)
Claimed-by: evoticketresolver_re6xre1e
Claimed-at: 2025-12-22T20:38:27Z
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Make the Bulgaria fairs/events work operational by converting the existing narrative calendar and event profiles into a structured dataset in `countries/bulgaria/data/entities/fairs-events.csv`.

---

## Context

Existing Bulgaria event materials:
- Calendar: `countries/bulgaria/entities/fairs-events/calendar-2025-2026.md`
- Profiles: `countries/bulgaria/entities/fairs-events/profiles/*.md`

Structured dataset exists but is empty:
- `countries/bulgaria/data/entities/fairs-events.csv`
- `countries/bulgaria/data/entities/fairs-events-dictionary.md`

Important constraint: many events are described in **month windows** (e.g., “Mar/Apr”) rather than confirmed dates. The CSV should not invent dates; use blank dates + clear notes when not confirmed.

---

## Allowed write paths

- `tickets/T-476-bulgaria-fairs-events-csv-populate.md`
- `countries/bulgaria/data/entities/fairs-events.csv`
- `countries/bulgaria/data/entities/fairs-events-dictionary.md`
- `countries/bulgaria/entities/fairs-events/README.md`

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

- `countries/bulgaria/data/entities/fairs-events.csv` populated with **≥10 rows** covering the “Must-do” + key “Consider” events in the calendar.
- `countries/bulgaria/entities/fairs-events/README.md` updated to reference the CSV + dictionary as the structured companion to the calendar/profiles.
- If needed: `countries/bulgaria/data/entities/fairs-events-dictionary.md` updated to explicitly allow `start_date`/`end_date` blanks when dates are unconfirmed, requiring the date window be captured in `notes`.

---

## Acceptance criteria

- [x] CSV has ≥10 data rows and every row includes `event_id`, `name`, `city`, `country=BG`, `organizer`, `format`, and `as_of`.
- [x] No event dates are invented: if exact dates are unknown, `start_date`/`end_date` are blank and `notes` includes the timing window (e.g., `timing: Mar/Apr (typical)`).
- [x] No files outside `Allowed write paths` were modified.

## Execution notes

- Populated `countries/bulgaria/data/entities/fairs-events.csv` from the 2025–2026 calendar + profiles with 14 operational rows (multi-city tours broken out by stop).
- Updated `countries/bulgaria/data/entities/fairs-events-dictionary.md` to allow blank `start_date`/`end_date` when dates are unconfirmed (timing captured in `notes`).
- Updated `countries/bulgaria/entities/fairs-events/README.md` to reference the CSV + dictionary as the structured companion to the narrative calendar/profiles.
