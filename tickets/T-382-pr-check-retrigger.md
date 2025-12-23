# T-382: Ensure canonicalize pushes retrigger required PR checks

Status: done
Type: integration
Priority: P0
Dependencies: (none)
Claimed-by: work
Claimed-at: 2026-02-06T00:00:00Z
Last-updated: 2026-02-06T01:00:00Z

---

## Goal

Stop PRs from getting stuck with "expected" canonicalize/gitleaks checks on the latest head commit by ensuring pushes from the canonicalize workflow retrigger required PR checks (especially gitleaks) on the updated commit.

---

## Context

Canonicalize runs on `pull_request_target` and can push fixup commits to PR branches. Those pushes are changing the PR head without reliably triggering the `pull_request`-based gitleaks workflow, leaving required checks "Expected" for the newest SHA while older runs show green. We need the canonicalize workflow to dispatch the gitleaks workflow after it pushes so the latest commit always receives required checks.

---

## Allowed write paths

- `.github/workflows/canonicalize-md.yml`
- `.github/workflows/secret-scan.yml`
- `tickets/T-366-pr-check-retrigger.md`
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

- Canonicalize workflow dispatches the gitleaks workflow (using the automation app token) when it pushes changes so required checks run on the updated PR head.
- gitleaks workflow accepts dispatch runs on the PR branch.
- Ticket updated with completion status and brief execution notes.

---

## Acceptance criteria

- After canonicalize pushes a commit to a same-repo PR branch, it triggers a gitleaks run (via workflow_dispatch) for that branch using the automation app token; failures are surfaced clearly.
- gitleaks workflow can be invoked via workflow_dispatch on arbitrary refs and still performs the PR-mode scan set when the ref corresponds to a PR branch.
- No files outside `Allowed write paths` are modified.
- Ticket marked `done` with concise execution notes after changes.

---

## Execution notes (optional)

- Canonicalize workflow now requests the gitleaks workflow via `workflow_dispatch` (using the automation app token) whenever it pushes fixes to a PR branch, and it exposes branch/base outputs to drive that dispatch.
- Added `actions: write` permission so canonicalize can dispatch workflows safely.
- gitleaks workflow accepts dispatch inputs (`pr_number`, `base_ref`) and uses them to build the changed-file scan set, so dispatched runs mirror PR-mode behavior instead of scanning the entire tree.
