# T-446: Romania — populate `countries/romania/data/entities/agents.csv` (v1) + dictionary

Status: done
Type: data
Priority: P1
Dependencies: T-127
Claimed-by: codex-run-20251222
Claimed-at: 2025-12-22T15:30:00Z
Completed-at: 2025-12-22T16:05:00Z
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Populate `countries/romania/data/entities/agents.csv` with a first, usable roster (minimum: the 10 existing agent profiles in `countries/romania/entities/agents/profiles/`) and update the dictionary so the dataset can be used for:
- partner tiering
- governance (risk/compliance)
- routing and attribution (profile_path, city coverage, relationship status)

---

## Context

Existing sources in-repo:
- Agent roster: `countries/romania/entities/agents/feeder-candidates.md`
- Profiles: `countries/romania/entities/agents/profiles/*.md`
- Dictionary scaffold: `countries/romania/data/entities/agents-dictionary.md`

---

## Allowed write paths

- `tickets/T-446-romania-agents-csv-v1.md`
- `countries/romania/data/entities/agents.csv`
- `countries/romania/data/entities/agents-dictionary.md`
- `countries/romania/entities/agents/feeder-candidates.md` (optional: add `agent_id` column and keep the table aligned)
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
- `countries/**` (except `countries/romania/**`)

---

## Required outputs

- Updated `countries/romania/data/entities/agents.csv` (minimum 10 rows)
- Updated `countries/romania/data/entities/agents-dictionary.md` reflecting the final schema
- (Optional) Updated `countries/romania/entities/agents/feeder-candidates.md` if adding explicit `agent_id` references

---

## Acceptance criteria

- [x] `countries/romania/data/entities/agents.csv` includes at least the 10 agents already profiled in `countries/romania/entities/agents/profiles/`.
- [x] Each row includes a stable `agent_id` and a working `profile_path`.
- [x] Tiering and relationship fields are present and consistently filled (`tier`, `relationship_status`, and `compliance_risk` or equivalent — define in dictionary).
- [x] Dictionary matches the dataset exactly.
- [x] No edits outside allowed paths.

## Completion Notes
- 2025-12-22 — Added governance-focused schema (tiering, relationship status, compliance risk, coverage cities, profile links) to the dictionary and aligned `agents.csv` header.
- 2025-12-22 — Populated 10 priority Romania agents with stable IDs, campus-ready services/program focus tags, and enablement notes tied to their profiles.
