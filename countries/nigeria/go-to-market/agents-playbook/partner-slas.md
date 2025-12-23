# Nigeria agent partner SLAs (UNIC Nicosia + UNIC Athens)

Last updated: **2025-12-22**  
Owner: **Agent Channel Lead (Nigeria)** (accountable) + **Admissions Ops (Nicosia/Athens)** (consulted)

## Purpose

Set measurable service levels for Nigeria-based education agent partners so UNIC can:
- protect applicant experience and brand trust
- convert faster without sacrificing quality or compliance
- reduce avoidable rework and downstream visa risk through higher-quality applicant files
- compare partners fairly using the same KPIs and review cadence

This document is an **operational SLA template** intended to be attached to (or referenced by) the commercial contract. If there is a conflict, the signed contract prevails.

## Scope (who this applies to)

Applies to:
- contracted education agent partners recruiting from Nigeria for **both campuses** (Nicosia and Athens)
- sub-agents only if pre-approved in writing and held to the same standards

Does not replace:
- commercial terms (commissions, payment terms, territory clauses)
- UNIC admissions decisions (academic assessment remains with UNIC)

## Operating principles (what “good” looks like)

- **Speed with quality:** fast responses, but never at the expense of accuracy, consent, or document integrity.
- **One source of truth:** all lead/applicant updates are logged in the agreed system (UNIC CRM/portal) with timestamps.
- **No surprises:** risks are flagged early (academic fit, English readiness, affordability, visa-readiness signals).
- **Compliance first:** no misrepresentation of fees, scholarships, rankings, recognition/licensure, or visa outcomes.

## Definitions (use these consistently)

### Business days & hours (Nigeria time)
- **Business hours:** Mon–Fri, 09:00–18:00 (**WAT**)
- **Business day:** Mon–Fri excluding public holidays
- SLA clocks for partner responsibilities use **WAT** unless otherwise stated.

### Lead stages
- **New lead:** prospective student inquiry received by the partner (digital/event/referral/school) with contact details.
- **Qualified lead (QL):** a lead that meets *all* criteria below and has explicit contact consent (see Consent).
  - **Identity + contactability:** full name + at least one reliable channel (email or phone).
  - **Consent:** explicit opt-in for contact; if WhatsApp will be used, explicit opt-in for WhatsApp.
  - **Intent:** clear programme cluster interest *or* a booked consultation date/time.
  - **Campus + intake:** campus preference recorded (**Nicosia / Athens / Undecided**) and intended intake (**Sep / Jan / Other**).
  - **Academic status:** current school/university, expected graduation month/year, and highest completed credential.
  - **English readiness:** existing English proof (if any) or a dated plan to test.
- **Unqualified lead:** missing consent, unreachable after the contact attempts standard, or clearly not eligible for an English-taught programme (e.g., refuses English testing and requires local-language delivery).

### Application stages
- **Application started:** applicant account created / application initiated in UNIC’s system (or formally handed off to UNIC with required fields if the partner cannot access the system).
- **Complete application (ready for decision):** mandatory document set uploaded, legible, and consistent (see Quality gates).
- **Offerholder:** applicant has received an offer (conditional or unconditional).
- **Deposit paid:** proof of deposit payment received and logged by UNIC.

### Consent (hard rule)
Partners must capture and log:
- **source of consent** (e.g., web form, fair scan + opt-in tick, email reply “yes”, signed consent form)
- **timestamp** (date/time)
- **channel(s) consented** (email/phone/SMS/WhatsApp)

No consent → no outbound messaging.

## Responsibilities (who does what)

### Partner responsibilities
- Counsel students/families accurately on UNIC programmes (Nicosia/Athens), requirements, fees, scholarships (only if confirmed), and timelines.
- Capture consent, log the full lead record, and maintain accurate pipeline stages.
- Pre-screen eligibility (academic/English/readiness) and flag risks early.
- Submit **complete, high-quality** applications with correct data and required documents.
- Respond to UNIC casework requests (missing info/doc clarification) within agreed response times.
- Follow brand and compliance rules (no false claims; no guaranteed visas).

### UNIC responsibilities
- Provide the partner with current programme portfolio, entry requirements, fees, scholarship rules, and official marketing assets.
- Provide training and updates (at minimum quarterly) on “what changed” and common application errors.
- Process complete applications within published internal targets; return incomplete files with clear missing-item requests.
- Provide a named escalation contact for partner operations and admissions queries.

## SLAs (measured weekly)

### 1) Lead capture, minimum information, and first response

#### Minimum information required per lead (before routing to UNIC)

