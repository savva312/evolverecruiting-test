# evolvebulgariarecruiting Roadmap: Multi-country recruiting

This file is the repo’s **plan + governance**. It answers:
- what this repo is trying to produce
- where things should live (repo map)
- how changes are allowed (change policy)
- what work is next (ticket queue)

**Work is executed via tickets** in `/tickets`.  
Agents and humans must follow `AGENTS.md`.

---

## 1) Mission

Build and maintain a high-quality, **country-first** repository that powers recruiting for **UNIC** and **UNIC Athens** across multiple markets (initially **Bulgaria**, **Nigeria**, **Greece**, and **Serbia**). The repo must stay:
Build and maintain a high-quality, **country-first** repository that powers recruiting for **UNIC** and **UNIC Athens** across multiple markets (initially **Bulgaria**, **Nigeria**, **Greece**, now adding **Romania**). The repo must stay:
- easy to navigate with clear scopes per ticket
- safe for parallel agent execution
- text-first and reviewable in PRs

---

## 2) Scope and non-goals

### In scope
- Creating/maintaining markdown documentation in `docs/` (or repo-specific folders)
- Creating/maintaining structured data in `data/` (if used)
- Creating reusable templates in `templates/` (if used)
- Adding indices/navigation pages so humans can find things quickly
- Ticketed refactors and improvements

### Out of scope (default)
- Storing secrets, credentials, API keys, or private tokens
- Storing personal data (PII) unless explicitly allowed and documented (default: **no**)
- Unbounded “cleanup refactors” not tied to a ticket
- Binary-first workflows (PDF/image/video) without a text extract plan

If a repo needs exceptions, add a **structure** ticket to document them and update this file.

---

## 3) Repo map (where content goes)

This is the **canonical layout** for this repo. Tickets must respect it.

### Control plane (always present)
- `README.md` — repo overview and how to use it
- `AGENTS.md` — operating rules for agents/humans
- `ROADMAP.md` — this file
- `tickets/projectmanager.md` — EvoManager automation control file (priorities, sprints, ticket-start budgets)
- `skills/` — reusable procedures and standards (global; e.g., `skills/id-governance` for deterministic IDs)
- `tickets/` — units of work and scope boundaries; archived tickets move into dated subfolders (`tickets/YYYYMM - Archived Tickets/`) and remain discoverable through `tickets/index.md` under an Archived section
- `executions/` — global agent run notes and intermediate artifacts (optional but recommended)

- Country directories live under `/countries/<country>/` (current set: `bulgaria`, `nigeria`, `greece`, `jordan`, `lebanon`, `romania`, `serbia`; extend via tickets).
- Each country directory contains its own research, data, and playbooks. Expected subfolders include:
  - `market/` — market research (mobility, affordability, education system, recognition/licensure)
  - `entities/` — schools, agents, regulators, NGOs/SGOs, fairs/events, competitors
  - `go-to-market/` — channel playbooks (schools, agents, digital, offerholder/yield)
  - `program-clusters/` — program-specific clusters with local competitors and positioning
  - `UNIC/` — campus-specific program inventories and positioning for UNIC Nicosia vs Athens (kept at repo root for all markets)
  - `data/` — structured data tied to the country
  - `reports/` — country reports (replacing the legacy research workspace path; interim run notes belong in `/executions/`)
- `/executions/**` is the global workspace for run logs; reports should be parked in `/countries/<country>/reports`.

### Common content areas (shared or country-scoped)
- `docs/` — human-readable documentation (global unless nested under a country)
- `data/` — structured machine-readable sources (global or country-specific when nested)
- `templates/` — reusable templates (letters, checklists, etc.)
- `scripts/` — small, auditable utilities (optional)
- `assets/` — source materials (binary allowed only with text-first guidance)
- `skills/` — global skills at root; country-specific skills live under each country namespace (e.g., `/countries/bulgaria/skills/`)

---

## 4) Change policy (how changes are allowed)

