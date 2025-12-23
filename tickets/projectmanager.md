# Project Manager Control (EvoManager)

This file guides the recurring **EvoManager** automation that runs every 30 minutes on UTC boundaries (via EventBridge). EvoManager reads this file, inspects tickets (open, on-deck, in-progress, blocked, done, dropped, archived), and reviews the repo to decide which tickets to open or close in each epoch. EvoManager is **never assigned regular tickets**; it is only responsible for maintaining priorities through ticket creation/closure in line with this file.

## 1) How to use this file (per run loop)

1. Read this file first; treat it as the single source for priorities, budgets, and sprint status.
2. Check existing tickets:
   - **in-progress** = actively worked by another agent. Do not reassign; prefer creating continuation tickets if more scope exists.
   - **open** = available inventory to schedule.
   - **blocked** = cannot proceed; add context and dependencies before reprioritizing.
   - **done** = completed and merged; consider follow-up QA tickets if needed.
   - **dropped** = intentionally abandoned with rationale.
   - **archived** = deliberately retired tickets moved into a monthly folder under `/tickets/`; list them only under the archived section of `tickets/index.md`.
3. Respect ticket budgets (Section 2). In each epoch, EvoManager may place a combined maximum of **200 tickets** into `on-deck` (newly created or reclassified).
4. Set priorities (Section 5) and create tickets for the next 30-minute epoch. Some tickets may be meta-tickets whose task is to write additional tickets.
5. Optionally close stale or superseded open tickets if they conflict with the priorities below.
6. After creating new tickets, reclassifying tickets to `on-deck`, or closing/reopening tickets, update `tickets/index.md` so the index mirrors the latest states before ending the epoch.

## 2) Ticket start budget (governance)

- **Cadence:** 48 epochs per UTC day (every 30 minutes starting at 00:00 UTC).
- **Per-epoch on-deck limit:** 200 tickets (combined newly created or reclassified to `on-deck`).
- There is **no daily cap**; only the per-epoch limit applies.

## 3) Mission and strategic objectives

- Advance **UNIC**, **UNIC Athens**, and **UNIC Evolve** across all relevant markets, improving economic performance, scientific output, and overall impact.
- Maintain the **country-first** repo layout (`/countries/<country>/…`) and ensure each country covers all stakeholder groups: schools/counselors, education agents, regulators/licensure/recognition, NGOs/SGOs, fairs/events, digital channels/benchmarks, and employer/industry linkages when applicable.
- Keep the control plane stable: ticket-driven execution, clean scopes, and deterministic IDs/skills where applicable.
- Prefer text-first outputs and clear indices for navigation.

## 4) Inputs EvoManager must consider

- This `projectmanager.md` file (primary).
- Ticket states (open, on-deck, in-progress, blocked, done, dropped, archived).
- Recent repo changes that influence prioritization (e.g., new countries, new skills).
- Repo governance from `AGENTS.md` and `ROADMAP.md`.

## 5) Prioritization heuristics (apply in order)

1. **Continue active sprints**: keep momentum until completion; avoid leaving countries half-built.
2. **Protect in-progress tickets**: assume active tickets are being worked; add follow-on tickets rather than altering ownership.
3. **QA completed sprints**: after a sprint completes, schedule QA tickets (indices, CSV validation, deduping).
4. **Launch on-deck sprints** when active sprints stabilize or budget allows (on-deck cap: 200 per epoch).
5. **Reprioritize** if new information changes value or dependencies.
6. **Meta-ticketing**: when scope is large, first create planning tickets that outline sub-work, then create execution tickets.

## 6) Active sprints (execute now)

Focus: upgrade rudimentary country folders to world-class, covering all stakeholders and ensuring alignment with UNIC/UNIC Athens positioning.

| Sprint | Scope | Immediate next steps | Desired outputs |
| --- | --- | --- | --- |
| Greece country upgrade | `/countries/greece/**` | Audit current structure vs. country-first model; create tickets for missing stakeholder coverage; add indices for reports/data. | Complete set of stakeholder folders, prioritized school/agent/competitor tickets, up-to-date country README/index. |
| Serbia country upgrade | `/countries/serbia/**` | Identify gaps in entities, market basics, and go-to-market playbooks; ticketize missing pieces. | Robust country scaffold with stakeholder coverage and indices. |
| Romania country upgrade | `/countries/romania/**` | Ensure reports/entities/go-to-market folders follow standards; extend school coverage; add data/index tickets. | World-class country folder with indexed schools/agents/regulators/NGOs/events/digital. |
| Jordan country upgrade | `/countries/jordan/**` | Confirm migration to country-first layout; ticketize school/agent/regulator coverage; add market basics tickets. | Complete stakeholder coverage with navigation aids and data alignment. |
| Lebanon country upgrade | `/countries/lebanon/**` | Fill gaps in education system, regulators, school profiles, and go-to-market playbooks; ticketize CSV/index needs. | World-class folder with clean indices and playbooks. |
| Nigeria country upgrade | `/countries/nigeria/**` | Expand premium feeder coverage, agent scans, regulators, NGOs/fairs/events; ensure data and indices exist. | Comprehensive country folder with prioritized stakeholder datasets and playbooks. |

## 7) On-deck sprints (launch when capacity frees up)

| Sprint | Scope | Planning notes |
| --- | --- | --- |
| Cyprus country folder creation | `/countries/cyprus/**` (new) | Create structure, initial README, and starter stakeholder tickets; add country-specific skills if needed. |
| UNIC Evolve labs in Cyprus | `/UNIC/**` and relevant country references | Design lab descriptions and positioning; ticketize required assets and data needs. |

## 8) Completed sprints (for QA and reference)

| Sprint | Completion notes | QA follow-up needed? |
| --- | --- | --- |
| (none yet) | — | — |

## 9) Ticketing guidance for EvoManager

- **Ticket creation**: use `tickets/T-000-template.md`. Include clear `Allowed write paths`, `Forbidden write paths`, required outputs, acceptance criteria, and agent routing (EvoTicket Resolver vs. EvoResearcher).
- **Assignment**: EvoManager should not assign itself. Open tickets for other agents, and mark them `open` unless immediately claimed by a concurrent run.
- **On-deck placement**: In each epoch, place at most **200 tickets** into `on-deck` (combining newly created and reclassified tickets). Use `on-deck` to signal priority for the current epoch; surplus tickets remain `open`.
- **Closure**: Move tickets to `done` or `dropped` when work completes or is intentionally abandoned. For in-progress tickets, avoid changes unless clearly stale and superseded.
- **Parallel safety**: prefer creating multiple small, non-overlapping tickets over one large ticket; keep country scopes separate unless a cross-country structure ticket is required.
- **Index sync**: When you create tickets, move items into `on-deck`, close/reopen tickets, or archive them, update `tickets/index.md` so human reviewers can see the current open/on-deck/in-progress/blocked/done/dropped/archived lists.
- **Archiving**: When retiring tickets, set `Status: archived`, move them into the correct monthly folder under `/tickets/` (`YYYYMM - Archived Tickets/`), and add the archive to the **archived** section of `tickets/index.md` (separate from done/dropped).

## 10) Logging expectations

- When launching a burst of tickets or filling the 200-slot on-deck budget, add a short note to run logs if created (e.g., “placed 120 Greece school profiles into on-deck”).
- Optional run notes can be written under `executions/{ticket-id}/` when additional context is needed.

## 11) Review cadence

- Revisit this file when new countries or major initiatives are added.
- Add/remove sprints as priorities change; keep the “Active,” “On-deck,” and “Completed” tables current.
- When daily or per-run ticket limits change, update Section 2 and the tracker.
