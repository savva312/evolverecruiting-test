# T-474: Bulgaria — populate `agents.csv` (sync with existing agent profiles)

Status: open
Type: data
Priority: P1
Dependencies: (none)
Claimed-by:
Claimed-at:
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Turn the existing Bulgaria agent roster into a usable dataset by populating `countries/bulgaria/data/entities/agents.csv` with rows that map cleanly to the 12 existing profiles under `countries/bulgaria/entities/agents/profiles/`.

This enables partner pipeline reporting, segmentation (campus/program fit), and attribution-ready partner tracking.

---

## Context

- The repo already contains 12 Bulgaria agent profiles and a tiered roster:
  - `countries/bulgaria/entities/agents/feeder-candidates.md`
  - `countries/bulgaria/entities/agents/profiles/*.md`
- The structured dataset exists but is empty (headers only):
  - `countries/bulgaria/data/entities/agents.csv`
  - `countries/bulgaria/data/entities/agents-dictionary.md`

---

## Allowed write paths

- `tickets/T-419-bulgaria-agents-csv-populate.md`
- `countries/bulgaria/data/entities/agents.csv`
- `countries/bulgaria/data/entities/agents-dictionary.md`
- `countries/bulgaria/entities/agents/README.md`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- `countries/**` (except `countries/bulgaria/**`)

---

## Required outputs

- `countries/bulgaria/data/entities/agents.csv` populated with **≥12 rows**, one per existing agent profile.
- `countries/bulgaria/entities/agents/README.md` updated to link to `agents.csv` + `agents-dictionary.md` as the structured companion to the profiles.
- If needed: `countries/bulgaria/data/entities/agents-dictionary.md` corrected for ISO country codes (e.g., `GB` not `UK`) and any clarified field guidance.

---

## Acceptance criteria

- [ ] `countries/bulgaria/data/entities/agents.csv` has ≥12 data rows and a non-empty `as_of` for every row.
- [ ] `primary_markets` uses ISO 3166-1 alpha-2 country codes (e.g., `CY;GR;GB`) and semicolon-separated multi-values.
- [ ] No agent rows use placeholder tokens like `TBD`/`N/A` inside the CSV (blank is allowed).
- [ ] No files outside `Allowed write paths` were modified.

