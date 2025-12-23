# T-007: Establish roadmap and initial ticket backlog

Status: archived
Type: structure
Priority: P0
Dependencies: (none)
Claimed-by: assistant
Claimed-at: 2025-12-20T14:55:16Z
Last-updated: 2025-12-20
Completed-at: 2025-12-20T14:55:16Z

---

## Goal

Refresh the repo roadmap around UNIC and UNIC Athens recruiting from Bulgaria and create a set of narrow, research-heavy tickets to begin populating the scaffolding.

---

## Context

- The repo currently has empty scaffolding across `market/`, `entities/`, `go-to-market/`, `program-clusters/`, `UNIC/`, and `data/`.
- Roadmap queue is empty; we need a sequenced backlog that respects scope boundaries for parallel runs.
- Tickets should favor focused scopes so EvoBuilder runs can invest deeply in each area without collisions.

---

## Allowed write paths

- `ROADMAP.md`
- `tickets/**`
- `research/**` (optional notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `skills/**`
- `.github/**`
- `scripts/**`
- `data/**` (except if explicitly required by a new ticket being created)
- `program-clusters/**` (except if explicitly required by a new ticket being created)
- `entities/**` (except if explicitly required by a new ticket being created)
- `go-to-market/**` (except if explicitly required by a new ticket being created)
- `UNIC/**` (except if explicitly required by a new ticket being created)

---

## Required outputs

- Updated `ROADMAP.md` with a mission tuned to UNIC + UNIC Athens from Bulgaria, workstreams, and a populated ticket queue.
- New tickets created and scoped for the first wave of repo population, with clear allowed write paths and acceptance criteria.
- Ticket index updated if helpful for navigation (optional).
- This ticket marked `done` with a brief “what changed” note when complete.

---

## Acceptance criteria

- Roadmap reflects the recruiting mission, repo map, and a prioritized queue of new tickets with IDs and priorities.
- At least 6–8 new tickets are added with narrow scopes, strong allowed/forbidden paths, required outputs, and acceptance criteria.
- Ticket numbering remains sequential with existing files, and statuses are `open` for new work.
- No protected files outside the allowed paths are modified.
- `Status`, `Claimed-by`, and timestamps in this ticket are accurate; status set to `done` upon completion.

---

## Notes/Context

Focus tickets on initial market baselines, priority entities, early go-to-market playbooks, and program-cluster competitor scans so later runs can dive deep with clear boundaries.

What changed: Updated ROADMAP mission and queue; added tickets T-006 through T-015 with narrow scopes for market baselines, entities, program clusters, go-to-market, data standards, and affordability.
