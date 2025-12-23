---
name: events-and-fairs
description: Global workflow, checklists, and lead capture standards for planning, executing, and following up on education fairs/events for UNIC and UNIC Athens.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: global
---

# Events and fairs (global)

## Goal

Provide a repeatable, consent-safe playbook to plan, run, and monetize education fairs and events that drive applications to **UNIC Nicosia** and **UNIC Athens**. Country-specific nuances (venue norms, privacy rules, language, payments) should live in each market’s addendum under `/countries/<country>/skills/events-and-fairs/` to reflect the updated country path.

---

## Before you start

1) Read the governing ticket and respect its **Allowed/Forbidden write paths**.  
2) Review repo guardrails when needed:
   - `/skills/ticket-boundaries/SKILL.md`
   - `/skills/markdown-authoring/SKILL.md`
   - `/skills/assets-and-sources/SKILL.md`
3) Check if a country addendum exists for local logistics, payment methods, or consent language; if not, keep this global baseline intact and capture local notes in the country scope.

---

## Scope boundaries

**In scope**
- Planning and executing fairs/webinars/open days where UNIC/UNIC Athens recruits students or influencers (parents, counselors, agents).
- Global standards for staffing, collateral, lead capture, consent, and post-event follow-up.
- QA, reporting, and ROI measurement.

**Out of scope**
- Country-specific regulations, payment flows, or organizer contracts (put in country addenda).
- Generic event theory without operational steps.
- Storing personal data beyond what is explicitly consented and necessary for follow-up.

---

## Principles (apply everywhere)

- **Consent-first**: No lead is contacted without explicit, logged consent (opt-in text + timestamp + collector).
- **Data minimization**: Collect only what is needed to route and follow up; avoid unnecessary sensitive fields.
- **Accessibility & inclusivity**: Signage, forms, and materials accommodate multiple languages where feasible; ensure booth layout is accessible.
- **UNIC vs UNIC Athens clarity**: All collateral and verbal scripts must differentiate campuses (location, admission timelines, pricing, recognition).
- **Source traceability**: Every lead, meeting, and booking is tied to an `event_id` and `organizer`.

---

## End-to-end workflow (timeboxed)

### 1) Targeting and selection (8–12 weeks out)
- Define objective and KPI stack: **leads captured**, **consent rate**, **booked meetings**, **applications started**, **deposit/tuition conversion**.
- Prioritize events by: audience fit (medicine vs non-medical), city priority, historical performance, organizer quality (lead-sharing rules, data protection posture), and booth placement.
- Pre-reserve speaking slots or micro-sessions; clarify AV and Wi‑Fi availability early.
- Build an `event brief` capturing: event name/ID, dates, venue, organizer contacts, target personas, target program clusters, expected footfall, fees, and success definition.

### 2) Pre-event preparation (4–6 weeks out)
- **Staffing plan**: assign roles per shift: Lead Qualifier, Registrar (owns consent + intake quality), Subject Matter/Program SME (medicine vs non-medical), Floater/Rover, and a Digital Wrangler (QR forms, link tests). Ensure coverage for peak hours and breaks.
- **Training**: run a 45–60 min drill on scripts, objection handling (recognition/licensure, pricing, scholarships), eligibility triage, and consent language. Include a micro-demo of the lead form and handoff to country pipelines.
- **Collateral**:
  - Campus comparison one-pager (UNIC Nicosia vs UNIC Athens) with clear pricing ranges and language of instruction.
  - Program-cluster sheets (medicine, CS/data/AI, business, psychology, design).
  - Recognition/licensure quick answers and links.
  - Scholarship/discount overview (if permitted).
  - QR/posters linking to the lead form; short URL + offline backup.
- **Logistics**: booth layout, power/Wi‑Fi, badge scanners (if allowed), swag (only if compliant), signage for consent and privacy notice, local language tags, appointment booking links.
- **Pre-bookings**: outreach to existing leads/partners to pre-schedule meetings; pre-fill slots in a shared calendar with buffer.

### 3) Lead capture standard (global schema)

**Event metadata (required on every record)**
- `event_id`, `event_name`, `organizer`, `city`, `country`, `venue`, `start_date`, `end_date`, `booth_location`, `collector_name`, `collection_channel` (`qr-form`, `badge-scan`, `paper`, `tablet`), `consent_text_version`.

**Person + intent fields (recommended minimum)**
- `lead_id` (stable slug), `persona` (`student`, `parent`, `counselor`, `agent`, `other`), `first_name`, `last_name`, `email`, `phone` (optional/format-checked), `whatsapp_opt_in` (Y/N), `timezone`, `country_of_residence`, `citizenship` (if relevant to visas).
- Academic interest: `program_cluster_interest` (multi-select: `medicine`, `cs-data-ai`, `business`, `psychology`, `design`, `law`, `finance`, `other`), `intended_intake` (term + year), `preferred_campus` (`nicosia`, `athens`, `undecided`), `study_level` (`bachelor`, `master`, `phd`, `other`).
- Qualification screen: `current_school_or_university`, `current_grade_or_year`, `gpa_or_equivalent` (optional), `english_level` (self-reported), `guardian_involved` (Y/N for minors), `funding_readiness` (`exploring`, `applying_scholarships`, `self-funded`, `sponsor`, `loan`).
- Routing + prioritization: `lead_stage_at_capture` (`curious`, `interested`, `ready_to_apply`, `offer_holder`), `hot_flags` (medicine prereqs met, deadline-sensitive, counselor referral), `referral_source` (`walk-up`, `invited`, `partner`, `school`, `social`, `email`, `other`).

