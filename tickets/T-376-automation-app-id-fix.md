# T-376: Enforce automation app token usage and resolve missing app ID

Status: done
Type: integration
Priority: P0
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-21T16:53:01Z
Last-updated: 2025-12-21T16:54:12Z

---

## Goal

Ensure CI workflows consistently use the evolve GitHub App token by resolving the correct app ID (supporting legacy/primary secret names) and failing fast with a clear error when credentials are absent, eliminating reliance on `GITHUB_TOKEN` fallbacks.

---

## Context

Previous runs failed because `app-id` was missing. The workflows now fall back to `GITHUB_TOKEN`, but we need deterministic use of the GitHub App token to avoid permission and behavior differences.

---

## Allowed write paths

- `.github/workflows/automerge.yml`
- `.github/workflows/canonicalize-md.yml`
- `.github/workflows/autoresolve-conflicts.yml`
- `tickets/T-363-automation-app-id-fix.md`
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

- Workflows resolve the automation app ID from available secrets (preferred `EVOLVE_AUTOMATION_APP_ID`, legacy `EVOLVE_AUTOMATION_APP`) and validate the private key.
- Workflows use the automation app token (no `GITHUB_TOKEN` fallback) and fail with actionable messaging if credentials are missing.
- Ticket updated to `done` with concise execution notes.

---

## Acceptance criteria

- Auto-merge, canonicalize, and autoresolve workflows obtain `app-id` reliably via the resolved secret name and use the GitHub App token for all API/git operations.
- If app credentials are missing, the workflows fail early with a clear error pointing to the required secrets.
- No files outside Allowed write paths are modified.
- Ticket marked `done` upon completion with a short summary.

---

## Execution notes (optional)

- Added a credentials resolution step to prefer `EVOLVE_AUTOMATION_APP_ID` and fall back to the legacy `EVOLVE_AUTOMATION_APP`, validating the private key and failing fast with clear errors if secrets are missing, so workflows always use the GitHub App token (no `GITHUB_TOKEN` fallback).
