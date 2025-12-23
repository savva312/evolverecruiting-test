# Funnel metrics data dictionary

Schema reference for `funnel-metrics.csv`. Follow `field-standards.md` for units, periods, and dates.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| stage | Funnel stage label. | enum | `applications` | Use: `awareness`, `leads`, `applications`, `offers`, `deposits`, `enrollments` (and optional: `starts`, `show_ups`). |
| metric | Metric name. | enum | `count` | Use: `count`, `conversion_rate`, `cost_per`, `yield`. |
| value | Metric value. | decimal | `420` | Numeric only; leave blank when unknown or when using this file as a reporting skeleton. |
| unit | Unit of measure. | enum | `students` | Use: `students` for `count`; `%` for `conversion_rate` and `yield` (stored as 0-100); `EUR` for `cost_per`. |
| period | Reporting period. | period | `2026-Q1` | Use period formats from `field-standards.md` (recommended: `YYYY-Q#` or `YYYY-MM`). |
| notes | Methodology or source notes. | string | `Includes both campuses` | Required in practice: define inclusions/exclusions and the exact numerator/denominator for rates. |
| as_of | Snapshot date. | date (YYYY-MM-DD) | `2025-12-22` | Required; snapshot date for when the row was last verified/updated. |

## Stage conventions (Bulgaria)

Recommended core stages (required for weekly scorecards):
- `awareness`
- `leads`
- `applications`
- `offers`
- `deposits`
- `enrollments`

Optional stages (add when the operation can measure them consistently):
- `starts` (first-day show-up / census start)
- `show_ups` (event show-ups; if tracked separately from starts)
