# Government regulators data dictionary

Schema reference for `government-regulators.csv`. Apply shared standards from `field-standards.md`.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| regulator_id | Stable unique identifier. | string | `reg-jo-mohesr` | Lowercase, ASCII. |
| name | Regulator or ministry name. | string | `Ministry of Higher Education and Scientific Research` | Official English name. |
| level | Administrative level. | enum | `national` | Use `national`, `regional`, `municipal`. |
| domain | Oversight domain. | enum | `higher_education` | Suggested: `higher_education`, `secondary`, `quality_assurance`, `licensing`, `recognition`, `immigration`, `other`. |
| contact_name | Point of contact. | string | `Admissions Equivalency Unit` | Optional. |
| contact_email | Contact email. | string (email) | `info@mohe.gov.jo` | Lowercase. |
| website | Official URL. | string (url) | `https://mohe.gov.jo/` | `https://` preferred. |
| notes | Scope, processes, links. | string | `Sets Tawjihi minima, oversees foreign credential recognition` | Keep concise. |
| as_of | Snapshot date. | date (YYYY-MM-DD) | `2026-02-04` | Required. |
