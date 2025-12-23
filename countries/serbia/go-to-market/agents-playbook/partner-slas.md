# Serbia agent partner SLAs (UNIC Nicosia + UNIC Athens)

Last updated: **2025-12-22**  
Owner: **Serbia Agent Channel Lead** (accountable) + **UNIC Admissions Ops (Nicosia/Athens)** (consulted)

## Purpose

Codify measurable service levels for Serbia-based agent partners so UNIC can:
- react to every prospect within hours, not days
- submit decision-ready applications that respect UNIC Nicosia seat caps (Medicine/MD, Architecture) and UNIC Athens portfolio nuances
- forecast deposits with confidence and intervene whenever quality or speed drifts

These SLAs pull timestamps from HubSpot/Slate (or the approved CRM) and must be reviewed weekly.

## Scope

Applies to all contracted Serbian education agents and pre-approved sub-agents sourcing for **both campuses**.  
Does **not** replace commercial contract terms or UNIC’s final admissions decisions.

## Lead ownership & routing rules (prevent disputes)

1. **UNIC-owned digital forms** (website, paid media, landing pages) → default to UNIC-owned. Leads may be reassigned to a partner **only** if:
   - the prospect explicitly names that partner **in writing**, or
   - UNIC Agent Lead assigns the record in CRM and logs the date.
2. **Agent-owned leads** (school visits, fairs where the partner staffed the booth, partner CRM imports) → partner-owned. UNIC will not reassign unless the partner misses the first-contact SLA twice in a row.
3. **UNIC fairs/roadshows** (UNIC-branded booths) → UNIC-owned, but partners present at the booth receive first right of nurture. If multiple partners are present, leads split on a rotation agreed **before** the event.
4. **Walk-ins / WhatsApp / referrals** → whichever party captures the lead **first** owns it. Always log the capture timestamp to resolve conflicts.
5. **Escalation:** if ownership is disputed for >24h, the Agent Channel Lead decides; their ruling is final for that cycle.

## Operating definitions

### Business hours (Serbia)
- Monday–Friday, 09:00–18:00 CET/CEST (Belgrade time).  
- Leads captured outside business hours must be worked by **12:00 next business day**.

### Lead stages
- **New lead:** inbound record with name + at least one contact channel.
- **Qualified lead (QL):** meets *all* criteria:
  - verified identity + working email/phone/WhatsApp consent (per GDPR)
  - programme cluster interest (Medicine/MD, CS/Data, Business, Design, Health/Life Sciences, Law/Governance, Other)
  - campus preference captured (`nicosia`, `athens`, `dual`, `undecided`)
  - intended intake (`Sep`, `Jan`, other)
  - current school/university + expected graduation month/year
  - English readiness (score or booked test date)
  - affordability signal (family-funded, scholarship, employer, other)
- **Unqualified lead:** missing consent, unreachable after the outreach cadence below, or clearly out of scope (e.g., requires Serbian-language delivery only).

### Application statuses
- **Application started:** applicant profile created in UNIC systems or the partner submitted the pre-check packet.
- **Complete application (decision-ready):** mandatory documents uploaded, legible, and aligned with programme checklist.
- **Offerholder:** conditional or unconditional offer issued.
- **Deposit confirmed:** proof received and reconciled by UNIC Finance.

### Programme baskets
- **Seat-limited:** UNIC Nicosia Medicine/MD, Architecture, select Health Sciences cohorts, any Athens programmes with capped labs. Apply the “urgent” SLA rows.
- **Open-capacity:** remaining programmes (Business, CS/Data, Design, etc.).

## SLA dashboard (review weekly)

### 1) Lead capture, response, and qualification

| Metric | SLA | Measurement notes |
| --- | --- | --- |
| CRM logging / lead file delivery | **≤24h** from capture | Timestamp when lead enters UNIC CRM vs capture time; mandatory fields completed. |
| First human contact | **≤4 business hours** (or by 12:00 next business day) | Automated emails do not count; track first call/SMS/email. |
| Outreach persistence | **≥3 attempts over 5 days** using ≥2 channels | Stop on opt-out; log each attempt. |
| Qualification decision | **≤2 business days** after first contact | Mark `qualified_at` or `disqualified_at` with reason. |
| Lead hand-off to UNIC (if needed) | **≤12h** once the partner cannot reach the lead | Tag `handoff_reason` to keep audit trail. |

### 2) Application build & readiness

| Metric | Standard (open-capacity) | Standard (seat-limited) | Measurement |
| --- | --- | --- | --- |
| Application started after QL | **≤3 business days** | **≤2 business days** | `application_started_at – qualified_at` |
| Document pre-check completed | **≤5 business days** | **≤3 business days** | Internal checklist signed + summary uploaded. |
| Complete application submitted | **≤7 business days** | **≤5 business days** | All mandatory docs + translation (if needed). |
| Admissions clarification response | **≤1 business day** | **≤12 hours** | SLA resets per inquiry from UNIC. |

