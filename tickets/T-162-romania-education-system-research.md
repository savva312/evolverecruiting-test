# T-162: Romania education system research and documentation

Status: done
Type: content
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-20T21:00:43Z
Last-updated: 2025-12-20

---

## Goal

Compile a sourced overview of Romania's schooling structure to update `countries/romania/market/education-system.md`, detailing governance, grade/age bands, curriculum streams, Bacalaureat and vocational credentials, grading scales, transition points, and university entry requirements.

---

## Context

- Links to relevant repo files:
  - `ROADMAP.md` repo map: country market research lives under `countries/<country>/market/`
  - `countries/romania/market/education-system.md`
- External constraints (if any): none noted
- Assumptions (label them): focus on mechanics, credentials, and sourcing

---

## Allowed write paths

- `countries/romania/market/education-system.md`
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
- `countries/*` outside `countries/romania/**`

---

## Required outputs

- `countries/romania/market/education-system.md` updated with governance, structure, credentials (Bacalaureat and vocational equivalents), grading scales, and tertiary entry pathways
- Optional notes under `research/<execution_id>/` summarizing sources used

---

## Acceptance criteria

- [x] `countries/romania/market/education-system.md` offers an up-to-date overview with governance, grade/age bands, curriculum tracks, exit exams/credentials, grading scales, vocational vs general routes, and university entry mechanics
- [x] Any added data or descriptions are clearly sourced or include source notes
- [x] No files are modified outside `Allowed write paths`
- [x] Internal links resolve to existing repo files

---

## Execution notes (optional)

- What changed (short): Added sourced overview of Romania’s education governance, grade bands, Bacalaureat structure, VET pathways, grading scale, and university entry mechanics; logged source links in `research/T-138-sources.md`.
- Any open questions: None noted.
- Follow-up tickets suggested: Consider program-specific subject prerequisites mapping for Romanian Bac profiles to UNIC/UNIC Athens degrees.
