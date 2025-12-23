# T-444: Ticket archiving control-plane update

Status: done
Type: structure
Priority: P0
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-22T16:59:37Z
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Add an `archived` ticket status, define the monthly archive folder structure, and create a repeatable skill for moving archived tickets. As part of this ticket, move tickets **T-001 through T-100** into the December archive, update their status to `archived`, and refresh index and control-plane docs to reflect the new lifecycle and navigation.

---

## Context

- Repo control-plane docs (AGENTS, README, ROADMAP, tickets/README) currently recognize only open/on-deck/in-progress/blocked/done/dropped.
- Tickets should gain an explicit archive lifecycle with monthly subfolders (e.g., `tickets/202512 - Archived Tickets/`).
- Archiving must be an intentional action (skill-driven) that relocates tickets and updates the index.

---

## Allowed write paths

- `AGENTS.md`
- `README.md`
- `ROADMAP.md`
- `tickets/**`
- `skills/**`
- `executions/**` (optional for notes)

---

## Forbidden write paths

- `countries/**`
- `UNIC/**`
- `reports/**`
- `Infrastructure/**`
- `scripts/**`
- `assets/**`

---

## Required outputs

- Updated control-plane docs reflecting the `archived` status and monthly archive folders: `AGENTS.md`, `README.md`, `ROADMAP.md`, `tickets/README.md`, `tickets/projectmanager.md`, `tickets/index.md`.
- New skill describing the archiving procedure (`skills/ticket-archiving/SKILL.md`) and updates to ticket-related skills (`skills/evobuilder-workflow/SKILL.md`, `skills/roadmap-tickets/SKILL.md`, `skills/ticket-creation/SKILL.md`) to reference the new status and workflow.
- New archive directory `tickets/202512 - Archived Tickets/` containing tickets `T-001` through `T-100`, each set to `Status: archived`.
- Tickets index updated with a dedicated “Archived” section that links to the December archive and distinguishes archived tickets from closed/done items.

---

## Acceptance criteria

- `archived` is a first-class status across AGENTS/README/ROADMAP/tickets docs, with clear rules on when to use it versus `done`/`dropped`.
- Archiving workflow is documented as a skill with steps to change status, move tickets into a YYYYMM-named archive folder, and refresh the index.
- `tickets/202512 - Archived Tickets/` exists and holds tickets `T-001`–`T-100`, all marked `Status: archived`.
- `tickets/index.md` has a separate Archived section (distinct from closed/done) that surfaces the December archive location.
- No files outside `Allowed write paths` are modified.

---

## Execution notes

- Added `archived` lifecycle across control-plane docs and skills, documenting monthly archive folders (`YYYYMM - Archived Tickets/`) and explicit index updates.
- Created `skills/ticket-archiving` with a deterministic retirement workflow and aligned related ticket skills to reference the new status.
- Moved tickets `T-001`–`T-100` into `tickets/202512 - Archived Tickets/`, setting each to `Status: archived`, and updated `tickets/index.md` with a dedicated Archived section.
