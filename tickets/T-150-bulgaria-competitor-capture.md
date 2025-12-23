# T-150: Bulgaria competitor capture and documentation

Status: done
Type: content
Priority: P1
Dependencies: T-017, T-019, T-097
Claimed-by: work
Claimed-at: 2025-12-20T20:56:08+00:00
Last-updated: 2025-12-20

---

## Goal

Research, capture, and document competitor institutions serving Bulgarian students, focusing on overlap with UNIC and UNIC Athens, and structure findings within `countries/bulgaria/entities/competitors/**`.

---

## Context

- Country-first layout keeps competitor content at `countries/bulgaria/entities/competitors/`.
- Prior work created baseline structure; this ticket ensures actionable competitor research with scope isolation.
- Coordinate with program-cluster workstreams to avoid duplication; link any shared UNIC positioning in `/UNIC/**` instead of duplicating.

---

## Allowed write paths

- `countries/bulgaria/entities/competitors/**`
- `countries/bulgaria/reports/**` (if summarizing findings)
- `research/**` (optional notes)
- `tickets/T-098-bulgaria-competitor-capture.md` (status updates only)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket for status updates)
- Country directories outside Bulgaria
- `.github/**`
- `scripts/**`

---

## Required outputs

- `countries/bulgaria/entities/competitors/README.md` updated with scope and priorities.
- At least three competitor profiles added or updated under `countries/bulgaria/entities/competitors/profiles/` with `last_verified` metadata and sources.
- Optional summary or pipeline log in `countries/bulgaria/reports/` if needed.

---

## Acceptance criteria

- [ ] Files modified only within allowed paths.
- [ ] Competitor profiles include sources, date stamps, and clear positioning notes relevant to UNIC/UNIC Athens.
- [ ] Internal links resolve to existing files (including any UNIC references).
- [ ] Data is text-first; no binaries added without extracts.

---

## Execution notes (optional)

- What changed (short): Claimed ticket; updated competitor scope README; added AUBG, Technical University of Sofia, and New Bulgarian University profiles with last_verified dates and sources.
- Any open questions: None.
- Follow-up tickets suggested: Consider deeper price benchmarking once 2026 tuition tables are published for AUBG and TU-Sofia English-language programmes.
