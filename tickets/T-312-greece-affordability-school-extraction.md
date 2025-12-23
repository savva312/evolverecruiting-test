# T-312: Extract Greek high schools from affordability report and seed tickets

Status: done
Type: data
Priority: P1
Dependencies: 20251221 Greek high schools affordability report
Claimed-by: work
Claimed-at: 2025-12-21T17:41:13Z
Last-updated: 2025-12-21T17:42:23Z

---

## Goal

Use the 2025-12-21 **Greek High Schools for UNIC Affordability** report to extract every high school referenced, seed structured tracking (README, index, CSV), and create follow-on tickets for writing full profiles (one per school) plus a consolidation ticket to refresh the aggregate artifacts after profile work.

## Context

- Source document: `countries/greece/reports/20251221-Greek High Schools for UNIC Affordability.md`.
- The schools span Attica, Thessaloniki metro, and other municipalities ≥50,000. Many are private Lyceums with limited fee transparency; some are premium international schools with published high fees.
- Work must stay Greece-scoped and use the global **schools-and-feeders** skill plus the **high-school-profile-template**.

## Allowed write paths

- `countries/greece/entities/schools/**`
- `countries/greece/data/entities/schools.csv`
- `tickets/T-3*.md`
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

- Updated `countries/greece/entities/schools/README.md` with affordability-report scope and navigation pointers.
- New `countries/greece/entities/schools/index.md` enumerating all extracted schools with signals, school_ids, and ticket links.
- Updated `countries/greece/data/entities/schools.csv` with rows for every school in the report (no duplicates for existing IDs).
- One ticket per school (profiles) plus a consolidation ticket for README/index/CSV refresh after profile delivery.
- Ticket status updated when complete with a short “What changed” summary.

## Acceptance criteria

- [x] README and index in `countries/greece/entities/schools/` reference the affordability report and list all extracted schools.
- [x] `countries/greece/data/entities/schools.csv` contains one row per school from the report with clear `school_id`, city, region, type, and affordability/program notes.
- [x] New tickets exist: one for each school profile using the global template, and one consolidation ticket to update aggregate artifacts post-profile completion.
- [x] No modifications outside `Allowed write paths`.
- [x] Ticket updated to `done` with completion note once outputs are delivered.

## Execution notes (optional)

- What changed (short): Extracted every high school from the 2025-12-21 affordability report into the Greece schools CSV and new index, updated the schools README, and generated tickets T-301–T-355 (profiles) plus T-356 (post-profile aggregation).
- 2025-12-21 refresh: Added coverage snapshot + maintenance guidance to the Greece schools README and index so profile authors can keep the CSV/index aligned during follow-on ticket delivery.
- Follow-up tickets suggested: n/a (handled in this ticket via generated tickets).
