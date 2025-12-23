# T-417: Ticketing system agent routing update

Status: done
Type: structure
Priority: P0
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-22T15:24:50Z
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A (Resolver ticket)
Research sections: N/A (Resolver ticket)
Research output path: N/A (Resolver ticket)

---

## Goal

Update the repo’s ticketing protocol to route tickets explicitly to EvoTicket Resolver or EvoResearcher, add required metadata for EvoResearcher tickets (report folder, research rounds, section count), and remove model-selection prompts now that EvoResearcher defaults to GPT-5.2 (H). Refresh control-plane docs, ticket templates, and skills so all new tickets follow the updated fields.

---

## Context

- The repo now has two agent roles: **EvoTicket Resolver** (default, single-round GPT-5.1/5.2 Codex) and **EvoResearcher** (multi-round GPT-5.2 (H) for deep reports).
- Each new ticket must name the agent. EvoResearcher tickets must also state the destination folder for the report, the number of research rounds, and the number of sections. Model selection is fixed to GPT-5.2 (H).
- Documentation and skills that govern ticket authoring, claiming, and research prompts need to be updated to reflect the new requirements.

---

## Allowed write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `tickets/README.md`
- `tickets/T-000-template.md`
- `skills/README.md`
- `skills/roadmap-tickets/SKILL.md`
- `skills/ticket-creation/SKILL.md`
- `skills/research-request-briefs/SKILL.md`
- `executions/**` (optional run notes)

---

## Forbidden write paths

- `countries/**`
- `UNIC/**`
- `reports/**`
- `skills/**` (except files listed in Allowed write paths)
- `.github/**`
- `scripts/**`
- Any other files not in Allowed write paths

---

## Required outputs

- `README.md` updated to describe the two agents and the new ticket fields for agent routing and EvoResearcher metadata.
- `AGENTS.md` updated with the new ticketing expectations (agent selection, EvoResearcher metadata, fixed model).
- `ROADMAP.md` updated where it describes ticket format/governance to include the agent routing requirements.
- `tickets/README.md` and `tickets/T-000-template.md` updated to enforce the new fields for agent selection and EvoResearcher metadata.
- `skills/roadmap-tickets/SKILL.md` and `skills/ticket-creation/SKILL.md` refreshed to include the new agent routing expectations.
- `skills/research-request-briefs/SKILL.md` updated so EvoResearcher briefs align to the new ticket metadata (no model selection; include report folder, section count, research rounds).
- `skills/README.md` updated if needed to reflect the revised research-request-briefs scope.

---

## Acceptance criteria

- [ ] All required outputs reflect the new two-agent model and explicitly require tickets to declare the agent.
- [ ] EvoResearcher tickets are documented as needing a report destination folder, research rounds, and section counts; no prompt asks for manager model selection.
- [ ] Ticket template and skills align on the required fields; control-plane files mention the two-agent workflow.
- [ ] No files outside Allowed write paths are modified.

---

## Execution notes (optional)

- What changed (short): Updated control-plane docs, ticket guides, and research brief skill to require agent selection on every ticket, add EvoResearcher-specific metadata (report folder, research rounds, section count), and remove model-selection prompts (GPT-5.2 (H) fixed).
- Any open questions: None.
- Follow-up tickets suggested: None.
