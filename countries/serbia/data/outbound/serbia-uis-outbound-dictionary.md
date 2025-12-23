# Serbia outbound mobility — UNESCO UIS extract (data dictionary)

Dataset file: `countries/serbia/data/outbound/serbia-uis-outbound.csv`  
As-of (extract run): **2025-12-22**

## What this dataset is

This is a tidy, destination-split extract from **UNESCO Institute for Statistics (UIS)**, using the **Bulk Data Download Service (BDDS)** Education OPRI release.

UIS publishes internationally mobile students primarily as **inbound mobility by host country**. By selecting the series “students from Serbia”, we can read the host-country values as **Serbia outbound mobility by destination**.

## Source links (exact)
- UIS Bulk Data Download hub: `https://databrowser.uis.unesco.org/resources/bulk`
- Education OPRI release ZIP used: `https://download.uis.unesco.org/bdds/202509/OPRI.zip`

Files inside the ZIP used for this extract:
- `OPRI_DATA_NATIONAL.csv` (values by `INDICATOR_ID`, `COUNTRY_ID`, `YEAR`)
- `OPRI_COUNTRY.csv` (ISO3 → country name)
- `OPRI_LABEL.csv` (indicator label)

## Indicator used (destination-split Serbia outbound)
- `indicator_id=26614`
- Label (from `OPRI_LABEL.csv`): **Inbound internationally mobile students from Europe: Students from Serbia, both sexes (number)**

Interpretation for recruiting:
- `host_country_iso3` = destination (host) country
- `count` = Serbian internationally mobile students enrolled in that host country (as published by UIS for the indicator above)

## Filters used (reproducible)
- `INDICATOR_ID = 26614`
- `YEAR = 2020..2024`
- `COUNTRY_ID = *` (all host countries published in the release for that indicator-year)

## Interpretation notes / limitations
- **Host codes are ISO3, not ISO2:** `host_country_iso3` uses ISO 3166-1 alpha-3 (e.g., `DEU`, `GRC`, `CYP`).
- **Coverage varies by year:** Not every host publishes values every year; 2024 is notably incomplete in this release slice.
- **Non-integer values exist:** Some countries’ `count` values are published with decimals in the BDDS file; the extract preserves values exactly as published.
- **Do not merge totals with Eurostat:** Use UIS as a broader-coverage cross-check and for destinations not present (or missing) in the Eurostat reporting set.

## Columns

| Column | Type | Example | Meaning |
|---|---:|---|---|
| `year` | `YYYY` | `2023` | Reference year (annual). |
| `origin_country_iso2` | ISO2 | `RS` | Country of origin (fixed: Serbia). |
| `host_country_iso3` | ISO3 | `DEU` | Host/destination country code (ISO3). |
| `host_country_name` | text | `Germany` | Host country label (from `OPRI_COUNTRY.csv`). |
| `indicator_id` | string | `26614` | UIS indicator identifier used for this extract. |
| `indicator_label` | text | `Inbound internationally mobile...` | Indicator label (from `OPRI_LABEL.csv`). |
| `count` | number (blank allowed) | `1289` | UIS-published value for the indicator/host/year (may be integer or decimal). |
| `magnitude` | text (blank allowed) | `NIL` | UIS magnitude field from `OPRI_DATA_NATIONAL.csv` (kept raw). |
| `qualifier` | text (blank allowed) |  | UIS qualifier field from `OPRI_DATA_NATIONAL.csv` (kept raw). |
| `source_release` | text | `UIS BDDS Education OPRI (202509 - September 2025)` | Human-readable release tag. |
| `source_url` | URL | `https://download.uis.unesco.org/...` | Direct URL to the BDDS ZIP used. |
| `as_of` | `YYYY-MM-DD` | `2025-12-22` | Snapshot date for when this extract was generated. |

## How to reproduce (minimal)
1. Download `OPRI.zip` from the `source_url`.
2. Filter `OPRI_DATA_NATIONAL.csv` to `INDICATOR_ID=26614` and `YEAR=2020..2024`.
3. Join `COUNTRY_ID` to `OPRI_COUNTRY.csv` to get `host_country_name`.
4. Export to a UTF-8 CSV with the columns above and `as_of=2025-12-22`.

