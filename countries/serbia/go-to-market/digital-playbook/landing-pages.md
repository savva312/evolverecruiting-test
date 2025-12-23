# Landing pages

Serbia-facing landing pages must convert high-intent traffic from paid media, counselors, and partner referrals into routed inquiries for UNIC Nicosia and UNIC Athens. This spec defines the page stack, non-negotiable sections, proof-point sources, and GDPR-compliant form/routing logic so Marketing, Admissions, and country teams can build consistently.

## Required page stack (minimum viable set)

| Page | Primary audience | Program cluster alignment | Localization | Core CTA(s) | Notes |
| --- | --- | --- | --- | --- | --- |
| Serbia general hub | Students + parents early in research | All clusters; serves as entry to others | SR hero + EN toggle | `Book a call`, `Chat on WhatsApp/Viber`, `Download Serbia guide` | Anchor SER market stats, highlight dual-campus system, route to comparison + cluster pages. |
| Athens vs Nicosia comparison | Applicants comparing campuses | Cross-cluster; reference shared programs | SR/EN split sections | `Compare campuses`, `Ask a counselor` | Live comparison matrix (tuition, housing, visas) pulling facts from `UNIC/**`. |
| Medicine (MD + Health) | Pre-med students, parents, counselors | `countries/serbia/program-clusters/medicine-md/` + `health-pharmacy-allied-health/` | SR primary, EN for accreditation blocks | `Reserve consultation`, `Download MD brief` | Include licensure disclaimer, clinical rotation map, scholarship info. |
| CS/Data/AI/Cyber | STEM prospects, hackathon partners | `cs-data-ai-cyber/serbia-playbook.md` | SR hero with EN tech jargon allowed | `See curriculum`, `Join virtual lab tour` | Highlight blockchain/fintech leadership, internship placements, and Athens offerings. |
| Business/Finance/Marketing | Business-focused students + parents | `business-finance-accounting-marketing/serbia-playbook.md` | SR hero; EN proof for ACCA/CIMA | `Talk to an advisor`, `Download career outcomes` | Feature mobility between campuses and employer partnerships. |
| Scholarships & affordability | Price-sensitive families, agents | All clusters; pair with `UNIC/*/scholarships` | SR cost calculator + EN policy detail | `Check eligibility`, `Email counselor PDF` | Present tuition ranges, payment plans, and documentation checklists. |
| Events & fairs calendar | Students, parents, counselors | All clusters; tie to `countries/serbia/entities/fairs` as added | SR-first with EN date format | `Register for event`, `Add to calendar` | Include webinar recordings, fair RSVP forms, and on-demand counselor sessions. |

> Optional pages once the above are live: Psychology/Psychotherapy, Law & Governance, Offer-holder hub, and Agent/co-branded microsites. Do not prioritize optional pages ahead of the mandatory seven.

## Mandatory module stack (applies to every landing page)

1. **Hero band (SR-first)** with subheadline naming the relevant campus(es) plus two CTAs: `Book a call` (Calendly or CRM form) and `Chat via WhatsApp/Viber`.
2. **Proof-point strip** (3–4 items) pulling facts from the sources listed under “Content source references.” Include at least one accreditation/recognition proof, one outcome/employer stat, and one housing/visa readiness callout.
3. **Program fit + outcomes** section that links directly to the relevant cluster playbook (e.g., `../program-clusters/medicine-md/serbia-playbook.md`). Use bullets summarizing Serbia-specific fit.
4. **Tuition + affordability framing** with transparent € ranges, explicit mention of installment plans, and link to `UNIC/unicnicosia/scholarships/README.md` or `UNIC/unicathens/scholarships/README.md` depending on campus.
5. **Recognition/licensure disclaimer** (especially for Medicine, Law, Health). Use italicized text referencing official recognition steps with link to the campus admissions or recognition source.
6. **Counselor/Agent CTA** block offering downloadable toolkits or direct counselor concierge email.
7. **WhatsApp + Viber sticky bar** persistent on mobile and desktop, paired with a fallback `Email us` link.
8. **Form panel** (embedded or modal) that uses the standard fields below and displays GDPR consent language plus link to the privacy notice.
9. **FAQs + supporting links** referencing the canonical UNIC folders (housing, visas, student life) so families can self-serve.

## Page-specific guidance

### Serbia general hub
- **Angle:** “EU degrees with predictable costs, delivered from Nicosia & Athens + Serbia-dedicated onboarding.”
- **Modules beyond the core stack:** Serbia pipeline stats (once available), timeline graphic for intake milestones, CTA tiles for each cluster (“Explore Medicine”, “Explore CS/Data/AI”, etc.).
- **Crosslinking:**  
  - Programs → [UNIC Nicosia programs](../../../../UNIC/unicnicosia/programs/README.md), [UNIC Athens programs](../../../../UNIC/unicathens/programs/README.md)  
  - Visa guidance → [UNIC Nicosia visas](../../../../UNIC/unicnicosia/visas/README.md), [UNIC Athens visas](../../../../UNIC/unicathens/visas/README.md)  
  - Housing overview → [UNIC Nicosia housing](../../../../UNIC/unicnicosia/housing/README.md), [UNIC Athens housing](../../../../UNIC/unicathens/housing/README.md)

### Athens vs Nicosia comparison page
- **Comparison matrix fields:** tuition per year, instructional language, flagship programs, housing distance/cost, visa processing time, part-time work allowances, and student life differentiators.
- **Data pull:**  
  - Tuition and program tables from `UNIC/unicathens/programs/README.md` and `UNIC/unicnicosia/programs/README.md`.  
  - Housing facts from `UNIC/unicnicosia/housing/README.md` and `UNIC/unicathens/housing/README.md`.  
  - Visa steps from `UNIC/unicnicosia/visas/README.md` vs `UNIC/unicathens/visas/README.md`.
- **CTA logic:** one button routes to campus-specific inquiry forms; a secondary CTA invites a joint counselor consult for undecided students.

### Medicine / Health landing page
- **Cluster alignment:** `countries/serbia/program-clusters/medicine-md/serbia-playbook.md` and `health-pharmacy-allied-health/serbia-playbook.md`.
- **Must include:**  
  - Accreditation + recognition copy referencing `UNIC/unicnicosia/programs/README.md` (MD section) and `UNIC/unicathens/programs/README.md` (Pharmacy/Medicine data).  
  - Licensure disclaimer summarizing NACID recognition steps and Serbian language exam expectations (pull from the playbook if detailed; add TODO if data missing).  
  - Clinical rotation map or timeline, linking to official campus program documents (`UNIC/unicnicosia/programs.md` or future detailed files).  
  - Scholarship tile pointing to the campus scholarship page.  
  - Counselor CTA emphasizing medical prerequisites checklist download.

### CS/Data/AI/Cyber landing page
- **Cluster alignment:** `countries/serbia/program-clusters/cs-data-ai-cyber/serbia-playbook.md`.
- **Proof points:**  
  - Blockchain/fintech reputation and internships from `UNIC/unicnicosia/programs/README.md` (CS/Data Science) and `UNIC/unicathens/programs/README.md` (Computer Science/Data Science).  
  - Employability stats referencing any repo data (add placeholder note if metric missing).  
  - Mention dual-campus pathways and highlight remote internship support with link to `UNIC/unicnicosia/student-life/README.md` (once populated).
- **CTA mix:** `Book AI/tech advisor call`, `Register for virtual lab tour`, `Ask about scholarship`.

### Business/Finance/Marketing landing page
- **Cluster alignment:** `countries/serbia/program-clusters/business-finance-accounting-marketing/serbia-playbook.md`.
- **Content requirements:**  
  - ACCA/CIMA exemptions referencing `UNIC/unicnicosia/programs/README.md` (Business & Accounting) and `UNIC/unicathens/programs/README.md` (Accounting, Business Administration).  
  - Mobility narrative (semester in Athens + internship in Cyprus).  
  - Parent reassurance block covering housing + cost-of-living (link to housing READMEs).
- **CTA mix:** `Talk to finance advisor`, `Download ROI calculator (Serbia Dinar + EUR)`, `WhatsApp us`.

### Scholarships & affordability landing page
- **Data sources:** `UNIC/unicnicosia/scholarships/README.md`, `UNIC/unicathens/scholarships/README.md`, plus tuition tables referenced earlier.
- **Modules:**  
  - Tuition comparison chart (Serbia vs UNIC campuses vs UK/EU benchmarks).  
  - Scholarship / discount matrix (merit, early-payment, sibling) with documentation checklist.  
  - Payment-plan explainer referencing campus admissions pages.  
  - FAQ on currency payments, bank instructions, and refund policies.  
  - Counselor CTA to request co-branded affordability decks.

### Events & fairs landing page
- **Purpose:** single registration hub for school visits, webinars, Serbia fairs, and counselor briefings.
- **Content elements:**  
  - Dynamic calendar with timezone-adjusted sessions (Belgrade time default).  
  - Past webinar recordings + summary downloads.  
  - RSVP form using the standard fields; route leads based on event cluster.  
  - Quick links to `countries/serbia/entities/fairs-events` once populated.  
  - WhatsApp/Viber buttons to confirm attendance or request school visits.

## Content source references (link these, do not duplicate)

| Content block | Source path |
| --- | --- |
| UNIC Nicosia program facts (Medicine, CS, Business) | [UNIC/unicnicosia/programs/README.md](../../../../UNIC/unicnicosia/programs/README.md) |
| UNIC Athens program facts and tuition | [UNIC/unicathens/programs/README.md](../../../../UNIC/unicathens/programs/README.md) |
| Admissions policies + document checklists | [UNIC/unicnicosia/admissions/README.md](../../../../UNIC/unicnicosia/admissions/README.md), [UNIC/unicathens/admissions/README.md](../../../../UNIC/unicathens/admissions/README.md) |
| Scholarship rules and eligibility | [UNIC/unicnicosia/scholarships/README.md](../../../../UNIC/unicnicosia/scholarships/README.md), [UNIC/unicathens/scholarships/README.md](../../../../UNIC/unicathens/scholarships/README.md) |
| Visa processes | [UNIC/unicnicosia/visas/README.md](../../../../UNIC/unicnicosia/visas/README.md), [UNIC/unicathens/visas/README.md](../../../../UNIC/unicathens/visas/README.md) |
| Housing/infrastructure proof | [UNIC/unicnicosia/housing/README.md](../../../../UNIC/unicnicosia/housing/README.md), [UNIC/unicathens/housing/README.md](../../../../UNIC/unicathens/housing/README.md) |
| Serbia-specific messaging | [`countries/serbia/program-clusters/*/serbia-playbook.md`](../../program-clusters), [`countries/serbia/go-to-market/digital-playbook/creative-library.md`](creative-library.md), [`countries/serbia/go-to-market/digital-playbook/channel-strategy.md`](channel-strategy.md) |

Always embed relative links (e.g., `[UNIC Nicosia programs](../../../../UNIC/unicnicosia/programs/README.md)`) so downstream builds do not break.

## Form spec (minimal GDPR-compliant)

| Field | Required? | Type | Notes |
| --- | --- | --- | --- |
| First name | Yes | Text | Store as `given_name`; supports Latin characters only. |
| Last name | Yes | Text | `family_name`; keep ≤64 chars. |
| Email | Yes | Email | Primary contact; validate format client-side. |
| Mobile / WhatsApp | Yes | Tel | Default to `+381` prefix with dropdown; label “WhatsApp or mobile.” |
| Viber number | Optional | Tel | Only show if different from WhatsApp; hide if user selects “Same as mobile.” |
| Preferred contact channel | Yes | Single select (`WhatsApp`, `Viber`, `Email`, `Phone call`) | Use to trigger routing SLA expectations. |
| City + high school | Yes | Text with autocomplete | Needed for counselor routing + travel planning. |
| Program cluster interest | Yes | Multi-select mapped to repo clusters (Medicine, CS/Data/AI, Business/Finance/Marketing, Psychology, Law, Design). |
| Campus preference | Yes | Single select (`UNIC Nicosia`, `UNIC Athens`, `Open to both`) |
| Intended intake month/year | Yes | Dropdown (rolling 6 intakes) | Drives urgency messaging. |
| Funding priority | Optional | Single select (`Scholarships`, `Self-funded`, `Employer/Family sponsor`) | Useful for scholarships page. |
| Counselor / agent status | Optional | Checkbox (`I am a counselor/agent`) | Reveals counselor CTA if checked. |
| Consent checkboxes | Yes | 1) GDPR consent; 2) Marketing opt-in (optional) | Text: “I agree to the Privacy Notice and to be contacted by UNIC via my selected channel.” |

