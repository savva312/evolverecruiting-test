# T-105: Global data model skill + country addenda

Status: done
Type: structure
Priority: P1
Dependencies: T-020, T-026
Claimed-by: work
Claimed-at: 2025-12-20T19:09:32Z
Last-updated: 2025-12-20

---

## Goal

Create a global Skill for data-model CSVs and Markdown profiles, then trim Bulgaria and Greece skill files into short country addenda that link to the global guidance and note any path conventions. Update country skill READMEs to point to the global Skill.

---

## Context

- Country-first layout keeps country procedures in `/country/skills/**`; cross-country guidance belongs in `/skills/**`.
- The Bulgaria data-model Skill currently holds reusable guidance that should be centralized for all markets.
- Country addenda should only capture local path or naming differences while deferring to the global standard.

---

## Allowed write paths

- `skills/data-model-csvs-and-profiles/**`
- `bulgaria/skills/bulgaria-data-model-csvs-and-profiles/**`
- `greece/skills/greece-data-model-csvs-and-profiles/**`
- `bulgaria/skills/README.md`
- `greece/skills/README.md`
- `tickets/T-087-global-data-model-skill.md`
- `research/**`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `tickets/**` (except this ticket file)
- `.github/**`
- `scripts/**`
- Any other country directories

---

## Required outputs

- `skills/data-model-csvs-and-profiles/SKILL.md`
- Updated addenda at `bulgaria/skills/bulgaria-data-model-csvs-and-profiles/SKILL.md` and `greece/skills/greece-data-model-csvs-and-profiles/SKILL.md`
- Updated references in `bulgaria/skills/README.md` and `greece/skills/README.md`

---

## Acceptance criteria

- Global Skill documents structure, slug rules, CSV standards, and profile templates without country-specific examples or paths.
- Bulgaria and Greece Skill files defer to the global Skill and only capture country-specific path/filenaming conventions.
- Country skill READMEs link to the global Skill for data-model standards.
- No files outside Allowed write paths are modified.
- Ticket updated to `Status: done` with a short “what changed” note when complete.

---

## Execution notes (optional)

- What changed (short): Added a global data-model Skill, trimmed Bulgaria and Greece skills into short addenda with local paths, and refreshed both country skill READMEs to reference the global standard.
- Any open questions: None.
- Follow-up tickets suggested: None.
