# NGOs and SGOs data dictionary

Schema reference for `ngos-sgos.csv`. Follow `field-standards.md` for shared conventions.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| org_id | Stable identifier for the organization. | string | `ngo-rs-educ-001` | Lowercase, ASCII. |
| name | Organization name. | string | `Serbian Education NGO` | Full name. |
| focus | Primary focus area. | enum | `scholarships` | Suggested: `scholarships`, `career_guidance`, `study_abroad`, `youth_development`, `community_outreach`, `other`. |
| region | Primary region served. | string | `Novi Sad` | City/region free text. |
| contact_name | Point of contact. | string | `Jelena Marković` | Optional. |
| contact_email | Contact email. | string (email) | `jelena.markovic@example.rs` | Lowercase. |
| website | Organization URL. | string (url) | `https://example.org` | `https://` preferred. |
| notes | Partnership or program notes. | string | `Runs STEM mentoring; partner-ready` | Keep concise. |
| as_of | Snapshot date. | date (YYYY-MM-DD) | `2025-12-20` | Required. |
