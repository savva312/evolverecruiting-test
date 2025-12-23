# T-371: Auto-merge workflow for clean PRs

Status: done  
Type: integration  
Priority: P2  
Dependencies: (none)  
Claimed-by: work  
Claimed-at: 2025-12-21T19:04:16Z  
Last-updated: 2025-12-21T19:08:56Z

---

## Goal

Add a GitHub Actions workflow that automatically enables auto-merge on clean, non-draft PRs targeting `main` when the PR originates from the same repository.

---

## Context

- PRs that have no conflicts and are ready for review should be auto-merged to reduce manual overhead.
- Workflow must not attempt to merge drafts, cross-repo PRs, or PRs targeting branches other than `main`.
- Use the GitHub CLI to request auto-merge and ignore conflicts gracefully.

---

## Allowed write paths

- `.github/workflows/automerge.yml`
- `.github/workflows/conflicts.yml`
- `tickets/T-358-automerge-workflow.md`

---

## Forbidden write paths

- All other files and directories not listed above

---

## Required outputs

- `.github/workflows/automerge.yml` defining the auto-merge workflow for qualifying PRs.
- `.github/workflows/conflicts.yml` defining a conflict-labeling workflow.
- `tickets/T-358-automerge-workflow.md` updated with status and execution notes.

---

## Acceptance criteria

- Workflow triggers on `pull_request` for opened, reopened, synchronized, and ready-for-review events.
- Workflow only runs for non-draft PRs whose base is `main` and head repo matches the target repo.
- Workflow attempts `gh pr merge --merge --auto` with `GITHUB_TOKEN`; if conflicts exist the run should finish without failing the check.
- No files outside Allowed write paths are modified.

---

## Execution notes (optional)

- What changed (short): Hardened `automerge.yml` with a GITHUB_TOKEN fallback when app credentials are missing, surfaced the token source in logs, and downgraded failures from branch updates or `gh pr merge --auto` to warnings while still skipping conflicted/behind branches.
- Open questions: None.
- Follow-up tickets suggested: None.
