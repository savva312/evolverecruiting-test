# T-377: Auto-resolve should honor `needs-rebase` label even when mergeable is stale

Status: done
Type: integration
Priority: P1
Dependencies: T-359-autoresolve-conflicts
Claimed-by: work
Claimed-at: 2026-02-05T00:00:00Z
Last-updated: 2026-02-05

---

## Goal

Fix the auto-resolve workflow so it attempts the union-merge resolution when a PR carries the `needs-rebase` label, even if GitHub reports a stale `mergeable` status. This closes the gap where conflicts are detected and labeled but the resolver skips the branch.

---

## Context

- The conflict labeling workflow correctly tags PRs with `needs-rebase`, but the resolver only runs when `mergeable == CONFLICTING`, so labeled PRs with stale/unknown mergeability are ignored.
- We should gate on the label signal and let the probe merge determine whether conflicts actually exist, while preserving same-repo and non-draft safeguards.

---

## Allowed write paths

- `.github/workflows/autoresolve-conflicts.yml`
- `tickets/T-364-autoresolve-needs-rebase-handoff.md`
- `executions/**` (optional run notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- Other `tickets/**` files
- Country directories (`countries/**`)
- `.github/**` files not listed in Allowed write paths

---

## Required outputs

- Auto-resolve workflow updated to process PRs tagged `needs-rebase` by attempting the union merge even when the GitHub `mergeable` flag is stale/unknown.
- Ticket updated to reflect completion status and a brief summary of the change.

---

## Acceptance criteria

- PRs targeting `main` with the `needs-rebase` label (non-draft, same-repo) are swept and reach the probe-merge/union-merge logic even when `mergeable` is not `CONFLICTING`.
- Probe merges still abort cleanly when no conflicts are present; union merge pushes only on success and labels stay consistent.
- No files outside `Allowed write paths` are modified.
- Ticket marked `done` with concise execution notes.

---

## Execution notes (optional)

- What changed: Auto-resolve now proceeds when the `needs-rebase` label is present, even if the GitHub `mergeable` flag is stale/unknown, letting the probe/union merge drive resolution while keeping same-repo and draft guards intact.
