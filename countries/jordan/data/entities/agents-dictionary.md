# Education agents data dictionary

Schema reference for `agents.csv`. Apply shared standards from `../field-standards.md`.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| agent_id | Stable unique identifier for the agency. | string | `ag-jo-amman-idp` | Lowercase, ASCII. |
| name | Agency name. | string | `IDP Education Jordan` | Use registered/brand name. |
| region | Primary operating region in Jordan. | string | `Amman` | City/region text. |
| services | Services offered. | multi-enum | `placements;visa_support;events` | Semicolon-separated; examples: `placements`, `visa_support`, `application_editing`, `events`, `scholarship_guidance`. |
| contact_name | Lead contact. | string | `Senior Counselor` | Person responsible for Jordan; leave blank if unknown. |
| contact_email | Contact email. | string (email) | `info@idp.com` | Lowercase. |
| primary_markets | Main destination markets served. | multi-enum | `CY;GR;UK;AU;CA;US` | Use ISO country codes; semicolon-separated. |
| notes | Relationship status, specialization, source. | string | `IELTS-linked pipeline; strong UK/AU/CA/US volume` | Keep succinct. |
| as_of | Snapshot date. | date (YYYY-MM-DD) | `2026-02-04` | Required for all rows. |
