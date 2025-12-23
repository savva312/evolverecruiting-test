# T-449: Serbia — Fix `schools.csv` schema errors (CSV parseability + missing contacts)

Status: done
Type: data
Priority: P1
Dependencies: (none)
Claimed-by: execution-2025-12-22-codex
Claimed-at: 2025-12-22
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Make `countries/serbia/data/entities/schools.csv` valid and reliably parseable, and fix the currently malformed rows.

---

## Context

- File has schema reference:
  - `countries/serbia/data/entities/schools-dictionary.md`
- Known breakage (as of 2025-12-22):
  - At least two rows have fewer columns than the header (CSV parse fails strict checks).
  - Missing contact emails should be filled where publicly available (or left blank while preserving column count).

---

## Allowed write paths

- `countries/serbia/data/entities/schools.csv`
- `executions/**` (optional; notes only)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket file for status updates)

---

## Required outputs

- `countries/serbia/data/entities/schools.csv`

---

## Acceptance criteria

- [x] Every row has the same number of columns as the header (can be verified via Python `csv` module).
- [x] Fixes the malformed rows for:
  - [x] École française de Belgrade (`sch-rs-belgrade-efb-006`)
  - [x] Prva ruska međunarodna škola “Valentina Tereškova” (`sch-rs-belgrade-valentina-tereskova-013`)
- [x] If a public contact email exists, it is populated; otherwise the column is left blank (but present).
- [x] No edits outside allowed write paths.

## What changed

- Restored the missing `contact_email` column entries for École française de Belgrade (`efb.admi@efb.rs`) and Prva ruska međunarodna škola “Valentina Tereškova” (`info@ruskaskola.edu.rs`).
- Ran a Python `csv` parse to confirm all rows now have 10 columns, matching the dictionary schema.