Form behavior requirements:
- Autofill `country = Serbia` but allow manual override for diaspora visitors.
- Display privacy link referencing the official UNIC privacy policy (same link used in global assets).
- Trigger GA4/Meta/TikTok conversion events on submit with UTM persistence (use session storage).

## Post-submit routing rules

1. **Immediate confirmation:** on-page thank-you module summarizing next steps plus CTA to download relevant brochure (cluster-specific).
2. **Routing matrix (populate within CRM/marketing automation):**

| Campus preference | Program cluster | CRM queue / owner | Follow-up SLA |
| --- | --- | --- | --- |
| UNIC Nicosia | Medicine / Health | `MED_NIC_RS` (per contacts in `UNIC/unicnicosia/admissions/README.md`) | 24h response; send medical checklist PDF. |
| UNIC Nicosia | CS/Data/AI/Cyber | `STEM_NIC_RS` (Nicosia admissions) | 24h; invite to virtual lab/Q&A. |
| UNIC Nicosia | Business/Finance/Marketing | `BUS_NIC_RS` | 24h; share ACCA exemptions sheet. |
| UNIC Athens | Medicine / Health (MD, Pharmacy) | `MED_ATH_RS` (Athens admissions) | 24h; include HAHE accreditation note. |
| UNIC Athens | CS/Data/AI/Cyber | `STEM_ATH_RS` | 24h; promote Athens tech ecosystem video. |
| UNIC Athens | Business/Finance/Marketing | `BUS_ATH_RS` | 24h; send tuition plan PDF. |
| Open to both | Medicine | Dual routing: `MED_NIC_RS` + `MED_ATH_RS` with flag `needs_comparison` | Joint counselor call within 24h. |
| Open to both | CS/Data/AI or Business | Assign to Serbia enrollment manager queue `GEN_RS` plus notify both campus teams | 24h; share comparison matrix link. |

3. **Counselor/agent submissions:** if the counselor checkbox is selected, CC the Serbia counselor success lead and link them to `countries/serbia/entities/schools` (once built) for tracking.
4. **Events page nuance:** attach `event_id` hidden field to the submission; pass to CRM and marketing automation to send reminder workflows.

## Compliance + QA checklist

- Proof points must cite the source path in hover notes or footers; no external claims without documentation.
- Recognition/licensure disclaimer text must include “Admission does not guarantee professional licensure; confirm local requirements” plus pointers to campus admissions resources.
- Tuition tables must use the latest numbers from campus program files; add “Last verified: YYYY-MM-DD” stamps.
- All WhatsApp/Viber CTAs must point to numbers managed by the Serbia enrollment team with compliance logging.
- Ensure Serbian translations are completed by a native speaker before publishing; store translation memory in the localization workspace.
- Page performance: LCP <2.0s on 4G (optimize media), forms accessible (labels + error states), and analytics events tested across devices.

## Implementation order of operations

1. Finalize copy decks per page using this spec and the creative library hooks.
2. Build layout components (hero, proof, tuition, FAQs) in the chosen CMS with localization toggles.
3. Connect forms to CRM with the routing matrix and confirm auto-responders per cluster/campus.
4. Run compliance review with Admissions (fact check), Legal (GDPR text), and Marketing Ops (tracking).
5. Launch pages sequentially: General hub → Medicine → CS/Data/AI → Business → Scholarships → Comparison → Events (events page can go live in parallel if data ready).
6. Post-launch, log any data gaps (e.g., missing housing stats) in `executions/` and open follow-up tickets if repository updates are required.
