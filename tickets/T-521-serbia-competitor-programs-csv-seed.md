# T-521: Serbia — Seed `competitor-programs.csv` (tuition + intakes by competitor program)

Status: open
Type: data
Priority: P1
Dependencies: (optional) T-453 (can be parallel)
Claimed-by:
Claimed-at:
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Populate `countries/serbia/data/programs/competitor-programs.csv` with a first, counseling-ready set of competitor programs including tuition, language, and intakes.

---

## Context

- Target file (currently empty):
  - `countries/serbia/data/programs/competitor-programs.csv`
- Related narrative inputs:
  - `countries/serbia/program-clusters/**/competitors.md`
  - `countries/serbia/entities/competitors/profiles/*.md`
- Constraints:
  - Use primary sources wherever possible (official university pages).
  - Do not guess tuition or intakes; if unknown, leave blank and explain in `notes` with a “verify” statement.

---

## Allowed write paths

- `countries/serbia/data/programs/competitor-programs.csv`
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

- `countries/serbia/data/programs/competitor-programs.csv`

---

## Acceptance criteria

- [ ] Adds at least 30 rows across the highest-relevance programs (minimum: Medicine/MD, CS, Business).
- [ ] Each row includes: competitor name, program name, degree level, delivery, tuition (EUR when stated), location, language, and intake months where published.
- [ ] `notes` includes source URLs and/or “verify” flags (no invented numbers).
- [ ] No edits outside allowed write paths.

