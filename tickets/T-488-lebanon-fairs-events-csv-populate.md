# T-488: Lebanon — populate `fairs-events.csv` (sync with existing calendar + profiles)

Status: done
Type: data
Priority: P1
Dependencies: (none)
Claimed-by: codex-gpt5
Claimed-at: 2025-12-23T13:15:00Z
Last-updated: 2025-12-23
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Populate `countries/lebanon/data/entities/fairs-events.csv` with structured rows for the events already documented in:
- `countries/lebanon/entities/fairs-events/calendar-2025-2026.md`
- `countries/lebanon/entities/fairs-events/profiles/*.md`

This turns the fairs/events work into an ops-ready dataset (filterable by season, city, format, and audience).

---

## Context

- Calendar: `countries/lebanon/entities/fairs-events/calendar-2025-2026.md`
- Profiles: `countries/lebanon/entities/fairs-events/profiles/README.md`
- Empty CSV: `countries/lebanon/data/entities/fairs-events.csv`
- Dictionary: `countries/lebanon/data/entities/fairs-events-dictionary.md`

---

## Allowed write paths

- `tickets/T-446-lebanon-fairs-events-csv-populate.md`
- `countries/lebanon/data/entities/fairs-events.csv`
- `countries/lebanon/data/entities/fairs-events-dictionary.md` (only if minor clarifications are needed)

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

- `countries/lebanon/data/entities/fairs-events.csv` populated with **≥12 rows** (or the number of events documented, whichever is higher).

---

## Acceptance criteria

- [x] Every row has `event_id`, `name`, `city`, `country`, `start_date` (or best-known approximation), `format`, and `as_of`.
- [x] Dates use ISO 8601 (`YYYY-MM-DD`) and unknown dates are left blank (not `TBD`).
- [x] `event_id` is stable, lowercase ASCII, and unique.
- [x] No files outside `Allowed write paths` were modified.

---

## Execution notes

- What changed (short): Populated `countries/lebanon/data/entities/fairs-events.csv` with 17 Lebanon events covering EducationUSA, Campus France, Access Masters/MBA, Education Beyond Borders (spring/fall), CedarEdu and Orient MENA roadshow city stops, BMI/CIS virtual fairs, and counselor forums, aligning dates/formats to the 2025–2026 calendar and linking each row back to the relevant profile in the notes.
