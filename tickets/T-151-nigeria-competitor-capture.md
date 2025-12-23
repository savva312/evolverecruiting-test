# T-151: Nigeria competitor capture and documentation

Status: done
Type: content
Priority: P1
Dependencies: T-017, T-021, T-097
Claimed-by: work
Claimed-at: 2025-12-20T20:56:25+00:00
Last-updated: 2025-12-20

---

## Goal

Research, capture, and document competitor institutions serving Nigerian students, emphasizing overlaps with UNIC and UNIC Athens programs, within `countries/nigeria/entities/competitors/**`.

---

## Context

- Nigeria is in scope under the country-first layout; competitor intelligence should live under `countries/nigeria/entities/competitors/`.
- Coordinate with program clusters and digital benchmarks tickets to avoid duplication.
- Shared UNIC campus positioning remains in `/UNIC/**`; link rather than duplicate.

---

## Allowed write paths

- `countries/nigeria/entities/competitors/**`
- `countries/nigeria/reports/**` (if summarizing findings)
- `research/**` (optional notes)
- `tickets/T-099-nigeria-competitor-capture.md` (status updates only)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket for status updates)
- Country directories outside Nigeria
- `.github/**`
- `scripts/**`

---

## Required outputs

- `countries/nigeria/entities/competitors/README.md` updated to reflect scope and priorities.
- At least three competitor profiles added or updated under `countries/nigeria/entities/competitors/profiles/` with sources and `last_verified` dates.
- Optional summary or pipeline log in `countries/nigeria/reports/` if helpful.

---

## Acceptance criteria

- [ ] Only allowed paths modified.
- [ ] Competitor profiles include positioning, pricing or scholarship notes, and sourced `last_verified` metadata.
- [ ] Links resolve and reference shared UNIC materials rather than duplicating them.
- [ ] Content is text-first with sources cited.

---

## Execution notes (optional)

- What changed (short): Added three competitor profiles (Nile University of Nigeria, National Open University of Nigeria, University of the People), updated competitor README, and logged a summary report.
- Any open questions: Need current tuition bands for Nile and NOUN to quantify price deltas.
- Follow-up tickets suggested: Ticket to capture Nile/NOUN tuition tables and to monitor UoPeople Nigerian enrolment data.
