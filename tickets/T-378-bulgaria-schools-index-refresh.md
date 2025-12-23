# T-378: Bulgaria schools README/index/CSV refresh

Status: done
Type: qa
Priority: P0
Dependencies: T-227-bulgaria-high-priority-schools-audit
Claimed-by: work
Claimed-at: 2025-12-21T17:23:26Z
Last-updated: 2025-12-21
What changed: Added a new Bulgaria schools index, refreshed the schools README navigation (including Varna Tier 2), and corrected CSV types/notes to match the latest profiles.

---

## Goal

Ensure the Bulgaria schools navigation and data are fully synchronized with the latest profiles. Update the schools README, main index, and `data/entities/schools.csv` so every existing profile is represented with accurate metadata and links; surface any gaps that need new tickets.

## Allowed write paths

- `countries/bulgaria/entities/schools/**`
- `countries/bulgaria/data/entities/schools.csv`
- `tickets/T-365-bulgaria-schools-index-refresh.md`
- `executions/**` (optional notes)

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/README.md`
- `.github/**`
- `scripts/**`

## Required outputs

- Refreshed `countries/bulgaria/entities/schools/README.md` with up-to-date navigation and summary of covered cities/regions.
- Updated `countries/bulgaria/entities/schools/index.md` (and any city/"other" sub-indexes) to list all existing school profiles with correct relative links and labels.
- Regenerated `countries/bulgaria/data/entities/schools.csv` aligned to the latest profile set and the dictionary in `countries/bulgaria/data/entities/schools-dictionary.md`, including stable IDs, city/region, ownership, type, contact email (if available), notes, and ISO `as_of` date.
- Follow-up ticket(s) if any missing profiles are discovered.

## Acceptance criteria

- README and index files reference every current Bulgarian school profile, grouped by city/region with working links and no duplicates.
- `schools.csv` rows align one-to-one with profile files and follow the dictionary conventions (field order, values, `as_of` date) without stale entries.
- Any missing or newly identified schools are documented via new ticket(s) under `tickets/` within allowed paths.
- No changes occur outside `Allowed write paths`; ticket metadata is updated upon completion.

## Notes/Context

- Treat profile filenames/IDs as source of truth for school names and city assignments.
- Preserve deterministic IDs (e.g., `sch-bg-<city>-<slug>`) and keep `as_of` set to the date of this refresh.