**Mandatory fields**
- student_full_name
- email OR phone
- city + state
- nationality (and residence country if different)
- campus_preference: `nicosia` / `athens` / `undecided`
- programme_cluster interest (or “undecided”)
- intended_intake: `sep` / `jan` / `other`
- current_education_level + expected_graduation_month_year
- english_status: `has_score` / `test_planned` / `unknown` (if planned: include date)
- consent_captured: `Y/N` (plus timestamp + channels)

**Recommended fields (increase conversion and reduce rework)**
- date_of_birth (store only in UNIC system where applicable)
- funding_source + affordability_risk_flag (`Y/N`)
- passport_status (`has_passport` / `in_process` / `no_passport`)
- parent/guardian contact (for minors)

#### Response-time targets

| Metric | SLA | How we measure | Notes |
| --- | --- | --- | --- |
| Lead logged to CRM/portal (or lead file delivered to UNIC) | **≤24h** from capture | lead_created_at – lead_captured_at | Mandatory fields populated. |
| First human contact attempt | **≤4 business hours** from lead receipt | first_contact_at – lead_received_at | If received outside business hours: by **12:00 next business day**. |
| Contact attempts standard (when no response) | **3 attempts / 5 days** | contact_attempt_count | Mix channels (email + phone). Stop on opt-out. |
| Qualification completed (QL or disqualified) | **≤2 business days** from first contact | qualified_at – first_contact_at | “Qualified” uses definitions above. |

### 2) Application build speed (from QL → submission)

| Metric | SLA | How we measure | Notes |
| --- | --- | --- | --- |
| Application started (after qualification) | **≤3 business days** | application_started_at – qualified_at | Partner books a doc-collection plan with dates. |
| Complete application submitted (ready for decision) | **≤7 business days** from application start | complete_application_at – application_started_at | If awaiting final exam results (e.g., WAEC/NECO; see `../../market/exams-and-calendar.md`), SLA extends to **≤10 business days** *only* if everything else is uploaded and tagged “awaiting_final_results”. |
| Response to UNIC missing-item request | **≤24h** | partner_reply_at – unic_request_at | If it requires a student document: respond within 24h with an ETA + plan. |

### 3) Quality gates (non-negotiable)

Quality is measured as **rejectable errors per submitted application**. The partner is accountable for preventing avoidable back-and-forth.

| Quality gate | Standard | Weekly measure |
| --- | --- | --- |
| Document legibility | All pages present, readable scans, no cropping; stamps/signatures visible | % applications flagged “illegible/partial docs” |
| Data consistency | Names/DOB/passport fields consistent; dates align across documents | % applications flagged “data mismatch” |
| Mandatory docs present at submission | 0 missing mandatory docs unless explicitly tagged “awaiting_final_results” | % complete-at-submission |
| English proof routing | If no English proof, a **test date** (or approved alternative plan) is recorded | % with english_plan_date when no score |
| Fit check completed | Partner records a basic fit check before submission | % submissions with fit_check_completed |

#### Document checklist expectations (what “complete” includes)

Use UNIC’s **programme-specific document checklist** as the source of truth. At minimum, partners must collect and submit the relevant items below (as applicable).

**Application documents (typical minimum)**
- Identity: passport bio page (and any prior passports if requested), clear passport validity
- Academics: transcripts + certificates (secondary and/or tertiary as applicable), grading scale where available
- English: IELTS/TOEFL (or approved equivalent) **or** a dated test plan
- Programme supporting docs (as required): CV, personal statement/motivation letter, references, portfolio, research proposal
- Supporting explanations (when relevant): name-change documents/affidavits, gap-year explanations

**Visa-readiness documents (campus-specific; use the official checklist)**
- Financial evidence and sponsor documentation (as required)
- Accommodation plan (if required)
- Medical / police / other declarations (as required)

**Document standards (required)**
- Do not alter documents. If fraud is suspected, escalate immediately.
- Scans must be complete, readable, and consistent; no cut-off stamps/signatures.
- Use secure upload methods for passports and sensitive documents (avoid consumer chat apps for document transfer).

**Fit check (minimum fields to record):**
- intended programme + campus (Nicosia/Athens)
- highest credential + expected graduation date
- English readiness (score or test date)
- affordability risk flag + funding source
- any “non-standard” factors (gaps, prior refusals, name changes) flagged early

### 4) Offerholder support (yield) + visa-readiness support

Partners are expected to drive conversion while staying truthful and compliant.

| Metric | SLA | How we measure | Notes |
| --- | --- | --- | --- |
| Offer explained to student/family | **≤2 business days** from offer issued | offer_explained_at – offer_issued_at | Must include next steps, realistic timelines, and campus-specific positioning. |
| Deposit plan captured | **≤3 business days** from offer issued | deposit_plan_at – offer_issued_at | Record “will pay by ___” or “needs extension”; log reason. |
| Proof of payment delivered to UNIC | **≤24h** from receipt | deposit_proof_sent_at – deposit_paid_at | Use secure channels; attach transaction proof where available. |
| Visa readiness checklist completed (post-deposit) | **≤5 business days** from deposit | visa_check_completed_at – deposit_paid_at | Not a visa guarantee; flags missing items early to reduce refusal risk. |

