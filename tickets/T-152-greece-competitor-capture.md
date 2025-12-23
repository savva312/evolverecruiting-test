# T-152: Greece competitor capture and documentation

Status: done
Type: content
Priority: P1
Dependencies: T-017, T-022, T-097
Claimed-by: work
Claimed-at: 2025-12-20T21:03:11Z
Last-updated: 2025-12-20

---

## Goal

Research, capture, and document competitor institutions serving Greek students, highlighting overlap with UNIC and UNIC Athens, within `countries/greece/entities/competitors/**`.

---

## Context

- Greece follows the country-first layout; competitor intel belongs under `countries/greece/entities/competitors/`.
- Coordinate with program clusters and UNIC positioning to avoid duplication.
- Shared campus materials stay under `/UNIC/**` and should be linked, not copied.

---

## Allowed write paths

- `countries/greece/entities/competitors/**`
- `countries/greece/reports/**` (if summarizing findings)
- `research/**` (optional notes)
- `tickets/T-100-greece-competitor-capture.md` (status updates only)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket for status updates)
- Country directories outside Greece
- `.github/**`
- `scripts/**`

---

## Required outputs

- `countries/greece/entities/competitors/README.md` updated with scope and priority notes.
- At least three competitor profiles added or updated under `countries/greece/entities/competitors/profiles/` including sources and `last_verified` metadata.
- Optional summary in `countries/greece/reports/` if needed.

---

## Acceptance criteria

- [x] Only allowed paths are modified.
- [x] Competitor profiles contain positioning, pricing/scholarship indicators, and sourced `last_verified` dates.
- [x] Links resolve and reference shared UNIC materials rather than duplicating them.
- [x] Content is text-first; no binaries without extracts.

---

## Execution notes (optional)

- What changed (short): Added scope/priorities to Greece competitor index and created three sourced profiles (ACG/Deree, European University Cyprus, UCLan Cyprus) with pricing, scholarships, and overlap notes (last_verified 2025-12-20).
- Any open questions: None noted.
- Follow-up tickets suggested: Extend coverage to non-Cyprus near-shore medical options (e.g., Bulgaria/Hungary) and Thessaloniki-based UK franchise colleges if prioritized.
