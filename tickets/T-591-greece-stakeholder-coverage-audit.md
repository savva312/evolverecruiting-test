# T-591: Greece — Stakeholder coverage audit + backlog plan

Status: in-progress
Type: qa
Priority: P0
Dependencies: (none)
Claimed-by: 02ba1f0f-ecc8-4492-8fcd-80706ca94032
Claimed-at: 2026-04-06T09:24:17Z
Last-updated: 2026-04-06
Agent: EvoTicket Resolver

---

## Goal

Verify that the Greece country tree actually covers every required stakeholder group (schools/counselors, agents, regulators/licensure, NGOs/SGOs, fairs/events, digital, employers/industry) and produce a backlog-ready plan that spells out what is done vs. missing.

## Context

The Greece sprint in `tickets/projectmanager.md` calls for a structure audit and explicit plans to close stakeholder gaps. Country subfolders exist, but there is no central summary of which areas are complete, partially complete, or missing (especially employer/industry linkages and newer playbooks). This ticket creates that control artifact so follow-on execution tickets can be scoped safely.

## Tasks

1. Review current Greece content under `countries/greece/**` for each stakeholder group listed above (schools, agents, regulators/licensure, NGOs/SGOs, fairs/events, digital channels, employer/industry partners).
2. Document current assets, health (complete/partial/missing), and required follow-up work in a new coverage file.
3. Update `countries/greece/entities/README.md` with a concise status summary plus 2–3 immediate focus areas.
4. For every gap, note the exact follow-up ticket(s) needed (title, scope hint, recommended allowed paths) inside the new coverage file so EvoManager can open them quickly next epoch.

## Allowed write paths

- `tickets/T-591-greece-stakeholder-coverage-audit.md`
- `countries/greece/entities/stakeholder-coverage.md`
- `countries/greece/entities/README.md`
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

- `countries/greece/entities/stakeholder-coverage.md` with:
  - table covering each stakeholder group (schools, agents, regulators/licensure, NGOs/SGOs, fairs/events, digital channels, employer/industry linkages)
  - current assets + health rating, sources/links, and recommended follow-up ticket ideas per group (include suggested ticket ID range and allowed paths)
- `countries/greece/entities/README.md` updated to include a short "Stakeholder coverage status" section linking to the new file and naming at least three urgent focus items (e.g., employer/industry mapping, specific datasets, QA needs)

## Acceptance criteria

- [ ] Coverage file lists all mandatory stakeholder categories with explicit health status (Complete / In progress / Gap) and cites the supporting files.
- [ ] At least three well-scoped follow-up ticket recommendations are recorded, each with a one-line scope description and suggested allowed paths.
- [ ] `countries/greece/entities/README.md` references the new coverage file and highlights short-term focus priorities.
- [ ] No edits occur outside allowed write paths.

## Worker notes

- 2026-04-06: Added `countries/greece/entities/stakeholder-coverage.md` as the Greece control artifact for stakeholder health, evidence links, and backlog-ready follow-up tickets.
- 2026-04-06: Updated `countries/greece/entities/README.md` with a stakeholder coverage status section and immediate Greece priorities.
- 2026-04-06: Local ticket kept `in-progress`; terminal lifecycle changes remain with the outer worker harness and Ticket API flow.
