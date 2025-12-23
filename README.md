# evolverecruiting: Global Enrollment Management for UNIC Nicosia & UNIC Athens

This repository is a **multi-country operating system** for **Global Enrollment Management** serving **UNIC Nicosia** and **UNIC Athens**. It is maintained by humans and automated agent runs (EvoBuilder) using a **ticket-driven workflow**.

## Purpose and scope

Build and maintain a country-first **global enrollment management** strategy for UNIC Nicosia and UNIC Athens across current and future markets. The repo enforces a consistent, top-level country layout so each market has its own reports, playbooks, and data while sharing global guidance and campus positioning. Content should support the full funnel—from awareness and pipeline build to application, admission, and yield—for both campuses, expanding over time to cover **all countries and all stakeholder groups** relevant to international recruiting.

## Navigation (start here)

- **Control plane:** [`AGENTS.md`](AGENTS.md) (operating rules), [`ROADMAP.md`](ROADMAP.md) (plan/queue), [`README.md`](README.md) (you are here)
- **Tickets:** browse or create scoped work in [`/tickets`](tickets/)
- **Automation control:** [`tickets/projectmanager.md`](tickets/projectmanager.md) for the EvoManager scheduler (priorities, sprints, ticket budgets)
- **Countries:** country-first content under [`/countries`](countries/) for `bulgaria`, `nigeria`, `greece`, `jordan`, `lebanon`, `romania`, `serbia` (expandable via tickets)
- **Shared campuses:** [`/UNIC`](UNIC/) for UNIC Nicosia and UNIC Athens source material referenced by every country
- **Skills:** global procedures in [`/skills`](skills/) plus any country-scoped skills under `/countries/<country>/skills/`
- **Runs/logs:** EvoBuilder run notes in [`/executions`](executions/); country reports live in `/countries/<country>/reports/`

## How work happens in this repo

All substantive work is done via **tickets**:

- The **work queue and sequencing** lives in [`ROADMAP.md`](ROADMAP.md).
- Each unit of work is a file in [`/tickets`](tickets/).
- Agents must follow the rules in [`AGENTS.md`](AGENTS.md).
- Reusable repo procedures live in [`/skills`](skills/).
- Tickets must declare which agent will execute them:
  - **EvoTicket Resolver** — default single-round GPT-5.1/5.2 Codex agent for most tickets.
  - **EvoResearcher** — multi-round GPT-5.2 (H) agent for deep research reports. EvoResearcher tickets must also state the report destination folder, required research rounds, and section count; the ticket body doubles as the prompt, and the model is fixed (no model selection field).

> If you want something added/changed, create or update a ticket. If a run is triggered without a referenced ticket, immediately create a new ticket with the next available ID, commit the claim, and include the ticket (marked done) in the PR alongside the work.

**Automation:** An EvoManager process runs exactly every 30 minutes on UTC boundaries (00 and 30 past the hour). It reads [`tickets/projectmanager.md`](tickets/projectmanager.md), reviews ticket states, and opens/closes tickets to steer the next epoch. EvoManager is never assigned regular tickets; it only manages ticket inventory and may place up to **200 tickets per epoch** into `on-deck` (whether newly created or reclassified).

## Repo control plane (always present)

These files/folders define how the repo is operated:

- [`README.md`](README.md) — what this repo is and how to use it
- [`AGENTS.md`](AGENTS.md) — operating rules for agents and humans
- [`ROADMAP.md`](ROADMAP.md) — the prioritized plan and governance
- [`tickets/projectmanager.md`](tickets/projectmanager.md) — EvoManager control file (priorities, sprints, ticket-start budgets)
- [`/tickets`](tickets/) — atomic work items (scope boundaries)
- [`/skills`](skills/) — reusable procedures and standards
- [`/executions`](executions/) — global EvoBuilder run workspace (notes/logs). `executions/**` is the home for run logs (current staging: `/executions/202512 runs/`); country reports live under `/countries/<country>/reports` (e.g., `/countries/bulgaria/reports`).

## Country-first layout

This repo is **country-first**. Each market lives under `/countries/<country>/` (e.g., `/countries/bulgaria/**`, `/countries/nigeria/**`, `/countries/greece/**`, `/countries/jordan/**`, `/countries/lebanon/**`, `/countries/romania/**`, `/countries/serbia/**`), and the set can expand as new countries are added. Each country directory should contain its own research, entities, go-to-market playbooks, program clusters, and campus positioning (e.g., `program-clusters/`, `entities/`, `go-to-market/`, `UNIC/`, `data/`, `reports/`). Country reports that once sat in the legacy research workspace should be relocated into the relevant `/countries/<country>/reports` folder, and interim run notes should be stored in `/executions/`. Shared campus content for **UNIC Nicosia** and **UNIC Athens** lives at the root `/UNIC/**` directory so all markets can reference a single source of truth.

### Stakeholder coverage (international recruiting)

Each country’s materials should eventually address all relevant stakeholder groups across the recruiting funnel, including:

- Secondary schools, counselors, and other premium feeders
- Education agents and channel partners
- Government regulators, recognition/licensure bodies, and accreditation agencies
- NGOs/SGOs and community organizations
- Events and fairs (national, regional, and school-level)
- Digital channels, campaigns, and performance/measurement standards
- Employer/industry connections when relevant to program positioning

