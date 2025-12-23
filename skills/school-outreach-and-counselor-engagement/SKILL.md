---
name: school-outreach-and-counselor-engagement
description: Global, end-to-end workflow for targeting, contacting, visiting, and cultivating schools and counselors to recruit for UNIC and UNIC Athens.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: global
---

# School outreach and counselor engagement (global)

## Goal

Provide a consistent playbook for how UNIC and UNIC Athens teams (staff or agents) target, contact, visit, and nurture schools and counselors. The skill is **country-agnostic**; local etiquette, holiday calendars, and language guidance belong in country addenda (see [Country addenda](#country-addenda-and-paths)).

Outcomes:
- Prioritized, consented counselor contacts with clear engagement history.
- Repeatable visit/meeting flow with artifacts ready (deck, one-pagers, data capture forms).
- Clean data logged for pipeline, yield, and event follow-up.

---

## Before you start

1) Read the executing ticket for scope and allowed paths.
2) Align on the country addendum (or create one) for etiquette, languages, and local school-year nuances.
3) Pull the latest program positioning: `/UNIC/**` for Nicosia vs Athens reference material.

---

## Country addenda and paths

- Local etiquette, holidays, preferred messaging apps, and naming conventions should live under:  
  `countries/<country>/skills/school-outreach-and-counselor-engagement/ADDENDUM.md` (reflects the updated `countries/` path).
- Reference local school and counselor lists from `countries/<country>/entities/` or `countries/<country>/go-to-market/` as applicable; do not duplicate them in the global skill.

---

## Roles and responsibilities

- **Owner (country team or agent lead):** Sets targeting priorities, approves outreach cadences, and ensures data quality.
- **Outreach executor (recruiter/agent):** Runs sequences, schedules visits, captures meeting notes, and uploads artifacts.
- **Data steward:** Reviews CRM/log quality weekly, fixes missing fields, and aligns with measurement standards.

---

## Targeting and list build

1) **Anchor list:** Start from the country’s priority schools list (if missing, create via a ticket). Include counselor names, roles, and contact channels.
2) **Prioritize:** Use a simple scoring model:
   - Demand fit (STEM/Health focus, international curriculum, outbound mobility history).
   - Access (existing relationship, alumni presence, warm introductions).
   - Timing (exam cycles, fair calendars, deadlines).
3) **Consent & compliance:** Check data capture permission per country addendum; log consent source and date.
4) **Data completeness fields:** School name, counselor name/role, email, phone/WhatsApp (if permitted), language preference, past interactions, and priority tier (A/B/C).

---

## Outreach sequences (templates to localize)

Use lightweight multichannel sequences; stop or slow down after explicit opt-out.

### New contact (email-led, 4 touches across 12–14 days)
1. **T0 (Day 1):** Introduction email with crisp value prop for UNIC + Athens, 2–3 relevant programs, and request for a 20–30 min call/visit; include link to program overview deck.
2. **T1 (Day 3–4):** Reply-on-thread bump with proposed time slots; attach 1-page counselor cheat sheet.
3. **T2 (Day 7–8):** Alternate channel (call or WhatsApp if permitted) focusing on outcomes (placement, scholarships, visa stability) + offer to share student cases.
4. **T3 (Day 12–14):** Final nudge with short survey or Calendly link; state you will pause unless they opt in.

### Dormant contact reactivation (3 touches across 10 days)
1. Value update: new scholarships/intakes, application window reminders.
2. Proof: recent student placements, new articulation or credit transfer options.
3. Action: invite to webinar/virtual counselor briefing; provide signup link.

### Post-event/fair follow-up (within 72 hours)
1. Thank-you email with recap bullets, programs requested, and links promised.
2. Schedule: offer a 15–20 min debrief; send booking link.
3. Data capture: attach/update meeting notes in CRM; tag event name and date.

---

## Visit/meeting preparation

1) **Prep checklist**
- Confirm attendees, room, and AV; ensure materials in local language if required by addendum.
- Print/bring: program one-pagers (Nicosia vs Athens), admissions timelines, scholarship summary, and a QR link to counselor resource folder.
- Pre-fill visit agenda and leave-behind packet; map questions to target programs.

