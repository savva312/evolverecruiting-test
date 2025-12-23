# Schools data dictionary

Schema reference for `schools.csv`. Follow shared rules in `../field-standards.md` for IDs, dates, and encoding.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| school_id | Stable unique identifier for the school. | string | `sch-jo-amman-acs` | Lowercase, ASCII; do not reuse. |
| name | Official school name (English). | string | `American Community School Amman` | Keep full legal/brand name. |
| city | City where the school is located. | string | `Amman` | Use Jordanian spelling in English. |
| region | Governorate/region. | string | `Amman Governorate` | Free text; align with official governorates when possible. |
| type | School category. | enum | `international` | Suggested: `secondary`, `gymnasium`, `vocational`, `international`, `boarding`, `other`. |
| ownership | Governance/ownership model. | enum | `private` | Use `public`, `private`, `foundation`, `other`. |
| contact_name | Primary contact person. | string | `Counseling Office` | Full name; leave blank if unknown. |
| contact_email | Contact email. | string (email) | `admissions@acsamman.edu.jo` | Lowercase; one address only. |
| notes | Context, sources, or partnership fit. | string | `High-fee IB/US pathway; strong medicine affordability signal` | Keep concise. |
| as_of | Snapshot date for the record. | date (YYYY-MM-DD) | `2026-02-04` | See `field-standards.md`. |
