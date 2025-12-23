# T-025: Post-migration cross-link cleanup

Status: archived
Type: content
Priority: P1
Dependencies: T-019, T-020, T-021, T-022
Claimed-by: work
Claimed-at: 2025-12-20T16:52:41Z
Last-updated: 2025-12-20

---

## Goal

Update internal links and references to match the new country-first layout (including `/country/reports`), and remove any obsolete directories left after migrations.

---

## Context

- Runs after all country migrations and the global skills split are complete.
- Ensures no references point to deprecated paths like `research/reports` or root-level Bulgaria directories.
- Should not touch control-plane files.

---

## Allowed write paths

- `**/*.md` (excluding control-plane files listed in Forbidden write paths)
- `**/*.yml`
- `**/*.yaml`
- `**/*.json`
- `tickets/T-023-cross-link-cleanup.md`
- `research/**` (optional run notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**` (except link updates strictly necessary to fix broken references)
- `tickets/**` (except this ticket file)
- `research/runs/**`
- `.github/**`
- `scripts/**`

---

## Required outputs

- All links updated to point to new country-first paths (including `/country/reports`)
- Obsolete directories or placeholders from migrations removed if empty
- `tickets/T-023-cross-link-cleanup.md` updated upon completion

---

## Acceptance criteria

- [x] No internal references to `research/reports` or old root-level Bulgaria paths remain
- [x] Links resolve to the new country directories and report locations
- [x] `research/runs` untouched
- [x] No files outside Allowed write paths are modified

---

## Execution notes (optional)

- What changed (short): Verified cross-links align to the country-first layout with no remaining references to deprecated `research/reports` or root-level Bulgaria paths; no edits required beyond closing the ticket record.
- Any open questions: None.
- Follow-up tickets suggested: None.
