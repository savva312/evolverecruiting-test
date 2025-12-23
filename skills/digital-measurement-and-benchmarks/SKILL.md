---
name: digital-measurement-and-benchmarks
description: Global measurement framework covering KPIs, UTM governance, tracking requirements, diagnostics, and reporting cadences for paid media and digital channels.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: global
license: Proprietary (UNIC Evolve internal)
---

# Digital measurement & benchmarks (global skill)

## Purpose
Provide a **country-agnostic measurement spine** for paid media and digital channels so every market can operate with consistent guardrails, troubleshooting steps, and reporting rhythms. Country nuances (calendars, local compliance) stay inside `/countries/<country>/` addenda.

## When to use
- A ticket requests KPIs, tracking specs, or benchmarks for digital channels.
- Campaigns need UTM governance or logging rules that multiple countries must follow.
- Performance issues require a global diagnostic playbook before market-specific adjustments.

## Principles
1) **Evidence over assumptions.** Use sourced program facts and historical data when setting targets; flag assumptions.
2) **Separation of global vs. country.** This file defines the baseline; country-specific overrides live under `/countries/<country>/` (note: country paths now sit under `/countries/**`, not legacy layouts).
3) **Privacy-first.** Assume GDPR-level consent; avoid non-compliant tracking and redact PII from repo artifacts.
4) **Traceability.** Every KPI, UTM parameter, and event mapping must be tied to a logging location that other teams can audit.

## Inputs
- Ticket objectives (CPL/CPA, intake targets, priority clusters/personas).
- Paid media/channel architecture (see `skills/paid-media-and-channel-playbooks/SKILL.md` for channel context).
- Country compliance notes and intake calendars (per-country skills and `/executions/` notes scoped by country).
- Existing analytics stack details (GA4/Looker/Meta/Google Ads/CRM).

## Outputs
- KPI framework with guardrails and action thresholds.
- UTM governance with required parameters and patterns.
- Tracking requirements (events, pixels, QA checks).
- Diagnostics playbook for underperformance.
- Reporting cadence with logging locations (global + country).

---

## KPI framework and guardrails
Use these as **starting points**; calibrate with country history and program economics.

### Funnel KPIs (directional ranges)
- **Awareness**: CPM and CPV benchmarks by video platform; target 50–70% VTR on :06s YouTube bumpers.
- **Traffic/Consideration**: CTR guardrails (Search 5–8% non-brand; Meta/TikTok/Display 0.8–1.5%). Landing page CVR 8–12% (lead gen) or 3–5% (apply start).
- **Lead generation**: CPL targets derived from application CPA goals (e.g., CPL ≤ 30% of target CPA). Lead-to-application rate 12–20% for qualified leads.
- **Application-to-offer/offer-to-enrol**: set per program cluster; document current baselines if available.

### Action thresholds
- If CPL is ≥25% above target after minimum spend (defined in ticket or default €150 per ad set), **pause/adjust**.
- Rotate creative if CTR is 20% below guardrail with ≥1,000 impressions.
- Escalate tracking QA if CVR drops >30% week-over-week without budget/mix changes.
- For offline events (offers, deposits), trigger reconciliation if CRM vs. platform conversions differ by >10%.

### Benchmark logging
- Capture market-level deltas in `/executions/<execution_id>/` or ticket-specific notes.
- Country benchmark snapshots should be stored in `/countries/<country>/reports/` (path updated to the `/countries/**` layout) with date, channel, cluster, and source.

---

## UTM governance
Apply consistent UTM patterns across all channels; enforce lowercase, hyphenated slugs.

Required parameters:
- `utm_source`: platform (`google`, `meta`, `tiktok`, `youtube`, `display`, `email`, `sms`, `partner`).
- `utm_medium`: `paid`, `organic`, `remarketing`, or `partner`.
- `utm_campaign`: `{country}-{cluster}-{funnel}-{yyyy}{mm}` (e.g., `ng-medicine-prospecting-202502`).
- `utm_content`: `{persona}-{creativehook}-{adformat}` (keep <50 chars).
- `utm_term`: search keywords or targeting cue; use `na` if not applicable.
- **Partner tagging:** append `partner=<slug>` as a query param for co-marketing; mirror in CRM fields.

