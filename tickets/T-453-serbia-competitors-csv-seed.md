# T-453: Serbia — Seed `competitors.csv` (top competitor set for Serbia recruiting)

Status: done
Type: data
Priority: P1
Dependencies: (none)
Claimed-by: codex-run-20251222
Claimed-at: 2025-12-22T10:45:00Z
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Populate `countries/serbia/data/entities/competitors.csv` with a practical first competitor set (at least 15) used in Serbia counseling and positioning.

---

## Context

- Structured target:
  - `countries/serbia/data/entities/competitors.csv`
  - Dictionary: `countries/serbia/data/entities/competitors-dictionary.md`
- Narrative sources to mine (read-only inputs):
  - `countries/serbia/entities/competitors/profiles/*.md`
  - `countries/serbia/program-clusters/**/competitors.md`

---

## Allowed write paths

- `countries/serbia/data/entities/competitors.csv`
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

- `countries/serbia/data/entities/competitors.csv`

---

## Acceptance criteria

- [x] Includes a balanced set across key Serbia program clusters:
  - [x] Medicine/health (CEE + Greece/Cyprus options)
  - [x] CS/data/AI/cyber
  - [x] Business/finance/marketing
- [x] Uses only the schema in `countries/serbia/data/entities/competitors-dictionary.md` (target programs are `;`-separated).
- [x] Each row has `as_of` populated and concise notes that include at least one source URL (if the schema doesn’t include a URL column, include URLs in `notes`).
- [x] No edits outside allowed write paths.

## What changed

- Seeded `countries/serbia/data/entities/competitors.csv` with 15 evidence-backed entries (5 medicine, 5 CS/data/AI/cyber, 5 business/finance/marketing) including Serbia publics, CEE medical faculties, Greece/Cyprus options, and EU CS/business destinations most cited by Serbia-facing agents.
