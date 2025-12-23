# Data field standards

These standards keep CSVs interoperable across recruiting data. Apply them to every dataset unless a data dictionary documents a stricter rule.

## Encoding and nulls
- **Encoding:** UTF-8 for all files; headers on the first row.
- **Nulls:** Leave cells blank for unknown/irrelevant values (no `N/A` or `TBD`).
- **Free text:** Use sentence case; avoid trailing spaces and line breaks.

## Identifiers and keys
- **ID fields:** `*_id` columns are stable, unique strings (ASCII only). Do not recycle IDs after deletion or renames.
- **Natural keys:** Where IDs do not exist yet, combine `{name}+{city}+{country}` patterns consistently until canonical IDs are set.
- **Referential links:** When linking tables, suffix with the referenced entity (e.g., `school_id`, `program_id`).

## Dates, periods, and time
- **Dates:** ISO 8601 `YYYY-MM-DD` (e.g., `2025-09-15`).
- **Date ranges:** Represent start/end as separate columns. Use inclusive ranges unless otherwise specified.
- **Periods:** Use `YYYY`, `YYYY-MM`, or `YYYY-Q#` depending on granularity (e.g., `2025-Q1`).
- **as_of column:** Snapshot date for the record in `YYYY-MM-DD`; required on benchmark or inventory tables.

## Numbers and currency
- **Integers/decimals:** Plain digits with `.` as the decimal separator; no thousands separators.
- **Currency amounts:** Store in EUR when suffixed `_eur` (e.g., `amount_eur`, `tuition_eur`). Keep numeric only.
- **Currency codes:** Use ISO 4217 alpha-3 uppercase (e.g., `EUR`, `USD`) in any `currency` column.

## Categorical and boolean fields
- **Booleans:** `true`/`false` lowercase (unquoted). Avoid `0/1` unless specified.
- **Enumerations:** Document allowed values in each dictionary; prefer lowercase `snake_case` or short phrases.
- **Multi-select lists:** Use semicolons with no spaces (`athens;online`) and order values alphabetically when practical.

## Names, locations, and contact fields
- **Country codes:** ISO 3166-1 alpha-2 for `country` columns (e.g., `JO`, `CY`).
- **Regions/cities:** Free text; follow Jordanian official spellings in English (e.g., `Amman`, `Irbid`).
- **Web/email:** `https://`-prefixed URLs; emails in lowercase ASCII.
- **Phone numbers:** E.164 format if added (e.g., `+359...`).

## Text quality and notes
- **Notes columns:** Keep concise context, source citations, or caveats; avoid narrative paragraphs.
- **Sources:** If a field is derived or estimated, mention the source and method briefly in `notes`.

Adhering to these rules keeps CSVs joinable and ready for automation across entities, programs, marketing, and operations datasets.
