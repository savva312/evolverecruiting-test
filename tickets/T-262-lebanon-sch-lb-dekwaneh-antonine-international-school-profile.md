# T-262: Lebanon: Antonine International School (Dekwaneh) profile

- **Status:** done  
- **Type:** content  
- **Priority:** P1  
- **Claimed-by:** work  
- **Claimed-at:** 2025-12-21T10:13:59Z  

## Objective
Draft a complete profile for **Antonine International School, Dekwaneh (AISD)**, covering curriculum streams, USD solidarity fund for Grades 10–12 ($2,450, 2024–25 table), counselor contacts, and a near-term outreach plan. Sync the structured entry in `countries/lebanon/data/entities/schools.csv` and update Lebanon school indexes.

## Allowed write paths
- countries/lebanon/entities/schools/**
- countries/lebanon/data/entities/schools.csv
- tickets/T-229-lebanon-sch-lb-dekwaneh-antonine-international-school-profile.md

## Forbidden write paths
- README.md
- AGENTS.md
- ROADMAP.md
- skills/**

## Required outputs
- New profile at `countries/lebanon/entities/schools/profiles/lb-dekwaneh-antonine-international-school/README.md` using the global high school template.
- Updated `countries/lebanon/entities/schools/README.md` and `countries/lebanon/entities/schools/profiles/README.md` to list AISD with tier and link.
- CSV row for `lb-dekwaneh-antonine-international-school` with curriculum, tier, USD affordability evidence, contact(s), and last_verified date.

## Acceptance criteria
- Profile includes identity, curriculum/tracks, USD fee evidence (amount + year + link), counselor/contact details, and a 90-day outreach plan.
- CSV contains one deduplicated row for AISD with priority tier and affordability evidence matching the profile.
- README and profile index add AISD with working relative links and tier designation.
- Sources rely on official AISD site pages (tuition/fees and admissions); no edits outside allowed paths.

## Dependencies
- None.

## Notes/Context
- Reference the AISD tuition and solidarity fund schedule page that shows the USD component for Grades 10–12 (2024–25).
- Completed 2025-12-21: Profile drafted, CSV row added, and school indexes updated with AISD entry and tier.
