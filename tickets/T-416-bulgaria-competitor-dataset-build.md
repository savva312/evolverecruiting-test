# T-416: Bulgaria competitor dataset build

Status: open
Type: data
Priority: P1
Dependencies: (none)

## Goal
Populate the empty `data/entities/competitors.csv` and expand competitor profiles so Bulgaria’s recruiting team has a structured view of the institutions we pitch against across program clusters.

## Allowed write paths
- `countries/bulgaria/data/entities/competitors.csv`
- `countries/bulgaria/data/entities/competitors-dictionary.md`
- `countries/bulgaria/entities/competitors/**`
- `tickets/T-416-bulgaria-competitor-dataset-build.md`

## Forbidden write paths
- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `countries/**` directories outside the competitor folders listed above
- `.github/**`
- `scripts/**`

## Required outputs
1. `competitors.csv` filled with **≥10** rows covering high-priority institutions (Bulgarian publics, Greek/Cyprus peers, CEE/Western EU options) with consistent IDs, data in every column, and `as_of` timestamps.
2. `competitors-dictionary.md` updated if new fields/definitions are needed to describe the captured data (e.g., add columns for pricing bands or entry tests) with clear guidance.
3. At least **5** refreshed or newly created competitor profile markdown files under `entities/competitors/profiles/` that align with the CSV rows (cross-link via IDs or filenames) and include tuition, entry criteria, messaging risks, and sources.
4. `entities/competitors/README.md` (optional) updated only if navigation/context needs to reflect the expanded roster.

## Acceptance criteria
- CSV validates (no blank headers, consistent delimiters) and matches the dictionary’s field definitions.
- Every competitor profile cites at least one source and lists `last_verified`.
- Profiles and CSV stay in sync (same IDs/names) and cover multiple program clusters (business, CS, medicine, psychology, etc.).
- Work is confined to the allowed paths and ticket metadata is updated when claimed/completed.

## Notes/Context
Use existing market/program research to prioritize which competitors matter most for Bulgarian students considering UNIC campuses. Flag any gaps that need separate deep-dive tickets (e.g., medicine vs business pricing comparisons) in your completion notes.
