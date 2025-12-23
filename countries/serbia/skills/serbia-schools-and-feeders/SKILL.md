---
name: serbia-schools-and-feeders
description: Build and maintain Serbia-specific profiles and structured datasets for priority secondary-school feeders (and related counselor ecosystems) used to recruit Serbian students to UNIC Nicosia and UNIC Athens. Produces per-school Markdown profiles plus CSVs for planning, targeting, and reporting.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: serbia
---

# Serbia schools and feeders

Use this skill together with the **global standard** in [`skills/schools-and-feeders/SKILL.md`](/skills/schools-and-feeders/SKILL.md), which holds the workflow, CSV fields, privacy rules, and the canonical profile template (`skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md`).

## Serbia-specific priorities

- **File locations:**  
  - Profiles: `countries/serbia/entities/schools/profiles/<city>/<school-slug>/README.md`.  
  - CSVs: `countries/serbia/data/entities/schools/serbia-feeder-schools.csv` (or ticket-specific filenames).  
  - Index: `countries/serbia/entities/schools/README.md` documents the rubric and links.
- **City sequence by default:** Belgrade first, then Novi Sad and Niš, followed by Kragujevac/Subotica/other regional hubs; document deviations in outputs.
- **Tiering lens (0–100 example):** outbound orientation/counseling (0–25); English or international alignment (0–25); program fit (Medicine, CS/Data/AI, Business, etc.) (0–20); access/receptivity (0–15); city/affluence proxy (0–15). Keep rubric visible in the index and aligned between CSV and profiles.
