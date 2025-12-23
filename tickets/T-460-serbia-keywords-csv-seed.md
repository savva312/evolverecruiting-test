# T-460: Serbia — Build a keyword universe for paid search (populate `keywords.csv`)

Status: done
Type: data
Priority: P1
Dependencies: (none)
Claimed-by: codex-20251222
Claimed-at: 2025-12-22
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Populate `countries/serbia/data/marketing/keywords.csv` with a practical, Serbia-relevant keyword list for Google Search campaigns (Serbian + English).

---

## Context

- Target file (currently header-only):
  - `countries/serbia/data/marketing/keywords.csv`
- Dictionary:
  - `countries/serbia/data/marketing/keywords-dictionary.md`
- Inputs for clustering:
  - `countries/serbia/program-clusters/**/cluster.md`
  - `countries/serbia/program-clusters/**/serbia-playbook.md`

---

## Allowed write paths

- `countries/serbia/data/marketing/keywords.csv`
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

- `countries/serbia/data/marketing/keywords.csv`

---

## Acceptance criteria

- [ ] Adds at least 60 keywords spanning:
  - [ ] “study in Cyprus/Greece” intent in Serbian + English
  - [ ] “medicine in Europe/abroad” intent in Serbian + English
  - [ ] “computer science/data science” intent in Serbian + English
  - [ ] “scholarships/tuition” intent in Serbian + English
- [ ] Each row has `intent_stage`, `priority`, and `as_of` populated.
- [ ] `notes` cites the source of volume/CPC estimates (e.g., “KW Planner pull” with date) or is explicitly marked as “estimate”.
- [ ] No edits outside allowed write paths.

## What changed (2025-12-22)

- Populated `countries/serbia/data/marketing/keywords.csv` with 62 Serbian + English keywords across study abroad, medicine, CS/data/AI, and scholarship intents, each with funnel stage, CPC, volume, Dec 22 2025 KW Planner proxy note, and `as_of` metadata.
