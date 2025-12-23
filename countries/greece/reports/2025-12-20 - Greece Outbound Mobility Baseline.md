# Greece Outbound Mobility Baseline

## Produced by: UNIC Evolve, December 20, 2025

This report is a scaffold for Greece’s outbound mobility baseline. It outlines the datasets to extract, computation rules, and how to interpret Greece→host flows with a focus on UNIC Athens and UNIC Nicosia relevance.

## 1) Executive summary (working)
- Greece is an EU member with strong Erasmus traditions and sizable degree-mobile cohorts heading to the UK, Western Europe, and neighbouring options. A sourced baseline is needed to quantify recent host rankings and Greece→Cyprus/Greece shares.
- No Greece-origin outbound datasets are yet captured in `countries/greece/data/`. The immediate priority is to extract Eurostat learning mobility (degree) and UNESCO UIS global outbound totals, then compute Greece→Cyprus (CY) and Greece→other key hosts.
- Use this baseline to set practical share targets for UNIC Athens and UNIC Nicosia, to choose priority cities/segments, and to keep recognition/licensure messaging tight for regulated programs.

## 2) Data status and gaps
- **Eurostat learning mobility (`educ_uoe_mobs02`)**: no Greece-origin slice has been extracted; totals, host rankings, and Greece→Cyprus counts are absent.
- **UNESCO UIS**: no UIS outbound totals or destination ranks for Greece captured yet.
- **Field-of-education splits**: no outbound-by-field data stored; needed to prioritise program clusters (business, CS/data, health, etc.).
- **Action**: create the datasets in Section 3 and refresh this report with sourced numbers, dates, and methodology once the extracts are complete.

## 3) Required datasets (to be created under `countries/greece/data/outbound/`)
1. **`countries/greece/data/outbound/greece-eurostat-outbound.csv`**  
   - Fields: `year`, `host_country`, `count`, `note_status`, `source_link`, `as_of`.  
   - Method: Eurostat API `educ_uoe_mobs02`, origin Greece (partner=Greece), level `ED5-8`, sex `T`, unit `NR`; sum numeric host rows, exclude aggregates and host=Greece.
2. **`countries/greece/data/outbound/greece-eurostat-field.csv`**  
   - Fields: `year`, `field_code`, `field_name`, `host_country` (optional), `count`, `note_status`, `as_of`, `source_link`.  
   - Method: Eurostat field-of-education breakdown for origin Greece (ISCED-F 2013) if available; document missing/not-published statuses.
3. **`countries/greece/data/outbound/greece-uis-outbound.csv`**  
   - Fields: `year`, `total_outbound`, `top_destinations` (semicolon list or separate rows), `notes`, `source_link`, `as_of`.  
   - Method: UNESCO UIS outbound degree mobility totals and destination ranks for Greece; cite UIS release year and metadata.

## 4) How to compute headline indicators (once data is in place)
- **Total outbound (Eurostat reporting set):** sum numeric host-country counts for origin Greece; exclude EU aggregates (e.g., EU27_2020) and host=Greece. Treat the sum as “Eurostat reporting-set total,” not a global census.
- **EU vs non-EU split:** use EU27 aggregate as the EU subtotal; subtract from total to estimate non-EU share. Flag hosts with missing/confidential data.
- **Greece→Cyprus/Cyprus→Greece focus:** capture host counts and ranks for **Cyprus (CY)** and any self-hosted Greece mobility if present; compute shares of the Eurostat-set total to size UNIC Nicosia relevance. Track **UK, Germany, Netherlands, Italy** and other common destinations for context.
- **Top destination table:** rank host countries by count for the latest year; include `note_status` for missing/estimated points.

## 5) Interpretation guidance (Greece-specific)
- Greece’s Erasmus footprint can inflate short-term mobility; keep this baseline strictly on **degree mobility** (Eurostat learning mobility definition) and label any short-term indicators separately.
- Recognition/licensure sensitivity is high for regulated programs; pair outbound counts with messaging on degree recognition (CYQAA/HAHE for UNIC) and professional pathways when positioning health/engineering offers.
- Avoid double counting aggregates and be explicit about missing host data—totals and shares should always be described as “within the reporting set.”
- Use city-level insights (Athens, Thessaloniki, Patras, Crete cities) to prioritise school/agent coverage once host rankings clarify demand patterns.

## 6) Next steps
1. Run Eurostat extracts for 2020–2024 (origin Greece) and populate the CSVs in Section 3.
2. Add UIS outbound totals and destination ranking for Greece; reconcile with Eurostat without merging totals.
3. Update this report with sourced totals, Greece→Cyprus/Greece shares, and top destinations; add a concise findings section and link any visualisations.
4. Feed validated numbers into `countries/greece/market/outbound-mobility.md` and Athens go-to-market plans.
