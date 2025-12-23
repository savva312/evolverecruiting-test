---
name: nigeria-data-model-csvs-and-profiles
description: Nigeria addendum to the global data-model Skill, capturing local paths for CSVs, dictionaries, and profiles.
metadata:
  owner: evobuilder
  version: "1.1"
  scope: nigeria
---

# Nigeria addendum: data model CSVs + profiles

Use the global Skill for standards on structure, slug rules, CSV formatting, dedupe, and profile templates:
- [Global data-model Skill](/skills/data-model-csvs-and-profiles/SKILL.md)

## Nigeria-specific path conventions

- **CSVs and dictionaries**: keep datasets under `countries/nigeria/data/<domain>/` (e.g., `countries/nigeria/data/entities/schools.csv`, `countries/nigeria/data/entities/agents.csv`). Store dictionary files beside the CSV (e.g., `schools-dictionary.md`).
- **Profiles**: place profiles at `countries/nigeria/entities/<type>/profiles/<slug>.md` for the relevant type (`schools`, `agents`, `competitors`, `government-regulators`, `ngos-sgos`, `fairs-events`, `exams-and-curricula`).
- **IDs and paths**: align `entity_id = <type>__<slug>` with the profile filename and `profile_path` stored in the CSV.

## Notes

- Capture Nigeria-only fields in the dataset dictionary next to the CSV and keep them consistent with the global standards (encoding, dates, booleans, pipe-delimited multi-values).
- Create new folders only if the active ticket allows changes to that scope.
