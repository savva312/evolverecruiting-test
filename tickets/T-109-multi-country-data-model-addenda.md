# T-109: Extend data-model addenda to remaining countries

Status: done
Type: structure
Priority: P1
Dependencies: T-087
Claimed-by: work
Claimed-at: 2025-12-20T19:35:00Z
Last-updated: 2025-12-20

---

## Goal

Apply the global data-model Skill by converting remaining country data-model skills (Nigeria, Jordan, Romania, Serbia) into short addenda that link to the global standard and capture local path conventions. Update each country skill README to reference the global Skill.

---

## Allowed write paths

- `nigeria/skills/nigeria-data-model-csvs-and-profiles/**`
- `jordan/skills/jordan-data-model-csvs-and-profiles/**`
- `romania/skills/romania-data-model-csvs-and-profiles/**`
- `serbia/skills/serbia-data-model-csvs-and-profiles/**`
- `nigeria/skills/README.md`
- `jordan/skills/README.md`
- `romania/skills/README.md`
- `serbia/skills/README.md`
- `tickets/T-088-multi-country-data-model-addenda.md`
- `research/**`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**` (global) unless a future ticket allows it
- `.github/**`
- `scripts/**`
- Any other country directories not listed above
- Other tickets

---

## Required outputs

- Updated Nigeria, Jordan, Romania, and Serbia data-model Skill files as country addenda pointing to the global Skill and noting local paths.
- Country skill READMEs updated to reference the global data-model Skill.
- Ticket updated to `Status: done` with a short completion note.

---

## Acceptance criteria

- Each country data-model Skill defers to the global Skill for standards and only documents country-specific path conventions and alignment of IDs/profile paths.
- READMEs for Nigeria, Jordan, Romania, and Serbia skills link to the global data-model Skill.
- No files outside Allowed write paths are modified.
- Ticket marked done with execution notes once complete.

---

## Execution notes (optional)

- What changed (short): Converted Nigeria, Jordan, Romania, and Serbia data-model Skills into short addenda that point to the global standard, updated country skill READMEs to link the global Skill, and aligned paths/IDs guidance for each market.
- Any open questions: None.
- Follow-up tickets suggested: None.