Global, non-country content remains at the root when explicitly needed; otherwise, default to country scopes.

Common supporting folders (used either globally or within each country) include:

- `docs/` — human-readable documents
- `data/` — structured machine-readable data (YAML/JSON/CSV)
- `templates/` — reusable templates (letters, checklists, etc.)
- `scripts/` — small, auditable utilities (optional)
- `assets/` — source materials (see “Text-only” note below)

The authoritative map for **this repo** should be described in `ROADMAP.md` under “Repo map”.

## Skills

Reusable “how we work here” guidance lives in [`/skills`](skills/).
At minimum, expect these skills (names may vary but intent should not):

- Ticket format & lifecycle
- Scope boundaries and safe editing
- Structure changes protocol
- Writing/style conventions
- (Optional) Asset handling and citation practices

Skill locations:

- Global skills: `/skills/**` (top-level files that apply to every country)
- Country-specific skills: `/countries/<country>/skills/**` inside each market (e.g., `/countries/bulgaria/skills/` for Bulgaria-only procedures)

If a skill is missing, add a ticket to create it rather than improvising.

## Tickets

Tickets are the unit of execution for both humans and agents.

- Browse open work: [`/tickets`](tickets/)
- Canonical queue / priority: [`ROADMAP.md`](ROADMAP.md)
- Ticket statuses: `open`, `on-deck`, `in-progress`, `blocked`, `done`, `dropped`, and `archived`. Archived tickets are deliberately retired items that have `Status: archived`, live in dated subfolders under `/tickets/` named `YYYYMM - Archived Tickets/` (e.g., `tickets/202512 - Archived Tickets/`), and are tracked in `tickets/index.md` under an archived section distinct from done/dropped.
- Use the ticket-archiving skill for any archive action so status changes, folder moves, and index updates happen together.

**Parallel runs:** this repo supports multiple concurrent agent runs **as long as** they claim tickets with **non-overlapping write scopes** (defined inside each ticket).

## Execution philosophy: speed, scale, and auto-merge

- **Massive parallelism + extreme speed:** Bias for many agents running at once across distinct ticket scopes to keep work moving across countries and stakeholders.
- **Go broad first, clean later:** Favour wide, parallel passes to land coverage quickly; defer refactors/polish to follow-on tickets as long as outputs stay within ticket scopes.
- **Auto-merge to maintain pace:** Auto-merging (including safe auto-resolution of text conflicts) is expected so long as ticket scopes are respected; text-first workflows make small errors visible and easy to fix in subsequent cleanup tickets.

## Text-only constraint (important)

EvoBuilder runs for this repo should assume **text-first inputs**.

- Preferred repo-native formats: `.md`, `.txt`, `.yml`, `.yaml`, `.json`, `.csv`
- Avoid relying on agents to interpret binary files directly (PDFs/images/videos) unless the workflow explicitly supports it.

If you must keep binaries (e.g., PDFs) for reference, also include a **text extract** alongside them (e.g., `assets/extracts/<name>.md`) so text-only runs can use the content.

## Quickstart

1. Read [`ROADMAP.md`](ROADMAP.md) and pick a ticket from [`/tickets`](tickets/).
2. Claim the ticket by setting `Status: in-progress`, `Claimed-by`, and `Claimed-at`, then commit that claim before changing other files. Ensure the ticket names the executing agent; if it is an **EvoResearcher** ticket, confirm it includes the report destination folder plus research rounds and section count.
3. Verify the ticket lists **allowed write paths**, **forbidden write paths**, **required outputs**, and **acceptance criteria**; do not edit protected files (`README.md`, `AGENTS.md`, `ROADMAP.md`, `skills/**`) without a structure ticket. EvoResearcher tickets should treat the ticket body as the research prompt and should not override the fixed GPT-5.2 (H) model.
4. Keep work inside the ticket’s scope and within a single country unless explicitly permitted; use `/executions/**` for run notes and `/countries/<country>/reports/` for reports.
5. Run EvoBuilder for one or more tickets (see `AGENTS.md` for execution rules).
6. Review the PR, merge, and mark tickets done.

## Contributing

- Keep changes ticket-scoped.
- Respect allowed/forbidden paths and country scopes defined in each ticket; parallel runs are safe only when scopes do not overlap.
- Do not refactor repo structure or touch protected files unless executing a **structure** ticket (see `AGENTS.md`).
- Prefer small, reviewable PRs and keep navigation links current (especially country directories, `/UNIC`, `/skills`, and `/executions`).

## Markdown formatting (canonicalization)

Keep Markdown files aligned with the repo’s canonical formatting (heading spacing, `-` bullets with two-space indents, trailing whitespace removal, collapsed blank lines, single EOF newline).

- **Fix in-place (auto-discover changed Markdown; default behavior):** `python scripts/canonicalize_md.py`
- **Explicit fix:** `python scripts/canonicalize_md.py --fix README.md scripts/README.md`
- **Check without writing:** `python scripts/canonicalize_md.py --check`
- New/untracked files are not auto-discovered; pass their paths explicitly.

An optional pre-commit hook is available in `.pre-commit-config.yaml`:

```bash
pip install pre-commit
pre-commit install
pre-commit run canonicalize-markdown --all-files  # or --files path/to/file.md
```
