# T-456: Romania — build agent onboarding playbook (due diligence + training + asset pack)

Status: done
Type: content
Priority: P1
Dependencies: T-446
Claimed-by: execution-20251222-codex
Claimed-at: 2025-12-22
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Expand `countries/romania/go-to-market/agents-playbook/onboarding.md` from a placeholder into an onboarding SOP that:
- defines a step-by-step onboarding flow (target → due diligence → contract → training → activation → first 10 leads QA)
- includes a Romania-specific due diligence checklist (ownership, sub-agent policy, GDPR handling, marketing claims)
- links to the exact Romania assets an agent needs (counselor toolkit items, program links, key deadlines)

---

## Context

Agent profiles exist, but agent operations do not. The playbook must be usable by a partner manager and reduce compliance risk.

Inputs:
- `countries/romania/entities/agents/feeder-candidates.md`
- `countries/romania/entities/agents/profiles/*.md`

## What changed
- Replaced the placeholder onboarding SOP with a Romania-specific, SLA-driven flow covering targeting through first-10-lead QA and linked every required asset.
- Added `countries/romania/go-to-market/agents-playbook/templates/agent-onboarding-checklist.md` so diligence, training, GDPR, and marketing approval steps are logged consistently.

---

## Allowed write paths

- `tickets/T-456-romania-agents-onboarding-playbook.md`
- `countries/romania/go-to-market/agents-playbook/onboarding.md`
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

- Updated `countries/romania/go-to-market/agents-playbook/onboarding.md`
- New checklist template:
  - `countries/romania/go-to-market/agents-playbook/templates/agent-onboarding-checklist.md`

---

## Acceptance criteria

- [ ] Onboarding doc includes a numbered process, owners, and time SLAs (e.g., due diligence within X days).
- [ ] Checklist template covers GDPR/data transfer, sub-agent disclosures, and marketing claims approvals.
- [ ] No edits outside allowed paths.
