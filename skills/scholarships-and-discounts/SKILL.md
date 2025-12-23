---
name: scholarships-and-discounts
description: Global procedure to inventory, qualify, and publish scholarships, discounts, and financial incentives for UNIC and UNIC Athens candidates.
compatibility: Applies to all countries; pair with country addenda under `/countries/<country>/skills/` for local schemes.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: global
license: Proprietary (UNIC Evolve internal)
---

# Scholarships and discounts (global skill)

## Purpose
Standardize how we capture, validate, and communicate scholarships, discounts, and other price/aid incentives so that every country team can plug in local offers without changing the core workflow or schema.

## When to use
- Tickets requesting scholarship/discount scans, refreshes, or playbooks.
- Building CSV/markdown inventories for offers tied to UNIC or UNIC Athens.
- Preparing counselor/parent-ready explanations of eligibility, value, deadlines, and documentation expectations.

## Compliance and scope guardrails
1) Do not promise eligibility, award amounts, or approval odds. Emphasize that offers are contingent on official criteria and funding availability.
2) Avoid unsourced numbers. If a range or cap is not published, mark the field as `unknown` and add a verification note.
3) Distinguish clearly between **merit/need awards**, **early-bird/loyalty discounts**, and **third-party funding**; keep stacking rules explicit.
4) Flag currency and campus applicability (UNIC vs UNIC Athens) for every entry.
5) Keep personal data out of skill artifacts; PII handling belongs in admissions systems, not in repo files.

## Required outputs
- **Global skill file (this document)**: workflow + schema + guardrails.
- **Country addenda (when requested by ticket)**: stored under `/countries/<country>/skills/` with local funding schemes; they must reference this global schema.
- **Structured data (when requested)**: CSV/markdown inventories aligned to the schema below and scoped to ticket paths (e.g., country directories).

## Dataset schema (scholarships_and_discounts.csv)
Use the following columns; expand only if a ticket requests additional fields. Keep boolean columns as `yes/no` and dates as ISO (`YYYY-MM-DD`).
- `program_name` — official scholarship/discount name; include cohort/year if applicable.
- `issuing_body` — UNIC, UNIC Athens, faculty, donor, government, or partner.
- `campus_applicability` — nicosia | athens | both; note if delivery mode matters (on-campus vs online).
- `target_audience` — undergrad/grad; international/domestic; specific nationalities; transfer; alumni/dependents.
- `eligibility_criteria` — succinct bullets (GPA thresholds, income proof, exam scores, program restrictions); cite sources.
- `award_type` — merit | need-based | athletic | early-bird | loyalty/alumni | partner | government/third-party.
- `value_structure` — fixed-amount | percentage | sliding | stipend; include currency/percent and whether renewable.
- `coverage` — tuition | fees | accommodation | living | travel; note exclusions.
- `stacking_rules` — can/cannot combine with other offers; priority rules if multiple apply.
- `number_of_awards` — published volume or `not-published`; avoid speculation.
- `duration_and_renewal` — length of award and renewal criteria; note GPA/credits checks.
- `application_channel` — automatic consideration | separate form | partner nomination | external portal.
- `deadline_type` — rolling | fixed date(s) | stage-based (early/regular/late); list ISO dates if published.
- `required_documents` — transcripts, financial docs, recommendation letters, essays; mark if translations/notarization needed.
- `decision_timing_notes` — any published windows; avoid guarantees.
- `messaging_notes` — key phrases to use/avoid, campus positioning, sensitivity flags.
- `source_links` — authoritative URLs; include PDF/announcement links with `last_verified`.
- `last_verified` — ISO date of the latest source check.
- `contact_point` — admissions contact or official mailbox when published; otherwise `n/a`.

## Markdown template (for narrative entries)
Use when a ticket requests markdown profiles instead of CSV rows.

```
### <Program name> (campus: Nicosia | Athens | Both)
- Issuing body: <unit/donor/government>
- Target audience: <levels + nationality/partner flags>
- Award type: <merit/need/etc.>
- Value and coverage: <amount/percent, what it covers, renewal rules>
- Eligibility highlights: <concise bullets>
- Application channel + deadlines: <automatic vs separate; key dates>
- Required documents: <bulleted list; note translations/notarization if applicable>
- Stacking and exclusions: <combine rules; non-eligible programs>
- Messaging notes: <phrases to use/avoid; sensitivity flags>
- Source links + last verified: <URLs | YYYY-MM-DD>
```

## Step-by-step workflow
1) **Clarify scope**: campus (Nicosia vs Athens), program clusters, and whether third-party funding is in scope.
2) **Inventory official sources**: university scholarships page(s), faculty/program pages, admissions FAQs, donor announcements, and government/partner portals.
3) **Extract structured facts**: eligibility, value structure, coverage, deadlines, documents, stacking rules, campus applicability. Capture only published details; mark `unknown` where not disclosed.
4) **Classify the offer**: assign `award_type`, `campus_applicability`, and `target_audience` to enable filtering and reuse.
5) **Document compliance notes**: highlight sensitive claims (e.g., limited funding, competitive selection, citizenship restrictions) and required disclaimers.
6) **Populate dataset/template**: fill the CSV or markdown template; ensure `source_links` and `last_verified` are present for every entry.
7) **QA**: validate URLs, check date formats, ensure currency units are explicit, and confirm stacking rules are captured.
8) **Handoff**: provide short messaging bullets for counselors/marketing and note any open questions to resolve with Admissions/Finance.

## Sourcing checklist (use for each entry)
- [ ] Primary source link captured (official UNIC/UNIC Athens page or issuing body).
- [ ] Eligibility criteria copied verbatim or paraphrased with no invented numbers.
- [ ] Value structure and coverage clarified; currency/percent units explicit.
- [ ] Deadline(s) confirmed or marked `rolling`/`not published`.
- [ ] Required documents listed; translation/notarization flags noted.
- [ ] Stacking rules and exclusions recorded.
- [ ] Campus applicability and program restrictions specified.
- [ ] `last_verified` date added for every source.

## Messaging and compliance guardrails
- Lead with **conditions and availability**: “subject to published criteria and available funding”; avoid guarantees.
- Avoid promising amounts when a range is given; state the range and cite the source.
- Use campus-specific positioning: call out when Athens pricing/eligibility differs from Nicosia.
- Keep statements channel-safe (parents, counselors, digital ads). No claims of “automatic approval” or “guaranteed discounts.”
- If an offer requires third-party approval (government/embassy/partner), state dependencies clearly.
- For currency conversions, show the official published value; conversions belong in separate calculators, not the dataset.

## Country addenda pattern
- Store addenda under `/countries/<country>/skills/` with a short “Country notes” section that lists local funding schemes and regulatory constraints.
- Do not duplicate the global workflow; only document local funding programs, citizenship restrictions, and documentation wrinkles.
- Cross-link any country datasets to the global schema so columns remain consistent.

## Quality bar
- Every entry includes `source_links` and `last_verified`.
- Eligibility, value, coverage, and stacking rules are present or explicitly marked `unknown/not published`.
- Campus applicability (Nicosia vs Athens) is stated for each offer.
- Messaging notes avoid overpromising and flag compliance-sensitive claims.
