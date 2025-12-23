# T-027: Centralize UNIC campus content at repo root

Status: archived
Type: structure
Priority: P1
Dependencies: T-017, T-019
Claimed-by: assistant
Claimed-at: 2025-12-20T16:17:46+00:00
Last-updated: 2025-12-20

---

## Goal

Move the `UNIC` directory (with `UNIC Nicosia` and `UNIC Athens` subfolders) from `bulgaria/` back to the repo root so campus program content is shared across geographies. Update control-plane guidance to reflect the centralized location.

---

## Context

- Program positioning is identical across markets; keeping a single root `UNIC/` avoids country-specific duplicates.
- Current layout has `bulgaria/UNIC/**` from the Bulgaria migration; this change recenters shared program materials.
- Control-plane files should explain the new global location and how countries reference it.

---

## Allowed write paths

- `bulgaria/UNIC/**`
- `UNIC/**`
- `AGENTS.md`
- `ROADMAP.md`
- `tickets/T-025-unic-root-centralization.md`
- `tickets/index.md`
- `research/T-025-unic-root-centralization/**` (optional notes)

---

## Forbidden write paths

- `README.md`
- `skills/**`
- `tickets/**` (except this ticket and `tickets/index.md`)
- `.github/**`
- `scripts/**`
- Any other directories not explicitly allowed above

---

## Required outputs

- `UNIC/` directory present at repo root containing `UNIC Nicosia` and `UNIC Athens` subfolders with their existing `programs.md` content.
- `bulgaria/UNIC/` removed with contents relocated to the root `UNIC/`.
- `AGENTS.md` and `ROADMAP.md` updated to describe the centralized `UNIC/` location and how countries should reference it.
- `tickets/T-025-unic-root-centralization.md` updated with final status/notes.

---

## Acceptance criteria

- Root-level `UNIC/` exists with intact `UNIC Nicosia` and `UNIC Athens` content.
- No `bulgaria/UNIC/` directory remains; no duplicate campus content under country folders.
- Control-plane files reflect the global `UNIC/` structure and expected usage across countries.
- Any internal references to the UNIC directory resolve to the root location (update if needed).
- No files outside Allowed write paths are modified.

---

## Execution notes (optional)

- What changed (short): Moved `bulgaria/UNIC` to root `UNIC/` so UNIC Nicosia and UNIC Athens program materials are shared across markets; updated AGENTS and ROADMAP control-plane notes to describe the centralized location; refreshed ticket index.
- Any open questions: None.
- Follow-up tickets suggested: If other country files reference country-scoped UNIC paths, schedule a small cleanup ticket to update those links (none observed in this pass).