**Exam-season adjustment:** For leads qualified between **15 May and 30 June** (Serbian graduation exams + university entrance prep; see `../../market/exams-and-calendar.md`), the “complete application” SLA extends to **≤10 business days** provided the partner uploads all available docs and tags the record `awaiting_matura_certificate`. No extension for seat-limited Medicine files—partners must provide interim proofs (predicted grades, confirmation letters).

### 3) Quality gates (zero tolerance)

| Quality gate | Threshold | Monitoring method |
| --- | --- | --- |
| Document legibility/completeness | **≥95%** of submissions free of `illegible` or `missing_doc` flags | Weekly QA sample of all new files. |
| Data consistency | **≤5%** of files needing corrections for name/DOB mismatches | Compare passport vs application fields. |
| English evidence plan | **100%** of files without scores include a booked test date or UNIC English placement plan | Field `english_plan_date` mandatory. |
| Programme fit checklist | **100%** seat-limited files and **≥90%** all other files have checklist uploaded | Use `fit_check_completed` flag; include science subject history for Medicine/Health. |
| Compliance | **0** GDPR/privacy breaches, **0** unapproved sub-agents | Any breach triggers immediate review. |

Partners falling below thresholds for two consecutive weeks enter corrective coaching; three weeks triggers probation.

### 4) Offerholder management & deposits

| Metric | SLA | Notes |
| --- | --- | --- |
| Offer explained to student/family | **≤2 business days** from offer issue | Document via call note or signed checklist. |
| Deposit plan captured | **≤3 business days** (open) / **≤48h** (seat-limited) | Record planned payment date + blockers. |
| Deposit proof submitted to UNIC | **≤24h** after receipt | Upload receipt + bank confirmation. |
| Visa/arrival briefing scheduled | **≤5 business days** post deposit | Attach summary + attendee list. |

## Reporting & forecasting rhythm

### Weekly operational report (due Mondays, 12:00 Belgrade time)
Email or upload the template below (CSV/Sheet is fine). Combine campus data but keep separate columns to surface seat pressure.

#### 1. Pipeline snapshot
| Stage | Leads (Nicosia) | Leads (Athens) | Leads (Undecided) | QoQ change | Comments (blockers) |
| --- | --- | --- | --- | --- | --- |
| New (logged but not contacted) |  |  |  |  |  |
| In outreach (1st–3rd attempt) |  |  |  |  |  |
| Qualified leads |  |  |  |  |  |
| Applications started |  |  |  |  |  |
| Complete applications |  |  |  |  |  |
| Offers outstanding |  |  |  |  |  |
| Offerholders awaiting deposit |  |  |  |  |  |
| Deposits paid (current month) |  |  |  |  |  |

#### 2. SLA compliance snapshot
| SLA | Target | This week | Notes / corrective action |
| --- | --- | --- | --- |
| First contact ≤4h | 90%+ |  |  |
| Qualification ≤2 days | 85%+ |  |  |
| Application complete ≤7/5 days | 80%+ |  |  |
| Quality flags per file | ≤10% |  |  |
| Weekly report on time | 100% |  |  |

#### 3. Forecast + risk narrative
- **Deposits forecast (next 30 days):** `#` expected for Nicosia / `#` for Athens; note seat-limited priority files.
- **At-risk list:** any offerholder with deposit due in ≤7 days, missing docs, or visa timing risk.
- **Support needs:** training, marketing assets, scholarship clarifications.

Use the table to document at-risk cases:

| Student initials / UNIC ID | Campus & programme | Stage | Risk description | Partner owner | Help needed from UNIC | ETA/resolution |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

### Monthly performance review (5th business day)
- Submit rolling-quarter metrics (conversion, cost-per-enrolment if tracked, compliance incidents).
- Present corrective plans for any SLA miss trends.

## Enforcement ladder

1. **Coaching notice** — auto-triggered when any SLA falls below target for 2 consecutive weeks. Requires written remediation plan and 100% file pre-check for the next 10 applications.
2. **Probation (30 days)** — triggered when the same SLA fails 3 of 4 weeks, or any privacy/compliance breach occurs. Actions: reduced lead allocation, weekly pipeline call with Agent Lead, and UNIC approval before new campaign launches.
3. **Suspension/termination** — if probation fails, gross misrepresentation happens, fraudulent documents are submitted, or GDPR violations repeat. Partner loses marketing support and commission accrual pauses until disputes resolved.

## How to operationalize

- **Dashboards:** HubSpot/Slate views filtered by `country=Serbia` + `partner_name`, grouping by stage and campus to mirror the weekly template.
- **Checklists:** Attach the programme fit checklist and compliance attestation to every application package so admissions can audit quickly.
- **Playbook linkage:** Align with `onboarding.md` for initial training, `compliance.md` for GDPR/sub-agent requirements, and `../../market/exams-and-calendar.md` for seasonal context.
- **Continuous improvement:** Agent Lead reviews SLA trendlines every Friday; improvements or escalations logged in `executions/`.
