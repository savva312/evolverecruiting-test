# T-263: Lebanon: Houssam Eddine Hariri High School (Saida) profile

- **Status:** done  
- **Type:** content  
- **Priority:** P2  
- **Claimed-by:** work  
- **Claimed-at:** 2025-12-21 10:13:52 UTC  
- **Completed-at:** 2025-12-21 10:13:52 UTC  

## What changed
- Added full high school profile for HHHS (Makassed Saida) with IB DP positioning, USD fee evidence, contact, and 90-day outreach plan.
- Updated Lebanon schools index/readme to include HHHS with tier and links.
- Added structured CSV row for HHHS with curriculum, tier, affordability evidence, and source links.

## Objective
Build a high school profile for **Houssam Eddine Hariri High School (Makassed Saida)** with IB DP positioning, USD fee evidence from the 2025–26 tuition images, counselor contacts, and a 90-day outreach plan. Align the structured data row in `countries/lebanon/data/entities/schools.csv` and surface the school in the Lebanon indexes.

## Allowed write paths
- countries/lebanon/entities/schools/**
- countries/lebanon/data/entities/schools.csv
- tickets/T-230-lebanon-sch-lb-saida-houssam-eddine-hariri-profile.md

## Forbidden write paths
- README.md
- AGENTS.md
- ROADMAP.md
- skills/**

## Required outputs
- New profile at `countries/lebanon/entities/schools/profiles/lb-saida-houssam-eddine-hariri/README.md` following the global high school template.
- Updated `countries/lebanon/entities/schools/README.md` and `countries/lebanon/entities/schools/profiles/README.md` with a link/tier entry for Houssam Eddine Hariri.
- CSV entry for `lb-saida-houssam-eddine-hariri` capturing curriculum, tier, USD affordability evidence, contact(s), and last_verified date.

## Acceptance criteria
- Profile documents identity, curriculum/tracks (incl. IB DP), USD fee evidence (amount + year + source), counselor/contact details, and a 90-day outreach plan.
- CSV holds a single deduplicated row for the school with tier and affordability fields aligned to the profile.
- README and profile index include the school with working links and tier designation.
- Sources use official mak-hhhs.edu.lb pages (tuition-fees and IB DP sections); no edits outside allowed paths.

## Dependencies
- None.

## Notes/Context
- Tuition evidence is currently embedded as images on the tuition-fees page; capture the USD amounts for secondary and cite the source link.
