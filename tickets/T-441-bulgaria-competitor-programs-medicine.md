# T-441: Bulgaria — populate `competitor-programs.csv` for Medicine competitors

Status: done
Type: data
Priority: P1
Dependencies: (none)
Claimed-by: evoticketresolver_ypihbgiz
Claimed-at: 2025-12-22T17:53:13Z
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Populate `countries/bulgaria/data/programs/competitor-programs.csv` with the Medicine/MD competitor entries already documented in:
- `countries/bulgaria/program-clusters/medicine-md/competitors.md`

This converts a narrative competitor list into a structured dataset usable for pricing comparisons and counselor-ready evidence packs.

---

## Context

- Narrative competitor list exists with tuition and sources:
  - `countries/bulgaria/program-clusters/medicine-md/competitors.md`
- Structured table exists but is empty:
  - `countries/bulgaria/data/programs/competitor-programs.csv`
  - `countries/bulgaria/data/programs/competitor-programs-dictionary.md`

---

## Allowed write paths

- `tickets/T-441-bulgaria-competitor-programs-medicine.md`
- `countries/bulgaria/data/programs/competitor-programs.csv`
- `countries/bulgaria/data/programs/competitor-programs-dictionary.md` (only if needed to represent MD/integrated degree levels cleanly)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**` (global)
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- `countries/**` (except `countries/bulgaria/**`)

---

## Required outputs

- `countries/bulgaria/data/programs/competitor-programs.csv` populated with **≥12 rows** that correspond to the competitors in the Medicine competitor list, including tuition, language, location, intake months, notes, and `as_of`.

---

## Acceptance criteria

- [x] No tuition values are invented; if a competitor tuition is not clearly stated in sources, leave `tuition_eur` blank and explain in `notes`.
- [x] `competitor` names match the narrative competitor list for easy cross-reference.
- [x] No files outside `Allowed write paths` were modified.

---

## What changed

- Populated `countries/bulgaria/data/programs/competitor-programs.csv` with 12 Medicine/MD competitor rows based on `countries/bulgaria/program-clusters/medicine-md/competitors.md`.
- Updated `countries/bulgaria/data/programs/competitor-programs-dictionary.md` to support `degree_level=professional-doctorate` for integrated MD degrees.
