---
name: agents-and-partner-ecosystem
description: Cross-country workflow, taxonomy, templates, and datasets for mapping and operating the education agent and partner ecosystem that supports UNIC and UNIC Athens recruitment.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: global
---

# Agents and partner ecosystem (global)

## Goal

Build a repeatable operational knowledge base of the partner ecosystem that drives student recruitment for UNIC and UNIC Athens across markets:

- **Education agencies** (generalist and medicine-specialist)
- **Fair organizers / event platforms**
- **Counseling networks / consultancies**
- **Related partner entities** that influence reach and conversion (school counseling hubs, career centers if distinct entities, etc.)

Outputs include:
- **Human-readable profiles** (`.md` per partner)
- **Structured datasets** (`.csv`) for evaluation, contracting, SLAs, and performance tracking

Use country addenda (e.g., `country/skills/*-agents-and-partner-ecosystem`) for local nuances.

---

## Before you start

1) Read the ticket you’re executing in `/tickets/` and obey:
- Allowed write paths
- Required outputs
- Prohibited actions (e.g., "do not create new folders", "do not add new partners")

2) Review repo-wide rules if needed:
- `/skills/ticket-boundaries/SKILL.md`
- `/skills/assets-and-sources/SKILL.md`
- `/skills/markdown-authoring/SKILL.md`

---

## Scope boundaries

### In scope
- Country-specific partner entities that influence outbound recruitment to UNIC / UNIC Athens.
- Publicly documented contact channels and business info.
- Partner evaluation criteria, onboarding requirements, SLAs, governance notes.
- Event calendars and participation notes as they relate to the market you’re working on.

### Out of scope
- Generic “how to work with agents” theory not tied to operations.
- Partner performance claims without evidence.
- Personal data beyond official, published business contact channels.

---

## Privacy and data handling

- Prefer **organizational contacts**:
  - official website contact email(s)
  - office phone numbers
  - corporate address
  - official social pages
- Avoid storing personal mobile numbers or private emails unless explicitly published as official business contacts on the partner’s own site.
- Never store student/parent personal data.
- When capturing “key people,” use names and roles only when publicly listed in an official capacity, and still prefer role-based contact channels.

---

## Outputs

### Required outputs (unless the ticket says otherwise)

1) **Partner index (Markdown)**
- Curated list by partner type and city footprint.
- Links to each partner profile.
- Short “how to use this list” section for recruiting operators.

2) **One Markdown profile per partner**
- Standard template
- Includes evaluation notes and operational guidance
- Includes sources and a `last_verified` date

3) **A structured CSV dataset**
- One row per partner
- Designed for routing, evaluation, contracting, and reporting

### Optional outputs (only if the ticket requests)

- A second CSV for partner events/fairs (if a ticket wants a schedule table)
- An SLA template (if requested by ticket)
- A co-marketing/creative requirements checklist (if requested by ticket)

---

## Recommended file locations

Adjust per ticket. Default pattern:

- `market/<country>/partners/index.md`
- `market/<country>/partners/profiles/<partner_slug>.md`
- `data/<country>/partners/<country>-partners.csv`

---

## Partner taxonomy (use consistently)

Classify each partner as one primary type:

- `agency-generalist`
- `agency-medicine-specialist`
- `fair-organizer`
- `counseling-consultancy`
- `school-network` (only if a distinct organizational entity)
- `media-community` (only if it materially affects recruitment)
- `other` (use sparingly; explain)

Capture secondary tags:
- `cities:` key coverage areas for the market
- `program_fit:` medicine, cs-data-ai, business, psychology, design, etc.

---

## What to capture

### A) Identity and footprint
- Official name (local/EN if applicable)
- Legal entity name (if public)
- Offices and coverage (cities served)
- Typical customer segment (parents, students, schools)
- Languages served
- Website and official social links

### B) Services that matter for recruitment
- Consulting / shortlisting
- Application preparation and document handling
- Interview preparation (especially Medicine)
- Event/fair organization and lead capture
- English testing / prep tie-ins (if offered)
- Housing/relocation support (if offered)

