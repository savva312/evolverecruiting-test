# School outreach tracker data dictionary

Schema reference for `school-outreach-tracker.csv`. Apply `countries/bulgaria/data/field-standards.md` for shared rules.

## PII policy (hard rule)

This table is **no-PII by design**. Do **not** store:
- Personal phone numbers (mobile), personal email addresses, or personal social handles
- Names of individual counselors/teachers/students (use roles only)
- Dates of birth, passport/ID numbers, home addresses, visa or immigration documents
- Any sensitive notes about minors or individual student situations

If personal details are required for follow-up, keep them in the official CRM or approved system of record under UNIC policy—**not** in this repo.

## Fields

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| touch_id | Unique ID for the interaction record. | id | `touch-bg-2026-01-15-001` | Recommended format: `touch-bg-YYYY-MM-DD-###` (sequential per day). |
| school_id | Foreign key to the school entity. | id | `sch-bg-sofia-american-college-of-sofia` | Must match `school_id` in `countries/bulgaria/data/entities/schools.csv`. |
| interaction_date | Date the interaction occurred (or is scheduled, if logged in advance). | date (YYYY-MM-DD) | `2026-01-15` | Use ISO date format. |
| interaction_type | What happened. | enum | `intro_email` | Suggested: `intro_email`, `follow_up_call`, `counselor_meeting`, `student_presentation`, `school_visit`, `fair_or_event`, `virtual_session`, `other`. |
| channel | How it happened. | enum | `email` | Suggested: `email`, `phone`, `in_person`, `video_call`, `messaging_app`, `event_platform`. |
| campus_focus | Which campus was positioned in this interaction. | enum | `both` | Use `nicosia`, `athens`, `both`. |
| school_stage | Current relationship stage at time of interaction. | enum | `meeting_scheduled` | Suggested: `targeted`, `contacted`, `meeting_scheduled`, `visited`, `engaged`, `active_referrer`, `paused`, `closed`. |
| outcome | Result of this interaction. | enum | `meeting_booked` | Suggested: `no_response`, `connected`, `information_sent`, `meeting_booked`, `visit_confirmed`, `presentation_delivered`, `reschedule_requested`, `declined`. |
| next_step | Next action to move the relationship forward. | string | `Send counselor toolkit + propose 2 dates` | Keep role-based and action-based; no names, emails, phones. |
| next_step_due | Due date for the next step. | date (YYYY-MM-DD) | `2026-01-20` | Blank if no next step. |
| owner_role | Who owns the next step (role/team, not a person). | string | `Bulgaria outreach lead` | Examples: `Bulgaria outreach lead`, `Athens admissions rep`, `Marketing`. |
| trip_id | Optional grouping for on-the-ground travel blocks. | id | `trip-bg-2026-01-sofia` | Free text but keep stable; blank for non-trip activity. |
| notes | Short context, constraints, or follow-up details. | string | `Requested virtual session for grade 12 in Feb` | No personal data; no student-specific notes. |
| as_of | Date the record was last reviewed/updated. | date (YYYY-MM-DD) | `2026-01-15` | Required for operational hygiene. |

