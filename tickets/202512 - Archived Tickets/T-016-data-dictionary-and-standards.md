# T-016: Data dictionary and field standards for CSVs

Status: archived
Type: data
Priority: P2
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-20 15:28:36Z
Last-updated: 2025-12-20 15:31:21Z

---

## Goal

Define consistent field names, data types, and value standards for the CSV scaffolding in `data/` to ensure future datasets are interoperable.

---

## Allowed write paths

- `data/README.md`
- `data/**/` (dictionary files only)
- `research/**`
- `tickets/T-014-data-dictionary-and-standards.md`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `.github/**`
- `scripts/**`
- `program-clusters/**`
- `entities/**`
- `market/**`
- `go-to-market/**`
- `UNIC/**`

---

## Required outputs

- A new `data/field-standards.md` describing shared columns (ids, as_of, currency, country codes, etc.) and examples.
- Data dictionary markdown files placed next to key CSVs (e.g., `data/entities/schools-dictionary.md`, `data/programs/scholarships-discounts-dictionary.md`) with field definitions and allowed values where constrained.
- Updated `data/README.md` linking to these dictionaries and standards.

---

## Acceptance criteria

- Standards cover IDs, dates, currencies, boolean handling, and text encoding.
- Each dictionary maps fields to descriptions, types, and sample values; notes external code lists if used.
- No files outside allowed paths are modified.
- Ticket status updated when claimed/done with a short “what changed” note.

---

## Notes/Context

Keep formats simple (CSV-friendly) and reference ISO codes where relevant. Aim for interoperability across entities, programs, marketing, and operations tables.

## Completion

- What changed: Added shared field standards plus data dictionaries for entities, programs, marketing, and operations CSVs; updated `data/README.md` with links.
