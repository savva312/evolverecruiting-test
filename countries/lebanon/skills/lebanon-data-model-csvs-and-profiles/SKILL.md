---
name: lebanon-data-model-csvs-and-profiles
description: Lebanon addendum pointing to the global data-model skill and documenting local storage paths for datasets and profiles.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: lebanon
---

# Lebanon addendum: data model CSVs + profiles

Follow the global standards for slugging, CSV formatting, dedupe, and profile templates:
- [Global data-model Skill](/skills/data-model-csvs-and-profiles/SKILL.md)

## Lebanon-specific path conventions

- **CSVs and dictionaries:** store datasets under `countries/lebanon/data/<domain>/` (e.g., `countries/lebanon/data/entities/schools.csv`, `countries/lebanon/data/partners/lebanon-partners.csv`, `countries/lebanon/data/competitors/...`). Place dictionary files beside each CSV when adding new tables.
- **Profiles:** place entity profiles at `countries/lebanon/entities/<type>/profiles/<slug>.md` for each type (`schools`, `agents`, `competitors`, `government-regulators`, `ngos-sgos`, `fairs-events`, `exams-and-curricula`).
- **IDs and paths:** use `entity_id = <type>__<slug>` and keep `profile_path` in the CSV aligned with the profile filename. Use `lb-` prefixes in slugs where it improves clarity.

## Notes

- Capture any Lebanon-only columns in the dataset dictionary next to the CSV so they remain discoverable.
- Create new folders only when the active ticket allows it; reuse existing `countries/lebanon/entities/**` structure.
- Record `last_verified` dates in both structured rows and profiles to track freshness.
