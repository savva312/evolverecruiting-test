# Creatives inventory data dictionary

Schema reference for `creatives-inventory.csv`. Follow `field-standards.md` for shared conventions.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| creative_id | Stable identifier for the creative asset. | string | `cr-jo-meta-2026-01` | Lowercase, ASCII. |
| channel | Channel where the asset runs. | enum | `facebook_ads` | Same allowed set as `channel-benchmarks`. |
| format | Ad format. | enum | `video` | Suggested: `video`, `single_image`, `carousel`, `story`, `reel`, `display_banner`, `email`. |
| theme | Core message/theme. | string | `Athens STEM with Schengen mobility` | Concise theme label. |
| hook | Leading hook or angle. | string | `Earn an EU degree close to home` | Short phrase. |
| cta | Call to action used. | string | `Book a call` | Text as appears in ad. |
| asset_link | Storage or tracking URL. | string (url) | `https://example.com/athens-stem-reel.mp4` | Prefer durable links; note privacy. |
| notes | Performance notes, targeting, approvals. | string | `Captioned in Arabic; strong saves among Amman 17–22` | Concise. |
| status | Operational status. | enum | `active` | Use `active`, `paused`, `draft`, `retired`, `test`. |
| as_of | Snapshot date. | date (YYYY-MM-DD) | `2026-02-04` | Required. |
