# Schools data dictionary

Schema reference for `schools.csv`. Follow shared rules in `../field-standards.md` for IDs, dates, and encoding.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| school_id | Stable unique identifier for the school. | string | `sch-lb-beirut-001` | Lowercase, ASCII; do not reuse. |
| name | Official school name (English). | string | `Beirut High School of Mathematics` | Keep full legal/brand name. |
| city | City where the school is located. | string | `Beirut` | Use Lebanese spelling in English. |
| region | Lebanese region/province. | string | `Beirut City` | Free text; align with national regions list when possible. |
| type | School category. | enum | `secondary` | Suggested: `primary`, `secondary`, `gymnasium`, `vocational`, `international`, `other`. |
| ownership | Governance/ownership model. | enum | `public` | Use `public`, `private`, `church/faith`, `foundation`, `other`. |
| contact_name | Primary contact person. | string | `Maria Ivanova` | Full name; leave blank if unknown. |
| contact_email | Contact email. | string (email) | `m.ivanova@example.bg` | Lowercase; one address only. |
| notes | Context, sources, or partnership fit. | string | `STEM focus; active Erasmus+` | Keep concise. |
| as_of | Snapshot date for the record. | date (YYYY-MM-DD) | `2025-12-20` | See `field-standards.md`. |