Deposit deadlines vary by intake and programme; align counseling to `../offerholder-and-yield/deposit-deadlines.md`.

## Communication norms (how we work together)

- **Primary channels:** email + official CRM/portal notes; WhatsApp may be used for coordination **only when opted-in** and never as the only record.
- **Casework response time:** respond to admissions/casework queries within **24h** (business days).
- **Meeting cadence:** 15-minute weekly pipeline touchpoint (optional for low-volume partners), monthly performance review, quarterly business review (QBR).
- **Escalations:** raise urgent cases early (deadline risk, compliance issues, suspected fraudulent documents) using the escalation path below.

## Marketing, pricing, and scholarship claims (brand protection)

- Use only **current, UNIC-approved** programme descriptions, fee sheets, and scholarship information.
- Do not advertise “guaranteed scholarships”, “guaranteed admissions”, or “guaranteed visas”.
- Do not run paid ads using UNIC brand assets without written approval from UNIC (including keywords and landing pages).
- Any scholarship/discount messaging must match the official written policy for the specific intake and campus.

## Escalation path (who to contact)

1. **Partner Manager (UNIC)** — operational issues, lead routing, reporting, training
2. **Admissions Ops Lead (UNIC)** — application casework, missing docs, timelines, exceptions
3. **Head of Enrollment / Country Lead** — repeated SLA breaches, commercial disputes, termination decisions

Partners must maintain an internal escalation contact (name, title, phone, email) available during business hours.

## Performance scorecard (KPIs)

All KPIs are measured monthly and reviewed quarterly. UNIC shares a partner scorecard; partners validate data and propose improvements.

| KPI | Definition (measurable) | Formula | Target (baseline) |
| --- | --- | --- | --- |
| 1) Lead first-contact compliance | % of new leads contacted within SLA | leads_contacted_within_sla / total_new_leads | **≥85%** |
| 2) Lead qualification speed | % of leads qualified/disqualified within SLA | leads_qualified_within_sla / total_contacted_leads | **≥80%** |
| 3) Lead-to-application conversion | % of QLs that start an application | applications_started / qualified_leads | Benchmark; improve QoQ |
| 4) Complete-at-submission rate | % applications submitted complete on first pass | complete_at_submission / submitted_applications | **≥90%** |
| 5) Rework rate | % applications returned for avoidable issues | returned_for_rework / submitted_applications | **≤10%** |
| 6) Offer rate | % submitted applications that receive an offer | offers_issued / submitted_applications | Track by programme cluster |
| 7) Deposit rate (yield proxy) | % offerholders who pay deposit | deposits_paid / offers_issued | Track by intake |
| 8) Visa outcome proxy | % of visa decisions that are approvals (where tracked) | visa_approvals / visa_decisions | **≥80%** (or improving trend) |
| 9) Reporting compliance | On-time submission of weekly + monthly reports | on_time_reports / total_reports_due | **100%** |

Notes:
- KPIs 3/6/7 are influenced by student quality and market conditions; they are used to **coach and forecast**, not to punish in isolation.
- “Visa outcome proxy” is monitored to catch preventable patterns (documentation gaps, unrealistic affordability, poor counseling). No partner may promise visa success.

## Partner tiering model (A/B/C)

Tiers are reviewed quarterly and updated with written notice. New partners start as **Tier C (Developing)** for the first full quarter.

| Tier | Typical profile | Minimum standards | Benefits | Consequences if standards missed |
| --- | --- | --- | --- | --- |
| **Tier A (Strategic)** | High-quality, reliable pipeline; proactive compliance | Meets all baseline KPI targets **and** 0 major compliance incidents | Priority training + early updates; eligible for co-marketing; named fast-path contact; invited to joint webinars/events | If missed for 1 quarter: downgraded to Tier B or placed on improvement plan |
| **Tier B (Core)** | Consistent partner; steady volume | Meets baseline speed/quality/reporting targets | Standard support; eligible for quarterly training; co-marketing by request | If missed for 1 quarter: written improvement plan; lead allocation may be reduced |
| **Tier C (Developing / Probation)** | New or underperforming partner | Must complete onboarding; must meet minimum compliance standards (consent, brand, data handling) | Access to core materials; additional coaching | Limited lead allocation; no co-marketing; monthly reviews; repeated misses trigger suspension/termination |

## Enforcement ladder (how we handle misses)

