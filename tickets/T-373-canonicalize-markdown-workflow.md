# T-373: Canonicalize Markdown workflow

Status: done  
Type: integration  
Priority: P2  
Dependencies: (none)  
Claimed-by: work  
Claimed-at: 2025-12-21T14:35:38Z  
Last-updated: 2025-12-21T14:36:01Z

---

## Goal

Add a GitHub Actions workflow that canonicalizes Markdown formatting on PRs by rewriting changed `.md` files in-place and pushing fixups to same-repo branches.

---

## Context

- PRs frequently contain minor Markdown formatting inconsistencies that block automation and create noisy reviews.
- A dedicated workflow should normalize headings, bullets, trailing whitespace, and EOF newlines for only the `.md` files changed in a PR, then push a fixup commit when running on same-repo branches.
- The workflow must be safe for pull_request_target usage (checkout PR head) and support manual runs for debugging.

---

## Allowed write paths

- `.github/workflows/canonicalize-md.yml`
- `tickets/T-360-canonicalize-markdown-workflow.md`

---

## Forbidden write paths

- All other files and directories not listed in Allowed write paths.

---

## Required outputs

- `.github/workflows/canonicalize-md.yml` implementing the canonicalization workflow described in the user request.
- `tickets/T-360-canonicalize-markdown-workflow.md` updated with status and execution notes.

---

## Acceptance criteria

- Workflow triggers on `pull_request_target` (opened, reopened, synchronize, ready_for_review) and `workflow_dispatch`.
- For `pull_request_target`, the job checks that the PR head repo matches the base repo before attempting pushes.
- The workflow checks out the PR head branch (for pull_request_target) or default branch (for workflow_dispatch) with fetch-depth 0.
- Formatting script:
  - Operates only on `.md` files changed in the PR (from `gh pr view ... --json files`).
  - Removes trailing whitespace, ensures a single newline at EOF, normalizes ATX heading spacing, strips closing hashes, and enforces `- ` bullets with two-space indentation steps.
  - Exits cleanly if no Markdown files are changed.
- If changes are made, commits with message `chore: canonicalize markdown` and pushes; otherwise exits without committing.
- Ticket updated to `done` with brief execution notes.

---

## Execution notes (optional)

- Added `.github/workflows/canonicalize-md.yml` to normalize Markdown formatting on PRs and push fixups for same-repo branches.
- Workflow mirrors requirements: pull_request_target + workflow_dispatch triggers, safety gate for forks, Markdown-only targeting via `gh pr view`, and canonicalization script covering headings, bullets, trailing whitespace, and EOF newline with auto-commit `chore: canonicalize markdown`.
