# T-375: Stabilize automation tokens for workflows

Status: done
Type: integration
Priority: P0
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-21T16:46:34Z
Last-updated: 2025-12-21T16:48:14Z

---

## Goal

Restore CI workflows that use the evolve GitHub App token by fixing the missing `app-id` input and adding a safe fallback so runs do not fail when the App secrets are unavailable.

---

## Context

Recent runs of the auto-merge and canonicalize workflows failed with `Input required and not supplied: app-id`, indicating the GitHub App ID secret is not being passed. We need to point the workflows at the correct secret and fall back to `GITHUB_TOKEN` when the App credentials are absent to keep automation unblocked.

---

## Allowed write paths

- `.github/workflows/automerge.yml`
- `.github/workflows/canonicalize-md.yml`
- `.github/workflows/autoresolve-conflicts.yml`
- `tickets/T-362-automation-token-fallback.md`
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

- Updated workflows use the correct GitHub App ID secret for the evolve automation app.
- Each workflow falls back to `GITHUB_TOKEN` when App secrets are missing so runs do not fail at the token step.
- This ticket file updated with completion status and a brief summary of changes.

---

## Acceptance criteria

- Auto-merge, canonicalize, and autoresolve workflows no longer fail with missing `app-id`; they either use `EVOLVE_AUTOMATION_APP_ID` with `EVOLVE_AUTOMATION_PRIVATE_KEY` or fall back to `GITHUB_TOKEN`.
- Logic for updating branches, canonicalizing markdown, and resolving conflicts continues to function with the selected token.
- No files outside Allowed write paths are modified.
- Ticket marked `done` with concise execution notes after changes.

---

## Execution notes (optional)

- Updated the auto-merge, canonicalize, and autoresolve workflows to read the GitHub App ID from `EVOLVE_AUTOMATION_APP_ID` and gracefully fall back to `GITHUB_TOKEN` when App secrets are absent so the runs no longer fail at token creation.
