# T-443: Bulgaria — align Bulgaria skills addenda to actual paths + data model

Status: done
Type: qa
Priority: P1
Dependencies: (none)
Claimed-by: evoticketresolver_ahf8wg0f
Claimed-at: 2025-12-22T17:52:51Z
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Remove “foot-gun” inconsistencies in Bulgaria country skills by ensuring every referenced path:
- exists in the repo, or
- is clearly marked as “to be created in a separate ticket”

This prevents future agents from writing to nonexistent paths (e.g., `countries/bulgaria/market/partners/**`) or contradicting the current Bulgaria data model.

---

## Context

Examples of path mismatches found during review:
- `countries/bulgaria/skills/bulgaria-agents-and-partner-ecosystem/SKILL.md` references `countries/bulgaria/market/partners/**` and `countries/bulgaria/data/partners/**` which do not exist.
- `countries/bulgaria/skills/bulgaria-scholarships-and-discounts/SKILL.md` references `countries/bulgaria/data/financial-aid/**` but scholarships are currently stored under `countries/bulgaria/data/programs/scholarships-discounts.csv`.

---

## Allowed write paths

- `tickets/T-443-bulgaria-skills-path-alignment.md`
- `countries/bulgaria/skills/**`

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

- Updated Bulgaria skills files where needed (minimum set):
  - `countries/bulgaria/skills/bulgaria-agents-and-partner-ecosystem/SKILL.md`
  - `countries/bulgaria/skills/bulgaria-scholarships-and-discounts/SKILL.md`
- Any additional Bulgaria skills edits required to make all referenced paths accurate and consistent with:
  - `countries/bulgaria/README.md`
  - `countries/bulgaria/data/README.md`

---

## Acceptance criteria

- [x] Every file path referenced in edited SKILL docs exists after the change (or is explicitly labeled as “does not exist yet” with a pointer to a ticket).
- [x] No edits made outside `countries/bulgaria/skills/**` and this ticket file.

## What changed

- Updated Bulgaria skill addenda to reference the repo’s actual Bulgaria paths (agents, scholarships, education calendar) and removed stale/nonexistent path guidance.
