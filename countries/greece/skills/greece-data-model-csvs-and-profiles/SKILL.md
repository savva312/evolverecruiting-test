---
name: greece-data-model-csvs-and-profiles
description: Greece addendum pointing to the global data-model Skill and documenting local storage paths for datasets and profiles.
metadata:
  owner: evobuilder
  version: "0.2"
  scope: greece
---

# Greece addendum: data model CSVs + profiles

Follow the global standards for slugging, CSV formatting, dedupe, and profile templates:
- [Global data-model Skill](/skills/data-model-csvs-and-profiles/SKILL.md)

## Greece-specific path conventions

- **CSVs and dictionaries**: store datasets under `countries/greece/data/<domain>/` (e.g., `countries/greece/data/entities/schools.csv`, `countries/greece/data/entities/agents.csv`, `countries/greece/data/programs/...`). Place dictionary files beside each CSV when new tables are added.
- **Profiles**: place entity profiles at `countries/greece/entities/<type>/profiles/<slug>.md` for each type (`schools`, `agents`, `competitors`, `government-regulators`, `ngos-sgos`, `fairs-events`, `exams-and-curricula`).
- **IDs and paths**: use `entity_id = <type>__<slug>` and keep `profile_path` in the CSV aligned with the profile filename.

## Notes

- Capture any Greece-only columns in the dataset dictionary next to the CSV so they remain discoverable.
- Create new folders only when the active ticket allows it; reuse existing `countries/greece/entities/**` structure.
