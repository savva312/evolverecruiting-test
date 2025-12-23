# T-154: Lebanon competitor capture and documentation

Status: done
Type: content
Priority: P2
Dependencies: T-017, T-097
Claimed-by: GPT-5.1-Codex-Max
Claimed-at: 2025-12-20T20:58:01Z
Last-updated: 2025-12-20

---

## Goal

Research, capture, and document competitor institutions serving Lebanese students, focusing on overlap with UNIC and UNIC Athens, within `countries/lebanon/entities/competitors/**`.

---

## Context

- Lebanon directory adheres to the country-first layout; competitor research should be contained within `countries/lebanon/entities/competitors/`.
- Coordinate with future Lebanon program-cluster or skills tickets; link to `/UNIC/**` resources rather than duplicating.

---

## Allowed write paths

- `countries/lebanon/entities/competitors/**`
- `countries/lebanon/reports/**` (if summarizing findings)
- `research/**` (optional notes)
- `tickets/T-102-lebanon-competitor-capture.md` (status updates only)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket for status updates)
- Country directories outside Lebanon
- `.github/**`
- `scripts/**`

---

## Required outputs

- `countries/lebanon/entities/competitors/README.md` updated with scope and priorities.
- At least two competitor profiles added or updated under `countries/lebanon/entities/competitors/profiles/` with sources and `last_verified` metadata.
- Optional summary in `countries/lebanon/reports/` if needed.

---

## Acceptance criteria

- [x] Only allowed paths modified.
- [x] Competitor profiles include positioning, pricing/scholarship signals where available, sources, and `last_verified` dates.
- [x] Links resolve and reference shared UNIC materials instead of duplicating them.
- [x] Content is text-first with cited sources.

---

## Execution notes (optional)

- What changed (short): Added competitor scope/priorities for Lebanon and two detailed profiles (AUB, University of the People) with pricing, aid signals, and positioning notes.
- Any open questions: Need future coverage of LAU and nearshore Cyprus/Greece/Türkiye options when data access is available.
- Follow-up tickets suggested:
