# T-388: Deterministic ID governance skill

Status: done
Type: structure
Priority: P1
Dependencies: T-020
Claimed-by: deterministic-id-governance
Claimed-at: 2025-12-21T19:09:25Z
Last-updated: 2025-12-21

---

## Goal

Create a global skill that standardizes deterministic IDs across countries and entity types, including formats, controlled kinds, normalization, canonical inputs per entity type, hash method, dedupe policy, and “how to mint” steps with examples for schools, agents, and events. Update the repo map to reflect the new global skill.

---

## Context

- `skills/**` is protected; changes require a `Type: structure` ticket.
- Existing data-model guidance needs a dedicated ID governance reference so entities, events, and partners stay deduped across countries.
- The skill should be global-first and avoid country-specific exceptions.

---

## Allowed write paths

- `skills/id-governance/**`
- `skills/README.md`
- `ROADMAP.md`
- `tickets/T-371-deterministic-id-governance-skill.md`
- `executions/**` (optional notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `tickets/**` (except this ticket file)
- `.github/**`
- `scripts/**`
- `countries/**`
- `reports/**`

---

## Required outputs

- `skills/id-governance/SKILL.md`
- Updated `skills/README.md` with the new skill
- Updated `ROADMAP.md` repo map if the new skill changes navigation expectations
- Ticket status updated to `done` with a short “what changed” note

---

## Acceptance criteria

- Skill documents the deterministic ID spec using the `<cc>_<kind>_<slug>__<hash>` format, controlled `kind` values, normalization rules, canonical key inputs per entity type, hash method, dedupe policy, “how to mint” steps, examples for schools/agents/events, and guidance on when not to mint.
- Repo map references the new skill so contributors can find it.
- No files outside `Allowed write paths` are modified.
- Ticket marked `done` with a concise “what changed” note upon completion.

---

## Execution notes (optional)

- What changed (short): Added a global ID governance skill with deterministic format, hashing, dedupe rules, minting steps, examples, and indexed it in the skills README and repo map.
- Any open questions: None.
- Follow-up tickets suggested: None.
