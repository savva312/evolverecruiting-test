# Agent Operating Rules (EvoBuilder) 

This repository is designed to be operated by **EvoBuilder** and other LLM agents (multiple providers/models). 
These rules exist to ensure safe, deterministic progress and enable parallel work without collisions.

**Substantive focus:** assemble a complete recruiting plan for **UNIC** and **UNIC Athens** across multiple countries (current markets: **Bulgaria**, **Nigeria**, **Greece**, **Jordan**, **Lebanon**, **Romania**, **Serbia**), expanding to **all relevant countries** over time. Each country should have its own subtree with research, data, and playbooks to source, convert, and onboard students for both campuses, covering every stakeholder group involved in international recruiting.

**Stakeholder scope:** schools and counselors, education agents and partners, government regulators and recognition/licensure bodies, NGOs/SGOs and community organizations, fairs/events, digital channels, and employer/industry linkages when relevant to program positioning.

If anything below conflicts with a ticket, the ticket must be updated via a structure ticket.

---

## 1) Source of truth

The repo’s operating system is:

1. [`AGENTS.md`](AGENTS.md) — global rules (this file)
2. [`ROADMAP.md`](ROADMAP.md) — repo plan + governance + repo map
3. Tickets in [`/tickets`](tickets/) — execution units and scope boundaries
4. [`tickets/projectmanager.md`](tickets/projectmanager.md) — EvoManager automation priorities, sprint tracker, and ticket-budget governance
5. Reusable procedures in [`/skills`](skills/) — “how” to do common work consistently

Agents must read **AGENTS + ROADMAP + the ticket(s)** before writing.

---

## 2) Core operating model

### Ticket-driven execution
Agents do not “improve the repo generally.”
Agents execute **tickets**.

A ticket defines:
- what to create/update
- where writing is allowed
- what is forbidden
- how success is verified
- which agent is responsible for execution

### Parallel safety
Multiple runs may happen in parallel if:
- each run claims distinct tickets
- claimed tickets have **non-overlapping allowed write paths**
- shared files are only edited by a structure ticket

### Agents (who runs tickets)
- **EvoTicket Resolver** — default single-round GPT-5.1/5.2 Codex agent for most tickets.
- **EvoResearcher** — multi-round GPT-5.2 (H) agent for deep research/reporting tickets. EvoResearcher tickets must name the report destination folder, required research rounds, and section count; the ticket body doubles as the prompt. Do **not** include model-selection fields (model is fixed).
- **EvoManager** — automation that runs exactly every 30 minutes on UTC boundaries (EventBridge). It is never assigned regular tickets; it only reads `tickets/projectmanager.md`, reviews ticket states, and opens/closes tickets. Per epoch, EvoManager may place at most **200 tickets** into `on-deck` (whether newly created or reclassified) and should not violate ticket scopes or reassign in-progress tickets.

---

## 3) Always-on constraints

### 3.0 Country-first layout (hard rule)
- Country directories live under `/countries/<country>/` (current markets: `bulgaria`, `nigeria`, `greece`, `jordan`, `lebanon`, `romania`, `serbia`; expandable via tickets as new markets come online).
- Country content (market, entities, go-to-market, program clusters, UNIC positioning, reports) lives under its country directory (e.g., `/countries/bulgaria/program-clusters`, `/countries/greece/reports`).
- Campus content shared across markets (e.g., UNIC Nicosia and UNIC Athens program materials) lives at root `/UNIC/**` and should be referenced by each country rather than duplicated inside country folders.
- `/executions/**` is the global workspace for EvoBuilder run logs; country reports belong under `/countries/<country>/reports`.

### 3.1 Scope enforcement (hard rule)
When executing a ticket, an agent:

- **MUST write only** within that ticket’s `Allowed write paths`
- **MUST NOT write** within the ticket’s `Forbidden write paths`
- Respect country boundaries: do not interleave edits across countries unless the ticket explicitly spans them.

If work is needed outside scope:
- do not do it
- add a short note in `executions/` (see “Execution notes”)
- propose a new ticket (or mark the current ticket blocked)

