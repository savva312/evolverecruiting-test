# Greece data directory

This folder houses structured, machine-readable datasets to support recruiting operations for UNIC and UNIC Athens from Greece. All CSVs should use UTF-8 encoding with headers in the first row. Prefer narrow, tidy tables with clear data dictionaries in adjacent notes when fields are non-obvious.

For a live catalog of Greece datasets and notes, see the [data index](./index.md).

## Structure

- `entities/` — canonical lists of ecosystem actors (schools, agents, regulators, NGOs/SGOs, fairs/events, competitors). Currently populated with CSVs for `schools`, `agents`, `government-regulators`, and `ngos-sgos`; all other entity datasets should be added via future tickets.
- `programs/` — program inventory for UNIC/UNIC Athens and competitors, plus scholarships or discounts. No Greece-local program CSVs exist yet; rely on shared UNIC program files until a ticket creates Greece-specific views.
- `marketing/` — performance and planning inputs for demand generation (keywords, channel benchmarks, creative inventory). This folder is a placeholder; first datasets should focus on channel benchmarks and campaign calendars.
- `operations/` — operating models and metrics (topic/calendar planning, funnel metrics, budget assumptions). This folder is a placeholder; use it for recurring operational dashboards once Greece datasets mature.

## Conventions

- CSVs should be additive and timestamped via `as_of` columns when possible.
- Use `id` columns when multiple tables may link (e.g., `entity_id`, `program_id`).
- Leave placeholder values blank rather than using `TBD`; document assumptions in a comment column or execution notes in `/executions/`.
- Keep any sensitive or regulated data out of this repo; note external sources instead.

## Field standards and dictionaries

Use [`field-standards.md`](./field-standards.md) for shared columns (IDs, dates, currencies, booleans) before adding new tables. Add Greece-specific dictionaries alongside each CSV as you populate this area (e.g., `entities/schools-dictionary.md`, `marketing/keywords-dictionary.md`). Mirror the Bulgaria structure for consistency, but keep definitions Greece-scoped.

The UNIC program inventory is centralized at [`../../UNIC/data/programs/unic-programs.csv`](../../UNIC/data/programs/unic-programs.csv) with its schema at [`../../UNIC/data/programs/unic-programs-dictionary.md`](../../UNIC/data/programs/unic-programs-dictionary.md); reference that shared file instead of creating a local copy here.

## Immediate follow-up data actions

- Assign named owners and confirm freshness for each dataset in the [data index](./index.md), especially `entities/schools.csv` and `entities/agents.csv`.
- Create and link per-table dictionary files (starting with schools, agents, regulators, and NGOs/SGOs) so column meanings stay consistent with the global data-model Skill.
- Decide on first marketing and operations datasets for Greece (e.g., channel benchmarks, campaign calendar) and open tickets to populate those tables using the shared field standards.
- Plan and ticket additional entity datasets (competitors, events/fairs, exams and curricula) so Greece coverage matches other priority markets.
