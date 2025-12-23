# T-257: Remove `/research` workspace and redirect interim notes to `/executions/`

Status: done  
Type: structure  
Priority: P1  
Dependencies: (none)  
Claimed-by: work  
Claimed-at: 2025-12-20T22:36:38Z  
Last-updated: 2025-12-20

---

## Goal

Delete the legacy `/research/` workspace and update documentation to direct all interim work and run notes to `/executions/`.

---

## Context

- Prior migrations moved run logs to `/executions/`, but the historical `/research/` folder still exists with outdated references.
- Contributors remain instructed to place execution notes in `/research/`, which causes confusion now that `/executions/` is the canonical workspace.
- Removing the folder and refreshing documentation keeps the control plane consistent and avoids parallel work drifting to a deprecated path.

---

## Allowed write paths

- `research/**`
- `executions/**`
- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `tickets/README.md`
- `tickets/T-000-template.md`
- `tickets/T-224-research-workspace-removal.md`
- `skills/**`
- `countries/**`

---

## Forbidden write paths

- Any path not explicitly listed under Allowed write paths

---

## Required outputs

- `/research/` is removed from the repo.
- Control-plane documentation and contributor guides direct interim work and run notes to `/executions/`.
- Ticket template and guidance reference `/executions/` instead of `/research/`.
- Ticket updated to `Status: done` with a brief completion note.

---

## Acceptance criteria

- No lingering `/research/` directory remains.
- References in allowed files instruct contributors to use `/executions/` for interim work/run notes.
- Paths and examples are consistent with the existing `/executions/` workspace structure.
- No edits outside Allowed write paths.

---

## Execution notes (optional)

- What changed (short): Removed the legacy `/research/` workspace, redirected control-plane and country documentation to use `/executions/` for interim notes, and updated the ticket template/guidance to match.
- Open questions: None.
- Follow-up tickets suggested: Optional sweep to update legacy tickets that still mention `research/**` as an optional notes path.
