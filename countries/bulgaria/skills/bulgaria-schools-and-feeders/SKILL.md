---
name: bulgaria-schools-and-feeders
description: Build and maintain Bulgaria-specific profiles and structured datasets for priority secondary-school feeders (and related counselor ecosystems) used to recruit Bulgarian students to UNIC Nicosia and UNIC Athens. Produces per-school Markdown profiles plus CSVs for planning, targeting, and reporting.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: bulgaria
---

# Bulgaria schools and feeders

Use this skill together with the **global standard** in [`skills/schools-and-feeders/SKILL.md`](/skills/schools-and-feeders/SKILL.md), which holds the workflow, CSV fields, privacy rules, and the canonical profile template (`skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md`).

## Bulgaria-specific priorities

- **City sequence by default:** Start with Sofia, Plovdiv, Varna, and Burgas before expanding to regional hubs (e.g., Ruse, Stara Zagora, Pleven, Veliko Tarnovo, Blagoevgrad). Note any deviations in the ticket output.
- **Tiering rubric (0–100 example):**
  - Outbound orientation / counseling capacity (0–25)
  - English intensity or international curriculum alignment (0–25)
  - Program fit with priority clusters (Medicine, CS/Data/AI, Business, etc.) (0–20)
  - Access and receptivity (published visits, fairs, counselor responsiveness) (0–15)
  - City/affluence or pipeline proxy (0–15)
- Document the exact rubric and city coverage in `countries/bulgaria/entities/schools/README.md` and align scores across the CSV and profiles.
