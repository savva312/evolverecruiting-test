# T-370: Ticket governance cleanup and renumbering

Status: done
Type: structure
Priority: P0
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-21T09:34:18Z
Last-updated: 2025-12-21

---

## Goal

Deliver a clean, conflict-free ticket set by closing legacy pre-T-223 tickets, recreating any still-needed scope with the updated non-conflicting ticket style, and resolving post-T-223 numbering overlaps so each ticket id is unique and ready for execution.

---

## Context

- Requested in the latest user instruction to organize all global tickets and ensure unique numbering.
- Repo governance rules live in `AGENTS.md` and `ROADMAP.md`.
- Ticket drafting conventions: `skills/ticket-creation/SKILL.md`, `skills/roadmap-tickets/SKILL.md`, and `skills/ticket-boundaries/SKILL.md`.

---

## Allowed write paths

- `tickets/**`
- `executions/**` (optional run notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `countries/**`
- `UNIC/**`
- `reports/**`

---

## Required outputs

- Updated statuses for all pre-T-223 tickets that remain open/in-progress/blocked to reflect closure, with brief execution notes.
- New tickets (with unique ids) covering any still-outstanding topics from the closed pre-T-223 set, authored in the conflict-minimized format from `skills/ticket-creation`.
- Resolved numbering for all tickets T-223 and above so no ids overlap, with minimal path/name changes.

---

## Acceptance criteria

- [ ] All tickets with ids below T-223 are either marked done/dropped/closed in this repository with justification or replaced by newly authored tickets.
- [ ] No duplicate ticket ids remain for open/in-progress tickets, and renumbered post-T-223 items have one-to-one filename and id alignment.
- [ ] New tickets follow the current ticket-writing standards (clear goal, allowed/forbidden paths, outputs, acceptance criteria, claim metadata when appropriate).
- [ ] All edits stay within `Allowed write paths`.
- [ ] Ticket index and references (if updated) match the final ticket ids.

---

## Execution notes (optional)

- What changed (short):
  - Closed/dropped all pre-T-223 tickets that were still open or in-progress and issued replacement tickets T-231–T-270 to preserve outstanding scopes with the current ticket-writing style.
  - Renumbered overlapping post-T-223 tickets (global skills and high-priority school syncs) to T-271–T-279 and removed the old conflicting files.
  - Regenerated `tickets/index.md` to reflect the new open/in-progress set and unique ids; retained the template ticket (T-000) as an intentional template.
  - Closed country setup and exams/calendar tickets that are already satisfied in the repo (Jordan setup; Lebanon/Romania/Serbia exam packs). School-profile tickets remain open where profiles are still incomplete (Bulgaria, Nigeria, Romania, Serbia, Lebanon); Greek school profile tickets were already present and unchanged.
- Any open questions:
  - None.
- Follow-up tickets suggested:
  - Consider a separate archival/renumbering pass for legacy completed tickets that still share ids if deeper uniqueness is desired for historical records.