### 3.2 Protected files (default)
Unless a ticket is `Type: structure` and explicitly allows it, agents must not modify:

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/README.md` (if present)

(Regular tickets generally should not change the control plane.)

### 3.3 Text-only expectation
Unless a ticket explicitly states otherwise, agents should assume **text-only understanding**.

- Use `.md`, `.txt`, `.yml/.yaml`, `.json`, `.csv`
- If a binary source (PDF/image) must be used, the repo should also contain a text extract.
  - If no extract exists, propose a ticket to add one.

### 3.4 Skills split (hard rule)
- Global skills live in `/skills/**` and apply to every country.
- Country-specific skills live inside each country namespace (e.g., `/countries/bulgaria/skills/**`, `/countries/nigeria/skills/**`, `/countries/greece/skills/**`); do not mix country procedures into global skill files.
- When adding skills, decide whether guidance is global or country-scoped and place it accordingly.

### 3.5 Stakeholder coverage (hard rule)
- Within each country scope, capture and maintain materials for the full recruiting ecosystem: feeder schools/counselors, education agents, regulators/licensure/recognition bodies, NGOs/SGOs, fairs/events, digital channels/benchmarks, and employer or industry partners where relevant.
- Do not defer stakeholder coverage to “later” without a ticketed plan; add tickets when new stakeholder groups need to be incorporated.

---

## 4) Ticket lifecycle and claiming

### 4.1 Ticket statuses
Tickets use one of:

- `open` — available
- `on-deck` — prioritized by EvoManager for the current epoch (max 200 combined newly created or reclassified per epoch)
- `in-progress` — claimed by a run
- `blocked` — cannot proceed (must state why)
- `done` — completed and merged
- `dropped` — intentionally abandoned
- `archived` — deliberately retired and moved into a monthly archive folder (see Archiving); must not be edited unless re-opened via a new ticket

### 4.2 Claiming a ticket (prevents collisions)
Before doing substantive work on a ticket, the agent should:

1. Update that ticket file:
   - set `Status: in-progress`
   - set `Claimed-by: {execution_id or branch}`
   - set `Claimed-at: {timestamp}`

2. Commit that change early in the PR.

If the repo policy forbids editing tickets, the repo is not configured for safe parallel runs; create a structure ticket to fix this.

#### If a run starts without a referenced ticket
- Immediately create a new ticket using the next available ID (see `tickets/index.md` or the numbering pattern in `/tickets`), set it to `in-progress`, and commit that claim before making other changes.
- Execute the work under that ticket, include the ticket file in the PR, and mark it `done` (with a short “What changed”) before merging.
- All other ticket rules and scope boundaries still apply.

### 4.3 Completing a ticket
When a ticket is complete:
- update ticket to `Status: done`
- include a short “What changed” note in the ticket (or a linked execution note)
- ensure required outputs and acceptance criteria are satisfied

### 4.4 Archiving tickets (explicit action only)

- Archiving is not automatic; it requires an explicit run using the **ticket-archiving** skill.
- Archive folders live under `/tickets/` and are named `YYYYMM - Archived Tickets/` (e.g., `tickets/202512 - Archived Tickets/`).
- To archive a ticket or range:
  - Set `Status: archived` in the ticket(s).
  - Move the ticket files into the correct monthly archive folder.
  - Update `tickets/index.md` to include the archive under an **archived** section (separate from done/dropped).
  - Keep `done`/`dropped` for active folder tickets; only use `archived` when tickets are relocated into the monthly archive.

---

## 5) Canonical ticket format (repo-agnostic)

Tickets are markdown files under `tickets/`, named like:

- `tickets/T-001-<short-slug>.md`

Each ticket should include the following fields (exact syntax can vary, but content must exist):

- `Status: open|in-progress|blocked|done|dropped`
- `Type: content|data|integration|structure|qa`
- `Priority: P0|P1|P2|P3`
- `Agent: EvoTicket Resolver|EvoResearcher`
- If `Agent: EvoResearcher`, also include:
  - `Research output path:` destination folder in the repo for the report deliverable(s)
  - `Research rounds:` integer count of research cycles
  - `Research sections:` integer count of report sections
- `Allowed write paths:` list of repo globs
- `Forbidden write paths:` list of repo globs
- `Required outputs:` explicit file paths expected to be created/updated
- `Acceptance criteria:` objective checks
- `Dependencies:` optional
- `Notes/Context:` optional
  
Additional guardrails:
- EvoResearcher tickets use GPT-5.2 (H) by default; do not add model-selection fields.
- The EvoResearcher ticket body should contain the actual prompt for the run (beyond the parameter fields above).

If a ticket is missing any of these, the agent should either:
- fix the ticket (if allowed), or
- mark it blocked and propose a ticket to correct it

---

## 6) ROADMAP expectations

`ROADMAP.md` should contain:

- Repo scope and non-goals
- Repo map (where content belongs)
- Change policy (especially structure changes)
- Ticket queue (P0/P1/P2/Blocked)
- Definition of Done for the repo

Agents should treat ROADMAP as the “plan” and tickets as “the work”.

---

## 7) Execution notes (recommended)

Agents may write run notes under:

- `executions/`

Common patterns:
- `executions/{execution_id}/notes.md`
- `executions/{execution_id}/ticket_T-001.md`

Execution notes should be:
- short
- factual
- focused on decisions, blockers, and references used
- never include secrets or PII

---

## 8) Writing and quality bar

- Prefer small, composable markdown files over huge monoliths.
- Minimize boilerplate; every section should add value.
- Use clear headings, stable filenames, and relative links.
- Do not introduce speculative content as fact; label assumptions.
- Keep diffs reviewable.

---

## 9) Structure changes protocol

Any of the following requires a `Type: structure` ticket:

- creating/renaming/removing top-level directories
- changing the repo map conventions
- editing `README.md`, `AGENTS.md`, or `ROADMAP.md`
- changing `skills/**`
- moving large sets of files

Structure tickets must:
- describe the migration plan
- list exactly what moves/renames occur
- update `ROADMAP.md` repo map accordingly

---

## 10) Default “do not do” list

Agents must not:
- write outside ticket scopes
- refactor “for cleanliness” without a structure ticket
- delete content unless explicitly required by a ticket
- add secrets, private tokens, credentials, or personal data to the repo
- fabricate citations or sources

---

## 11) How EvoBuilder should interpret “sections” 

If EvoBuilder is configured with `(y)` “sections”, interpret that as: 

- **one section ≈ one ticket executed**
- sections should produce **repo file changes**, not a single giant report
- any “final report” should be optional and ticket-scoped (e.g., an index page), not the default


---
