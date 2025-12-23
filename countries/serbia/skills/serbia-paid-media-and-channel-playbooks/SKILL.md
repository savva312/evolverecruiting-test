---
name: serbia-paid-media-and-channel-playbooks
description: Build and maintain Serbia-specific paid media + channel playbooks (Search/Meta/TikTok/YouTube/retargeting/messaging), tied to Serbia’s calendar and UNIC/UNIC Athens program clusters. Produces executable campaign structures, creative briefs/copy libraries, KPI guardrails, and structured CSVs for tracking spend, UTMs, CPL/CPA, and funnel performance.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: serbia
license: Proprietary (UNIC Evolve internal)
---

# Serbia: paid media & channel playbooks (skill)

## How this skill relates to the global playbook
- Use the global baseline at `/skills/paid-media-and-channel-playbooks/SKILL.md` for shared objectives, schemas, and workflow.
- Use this Serbia file for calendar, flighting, localization, and compliance specifics that layer onto the global spec.

### Serbia addendum: localization and compliance anchors
- Language: SR + EN variants for ads and LPs; add SR subtitles/captions for video when SR is primary.
- Consent and messaging: Viber/WhatsApp/SMS require explicit opt-in; avoid unsolicited outreach. Treat GDPR-style consent and data handling as the default bar.
- Regulated programs: For Medicine/health, include recognition/licensure disclaimers and avoid job or visa guarantees. Align flighting with Matura/exam periods when planning campaigns.

## Purpose
This skill turns Serbia recruiting strategy into **executable, measurable acquisition** across digital channels—without drifting into generic EU recruiting advice.

It produces:
- Serbia-specific channel strategy by **program cluster** (e.g., Medicine vs CS/Data/AI vs Business, etc.)
- campaign architecture (what to run, where, when, and why)
- localization-ready copy + creative briefs that are compliant and consistent
- a measurement/UTM and dashboarding spec so results can be compared week-to-week
- structured CSVs for spend and performance tracking inside the repo

## When to use
Use this skill when a ticket asks for any of:
- “Serbia paid media plan” (budget, channels, flighting, KPIs)
- “Search keyword plan for Serbia” (SR + EN queries, negatives)
- “Meta/TikTok creative system + copy library (Serbian)”
- “UTM + attribution rules” (including partners/agents)
- “Retargeting + offer-holder nurture flows”
- “Calendar-driven flighting around IB/Matura/WEF/etc.”

## Hard constraints (read first)
1) **Follow ticket boundaries.**
   Before writing, open the active ticket in `/tickets/` and follow:
   - Allowed write paths
   - Files to create/update
   Do not write outside ticket boundaries.

2) **No unverified claims.**
   Paid media assets frequently repeat facts (tuition, language, recognition, scholarships).
   - Only use claims that are backed by official sources (UNIC/UNIC Athens) or by repo facts that themselves cite official sources.
   - If a claim cannot be verified, remove it or mark as draft for verification.

3) **Serbia-specific only.**
   Avoid generic “international students in Europe” guidance unless the ticket explicitly requests a generalized section.

4) **Privacy and compliance are mandatory.**
   - Do not write or store personal data in the repo (no student names, emails, phone numbers).
   - Any tracking approach must assume GDPR requirements (consent, purpose limitation).
   - Do not propose “agent rebates” or misleading scholarship promises.

5) **Separate: facts vs tactics.**
   This skill creates tactics (campaigns, copy, budgets), but it must reference the repo’s facts layer:
   - `/data/` for program pricing/language facts
   - cluster definitions
   - Serbia calendar windows

## Inputs (what this skill depends on)
This skill usually depends on:
- Program cluster taxonomy (repo-defined)
- UNIC/UNIC Athens portfolio facts (language, tuition, intakes, admissions)
- Serbia education calendar + exam blackouts
- Priority schools + city clusters (Belgrade / Novi Sad / Nis / Kragujevac + regional)
- Partner/agent list (for co-marketing and attribution)

If those are incomplete, write what you can and open/append “missing prerequisites” notes in the ticket’s scratchpad area (as allowed).

## Outputs
Depending on the ticket, produce one or more of:

### A) Channel playbook markdown
Recommended sections:
- Objectives (by cluster)
- Audience segmentation (student vs parent vs counselor)
- Channel mix rationale (Search vs Social vs Video vs Retargeting)
- Serbia-specific seasonality + flighting (Jan–Oct; exam blackouts)
- Creative system + hooks (by persona/cluster)
- Landing page requirements (Serbia-ready)
- KPIs + guardrails + action thresholds
- Measurement spec (UTMs, offline conversions)
- Compliance checklist (claims, disclaimers, recognition links)

### B) Structured CSV(s) for operational tracking
If the repo already has schemas, follow them. Otherwise, use these recommended schemas.

#### `paid_media_campaign_plan.csv` (recommended)
One row per campaign group.

Columns:
- `country` (always `RS`)
- `cluster` (must match repo cluster tags)
- `channel` (`Google_Search`, `Meta`, `TikTok`, `YouTube`, `Display`, `Viber`, etc.)
- `objective` (`Leads`, `Applications`, `Webinar_Registrations`, `Retargeting`, `OfferHolder_Conversion`)
- `target_cities` (semicolon separated)
- `language` (`SR`, `EN`, `SR+EN`)
- `flight_start` (YYYY-MM-DD)
- `flight_end` (YYYY-MM-DD)
- `monthly_budget_eur` (number)
- `primary_kpis` (semicolon separated)
- `benchmarks` (short text: CPC/CPL/CTR targets)
- `landing_page_ref` (path or slug; no URLs if repo uses internal refs)
- `notes`

