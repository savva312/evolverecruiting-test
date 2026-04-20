# T-505: Serbia — Populate `agents.csv` from existing agent profiles

Status: done
Type: data
Priority: P1
Dependencies: (none)
Claimed-by: codex-run-20251223
Claimed-at: 2025-12-23T00:00:00Z
Last-updated: 2025-12-23
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Create a usable, filterable Serbia agent dataset by populating `countries/serbia/data/entities/agents.csv` using the already-written agent profiles.

---

## Context

- Existing long-form inputs:
  - `countries/serbia/entities/agents/README.md`
  - `countries/serbia/entities/agents/feeder-candidates.md`
  - `countries/serbia/entities/agents/profiles/*.md`
- Target structured output:
  - `countries/serbia/data/entities/agents.csv`
  - Dictionary: `countries/serbia/data/entities/agents-dictionary.md`

---

## Allowed write paths

- `countries/serbia/data/entities/agents.csv`
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

- `countries/serbia/data/entities/agents.csv`

---

## Acceptance criteria

- [x] `countries/serbia/data/entities/agents.csv` contains at least the agents listed in `countries/serbia/entities/agents/README.md`.
- [x] Uses the schema in `countries/serbia/data/entities/agents-dictionary.md` (services and markets are `;`-separated).
- [x] Every row has `as_of` populated (YYYY-MM-DD) and no placeholder emails/domains.
- [x] No edits outside allowed write paths.

### What changed
- Populated `countries/serbia/data/entities/agents.csv` with ten agents sourced from the Serbia agent profiles, including services, destinations, and compliance notes dated 2025-12-23.
