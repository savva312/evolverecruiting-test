# T-385: Disable canonicalize workflow

Status: done
Type: integration
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-21T18:39:44Z
Last-updated: 2025-12-21T18:44:00Z

---

## Goal

Disable the Canonicalize Markdown GitHub Action and archive its workflow definition so it no longer runs but remains available for reference.

---

## Context

- The Canonicalize Markdown workflow has been flaky and is currently blocking progress.
- We want to prevent it from running on pull requests while keeping the implementation around in an archived location in case it is needed later.

---

## Allowed write paths

- `.github/workflows/canonicalize-md.yml`
- `.github/workflows-archive/canonicalize-md.yml`
- `tickets/T-369-disable-canonicalize-workflow.md`
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

- Canonicalize workflow disabled so it no longer triggers in `.github/workflows`.
- Archived copy of the workflow saved at `.github/workflows-archive/canonicalize-md.yml` for future reference.
- Ticket updated with execution notes and marked done once the workflow is disabled and archived.

---

## Acceptance criteria

- No active workflow named Canonicalize Markdown remains under `.github/workflows`.
- Archived copy exists at `.github/workflows-archive/canonicalize-md.yml`.
- Ticket updated to `done` with a brief summary of the changes.

---

## Execution notes (optional)

- Archived `canonicalize-md.yml` under `.github/workflows-archive/` and removed it from `.github/workflows` to disable the automation.
