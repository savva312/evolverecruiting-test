# Government regulators data dictionary

Schema reference for `government-regulators.csv`. Apply shared standards from `field-standards.md`.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| regulator_id | Stable unique identifier. | string | `reg-bg-moe-001` | Lowercase, ASCII. |
| name | Regulator or ministry name. | string | `Ministry of Education and Science` | Official English name. |
| level | Administrative level. | enum | `national` | Use `national`, `regional`, `municipal`. |
| domain | Oversight domain. | enum | `higher_education` | Suggested: `higher_education`, `secondary`, `quality_assurance`, `licensing`, `recognition`, `other`. |
| contact_name | Point of contact. | string | `Elena Petkova` | Optional. |
| contact_email | Contact email. | string (email) | `e.petkova@mon.bg` | Lowercase. |
| website | Official URL. | string (url) | `https://www.mon.bg` | `https://` preferred. |
| notes | Scope, processes, links. | string | `Handles diploma recognition; use ENIC-NARIC guide` | Keep concise. |
| as_of | Snapshot date. | date (YYYY-MM-DD) | `2025-12-20` | Required. |
