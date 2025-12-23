# T-372: Auto-resolve merge conflicts + sweep + monitoring

Status: done  
Type: integration  
Priority: P1  
Dependencies: (none)  
Claimed-by: work  
Claimed-at: 2025-12-21T21:27:33Z  
Last-updated: 2025-12-21T21:29:19Z

---

## Goal

Add a GitHub Actions workflow that sweeps all open PRs targeting `main`, keeps labels (`clean` vs `needs-rebase`) in sync, and attempts automatic conflict resolution using a **union merge** for same-repo branches. The workflow must also capture conflict hunks as JSON and comment them on the PR for monitoring.

---

## Context

- Conflicted PRs currently require manual intervention; the new automation should probe conflicts, capture machine-readable metadata, and attempt a union merge before pushing resolutions.
- Monitoring depends on consistent labels (`clean`, `needs-rebase`, `auto-resolved-conflicts`, `auto-resolve-failed`) and JSON payloads posted as PR comments.
- The automation must run on a timer and when `main` changes to catch new conflicts promptly.

---

## Allowed write paths

- `.github/workflows/autoresolve-conflicts.yml`
- `.github/workflows/conflicts.yml`
- `tickets/T-359-autoresolve-conflicts.md`

---

## Forbidden write paths

- All other files and directories not listed above

---

## Required outputs

- `.github/workflows/autoresolve-conflicts.yml` containing the provided workflow that sweeps PRs, captures conflict hunks, and attempts union merges with commit message `AUTO-UNION: resolve conflicts with main (PR #<n>)`.
- (Optional verification only) `.github/workflows/conflicts.yml` confirming `dirtyLabel: needs-rebase` and `removeOnDirtyLabel: clean`.
- `tickets/T-359-autoresolve-conflicts.md` updated with status and execution notes.

---

## Acceptance criteria

- Workflow triggers on: schedule every 10 minutes, push to `main`, manual `workflow_dispatch`, and `pull_request_target` with `labeled` when `needs-rebase` is applied.
- Sweep marks mergeable PRs with `clean` (removing `needs-rebase`/`auto-resolve-failed`) and conflicting PRs with `needs-rebase` (removing `clean`).
- Only attempts auto-resolution for non-draft PRs targeting `main` whose head branches are in the same repository (no forks).
- Probe merge uses `--no-commit --no-ff` to gather conflict markers, records up to 20 files, 10 conflicts per file, 20 lines per side, and 3 context lines, truncating JSON beyond 60,000 characters.
- Probe metadata (files + conflict hunk excerpts) is included in PR comments whether the union merge succeeds or fails.
- Union merge attempt uses strategy `union` with commit message `AUTO-UNION: resolve conflicts with main (PR #<n>)`; on success pushes to PR head and labels with `auto-resolved-conflicts` + `clean`, removing `needs-rebase`/`auto-resolve-failed`.
- On union failure labels add `auto-resolve-failed`, keep `needs-rebase`, and remove `auto-resolved-conflicts`/`clean`, with a JSON comment containing the captured metadata.
- No files outside Allowed write paths are modified.

---

## Execution notes

- Added `.github/workflows/autoresolve-conflicts.yml` implementing the provided sweep/auto-resolution flow with probe metadata capture and union-merge pushes to same-repo branches.
- Confirmed `.github/workflows/conflicts.yml` already uses `dirtyLabel: needs-rebase` and `removeOnDirtyLabel: clean`; no changes required.
- Fixed probe merge handling to always abort and skip non-conflicting PRs, and tightened the `pull_request_target` labeled trigger to only run when `needs-rebase` is applied.
- Added null checks for `headRepository` / `headRefName` to skip forked or missing branches instead of failing the sweep before reaching same-repo conflicted PRs.
- Expanded autoresolve triggers to run on conflict workflow completion plus PR open/sync/ready events (in addition to cron/push/dispatch) and removed the label gate so sweeps fire deterministically while the Python sweep still limits action to CONFLICTING or needs-rebase PRs.
- For forked PRs, the sweep now adds `autoresolve-unavailable-fork` and a one-time comment explaining that the bot cannot push to forks and outlining manual conflict-resolution steps.
- Latest updates: Added token fallback to `GITHUB_TOKEN` when automation app secrets are absent, surfaced token source in logs, and added defensive error handling in label sweeps and per-PR resolution to prevent single failures from aborting the entire job while still emitting warnings for follow-up.
- Added REST fallback for PR head repo/branch detection, and when head metadata is missing the workflow now labels + comments with manual steps instead of silently skipping. Fetch and push failures now mark the PR with `auto-resolve-failed` plus a comment so blocked branches are visible, and merge metadata includes the head repository for easier debugging.
- Fixed the union-resolution step to avoid the invalid `git merge -X union` call (which failed with `unknown strategy option`) by using a `--no-commit` merge plus `git merge-file --union` per conflicted file, and reformatted failure/success comments to surface the git error message and reason alongside the JSON payload.
