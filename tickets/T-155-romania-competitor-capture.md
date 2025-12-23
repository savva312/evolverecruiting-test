# T-155: Romania competitor capture and documentation

Status: done
Type: content
Priority: P2
Dependencies: T-017, T-097
Claimed-by: work
Claimed-at: 2025-12-22
Last-updated: 2025-12-22

---

## Goal

Research, capture, and document competitor institutions serving Romanian students, focusing on overlap with UNIC and UNIC Athens, within `countries/romania/entities/competitors/**`.

---

## Context

- Romania directory follows the country-first layout; competitor research should stay under `countries/romania/entities/competitors/`.
- Coordinate with any future Romania program-cluster work; link to `/UNIC/**` resources rather than duplicating.

---

## Allowed write paths

- `countries/romania/entities/competitors/**`
- `countries/romania/reports/**` (if summarizing findings)
- `research/**` (optional notes)
- `tickets/T-103-romania-competitor-capture.md` (status updates only)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket for status updates)
- Country directories outside Romania
- `.github/**`
- `scripts/**`

---

## Required outputs

- `countries/romania/entities/competitors/README.md` updated with scope and priorities.
- At least two competitor profiles added or updated under `countries/romania/entities/competitors/profiles/` with sources and `last_verified` metadata.
- Optional summary in `countries/romania/reports/` if needed.

---

## Acceptance criteria

- [x] Only allowed paths modified.
- [x] Competitor profiles include positioning, pricing/scholarship signals where available, sources, and `last_verified` dates.
- [x] Links resolve and reference shared UNIC materials instead of duplicating them.
- [x] Content is text-first with cited sources.

---

## Execution notes (optional)

- What changed (short): Added Romania competitor scope/priorities and two competitor profiles (Carol Davila UMF and Ovidius University – English Medicine/Dentistry) with tuition signals, admissions filters, and implications for UNIC/UNIC Athens.
- Any open questions: None.
- Follow-up tickets suggested: Add more English-language competitors in Hungary/Bulgaria once fee tables for 2025–2026 publish.
