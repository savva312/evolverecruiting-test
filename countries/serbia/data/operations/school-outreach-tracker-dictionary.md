# School outreach tracker data dictionary

Schema reference for `school-outreach-tracker.csv`. Follow `countries/serbia/data/field-standards.md` for IDs, dates, and period formats.

## PII policy (hard rule)

This tracker is strictly **no-PII**. Do **not** store:
- Personal phone numbers, personal email addresses, or social handles for counselors/students
- Names of individual students or personal notes about their situations
- Passport/ID numbers, addresses, birthdates, or any visa/document data

If personal information is needed, record it only inside the approved CRM per UNIC policy—not in this repo.

## Fields

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| school_id | Foreign key to the school entity. | id | `sch-rs-belgrade-isb-001` | Must match `school_id` in `countries/serbia/data/entities/schools.csv`. |
| stage | Current relationship status for the school. | enum | `meeting_scheduled` | Suggested set: `research`, `targeting`, `intro_email_sent`, `call_attempted`, `call_scheduled`, `call_completed`, `meeting_scheduled`, `visit_scheduled`, `visit_completed`, `agent_coordination`, `nurture`, `paused`. Keep values lowercase with underscores. |
| last_touch_date | Most recent interaction date (or leave blank if none yet). | date (YYYY-MM-DD) | `2025-12-19` | Use ISO format; blank allowed only when no outreach has occurred. |
| next_touch_date | Planned next action date. | date (YYYY-MM-DD) | `2026-01-16` | Leave blank only if no follow-up is scheduled. |
| owner | Role/team accountable for the next touch. | string | `Belgrade outreach pod` | Use roles or pods (e.g., `Serbia outreach lead`, `Agent manager (Belgrade)`, `Novi Sad outreach pod`). No personal names. |
| notes | Operational context and next steps. | string | `Counselor confirmed Jan visit; bring scholarships slide.` | Keep concise action notes. No PII or student-specific details. |
| as_of | Date the row was last reviewed/updated. | date (YYYY-MM-DD) | `2025-12-22` | Update whenever the record changes. |

## Usage guidance

- Update the tracker immediately after every touch (email, call, visit, event) so the entire team has a single operational view.
- For multi-touch sequences, keep one row per school and roll the stage forward rather than duplicating rows.
- When a school goes dormant, set `stage = paused` and add the reason in `notes`; reactivate by moving back to the relevant stage.