### Minimum thresholds (reviewed monthly)
Unless otherwise agreed in writing:
- **Speed compliance:** ≥**85%** first-contact SLA; ≥**80%** qualification SLA.
- **Quality compliance:** ≥**90%** complete-at-submission; ≤**10%** avoidable rework rate.
- **Reporting compliance:** 100% on-time weekly + monthly reports.

### Actions
1) **Coaching notice (Week 1)** — documented feedback + training refresh; UNIC may require 100% file pre-check for 2 weeks.
2) **Written warning (Month 1)** — if thresholds missed or reporting late twice in a month; partner submits a 30-day improvement plan with owners and dates.
3) **Probation (Month 2)** — if thresholds missed for 2 consecutive months or severe but remediable issues:
   - reduced lead allocation until recovery
   - mandatory weekly pipeline call
   - audit of the next 20 files (or 100% of files for 2 weeks, whichever is higher)
4) **Suspension / termination (immediate or Month 3)** — if any of the following occur:
   - data/privacy breach (contacting without consent; sharing sensitive docs insecurely; repeated policy violations)
   - misrepresentation of UNIC programmes/recognition/fees/scholarships/visa outcomes
   - suspected fraudulent documents or unethical behavior
   - probation targets missed for a third consecutive month

## Quarterly Business Review (QBR) process (required)

QBRs are how we scale performance without creating “heroics”.

**Cadence:** once per quarter (45–60 minutes)  
**Inputs (shared 48h before):**
- KPI scorecard (last 3 months) + trend notes
- funnel volumes (leads → applications → offers → deposits → arrivals)
- top 5 loss reasons + 3 actions to reduce them
- quality error themes (top 3) + prevention plan
- compliance incidents (if any) + corrective actions

**Outputs (documented within 5 business days):**
- next-quarter targets (volume + quality + speed)
- training plan (what topics, who attends, dates)
- marketing plan (events/webinars/digital) with owners
- tier decision (A/B/C) and any changes to lead allocation

## Reporting cadence (templates)

### Weekly (operational) — every Monday by 12:00 WAT
Submit (CRM export acceptable):
- new leads received, QLs, applications started, complete applications submitted
- SLA compliance (% for first contact, qualification, application start)
- top blockers (awaiting results, English testing backlog, affordability constraints)
- at-risk offerholders (deposit due in ≤7 days)

### Monthly (performance) — 5th business day of the month
Submit the template below and join a 45-minute performance review call.

### Monthly reporting template (fields required)

Use **UNIC CRM Lead/Application IDs**. Do not send passports, national IDs, or scanned sensitive documents in reports.

| Field | Required | Format/example | Notes |
| --- | --- | --- | --- |
| reporting_month | Yes | `2025-12` |  |
| partner_name | Yes | Text |  |
| record_type | Yes | `lead` / `application` / `offerholder` |  |
| unic_lead_id | Yes (lead) | Text/ID | Use UNIC ID; if unavailable, provide partner_internal_id and student_initials. |
| unic_application_id | Yes (application/offerholder) | Text/ID |  |
| lead_captured_at | Yes | ISO datetime |  |
| lead_source | Yes | `school`/`fair`/`digital`/`referral`/`other` |  |
| city | Recommended | Text |  |
| state | Recommended | Text |  |
| consent_captured | Yes | `Y/N` | Must be `Y` for outreach. |
| consent_timestamp | Yes if consent_captured=Y | ISO datetime |  |
| consent_channels | Yes if consent_captured=Y | `email,phone,whatsapp` | WhatsApp only if opted-in. |
| campus_preference | Yes | `nicosia`/`athens`/`undecided` |  |
| programme_cluster | Yes | Text |  |
| intake | Yes | `sep`/`jan`/`other` |  |
| first_contact_at | Yes | ISO datetime |  |
| qualified_lead | Yes | `Y/N` | Uses QL definition in this doc. |
| qualified_at | Yes if qualified_lead=Y | ISO datetime |  |
| application_started_at | If applicable | ISO datetime |  |
| complete_application_at | If applicable | ISO datetime |  |
| awaiting_final_results | If applicable | `Y/N` | Use only when relevant. |
| quality_flags | If applicable | `illegible_docs;data_mismatch;missing_docs` | Semi-colon list; empty if none. |
| offer_issued_at | If applicable | ISO datetime |  |
| offer_explained_at | If applicable | ISO datetime |  |
| deposit_due_date | If applicable | ISO date | Align to `deposit-deadlines.md` rules. |
| deposit_plan_at | If applicable | ISO datetime |  |
| deposit_paid_at | If applicable | ISO datetime/date |  |
| visa_decision | If applicable | `approved`/`refused`/`pending` | If tracked. |
| outcome | Yes | `active`/`won`/`lost` |  |
| loss_reason | If outcome=lost | Text (controlled list preferred) | e.g., price, destination, failed English, timeline. |