### C) Evidence of relevance
Use **credible signals**:
- partner’s own published claims (carefully phrased)
- exhibitor lists (where available)
- public partnerships (HEI partner pages)
- event histories (posted schedules, archives)
If evidence is weak, explicitly mark as such.

### D) Contact channels (org-level)
- Contact email
- Phone
- Address
- Contact form URL
- Official social handles

### E) Operating guidance (actionable)
- Suggested engagement model:
  - referral/commission partnership
  - co-marketing (webinars, fairs)
  - school-access collaboration
- What they are good for (and not good for)
- Risks (misrepresentation, rebates, data handling) — only if evidenced or standard risk patterns apply; be careful not to accuse without facts.
- What to confirm in due diligence

---

## Dataset specification

### File: `<country>-partners.csv`

One row per partner.

Recommended columns:

- `partner_id` (stable slug, e.g., `athens-education-fair`, `lagos-medicine-agency`)
- `partner_name`
- `partner_type` (from taxonomy above)
- `cities_covered` (comma-separated)
- `program_fit_tags` (comma-separated: `medicine`, `cs-data-ai`, `business`, etc.)
- `services` (comma-separated: `shortlisting`, `applications`, `interview-prep`, `fairs`, `webinars`, `visa-support`, `relocation`)
- `website_url`
- `contact_email`
- `contact_phone`
- `address`
- `notes_short` (1–2 sentences, factual)
- `source_name`
- `source_url`
- `last_verified` (YYYY-MM-DD)

Conventions:
- Keep `notes_short` concise and factual.
- Put analysis and recruiting playbook detail into the `.md` profile.

---

## Partner profile template (Markdown)

Each `profiles/<partner_slug>.md` should include:

1) **Snapshot**
- Partner type, footprint, who they serve, what they do

2) **Why this partner matters**
- 3–7 bullets (factual and practical for the market)

3) **Program cluster fit**
- Which clusters they likely influence (medicine vs non-medical)
- Any relevant nuance (e.g., strongest cities or segments)

4) **Engagement playbook**
- How to activate them (webinar, fair, counselor access, referral loop)
- What collateral they need (pricing/recognition pages, deadlines)
- What success looks like (pipeline expectations)

5) **Due diligence checklist**
- Legal entity basics
- Data/privacy posture (GDPR when applicable)
- How leads are captured and transferred (consent flag)
- Any public policies about fees or refunds (if applicable)

6) **Risks and guardrails**
- Prohibit agent rebates / misrepresentation
- Commission base and policy reminders (if applicable)
- Creative approval rules

7) **Contacts**
- Website, email/phone, address, socials

8) **Sources**
- Bullet list of sources
- `Last verified: YYYY-MM-DD`

---

## Procedure (step-by-step)

1) Build an initial partner list
- Start with major fair organizers + top agencies in capital and regional cities.
- Separate medicine-specialists from generalists.

2) Populate the CSV first
- Create stable slugs
- Fill minimum fields
- Add sources + `last_verified`

3) Write/update the index page
- Group by partner type and by city coverage
- Add “activation ideas” per group

4) Write partner profiles
- Use the template
- Keep content specific to the market

5) Quality check
- Every partner has at least one credible source
- No personal/private contact data beyond official business channels
- No unverified accusations or claims

---

## Scoring and prioritization (recommended)

If the ticket asks for tiering, use a simple rubric and document it:

- Coverage footprint (0–25)
- Conversion influence (0–25)
- Segment strength (medicine vs non-medical) (0–20)
- Operational quality signals (0–15)
- Transparency/compliance posture (0–15)

Explain the rationale briefly; avoid over-precision.

---

## Common pitfalls

- Copying “top agency” lists from low-quality sources with no verification.
- Storing personal contacts that are not clearly official business channels.
- Mixing in generic partner-management content instead of market-specific partner intelligence.
- Writing long prose without producing CSV outputs operators need.

---

## “Done” checklist

- [ ] `<country>-partners.csv` exists/updated with sources + `last_verified`
- [ ] `market/<country>/partners/index.md` exists/updated and links to profiles
- [ ] New/updated partner profiles follow the template and are market-specific
- [ ] No personal/private data stored beyond official business channels
- [ ] All outputs are within ticket-approved write paths
