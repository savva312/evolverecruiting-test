# Funnel metrics data dictionary

Schema reference for `funnel-metrics.csv`. Follow `field-standards.md` for periods and numeric formats.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| period | Reporting period. | period | `2026-Q1` | Use `YYYY`, `YYYY-Q#`, or `YYYY-MM`. |
| lead_volume | Number of new leads. | integer | `1800` | Numeric only. |
| inquiries_to_apps | Conversion rate from inquiry to application. | decimal | `0.18` | Expressed as proportion (0–1). |
| apps_to_offers | Conversion rate from application to offer. | decimal | `0.65` | Proportion. |
| offers_to_deposits | Conversion rate from offer to deposit. | decimal | `0.32` | Proportion. |
| deposits_to_enrols | Conversion rate from deposit to enrolled. | decimal | `0.9` | Proportion. |
| notes | Context or anomalies. | string | `Ramadan impacted Mar lead-to-app` | Concise. |
| as_of | Snapshot date. | date (YYYY-MM-DD) | `2026-02-04` | Required. |
