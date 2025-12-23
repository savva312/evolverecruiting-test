# NGOs/SGOs data dictionary

Schema reference for `ngos-sgos.csv`. Apply shared standards from `../field-standards.md`.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| org_id | Stable identifier for the organization. | string | `ngo-ng-ptdf` | Lowercase, ASCII, hyphen-separated. |
| name | Organization name. | string | `Petroleum Technology Development Fund (PTDF)` | Use official/brand name. |
| scope | Geographic coverage. | enum | `national` | Use `national`, `regional`, `state-specific`, or `pan-africa`. |
| focus | Focus areas. | multi-enum | `scholarships;mobility-support;stem` | Semicolon-separated; align with topical themes. |
| audience | Primary student segments. | multi-enum | `postgraduate;stem;low-income` | Semicolon-separated (e.g., `undergraduate;girls;entrepreneurship`). |
| partnership_notes | Partnership or outreach angle. | string | `Targets oil & gas talent; align UNIC MSc Energy + joint webinars.` | Concise, action-oriented. |
| status | Pipeline status. | enum | `priority` | Use `priority`, `prospect`, or `monitor`. |
| last_reviewed | Snapshot date. | date (YYYY-MM-DD) | `2025-12-20` | Required for all rows. |
| sources | Key reference URLs. | multi-enum | `https://ptdf.gov.ng/` | Semicolon-separated URLs; optional if captured elsewhere. |
