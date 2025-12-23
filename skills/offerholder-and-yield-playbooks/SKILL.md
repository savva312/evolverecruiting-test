---
name: offerholder-and-yield-playbooks
description: Global offerholder-to-enrolment workflow with cadences, channel mix, objection handling, SLAs, consent rules, and required artifacts that each country extends via a local addendum.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: global
license: Proprietary (UNIC Evolve internal)
---

# Offerholder and yield playbooks (global skill)

## Purpose
Create a **repeatable, compliant, multi-channel process** that turns offers into enrolments for UNIC and UNIC Athens. This global baseline keeps workflows, cadences, and data standards consistent while letting each country add local compliance or channel nuances in its country directory.

## When to use
Invoke this skill when a ticket requires:
- Offerholder or admitted-student conversion plans across any market.
- Nurture cadences after offer release, conditional acceptance, or scholarship notification.
- Objection-handling scripts and FAQ handling for cost, visas, or recognition.
- Deposit and document chase workflows with SLAs and logging standards.
- Channel mix and consent guidance for email/SMS/WhatsApp/voice and counselor handoffs.

## Hard constraints
1) **Stay ticket- and country-scope aligned.** Keep global guidance here; country-specific rules live under `/countries/<country>/...` addenda and must not be duplicated.
2) **Consent-first.** Assume GDPR-level consent; only use channels with explicit opt-in and document timestamps, source, and channel allowed.
3) **No speculative promises.** Use only verified program facts (deadlines, fees, recognition, scholarships); flag unknowns instead of guessing.
4) **SLA discipline.** Define owners and response times; escalate when SLAs are breached and log every touch.
5) **Separation of facts vs. tactics.** Keep source references for claims; clearly label assumptions or tests.

## Inputs
- Offer file or CRM export with: applicant ID, program/cluster, intake term, offer type (conditional/unconditional), deadline, deposit amount, scholarship status.
- Consent log by channel (email/SMS/WhatsApp/voice/agent).
- Country addendum (local compliance, channel viability, working hours, language).
- Deadlines and capacity constraints from program owners.
- FAQs/objection bank and current pricing/recognition sources.

## Outputs
- Offerholder conversion plan (markdown) with timeline, owners, SLAs, and channel mix.
- Cadence templates by stage (post-offer, pre-deposit, visa/documents, pre-arrival).
- Script/copy blocks for email, SMS/WhatsApp, and calls (cluster-agnostic; to be localized per country addendum).
- Objection handling guide mapped to data-backed answers and deflection paths.
- Data/CRM logging schema and QA checklist.

## End-to-end workflow (global baseline)
1) **Day 0 — Offer issued**
   - Trigger: offer letter sent; set `offer_status=Offered`, capture `offer_deadline`, `deposit_due`, `conditions`.
   - Auto-enroll into post-offer cadence based on persona (student/parent/agent) and program cluster.
2) **Day 0–2 — Acknowledgement and clarity**
   - Email: offer summary, next steps, deposit amount, deadline, required documents, recognition links, visa guidance link, counselor contact.
   - SMS/WhatsApp (if consent): short confirmation and link to portal/next-step checklist.
   - Call attempt within 24–48h for high-intent personas; leave voicemail + follow-up SMS if unreachable.
3) **Day 3–14 — Decision support**
   - Weekly webinar/group Q&A invite; reminder 24h prior.
   - Share program outcomes (placements/alumni), scholarship terms, accommodation guidance.
   - Route nuanced queries to program lead; log handoff and due-back date.
4) **Day 10–deadline — Deposit and docs chase**
   - Reiterate deposit mechanics, acceptable payment methods, and receipt upload path.
   - Checklist for conditions (transcripts, English tests, passport, photos); surface country-specific document rules in addenda.
   - Escalate to phone call if no engagement after 2 touchpoints; involve agents/counselors where applicable.
5) **Post-deposit — Visa/enrolment prep**
   - Send visa packet (required docs, processing times, appointment tips), accommodation options, travel timeline.
   - Pre-arrival tasks: orientation registration, tuition balance dates, emergency contacts.
6) **Pre-arrival — Warm welcome**
   - Welcome series with campus/athens differentiation, arrival-day logistics, and academic onboarding.
7) **Continuous QA**
   - Weekly pipeline review: offer-to-deposit, deposit-to-enrolment, visa approvals.
   - SLA checks on response times and unattended offers; trigger recovery cadences.

## Channel mix and cadence templates (sample, adjust per country addendum)

