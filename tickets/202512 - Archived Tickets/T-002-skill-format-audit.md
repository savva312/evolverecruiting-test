# T-002: Audit and align SKILL.md formatting

Status: archived
Type: structure
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-20T13:37:39Z
Last-updated: 2025-12-20

---

## Goal

Review every `skills/*/SKILL.md` file and ensure it matches the standard Agent Skills frontmatter format (name/description + metadata block). Add or fix frontmatter so all skills are consistent with agentskills.io conventions.

---

## Context

- The repo uses the Agent Skills format with YAML frontmatter at the top of each `SKILL.md`.
- Some skills may be missing frontmatter or have inconsistent metadata fields.
- Align fields with the existing standard used by other skills in this repo (e.g., `metadata` block, consistent identifiers, scope for Bulgaria-specific skills).

---

## Allowed write paths

- `skills/**`
- `tickets/T-002-skill-format-audit.md`
- `research/**`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `tickets/**` (except this ticket file)
- `.github/**`
- `scripts/**`

---

## Required outputs

- Updated `SKILL.md` files under `skills/` (as needed)
- `tickets/T-002-skill-format-audit.md` (status + notes)

---

## Acceptance criteria

- All `skills/*/SKILL.md` files start with YAML frontmatter that includes `name`, `description`, and a `metadata` block.
- Bulgaria-specific skills include `metadata.scope: bulgaria` and `metadata.owner: evobuilder` unless a more specific owner is required.
- Any proprietary skills retain or add `license` info in the frontmatter.
- No files are modified outside the allowed write paths.
- Ticket fields accurately reflect status and changes.

---

## Execution notes (optional)

- What changed (short): Added or aligned YAML frontmatter and metadata across all `skills/*/SKILL.md` files; ensured Bulgaria skills include scope/owner and preserved proprietary licenses.
- Follow-ups suggested: None.
