# T-040: Bulgaria high school skills alignment with global template

Status: archived
Type: structure
Priority: P1
Dependencies: T-026-high-school-profile-template
Claimed-by: assistant
Claimed-at: 2025-03-19T00:00:00Z
Last-updated: 2025-03-19

---

## Goal

Ensure Bulgaria’s school-related skills defer to the global high school profile template, removing duplicate templates and reconciling instructions so teams use the global standard.

---

## Context

- Bulgaria skills currently embed their own profile templates, which may drift from the global `skills/high-school-profile-template` skill.
- The repository policy requires global skills to remain the source of truth for shared patterns; country skills should only add Bulgaria-specific guidance.

---

## Allowed write paths

- `tickets/T-029-bulgaria-high-school-skill-alignment.md`
- `bulgaria/skills/**`
- `skills/high-school-profile-template/**`
- `skills/README.md` (only if needed to reflect alignment)
- `research/**` (optional execution notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `tickets/**` (except this ticket)
- `research/runs/**`
- `.github/**`
- `scripts/**`
- Other country directories (`/nigeria/**`, `/greece/**`, etc.)

---

## Required outputs

- Bulgaria school-related skills reference the global high school profile template instead of duplicating it.
- Overlapping or conflicting profile template content is removed from Bulgaria skills while preserving Bulgaria-specific guidance.
- Global high school profile skill remains the canonical template, with any necessary clarifications captured.
- Ticket file updated upon completion with status `done` and a brief “What changed” note.

---

## Acceptance criteria

- [x] No standalone high school profile templates remain inside Bulgaria skills; they point to the global template.
- [x] Bulgaria-specific guidance (tiers, outreach nuances, CSV expectations) is retained.
- [x] Global template remains unchanged or is clarified only where needed for alignment.
- [x] Only files within Allowed write paths are modified.
- [x] Ticket status updated to `done` with completion notes.

---

## Notes/Context

Focus on aligning `bulgaria/skills/bulgaria-schools-and-feeders` and `bulgaria/skills/bulgaria-schools-and-counselor-mapping` with the global template.

What changed (short): Pointed Bulgaria school skills to the global high school profile template, removed the local duplicate templates, refreshed paths to the country directories, and clarified optional metadata handling in the global skill.
