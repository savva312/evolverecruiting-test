# Funnel metrics data dictionary

Schema reference for `funnel-metrics.csv`. Follow `field-standards.md` for units, periods, and dates.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| stage | Funnel stage label. | enum | `mqls` | Use ordered pipeline: `leads` → `mqls` → `meetings` → `applications` → `offers` → `deposits` → `enrollments`. |
| metric | Metric name. | enum | `conversion_rate` | Use: `count`, `conversion_rate`, `yield`, `cost_per`. |
| value | Weekly target for the metric during the stated period. | decimal | `33` | Counts measured in students; rates stored as 0–100; currency rows in EUR. |
| unit | Unit of measure. | enum | `students` | Use: `students`, `%`, `EUR`. |
| period | Reporting period. | period | `2026-Q1` | Use formats from `field-standards.md`; for weekly cadences store the quarter containing the target. |
| notes | Methodology or source notes. | string | `Definition: ...; Measurement: ...; Source: ...; Target rationale: ...` | Notes must capture definition, measurement system, source-of-truth platform, and reason for the target. |
| as_of | Snapshot date. | date (YYYY-MM-DD) | `2025-12-22` | Required; update whenever a target or definition changes. |

## Stage conventions (Romania)

Romania uses a seven-stage pipeline covering both UNIC Nicosia and UNIC Athens. The stage ordering is mandatory for consistent conversion math:

1. `leads` — new Romania-qualified contacts entering HubSpot (web forms, events, counselor uploads, paid media, agent imports).
2. `mqls` — leads that either score ≥65 in HubSpot or are verified by a counselor/agent as ready for recruiter outreach.
3. `meetings` — consultations scheduled and completed (HubSpot meetings synced to Slate or meetings logged directly in Slate).
4. `applications` — submitted applications in Slate with Romania high school codes or source tags.
5. `offers` — conditional or unconditional offers released after academic review.
6. `deposits` — offers that paid the enrollment deposit within the SLA (Day 14 standard, Day 10 Medicine).
7. `enrollments` — students marked as present during census Week 1 in Banner SIS (both campuses).

When adding metrics, make sure the `stage` value corresponds to the destination state of the metric (e.g., a deposit conversion rate row uses `stage = deposits`). If Romania needs additional intermediate stages (visa ready, housing confirmed, etc.), create a ticket before expanding the enum so downstream automations stay deterministic.

## Notes template

All `notes` cells must follow this pattern so that any reviewer can reconcile the metric quickly:
```
Definition: <who/what is counted and the time window>;
Measurement: <query or filter used>;
Source: <system(s) of record>;
Target rationale: <why the number is set where it is>.
```
