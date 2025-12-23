# T-261: Lebanon: Collège des Saints-Cœurs Sioufi profile

- **Status:** done  
- **Claimed-by:** work  
- **Claimed-at:** 2025-12-21T10:14:56Z  
- **Type:** content  
- **Priority:** P1  

## Objective
Create a full high school profile for **Collège des Saints-Cœurs Sioufi (Beirut)** using the global high school template. Capture USD contribution evidence ($2,500–$2,600 for lycée in 2024–25), curriculum/track details, counselor contacts, and an outreach plan. Align structured data in `countries/lebanon/data/entities/schools.csv` and update Lebanon school indexes.

## Allowed write paths
- countries/lebanon/entities/schools/**
- countries/lebanon/data/entities/schools.csv
- tickets/T-228-lebanon-sch-lb-beirut-sscc-sioufi-profile.md

## Forbidden write paths
- README.md
- AGENTS.md
- ROADMAP.md
- skills/**

## Required outputs
- New profile markdown at `countries/lebanon/entities/schools/profiles/lb-beirut-sscc-sioufi/README.md` following the global high school template.
- Updated `countries/lebanon/entities/schools/README.md` and `countries/lebanon/entities/schools/profiles/README.md` with links/tier entry for SSCC Sioufi.
- Updated row in `countries/lebanon/data/entities/schools.csv` for `lb-beirut-sscc-sioufi` with curriculum, tier, USD evidence, contacts, and last_verified date.

## Acceptance criteria
- Profile includes identity, curriculum/tracks, USD fee evidence (amount + year), counselor/contact details, and a 90-day outreach plan.
- CSV gains a single, deduplicated row for `lb-beirut-sscc-sioufi` with priority tier and affordability evidence that matches the profile.
- README and profiles index list SSCC Sioufi with working relative links and tier designation.
- Sources are cited with on-domain school links; no changes outside allowed paths.

## Dependencies
- None.

## Notes/Context
- Source fee evidence from the SSCC Sioufi tuition page showing the 2024–25 USD contribution for lycée levels (seconde–terminale).

## What changed (2025-12-21)
- Added full SSCC Sioufi profile with USD contribution evidence, curriculum, contacts, and 90-day outreach plan.
- Updated Lebanon school hub and profiles index to include SSCC Sioufi with links/tier.
- Inserted structured row for `lb-beirut-sscc-sioufi` in `countries/lebanon/data/entities/schools.csv` with affordability evidence and contacts.
