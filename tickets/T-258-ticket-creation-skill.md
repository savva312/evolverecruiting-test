# T-258: Global ticket creation skill

Status: done
Type: structure
Priority: P1
Dependencies: T-017, T-020
Claimed-by: work
Claimed-at: 2025-12-21T08:39:22Z
Last-updated: 2025-12-21

---

## Goal

Create a global skill that teaches agents how to draft and close tickets with clarity, narrow scopes, non-overlapping write paths, and strong documentation of decisions and follow-ups.

---

## Context

- Agents must operate via tickets; we need a concise, repeatable recipe for drafting conflict-proof tickets and closing them with learnings captured.
- The skill should reinforce writing tickets that separate base/index updates from parallelized execution work to avoid merge conflicts.
- It should also document how to record key decisions, gaps, and suggested follow-up tickets inside the ticket itself.

---

## Allowed write paths

- `skills/ticket-creation/**`
- `skills/roadmap-tickets/SKILL.md`
- `skills/README.md`
- `tickets/T-225-ticket-creation-skill.md`
- `research/**` (optional notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- Any country directories (e.g., `/countries/**`)
- Other tickets in `/tickets/**` (except status updates to this file)
- `.github/**`
- `scripts/**`

---

## Required outputs

- `skills/ticket-creation/SKILL.md` documenting how to create and finish tickets with clear scopes, allowed/forbidden paths, outputs, and decision logging.
- Updated `skills/roadmap-tickets/SKILL.md` to reference the new ticket creation workflow and incorporate the conflict-minimization guidance.
- Updated `skills/README.md` index to include the new skill.
- `tickets/T-225-ticket-creation-skill.md` marked `done` with a short “What changed” note after completion.

---

## Acceptance criteria

- New global skill provides a step-by-step playbook for drafting tickets: clarity of goals, narrow scope, allowed/forbidden write paths, required outputs, acceptance criteria, and claim metadata.
- Guidance instructs agents to document decisions, learnings, blockers, and follow-up tickets directly in the ticket before closing.
- Skill emphasizes parallel safety: split shared index/base-file edits into dedicated tickets to avoid collisions when many tickets run in parallel.
- `skills/roadmap-tickets/SKILL.md` references or embeds the new workflow without duplicating content.
- `skills/README.md` lists the new skill.
- No files outside `Allowed write paths` are modified.

---

## Execution notes (optional)

- What changed (short): Added global `ticket-creation` skill, refreshed `roadmap-tickets` with conflict-minimization and closure logging guidance, and indexed the new skill in `skills/README.md`.
- Any open questions: None.
- Follow-up tickets suggested: Consider country addenda only if local ticket formats ever diverge.
