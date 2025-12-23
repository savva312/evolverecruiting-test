# Content calendar data dictionary

Schema reference for `content-calendar.csv`. Apply `field-standards.md` for shared fields.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| month | Month for the plan. | period | `2025-09` | Use `YYYY-MM`. |
| theme | Primary topic/theme. | string | `Offerholder support` | Short description. |
| primary_channel | Lead channel for distribution. | enum | `instagram` | Suggested: `instagram`, `facebook`, `tiktok`, `youtube`, `email`, `blog`, `events`, `agents`. |
| asset_type | Content format. | enum | `video` | Suggested: `video`, `story`, `carousel`, `blog`, `webinar`, `email`, `pdf`, `landing_page`. |
| owner | Responsible person/team. | string | `Content lead` | Free text. |
| status | Workflow status. | enum | `planned` | Use `planned`, `in_progress`, `scheduled`, `published`, `paused`. |
| notes | Additional context or dependencies. | string | `Student testimonial needs approval` | Concise. |
| as_of | Snapshot date. | date (YYYY-MM-DD) | `2025-12-20` | Required. |
