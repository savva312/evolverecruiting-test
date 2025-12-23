# Serbia Outbound Mobility Baseline (Eurostat + UIS)

Produced by: UNIC Evolve, **December 20, 2025**  
Last updated: **2025-12-22**

This report turns Serbia outbound mobility from a scaffold into a **sourced baseline** using:
- **Eurostat** (learning mobility / tertiary): destination-split Serbia-origin mobility inside the Eurostat reporting set.
- **UNESCO UIS (BDDS Education OPRI)**: a broader destination view that surfaces hosts missing from the Eurostat slice.

Primary use for enrollment: calibrate **where Serbian students already go** for tertiary study abroad (destination competition set), and size **Greece (Athens)** + **Cyprus (Nicosia)** as destinations in that context.

## 1) Data files (repo)
- Eurostat extract: `countries/serbia/data/outbound/serbia-eurostat-outbound.csv`  
  Dictionary: `countries/serbia/data/outbound/serbia-eurostat-outbound-dictionary.md`
- UIS extract: `countries/serbia/data/outbound/serbia-uis-outbound.csv`  
  Dictionary: `countries/serbia/data/outbound/serbia-uis-outbound-dictionary.md`

## 2) Executive summary (sourced)

**Eurostat reporting-set view (latest near-complete year: 2023):**
- **Serbia→host (ISCED ED5–8; both sexes):** **9,707** (sum of published host-country values; excludes aggregates and host=RS)
- **Top destinations by count:** Hungary (1,986), Germany (1,289), Austria (1,245), Türkiye (786), Slovakia (642), Bulgaria (596), Italy (562), Romania (560), France (343), North Macedonia (332)
- **Greece (EL):** **87** (rank **16**; **0.90%** of the reporting-set total)
- **Cyprus (CY):** **9** (rank **28**; **0.09%**)

**UIS global view (2023):**
- Adds destinations missing (or not published) in the Eurostat slice. In 2023, UIS surfaces **Bosnia and Herzegovina** (1,667) and **Slovenia** (1,490) as major hosts for Serbian students, alongside Hungary/Austria/Germany.

**Enrollment implication (Greece/Cyprus):**
- Serbia→Greece and Serbia→Cyprus are **small** in the observed destination set. Treat Athens/Nicosia growth as a **conversion play against bigger destination competitors** (Central Europe + the region), not as a “large existing Greece/Cyprus demand capture”.

## 3) Sources and methodology (exact)

### 3.1 Eurostat (destination-split within reporting set)
- Dataset code: `educ_uoe_mobs02` (“Mobile students from abroad enrolled by education level, sex and country of origin”)
- Dataset page: `https://ec.europa.eu/eurostat/databrowser/view/educ_uoe_mobs02/default/table`
- API query used (JSON):  
  `https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/educ_uoe_mobs02?partner=RS&sex=T&isced11=ED5-8&time=2020&time=2021&time=2022&time=2023&time=2024`

Filters applied:
- Origin (country of origin): `partner=RS` (Serbia)
- Level: `isced11=ED5-8` (tertiary)
- Sex: `sex=T` (total)
- Unit: `unit=NR` (number)
- Frequency: `freq=A` (annual)
- Years: 2020–2024

Key cautions:
- The Eurostat slice is a **reporting set**, not a global census.
- `EU27_2020` / `EU28` aggregate rows appear; do not sum aggregates with country rows.
- 2024 is **partial** coverage in this slice (many host countries have no value published in the extract), so use 2023 for stable rankings.

### 3.2 UNESCO UIS (BDDS Education OPRI; destination-split)
- Bulk hub: `https://databrowser.uis.unesco.org/resources/bulk`
- Release ZIP used: `https://download.uis.unesco.org/bdds/202509/OPRI.zip`
- Extract logic: filter `OPRI_DATA_NATIONAL.csv` to `INDICATOR_ID=26614` (students from Serbia), and read `COUNTRY_ID` as the **host/destination** (ISO3).

Key cautions:
- Host codes are ISO3 (e.g., `DEU`, `GRC`, `CYP`).
- Coverage varies by year; 2024 is notably incomplete.
- Some values are published with decimals in the BDDS file; the extract preserves them as published.

