# Data directory

This folder houses structured, machine-readable datasets to support recruiting operations for UNIC and UNIC Athens from Bulgaria. All CSVs should use UTF-8 encoding with headers in the first row. Prefer narrow, tidy tables with clear data dictionaries in adjacent notes when fields are non-obvious.

## Structure

- `entities/` — canonical lists of ecosystem actors (schools, agents, regulators, NGOs/SGOs, fairs/events, competitors).
- `programs/` — program inventory for UNIC/UNIC Athens and competitors, plus scholarships or discounts.
- `marketing/` — performance and planning inputs for demand generation (keywords, channel benchmarks, creative inventory).
- `operations/` — operating models and metrics (topic/calendar planning, funnel metrics, budget assumptions).

## Conventions

- CSVs should be additive and timestamped via `as_of` columns when possible.
- Use `id` columns when multiple tables may link (e.g., `entity_id`, `program_id`).
- Leave placeholder values blank rather than using `TBD`; document assumptions in a comment column or execution notes in `/executions/`.
- Keep any sensitive or regulated data out of this repo; note external sources instead.

## Field standards and dictionaries

- Shared standards: [`field-standards.md`](field-standards.md) for IDs, dates, currency, encoding, and enumerations.
- Entities dictionaries: [`entities/schools-dictionary.md`](entities/schools-dictionary.md), [`entities/agents-dictionary.md`](entities/agents-dictionary.md), [`entities/fairs-events-dictionary.md`](entities/fairs-events-dictionary.md), [`entities/competitors-dictionary.md`](entities/competitors-dictionary.md), [`entities/government-regulators-dictionary.md`](entities/government-regulators-dictionary.md), [`entities/ngos-sgos-dictionary.md`](entities/ngos-sgos-dictionary.md).
- Programs dictionaries: [`programs/competitor-programs-dictionary.md`](programs/competitor-programs-dictionary.md), [`programs/scholarships-discounts-dictionary.md`](programs/scholarships-discounts-dictionary.md). The shared UNIC program inventory lives at [`../../UNIC/data/programs/unic-programs.csv`](../../UNIC/data/programs/unic-programs.csv) with its schema at [`../../UNIC/data/programs/unic-programs-dictionary.md`](../../UNIC/data/programs/unic-programs-dictionary.md); reference it instead of keeping local copies.
- Marketing dictionaries: [`marketing/keywords-dictionary.md`](marketing/keywords-dictionary.md), [`marketing/channel-benchmarks-dictionary.md`](marketing/channel-benchmarks-dictionary.md), [`marketing/creatives-inventory-dictionary.md`](marketing/creatives-inventory-dictionary.md).
- Operations dictionaries: [`operations/budget-model-dictionary.md`](operations/budget-model-dictionary.md), [`operations/content-calendar-dictionary.md`](operations/content-calendar-dictionary.md), [`operations/funnel-metrics-dictionary.md`](operations/funnel-metrics-dictionary.md).
