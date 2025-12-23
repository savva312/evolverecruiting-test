---
name: lebanon-schools-and-counselor-mapping
description: Map Lebanon secondary schools, counselor relationships, and visit history to guide outreach sequencing.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: lebanon
---

# Lebanon schools and counselor mapping

Use with the global workflow in [`skills/schools-and-feeders/SKILL.md`](/skills/schools-and-feeders/SKILL.md), which covers the canonical steps, CSV fields, privacy rules, and profile template.

## Lebanon-specific guidance

- **Co-locate counselor notes:** keep counselor/access details inside the same profiles and CSV rows you create for feeders (`countries/lebanon/entities/schools/profiles/<city>/<school-slug>/README.md` and `countries/lebanon/data/entities/schools/lebanon-feeder-schools.csv`, unless the ticket specifies otherwise).
- **Coverage summaries:** log visit history, responsiveness, and last-verified dates in `countries/lebanon/entities/schools/README.md` so tiering and freshness are visible.
- **Prioritization:** focus on Beirut international/bilingual schools first, then Tripoli and Sidon/Saida, followed by Zahle and other regional hubs. Note which counselors support Medicine vs non-medical pathways to route UNIC Nicosia vs UNIC Athens messages.
- **Privacy:** prefer role-based contacts; include individual counselor names only when officially published by the school and avoid personal phone numbers. Capture `last_verified` for each contact touchpoint.
