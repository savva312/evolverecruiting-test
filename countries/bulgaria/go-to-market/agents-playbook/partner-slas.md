# Bulgaria agent partner SLAs (UNIC Nicosia + UNIC Athens)

Last updated: **2025-12-22**  
Owner: **Agent Channel Lead (Bulgaria)** (accountable) + **Admissions Ops (Nicosia/Athens)** (consulted)

## Purpose

Set measurable service levels for Bulgaria-based education agent partners so UNIC can:
- protect applicant experience and brand trust
- convert faster without sacrificing quality or compliance
- compare partners fairly using the same metrics
- enforce outcomes through an escalation ladder

These SLAs are designed to be measured weekly from CRM timestamps and partner reports.

## Scope (who this applies to)

Applies to:
- contracted education agent partners recruiting from Bulgaria for **both campuses** (Nicosia and Athens)
- sub-agents are allowed only if pre-approved in writing and held to the same SLAs

Does not replace:
- contractual commercial terms (commissions, payment terms, territory clauses)
- UNIC admissions decisions (academic assessment remains with UNIC)

## Definitions (use these consistently)

### Business days & hours (Bulgaria time)
- **Business hours:** Mon–Fri, 09:00–18:00 (BG local time)
- **Business day:** Mon–Fri excluding public holidays
- SLA clocks use **Bulgaria local time** unless otherwise stated.

### Lead stages
- **New lead:** a prospective student inquiry received by the partner (event/digital/referral/school) with contact details.
- **Qualified lead (QL):** a lead that meets *all* criteria below and has explicit contact consent (see Consent).
  - **Identity + contactability:** name + at least one reliable channel (email or phone).
  - **Consent:** explicit opt-in for contact; if WhatsApp/Viber will be used, explicit opt-in for that channel.
  - **Intent:** clear programme cluster interest *or* a booked consultation date/time.
  - **Campus + intake:** campus preference recorded (**Nicosia / Athens / Undecided**) and intended intake (**Sep / Jan / Other**).
  - **Academic status:** current school/university, expected graduation month/year, and highest completed credential.
  - **English readiness:** existing English proof (if any) or plan/date to test.
- **Unqualified lead:** missing consent, unreachable after the contact attempts standard, or clearly not eligible for an English-taught programme (e.g., refuses English testing and requires a local-language delivery).

### Application stages
- **Application started:** applicant account created / application initiated in UNIC’s system (or formally handed off to UNIC with required fields if the partner cannot access the system).
- **Complete application (ready for decision):** the mandatory document set for the programme cluster is uploaded, legible, and consistent (see Quality Gates).
- **Offerholder:** applicant has received an offer (conditional or unconditional).
- **Deposit paid:** proof of deposit payment received and logged by UNIC.

### Consent (hard rule)
Partners must capture and log:
- **source of consent** (e.g., web form, fair scan + opt-in tick, email reply “yes”, signed consent form)
- **timestamp** (date/time)
- **channel(s) consented** (email/phone/SMS/Viber/WhatsApp)

No consent → no outbound messaging.

## Channel rules (Bulgaria-appropriate + GDPR-aligned)

- **Default channels:** email + phone; **Viber** is acceptable where consent exists.
- **WhatsApp/Viber:** use **only with explicit opt-in** for that channel; record it in CRM. If not sure, do not use it.
- **No group chats** that include multiple prospects/families.
- **Minors:** if the prospect is under 18, route substantive admissions conversations through a parent/guardian or school counselor whenever possible; capture parent/guardian consent for direct messaging.
- **Sensitive documents:** do not send passports/IDs/transcripts over consumer chat apps. Use UNIC’s secure upload flow or agreed secure transfer method.
- **No national ID numbers:** do not request or store national ID numbers; use CRM Lead/Application IDs.

## SLAs (measured weekly)

### 1) Lead capture & first response

| Metric | SLA | How we measure | Notes |
| --- | --- | --- | --- |
| Lead logged to CRM (or lead file delivered to UNIC) | **≤24h** from capture | lead_created_at – lead_captured_at | Required fields must be populated (see Reporting). |
| First human contact attempt | **≤4 business hours** from lead receipt | first_contact_at – lead_received_at | If received outside business hours: by **12:00 next business day**. |
| Contact attempts standard (when no response) | **3 attempts / 5 days** | contact_attempt_count | Mix channels (email + phone/SMS). Stop on opt-out. |
| Qualification completed (QL or disqualified) | **≤2 business days** from first contact | qualified_at – first_contact_at | “Qualified” uses the definition above. |

### 2) Application build speed

| Metric | SLA | How we measure | Notes |
| --- | --- | --- | --- |
| Application started (after qualification) | **≤3 business days** | application_started_at – qualified_at | If student requests delay, log “student_requested_delay” with date. |
| Complete application (ready for decision) | **≤7 business days** from application started | complete_at – application_started_at | Separate targets for exam season below. |
| Admissions clarification response | **≤1 business day** | partner_reply_at – admissions_request_at | Applies to missing docs, clarifications, corrections. |

**Exam-season adjustment (Bulgaria):** for leads qualified during the Matura window (see `../../market/exams-and-calendar.md`), the “Complete application” SLA extends to **≤10 business days** if the student is awaiting final school documents. Partner must still upload everything else and tag “awaiting_matura_docs”.

### 3) Quality gates (non-negotiable)

Quality is measured as **rejectable errors per submitted application**. A partner is accountable for preventing avoidable back-and-forth.

