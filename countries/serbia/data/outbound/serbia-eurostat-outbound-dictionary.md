# Serbia outbound mobility — Eurostat extract (data dictionary)

Dataset file: `countries/serbia/data/outbound/serbia-eurostat-outbound.csv`  
As-of (extract run): **2025-12-22**

## What this dataset is

This is a tidy, destination-split extract of **Eurostat learning mobility (tertiary)** for **Serbia (RS) as country of origin**.

Each row represents the number of **mobile students from Serbia enrolled in the host/reporting country** (`host_country_eurostat`) in the given year, for ISCED 2011 **ED5–8 (tertiary)** and **both sexes**.

Important: Eurostat collects this as **inbound mobility by host**. For our purposes, that inbound-by-host view is interpreted as **Serbia outbound mobility by destination**.

## Source links (exact)
- Eurostat dataset (Data Browser): `https://ec.europa.eu/eurostat/databrowser/view/educ_uoe_mobs02/default/table`
- Exact API query used for this extract (JSON):
  - `https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/educ_uoe_mobs02?partner=RS&sex=T&isced11=ED5-8&time=2020&time=2021&time=2022&time=2023&time=2024`

## Filters used (reproducible)
- `source_dataset=educ_uoe_mobs02`
- `partner=RS` (country of origin: Serbia)
- `isced11=ED5-8` (tertiary)
- `sex=T` (both sexes)
- `unit=NR` (number)
- `freq=A` (annual)
- `time=2020..2024`
- `geo=*` (host/reporting country; includes aggregates and RS itself)

## Interpretation notes (read this before using totals)
- **Reporting set, not global census:** Totals created by summing host countries represent “within the Eurostat reporting set”, not worldwide Serbian outbound mobility.
- **Aggregates are present:** `EU27_2020` and `EU28` are aggregate rows. Do **not** sum them together with country rows (double counting).
- **Self-host row is present:** `host_country_eurostat=RS` appears in the extract. For “outbound abroad”, exclude it.
- **2024 is partial:** many host countries do not have a 2024 value in this slice; treat 2024 as *incomplete* for rankings/trends.

## Columns

| Column | Type | Example | Meaning |
|---|---:|---|---|
| `year` | `YYYY` | `2023` | Reference year (annual). |
| `origin_country_iso2` | ISO2 | `RS` | Country of origin (fixed: Serbia). |
| `host_country_eurostat` | Eurostat geo code | `HU`, `DE`, `EU27_2020` | Host/reporting country (destination). Mostly ISO2; may include aggregates. |
| `host_country_name` | text | `Hungary` | Host country label from the API response. |
| `isced11` | code | `ED5-8` | Education level filter used. |
| `sex` | code | `T` | Sex filter used (total). |
| `unit` | code | `NR` | Unit (number). |
| `freq` | code | `A` | Frequency (annual). |
| `count` | integer (blank allowed) | `1986` | Count of mobile students from Serbia enrolled in the host country for the year. Blank = no value published for that host-year in this slice. |
| `status` | code (blank allowed) | `d` | Eurostat observation flag as returned by the API (kept **raw**). Treat any non-empty flag as “use with caution”. |
| `source_dataset` | text | `educ_uoe_mobs02` | Eurostat dataset code. |
| `source_url` | URL | `https://ec.europa.eu/...` | The exact API URL used (repeated for reproducibility). |
| `as_of` | `YYYY-MM-DD` | `2025-12-22` | Snapshot date for when this extract was generated. |

## How to reproduce (minimal)
1. Open the `source_url` above in a browser or download it with `curl`.
2. Use the `geo` and `time` dimensions from the JSON response to convert the dataset into one row per host-year.
3. Write a UTF-8 CSV with the columns above and `as_of=2025-12-22`.

