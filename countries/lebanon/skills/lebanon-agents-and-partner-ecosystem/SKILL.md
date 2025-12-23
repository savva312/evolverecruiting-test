---
name: lebanon-agents-and-partner-ecosystem
description: Lebanon addendum to the global agents-and-partner-ecosystem skill, noting local partner emphases, city tags, and storage paths.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: lebanon
---

# Lebanon agents and partner ecosystem (addendum)

Use `/skills/agents-and-partner-ecosystem/SKILL.md` as the **primary workflow** for taxonomy, datasets, privacy rules, and QA. This file only records Lebanon-specific emphases and storage paths.

## How to use
- Run the global workflow for structure, CSV schema, and profile templates.
- Apply the Lebanon notes below when working inside `countries/lebanon/**` tickets.

## Lebanon partner emphases
- **Partner types to prioritize:** generalist agencies with Beirut coverage, medicine-focused consultancies, fair organizers with Lebanon stops, and counseling hubs embedded in international or bilingual schools.
- **City tags:** start with `Beirut`, `Tripoli`, `Sidon/Saida`, `Tyre`, `Zahle`; add regional reach when partners cover Bekaa or North governorates.
- **Program-fit tags:** default to `medicine`, `cs-data-ai`, `business`, and `psychology`; add `design` or `law` only when evidenced in Lebanon-facing marketing.
- **Compliance reminders:** confirm fee transparency, avoid unsourced scholarship claims, and prefer organization-level contacts over personal numbers. Cite `last_verified` dates on all partner profiles and CSV rows.

## Recommended Lebanon file paths (if the ticket allows)
- `countries/lebanon/market/partners/index.md`
- `countries/lebanon/market/partners/profiles/<partner_slug>.md`
- `countries/lebanon/data/partners/lebanon-partners.csv`

## Dataset and profile notes
- Reuse the global taxonomy and dataset schema; keep `partner_id` slugs stable (e.g., `lb-beirut-<partner>`).
- Capture coverage by city and program-fit tags in both the CSV and the profile header.
- Keep risk/compliance notes factual and sourced; route broader agent-governance policy questions back to the global skill.
