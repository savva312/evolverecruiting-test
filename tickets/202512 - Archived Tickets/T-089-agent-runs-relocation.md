# T-089: Agent run workspace relocation

Status: archived
Type: structure  
Priority: P1  
Dependencies: (none)  
Claimed-by: GPT-5.1-Codex-Max  
Claimed-at: 2025-12-20T18:28:37+00:00  
Last-updated: 2025-12-20

---

## Goal

Rename the global run workspace from `/research/runs` to `/agent runs/`, create `/agent runs/202512 runs/` for current EvoBuilder runs, and update documentation to reflect the new location.

---

## Context

- User requested renaming the run log folder to `/agent runs/` and to stand up `/agent runs/202512 runs/` for immediate use.
- Current control-plane files and country READMEs still point to `research/runs`; they need to align with the new path.
- This is a structure change because it moves a top-level directory and updates control-plane documentation.

---

## Allowed write paths

- `agent runs/**`
- `research/**`
- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `QA/T-024-qa-report.md`
- `tickets/index.md`
- `tickets/T-073-agent-runs-relocation.md`
- `nigeria/README.md`
- `nigeria/skills/nigeria-repo-routing/SKILL.md`
- `nigeria/reports/README.md`
- `romania/reports/README.md`
- `serbia/reports/README.md`
- `jordan/reports/README.md`
- `bulgaria/reports/README.md`

---

## Forbidden write paths

- `skills/**`
- `tickets/**` (except `tickets/index.md` and this ticket file)
- `.github/**`
- `scripts/**`
- Any path not explicitly listed under Allowed write paths

---

## Required outputs

- `/agent runs/` exists with the prior `research/runs` contents migrated and updated to the new path naming.
- `/agent runs/202512 runs/` created for current EvoBuilder runs (include a placeholder file to keep the directory tracked).
- Control-plane docs (`AGENTS.md`, `ROADMAP.md`, `README.md`) reference the new run workspace.
- Downstream docs that direct contributors to the run workspace (country report READMEs, QA notes, Nigeria routing skill) reference `/agent runs/`.
- Ticket index updated with this ticket entry; ticket file updated to `Status: done` upon completion.

---

## Acceptance criteria

- `research/runs` is removed/replaced by `/agent runs/` with content intact and paths updated.
- `/agent runs/202512 runs/` exists and is tracked.
- Control-plane documentation and referenced downstream docs point to `/agent runs/` instead of `research/runs`.
- No changes land outside Allowed write paths.
- Ticket status moved to `done` with a short summary of changes.

---

## Execution notes (optional)

- What changed (short): Moved the global run workspace to `/agent runs/`, created `/agent runs/202512 runs/`, migrated the run README/index, and refreshed control-plane and country docs to point to the new path.
- Open questions: None.
- Follow-up tickets suggested: None at this time.
