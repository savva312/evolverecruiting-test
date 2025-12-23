# Tickets

Tickets are the **unit of work** for this repo.
- an automation control file (`projectmanager.md`) used by the EvoManager scheduler to open/close tickets every 30 minutes (UTC) and place up to 200 tickets per epoch into `on-deck`
Each ticket must include:

- `Status: open | on-deck | in-progress | blocked | done | dropped | archived`
- **on-deck**: prioritized by EvoManager for the current 30-minute epoch (combined cap of 200 per epoch across newly created or reclassified tickets)
If a run is triggered without a referenced ticket, the first action should be to create a new ticket with the next available ID, set it to `in-progress`, and commit that claim before any other changes. The ticket must be included in the PR and marked `done` with a brief summary.

This folder enables:
- safe parallel agent runs
- clear boundaries on where agents can write
- reviewable PRs with objective acceptance criteria
- explicit routing to the right agent (EvoTicket Resolver or EvoResearcher)

See also: `AGENTS.md` for global operating rules.

---

## 1) Ticket naming

Each ticket is a markdown file:

- `tickets/T-001-short-slug.md`

Rules:
- unique ID (`T-###`)
- short, stable slug
- one ticket = one coherent deliverable

---

## 2) Ticket lifecycle (status)

Each ticket must include:

- `Status: open | on-deck | in-progress | blocked | done | dropped | archived`

Meaning:
- **open**: available to execute
- **on-deck**: prioritized for the current EvoManager epoch
- **in-progress**: claimed by a run
- **blocked**: cannot proceed (must state why)
- **done**: completed and merged
- **dropped**: intentionally abandoned (with rationale)
- **archived**: deliberately retired, status updated, moved into a dated archive folder under `/tickets/` (`YYYYMM - Archived Tickets/`), and listed in `tickets/index.md` under **archived** (separate from done/dropped)

---

## 3) Agent routing (required)

Each ticket must state which agent should run it:

- **EvoTicket Resolver** — default single-round GPT-5.1/5.2 Codex agent for general tickets.
- **EvoResearcher** — multi-round GPT-5.2 (H) agent for deep research/reporting.

If `Agent: EvoResearcher`, also include:

- `Research output path`: folder in the repo where the final report will be saved
- `Research rounds`: integer number of research iterations
- `Research sections`: integer number of sections expected in the report
- The ticket body should contain the research prompt itself. Do **not** include a model-selection field (model is fixed to GPT-5.2 (H)).

---

## 4) Claiming tickets (required for parallel runs)

Before making substantive changes, the executing run should:

1. Set `Status: in-progress`
2. Set `Claimed-by: {execution_id or branch}`
3. Set `Claimed-at: {timestamp}`

Commit the claim early.

This provides a lightweight lock so parallel runs don’t collide.

---

## 5) Ticket types

Each ticket must include a type:

- `Type: content | data | integration | structure | qa`

Guidance:
- **content**: write or update docs
- **data**: add/update YAML/JSON/CSV + schemas if applicable
- **integration**: connect pieces (indices, navigation, cross-links)
- **structure**: repo map changes, protected file edits, refactors
- **qa**: audits, consistency checks, link fixes, formatting passes

---

## 6) Scope boundaries (the most important field)

Each ticket must define:

### Allowed write paths
A list of file globs where the agent is allowed to write.

### Forbidden write paths
A list of file globs that must not be modified.

If work is needed outside allowed scope:
- do not do it
- mark the ticket blocked OR propose a follow-up ticket

Parallelism depends on these boundaries being clean and non-overlapping.

---

## 7) Required outputs and acceptance criteria

Every ticket must include:

- **Required outputs**: exact file paths expected to be created/updated
- **Acceptance criteria**: objective checks a reviewer can validate

Avoid subjective “good quality” criteria; prefer checkable outcomes.

---

## 8) Archiving tickets (explicit action)

- Archive folders live under `/tickets/` and follow `YYYYMM - Archived Tickets/` naming (e.g., `tickets/202512 - Archived Tickets/`).
- To archive tickets, use the ticket-archiving skill: set `Status: archived`, move the ticket file(s) into the correct monthly archive folder, and add the archive to `tickets/index.md` under the **archived** section (separate from done/dropped).
- Keep active `open`/`on-deck`/`in-progress`/`blocked`/`done`/`dropped` tickets in the root `tickets/` folder.

---

## 9) Execution notes (recommended)

If the run needs to leave a trace of decisions or research, write to:

- `executions/{execution_id}/...`

Execution notes are optional and should be short and factual.

---

## 10) Template

Use: `tickets/T-000-template.md`

Copy it and fill it in for new tickets.
