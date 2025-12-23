# T-037: Sofia feeder school dossiers (extraction)

Status: archived
Type: content
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-20T16:57:34Z
Last-updated: 2025-12-20

---

## Goal

Extract Sofia feeder school information from the provided "Sofia Feeder Schools Strategy" report into structured markdown dossiers using the global high school profile skill as a guide (focus on school info, not marketing plans).

---

## Context

- Work is limited to Sofia schools mentioned in the report (Tier 1, Tier A, and Tier 2 watchlist).
- Use the global high-school profile template as the closest fit; omit recruiting plan sections beyond basic fit notes.

---

## Allowed write paths

- `bulgaria/entities/schools/profiles/sofia/**`
- `bulgaria/entities/schools/README.md`
- `tickets/T-028-sofia-feeder-school-dossiers.md`
- `research/**` (optional)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `.github/**`
- `scripts/**`
- `research/runs/**`
- other tickets

---

## Required outputs

- Individual `.md` dossiers for each Sofia school named in the source report (Tier 1, Tier A, Tier 2 watchlist) placed under `bulgaria/entities/schools/profiles/sofia/` using the high-school profile template structure (snapshot, affordability signals, outbound evidence, UNIC fit, gaps/sources).
- Updated `bulgaria/entities/schools/README.md` entry for the Sofia profiles, if navigation needs to reflect the new files.
- Ticket updated to `done` with a short “what changed” note when complete.

---

## Acceptance criteria

- Dossiers capture school type, curriculum/language cues, affordability signals, and outbound evidence provided in the report; speculative data labeled as assumptions.
- UNIC Nicosia vs UNIC Athens fit summarized per school without adding new marketing plans.
- Only allowed paths modified; no control-plane files changed.
- Ticket status updated with completion note.

---

## Execution notes (optional)

- What changed (short): Created 16 Sofia feeder school dossiers from the provided strategy report and linked them from the Bulgaria schools index.
- Any open questions: None.
- Follow-up tickets suggested: Refresh each dossier with verified contacts, curricula, and updated outcomes when available.
