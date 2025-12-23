# T-426: Bulgaria — write agent onboarding playbook (operational v1)

Status: done
Type: content
Priority: P0
Dependencies: T-419 (recommended)
Claimed-by: evoticketresolver__yc28cn6
Claimed-at: 2025-12-22T17:49:30Z
Last-updated: 2025-12-22
Completed-at: 2025-12-22T17:52:28Z
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Replace the placeholder `countries/bulgaria/go-to-market/agents-playbook/onboarding.md` with a practical, Bulgaria-specific onboarding workflow that an agent manager can run end-to-end (pilot → launch → quarterly review).

---

## Context

- Placeholder file: `countries/bulgaria/go-to-market/agents-playbook/onboarding.md`
- Existing agent roster and profiles:
  - `countries/bulgaria/entities/agents/feeder-candidates.md`
  - `countries/bulgaria/entities/agents/profiles/*.md`

---

## Allowed write paths

- `tickets/T-426-bulgaria-agent-onboarding-playbook.md`
- `countries/bulgaria/go-to-market/agents-playbook/onboarding.md`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**` (global)
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- `countries/**` (except `countries/bulgaria/**`)

---

## Required outputs

- `countries/bulgaria/go-to-market/agents-playbook/onboarding.md` updated to include, at minimum:
  - onboarding stages and owners (due diligence, contracting, training, launch, reporting)
  - a 30/60/90-day pilot plan with KPIs
  - asset checklist (what the agent gets, and what the agent must not claim)
  - a required data handoff format (fields the agent must provide for every lead)

---

## Acceptance criteria

- [x] The playbook is actionable (checklists + timelines), not generic prose.
- [x] It includes explicit guardrails for Athens vs Nicosia messaging to prevent offer confusion.
- [x] No files outside `Allowed write paths` were modified.

---

## What changed

- Replaced the placeholder onboarding document with an operational Bulgaria-specific workflow (owners, stage map, 30/60/90 pilot KPIs, asset checklist, Athens vs Nicosia guardrails, and required lead handoff format).
