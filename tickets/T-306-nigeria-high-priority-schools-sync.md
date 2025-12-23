# T-306: Nigeria high-priority school assets sync

Status: done  
Type: content  
Priority: P1  
Dependencies: (none)  
Claimed-by: work  
Claimed-at: 2025-12-21T10:20:18+00:00  
Last-updated: 2025-12-21

---

## Goal

Review all existing **high-priority Nigerian school profiles** and ensure the navigation README/index and the structured roster (`schools.csv`) are synchronized with the latest profile information. Add follow-up tickets for any missing high-priority schools that should have profiles.

---

## Context

- Multiple tickets recently added premium/priority Nigerian school profiles, but the navigation README/index and CSV were not always updated due to conflicts.
- High-priority scope includes Tier1 and Tier2 schools (and any other premium feeders already profiled under `countries/nigeria/entities/schools/profiles/**`).
- Keep work confined to Nigeria; do not touch other countries or global control-plane files.

---

## Allowed write paths

- `countries/nigeria/entities/schools/**`
- `countries/nigeria/data/entities/**`
- `tickets/**`
- `executions/**`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- Other country directories (e.g., `countries/bulgaria/**`, `countries/greece/**`, etc.)
- `.github/**`
- `scripts/**`

---

## Required outputs

- Updated `countries/nigeria/entities/schools/README.md` (and index if present/created) reflecting the current high-priority school set with links by city and counts.
- Updated `countries/nigeria/data/entities/schools.csv` synchronized to all profiled high-priority schools, with `last_verified` refreshed where profiles drive updates.
- Any missing high-priority schools identified are ticketed individually under `tickets/` with clear scope and allowed paths.
- Ticket updated on completion with status `done` and a short “What changed” summary.

---

## Acceptance criteria

- [x] Every high-priority Nigerian school profile under `countries/nigeria/entities/schools/profiles/**` has a corresponding, up-to-date row in `countries/nigeria/data/entities/schools.csv` (IDs, tier/evidence, pathways, fee notes, sources, `last_verified`).
- [x] `countries/nigeria/entities/schools/README.md` (and any index file) list and link the current high-priority schools by city/region, with counts that match the CSV/profile set.
- [x] Any missing high-priority schools are captured as new, properly formatted tickets with clear allowed write paths.
- [x] No changes occur outside `Allowed write paths`.
- [x] Ticket status set to `done` with “What changed” summary once outputs are delivered.

---

## Execution notes (optional)

- What changed: Regenerated `countries/nigeria/entities/schools/index.md` directly from `schools.csv`, refreshed `last_verified` to 2025-12-21 for all 61 high-priority schools, and aligned the schools README with the synced counts/links.
- Missing profiles: None — every profiled school has a matching CSV row and index entry.
- Follow-ups: Regenerate the index from `schools.csv` whenever new schools are added; keep `last_verified` aligned when data updates.
