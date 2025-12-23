# Competitor programs data dictionary

Schema reference for `competitor-programs.csv`.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| program_id | Stable unique identifier. | string | `prog-ng-med-001` | Lowercase, ASCII. |
| institution | Institution/provider name. | string | `Example International University` | Matches entry in competitors table when applicable. |
| program_name | Program name. | string | `MBBS Medicine` | Full display name. |
| level | Program level. | enum | `bachelor` | Example: `bachelor`, `master`, `foundation`, `short_course`. |
| cluster | Program cluster. | enum | `medicine-md` | Use cluster slugs from `program-clusters`. |
| duration | Program length. | string | `6 years` | Include units. |
| tuition_eur | Tuition in EUR. | number | `12000` | Annual or total; specify in notes. |
| notes | Positioning, scholarships, recognition. | string | `English-taught; clinical rotations in EU.` | Concise. |
| as_of | Snapshot date. | date (YYYY-MM-DD) | `2025-12-20` | Required for all rows. |
