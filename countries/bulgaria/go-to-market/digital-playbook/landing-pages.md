# Bulgaria landing pages — requirements spec (UNIC Nicosia + UNIC Athens)

This spec defines the **minimum landing page set**, **page template requirements**, **localization rules**, and the **form + routing logic** needed to grow Bulgaria leads without creating Athens/Nicosia follow-up confusion.

Primary users: Bulgaria digital + admissions ops + counselors.

## 1) Principles (non-negotiables)

- **One page = one primary intent:** a prospect should know *what they are inquiring about* (campus + program) in <10 seconds.
- **Campus clarity first:** every page and every follow-up must state **UNIC Nicosia** or **UNIC Athens** explicitly.
- **Short forms for paid traffic; longer forms for high intent:** start with 5–7 required fields, then progressive profiling.
- **Bulgarian-first top-of-funnel:** Bulgarian (BG) copy is required for paid prospecting; English (EN) versions are required for international parents/diaspora and high-intent search where appropriate.
- **Compliance is part of conversion:** GDPR-consistent consent, clear privacy link, and a consent text/version stored with the lead record.

## 2) Required landing pages (launch v1)

### Must-have (ship first)

These are required to run Bulgaria campaigns at scale with accurate routing.

| Page ID | Page name | Language versions | Primary audience | Primary CTA | Notes |
|---|---|---|---|---|---|
| `BG-HUB-001` | Bulgaria hub (UNIC Nicosia + UNIC Athens) | BG + EN | Students (17–24), parents | “Get a consultation” / “Ask a question” | The **only** page allowed to compare campuses at a high level; routes into program LPs. |
| `BG-MD-NIC-001` | Medicine (MD) — UNIC Nicosia | BG + EN | Grade 11–12 + parents | “Check eligibility” | Campus-specific to avoid mixing medical workflows. |
| `BG-MD-ATH-001` | Medicine (MD) — UNIC Athens | BG + EN | Grade 11–12 + parents | “Check eligibility” | Campus-specific; align messaging with Athens fee structure (as applicable). |
| `BG-TECH-001` | Computing in English (Computer Science + Data Science) — campus choice | BG + EN | Students (STEM) + parents | “Request program advice” | Dual-campus page requires **campus preference** in the form. |
| `BG-BIZ-001` | Business in English (Business/Accounting/Marketing) — campus choice | BG + EN | Students + parents | “Get a tuition & scholarship estimate” | Dual-campus page requires **campus preference** in the form. |

### Nice-to-have (v2 backlog)

Ship these after v1 is stable and routing quality is proven.

| Page ID | Page name | Why it matters | When to build |
|---|---|---|---|
| `BG-NIC-NURS-001` | Nursing — UNIC Nicosia | Separate healthcare funnel; different objections and compliance | After MD CPL stabilizes |
| `BG-NIC-LAW-001` | Law (LLB) — UNIC Nicosia | High-intent niche; avoid confusion with Athens Greek-taught law | After v1 hub + tech pages |
| `BG-PARENTS-001` | Parent guide (campus, safety, housing, support) | Improves conversion on parent-heavy segments | After initial proof points exist |
| `BG-COUNSELORS-001` | Counselor/career office page | Enables school pipeline and counselor referrals | When school outreach playbook is active |
| `BG-OPEN-DAY-001` | Open day / webinar registration | Event-driven spikes and retargeting | Before peak Feb/Jun–Jul outreach |

## 3) Page template requirements (apply to every Bulgaria LP)

### 3.1 Required blocks (copy + UX)

1) **Hero (above the fold)**
   - Explicit campus label: **UNIC Nicosia** or **UNIC Athens** (or both, only on `BG-HUB-001`)
   - Program label (if program LP)
   - 1-sentence value proposition in BG + matching EN version
   - Primary CTA button anchored to form

2) **“Why this campus/program” (proof points)**
   - 3–5 bullets max; no dense paragraphs
   - Must include at least:
     - **Recognition/licensure guidance** framing (see FAQ requirements below)
     - **Language of instruction** (English vs Greek) clearly stated
     - **Tuition currency** (EUR) and scholarship availability framing (no promises)

