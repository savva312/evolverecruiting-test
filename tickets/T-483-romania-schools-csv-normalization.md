# T-483: Romania — normalize `countries/romania/data/entities/schools.csv`

Status: done
Type: data
Priority: P0
Dependencies: (none)
Claimed-by: evoticketresolver_nyr_aefr
Claimed-at: 2025-12-22T20:37:47Z
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Make `countries/romania/data/entities/schools.csv` operationally usable by:
- removing repeated header rows and mixed schemas
- enforcing **one header row** and a **single canonical column set**
- ensuring every row has the same number of columns
- updating `countries/romania/data/entities/schools-dictionary.md` so it matches the final schema

No data should be silently lost: if legacy columns don’t fit the canonical schema, preserve their content in `notes_short` (or a clearly documented column).

---

## Context

- Current file contains multiple headers and multiple schemas (likely pasted from different exports), making it unsafe for filtering or joining.
- Romania already has a clean “high potential feeder” dataset at:
  - `countries/romania/data/entities/schools/romania-high-potential-feeder-high-schools.csv`
  - `countries/romania/data/entities/schools/romania-high-potential-feeder-high-schools-dictionary.md`

Use the high-potential CSV schema as the starting point unless there is a strong reason not to.

---

## Allowed write paths

- `tickets/T-483-romania-schools-csv-normalization.md`
- `countries/romania/data/entities/schools.csv`
- `countries/romania/data/entities/schools-dictionary.md`
- `countries/romania/data/field-standards.md` (only if needed to resolve delimiter/boolean conventions; keep changes minimal)
- `executions/**` (optional for notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `.github/**`
- `scripts/**`
- `tickets/**` (except this ticket file)
- `countries/**` (except `countries/romania/data/**`)

---

## Required outputs

- Updated `countries/romania/data/entities/schools.csv`
- Updated `countries/romania/data/entities/schools-dictionary.md`
- (Optional) Updated `countries/romania/data/field-standards.md` if the ticket uncovers standards that contradict existing Romania CSV practice

---

## Acceptance criteria

- [x] `countries/romania/data/entities/schools.csv` has **exactly one header row** and **one schema**.
- [x] Every row has the same number of columns as the header (no ragged rows).
- [x] No duplicate `school_id` rows exist (unless explicitly documented as multi-campus and intentionally modeled).
- [x] `countries/romania/data/entities/schools-dictionary.md` exactly matches the final column set and documents allowed values for categorical fields.
- [x] No edits outside allowed paths.

---

## What changed

- Normalized `countries/romania/data/entities/schools.csv` into a single, consistent schema aligned to the Romania high-potential feeder dataset (all `school_id` rows preserved; no repeated headers; no ragged rows).
- Updated `countries/romania/data/entities/schools-dictionary.md` to match the final column set and document allowed values/field conventions.
- Clarified `countries/romania/data/field-standards.md` to explicitly allow dictionary-defined pipe-delimited list fields where applicable.
