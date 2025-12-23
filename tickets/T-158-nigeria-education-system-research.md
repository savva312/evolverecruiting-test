# T-158: Nigeria education system research and documentation

Status: done
Type: content
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-01-05T00:00:00Z
Last-updated: 2025-12-20

---

## Goal

Produce a structured, source-backed summary of Nigeria's basic/secondary education pathways to refresh `countries/nigeria/market/education-system.md`, covering governance, curriculum structure, WAEC/NECO pathways, grading scales, transition points, vocational streams, and university entry (including JAMB/UTME specifics).

---

## Context

- Links to relevant repo files:
  - `ROADMAP.md` repo map: country market research lives under `countries/<country>/market/`
  - `countries/nigeria/market/education-system.md`
- External constraints (if any): none noted
- Assumptions (label them): focus on system mechanics and key credentials; include source notes

---

## Allowed write paths

- `countries/nigeria/market/education-system.md`
- `research/**` (optional; only for notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- `countries/*` outside `countries/nigeria/**`

---

## Required outputs

- `countries/nigeria/market/education-system.md` updated with governance, structure, credentials, national exams (WAEC/NECO), grading scales, and tertiary entry details
- Optional notes under `research/<execution_id>/` summarizing sources used

---

## Acceptance criteria

- [x] `countries/nigeria/market/education-system.md` provides an up-to-date overview with governance, grade/age bands, curriculum tracks, WAEC/NECO and other exit exams, grading scales, vocational vs general routes, and university entry (including JAMB/UTME)
- [x] Any added data or descriptions are clearly sourced or include source notes
- [x] No files are modified outside `Allowed write paths`
- [x] Internal links resolve to existing repo files

---

## Execution notes (optional)

- What changed (short): Refreshed `countries/nigeria/market/education-system.md` with governance, grade/age bands, WAEC/NECO timelines and grading, vocational/technical pathways, UTME/post-UTME and direct entry options, and source notes.
- Any open questions: None.
- Follow-up tickets suggested: Consider adding a Nigeria-specific admissions packaging checklist under `countries/nigeria/go-to-market/` (new ticket needed).
