# Channel benchmarks data dictionary

Schema reference for `channel-benchmarks.csv`.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| channel | Channel name. | enum | `meta` | Example: `meta`, `google_search`, `google_display`, `tiktok`, `youtube`, `linkedin`. |
| metric | Metric tracked. | enum | `cpl` | Example: `cpc`, `cpm`, `ctr`, `cpl`, `cpa`. |
| audience | Audience description. | string | `Nigerian undergrad prospects` | Keep concise. |
| value | Metric value. | number | `3.50` | Use EUR values unless specified. |
| unit | Unit of measure. | string | `EUR` | Free text. |
| source | Data source. | string | `Meta ads export` | Mention tool/report. |
| as_of | Snapshot date. | date (YYYY-MM-DD) | `2025-12-20` | Required for all rows. |
