---
name: bulgaria-agents-and-partner-ecosystem
description: Bulgaria addendum to the global agents-and-partner-ecosystem skill, capturing country-specific partner types, tags, and file paths for UNIC and UNIC Athens recruiting work.
metadata:
  owner: evobuilder
  version: "1.1"
  scope: bulgaria
---

# Bulgaria agents and partner ecosystem (addendum)

Use the **global** skill at `/skills/agents-and-partner-ecosystem/SKILL.md` for workflow, templates, taxonomy, and privacy rules. Apply this addendum only for Bulgaria-specific partner types, tags, and storage paths.

## How to use

- Follow the global procedure for building indexes, profiles, and CSVs; do not duplicate that guidance here.
- Use the Bulgaria-specific partner emphases and file locations below when executing tickets scoped to `countries/bulgaria/**`.

## Bulgaria-specific partner emphases

- **Partner types to watch:** generalist agencies with Sofia/Plovdiv coverage; medicine-specialist agencies (often with interview prep add-ons); fair organizers (e.g., World Education Fair/Integral and city tours); counseling consultancies embedded in top language schools; school-network career centers when they operate separately from the school brand.
- **City tags:** prioritize `Sofia`, `Plovdiv`, `Varna`, `Burgas`, `Ruse` (add others if evidenced). Capture whether coverage is in-person or remote.
- **Program-fit tags:** keep `medicine`, `cs-data-ai`, `business`, `psychology`, `design` as defaults; add `law` or `hospitality` only if the partner actively markets those routes from Bulgaria.
- **Evidence reminders:** validate fair organizers via exhibitor lists and prior event schedules; confirm agency services through their own pages before citing.
- **Compliance cues:** Bulgaria partners should acknowledge GDPR; flag if fee/commission policies are unclear or if they promote rebates.

## Recommended Bulgaria file paths

Use these when permitted by the ticket:

- `countries/bulgaria/entities/agents/README.md` (primary index pointing to profiles and CSV)
- `countries/bulgaria/entities/agents/profiles/<partner_slug>.md`
- `countries/bulgaria/data/entities/agents.csv` (canonical partner list)
- `countries/bulgaria/data/entities/agents-dictionary.md` (schema for `agents.csv`)

## Quick CSV and profile notes

- `agent_id` should follow the dictionary pattern (e.g., `ag-bg-sofia-uni-001`) and remain stable even if the profile slug changes.
- In profiles, include activation notes specific to Bulgaria fairs (timing, cities) and Bulgarian-language collateral needs.

## Done reminder

- Bulgaria outputs should link back to the global skill and use its taxonomy; only the Bulgaria-specific tags and paths above should differ.
