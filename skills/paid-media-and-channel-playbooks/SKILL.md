---
name: paid-media-and-channel-playbooks
description: Build and maintain cross-country paid media and channel playbooks (Search/Meta/TikTok/YouTube/retargeting/messaging) with reusable objectives, campaign schemas, creative systems, and measurement specs that each country can extend via local addenda.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: global
license: Proprietary (UNIC Evolve internal)
---

# Paid media & channel playbooks (global skill)

## Purpose
Turn recruiting strategy into **executable, measurable acquisition** across digital channels while keeping country nuances in country skills. This file defines the common objectives, CSV schemas, and workflow used by all markets.

## When to use
Invoke this skill when a ticket requests any of the following across one or multiple markets:
- Paid media/channel playbooks (budget, mix, flighting, KPIs)
- Search/Meta/TikTok/YouTube plans, keyword sets, or campaign architectures
- Creative system and copy library requests
- UTM/measurement specs and reporting fields
- Retargeting and offer-holder nurture flows

## Hard constraints
1) **Follow ticket boundaries.** Stay within allowed write paths and requested outputs.
2) **Fact-check every claim.** Use only sourced program facts (tuition, recognition, scholarships, deadlines). Do not invent offers or guarantees.
3) **Keep country specifics in country skills.** This file is the global baseline; country files hold calendars, local compliance, and localization rules. Link back to them in deliverables.
4) **Privacy and compliance first.** Assume GDPR-level consent/processing standards, avoid storing personal data in-repo, and do not suggest non-compliant tracking.
5) **Separate facts from tactics.** Reference program data, cluster definitions, and campus positioning before writing tactics.

## Inputs
- Program cluster taxonomy and campus facts (UNIC and UNIC Athens)
- Country calendars and intake windows (pulled from country skills)
- Priority segments (student/parent/counselor/agent) per market
- Local compliance notes (per country skill) and any ticketed constraints
- Partner/agent lists when attribution or co-marketing is required

## Outputs
Depending on the ticket, produce one or more of:

### A) Channel playbook (markdown)
Recommended sections:
- Objectives and success metrics (by cluster/persona)
- Audience segmentation and targeting approach
- Channel mix rationale
- Flighting windows (pull from the relevant country addendum)
- Creative system and hooks
- Landing page requirements
- KPIs, guardrails, and action thresholds
- Measurement spec (UTMs, offline conversion handling)
- Compliance checklist

### B) Structured CSVs (recommended schemas)
Use these schemas unless the ticket supplies another template.

#### `paid_media_campaign_plan.csv`
One row per campaign group.

Columns:
- `country` (ISO-2)
- `cluster` (match repo cluster tags)
- `channel` (`Google_Search`, `Meta`, `TikTok`, `YouTube`, `Display`, `Messaging`, etc.)
- `objective` (`Leads`, `Applications`, `Webinar_Registrations`, `Retargeting`, `OfferHolder_Conversion`)
- `target_cities` (semicolon separated)
- `language` (e.g., `EN`, local language, or combined)
- `flight_start` (YYYY-MM-DD)
- `flight_end` (YYYY-MM-DD)
- `monthly_budget_eur` (number)
- `primary_kpis` (semicolon separated)
- `benchmarks` (short text: CPC/CPL/CTR targets)
- `landing_page_ref` (path or slug)
- `notes`

#### `utm_spec.csv`
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

#### `creative_library.csv`
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

### C) Copy blocks
Cluster-tagged ad copy, landing page copy blocks, webinar blurbs, and messaging/SMS nudges that align with sourced claims and country compliance.

## Workflow
### Step 0 — Read the ticket and scope the deliverables
- Identify markets, clusters, and personas in scope.
- Confirm required formats (markdown vs CSV) and delivery paths.

### Step 1 — Align objectives and guardrails
- Capture ticketed goals (CPL/CPA, application targets, capacity limits).
- Note any excluded channels or budget ceilings.

### Step 2 — Define personas per cluster
- Student, parent, counselor/agent, and diaspora nuances as applicable.
- Map intent stages (prospecting, consideration, retargeting, offer-holder).

### Step 3 — Build campaign architecture per channel
- Campaigns/ad sets by cluster and funnel stage.
- Targeting approach (city, age, interests, lookalikes from consented lists).
- Guardrails (negatives, exclusions, frequency caps conceptually).

### Step 4 — Create creative system and copy library
- Hooks and claims tied to sourced facts.
- Rotation cadence and localization guidance (language, subtitles, format ratios).
- "Do not say" rules for sensitive claims or regulated programs.

### Step 5 — Landing page and funnel requirements
- Required elements for clarity (tuition, recognition links, next steps).
- Lead flow and follow-up expectations (e.g., webinar registration vs direct apply).

### Step 6 — Measurement and reporting spec
- Canonical UTMs and parameter rules (including partner attribution if needed).
- Offline conversion process (offers, deposits, starts) with consent assumptions.
- Weekly dashboard fields and alert thresholds.

### Step 7 — Compliance review checklist
- Verify all claims and sources.
- Ensure tracking/remarketing respects consent rules.
- Add country-specific compliance checks from the relevant country skill.

## KPI guardrails (calibrate per country)
These are starting points; adjust to historical performance and country norms.

- Search: CTR 5–8% non-brand; LP conversion 8–12%.
- Meta: CTR ~1.0–1.5%; lead rate 6–9%.
- TikTok: CTR around 1%; lead rate 6–8% (creative-dependent).
- Video/YouTube: treat as awareness/retargeting feeder; define CPV and view-through targets per market.

Action thresholds: pause or rework any ad set that is ≥25% above CPL target after the minimum spend threshold defined in the ticket; rotate creatives that underperform CTR benchmarks after sufficient impressions.

## Definition of Done (DoD)
- Executable channel plan(s) with country addenda linked where applicable.
- CSV schemas or files produced per ticket.
- Measurement spec (UTMs + dashboard fields) delivered.
- Compliance checklist completed, including country-specific items.
- All outputs stay within the ticket’s allowed write paths.