#### `utm_spec.csv` (recommended)
Defines canonical UTMs so all agents and channels match.

Columns:
- `utm_source`
- `utm_medium`
- `utm_campaign_pattern`
- `utm_content_pattern`
- `utm_term_pattern`
- `required_fields` (e.g., `city;cluster;persona;partner`)
- `examples`
- `last_updated`

#### `creative_library.csv` (recommended)
One row per creative concept.

Columns:
- `cluster`
- `persona`
- `hook_short`
- `claim_type` (`pricing`, `recognition`, `proximity`, `capacity`, `outcomes`, `scholarship`)
- `claim_text`
- `required_source_refs` (paths/urls to sources)
- `format` (`9x16_video`, `carousel`, `static`, `youtube_60s`, etc.)
- `cta`
- `language`
- `notes_compliance`

### C) Copy blocks (Serbian + English)
A markdown file (or folder of files) containing:
- ad copy (short/long)
- landing page copy blocks
- webinar titles/descriptions
- SMS/Viber nudge templates (offer-holder)
All must be cluster-tagged and fact-checked.

## Workflow (step-by-step)
### Step 0 — Read the ticket and scope the deliverables
- Identify program clusters in scope (e.g., MD, CS/Data/AI, Business, etc.)
- Confirm allowed write paths and required output formats (MD vs CSV vs both)

### Step 1 — Anchor to Serbia’s calendar (non-negotiable)
Use the repo’s Serbia calendar skill outputs to define:
- heavy acquisition windows (Feb–Mar; Sep–Oct)
- blackout windows (IB and Matura periods; other key school breaks)
- deadlines that materially change conversion (deposit / early-decision if applicable)

Deliverable: a short “flight map” table for Serbia.

### Step 2 — Define personas per cluster
At minimum:
- Student (high intent) + Parent (co-decision) + Counselor/Agent influence
- Serbia-specific variations (Belgrade IB school vs regional elite language school, etc.)

Deliverable: persona matrix by cluster.

### Step 3 — Build campaign architecture per channel
For each channel:
- campaigns by cluster + stage (prospecting, consideration, retargeting, offer-holder)
- targeting (city, age bands, interests, lookalikes from consented first-party lists)
- guardrails (negatives, exclusions, frequency caps conceptually)
- creative requirements and rotation cadence

Deliverable: campaign plan + rationale.

### Step 4 — Create creative system and copy library
- Hooks must be Serbia-relevant (proximity, calendar deadlines, transparent cost)
- Every numeric claim must cite official sources or repo facts that cite sources
- Include “Do not say” rules (e.g., transport discounts if not applicable)

Deliverable: creative library + ready-to-run copy blocks.

### Step 5 — Landing page + funnel requirements
Define the minimum LP elements to match Serbia expectations:
- net price clarity (but only if scholarship policy is published and sourced)
- realistic COA bands (if the repo maintains them)
- recognition/quality assurance links (one-click)
- clear next steps (apply, consult, webinar, fast pre-check)

Deliverable: LP checklist and flow diagram (text-based is fine).

### Step 6 — Measurement & reporting spec
- canonical UTMs (including partner attribution where relevant)
- offline conversion upload requirements (offers, deposits, starts) as a process spec
- weekly dashboard fields and thresholds

Deliverable: UTM spec + KPI table.

### Step 7 — Compliance review checklist
Before finalizing, ensure:
- no invented scholarships/discounts
- no misleading “guarantees”
- regulated profession messaging (Medicine) includes appropriate disclaimers
- GDPR/consent assumptions are respected in any tracking or list usage

Deliverable: a “release checklist” at bottom of the playbook.

## KPI guardrails (recommended defaults; adjust if ticket specifies)
These are starting points; calibrate using historical Serbia results if available.

- Search:
  - Non-brand CTR: 5–8%
  - CPC: target bands by cluster (define in ticket)
  - LP conversion (click→lead): 8–12%

- Meta:
  - CTR: 1.0–1.5%
  - Lead rate: 6–9%
  - CPL threshold: define in EUR and enforce 72-hour rule after minimum spend

- TikTok:
  - CTR: ~1.0% (creative-dependent)
  - Lead rate: ~6–8%

- YouTube:
  - CPV: define band; treat as awareness/retargeting feeder
  - Use retargeting to convert, not video alone

Action thresholds:
- Pause or rework any ad set that is ≥25% above CPL target after a minimum spend threshold defined in ticket.
- Rotate creatives that underperform CTR benchmarks after sufficient impressions.

## Common pitfalls
- Mixing clusters (Medicine messaging accidentally used in general UG campaigns)
- Using “net price” language without a published scholarship basis
- Generic EU recruiting advice (not Serbia-specific)
- Storing personal lead data in repo
- Failing to align flighting to IB/Matura windows
- Claim drift (pricing or recognition statements not consistent with portfolio facts)

## Definition of Done (DoD)
A ticket using this skill is “done” when:
- There is an executable Serbia channel plan tied to calendar windows
- Copy/creative concepts are cluster-tagged and fact-checked
- Measurement spec exists (UTMs + dashboard fields)
- Any structured CSV outputs required by ticket are created/updated
- All outputs remain within the allowed write paths for the ticket
