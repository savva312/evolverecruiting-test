# T-181: Rename agent run workspace to /executions/

Status: done  
Type: structure  
Priority: P1  
Dependencies: (none)  
Claimed-by: work  
Claimed-at: 2025-12-20T22:37:15Z  
Last-updated: 2025-12-20T22:38:33Z

---

## Goal

Rename the global run workspace from the legacy agent-run folder to `/executions/`, migrate contents, and update all documentation and references to the new path.

---

## Context

- The current run workspace lives in a legacy “agent runs” folder, but stakeholders want it standardized to `/executions/`.
- The rename touches control-plane docs and downstream references that direct contributors to the run workspace.
- This is a structure change because it moves a top-level directory and updates governance docs.

---

## Allowed write paths

- `executions/**`
- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `tickets/index.md`
- `tickets/T-149-agent-runs-to-executions.md`
- `countries/bulgaria/README.md`
- `countries/bulgaria/reports/README.md`
- `countries/nigeria/README.md`
- `countries/nigeria/reports/README.md`
- `countries/nigeria/skills/nigeria-repo-routing/SKILL.md`
- `countries/romania/README.md`
- `countries/romania/reports/README.md`
- `countries/serbia/README.md`
- `countries/serbia/reports/README.md`
- `countries/jordan/reports/README.md`
- `skills/digital-measurement-and-benchmarks/SKILL.md`

---

## Forbidden write paths

- Any path not explicitly listed under Allowed write paths

---

## Required outputs

- `/executions/` exists with all prior legacy run-workspace contents migrated and paths updated.
- Documentation and references point to `/executions/` instead of the retired agent-run folder.
- Ticket index includes this ticket entry.
- Ticket status marked `done` with a brief change summary when complete.

---

## Acceptance criteria

- No references to the legacy agent-run workspace remain in allowed files; they point to `/executions/`.
- The old agent-run workspace is removed/replaced by `/executions/` with content intact (including subfolders like `202512 runs/`).
- Control-plane docs and downstream referenced files reflect the new path.
- Changes stay within allowed paths and are committed with this ticket.

---

## Execution notes (optional)

- What changed (short): Renamed the legacy agent-run workspace to `/executions/`, confirmed the staging folder at `executions/202512 runs/`, and scrubbed allowed docs (ticket index + ticket text) to point to the new path.
- Open questions: None.
- Follow-up tickets suggested: None currently.
