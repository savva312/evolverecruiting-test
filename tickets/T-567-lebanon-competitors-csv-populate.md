# T-567: Lebanon — populate `competitors.csv` (sync with competitor profiles)

Status: open
Type: data
Priority: P2
Dependencies: T-462, T-463, T-464 (recommended)
Claimed-by:
Claimed-at:
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Populate `countries/lebanon/data/entities/competitors.csv` with one row per competitor profile currently present under `countries/lebanon/entities/competitors/profiles/`.

This converts competitor notes into a dataset that can be filtered by home country and target programs.

---

## Context

- Competitor profiles: `countries/lebanon/entities/competitors/profiles/*.md`
- Empty dataset: `countries/lebanon/data/entities/competitors.csv`
- Dictionary: `countries/lebanon/data/entities/competitors-dictionary.md`

---

## Allowed write paths

- `tickets/T-465-lebanon-competitors-csv-populate.md`
- `countries/lebanon/data/entities/competitors.csv`
- `countries/lebanon/data/entities/competitors-dictionary.md` (only if minor clarifications are needed)

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

- `countries/lebanon/data/entities/competitors.csv` populated with **≥5 rows** (or the number of competitor profiles, whichever is higher).

---

## Acceptance criteria

- [ ] Every row has `competitor_id`, `name`, `home_country`, and `as_of`.
- [ ] `home_country` uses ISO 3166-1 alpha-2 codes (e.g., `LB`, `US`).
- [ ] `target_programs` uses semicolon-separated tags (e.g., `medicine;business;cs_data_ai`) aligned to Lebanon program cluster naming where possible.
- [ ] No files outside `Allowed write paths` were modified.