## 4) Findings (tables)

### 4.1 Eurostat reporting-set totals (Serbia origin; ED5–8; sex=T)
Totals below are computed as the **sum of host-country values** in the extract, excluding aggregates and host=RS.

| Year | Hosts with values | Reporting-set total | Note |
|---:|---:|---:|---|
| 2020 | 31 | 10,416 | Baseline year in this extract |
| 2021 | 32 | 10,375 | Slight decrease |
| 2022 | 32 | 9,676 | Downshift vs 2020–2021 |
| 2023 | 31 | 9,707 | Flat vs 2022 |
| 2024 | 13 | 3,461 | **Partial coverage**; do not use for rankings |

### 4.2 Top destinations (Eurostat; 2023)
Shares are calculated against the 2023 reporting-set total (9,707).

| Rank | Host (geo) | Count | Share |
|---:|---|---:|---:|
| 1 | HU — Hungary | 1,986 | 20.46% |
| 2 | DE — Germany | 1,289 | 13.28% |
| 3 | AT — Austria | 1,245 | 12.83% |
| 4 | TR — Türkiye | 786 | 8.10% |
| 5 | SK — Slovakia | 642 | 6.61% |
| 6 | BG — Bulgaria | 596 | 6.14% |
| 7 | IT — Italy | 562 | 5.79% |
| 8 | RO — Romania | 560 | 5.77% |
| 9 | FR — France | 343 | 3.53% |
| 10 | MK — North Macedonia | 332 | 3.42% |
| 16 | EL — Greece | 87 | 0.90% |
| 28 | CY — Cyprus | 9 | 0.09% |

### 4.3 Greece and Cyprus trend (Eurostat; 2020–2023)
Shares are against the reporting-set total for each year.

| Year | Greece (EL) | EL share | Cyprus (CY) | CY share |
|---:|---:|---:|---:|---:|
| 2020 | 89 | 0.85% | 9 | 0.09% |
| 2021 | 91 | 0.88% | 14 | 0.13% |
| 2022 | 90 | 0.93% | 10 | 0.10% |
| 2023 | 87 | 0.90% | 9 | 0.09% |

### 4.4 Top destinations (UIS; 2023, rounded for readability)
Values shown are **rounded** to the nearest whole number for readability; refer to `countries/serbia/data/outbound/serbia-uis-outbound.csv` for raw published values.

| Rank | Host (ISO3) | Count (rounded) | Note |
|---:|---|---:|---|
| 1 | HUN — Hungary | 1,986 | aligns with Eurostat top destination |
| 2 | BIH — Bosnia and Herzegovina | 1,667 | not present as a published 2023 value in the Eurostat slice |
| 3 | SVN — Slovenia | 1,490 | high-volume regional destination |
| 4 | DEU — Germany | 1,289 | aligns with Eurostat |
| 5 | AUT — Austria | 1,245 | aligns with Eurostat |
| 6 | USA — United States of America | 851 | outside the Eurostat reporting set |
| 7 | SVK — Slovakia | 642 | aligns with Eurostat |
| 8 | BGR — Bulgaria | 596 | aligns with Eurostat |
| 9 | ITA — Italy | 562 | aligns with Eurostat |
| 10 | ROU — Romania | 560 | aligns with Eurostat |
| 21 | GRC — Greece | 87 | small in destination ranking |
| 36 | CYP — Cyprus | 9 | very small in destination ranking |

## 5) How to use this baseline (enrollment actions)
- **Build Serbia destination competitor messaging** around the observed top hosts (Hungary/Austria/Germany + regional destinations), and explicitly address “why UNIC/UNIC Athens vs those”.
- **Treat Greece/Cyprus as niche destinations** in the current outbound set; set expectations accordingly and plan for demand creation, not only capture.
- **Operationalize in CRM/lead forms:** add a “primary destination(s) considered” question; track against the top-host list to validate positioning.
- **Channel prioritization:** focus counselor + agent development in **Belgrade / Novi Sad / Niš**, and ask partners which destination set they most often place students into (use this baseline as the benchmark list).
- **Next upgrades:** add field-of-education splits (where available) and overlay with feeder schools/agents to translate mobility totals into a target account list.
