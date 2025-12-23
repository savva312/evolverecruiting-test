# T-019: Multi-country control plane update

Status: archived
Type: structure
Priority: P0
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-20T16:02:45+00:00
Last-updated: 2025-12-20

---

## Goal

Update control-plane guidance so the repository formally adopts a multi-country layout with top-level country directories (e.g., `/bulgaria`, `/nigeria`, `/greece`). Document how reports relocate to country scopes and how skills are split between global and country-specific locations.

---

## Context

- Drives the structural migration requested for a multi-country repo, including country-specific reports and skills.
- Current control plane assumes Bulgaria-only scope; needs to reflect the new cross-country model.
- Must set clear rules before any content moves.

---

## Allowed write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `tickets/T-017-multi-country-control-plane.md`
- `tickets/index.md` (only for adding this ticket to the index, if used)

---

## Forbidden write paths

- All other files and directories not listed above

---

## Required outputs

- `README.md` updated with the multi-country repo map and contribution guidance
- `AGENTS.md` updated with new scope rules for country directories, reports, and skills split
- `ROADMAP.md` updated to describe the multi-country layout and change policy
- `tickets/T-017-multi-country-control-plane.md` status/notes updated upon completion

---

## Acceptance criteria

- [x] Control-plane files reflect top-level country directory conventions (e.g., `/bulgaria`, `/nigeria`, `/greece`)
- [x] Guidance clarifies that `research/runs` stays unchanged and `research/reports` is replaced by `/country/reports`
- [x] Skills policy clearly separates global skills (`/skills/**`) from country skills (`/skills/<country>/**`)
- [x] No files outside Allowed write paths are modified

---

## Execution notes (optional)

- What changed (short): Updated README, AGENTS, and ROADMAP to adopt a country-first layout (Bulgaria, Nigeria, Greece), clarify country report locations vs. research runs, and codify the global vs. country skills split. Ticket queue reordered around multi-country migrations.
- Any open questions: None.
- Follow-up tickets suggested: Proceed with T-018 through T-024 to execute migrations and QA.
