# T-451: Serbia — Populate `fairs-events.csv` from existing event profiles

Status: done
Type: data
Priority: P1
Dependencies: (none)
Claimed-by: codex-gpt5
Claimed-at: 2025-12-22
Completed-at: 2025-12-22
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Turn the Serbia fairs/events knowledge already in markdown into a structured dataset for planning, filtering, and ROI tracking.

---

## Context

- Existing inputs:
  - `countries/serbia/entities/fairs-events/calendar-2025-2026.md` (needs refresh in a separate ticket)
  - `countries/serbia/entities/fairs-events/profiles/*.md`
- Target structured output:
  - `countries/serbia/data/entities/fairs-events.csv`
  - Dictionary: `countries/serbia/data/entities/fairs-events-dictionary.md`

---

## Allowed write paths

- `countries/serbia/data/entities/fairs-events.csv`
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

- `countries/serbia/data/entities/fairs-events.csv`

---

## Acceptance criteria

- [ ] Adds rows for the current priority events (at minimum): World Education Fair (Integral), Education Beyond Borders (Belgrade), EducationUSA/Fulbright (Belgrade), and key virtual/counselor events if recurring.
- [ ] Dates are populated for the next upcoming cycle (2026 dates where available); if exact dates are not published, leave blank and add a clear “verify by” note in `notes` (do not invent).
- [ ] `country` uses ISO `RS` and `format` uses only `in-person|virtual|hybrid`.
- [ ] No edits outside allowed write paths.

## Completion notes
- Populated `countries/serbia/data/entities/fairs-events.csv` with six 2026-focused rows covering Integral World Education Fair tour, Education Beyond Borders, EducationUSA/Fulbright Belgrade, Integral Virtual Fair, Unify Roadshow, and Balkan/CEE counselor forums.
- Included “verify by” guidance plus budgeting/positioning context in `notes` while using `RS` country codes and allowed format values.
