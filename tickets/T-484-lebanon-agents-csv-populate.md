# T-484: Lebanon — populate `agents.csv` (sync with existing agent profiles)

Status: done
Type: data
Priority: P1
Dependencies: (none)
Claimed-by: evoticketresolver_iuwmz__q
Claimed-at: 2025-12-22T20:41:47Z
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Turn the existing Lebanon agent roster into a usable dataset by populating `countries/lebanon/data/entities/agents.csv` with **one row per existing agent profile** under `countries/lebanon/entities/agents/profiles/`.

This enables partner pipeline reporting, segmentation (program/campus fit), and attribution-ready partner tracking.

---

## Context

Existing Lebanon agent content:
- Tiered roster: `countries/lebanon/entities/agents/feeder-candidates.md`
- Profiles: `countries/lebanon/entities/agents/profiles/*.md`

Structured dataset exists but is empty (headers only):
- `countries/lebanon/data/entities/agents.csv`
- `countries/lebanon/data/entities/agents-dictionary.md`

---

## Allowed write paths

- `tickets/T-484-lebanon-agents-csv-populate.md`
- `countries/lebanon/data/entities/agents.csv`
- `countries/lebanon/data/entities/agents-dictionary.md` (only if minor clarifications are needed)
- `countries/lebanon/entities/agents/README.md` (optional: add links to the CSV + dictionary)

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

- `countries/lebanon/data/entities/agents.csv` populated with **≥15 rows** (or the current count of agent profiles, whichever is higher), one per existing profile.
- (Optional) `countries/lebanon/entities/agents/README.md` updated to link to `agents.csv` and `agents-dictionary.md`.

---

## Acceptance criteria

- [x] Every row has `agent_id`, `name`, `services`, `primary_markets`, and `as_of`.
- [x] `primary_markets` uses ISO 3166-1 alpha-2 country codes and semicolon-separated multi-values (e.g., `CY;GR;FR`).
- [x] No `TBD` / `N/A` tokens in the CSV (blank cells are allowed).
- [x] No personal phone numbers, DOB/passport/ID, or other sensitive data added to the repo.
- [x] No files outside `Allowed write paths` were modified.

## What changed

- Populated `countries/lebanon/data/entities/agents.csv` with one row per existing profile (15 total).
- Clarified `agents-dictionary.md` examples (ISO `GB` for the UK; added `accommodation` and `test_prep` as service examples).
- Linked the dataset + dictionary from `countries/lebanon/entities/agents/README.md`.
