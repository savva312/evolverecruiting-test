# T-001: Standardize bulgaria-data-model-csvs-and-profiles skill header

Status: archived
Type: structure
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-20T13:25:44Z
Last-updated: 2025-12-20

---

## Goal

Align the top matter of `bulgaria/skills/bulgaria-data-model-csvs-and-profiles/SKILL.md` with the standard Skill format used elsewhere in this repo (frontmatter first, consistent metadata fields).

---

## Context

- Reference skill format examples with YAML frontmatter first: `skills/git-pr-hygiene/SKILL.md`, `bulgaria/skills/bulgaria-education-system-and-calendar/SKILL.md`.
- Task reported via user request to standardize the header formatting.

---

## Allowed write paths

- `bulgaria/skills/bulgaria-data-model-csvs-and-profiles/**`
- `tickets/T-001-skill-format-standardization.md`
- `research/**`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**` (except as allowed above)
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`

---

## Required outputs

- `bulgaria/skills/bulgaria-data-model-csvs-and-profiles/SKILL.md`

---

## Acceptance criteria

- [x] `bulgaria/skills/bulgaria-data-model-csvs-and-profiles/SKILL.md` begins with YAML frontmatter that matches the standard Skill format (frontmatter first, includes `name`, `description`, and metadata block as used in other skills).
- [x] No files modified outside `Allowed write paths`.
- [x] Updated content follows existing repo conventions for markdown and Skill structure.
- [x] Ticket fields remain accurate (status, claim info).

---

## Execution notes (optional)

- What changed (short): Standardized `bulgaria/skills/bulgaria-data-model-csvs-and-profiles/SKILL.md` to start with YAML frontmatter, adding metadata for owner, version, and scope.
- Any open questions: None.
- Follow-up tickets suggested: None.
