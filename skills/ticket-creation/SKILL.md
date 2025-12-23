---
name: ticket-creation
description: "How to draft, claim, and close EvoBuilder tickets with crisp scopes, parallel-safe write paths, and documented decisions."
compatibility: Repos that use `AGENTS.md`, `ROADMAP.md`, and `/tickets/*.md` as the control plane.
metadata:
  author: canonical
  version: "1.0"
---

## When to use this skill
- Anytime you need to create or revise a ticket.
- When existing tickets are too broad, collide on shared files, or lack clear outputs/acceptance criteria.

## Inputs you need
1) `AGENTS.md` and `ROADMAP.md` for repo-wide rules and the repo map.  
2) Any related tickets to avoid overlap or to link dependencies.  
3) Paths/folders the work will touch so you can define **allowed** vs **forbidden** write paths up front.
4) The executing agent: **EvoTicket Resolver** (default) or **EvoResearcher**. If EvoResearcher, also gather the report destination folder, research rounds, section count, and the prompt body (model is fixed to GPT-5.2 (H); do not add a model-selection field).

## Part A — Drafting the ticket (world-class prompt style)
1) **Anchor the goal.** Write one sentence on the user-visible outcome. Avoid bundling multiple deliverables.  
2) **Assign the agent.** Set `Agent: EvoTicket Resolver` unless deep research is required; for EvoResearcher tickets, include `Research output path`, `Research rounds`, and `Research sections`, and place the research prompt in the ticket body. Skip any model-selection field (fixed to GPT-5.2 (H)).  
3) **Define the outputs and acceptance.** List exact files (paths + formats) and objective checks (“contains at least X rows”, “links resolve”).  
4) **Carve the write boundary.**
   - Allowed paths must be **minimal, non-overlapping globs**. Keep them inside one country or area unless the work truly spans multiple scopes.
   - Forbidden paths must name protected files (`README.md`, `AGENTS.md`, `ROADMAP.md`, `skills/**` unless a structure ticket) and any shared assets not needed.
   - If many parallel tickets will touch a shared index/CSV/README, **split them**:
     - Create micro-tickets for each atomic task (e.g., 100 school profiles, each ticket only edits its profile file).
     - Create a separate “index/update” ticket that alone updates shared CSVs or index pages. This avoids 100 merge conflicts.
   - Declare country boundaries explicitly (e.g., allowed paths under `/countries/greece/**` only).
5) **Specify status + ownership metadata.**
   - Default new tickets to `Status: open` until an agent claims them.
   - Include `Priority`, `Type`, `Dependencies`, and claim fields (`Claimed-by`, `Claimed-at`) once work starts.
   - Reserve `Status: archived` for tickets that are deliberately retired, moved into `tickets/YYYYMM - Archived Tickets/`, and listed in `tickets/index.md` under the Archived section (separate from Closed/Done); use the ticket-archiving skill when doing so.
6) **Write the body like a prompt.**
   - **Context:** why this matters; links to upstream work.
   - **Task:** bullet the required actions only.
   - **Constraints & scope guards:** restate allowed/forbidden paths, country limits, and any “do not touch” items.
   - **Outputs + acceptance criteria:** copy from step 2; keep objective.
   - **Follow-up hooks:** reserve space for “Execution notes / Follow-up tickets” so agents know where to log decisions.

## Part B — Claiming and executing (fast loop)
- Before editing any scoped file, set `Status: in-progress`, add `Claimed-by` (branch or execution id), and timestamp `Claimed-at`.
- If you discover missing inputs or out-of-scope needs, write them under **Out of scope / follow-ups** instead of expanding the ticket mid-flight.

## Part C — Closing the ticket (document the learning)
1) Set `Status: done` and refresh `Last-updated`.  
2) Under “Execution notes” (or a short “What changed” block), capture:
   - Key decisions and their rationale.
   - Gaps, blockers, and how they were resolved (or remain open).
   - Links to outputs and any deviations from the original paths.
   - Suggested follow-up tickets, scoped narrowly with proposed allowed paths.
3) If the ticket created new shared artifacts (CSV/index), state whether a future batching ticket should reconcile or expand them.
4) Keep the ticket readable: concise bullets, no prose dumps, and explicit next steps.

## Quality checklist (use before saving)
- [ ] Goal and outputs are single-purpose and testable.
- [ ] `Agent` is set; EvoResearcher tickets list research rounds/sections/output path and include the prompt (no model-selection field).
- [ ] Allowed write paths are minimal, non-overlapping, and country-bounded.
- [ ] Forbidden paths list protected/control-plane files not needed for this ticket.
- [ ] Acceptance criteria are objective (counts, formats, link validity).
- [ ] Parallel-safety noted: shared index/CSV edits are isolated to a dedicated ticket.
- [ ] Claim metadata present when work starts; closure notes capture decisions and follow-ups.

## See also
- Pair this with `skills/roadmap-tickets/SKILL.md` for the canonical ticket schema.
- Use `skills/ticket-boundaries/SKILL.md` when executing to respect allowed paths.
