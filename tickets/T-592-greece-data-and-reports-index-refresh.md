# T-592: Greece — Data + reports index refresh (make inventories actionable)

Status: done
Type: integration
Priority: P0
Dependencies: (none)
Claimed-by: work
Claimed-at: 2026-04-16T09:29:16Z
Last-updated: 2026-04-16
Agent: EvoTicket Resolver

---

## Goal

Give Greece operators a single place to see which datasets and reports exist, what is missing, and how fresh each artifact is by creating data/report indices that cite every file under `countries/greece/data/**` and `countries/greece/reports/**`.

## Context

- `countries/greece/data/README.md` describes folder conventions but lacks an actual inventory or freshness tracker.
- `countries/greece/reports/README.md` only states formatting guidelines; it does not list the four reports already in the folder or note pending deliverables.
- Active sprints call for better data/report navigation so downstream tickets can target the right files and avoid duplicate work.

## Tasks

1. Catalog every CSV/dictionary/notes file under `countries/greece/data/**` (entities, programs, marketing, operations). Capture owner, last-updated date, maturity (complete/partial/placeholder), and next required action.
2. Create `countries/greece/data/index.md` to present the catalog in table form; link to each dataset/dictionary.
3. Update `countries/greece/data/README.md` so it links to the new index and surfaces top data priorities (at least three short bullets).
4. Update `countries/greece/reports/README.md` with a table that lists each report file (title, date, summary, next action) and includes a backlog subsection for reports that still need to be written.

## Allowed write paths

- `tickets/T-592-greece-data-and-reports-index-refresh.md`
- `countries/greece/data/index.md`
- `countries/greece/data/README.md`
- `countries/greece/reports/README.md`
- `executions/**` (optional notes)

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `.github/**`
- `scripts/**`
- Other country folders under `countries/**`

## Required outputs

- New `countries/greece/data/index.md` covering every dataset/dictionary under `countries/greece/data/**` with columns for `file`, `owner`, `last_updated`, `status`, and `next_action`.
- Updated `countries/greece/data/README.md` that links to the index, summarizes the state of each subfolder, and lists at least three immediate data follow-ups.
- Updated `countries/greece/reports/README.md` containing:
  - table of current reports with summary + last updated + intended audience
  - backlog subsection that enumerates remaining priority reports (with short scope statements)

## Acceptance criteria

- [ ] Data index lists every CSV/dictionary currently in `countries/greece/data/**` (entities, programs, marketing, operations) and clearly marks which ones are placeholders vs. populated.
- [ ] Report README lists all existing reports in the folder and provides next actions/backlog for at least two additional reports.
- [ ] README updates link directly to the new index/table sections so future agents can navigate quickly.
- [ ] No edits occur outside allowed write paths.

## Execution notes

- What changed (short): Verified that `countries/greece/data/index.md` already catalogs all current Greece datasets/dictionaries and that `countries/greece/data/README.md` and `countries/greece/reports/README.md` contain the required navigation, summaries, and backlog; left those files unchanged and updated this ticket to reflect completion.
- Open questions: Dataset owners and explicit freshness verification still need to be confirmed in future Greece data tickets.
