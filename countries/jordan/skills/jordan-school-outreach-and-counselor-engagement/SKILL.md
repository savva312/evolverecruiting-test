---
name: jordan-school-outreach-and-counselor-engagement
description: Jordan addendum to the global school outreach and counselor engagement skill; captures local etiquette, calendar, and consent notes.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: jordan
---

# Jordan addendum: school outreach & counselor engagement

Use `/skills/school-outreach-and-counselor-engagement/SKILL.md` for the end-to-end workflow. Apply these Jordan-specific adjustments.

## Data sources and routing
- Start from school/counselor profiles in `countries/jordan/entities/schools/` and CSVs under `countries/jordan/data/entities/`.
- Tag interactions by city (Amman, Irbid, Zarqa, Aqaba, other) and curriculum (Tawjihi vs IB/IGCSE/American) to tailor messaging.
- Log consent and touchpoints in the country data model (`countries/jordan/skills/jordan-data-model-csvs-and-profiles/`) before syncing elsewhere.

## Language and etiquette
- Default to Arabic for first contact; provide English materials for international/private schools. Confirm preferred language early.
- Avoid in-person visits during Tawjihi exam periods and results weeks; offer virtual counselor briefings instead.
- WhatsApp is common but obtain opt-in before sending follow-ups; some schools prefer email/phone for formal scheduling.

## Visit logistics
- Some public schools require advance approval from principals or directorates; share agenda and attendee names ahead of time.
- Be mindful of gender-specific school rules for staffing and meeting setup; confirm expectations when scheduling.
- Carry concise UNIC vs UNIC Athens comparisons and scholarship summaries cleared by admissions.

## Consent and data protection
- Capture explicit permission before storing counselor or student contacts; log source and timestamp for each opt-in.
- Do not store national ID numbers or passport details in notes; keep records to contact info, program interest, and interaction history.

## Follow-up cadence
- Send Arabic-language recaps within 48 hours of visits or fairs, with English attachments for international schools.
- Schedule webinars/application workshops shortly after exam results when counselors and families have clarity on scores.