3) **Costs & scholarships (high visibility)**
   - Tuition displayed in **EUR** and optionally shown as an **approx. BGN estimate** (with “FX varies” disclaimer)
   - Scholarship framing: “merit/need-based options may apply” + link to current scholarship source for the campus (if available)
   - Include non-tuition costs bucket (housing, insurance, admin fees) as **categories**, not fabricated totals

4) **Admissions steps (reduce friction)**
   - 4–6 steps max (Inquiry → Eligibility → Documents → Offer → Deposit/Enrolment)
   - Make **intake timing** explicit (see calendar guidance below)

5) **Student life & housing (minimum viable reassurance)**
   - 3 bullets + 1 photo module (real assets)
   - Link to the relevant campus housing pages (see `UNIC/**/housing/`)

6) **FAQ (required questions; exact list in section 6)**

7) **Footer trust**
   - Privacy policy link + consent language (see form spec)
   - Contact details (email/phone) and timezone
   - “Campus confirmation” line: “Your inquiry is for: [Campus]”

### 3.2 Bulgaria-specific copy requirements

- Always include a short **“Returning to Bulgaria”** panel:
  - For non-regulated careers: recognition may be employer-led; for regulated professions, a formal route applies.
  - Link internally to: `countries/bulgaria/market/recognition-and-licensure.md`
- Always include a **timing nudge** aligned to Bulgaria exam season and decision windows:
  - Link internally to: `countries/bulgaria/market/exams-and-calendar.md`

## 4) Localization checklist (BG/EN)

### 4.1 Language and tone

- Bulgarian version uses **clear, non-technical Bulgarian**; avoid legal jargon in the hero and lead paragraphs.
- English version is written for diaspora + international parents (short sentences, no idioms).
- Use consistent campus naming:
  - “**UNIC Nicosia (Cyprus)**”
  - “**UNIC Athens (Greece)**”

### 4.2 Numbers, dates, grades

- Currency: tuition in **EUR**, optionally show **BGN estimate** with a “rate varies” note.
- Dates: prefer **Month YYYY** and avoid ambiguous numeric formats.
- Bulgarian grade scale: when asking for grades, use **2–6** scale guidance (label it explicitly).

### 4.3 Proof points and compliance

- Do not claim guaranteed recognition, licensure, or jobs. Use “typical pathway” language and point to the Bulgaria recognition brief.
- Any accreditation/authority statements must be **campus-accurate** (Athens vs Nicosia).
- Always display the privacy link and GDPR consent text near the submit button.

## 5) Form spec (fields + validations)

### 5.1 Two form modes (recommended)

- **Short form (paid traffic default):** 5–7 required fields; optimize CPL and speed.
- **Long form (high-intent search / organic):** adds qualification fields; optimize downstream conversion and counselor efficiency.

### 5.2 Required lead routing fields (must exist on every submission)

These prevent Athens/Nicosia confusion and ensure correct ownership.

| Field | Required | Type | How it’s set | Purpose |
|---|---:|---|---|---|
| `campus_preference` | Yes* | enum | User selection (dual-campus) or hidden default (campus-specific) | Drives assignment + follow-up collateral. |
| `campus_assigned` | Yes | enum | Set by routing logic | The campus team that owns the lead. |
| `program_interest` | Yes | string | User selection or hidden default | Primary program line of interest. |
| `degree_level` | Yes | enum | User selection or hidden default | `undergraduate` / `postgraduate` / `other`. |
| `intake_preference` | Yes | string | User selection | Prevents “wrong intake” follow-up. |
| `language_preference` | Yes | enum | Auto from page + user override | `bg` / `en`. |
| `landing_page_id` | Yes | string | Hidden | Enables LP-level performance analysis. |
| `utm_source` / `utm_medium` / `utm_campaign` / `utm_content` / `utm_term` | Yes (if present) | string | Hidden capture | Attribution and creative learning. |

\*On dual-campus pages, `campus_preference` must be **explicitly chosen** (not inferred).

### 5.3 Short form (minimum viable required fields)

| Field | Required | Notes |
|---|---:|---|
| First name | Yes | Bulgarian + Latin allowed. |
| Last name | Yes | Bulgarian + Latin allowed. |
| Email | Yes | Use double-entry validation only on long form. |
| Phone (mobile) | Optional (recommended) | Default country code `+359`; store E.164. |
| City | Optional | Useful for event targeting (Sofia/Plovdiv). |
| Program interest | Yes | Dropdown; prefilled on program LPs. |
| Campus preference | Yes* | Required on dual-campus pages; hidden on campus-specific. |
| Intake preference | Yes | Use human-readable values (e.g., “Feb 2026”, “Sep 2026”, “Next available”). |
| Consent (data processing) | Yes | Checkbox + privacy link; store timestamp + text version. |
| Marketing consent | No | Separate optional checkbox. |

