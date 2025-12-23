# Government regulators data dictionary

Schema reference for `government-regulators.csv`. Apply shared standards from `../field-standards.md`.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| regulator_id | Stable unique identifier. | string | `reg-ng-nuc-001` | Lowercase, ASCII. |
| name | Regulator or ministry name. | string | `National Universities Commission` | Official English name. |
| level | Administrative level. | enum | `national` | Use `national`, `state`, `local`. |
| domain | Oversight domain. | enum | `quality_assurance` | Suggested: `quality_assurance`, `recognition`, `legalization`, `immigration`, `visas`, `other`. |
| contact_name | Point of contact. | string | `Director, Accreditation` | Optional. |
| contact_email | Contact email. | string (email) | `info@nuc.edu.ng` | Lowercase. |
| website | Official URL. | string (url) | `https://www.nuc.edu.ng/` | `https://` preferred. |
| notes | Scope, processes, links. | string | `Publishes accreditation results and cautions on unapproved universities.` | Keep concise. |
| as_of | Snapshot date. | date (YYYY-MM-DD) | `2025-12-20` | Required. |
