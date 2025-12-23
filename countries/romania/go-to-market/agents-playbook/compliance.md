# Romania agent compliance playbook (UNIC Nicosia + UNIC Athens)

**Purpose:** keep every Romania-based agent (and their sub-agents) fully aligned with GDPR, ANSPDCP (Romania’s data protection authority) expectations, and UNIC brand guardrails.  
**Audience:** enrollment managers, partner success owners, and compliance leads who supervise Romania recruitment.  
**Non-legal note:** this is an operational SOP, not legal advice. Escalate edge cases to UNIC Legal/Compliance.

---

## 0) Non-negotiables (instant stop + escalation)

Trigger an immediate referral freeze, notify Enrollment + Legal, and open a compliance case if you see any of the following:

1. **Consent-less lead transfers** — no documented opt-in naming UNIC/UNIC Athens, missing timestamp, or unverifiable capture method.
2. **Over-collection or unsafe storage** — passport scans, DOB, or health data sent by WhatsApp/email prior to the official UNIC application flow.
3. **Unapproved marketing claims** — any “guaranteed visa/licensure/scholarship” wording or housing/employment promises not present in the official messaging pack.
4. **Undisclosed or uncontracted sub-agents** — especially when leads originate from other EU states or use lookalike social ads.
5. **Rebate/cashback schemes** — refunding deposits, promising commission sharing, or charging “priority processing” fees tied to admission outcomes.

---

## 1) Mandatory compliance gates before onboarding

| Gate | What must be collected/verified | Evidence owner |
| --- | --- | --- |
| **Entity + authority** | Trade register excerpt, fiscal/VAT number, beneficial owners, signatory ID (reference only, do **not** store copies in repo). | Partner success |
| **GDPR readiness** | Privacy notice in Romanian/English, consent wording, storage location, retention schedule, DPO/contact. | Compliance |
| **Lead capture proof** | Screenshots or export showing consent text, checkbox, timestamp, source URL/form ID. | Agent (review sample of 5) |
| **Sub-agent mapping** | Names, city/country, channel, % of volume, confirmation they sign UNIC flow-down clauses. | Partner success |
| **Marketing + claims inventory** | Landing pages, decks, ads. Must show UNIC-approved copy or highlight items requiring review. | Marketing enablement |
| **Commercial transparency** | Student-facing fee sheet, commission structure tied to official tuition list, confirmation no rebates. | Finance |

> **Onboarding gate:** all evidence logged in the agent’s CRM record + templates completed before sharing application links or CRM access.

---

## 2) GDPR + data handling rules (Romania/EU)

### 2.1 Data fields agents may collect/share at “lead” stage
- Full name
- Primary email + mobile/WhatsApp (with opt-in)
- City + country of residence
- Intended program/level/campus (Nicosia vs Athens) + preferred intake
- Current school/university + graduation year (optional but useful for targeting)
- Budget bandwidth (binned ranges) if volunteered

### 2.2 Fields **prohibited** until UNIC requests them through a secure workflow
- Passport or ID numbers/scans
- Date of birth, national identification numbers, social security-like identifiers
- Health/disability data, religious/ethnic background, political views
- Criminal history documents
- Payment card/bank data
- Parents’ financial statements unless explicitly asked by UNIC Financial Aid

### 2.3 Consent requirements
1. **Explicit + granular:** UNIC Nicosia and UNIC Athens must be named. If both campuses are covered, use a single checkbox referencing both.
2. **Informed:** consent text must state what data is collected, why it is shared, that withdrawals are honored, and provide contact/DPO email.
3. **Traceable:** store timestamp, IP/device or location, collection channel, agent staff member, and the exact snippet shown to the student.
4. **Retrievable:** agents must provide evidence within **5 business days**. Use the `agent-gdpr-consent-proof-checklist.md` template to audit quarterly.

### 2.4 Data transfer + security expectations
- Allowed channels: UNIC CRM portal, secure SFTP upload, or encrypted email (Office 365 message encryption).  
- Forbidden: public Google Sheets, open WhatsApp threads containing sensitive data, USB drives, or personal email accounts.
- Cross-border transfers (Romania → Cyprus/Greece) operate under GDPR Article 46 (contractual necessity). Agents must ensure hosting in EEA or in countries with adequacy decisions; otherwise add SCCs.

### 2.5 Retention + deletion
- **Marketing leads:** keep no longer than **12 months** without re-consent.  
- **Applicants:** once UNIC confirms receipt, delete redundant local copies within **30 days** unless the agent must retain for invoicing or regulator purposes.  
- Maintain a simple deletion log (date, record type, staff initials) to prove compliance.

### 2.6 Data subject rights + incident response
- **DSARs (access/correct/delete):** acknowledge within **2 business days**, fulfill within **30 days**, inform UNIC if UNIC also holds the data.
- **Incident workflow:** notify UNIC within **24 hours** of discovering loss/misuse, include what happened, data categories, record count, containment steps, and whether ANSPDCP notification may be required.

---

## 3) Marketing + messaging guardrails (what agents can/cannot say)

