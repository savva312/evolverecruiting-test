# Creatives inventory data dictionary

Schema reference for `creatives-inventory.csv`.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| asset_id | Stable asset identifier. | string | `cr-ng-2025-001` | Lowercase, ASCII. |
| asset_name | Asset name. | string | `Medicine testimonial Lagos` | Short label. |
| format | Creative format. | enum | `video` | Example: `image`, `video`, `carousel`, `document`. |
| message_angle | Key message. | string | `Scholarships + visa support` | Keep concise. |
| channel | Channel used. | enum | `meta` | Align to channel taxonomy. |
| target_audience | Intended audience. | string | `Nigeria undergrad` | Free text. |
| status | Asset status. | enum | `ready` | Example: `draft`, `ready`, `paused`, `retired`. |
| source_link | Storage link. | string (url) | `https://example.com/assets/medicine-video.mp4` | Use accessible links. |
| notes | Performance or QA notes. | string | `Strong CTR; reuse in Abuja campaigns.` | Concise. |
| as_of | Snapshot date. | date (YYYY-MM-DD) | `2025-12-20` | Required for all rows. |