Governance rules:
- Maintain an **examples table** in `utm_spec.csv` when produced by tickets.
- Do not reuse campaign slugs across intakes; update the `yyyy{mm}` suffix.
- Capture UTMs in form handlers and ensure CRM mapping matches analytics fields.
- Reject launches if any required UTM is missing or malformed.

---

## Tracking requirements
1) **Analytics + pixels**
   - GA4 baseline with cross-domain where applicable; enable enhanced measurement only if compliant.
   - Platform pixels (Meta/TikTok/Google Ads) deployed via GTM with server-side enabled when available.
   - Unique conversion events per intent stage: `lead_submit`, `apply_start`, `application_submit`, `offer_accepted`, `deposit_paid`.
2) **Event hygiene**
   - Standardize event parameters: `country`, `cluster`, `persona`, `campaign_slug`, `landing_page`, `partner`.
   - Fire events once per action; dedupe via GTM or server-side tagging.
   - Record consent status and storage duration when applicable.
3) **Data quality checks (weekly)**
   - Compare platform vs. GA4 session counts (expect ±10–15% variance).
   - Verify form UTM capture rate ≥95% for paid traffic.
   - Check CRM intake for event timestamps and country mapping; fix any nulls.
4) **Offline/CRM reconciliation**
   - Export weekly offer/accept/deposit counts and match to `campaign_slug`.
   - Log reconciliation gaps and root causes in ticket notes; escalate if >10% mismatch persists 2 weeks.

---

## Diagnostics playbook (underperformance)
Follow this order to minimize false fixes.

1) **Tracking sanity**
   - Verify UTMs present; check conversion fire rate vs. expected.
   - Confirm correct landing page variant per ad set.
2) **Traffic quality**
   - CTR vs. guardrails; check search query reports/placements.
   - Audience overlap and frequency (Meta/TikTok); cap if frequency >3/week on remarketing.
3) **Offer/LP alignment**
   - Message matches program facts; tuition/recognition visible; form friction minimized.
   - Page speed/core vitals within acceptable range (LCP <3s).
4) **Bidding/budget**
   - Budget sufficiency for learning phase; raise if below platform minimums.
   - Bid strategy fit (e.g., tCPA only after 50+ conversions in 30 days).
5) **Creative**
   - Rotate in new hooks if CTR under guardrail; localize where allowed.
6) **External factors**
   - Seasonality/intake windows; check with country calendars.

Escalation: if no improvement after 2 iterations, request country-specific diagnostics and document assumptions.

---

## Reporting cadence and logging
- **Weekly performance review:** channel KPIs vs. targets; highlight variances, next actions. Store outputs in ticket path or `/executions/<execution_id>/`.
- **Monthly benchmark refresh:** update CPM/CPC/CPL ranges by channel and cluster; publish to `/countries/<country>/reports/` for market snapshots and summarize globally in `reports/` if requested.
- **Quarterly audit:** UTM compliance rate, event coverage, pixel health, and dashboard accuracy.

### Dashboards (specify fields)
At minimum, capture:
- Spend, impressions, clicks, sessions (UTM-scoped), leads, applications, offers, deposits/starts.
- Derived metrics: CPM, CPC, CTR, CVR (session→lead, lead→app), CPA (app/offer/deposit), ROI proxy if available.
- Slicers: country, cluster, persona, funnel stage, partner, campaign slug, landing page.

### Alerting
- Set alerts for: sudden CVR drop >30%, cost spikes >20% day-over-day, UTM missingness >5%, pixel firing errors.
- Document alerts and responses in run notes for traceability.

---

## How this connects to other skills
- **Channel context:** Use architectures and creative guidance from `skills/paid-media-and-channel-playbooks/SKILL.md`.
- **Data schemas:** Align CSV outputs with `skills/data-model-csvs-and-profiles/` if tickets request data exports.
- **Country addenda:** Add country-specific benchmarks, compliance, and localized diagnostics under each `/countries/<country>/skills/` subtree without modifying this global baseline.

## Definition of Done
- KPI targets, UTMs, tracking requirements, diagnostics, and reporting cadences are documented in this file.
- Guidance is global and references channel skill(s); no country-specific edits here.
- Logging/reporting instructions point to the `/countries/<country>/` layout and ticket/run-note paths.
