# T-038: Varna high school profiles (report extraction)

Status: archived
Type: content
Priority: P1
Dependencies: (none)
Claimed-by: assistant
Claimed-at: 2025-12-20T17:01:27Z
Last-updated: 2025-12-20
What changed: Added Varna high school profiles (Tier 1 and Tier 2) using the global template and linked them from Varna and country school indexes.

---

## Goal

Extract school information from the provided Varna feeder report and populate Varna high school profiles using the global high school template structure.

---

## Allowed write paths

- `bulgaria/entities/schools/profiles/varna/**`
- `bulgaria/entities/schools/README.md`
- `tickets/T-028-varna-high-school-profiles.md`
- `research/**` (optional run notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `.github/**`
- `scripts/**`
- `research/runs/**`
- Other tickets (except status updates to this file)

---

## Required outputs

- Varna school profile files created or updated under `bulgaria/entities/schools/profiles/varna/**` using the global high school profile template structure.
- Updated `bulgaria/entities/schools/README.md` (if needed) to reference new Varna profiles.
- This ticket updated to reflect completion status.

---

## Acceptance criteria

- Profiles are populated with school identity and evidence-based details from the supplied Varna report; recruiting plan instructions from the report are omitted.
- Template sections are retained; unknown fields are left as placeholders or marked as needing verification.
- No files outside Allowed write paths are modified.
- Ticket status updated to `done` with a brief “What changed” note when completed.

---

## Notes/Context

Use the report’s Tier 1 and Tier 2 school information to fill profile fields (names, type, selectivity signals, language/certification signals, and tuition-fit assessments).
