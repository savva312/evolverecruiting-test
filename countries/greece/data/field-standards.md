# Data field standards (Greece)

Use these standards across Greece CSVs to keep data interoperable with other markets. When a dictionary calls for stricter values, follow that dictionary.

## Encoding and nulls
- **Encoding:** UTF-8 with headers in row one.
- **Nulls:** Leave cells blank for unknown/irrelevant values (avoid `N/A`, `TBD`).
- **Free text:** Sentence case; no trailing spaces or embedded line breaks.

## Identifiers and keys
- **ID fields:** `*_id` values are stable, unique ASCII strings and never re-used.
- **Natural keys:** If IDs are missing, combine `{name}+{city}+{country}` consistently until canonical IDs are issued.
- **Referential links:** When joining tables, suffix IDs with the referenced entity (e.g., `school_id`, `program_id`).

## Dates, periods, and time
- **Dates:** ISO 8601 `YYYY-MM-DD`.
- **Date ranges:** Separate `start_date` / `end_date` columns; ranges are inclusive unless noted.
- **Periods:** Use `YYYY`, `YYYY-MM`, or `YYYY-Q#` based on granularity.
- **as_of:** Snapshot date in `YYYY-MM-DD`; required on benchmarks and inventory tables.

## Numbers and currency
- **Integers/decimals:** Plain digits; `.` as decimal separator; no thousands separators.
- **Currency amounts:** Store numeric EUR values in `_eur` columns (e.g., `tuition_eur`).
- **Currency codes:** ISO 4217 alpha-3 uppercase (e.g., `EUR`, `USD`) when a `currency` column is present.

## Categorical and boolean fields
- **Booleans:** `true` / `false` lowercase (unquoted); avoid `0/1`.
- **Enumerations:** Document allowed values in each dictionary; prefer lowercase `snake_case` or short phrases.
- **Multi-select lists:** Semicolon-separated with no spaces (`athens;online`), ordered alphabetically when practical.

## Names, locations, and contact fields
- **Country codes:** ISO 3166-1 alpha-2 (e.g., `GR` for Greece, `CY` for Cyprus).
- **Regions/cities:** English spellings for Greek locations (e.g., `Athens`, `Thessaloniki`, `Patras`); keep accents consistent where used.
- **Web/email:** URLs prefixed with `https://`; emails lowercase ASCII.
- **Phone numbers:** E.164 format if present (e.g., `+30210...`).

## Text quality and notes
- **Notes columns:** Keep concise context, caveats, or source mentions; avoid narrative paragraphs.
- **Sources:** Cite data origins or estimation methods briefly in `notes` when values are derived.

Applying these rules keeps Greece datasets joinable and ready for automation alongside Bulgaria, Nigeria, and other markets.
