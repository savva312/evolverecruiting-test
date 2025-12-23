# T-520: Lebanon — complete agent playbook (onboarding + compliance + SLAs)

Status: on-deck
Type: integration
Priority: P1
Dependencies: T-445 (recommended)
Claimed-by:
Claimed-at:
Last-updated: 2025-12-23
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Turn the Lebanon agent playbook placeholders into operational documents that the team can use to:
- vet and onboard Lebanon agents
- run pilots with clear KPIs
- enforce pricing/discount controls and compliant marketing
- review performance and decide to renew/exit

---

## Context

Placeholders to replace:
- `countries/lebanon/go-to-market/agents-playbook/onboarding.md`
- `countries/lebanon/go-to-market/agents-playbook/compliance.md`
- `countries/lebanon/go-to-market/agents-playbook/partner-slas.md`

Supporting context:
- Agent roster and profiles: `countries/lebanon/entities/agents/README.md`
- Country addendum skill: `countries/lebanon/skills/lebanon-agents-and-partner-ecosystem/SKILL.md`

---

## Allowed write paths

- `tickets/T-454-lebanon-agent-onboarding-compliance-slas.md`
- `countries/lebanon/go-to-market/agents-playbook/onboarding.md`
- `countries/lebanon/go-to-market/agents-playbook/compliance.md`
- `countries/lebanon/go-to-market/agents-playbook/partner-slas.md`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**` (global)
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- `countries/**` (except `countries/lebanon/**`)

---

## Required outputs

- `countries/lebanon/go-to-market/agents-playbook/onboarding.md` updated with:
  - due diligence checklist (licensing, ownership, sub-agent chains, references, marketing practices)
  - onboarding timeline + training checklist
  - “pilot period” structure and success criteria (90 days)
- `countries/lebanon/go-to-market/agents-playbook/compliance.md` updated with:
  - data handling rules (no sensitive docs via WhatsApp, consent capture, retention)
  - discount/offer authorization policy (no unapproved discounts)
  - escalation process for misconduct or misrepresentation
- `countries/lebanon/go-to-market/agents-playbook/partner-slas.md` updated with:
  - SLAs for lead response, application quality, document completeness, reporting cadence
  - KPI definitions that align with `agent-performance.csv` (T-449)

---

## Acceptance criteria

- [ ] Docs are actionable (checklists, owners, timelines) and avoid legal claims; use “policy/procedure” language.
- [ ] Explicitly covers commission/FX handling and how to avoid student harm in volatile-payment conditions.
- [ ] No files outside `Allowed write paths` were modified.

