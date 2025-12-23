# T-386: Disable and archive gitleaks actions

Status: done
Type: integration
Priority: P1
Dependencies: (none)
Claimed-by: local
Claimed-at: 2025-01-08T00:00:00Z
Last-updated: 2025-01-08T00:10:00Z

---

## Goal

Disable gitleaks-based GitHub Actions workflows and archive the configuration so secret scanning no longer runs automatically while keeping historical context available.

---

## Context

- The repository previously added a gitleaks secret scanning workflow, but it now needs to be turned off.
- We should preserve the prior workflow/configuration for reference while preventing it from executing in GitHub Actions.

---

## Allowed write paths

- `.github/workflows/secret-scan.yml`
- `.github/workflow-archive/secret-scan.yml`
- `tickets/T-370-disable-gitleaks-actions.md`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/README.md`
- All other files and directories not explicitly listed in Allowed write paths

---

## Required outputs

- `.github/workflows/secret-scan.yml` removed or disabled so the workflow no longer runs in GitHub Actions.
- `.github/workflow-archive/secret-scan.yml` storing the archived version of the workflow for reference.
- `tickets/T-370-disable-gitleaks-actions.md` updated with execution notes and status.

---

## Acceptance criteria

- No active gitleaks workflow remains under `.github/workflows/`.
- The prior gitleaks workflow content is archived under `.github/workflow-archive/` with a clear note that it is disabled/archived.
- Ticket fields reflect completion status and note the archiving action.
- No files outside Allowed write paths are modified.

---

## Execution notes (optional)

- What changed (short): Archived the gitleaks workflow under `.github/workflow-archive/` and removed it from active workflows.
- Any open questions: None.
- Follow-up tickets suggested: None.
