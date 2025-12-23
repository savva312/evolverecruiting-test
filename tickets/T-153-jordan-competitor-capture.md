# T-153: Jordan competitor capture and documentation

Status: done
Type: content
Priority: P2
Dependencies: T-017, T-097
Claimed-by: work
Claimed-at: 2025-12-20
Last-updated: 2025-12-20

---

## Goal

Research, capture, and document competitor institutions serving Jordanian students, emphasizing overlap with UNIC and UNIC Athens, within `countries/jordan/entities/competitors/**`.

---

## Context

- Jordan directory follows the country-first layout; competitor intelligence belongs under `countries/jordan/entities/competitors/`.
- Coordinate with any future Jordan program-cluster tickets; link to shared `/UNIC/**` materials instead of duplicating.

---

## Allowed write paths

- `countries/jordan/entities/competitors/**`
- `countries/jordan/reports/**` (if summarizing findings)
- `research/**` (optional notes)
- `tickets/T-101-jordan-competitor-capture.md` (status updates only)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket for status updates)
- Country directories outside Jordan
- `.github/**`
- `scripts/**`

---

## Required outputs

- `countries/jordan/entities/competitors/README.md` updated with scope and priority cues.
- At least two competitor profiles added or updated under `countries/jordan/entities/competitors/profiles/` with sources and `last_verified` metadata.
- Optional summary in `countries/jordan/reports/` if helpful.

---

## Acceptance criteria

- [ ] Only allowed paths modified.
- [ ] Competitor profiles include positioning notes, pricing/scholarship indications where available, sources, and `last_verified` dates.
- [ ] Links resolve and reference shared UNIC materials instead of duplicating them.
- [ ] Content is text-first with cited sources.

---

## Execution notes (optional)

- What changed (short): Added Bilkent University (Turkey) and Middle East University (Jordan) competitor profiles with pricing/aid signals, positioning vs UNIC/UNIC Athens, and updated Jordan competitor README with scope/priorities.
- Any open questions: Tuition-per-credit for MEU not published; confirm total tuition schedule for common majors.
- Follow-up tickets suggested: Add channel intelligence for Jordan-facing digital/agent marketing once sources identified.
