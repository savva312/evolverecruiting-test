# Creatives inventory data dictionary

Schema reference for `creatives-inventory.csv`. Follow `field-standards.md` for shared conventions.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| creative_id | Stable identifier for the creative asset. | string | `cr-bg-facebook_ads-2025-12-001` | Lowercase, ASCII. |
| channel | Channel where the asset runs. | enum | `facebook_ads` | Allowed: `facebook_ads`, `instagram`, `tiktok`, `google_search`, `google_display`, `youtube`, `linkedin`. |
| format | Ad format. | enum | `video` | Suggested: `video`, `single_image`, `carousel`, `story`, `reel`, `display_banner`, `email`. |
| theme | Core message/theme. | string | `Athens campus lifestyle` | Concise theme label. |
| hook | Leading hook or angle. | string | `Graduate in English with EU degree` | Short phrase. |
| cta | Call to action used. | string | `Apply now` | Text as appears in ad. |
| asset_link | Storage or tracking URL. | string (url) | `https://drive.example.com/creative.mp4` | Prefer durable links; note privacy. |
| notes | Performance notes, targeting, approvals. | string | `Strong for seniors; localized subtitles` | Concise. |
| status | Operational status. | enum | `active` | Use `active`, `paused`, `draft`, `retired`, `test`. |
| as_of | Snapshot date. | date (YYYY-MM-DD) | `2025-12-20` | Required. |