### Baseline cadence (offer to deposit)
| Day | Channel | Content | Owner | SLA/Next step |
| --- | --- | --- | --- | --- |
| 0 | Email | Offer summary, deadline, deposit amount, portal link, counselor contact | Admissions ops | Send within 2h of offer |
| 1 | SMS/WhatsApp | “Offer sent — here’s your next step + deadline” | Admissions ops | If unopened email after 24h |
| 2 | Call | Confirm receipt, answer key questions, schedule Q&A | Counselor/agent | 2 call attempts over 2 days |
| 4 | Email | Program outcomes, recognition/visa link, FAQ | Admissions ops | Personalize by cluster |
| 7 | SMS/WhatsApp | Deposit reminder + payment options | Admissions ops | Escalate to call if no response |
| 10 | Call | Objection handling, payment support | Counselor/agent | Escalate ticket if unreachable |
| 14 | Email | Scholarship/financing guidance, accommodation starter | Admissions ops | Include self-serve links |
| 17 | SMS/WhatsApp | Deadline countdown + “book a call” link | Admissions ops | Move to intensive if silent |
| 21 | Email | Last-call before deadline; checklist recap | Admissions ops | CC agent/parent if consented |

### Intensive cadence (deadline ≤10 days or silent)
- 3 touches across 5 days: Day 0 email + SMS, Day 2 call + SMS, Day 5 email + call. Switch off once response is logged.

### Post-deposit cadence (visa/pre-arrival)
- Week 0: Deposit confirmation email + receipt instructions; SMS acknowledgement.
- Week 1: Visa pack + document checklist; invite to visa clinic/webinar.
- Week 2: Accommodation guidance + peer/ambassador connect.
- Week 3: Orientation registration + travel planning form.
- Week 4 (pre-arrival): Arrival day instructions, emergency contacts, academic onboarding links.

## Objection handling (global scripts to be localized)
- **Cost/affordability:** Offer payment schedule, scholarship terms, and ROI outcomes. Avoid promising approvals; cite published fees and scholarship rules with sources.
- **Visa risk:** Share historical approval guidance and required documents; never guarantee visas. Provide timelines and prep checklist; escalate complex cases to compliance.
- **Recognition/licensure:** Link to `/UNIC/recognition` assets or program-specific recognition notes; avoid localized promises.
- **Accommodation/safety:** Provide vetted housing options and safety resources; defer city-specific claims to country addenda.
- **Language/prep gaps:** Offer language support options, bridging courses, and conditional offer steps.
- **Start-date flexibility:** Offer deferral rules and fees; log if deferral is requested and trigger deferral workflow.

## Data capture and logging (minimum fields)
- `applicant_id`, `offer_id`, `program_cluster`, `intake_term`, `campus` (UNIC vs UNIC Athens).
- `offer_type` (conditional/unconditional), `offer_deadline`, `deposit_amount`, `deposit_deadline`.
- `scholarship_status` (awarded/pending/none) and conditions.
- `consent` records per channel (status, timestamp, source, proof).
- `current_stage` (`Offered`, `Engaged`, `Committed`, `Deposited`, `Visa_In_Process`, `Cleared`, `Enrolled`).
- `last_contact` (datetime + channel), `next_action` (owner + due date), `objection_flag` (type), `escalation_owner`.
- `documents_required` vs `documents_received` with dates and verifier.
- `agent_or_school_partner` (if applicable) and their SLA.
- Outcome fields: `deposit_received_date`, `visa_status`, `arrival_confirmed`, `enrolled_date`.

## SLAs and ownership
- **Speed to first response:** <24h after offer; <4h during business hours where staffing allows.
- **Unanswered inquiries:** Response within 1 business day; escalate after 2 attempts.
- **Deposit chase:** Escalate to counselor/agent after 2 missed touches; manager review if >7 days past deadline.
- **Document verification:** Within 3 business days of receipt.
- **Visa packet dispatch:** Within 48h of deposit confirmation.
Assign explicit owners (Admissions ops, Counselor, Agent partner) and log ownership per contact.

## Consent, privacy, and channel rules
- Use only channels with recorded opt-in; SMS/WhatsApp require explicit consent and local compliance (consult country addendum).
- Store consent proof (timestamp, source form, IP where available) in CRM; do not store PII in-repo.
- Include unsubscribe/opt-out in email and messaging; honor within 24h.
- Avoid sensitive data in SMS/WhatsApp (no passport or financial details); direct to secure portal uploads.
- Track guardian/parent permissions for minors per country rules.

## Required artifacts (per ticket deliverable)
- **Cadence pack:** Markdown section or appendix with day-by-day touches, owners, scripts.
- **Script library:** Email + SMS/WhatsApp + call openers for common scenarios (offer sent, reminder, deposit chase, visa pack, welcome). Localize in country addenda only.
- **Objection bank:** Standard questions with approved responses and escalation paths.
- **Checklist assets:** Offer-to-enrolment checklist, deposit instructions, visa document list, arrival checklist.
- **Measurement spec:** Offer-to-deposit and deposit-to-enrolment funnel with target conversion rates and dashboard fields (`offers`, `engaged`, `calls_done`, `deposits`, `visa_submitted`, `enrolled`); define update frequency (weekly) and owner.

## How to use with countries
- Global baseline lives here; each market adds a lightweight addendum under its country directory (e.g., `/countries/<country>/skills/offerholder-and-yield-playbooks/ADDENDUM.md`) covering local consent, channel availability, working hours, and visa nuances.
- Do not duplicate global content in country files; cross-link instead.
- When country paths change, ensure addenda mirror the current `/countries/<country>/...` layout and update links in tickets accordingly.
