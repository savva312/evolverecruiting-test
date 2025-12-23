# T-368: Refresh Greece schools README/index/CSV after affordability profile wave

Status: done
Type: content
Priority: P2
Dependencies: T-301 through T-355
Claimed-by: work
Claimed-at: 2025-02-18
Last-updated: 2025-02-18

---

## Goal

After completing the affordability-report school profiles (T-301–T-355), update the Greece schools README, index, and CSV to reflect profile completion status, links, and any validated data improvements.

## Context

- Source list captured in `countries/greece/reports/20251221-Greek High Schools for UNIC Affordability.md` and structured via T-300.
- Profiles for each school are scoped in T-301–T-355 with individual allowed paths.
- This ticket consolidates navigation and data alignment once profile drafts exist.

## Allowed write paths

- `countries/greece/entities/schools/README.md`
- `countries/greece/entities/schools/index.md`
- `countries/greece/data/entities/schools.csv`
- `tickets/T-356-greece-schools-index-and-csv-refresh.md`
- `executions/**` (optional run notes)

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- Other country directories (e.g., `countries/bulgaria/**`, `countries/nigeria/**`, etc.)
- `.github/**`
- `scripts/**`

## Required outputs

- Updated README and index summarizing completed affordability profiles with links to files and tickets.
- CSV row adjustments (if needed) to reflect any corrected metadata from profile work.
- Ticket notes summarizing which school tickets were completed and what changed.

## Acceptance criteria

- README and index reference the affordability source report, list covered schools, and link to their profiles.
- CSV remains consistent with profile metadata after updates.
- No modifications outside allowed paths; protected files unchanged.
- Ticket is updated with completion notes when finished.

## Completion notes (2025-02-18)

- Added a `Profile` column to the Greece schools index linking 46 delivered affordability-report drafts and marking the 9 pending profiles.
- Updated the schools README with a T-356 refresh summary, pending school list, and CSV alignment notes; CSV already matched the 55 school_ids so no row edits were required.
