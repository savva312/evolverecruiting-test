---
name: jordan-unic-portfolio-pricing-and-language
description: Maintain a Jordan-ready, source-backed inventory of UNIC Nicosia and UNIC Athens programs (what’s offered, language of instruction, tuition/fees, intakes, admissions requirements, and Jordan-facing notes). Produces both structured CSVs and per-program markdown profiles for consistent counseling, pricing transparency, and cluster mapping.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: jordan
license: Proprietary (UNIC Evolve internal)
---

# Jordan: UNIC portfolio, pricing, and language (skill)

## Purpose
Jordanian recruiting becomes operationally reliable only if we have a **single, maintained source of truth** for:
- which programs UNIC offers in **Nicosia** vs **Athens**
- language of instruction (English vs Greek; program-by-campus)
- tuition/fees and payment plan facts (as publicly published)
- intakes and admissions requirements (English proof, prerequisites, interviews)
- Jordan-facing notes (recognition links, degree awarding institution, etc.)

This skill creates and maintains that system in **both**:
1) structured data (CSV tables used by other docs/agents)
2) human-readable markdown profiles (used by counselors, scripts, landing pages)

## When to use
Use this skill when a ticket asks for:
- “Inventory all UNIC Athens programs in English + prices”
- “Track UNIC Nicosia vs UNIC Athens by cluster”
- “Create program profiles for Jordan counseling”
- “Build a dataset for tuition, fees, language, intakes, requirements”
- “Validate that repo pricing claims match official pages”
- “Produce Jordan-ready program tables for reports/landing pages”

## Hard constraints (read first)
1) **Follow ticket boundaries.** Before writing, open the active ticket in `/tickets/` and read:
   - Allowed write paths
   - Files to create/update
   Only write inside those paths.

2) **Do not invent pricing or policy.**
   - Tuition, fees, intakes, and scholarship rules must come from official UNIC/UNIC Athens pages or clearly labeled internal sources if the ticket explicitly allows internal references.
   - If you cannot source a number, leave it blank and add a “missing/verify” note.

3) **Separate “published facts” from “recommended Jordan tactics.”**
   This skill is mainly the *facts layer*. If the ticket asks for counseling scripts or recommended merit mapping, keep that in separate docs, and link back to these facts.

4) **Version drift matters.**
   Always include `last_verified` on structured rows and a “Last verified” line in markdown profiles.

## Outputs
Depending on the ticket, produce one or more of the following:

### A) Master structured dataset(s) (CSV)
If the repo already defines schemas, follow them. If not, use these recommended schemas.

#### `unic_programs.csv` (recommended schema)
One row per **program × campus × delivery location × language**.

Columns:
- `program_id` (stable slug, e.g., `athens-md-english`, `nicosia-bsc-compsci-english`)
- `institution_awarding` (e.g., `University of Nicosia`)
- `campus` (`Nicosia`, `Athens`)
- `delivery_location` (city/country; if different from campus, specify)
- `program_name`
- `degree_type` (e.g., `BSc`, `BA`, `BBA`, `MSc`, `MD`, `PhD`)
- `degree_level` (`UG`, `PG`, `Doctorate`, `Professional`)
- `language_of_instruction` (`English`, `Greek`, `Mixed`)
- `duration_years` (numeric if clear)
- `intakes` (semicolon separated, e.g., `Fall;Spring`, or `Autumn`)
- `tuition_basis` (`per_year`, `per_semester`, `per_credit`, `total_program`)
- `tuition_amount_eur` (number only if published)
- `mandatory_fees_notes` (short; only if sourced)
- `payment_plan_notes` (short; only if sourced)
- `admissions_summary` (short, factual)
- `english_requirements` (short; test + minimums if sourced)
- `prerequisites` (short; e.g., “Biology + Chemistry/Physics/Math for MD” if sourced)
- `selection_process` (e.g., `file_review`, `interview`, `exam`)
- `program_cluster_tags` (semicolon separated; uses repo-defined clusters)
- `official_program_url`
- `official_tuition_url` (if separate)
- `source_urls` (semicolon separated)
- `last_verified` (YYYY-MM-DD)
- `notes_jordan` (short: only Jordan-relevant facts like recognition link targets, common doc expectations)

#### Optional: `unic_scholarships_and_discounts.csv`
Only if the ticket requests it and only for published policies.

Columns:
- `policy_id`
- `campus`
- `program_scope` (e.g., `non_medical_ug`, `medicine`, `all_programs`, or list)
- `policy_name`
- `discount_type` (`merit_percent`, `fixed_amount`, `early_payment_discount`, `fee_credit`)
- `value_range` (e.g., `10%–40%` or `€3000`)
- `stacking_rules` (if published)
- `renewal_rules` (if published)
- `official_policy_url`
- `last_verified`
- `notes`

### B) Program profiles (Markdown)
One file per program (or per program×campus if needed by ticket).
Minimum sections:
- Snapshot (campus, degree, language, duration)
- Tuition & fees (with sources)
- Intakes & key dates (if published)
- Admissions requirements (English, prerequisites, selection steps)
- Jordan-facing notes (recognition links to use; typical parent questions)
- Sources + Last verified

## Step-by-step workflow
### Step 0 — Read ticket and confirm allowed write paths
- Open the ticket.
- Copy “Allowed write paths” into your working notes.
- Identify the required outputs (CSV, markdown profiles, or both).

### Step 1 — Establish the authoritative source set
For each program and campus:
- Find the **official program page**
- Find the **official tuition/fees page** (if separate)
- Find the **official admissions requirements** page (if separate)
- For Medicine or regulated programs, find any official faculty/school policy page(s)

Record the URLs before extracting any numbers.

### Step 2 — Normalize program identity
Create stable slugs:
- Use consistent naming for campus: `athens-...` vs `nicosia-...`
- Include language when it differs materially: `...-english`, `...-greek`
- Avoid changing `program_id` once created unless the ticket explicitly requests a migration.

### Step 3 — Extract facts into CSV first
Populate `unic_programs.csv` row-by-row.
Rules:
- Use EUR only if the source uses EUR; otherwise convert only if the ticket explicitly requests conversion.
- If tuition is “per credit”, set `tuition_basis=per_credit` and store the per-credit amount in `tuition_amount_eur`.
- If you cannot find mandatory fees, do not guess; leave blank and add a note.

### Step 4 — Write/refresh markdown profiles
For each program profile:
- Keep it short and scannable
- Include explicit links to the official sources
- Add a “Jordan-ready counseling note” section that is strictly factual:
  - awarding institution name
  - language of instruction
  - what’s required for application (docs/tests)
  - where to point families for recognition (links only; no legal promises)

### Step 5 — Cross-check for internal consistency
- Every markdown number must be in the CSV and sourced.
- Every CSV row must have at least one official URL and `last_verified`.
- Cluster tags must match the repo’s cluster taxonomy.

## Quality bar
- The portfolio inventory is accurate, deduped, and maintainable.
- Facts are cleanly separated from strategy/tactics.
- A downstream agent can build Jordan landing pages or scripts without re-researching tuition/program facts.

## Common pitfalls
- Mixing “campus” and “awarding institution” (be explicit: awarding institution is UNIC)
- Copying numbers from third-party aggregators (avoid)
- Writing “net price” claims without a published scholarship policy source
- Treating Greek-only programs as English (track language precisely)
- Forgetting `last_verified` (this repo will drift over time)

## Suggested program cluster tagging (do not invent new tags)
Use the repo’s defined cluster taxonomy. If the ticket requires changes to clusters, do that work in the cluster ticket first, then re-tag programs here.
