# T-458: Romania — agent compliance + GDPR playbook (operational)

Status: done
Type: content
Priority: P0
Dependencies: T-456
Claimed-by: CodexRun-2025-12-22
Claimed-at: 2025-12-22
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Expand `countries/romania/go-to-market/agents-playbook/compliance.md` into a Romania-ready compliance SOP that:
- defines mandatory compliance checks for agents (GDPR consent proof, data retention, sub-agent disclosures)
- defines marketing claims guardrails (scholarship claims, visa/recognition language, housing guarantees)
- includes a “compliance incident” workflow and remediation steps

---

## Context

Romania is an EU/GDPR jurisdiction; agent lead sharing must be consent-safe and auditable.

Use existing agent profiles for context; do not add personal data to the repo.

---

## Allowed write paths

- `tickets/T-458-romania-agents-compliance-gdpr.md`
- `countries/romania/go-to-market/agents-playbook/compliance.md`
- `countries/romania/go-to-market/agents-playbook/templates/**` (new files allowed)
- `executions/**` (optional for notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `.github/**`
- `scripts/**`
- `tickets/**` (except this ticket file)
- `countries/**` (except `countries/romania/go-to-market/**`)

---

## Required outputs

- Updated `countries/romania/go-to-market/agents-playbook/compliance.md`
- New templates:
  - `countries/romania/go-to-market/agents-playbook/templates/agent-gdpr-consent-proof-checklist.md`
  - `countries/romania/go-to-market/agents-playbook/templates/agent-sub-agent-disclosure-form.md`

---

## Acceptance criteria

- [x] Compliance doc includes: GDPR consent requirements, allowed data fields, retention guidance, and audit cadence.
- [x] Includes explicit “what not to claim” wording examples for agents (scholarships, visa timelines, recognition/licensure).
- [x] Templates exist and are usable.
- [x] No edits outside allowed paths.

---

## Completion notes

What changed:
- Expanded `countries/romania/go-to-market/agents-playbook/compliance.md` into a Romania-specific SOP covering GDPR data limits, consent proof, marketing guardrails, incident workflow, sub-agent controls, and quarterly audit cadence.
- Added `countries/romania/go-to-market/agents-playbook/templates/agent-gdpr-consent-proof-checklist.md` for quarterly evidence sampling.
- Added `countries/romania/go-to-market/agents-playbook/templates/agent-sub-agent-disclosure-form.md` to standardize approvals before sub-agent activation.
