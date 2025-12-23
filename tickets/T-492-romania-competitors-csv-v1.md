# T-492: Romania — populate `countries/romania/data/entities/competitors.csv` (v1) + dictionary

Status: on-deck
Type: data
Priority: P1
Dependencies: T-155
Claimed-by:
Claimed-at:
Last-updated: 2025-12-23
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Make `countries/romania/data/entities/competitors.csv` usable by:
- adding rows for the existing competitor profiles in `countries/romania/entities/competitors/profiles/`
- defining a Romania-relevant competitor schema (cluster tags, country/city, tuition range signals)
- updating `countries/romania/data/entities/competitors-dictionary.md` so it matches the final columns

---

## Context

Existing in-repo inputs:
- `countries/romania/entities/competitors/profiles/*.md`
- `countries/romania/entities/competitors/README.md`
- `countries/romania/data/entities/competitors.csv` (currently empty)
- `countries/romania/data/entities/competitors-dictionary.md` (schema scaffold)

This ticket is about the **entity index** (competitor institutions/providers). Program-level pricing belongs in `countries/romania/data/programs/competitor-programs.csv` (see T-450).

---

## Allowed write paths

- `tickets/T-447-romania-competitors-csv-v1.md`
- `countries/romania/data/entities/competitors.csv`
- `countries/romania/data/entities/competitors-dictionary.md`
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

- Updated `countries/romania/data/entities/competitors.csv` (minimum: rows matching existing competitor profiles)
- Updated `countries/romania/data/entities/competitors-dictionary.md`

---

## Acceptance criteria

- [ ] `countries/romania/data/entities/competitors.csv` contains rows for each existing competitor profile under `countries/romania/entities/competitors/profiles/`.
- [ ] Each row includes a stable `competitor_id` and a working `profile_path`.
- [ ] A `program_clusters` field (or equivalent) exists and is consistently populated.
- [ ] Dictionary matches the dataset exactly.
- [ ] No edits outside allowed paths.