**Consent and compliance**
- `consent_to_contact` (Y/N), `consent_timestamp`, `consent_collector`, `preferred_channel` (`email`, `phone`, `whatsapp`, `sms`, `other`), `preferred_contact_window` (local time bands), `data_processing_notice_url`. If Y is not recorded, **do not contact**; only count as “footfall”.
- For minors, record `guardian_consent` (Y/N) and the guardian’s name + contact if provided in compliance with local rules.

**Data handling rules**
- Use QR-first forms; keep 1–2 printed sheets as failover and digitize within 12 hours.
- Validate emails live (format + confirm verbally); avoid typing notes in free text when a structured field exists.
- Deduplicate on `email + event_id` at ingest; preserve originals in an append-only raw log for audit.

### 4) Onsite execution (event days)
- **Booth rhythm**: open with a 30-second qualification, capture consent before deep advising, and steer high-intent leads to same-day or next-day appointments.
- **Micro-sessions**: run short talks (10–15 minutes) on medicine prerequisites, scholarships, or campus differences; capture attendance via QR check-ins.
- **Quality control**: Registrar spot-checks every 30–60 minutes for missing consent, empty critical fields, or unclear handwriting; retrain on the spot.
- **Risk/issue log**: note any data incidents, organizer restrictions (e.g., no QR), competitor positioning heard, and questions to close in post-event comms.

### 5) Post-event follow-up (T+0 to T+30)

**T+0 (same day)**
- Export/sync raw leads; run dedupe; tag by `event_id`.
- Consent audit; remove any records without valid consent from outreach lists.
- Route hot leads (`ready_to_apply`, deadline-sensitive) to country admissions within hours; book slots before leaving the venue.

**T+1–2 days**
- Send personalized recap email per persona with campus-specific CTAs (book meeting, download program sheet, join webinar).  
- Call/WhatsApp (if opted-in) hot leads; confirm application timelines and document checklist.  
- Invite counselors/agents met to a short debrief call; schedule within the week.

**T+3–7 days**
- Nurture sequence: webinar invite, recognition/licensure FAQ, scholarship/discount overview (if applicable), application start guide.  
- Update CRM statuses, owners, and next actions; log no-contact reasons separately.

**T+14–30 days**
- Re-engage non-responders with a lighter cadence (one email + one opted-in WhatsApp/SMS if allowed).  
- Publish a short event summary internally: leads, consent rate, meetings booked, applications started, what to change next time.

Sample cadence (adjust per market rules):
- **Day 1:** Email recap + booking link; call/WhatsApp hot leads.  
- **Day 3:** Webinar invite + campus comparison PDF.  
- **Day 7:** Deadline reminder + application start CTA.  
- **Day 21:** Check-in + offer to pair with current student/ambassador.

### 6) Reporting and ROI
- Track: total leads, consent rate, meetings booked, attendance rate, applications started, offers issued, deposits/tuition, cost per consented lead, cost per application, and per-campus split.
- Compare to baseline targets from the `event brief`; flag deviations with root-cause notes (footfall, staffing gaps, wrong audience, bad booth placement).
- Maintain a post-mortem template: what worked, what failed, content gaps, organizer feedback, and actions before the next event.

### 7) Country addenda (how to extend safely)
- Keep this file global; add **local overrides** under `/countries/<country>/skills/events-and-fairs/`:
  - Local consent/opt-in wording, minor handling, and WhatsApp/SMS legality.
  - Language requirements for signage/forms.
  - Payment/receipt flows if events require on-site fees.
  - Organizer-specific rules (badge scanners, lead file formats, exclusivity clauses).
- Do not duplicate the global schema; extend it with add-on fields or scripts relevant to that market.

---

## Checklists (copy/use)

**Pre-event (summary)**
- [ ] Event brief approved with KPIs, audience, and booth details.
- [ ] Staff assigned, trained, and scheduled with backups.
- [ ] Collateral localized and double-checked for campus clarity.
- [ ] Lead form tested (QR + offline); consent text validated.
- [ ] Appointment links live; calendar shared; time zones confirmed.
- [ ] Logistics confirmed (power, Wi‑Fi, shipping, badges, uniforms, swag policy).

**Onsite**
- [ ] Daily huddle with scripts, targets, and contingency plans.
- [ ] Consent captured before outreach; spot-check form completeness hourly.
- [ ] Hot leads routed immediately; micro-sessions announced with QR check-in.
- [ ] Issue log maintained (data incidents, organizer constraints, competitor intel).

**Post-event**
- [ ] Data synced and deduped; consent failures removed from outreach.
- [ ] Follow-up cadence launched (email + calls/WhatsApp where allowed).
- [ ] CRM updated with owners, stages, and next actions.
- [ ] Post-mortem documented with actions for the next event.

---

## Data model (starter)

Minimum columns for a CSV or CRM import (extend per tool):
- `event_id`, `event_name`, `event_type` (`fair`, `webinar`, `open_day`, `school_visit`)
- `lead_id`, `first_name`, `last_name`, `email`, `phone`, `persona`
- `program_cluster_interest`, `preferred_campus`, `intended_intake`, `study_level`
- `country_of_residence`, `citizenship`, `timezone`
- `referral_source`, `lead_stage_at_capture`, `hot_flags`
- `consent_to_contact`, `consent_timestamp`, `consent_collector`, `preferred_channel`, `preferred_contact_window`
- `collection_channel`, `organizer`, `booth_location`, `collector_name`
- `notes_short` (controlled, factual only), `sources` (links used onsite), `last_verified`

Keep `notes_short` factual; store qualitative observations in the event post-mortem, not in free-form lead notes.
