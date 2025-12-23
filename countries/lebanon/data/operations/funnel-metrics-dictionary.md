# Funnel metrics data dictionary

Schema reference for `funnel-metrics.csv`. Follow `field-standards.md` for units, periods, and dates.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| stage | Funnel stage label. | enum | `applications` | Suggested: `awareness`, `leads`, `applications`, `offers`, `enrollments`, `retention`. |
| metric | Metric name. | string | `count` | Examples: `count`, `conversion_rate`, `cost_per`, `yield`. |
| value | Metric value. | decimal | `420` | Numeric only. |
| unit | Unit of measure. | string | `students` | Examples: `students`, `%`, `EUR`. |
| period | Reporting period. | period | `2025-Q2` | Use period formats from `field-standards.md`. |
| notes | Methodology or source notes. | string | `Includes both campuses` | Concise. |
| as_of | Snapshot date. | date (YYYY-MM-DD) | `2025-12-20` | Required. |