2) **Artifacts to carry or share**
- **Deck:** UNIC + UNIC Athens positioning, key programs, admissions timelines, and graduate outcomes.
- **Counselor cheat sheet (1 page):** eligibility, document checklist, deadlines, fees, scholarship overview, and application portal link.
- **Student-facing flyer (optional):** QR to virtual tour, sample SOPs, and quick start checklist.
- **Data capture form:** digital or paper template with the fields in [Data capture fields](#data-capture-fields).

---

## Meeting/visit agenda (45–60 minutes, adjust locally)

1. **Arrival and context (5 min):** Reconfirm goals, number of students in relevant tracks, and counselor priorities.
2. **University positioning (10–12 min):** Contrast UNIC vs UNIC Athens (programs, cost, language of instruction, residency outcomes).
3. **Program spotlight (10–15 min):** 2–3 programs aligned to the school’s profile; include entry criteria and timelines.
4. **Process walkthrough (10 min):** Application steps, document checklist, review timelines, and decision triggers.
5. **Scholarships/financials (5–8 min):** Merit/need options, payment plans, and incentives; avoid promising custom discounts without approval.
6. **Student case studies (5 min):** Local/regional success stories; keep names anonymized unless consented.
7. **Next steps (5 min):** Agree on upcoming events (webinar/class talk), materials needed, and data to be shared.

---

## Data capture fields

Capture consistently for every touchpoint. Minimum fields:
- School and campus (if multi-campus), city, and country.
- Counselor/contact: name, role, email, phone/WhatsApp (if permitted), language.
- Interaction type (email, call, visit, webinar, fair) and date.
- Programs of interest (Nicosia vs Athens), intake term, and student volume estimate.
- Questions/objections raised; materials shared; commitments made.
- Next action owner and due date.
- Opt-in/consent status + source.

Recommended structure: log in CRM; if working offline, use a CSV aligned to `/skills/data-model-csvs-and-profiles/SKILL.md` then import.

---

## Follow-up and nurture cadences

- **After meeting/visit (within 24–48 hours):**
  - Send recap with agreed actions, program links, and scholarship summary.
  - Share recording or deck if requested; include QR/links to application portal.
  - Book the next touch (webinar, class talk, application workshop).
- **Warm nurture (monthly):** Program updates, scholarship windows, student stories, and deadlines.
- **Hot cycles (application windows):** Weekly check-ins on candidate pipeline, document readiness, and decision timelines.
- **Dormant contacts (>90 days inactive):** Move to reactivation sequence; reassess priority tier.

---

## Measurement and QA

- **Contactability:** % of priority list with verified counselor emails and phone/WhatsApp (if allowed).
- **Engagement:** Reply rate, meeting set rate, and attendance for visits/webinars.
- **Conversion:** Applications started, submitted, and offers/acceptances attributable to each school.
- **Data quality:** % interactions with complete required fields; weekly QA by data steward.
- **Cycle speed:** Time from first contact to first meeting, and to first submitted application.

Run a monthly review to refresh priority tiers and retire inactive schools; document changes in the relevant country addendum to keep the global skill stable.

---

## Risk and escalation guardrails

- Do not promise bespoke discounts or scholarships without documented approval.
- Respect local contact rules (GDPR/PDPA equivalents) per country addendum; honor opt-outs immediately.
- Avoid spamming counselors—cap sequences to 3–4 touches unless they opt in.
- If artifacts need translation, use country addenda to assign ownership and approval steps.

---

## How to adapt locally (without changing this file)

- Create or update `countries/<country>/skills/school-outreach-and-counselor-engagement/ADDENDUM.md` with:
  - Language and tone adjustments.
  - Preferred channels (e.g., WhatsApp/WeChat/Telegram) and quiet hours.
  - School-year calendars, exam blocks, and blackout dates.
  - Required legal notices or consent language.
- Keep global sections intact; addenda should **extend**, not override, unless a structure ticket mandates changes.