| Quality gate | Standard | Weekly measure |
| --- | --- | --- |
| Document legibility | All pages present, color scans where possible, no cropping, readable stamps/signatures | % applications flagged “illegible/partial docs” |
| Consistency | Names match across documents; DOB/passport fields consistent; no conflicting graduation dates | % applications flagged “data mismatch” |
| Mandatory docs present | 0 missing mandatory docs at submission (unless tagged “awaiting_matura_docs”) | % complete-at-submission |
| English proof routing | If English proof not available, a **test plan date** is recorded; no “we will send later” without a date | % with english_plan_date when no score |
| Programme fit screen (Medicine/MD vs non-MD) | Partner completes the fit checklist before submission and flags risks early | % submissions with “fit_check_completed” |

**Fit checklist (minimum fields to record):**
- intended programme + campus (Nicosia/Athens)
- highest credential + expected graduation date
- science/math background where relevant (esp. Medicine/MD and STEM)
- English readiness (score or test date)
- budget/affordability risk flag (Y/N) and funding source (family/scholarship/other)

### 4) Offerholder support & deposit speed

Partners are expected to drive conversion while staying truthful and compliant.

| Metric | SLA | How we measure | Notes |
| --- | --- | --- | --- |
| Offer explained to student/family | **≤2 business days** from offer issued | offer_explained_at – offer_issued_at | Must include next steps, document needs, and realistic timelines. |
| Deposit plan captured | **≤3 business days** from offer issued | deposit_plan_at – offer_issued_at | Record “will pay by ___” or “needs extension”; log reason. |
| Proof of payment delivered to UNIC | **≤24h** from receipt | deposit_proof_sent_at – deposit_paid_at | Use secure channels; attach transaction proof where available. |

Deposit deadlines vary by intake and programme; align counseling to `../offerholder-and-yield/deposit-deadlines.md`. For limited-capacity programmes (e.g., Medicine/MD), partners should treat deposit counseling as urgent and prioritize Day 0–10 execution.

## Reporting cadence (required)

### Weekly (operational) — every Monday by 12:00 BG time
Submit a short operational report (can be exported from CRM) with:
- new leads received, QLs, applications started, complete applications submitted
- SLA compliance (% for first contact, qualification, application start)
- top blockers (e.g., awaiting Matura docs, English testing backlog)
- at-risk offerholders (deposit due in ≤7 days)

### Monthly (performance) — 5th business day of the month
Submit the full template below and join a 45-minute performance review call.

## Monthly reporting template (fields required)

Use **UNIC CRM Lead/Application IDs**. Do not send passports, national IDs, or birth dates in reports.

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
| consent_captured | Yes | `Y/N` | Must be `Y` for outreach. |
| consent_timestamp | Yes if consent_captured=Y | ISO datetime |  |
| consent_channels | Yes if consent_captured=Y | `email,phone,viber` | WhatsApp/Viber only if opted-in. |
| campus_preference | Yes | `nicosia`/`athens`/`undecided` |  |
| programme_cluster | Yes | Text | Medicine/MD, CS, Business, etc. |
| intake | Yes | `sep`/`jan`/`other` |  |
| first_contact_at | Yes | ISO datetime |  |
| qualified_lead | Yes | `Y/N` | Uses the QL definition in this doc. |
| qualified_at | Yes if qualified_lead=Y | ISO datetime |  |
| application_started_at | If applicable | ISO datetime |  |
| complete_application_at | If applicable | ISO datetime |  |
| awaiting_matura_docs | If applicable | `Y/N` | Use only when relevant. |
| quality_flags | If applicable | `illegible_docs;data_mismatch;missing_docs` | Semi-colon list; empty if none. |
| offer_issued_at | If applicable | ISO datetime |  |
| offer_explained_at | If applicable | ISO datetime |  |
| deposit_due_date | If applicable | ISO date | From `deposit-deadlines.md` rules. |
| deposit_plan_at | If applicable | ISO datetime |  |
| deposit_paid_at | If applicable | ISO datetime/date |  |
| outcome | Yes | `active`/`won`/`lost` |  |
| loss_reason | If outcome=lost | Text (controlled list preferred) | e.g., price, destination, failed English, timeline. |

## Enforcement ladder (how we handle misses)

### Performance thresholds (reviewed monthly)
Unless otherwise agreed in writing:
- **Speed compliance:** ≥**85%** of records meet first-contact SLA; ≥**80%** meet qualification SLA.
- **Quality compliance:** ≥**90%** applications are complete-at-submission (or correctly tagged awaiting Matura docs); ≤**10%** have avoidable quality flags.
- **Reporting compliance:** 100% on-time weekly operational report; monthly template submitted by deadline.

### Actions
1) **Coaching notice (Week 1)** — documented feedback + training refresh; UNIC may require 100% file pre-check for 2 weeks.
2) **Written warning (Month 1)** — if thresholds missed or reporting late twice in a month; partner submits a 30-day improvement plan with owners and dates.
3) **Probation (Month 2)** — if thresholds missed for 2 consecutive months or severe but remediable issues:
   - reduced lead allocation until recovery
   - mandatory weekly pipeline call
   - audit of the next 20 files (or 100% of files for 2 weeks, whichever is higher)
4) **Suspension / termination (immediate or Month 3)** — if any of the following occur:
   - data/privacy breach (contacting without consent; sharing sensitive docs over insecure channels; repeated policy violations)
   - misrepresentation of UNIC programmes/recognition/visa outcomes
   - suspected fraudulent documents or unethical behavior
   - probation targets missed for a third consecutive month

## Practical operating rhythm (recommended)

- **Weekly (15 min):** agent manager reviews SLA dashboard + at-risk offerholders.
- **Monthly (45 min):** partner performance review: conversion, blockers, training needs, next-month targets.
- **Quarterly:** compliance refresher + “what changed” on admissions requirements and campus positioning.
