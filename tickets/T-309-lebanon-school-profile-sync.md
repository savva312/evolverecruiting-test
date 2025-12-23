# T-309: Lebanon high-priority school profile sync

- **Status:** done
- **Type:** data
- **Priority:** P0
- **Claimed-by:** work
- **Claimed-at:** 2025-12-21 17:23:07 UTC

## Objective
Audit all high-priority Lebanese school profiles recently added via tickets and ensure navigation pages and structured data stay aligned. Update the schools README, profiles index, and `countries/lebanon/data/entities/schools.csv` to reflect the latest profile content. Identify any high-priority schools that should have profiles but do not, and open dedicated tickets for each gap.

## Allowed write paths
- countries/lebanon/entities/schools/**
- countries/lebanon/data/entities/schools.csv
- tickets/T-277-lebanon-school-profile-sync.md
- tickets/T-228-*.md
- tickets/T-229-*.md
- tickets/T-230-*.md
- tickets/T-231-*.md

## Forbidden write paths
- README.md
- AGENTS.md
- ROADMAP.md
- skills/**

## Required outputs
- Updated `countries/lebanon/entities/schools/README.md` summarizing the high-priority school set with links and status notes.
- An index under `countries/lebanon/entities/schools/profiles/README.md` that lists each high-priority school profile.
- Refreshed `countries/lebanon/data/entities/schools.csv` (single header row; one row per high-priority school with current evidence and contacts).
- New ticket(s) for any missing high-priority profiles (one ticket per school), using the T-228–T-230 number range.

## Acceptance criteria
- README and profiles index both list all current high-priority Lebanese schools with working relative links to their profiles and clear tier/fit signals.
- `countries/lebanon/data/entities/schools.csv` is deduplicated, reflects the latest profile facts (tier, program-fit tags, USD evidence, last verified), and contains no repeated header rows.
- Any identified missing high-priority school has its own ticket filed in the allowed number range with scope, outputs, and acceptance criteria.
- Changes stay within allowed paths; ticket status is updated to `done` when complete with a short “What changed” note.

## Dependencies
- None.

## Notes/Context
- Source lists to cross-check: `countries/lebanon/entities/schools/README.md`, `countries/lebanon/reports/20251220-Lebanon USD-Feeder High Schools.md`, and existing profile folders under `countries/lebanon/entities/schools/profiles/`.

## What changed
- Recounted and synced the Lebanon high-priority set to 18/18 schools; updated `countries/lebanon/entities/schools/README.md` with the full geography tables, CSV IDs, and a clean data-quality note confirming no backlog.
- Rebuilt `countries/lebanon/entities/schools/profiles/README.md` into a single, program-tagged index covering all 18 profiles with CSV-aligned tiers and live links.
- Deduplicated and rewrote `countries/lebanon/data/entities/schools.csv` to one header and one row per school (18 total), keeping latest evidence, contacts, program-fit tags, and `last_verified` stamps standardized to 2025-12-21.
