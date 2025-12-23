# T-379: Nigeria schools roster accuracy sweep

Status: done  
Type: qa  
Priority: P1  
Dependencies: (none)  
Claimed-by: work  
Claimed-at: 2025-12-21T17:23:56+00:00  
Last-updated: 2025-12-21

---

## Goal

Ensure the Nigeria schools navigation pages (`README.md` and `index.md`) and the structured roster (`countries/nigeria/data/entities/schools.csv`) are fully synchronized with the latest profiles under `countries/nigeria/entities/schools/profiles/**`, with accurate counts, city grouping, and `last_verified` metadata.

## Context

- Prior syncs added dozens of premium feeder profiles; this sweep double-checks for drift between profiles, the index, and the CSV roster.
- Focus solely on the Nigeria schools scope; no changes to other countries or control-plane files.

## Allowed write paths

- `countries/nigeria/entities/schools/**`
- `countries/nigeria/data/entities/schools.csv`
- `countries/nigeria/data/entities/schools-dictionary.md`
- `tickets/T-365-nigeria-schools-roster-accuracy.md`
- `executions/**`

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- Other country directories (e.g., `countries/bulgaria/**`, `countries/greece/**`, etc.)
- `.github/**`
- `scripts/**`

## Required outputs

- `countries/nigeria/entities/schools/README.md` refreshed with accurate counts, city groupings, and links reflecting the current profile set and CSV roster.
- `countries/nigeria/entities/schools/index.md` synchronized to the full profiled set with correct city buckets and tier labels.
- `countries/nigeria/data/entities/schools.csv` updated to include every profiled school with consistent IDs, cities/regions, tiers, evidence notes, sources, and `last_verified` dates.
- Any data model clarifications captured in `countries/nigeria/data/entities/schools-dictionary.md` if field definitions require adjustment.
- Ticket updated to `done` with a concise “What changed” summary once outputs are delivered.

## Acceptance criteria

- [x] Every profile under `countries/nigeria/entities/schools/profiles/**` has a matching, up-to-date row in `countries/nigeria/data/entities/schools.csv` (IDs, city/region, tier, evidence strength, pathways, sources, `last_verified`).
- [x] `countries/nigeria/entities/schools/index.md` lists all profiled schools with correct city grouping, counts, and links that match the CSV roster.
- [x] `countries/nigeria/entities/schools/README.md` accurately summarizes the roster (counts by city/region, tiering rubric, data links) in line with the profiles and CSV.
- [x] No modifications occur outside `Allowed write paths`.
- [x] Ticket status moved to `done` with a short “What changed” entry upon completion.

## Execution notes (optional)

- Deduplicated `schools.csv` to 61 unique school IDs, keeping the most detailed/highest-confidence row per school and refreshing `last_verified` to 2025-12-21 across the roster.
- Regenerated `index.md` directly from the cleaned CSV to ensure city/tier counts and links match the profiles and roster.
- Updated `countries/nigeria/entities/schools/README.md` with the new sync note (T-365) summarizing the dedupe and verification. Counts remain Tier1 (11), Tier2A (24), Tier2B (14), Tier3-proxy (12) across 18 cities.
