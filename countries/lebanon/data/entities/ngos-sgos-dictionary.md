# NGOs and SGOs data dictionary

Schema reference for `ngos-sgos.csv`. Follow `field-standards.md` for shared conventions and keep rows aligned with the profiles in `../../entities/ngos-sgos/profiles/`.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| org_id | Stable identifier for the organization. | string | `ngo-lb-amideast` | Lowercase, ASCII. |
| name | Organization name. | string | `AMIDEAST Lebanon` | Full name used in index/profile. |
| scope | Geographic or community scope. | enum | `national`, `camp-focused`, `diaspora-linked` | Use one of: `national`, `camp-focused`, `diaspora-linked`, `regional-hub`. |
| focus_area | Main service type. | enum | `advising` | Use one of: `advising`, `scholarships`, `refugee_support`, `career_skills`, `humanitarian_education`. |
| audience | Primary student segments served. | string | `Lebanese + Palestinian/Syrian refugees` | Keep concise (<=120 chars). |
| partnership_notes | Key partnership angle or ask. | string | `Co-host webinars + fee waivers for EducationUSA advisees` | Summarize why UNIC should engage. |
| status | Engagement status/priority. | enum | `priority-high` | Suggested: `priority-high`, `priority-medium`, `watchlist`. |
| last_reviewed | Snapshot date for the row. | date (YYYY-MM-DD) | `2025-12-20` | Update when profiles change. |
