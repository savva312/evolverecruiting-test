# T-427: Bulgaria — write agent compliance playbook (due diligence + guardrails)

Status: done
Type: content
Priority: P0
Dependencies: (none)
Claimed-by: evoticketresolver_163to43p
Claimed-at: 2025-12-22T17:50:04Z
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Replace the placeholder `countries/bulgaria/go-to-market/agents-playbook/compliance.md` with a Bulgaria-ready compliance checklist covering:
- GDPR/data handling (consent, lead transfer, retention)
- marketing claim control (scholarships, recognition, job outcomes)
- anti-rebate policy (no cashback / fee manipulation)
- sub-agent risk controls

---

## Context

- Placeholder file: `countries/bulgaria/go-to-market/agents-playbook/compliance.md`
- Relevant Bulgaria guidance:
  - `countries/bulgaria/market/recognition-and-licensure.md`
  - `countries/bulgaria/entities/agents/feeder-candidates.md` (risk notes)

---

## Allowed write paths

- `tickets/T-427-bulgaria-agent-compliance-playbook.md`
- `countries/bulgaria/go-to-market/agents-playbook/compliance.md`

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

- `countries/bulgaria/go-to-market/agents-playbook/compliance.md` updated to include:
  - a due diligence checklist (what to collect/verify)
  - red flags and “stop” conditions
  - required lead-consent language requirements (high-level, non-legal)
  - audit cadence (quarterly) and what is reviewed

---

## Acceptance criteria

- [x] Checklist explicitly avoids storing sensitive/PII in-repo (no passports, DOBs, national IDs).
- [x] Compliance guardrails are written as enforceable operational rules, not advice.
- [x] No files outside `Allowed write paths` were modified.

---

## What changed

- Replaced the placeholder compliance file with an enforceable operational playbook: due diligence gates, GDPR/consent rules, claims control, anti-rebate policy, sub-agent controls, red flags, and quarterly audit checks.
