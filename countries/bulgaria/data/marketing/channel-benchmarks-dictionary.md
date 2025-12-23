# Channel benchmarks data dictionary

Schema reference for `channel-benchmarks.csv`. Apply shared standards in `field-standards.md`.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| channel | Marketing channel. | enum | `facebook_ads` | Suggested: `facebook_ads`, `instagram`, `tiktok`, `google_search`, `google_display`, `youtube`, `email`, `offline_events`, `agents`. |
| metric | Benchmark metric name. | string | `cpc_eur` | Use lowercase `snake_case` metric keys (e.g., `ctr`, `cvr`, `cpl_eur`). |
| value | Metric value. | decimal | `1.20` | Numeric only. |
| unit | Unit of measure. | string | `%` | Examples: `%`, `EUR`, `leads`, `clicks`. |
| source_period | Timeframe/source window. | string | `2025-Q3` | Use period formats from `field-standards.md`. |
| sample_size | Size of sample used. | integer | `1200` | Leave blank if unknown. |
| notes | Context, targeting, methodology. | string | `BG prospective students; Lookalike 2%` | Concise. |
| as_of | Snapshot date. | date (YYYY-MM-DD) | `2025-12-20` | Required. |
