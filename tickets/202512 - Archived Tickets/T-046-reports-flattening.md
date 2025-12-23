# T-046: Flatten country report folders

Status: archived
Type: structure
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-20T17:50:18Z
Last-updated: 2025-12-20

---

## Goal

Eliminate the `reports/structured/` subfolder pattern in every country subtree so each country uses a single `/reports/` directory. Move any reports currently nested under `reports/structured/` up one level and update local README guidance and internal references accordingly.

---

## Context

- Current country trees (e.g., Bulgaria, Greece, Jordan, Romania, Serbia) contain `reports/structured/` plus documentation that points to that layout.
- Simplifying to a flat `/reports/` per country reduces nesting and makes paths consistent.

---

## Allowed write paths

- `bulgaria/reports/**`
- `bulgaria/market/**`
- `greece/reports/**`
- `greece/market/**`
- `nigeria/reports/**`
- `nigeria/market/**`
- `romania/reports/**`
- `romania/market/**`
- `jordan/reports/**`
- `jordan/market/**`
- `serbia/reports/**`
- `serbia/market/**`
- `tickets/T-032-reports-flattening.md`
- `research/T-032-reports-flattening/**` (optional notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket file)
- `research/runs/**`
- `.github/**`
- `scripts/**`
- Any files outside the allowed country paths above

---

## Required outputs

- All country report files previously under `reports/structured/` moved to the country `reports/` root.
- Country report README files updated to describe the flattened layout (no `structured/` subsection).
- Any in-country references pointing to `reports/structured/` updated to the new flat paths.
- `tickets/T-032-reports-flattening.md` updated on completion with status and a short change note.

---

## Acceptance criteria

- [x] No `reports/structured/` directories remain under any country subtree.
- [x] All report files formerly in `reports/structured/` exist in the corresponding `reports/` root with correct filenames and links.
- [x] Country README and market pages reference the flat `reports/` paths only.
- [x] No files outside the Allowed write paths are modified.

---

## Execution notes (optional)

- What changed (short): Flattened country report folders by moving structured reports into each `reports/` root, deleting `reports/structured` directories, updating country report README files, and fixing market outbound-mobility links to point to the flat paths.
- Any open questions: None.
- Follow-up tickets suggested: None.
