---
name: country-setup
description: "Layered ticket playbook to onboard a new country: scaffold directories, map stakeholders, and ticketize profiles safely."
compatibility: Repos using AGENTS.md + ROADMAP.md with country-first layout under `/countries/<country>/`.
metadata:
  author: evobuilder
  version: "1.0"
---

## When to use this skill
- You need to add a **new country namespace** and fill it with research/playbooks for UNIC and UNIC Athens.
- You must break the launch into **parallel-safe tickets** (scaffolding, discovery, profiling) without touching other countries.

## Inputs you need (preflight)
1) `AGENTS.md` + `ROADMAP.md` for repo rules and the country-first layout.  
2) The country name and ISO 2-letter code (for IDs, slugs, and folder names under `/countries/<country>/`).  
3) Any upstream tickets or dependencies (e.g., program positioning, ID governance, global data model).  
4) Existing global skills to reuse: `ticket-creation`, `ticket-boundaries`, `repo-conventions`, `id-governance`, `data-model-csvs-and-profiles`, `high-school-profile-template`, `schools-and-feeders`, `recognition-and-licensure`, `events-and-fairs`, `digital-measurement-and-benchmarks`, `program-clusters-and-competitor-sets`.

## Phase 1 — Preflight and scoping (before any edits)
- Confirm a **structure ticket** covers skills/roadmap changes if needed; country launches are structure-level work.
- Lock the **country folder name**: `/countries/<country-slug>/` (lowercase, hyphenated if multi-word). Keep campuses/global assets in `/UNIC/**`.
- Define **what stays out of scope** (other countries, global skills beyond this ticket). If any shared index/CSV must change, spin a separate ticket for it.
- Decide the **ID seed** (`<cc>` ISO2) for future entities; note it in ticket notes.

## Phase 2 — Scaffolding ticket (single-ownership)
Create one structure ticket to lay down the country shell only. Allowed paths should be limited to `/countries/<country>/**` plus the ticket file. Include:
- Directory tree: `entities/` (schools, agents, regulators, NGOs/SGOs, fairs/events, competitors), `market/`, `go-to-market/`, `program-clusters/`, `data/`, `reports/`, `skills/` (country-specific addenda only).
- Country README with map + contribution guardrails; link to country skills subtree.
- Empty or stub index files (no profiles yet) and a `reports/` placeholder noting reports vs. `executions/` runs.

## Phase 3 — Layered discovery & ticketization
Break work into **parallel-safe micro-tickets**. Each ticket must have narrow allowed paths under the country folder. Suggested stack:
- **Schools & feeders**
  - Ticket 1: `entities/schools/index` — school roster CSV/MD seed + sourcing plan; no profiles.
  - Ticket 2+: One ticket per **school profile** under `entities/schools/<slug>.md`, using `high-school-profile-template` and `id-governance` for deterministic IDs.
- **Education agents / partners**
  - Ticket 1: scan + roster under `entities/agents/` with source notes.
  - Ticket 2+: per-agent profiles or outreach briefs, one file per ticket.
- **Regulators / recognition & licensure bodies**
  - Ticket 1: landscape + authority list under `entities/regulators/` with pathways; follow `recognition-and-licensure` skill.
  - Ticket 2+: deep dives per authority if needed.
- **NGOs / SGOs / community orgs**
  - Ticket 1: mapping under `entities/ngos-sgos/` with mission, reach, relevance to recruiting.
- **Fairs & events**
  - Ticket 1: calendar seed in `entities/fairs-events/` + sourcing checklist.
  - Ticket 2+: per-event briefs or partner packs.
- **Digital benchmarks**
  - Ticket: channel + benchmark baselines in `go-to-market/digital/` using `digital-measurement-and-benchmarks` skill.
- **Program clusters & competitors**
  - Ticket 1: country cluster index in `program-clusters/` linked to `/UNIC/**` offerings.
  - Ticket 2+: per-competitor profiles under `entities/competitors/` (one ticket each) using `program-clusters-and-competitor-sets`.
- **Offerholder/yield & outreach playbooks**
  - Ticket(s): channel playbooks under `go-to-market/schools/`, `go-to-market/agents/`, and `go-to-market/offerholder-yield/` using relevant global skills.
- **Data & IDs**
  - Ticket: country data-model addendum in `skills/<country>-data-model-addendum` (country subtree) linking to the global data-model skill; add CSV schemas in `/countries/<country>/data/` if needed.

## Phase 4 — Ticket hygiene and boundaries
- Each ticket must list **Allowed write paths** inside `/countries/<country>/...` only; forbid `README.md`, `AGENTS.md`, `ROADMAP.md`, other countries, `.github/**`, and `skills/**` (unless a structure ticket for country skills addenda).
- If multiple tickets touch a shared index (school roster CSV, competitor list), create a **separate “index refresh” ticket** to avoid conflicts.
- Record **Claimed-by/Claimed-at** before editing; log deviations or blockers in execution notes.

## Phase 5 — Build order and execution tips
1) Run the **scaffolding ticket** first to create folders + README.
2) Start **rosters/index tickets** (schools, agents, regulators, events) to define scope and IDs.
3) Fan out **profile tickets** per entity to enable parallel execution.
4) Add **go-to-market playbooks** once core entities exist (schools/agents/regulators).
5) Close with **program clusters + competitor profiling** so positioning references real entities.
6) Keep **data/CSV work** in dedicated tickets to prevent schema collisions.

## Phase 6 — QA and closure before marking “done”
- Confirm all outputs live under `/countries/<country>/` and match the repo map (no stray files at root).
- Verify IDs/slugs follow `id-governance` and file naming is deterministic.
- Check cross-links: country README points to skills, indices, and UNIC shared materials without duplicating `/UNIC/**` content.
- Ensure required stakeholder groups are present (schools, agents, regulators, NGOs/SGOs, fairs/events, digital, competitors/program clusters).
- Tickets are closed with **execution notes** and follow-up tickets listed for remaining gaps.

## Quick ticket templates (copy/paste)
- **Scaffolding ticket (structure):** Allowed `countries/<country>/**` + this ticket; Forbidden global control plane; Outputs: directory tree + README + stub indices.
- **Roster ticket (content/data):** Allowed `countries/<country>/entities/<area>/**` + ticket; Outputs: index CSV/MD with source notes + assumptions; Acceptance: sourcing coverage % and ID pattern noted.
- **Profile ticket (content):** Allowed `countries/<country>/entities/<area>/<slug>.md` + ticket; Must use relevant template/skill; cite sources.
- **Index refresh ticket (qa/content):** Allowed specific index file path(s); Acceptance: links/IDs deduped, counts updated.

## See also
- `skills/ticket-creation` and `skills/ticket-boundaries` for writing/claiming tickets.
- `skills/repo-conventions` and `skills/markdown-authoring` for formatting and house style.
- `skills/id-governance` + `skills/data-model-csvs-and-profiles` for deterministic IDs and schema compliance.