### 3.1 Approved materials only
- Use the shared UNIC fact sheets, tuition tables, scholarship briefs, and recognition guidance stored in `/UNIC/` and `countries/romania/market/**`.
- Any custom ad, landing page, webinar script, or press pitch requires Marketing approval with a ticket or email trail.

### 3.2 “What not to claim” cheat sheet
| Risk area | Forbidden wording examples | Acceptable alternative |
| --- | --- | --- |
| **Scholarships/discounts** | “Guaranteed scholarship for every Romanian student”, “We can top up UNIC’s award”, “Apply through us for an automatic 40% tuition cut.” | “UNIC offers merit-based scholarships; eligibility and award size are confirmed by UNIC after review.” |
| **Visa/residency** | “We guarantee your Cyprus visa in 3 weeks”, “UNIC has a fast lane at the Greek embassy”, “No interview needed if you apply with us.” | “UNIC guides you through the visa process; final decisions and timelines belong to government authorities.” |
| **Recognition/licensure** | “UNIC MD gives you automatic Romanian residency rights”, “UNIC Nursing license is instantly recognized by OAMGMAMR”, “Law graduates can practice in Romania without any exams.” | “Recognition/licensure depends on Romanian competent authorities (e.g., OAMGMAMR, Ministry of Education). UNIC provides documentation but outcomes vary.” |
| **Housing/employment** | “UNIC guarantees you a single room in Nicosia/Athens”, “We guarantee internships at top Greek banks.” | “UNIC shares housing support and career services; availability is limited and competitive.” |

> If an agent cannot cite the exact PDF/page supporting a claim, they **cannot** say it.

### 3.3 Digital conduct
- No standalone “unicromania.ro” or lookalike websites without UNIC’s DNS approval.  
- Paid ads must run from agent-owned accounts with UNIC access for auditing.  
- UTM parameters must follow the Romania digital spec (see digital playbook).

---

## 4) Compliance incident workflow + remediation

1. **Detect** — frontline teams log the issue in the compliance tracker (source, date, summary, evidence).  
2. **Contain** — pause new referrals for the agent/sub-agent involved; if data exposure occurred, secure/remove public links within 4 hours.  
3. **Notify** — within 24 hours inform Enrollment VP, Legal, Data Protection Officer, and any impacted campus leads.  
4. **Triage severity**  
   - *Low:* isolated copy error, no PII at risk.  
   - *Medium:* repeated copy error, missing consent proof.  
   - *High:* data breach, fraudulent claims, undisclosed sub-agent.
5. **Remediate** — co-create an action plan with deadlines (e.g., re-train staff, purge data, rewrite marketing assets, re-run consent audit). Document completion evidence in the execution log.  
6. **Decide** — after remediation, classify outcome: “Return to normal monitoring”, “Probation (extra audits for 2 quarters)”, or “Terminate contract”.  
7. **Report** — summarize incident + fix in the quarterly compliance pack and store supporting files in `/executions/<incident-id>/`.

---

## 5) Sub-agent controls

1. **Pre-approval only:** no sub-agent can represent UNIC until the `agent-sub-agent-disclosure-form.md` is approved and appended to the main contract.  
2. **Flow-down obligations:** primary agent must prove each sub-agent received the compliance playbook, GDPR rules, and marketing kit (acknowledgment email or e-sign).  
3. **Lead traceability:** every lead must reference the sub-agent ID + capture channel; missing metadata = reject lead.  
4. **Audit parity:** sub-agents are subject to the same quarterly sampling and can be suspended independently.  
5. **Liability:** primary agent remains wholly liable for misconduct and must cover remediation costs if sub-agent actions cause regulator filings or student harm.

---

## 6) Audit cadence + toolkit

- **Frequency:** quarterly for all active Romania agents; ad-hoc after incidents or upon entering new cities/channels.  
- **Sample size:** minimum 10 recent leads (or 20% of quarter leads if <50 total).  
- **Inputs requested:** consent proof checklist, marketing artifacts, sub-agent roster updates, complaint log, data deletion log, commission reconciliation.  
- **Execution:** use the consent checklist template; score each requirement (pass/partial/fail).  
- **Outputs:** audit memo stored in `/countries/romania/reports/` (if applicable) + remediation tickets for any fail.  
- **Escalation levels:**  
  - Pass = continue standard cadence.  
  - Conditional pass = 30-day corrections + follow-up audit.  
  - Fail = suspend referrals until fixed; repeat fail = termination review.

---

## 7) Operational enforcement summary

- **Before first lead:** complete due diligence, sign contract with GDPR + sub-agent clauses, deliver compliance briefing, collect template acknowledgments.  
- **During partnership:** maintain quarterly audits, monitor digital campaigns, verify invoices align with actual enrollments, and refresh consent wording annually or whenever legal text changes.  
- **Documentation hygiene:** keep completed templates + audit outputs in the agent’s record; never push student PII into the repo.  
- **Collaboration loop:** Enrollment Ops owns this playbook, Legal reviews major updates, Marketing approves claim wording, Finance enforces anti-rebate clauses.

By following this SOP + the accompanying templates, Romania agent operations remain auditable, privacy-safe, and on-brand for both UNIC Nicosia and UNIC Athens.