### Protected files/directories (default)
Unless a ticket is `Type: structure` and explicitly allows it, do not modify:
- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/README.md`

### Structure changes
Any of the following requires a `Type: structure` ticket:
- creating/renaming/removing top-level directories (including country directories under `/countries/`)
- changing conventions in the repo map (including adding new countries)
- changing the “protected files” policy
- moving/renaming many files (“refactor”)
- changing skills, ticket formats, or roadmap governance
- migrating content between country directories or between global and country scopes

Structure tickets must describe:
- what changes
- migration steps
- what links/indices must be updated

### Skills split
- Global skills live in `/skills/**` (rooted files apply to every country).
- Country-specific skills live in `/countries/<country>/skills/**` (e.g., `/countries/bulgaria/skills/**`, `/countries/nigeria/skills/**`, `/countries/greece/skills/**`) and must not leak into global skills.
- When introducing a new country, add a dedicated skills subtree under that country via a structure ticket.

### Ticket agent routing
- Every ticket must state the executing agent: **EvoTicket Resolver** (default) or **EvoResearcher**.
- EvoResearcher tickets must also specify the report destination folder, expected number of research rounds, and section count. The model is fixed to GPT-5.2 (H), and the ticket body itself is the prompt.

### Ticket lifecycle and archives
- Valid statuses now include `archived` in addition to `open`, `on-deck`, `in-progress`, `blocked`, `done`, and `dropped`.
- Archiving is a deliberate action governed by the ticket-archiving skill: set `Status: archived`, move tickets into `tickets/YYYYMM - Archived Tickets/`, and add the archive to `tickets/index.md` under an **archived** section separate from done/dropped.
- Keep active tickets (including `done`/`dropped`) in the root `tickets/` folder; only relocated tickets should carry the `archived` status.

### Runs triggered without a referenced ticket
- If an agent run starts without a ticket, create a new ticket immediately using the next available ID (see `tickets/index.md` or the folder listing), mark it `in-progress`, and commit that claim before other changes.
- Execute the work under that ticket, include the ticket file in the PR, and mark it `done` with a short summary in the same PR.
- All other ticket and scope rules remain unchanged.

---

## 5) Parallel work model

This repo supports **parallel EvoBuilder runs**.

Rule: parallel work is safe if each run executes tickets with **non-overlapping `Allowed write paths`**.

Examples:
- Ticket A allowed: `docs/region-a/**`
- Ticket B allowed: `docs/region-b/**`
These can run in parallel safely.

**Automation cadence:** An EvoManager process runs exactly every 30 minutes on UTC boundaries (EventBridge). It reads `tickets/projectmanager.md`, reviews ticket states, and opens/closes tickets. Per epoch, it may place at most **200 tickets** into `on-deck` (whether newly created or reclassified). EvoManager is never assigned regular tickets and must not interfere with in-progress tickets.

If you see repeated collisions, add a structure ticket to improve boundaries.

---

## 6) Definition of done (DoD)

“Done” for this repo means:

### Control plane is stable
- `README.md`, `AGENTS.md`, `ROADMAP.md` exist and are consistent
- `skills/` contains the minimal working set for this repo
- tickets are using the canonical format and scopes

### Content completeness (repo-specific)
Define what “complete” means for this topic, e.g.:
- required indices exist (entry pages, topic map)
- core docs/data exist for each workstream
- navigation links resolve and don’t 404 inside the repo
- P0 + P1 tickets are completed or intentionally dropped

### Operational cleanliness
- no changes outside ticket scopes
- no secrets / private tokens committed
- PRs remain reviewable (avoid huge unscoped diffs)

---

## 7) Workstreams (optional but recommended)

Use workstreams to keep work separable.

- **W1 Docs**: `docs/**`
- **W2 Data**: `data/**`
- **W3 Templates**: `templates/**`
- **W4 Indices/Navigation**: usually `docs/index.md` or root-level indexes
- **W5 Automation** (optional): `scripts/**`, `.github/**`

---

## 8) Ticket queue

This is the prioritized queue. Each entry must correspond to a ticket file under `/tickets`.

### P0 — Must do
- T-017 — Multi-country control plane update
- T-018 — Country migration ticket scaffolding
- T-019 — Bulgaria migration to country-first layout
- T-020 — Global skills split
- T-021 — Nigeria migration to country-first layout
- T-022 — Greece migration to country-first layout
- T-023 — Post-migration cross-link cleanup
- T-024 — Multi-country migration QA

### P1 — Next
- T-006 — Bulgaria outbound mobility baseline
- T-007 — Priority Sofia/Plovdiv school profiles
- T-008 — Bulgaria education agents scan
- T-009 — Medicine/MD competitor set for Bulgaria
- T-010 — Digital channel benchmark pack (Bulgaria)
- T-011 — School outreach playbook v1
- T-012 — Offerholder/yield workflows for Bulgaria
- T-013 — UNIC program positioning: Nicosia vs Athens
- T-015 — Scholarships/discounts landscape (Bulgaria)

### P2 — Later
- T-014 — Data dictionary + field standards for CSVs

### Blocked
- (none)

--- 

## 9) Decisions log (optional)

If the repo accumulates repeated “why” decisions, either:
- add short entries here, or
- create `DECISIONS.md` via a structure ticket.

Format suggestion:
- `YYYY-MM-DD — Decision — Rationale — Links`
