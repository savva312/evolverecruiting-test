# UNIC programs data dictionary

Schema reference for the shared `unic-programs.csv` stored at `UNIC/data/programs/`. Apply repo-wide field standards (`field-standards.md` in each country’s data area) for IDs, dates, and encoding.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| program_id | Stable UNIC program identifier. | string | `unic-nic-bsc-cs` | Lowercase, ASCII. |
| campus | Campus offering the program. | enum | `Nicosia` | Use `Nicosia`, `Athens`. |
| program_name | Program title. | string | `BSc Computer Science` | Official catalog name. |
| degree_level | Degree level. | enum | `bachelor` | Suggested: `bachelor`, `master`, `doctoral`, `certificate`, `other`. |
| delivery | Delivery mode. | enum | `on-campus` | Use `on-campus`, `online`, `hybrid`. |
| tuition_eur | Annual tuition in EUR. | decimal | `7500` | Numeric only. |
| intake_months | Months with intakes. | multi-enum | `February;September` | Semicolon-separated month names (Title case). |
| language | Instruction language. | string | `English` | Free text. |
| scholarship_eligibility | High-level scholarship guidance. | string | `Merit scholarships up to 30%` | Summaries only; details in scholarships table. |
| notes | Admissions or positioning notes. | string | `STEM scholarships for priority cohorts` | Concise. |
| as_of | Snapshot date. | date (YYYY-MM-DD) | `2025-12-20` | Required. |
