# UNIC data workspace

This folder centralizes campus-level structured data that all countries should reference instead of duplicating per-market copies.

## Files

- [`programs/unic-programs.csv`](programs/unic-programs.csv) — authoritative UNIC Nicosia + UNIC Athens program inventory.
- [`programs/unic-programs-dictionary.md`](programs/unic-programs-dictionary.md) — schema reference for the shared CSV.

## Usage

- Reference this CSV from country analyses, playbooks, and joins (e.g., scholarships, competitors). Do not recreate per-country `unic-programs.csv` copies.
- Add campus-wide updates here (tuition, intakes, notes) and include an `as_of` date for each row.
- Country-specific supplements (e.g., localized positioning, feeder mappings) should live in each country’s data folder and link back via `program_id`.
