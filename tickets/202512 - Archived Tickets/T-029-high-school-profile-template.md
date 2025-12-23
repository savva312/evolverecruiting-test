# T-029: Global high school profile template skill

Status: archived
Type: structure
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-03-15T00:00:00Z
Last-updated: 2025-03-15

---

## Goal

Add a global skill that provides the canonical markdown template for high school profiles, plus a ready-to-use template file. Keep it in `/skills/` so all countries can reuse the same pattern without duplicating content.

---

## Context

- User-provided high school profile template (see request).
- Root `AGENTS.md` requires a structure ticket to modify `skills/**`.
- Template should remain country-agnostic and fit within the existing Agent Skills format.

---

## Allowed write paths

- `skills/high-school-profile-template/**`
- `skills/README.md`
- `tickets/T-026-high-school-profile-template.md`
- `research/**` (optional run notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/bulgaria/**`
- `skills/nigeria/**`
- `skills/greece/**`
- `.github/**`
- `scripts/**`
- `research/runs/**`
- Other tickets (except status updates to this file)

---

## Required outputs

- `skills/high-school-profile-template/SKILL.md` describing how to use and adapt the template.
- `skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md` containing the canonical markdown template.
- `skills/README.md` updated to list the new skill.

---

## Acceptance criteria

- [x] New skill folder follows the Agent Skills format with YAML frontmatter.
- [x] Template file is clean markdown, ready for copy/paste by country teams.
- [x] No country-specific content is included; guidance remains global.
- [x] Only files in Allowed write paths are modified.
- [x] Ticket status updated to `done` with a short “What changed” note.

---

## Execution notes (optional)

- What changed (short): Added global high school profile template skill with usage guidance and the canonical template file; updated skills index.
- Any open questions: None.
- Follow-up tickets suggested: None.
