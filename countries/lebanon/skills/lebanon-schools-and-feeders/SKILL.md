---
name: lebanon-schools-and-feeders
description: Identify and prioritize Lebanon feeder schools and pathways that convert to UNIC and UNIC Athens enrollments.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: lebanon
---

# Lebanon schools and feeders

Use this alongside the global playbook in [`skills/schools-and-feeders/SKILL.md`](/skills/schools-and-feeders/SKILL.md) for workflow, CSV fields, privacy rules, and the canonical profile template.

## Lebanon-specific guidance

- **File locations (if the ticket allows):**
  - Profiles: `countries/lebanon/entities/schools/profiles/<city>/<school-slug>/README.md` (use the global high school profile template).
  - CSVs: `countries/lebanon/data/entities/schools/lebanon-feeder-schools.csv` (or ticket-specific filenames).
  - Index: `countries/lebanon/entities/schools/README.md` documents the rubric and links.
- **Default prioritization:** start with Beirut metro (IB, Cambridge, bilingual language schools, top private schools), then Tripoli, Sidon/Saida, Tyre, and Zahle; add Bekaa/North hubs as tickets require.
- **Slugging:** use stable IDs such as `lb-<city>-<school-slug>` and keep `school_id` aligned between the CSV and profile path.
- **Tiering and fit:** reuse the global rubric but highlight program-fit tags (`medicine`, `cs-data-ai`, `business`, `psychology`, `design`) that matter for Lebanon shortlists. Avoid unsourced claims about outcomes.
- **Privacy:** prefer organization-level contacts; include counselor names only when published on official school channels and record `last_verified` dates.
