# T-580: Lebanon — refresh `data/README.md` (index + “what’s filled” scoreboard)

Status: open
Type: qa
Priority: P2
Dependencies: T-445, T-446, T-447, T-448, T-449, T-459 (recommended)
Claimed-by:
Claimed-at:
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Make the Lebanon data directory easier to use operationally by updating the index README to:
- link to newly created datasets (ops trackers + market mobility dataset)
- call out which CSVs are currently populated vs empty (scoreboard)
- give a short “how to extend safely” section (IDs, as_of, no-PII reminders)

---

## Context

- Lebanon data hub: `countries/lebanon/data/README.md`
- Several datasets are currently empty (headers only) while others are populated; operators need a quick “what’s ready” view.

---

## Allowed write paths

- `tickets/T-469-lebanon-data-readme-refresh.md`
- `countries/lebanon/data/README.md`

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

- `countries/lebanon/data/README.md` updated with:
  - links to `data/operations/school-outreach-tracker.csv`, `data/operations/event-roi.csv`, `data/operations/agent-performance.csv`
  - link to `data/market/outbound-mobility.csv` (if created via T-459)
  - a short “dataset status” table (populated vs empty) across entities/programs/marketing/operations

---

## Acceptance criteria

- [ ] README uses relative links that resolve in-repo.
- [ ] README includes a clear no-PII reminder.
- [ ] No files outside `Allowed write paths` were modified.

