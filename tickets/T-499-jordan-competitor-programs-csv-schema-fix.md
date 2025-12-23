# T-499: Jordan — fix competitor programs CSV schema + seed Jordan-relevant entries

Status: done
Type: data
Priority: P0
Dependencies: (none)
Claimed-by: evoticketresolver_rmf82qr3
Claimed-at: 2025-12-22T20:44:50Z
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Fix `countries/jordan/data/programs/competitor-programs.csv` so it conforms to its data dictionary and is machine-parseable, then seed it with a small, high-value set of Jordan-relevant competitor program rows.

---

## Context

`countries/jordan/data/programs/competitor-programs.csv` currently breaks CSV parsing because `location` values include commas (e.g., `Amman, JO`) without quoting, resulting in inconsistent column counts.

Schema reference:
- `countries/jordan/data/programs/competitor-programs-dictionary.md`

---

## Allowed write paths

- `tickets/T-499-jordan-competitor-programs-csv-schema-fix.md`
- `countries/jordan/data/programs/competitor-programs.csv`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**` (global)
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- `countries/**` (except `countries/jordan/**`)

---

## Required outputs

- `countries/jordan/data/programs/competitor-programs.csv` updated:
  - valid CSV per the dictionary (10 columns, consistent rows)
  - at least 12 seeded rows across top Jordan-relevant competitor programs (Medicine/Health, CS/Data, Business)

---

## Acceptance criteria

- [x] CSV parses with consistent column counts across all rows per `competitor-programs-dictionary.md`.
- [x] Any `location` values containing commas are properly quoted (or reformatted) so the CSV remains valid.
- [x] `tuition_eur` values are numeric only (no currency symbols) and only included when sourced; otherwise omit the row or add a clearly labeled `notes` caveat without inventing numbers.
- [x] All rows include `as_of` in `YYYY-MM-DD`.

---

## What changed

- Rewrote `countries/jordan/data/programs/competitor-programs.csv` to be machine-parseable (10-column schema; quoted comma-containing locations).
- Removed unsourced `tuition_eur` values (left blank) and added notes caveats instead of inventing numbers.
- Seeded 14 Jordan-relevant competitor program rows across Medicine/Health, CS/Engineering, and Business; `as_of` set to `2025-12-22`.
