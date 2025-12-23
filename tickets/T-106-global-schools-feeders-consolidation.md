# T-106: Global schools and feeders skill consolidation

Status: done
Type: structure
Priority: P1
Dependencies: T-020, T-026, T-029
Claimed-by: work
Claimed-at: 2025-03-20T00:00:00Z
Last-updated: 2025-03-20

---

## Goal

Create a global schools-and-feeders skill that centralizes shared workflow, CSV standards, privacy rules, and profile placement guidance, then align Bulgaria and Greece skills to reference it while keeping country-specific tiering and prioritization details local.

---

## Context

- Bulgaria and Greece currently maintain overlapping instructions for school and counselor workflows.
- The global high school profile template (`skills/high-school-profile-template`) should remain the source of truth for profile fields; this ticket links country skills to the global standard.
- Consolidation reduces duplication and ensures privacy guidance is consistent across markets.

---

## Allowed write paths

- `skills/**`
- `bulgaria/skills/**`
- `greece/skills/**`
- `tickets/T-087-global-schools-feeders-consolidation.md`
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
- Other country directories (e.g., `/nigeria/**`, `/serbia/**`, `/romania/**`, `/jordan/**`)

---

## Required outputs

- New global skill at `/skills/schools-and-feeders/SKILL.md` consolidating shared workflow, CSV fields, privacy expectations, and profile placement guidance while pointing to `skills/high-school-profile-template`.
- Greece skills updated to reference the global standard and retain only Greece-specific tiering or path references.
- Bulgaria skills updated with brief pointers to the global skill while preserving Bulgaria-specific tiering or city prioritization.
- Ticket updated with completion status and short summary when work is done.

---

## Acceptance criteria

- Global schools-and-feeders skill exists and is text-first, with clear links to the high school profile template and CSV/privacy standards.
- Greece skills (`greece/skills/greece-schools-and-feeders`, `greece/skills/greece-schools-and-counselor-mapping`) delegate to the global skill and include only local tiers/paths.
- Bulgaria skills (`bulgaria/skills/bulgaria-schools-and-feeders`, `bulgaria/skills/bulgaria-schools-and-counselor-mapping`) point to the global skill and retain only Bulgaria-specific tiering/city guidance; duplicate template content removed.
- No edits occur outside Allowed write paths; protected files remain untouched.
- Ticket marked `done` with a short “What changed” note after completion.

---

## Notes/Context

Focus on consolidation and link hygiene; do not alter the underlying high school profile template fields except by reference.

## Execution notes

- What changed (short): Added a global schools-and-feeders skill that centralizes workflow, CSV fields, privacy rules, and template references; aligned Greece skills to defer to the global standard; trimmed Bulgaria skills to point to the global skill while keeping Bulgaria-specific tiering and city priorities.
