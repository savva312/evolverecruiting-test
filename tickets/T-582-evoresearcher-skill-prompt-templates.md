# T-582: EvoResearcher skill upgrade + prompt templates (starting with high-school profiling)

Status: done
Type: structure
Priority: P1
Dependencies: (none)
Claimed-by: evoticketresolver_hzaht4ig
Claimed-at: 2025-12-22T20:06:45Z
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Improve the global guidance for creating **EvoResearcher** tickets/briefs (where the ticket body is the prompt) and add reusable **prompt templates** for common repeated research tasks, starting with a deep comprehensive **high-school profile** prompt template.

---

## Context

- Relevant repo skills:
  - `skills/research-request-briefs/SKILL.md`
- Related historical tickets (context only):
  - `tickets/T-369-research-request-brief-skill.md`
  - `tickets/T-417-ticketing-system-agent-routing.md`

---

## Allowed write paths

- `tickets/T-582-evoresearcher-skill-prompt-templates.md`
- `skills/research-request-briefs/**`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**` (except `skills/research-request-briefs/**`)
- `tickets/**` (except this ticket file)
- `.github/**`
- `scripts/**`

---

## Required outputs

- `skills/research-request-briefs/SKILL.md` (updated)
- `skills/research-request-briefs/prompt-templates/README.md` (new)
- `skills/research-request-briefs/prompt-templates/high-school-profile.md` (new)

---

## Acceptance criteria

- [ ] Required output files exist at the specified paths
- [ ] The EvoResearcher skill clearly documents how to write an EvoResearcher ticket prompt (ticket body = prompt beyond parameter fields)
- [ ] Prompt templates are copy/paste-friendly and explicitly designed to be customized
- [ ] No files were modified outside `Allowed write paths`

---

## Execution notes (optional)

- What changed (short): Updated `skills/research-request-briefs/SKILL.md` with ticket-first guidance for EvoResearcher prompts and added a `prompt-templates/` folder with a copy/paste high-school profiling prompt template.
- Follow-up tickets suggested: Add additional prompt templates (e.g., education-agent profile, regulator mapping, competitor profiling) and optionally standardize legacy brief formats that still use older metadata keys (e.g., `manager_model`).
