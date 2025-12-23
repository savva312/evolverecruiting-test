# T-455: Serbia — Align `ngos-sgos.csv` to its data dictionary (schema + IDs)

Status: done
Type: data
Priority: P1
Dependencies: (none)
Claimed-by: codex-20251222-run1
Claimed-at: 2025-12-22T09:45Z
Last-updated: 2025-12-22T10:05Z
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Fix the schema mismatch between `countries/serbia/data/entities/ngos-sgos.csv` and `countries/serbia/data/entities/ngos-sgos-dictionary.md` by migrating the CSV to the documented schema (with stable `org_id`s).

---

## Context

- Current mismatch:
  - `countries/serbia/data/entities/ngos-sgos.csv` uses non-standard headers and does not include IDs.
  - The dictionary expects `org_id`, `focus`, `region`, contacts, website, `as_of`, etc.
- Existing narrative source list:
  - `countries/serbia/entities/ngos-sgos/index.md`
  - `countries/serbia/entities/ngos-sgos/profiles/*.md`

---

## Allowed write paths

- `countries/serbia/data/entities/ngos-sgos.csv`
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

- `countries/serbia/data/entities/ngos-sgos.csv`

---

## Acceptance criteria

- [x] CSV header and rows match the schema in `countries/serbia/data/entities/ngos-sgos-dictionary.md`.
- [x] Each organization has a stable `org_id` (ASCII, lowercase) and `as_of` date.
- [x] No information is lost: partnership/status notes from the old CSV are carried into `notes`.
- [x] No edits outside allowed write paths.

## Completion

- Rebuilt `countries/serbia/data/entities/ngos-sgos.csv` with schema-compliant header, stable `org_id`s, and 2025-12-22 `as_of` snapshot.
- Carried forward scope, focus area, audience, partnership notes, status, and last-reviewed metadata into the `notes` field for every organization.
