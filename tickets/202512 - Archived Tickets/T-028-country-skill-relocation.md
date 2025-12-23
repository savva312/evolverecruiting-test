# T-028: Country skill relocation

Status: archived
Type: structure
Priority: P0
Dependencies: T-017, T-019, T-020, T-021, T-022
Claimed-by: work
Claimed-at: 2025-02-25T00:00:00Z
Last-updated: 2025-02-25

---

## Goal

Move country-specific skills out of the global `/skills/<country>/**` tree into each country’s root namespace (e.g., `/bulgaria/skills/**`, `/greece/skills/**`, `/nigeria/skills/**`) while keeping general skills in `/skills/**`. Update documentation to reflect the new layout.

---

## Context

- Aligns the repo with the country-first layout by colocating country skills with their market content.
- Follows the multi-country control plane defined in T-017 and prior migrations (T-019, T-021, T-022).
- Requires updating control-plane docs so future tickets reference the new locations.

---

## Allowed write paths

- `tickets/T-026-country-skill-relocation.md`
- `skills/**` (global/general skills only)
- `bulgaria/skills/**`
- `greece/skills/**`
- `nigeria/skills/**`
- `bulgaria/**` (only for updating documentation references)
- `greece/**` (only for updating documentation references)
- `nigeria/**` (only for updating documentation references)
- `tickets/T-001-skill-format-standardization.md`
- `tickets/T-019-bulgaria-migration.md`
- `tickets/T-020-global-skills-split.md`
- `tickets/T-021-nigeria-migration.md`
- `tickets/T-022-greece-migration.md`
- `README.md`
- `ROADMAP.md`
- `AGENTS.md`
- `research/**` (optional execution notes)

---

## Forbidden write paths

- Any country directories beyond those listed above
- `tickets/**` except this ticket file
- `research/runs/**`
- `.github/**`
- `scripts/**`

---

## Required outputs

- Country-specific skill folders reside under `/bulgaria/skills/`, `/greece/skills/`, and `/nigeria/skills/`.
- `/skills/` contains only global (multi-country) skills.
- Control-plane documentation (e.g., `README.md`, `AGENTS.md`, `ROADMAP.md`, relevant country docs) reflects the new layout.
- Ticket file updated upon completion with status and summary.

---

## Acceptance criteria

- [x] No country-specific skill content remains under `/skills/<country>/`.
- [x] Country skill folders exist under each country root with intact content and links.
- [x] Global skills remain in `/skills/` with no country leakage.
- [x] Documentation references point to the new paths.
- [x] No files outside Allowed write paths are modified.

---

## Execution notes (optional)

- What changed (short): Moved Bulgaria, Greece, and Nigeria skill folders into their country namespaces, refreshed global and country documentation to reflect the new layout, and updated related tickets to match the country-first skills split.
- Any open questions: None.
- Follow-up tickets suggested: None.
