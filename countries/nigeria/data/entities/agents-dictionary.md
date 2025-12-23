# Education agents data dictionary

Schema reference for `agents.csv`. Apply shared standards from `../field-standards.md`.

**Non-PII rule:** do not store personal phone numbers or personal emails in this dataset. Use role-based inboxes only (e.g., `info@`, `admissions@`) or leave contact fields blank.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| agent_id | Stable unique identifier for the agency. | string | `ag-ng-lagos-001` | Lowercase, ASCII. |
| name | Agency name. | string | `FuturePath Education` | Use registered/brand name. |
| region | Primary operating region in Nigeria. | string | `Lagos` | City/region text. |
| services | Services offered. | multi-enum | `placements;visa_support;events` | Semicolon-separated; examples: `placements`, `visa_support`, `application_editing`, `events`, `scholarship_guidance`. |
| contact_name | Role-based contact label (avoid personal PII). | string | `Partnerships Desk` | Use shared roles only; leave blank if only personal contacts are available. |
| contact_email | Role-based inbox only (avoid personal PII). | string (email) | `info@example.ng` | Use shared addresses only (e.g., `info@`, `admissions@`); leave blank otherwise. |
| primary_markets | Main destination markets served. | multi-enum | `CY;GR;UK` | Use ISO country codes; semicolon-separated. |
| notes | Relationship status, specialization, source. | string | `Prefers medicine programs; Cyprus experience` | Keep succinct. |
| as_of | Snapshot date. | date (YYYY-MM-DD) | `2025-12-20` | Required for all rows. |
