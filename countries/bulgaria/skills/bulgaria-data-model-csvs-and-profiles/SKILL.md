---
name: bulgaria-data-model-csvs-and-profiles
description: Bulgaria addendum to the global data-model Skill, capturing local paths and where to place CSVs, dictionaries, and profiles.
metadata:
  owner: evobuilder
  version: "1.1"
  scope: bulgaria
---

# Bulgaria addendum: data model CSVs + profiles

Use the global Skill for standards on structure, slug rules, CSV formatting, dedupe, and profile templates:
- [Global data-model Skill](/skills/data-model-csvs-and-profiles/SKILL.md)

## Bulgaria-specific path conventions

- **CSVs and dictionaries**: keep datasets under `countries/bulgaria/data/<domain>/` (e.g., `countries/bulgaria/data/entities/schools.csv`, `countries/bulgaria/data/entities/agents.csv`). Store dictionary files beside the CSV (e.g., `schools-dictionary.md`) and reuse `countries/bulgaria/data/field-standards.md`.
- **Profiles**: place profiles at `countries/bulgaria/entities/<type>/profiles/<slug>.md` for the relevant type (`schools`, `agents`, `competitors`, `government-regulators`, `ngos-sgos`, `fairs-events`, `exams-and-curricula`).
- **IDs and paths**: align `entity_id = <type>__<slug>` with the profile filename and `profile_path` stored in the CSV.

## Notes

- Add Bulgaria-only fields to the dataset dictionary next to the CSV and keep them consistent with the global standards (encoding, dates, booleans, pipe-delimited multi-values).
- Create new folders only if the active ticket allows changes to that scope.
