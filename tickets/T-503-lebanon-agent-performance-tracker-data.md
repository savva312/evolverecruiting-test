# T-503: Lebanon — add agent performance tracker dataset (partner scorecard spine)

Status: open
Type: data
Priority: P1
Dependencies: T-445 (recommended)
Claimed-by:
Claimed-at:
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Add a structured partner-performance table so the Lebanon team can manage agents as a pipeline channel (applications → offers → deposits → starts) without relying on narrative notes.

---

## Context

- Agent roster exists as profiles + tiering:
  - `countries/lebanon/entities/agents/feeder-candidates.md`
  - `countries/lebanon/entities/agents/profiles/*.md`
- `countries/lebanon/data/entities/agents.csv` should be populated first (T-445) so this table can reference `agent_id`.

---

## Allowed write paths

- `tickets/T-449-lebanon-agent-performance-tracker-data.md`
- `countries/lebanon/data/operations/agent-performance.csv`
- `countries/lebanon/data/operations/agent-performance-dictionary.md`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**` (global)
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- `countries/**` (except `countries/lebanon/**`)

---

## Required outputs

- `countries/lebanon/data/operations/agent-performance.csv` created with headers and (optionally) one example row.
- `countries/lebanon/data/operations/agent-performance-dictionary.md` created defining fields (agent_id, period, campus, leads, apps, offers, deposits, starts, notes, as_of) and calculation notes.

---

## Acceptance criteria

- [ ] Table uses `agent_id` as the join key (no free-text agent names in the performance table).
- [ ] Dictionary explicitly prohibits storing applicant PII and sensitive documents in this repo.
- [ ] No files outside `Allowed write paths` were modified.

