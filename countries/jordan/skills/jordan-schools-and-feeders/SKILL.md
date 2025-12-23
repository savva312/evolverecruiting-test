---
name: jordan-schools-and-feeders
description: Build and maintain Jordan-specific profiles and structured datasets for priority secondary-school feeders (and related counselor ecosystems) used to recruit Jordanian students to UNIC Nicosia and UNIC Athens. Produces per-school Markdown profiles plus CSVs for planning, targeting, and reporting.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: jordan
---

# Jordan schools and feeders

Use this skill together with the **global standard** in [`skills/schools-and-feeders/SKILL.md`](/skills/schools-and-feeders/SKILL.md), which holds the workflow, CSV fields, privacy rules, and the canonical profile template (`skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md`).

## Jordan-specific priorities

- **File locations:**  
  - Profiles: `countries/jordan/entities/schools/profiles/<city>/<school-slug>/README.md`.  
  - CSVs: `countries/jordan/data/entities/schools/jordan-feeder-schools.csv` (or ticket-specific filenames).  
  - Index: `countries/jordan/entities/schools/README.md` documents the rubric and links.
- **City sequence by default:** Amman first, then Irbid/Zarqa/Aqaba before secondary regional hubs; document any deviation in outputs.
- **Tiering lens (0–100 example):** outbound orientation/counseling (0–25); English or international alignment (0–25); program fit (Medicine, CS/Data/AI, Business, etc.) (0–20); access/receptivity (0–15); city/affluence proxy (0–15). Keep rubric visible in the index and aligned between CSV and profiles.

---

## Execution tips (use with the global workflow)
- Build/refresh the CSV first (`countries/jordan/data/entities/schools/jordan-feeder-schools.csv`) and keep `last_verified` populated with sources.
- Maintain an index in `countries/jordan/entities/schools/README.md` with rubric, city coverage, and profile links.
- Profiles stay under `countries/jordan/entities/schools/profiles/<city>/<school-slug>/README.md` using the global template; keep contacts organizational and cite sources.
