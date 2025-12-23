# Education agents data dictionary

Schema reference for `agents.csv`. Apply shared standards from `../field-standards.md`.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| agent_id | Stable unique identifier for the agency. | string | `ag-lb-beirut-uni-001` | Lowercase, ASCII. |
| name | Agency name. | string | `FuturePath Education` | Use registered/brand name. |
| region | Primary operating region in Lebanon. | string | `Beirut` | City/region text. |
| services | Services offered. | multi-enum | `placements;visa_support;events` | Semicolon-separated; examples: `placements`, `visa_support`, `application_editing`, `events`, `scholarship_guidance`, `accommodation`, `test_prep`. |
| contact_name | Lead contact. | string | `Rana Haddad` | Person responsible for Lebanon. |
| contact_email | Contact email. | string (email) | `petar.dimitrov@example.bg` | Lowercase. |
| primary_markets | Main destination markets served. | multi-enum | `CY;GR;GB` | Use ISO 3166-1 alpha-2; semicolon-separated. |
| notes | Relationship status, specialization, source. | string | `Prefers medical programs; works with Cyprus` | Keep succinct. |
| as_of | Snapshot date. | date (YYYY-MM-DD) | `2025-12-20` | Required for all rows. |
