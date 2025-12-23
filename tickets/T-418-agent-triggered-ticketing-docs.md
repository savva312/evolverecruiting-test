# T-418: Document ticket creation when runs start without a ticket

Status: done
Type: structure
Priority: P1
Dependencies: (none)
Claimed-by: main
Claimed-at: 2025-02-20
Last-updated: 2025-02-20
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Document the required workflow when an agent is triggered without a referenced ticket, ensuring it creates a ticket for the work, includes it in the PR, and marks it closed at completion.

---

## Context

- Links to relevant repo files:
  - `AGENTS.md` section(s): Agent operating rules
  - `ROADMAP.md` section(s): change policy and ticket queue overview
  - `tickets/README.md`: ticket governance guidance
  - `tickets/T-000-template.md`: canonical ticket format
- External constraints: None noted
- Assumptions: Documentation updates will align with existing ticketing framework and control-plane files.

---

## Allowed write paths

- `AGENTS.md`
- `ROADMAP.md`
- `README.md`
- `tickets/README.md`
- `tickets/T-000-template.md`
- `tickets/T-418-agent-triggered-ticketing-docs.md`
- `executions/**` (optional for notes)

---

## Forbidden write paths

- `skills/**`
- `countries/**`
- `UNIC/**`
- `reports/**`
- `Infrastructure/**`
- `scripts/**`
- `.github/**`
- `executions/**` (except optional notes)
- Any path not listed in Allowed write paths

---

## Required outputs

- Updated documentation in the allowed files reflecting the ticket-on-trigger requirement.
- Ticket `tickets/T-418-agent-triggered-ticketing-docs.md` marked `done` with a short summary.

---

## Acceptance criteria

- [ ] AGENTS, ROADMAP, README, and ticket docs clearly state that agent runs without a pre-existing ticket must create, include, and close a ticket in the PR.
- [ ] No files outside Allowed write paths are modified.
- [ ] Ticket fields remain consistent with repo conventions (status updates, claim info, dates).
- [ ] Language aligns with existing ticketing workflow without altering other ticket rules.

---

## Execution notes (optional)

- What changed (short): Documented the requirement that runs without referenced tickets must create a new ticket, include it in the PR, and mark it done; refreshed AGENTS, ROADMAP, README, and ticket guidance accordingly.
- Any open questions: None.
- Follow-up tickets suggested: None.