### 5.4 Long form (qualification fields; add after v1)

Only add when counselors confirm these fields improve conversion-to-enrolment.

| Field | Why add it |
|---|---|
| Current grade / year (e.g., Grade 11/12) | Align outreach to Matura timing. |
| Average grade (BG 2–6) | Fast eligibility triage for competitive programmes. |
| English level (self-report + test option) | Drives language-support messaging. |
| Preferred contact channel (phone/email/Viber/WhatsApp) | Reduces missed contacts; capture consent by channel. |
| Parent contact (optional) | Improves yield on parent-led decisions; GDPR-sensitive, use carefully. |

### 5.5 GDPR consent language requirements (structure)

Do not treat this as legal advice; the enrollment team must review with compliance. Minimum structure:

- **Required checkbox (data processing + contact for admissions):**
  - “I agree that my personal data will be processed by the University of Nicosia / UNIC Athens for the purpose of handling my enquiry and admissions guidance, in line with the Privacy Notice.”
- **Optional checkbox (marketing):**
  - “I agree to receive updates about programmes, events, and scholarships. I can unsubscribe at any time.”
- Always show:
  - a **Privacy Notice link**
  - `consent_timestamp`
  - `consent_text_version` (e.g., `bg-v1-2025-12-22`)

## 6) FAQ requirements (minimum set)

Every must-have landing page includes an FAQ section with Bulgaria-relevant answers and internal links.

### Recognition & licensure (Bulgaria)
- “Will my degree be recognized in Bulgaria?” (academic recognition vs employer-led recognition)
- “What if my profession is regulated (medicine/nursing/pharmacy/law)?”
- “How long does recognition usually take and which authority handles it?”
- Link internally to: `countries/bulgaria/market/recognition-and-licensure.md`

### Costs, scholarships, and payments
- “What are the tuition fees and what else should I budget for?”
- “Are scholarships available for Bulgarian students?”
- “Can I pay in instalments?”
- Link to campus scholarship/admissions sources under `UNIC/` where applicable.

### Deadlines and timing
- “When should I apply if I am in Grade 12 in Bulgaria?”
- “What happens around Matura exams and results?”
- Link internally to: `countries/bulgaria/market/exams-and-calendar.md`

### Housing and student life
- “Where can I live and what does it cost?”
- “Is accommodation guaranteed?”
- Link to: `UNIC/unicnicosia/housing/README.md` and/or `UNIC/unicathens/housing/README.md`

## 7) Routing logic (prevent Athens/Nicosia confusion)

### 7.1 Rules

1) **Campus-specific LPs (`BG-MD-NIC-001`, `BG-MD-ATH-001`, etc.)**
   - Set `campus_preference` and `campus_assigned` as hidden fields.
   - Do not show a campus dropdown (avoid accidental mismatches).

2) **Dual-campus LPs (`BG-TECH-001`, `BG-BIZ-001`, `BG-HUB-001`)**
   - Make `campus_preference` **required**.
   - If a prospect selects a program that is only available on one campus, auto-set the campus and show it as locked.

3) **No silent inference**
   - If `campus_preference` is missing, route to a **Bulgaria triage queue** with a first-touch script that confirms campus before sending programme collateral.

### 7.2 Follow-up safety checks (operations)

- Every outbound email/SMS/WhatsApp template must include:
  - **Campus name in the subject line or first line**
  - Program name
  - Intake preference
- First counselor touchpoint script starts with:
  - “I’m calling from **[UNIC Nicosia / UNIC Athens]** about your enquiry for **[program]** starting **[intake]** — is that correct?”

## 8) Build checklist (definition of “ready to launch”)

- Page loads <2 seconds on mobile; form works on iOS/Android.
- All submissions contain `campus_preference`, `campus_assigned`, `program_interest`, `intake_preference`, and `landing_page_id`.
- Consent checkbox required; privacy link visible; consent metadata stored with lead.
- Thank-you page confirms campus + program and offers next step (book a call / upload docs).
