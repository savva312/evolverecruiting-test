# T-374: Secret scan workflow (gitleaks)

Status: done
Type: integration
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-21T15:24:27Z
Last-updated: 2025-12-21T15:25:08Z

---

## Goal

Add a gitleaks-based secret scanning workflow that focuses on changed files for PRs, scans the full tree on pushes to `main`, uploads a redacted JSON report artifact, and labels PRs with `secrets` when findings occur while removing the `clean` label. Update auto-merge logic to avoid merging PRs labeled `secrets`.

---

## Context

- Adds lightweight, rules-based secret detection for this content repo with low noise by limiting scans to changed files in PRs.
- Ensures failed scans label PRs for monitoring and prevents auto-merge when secrets are present.

---

## Allowed write paths

- `.github/workflows/secret-scan.yml`
- `.github/workflows/automerge.yml`
- `.gitleaks.toml`
- `.gitleaksignore`
- `tickets/T-361-secret-scan-workflow.md`

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

- `.github/workflows/secret-scan.yml` defining the PR/push secret scan using gitleaks with changed-file scope on PRs, full-tree on pushes, JSON report artifact upload, and failure labeling logic.
- `.gitleaks.toml` capturing the repo-level gitleaks configuration using default rules and placeholders for allowlists.
- `.github/workflows/automerge.yml` updated to block auto-merge when a PR has the `secrets` label.
- `tickets/T-361-secret-scan-workflow.md` updated with status and execution notes.

---

## Acceptance criteria

- Workflow triggers on `pull_request` (opened, reopened, synchronize, ready_for_review), `push` to `main`, and `workflow_dispatch`.
- PR runs scan only on files changed in the PR using the provided build-and-copy logic; push runs scan on full working tree.
- gitleaks is run with `--no-git`, redaction enabled, JSON report output to `gitleaks-report.json`, exits non-zero on findings, and uses `.gitleaks.toml` config.
- Report artifact is always uploaded.
- When the scan fails on a PR, the workflow applies the `secrets` label and removes `clean` (best-effort) using GitHub CLI; job has `pull-requests: write` and `issues: write` permissions to support labeling.
- Auto-merge workflow avoids merging PRs labeled `secrets` per the specified condition.
- No files outside Allowed write paths are modified.

---

## Execution notes (optional)

- What changed (short): Swapped the action for the Docker CLI-based gitleaks scan with changed-file PR scope, full-tree push scans, config/ignore propagation, report artifact upload, and PR labeling on failures; ensured auto-merge remains gated by the `secrets` label.
- Any open questions: Ensure the `secrets` label exists in the repository label set.
- Follow-up tickets suggested: None.
- 2025-12-21: Removed empty `[allowlist]` section from `.gitleaks.toml` to avoid config validation failures during gitleaks startup.
