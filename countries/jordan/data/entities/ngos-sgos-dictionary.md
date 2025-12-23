# NGOs and SGOs data dictionary

Schema reference for `ngos-sgos.csv`. Follow `field-standards.md` for shared conventions.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| org_id | Stable identifier for the organization. | string | `ngo-jo-amman-cpf` | Lowercase, ASCII. |
| name | Organization name. | string | `Crown Prince Foundation` | Full name. |
| focus | Primary focus area. | enum | `scholarships` | Suggested: `scholarships`, `career_guidance`, `study_abroad`, `youth_development`, `community_outreach`, `other`. |
| region | Primary region served. | string | `Amman` | City/region free text. |
| contact_name | Point of contact. | string | `Scholarship Office` | Optional. |
| contact_email | Contact email. | string (email) | `info@cpf.jo` | Lowercase. |
| website | Organization URL. | string (url) | `https://www.cpf.jo/` | `https://` preferred. |
| notes | Partnership or program notes. | string | `STEM and youth programmes with scholarship funding` | Keep concise. |
| as_of | Snapshot date. | date (YYYY-MM-DD) | `2026-02-04` | Required. |
