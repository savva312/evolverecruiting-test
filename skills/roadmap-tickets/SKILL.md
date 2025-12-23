---
name: roadmap-tickets
description: How to structure ROADMAP.md and /tickets/*.md for EvoBuilder repos, including required ticket frontmatter fields, statuses, agent routing, outputs, and how to run parallel agents safely.
compatibility: Repos that want deterministic, ticket-driven agent work.
metadata:
  author: canonical
  version: "1.0"
---

## ROADMAP.md purpose
ROADMAP.md is the single place that explains:
- what exists now (map of key folders)
- what “done” means for this repo
- milestones (phases) and their acceptance criteria
- the ticket system and how parallelization works

ROADMAP.md should link to:
- active tickets
- key “index” docs (if any)
- any conventions unique to this repo’s subject matter

## Ticket files purpose
Each ticket is a **self-contained instruction contract**:
- scope (what to do)
- boundaries (where you may write)
- outputs (what files must exist after completion)
- agent routing (EvoTicket Resolver vs EvoResearcher) and, when relevant, research metadata
- For step-by-step drafting, pair this file with `skills/ticket-creation/SKILL.md`, which walks through writing, claiming, and closing tickets with documented decisions and follow-ups.

## Canonical ticket format (frontmatter + body)

### Required frontmatter fields
Use YAML frontmatter at the top of each ticket:

- `id` (string): stable ticket id, e.g. `T-012`
- `title` (string)
- `status`: `todo | on_deck | in_progress | blocked | done | dropped | archived` (maps to `Status` in ticket bodies)
- `priority`: `p0 | p1 | p2 | p3`
- `agent`: `evoticket_resolver | evoresearcher`
- `allowed_write_paths`: list of glob-like paths (relative), e.g.
  - `docs/countries/es/**`
  - `data/schools/es.yml`
- `outputs`: list of file paths expected at completion
- `created_at` / `updated_at`: ISO timestamps

If `agent: evoresearcher`, also include:
- `research_output_path`: folder path in the repo where the report will be saved
- `research_rounds`: integer count of research iterations
- `research_sections`: integer section count for the final report

Agent selection guidance:
- **evoticket_resolver** — default single-round GPT-5.1/5.2 Codex agent for most tasks.
- **evoresearcher** — multi-round GPT-5.2 (H) agent for deep research; use only when a structured research report is required.

Archived tickets:
- Use `archived` only after a deliberate retirement: set the status, move the ticket into `tickets/YYYYMM - Archived Tickets/`, and record it in `tickets/index.md` under an Archived section separate from Closed/Done.

Do **not** include model-selection fields for EvoResearcher tickets (model is fixed to GPT-5.2 (H)), and the ticket body should contain the research prompt itself.

### Recommended frontmatter fields
- `claimed_by`, `claimed_at` (for parallel runs)
- `depends_on`: list of ticket ids
- `inputs`: links/paths to relevant repo docs
- `definition_of_done`: short checklist

### Ticket body sections (recommended)
- Context
- Task
- Constraints & boundaries
- Outputs
- Notes / follow-ups

## Parallelization rules
Parallel runs work when:
- tickets have **non-overlapping `allowed_write_paths`**
- each agent claims a ticket before editing
- cross-cutting edits happen via dedicated tickets (not “drive-by” changes)

### Drafting parallel-safe tickets (conflict minimization)
- Keep each ticket single-purpose with explicit outputs and acceptance criteria.
- Make allowed paths as narrow as possible, and list forbidden paths for protected or shared files.
- If multiple tickets would touch a shared index/CSV/README, split work:
  - micro-tickets for the atomic tasks (e.g., 100 school profiles, each editing only its file)
  - one aggregator ticket that alone updates the shared index/CSV to avoid merge churn
- Require claim metadata (`Status: in-progress`, `Claimed-by`, `Claimed-at`) before edits start.
- At close-out, log key decisions, learnings, blockers, and proposed follow-up tickets directly in the ticket to keep history reviewable.
