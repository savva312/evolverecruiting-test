---
name: bulgaria-competitive-landscape-by-program-cluster
description: Map Bulgarian outbound-study competitors by program cluster (e.g., Medicine, CS/Data/AI, Business, Psychology, Design) using official tuition/admissions sources, and produce cluster-specific competitor datasets and narrative benchmarks. Use to maintain evidence-backed positioning for UNIC Nicosia and UNIC Athens.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: bulgaria
license: Proprietary (UNIC Evolve internal)
---

# Bulgaria competitive landscape by program cluster (skill)

This file now defers to the global workflow in [`skills/program-clusters-and-competitor-sets/SKILL.md`](/skills/program-clusters-and-competitor-sets/SKILL.md) for methods, templates, and quality checks. Use the global skill for the process; keep Bulgaria-specific cluster coverage and storage paths in the addendum below.

## Purpose
This skill builds a competitor benchmark system that is:
- **clustered** (because Bulgaria’s competitive set differs by program)
- **source-backed** (official tuition/admissions pages)
- **maintainable** (CSV + a concise cluster narrative)

## When to use
Use when tickets ask for:
- defining the right program clusters for Bulgaria recruiting
- competitor lists for each cluster (EU + regional)
- tuition and admissions benchmarking
- constraints like numerus fixus / capacity / exams (where relevant)

## Hard constraints
1) Follow ticket boundaries.
2) Use **official sources** for:
   - tuition
   - admissions requirements
   - deadlines/intakes
3) Keep it Bulgaria-relevant:
   - include competitors Bulgarian families actually pick (evidence via fairs/agents/market context if available)

## Outputs
### A) Cluster narrative (Markdown)
For each cluster:
- why this cluster exists (Bulgaria demand logic)
- typical destinations and decision drivers
- the short competitor set that matters most
- what UNIC Athens / UNIC Nicosia competes on for Bulgaria

### B) Competitor dataset (CSV) per cluster
Recommended schema:
- `cluster`
- `institution`
- `country`
- `city`
- `program_name`
- `degree_level` (`UG`, `PG`, `MD`, etc.)
- `language_of_instruction`
- `duration_years`
- `tuition_per_year_eur` (or `tuition_total_eur` if that’s how it’s published)
- `fees_notes` (admin/insurance if known and sourced)
- `intakes`
- `selection_mechanism` (exam/interview/file/etc.)
- `capacity_or_constraints` (e.g., fixus/caps; only if sourced)
- `source_url`
- `last_verified`

## Step-by-step workflow
1) Confirm which clusters the ticket covers.
2) Build “candidate competitor list” from:
   - Bulgarian agent/fair context (what families see)
   - Bulgaria outbound patterns (where available in-repo)
   - known regional competitor schools
3) For each competitor:
   - find official tuition + admissions pages
   - extract only what you can source
4) Populate the CSV and write the cluster narrative:
   - show the “top set” first (the 10–20 that actually matter)
5) Add maintenance notes:
   - which data changes yearly
   - what to re-check each cycle

## Quality bar
- Sources are clean and official
- The dataset is filterable and comparable
- The narrative makes clear *why* these competitors matter for Bulgaria

---

## Bulgaria addendum: cluster coverage and file paths

- medicine-and-health — `countries/bulgaria/program-clusters/medicine-md/competitors.md`
- computing-data-ai — `countries/bulgaria/program-clusters/cs-data-ai-cyber/competitors.md`
- business-economics-finance — `countries/bulgaria/program-clusters/business-finance-accounting-marketing/competitors.md`
- psychology-and-social-sciences — `countries/bulgaria/program-clusters/psychology-counselling-behavioral/competitors.md`
- law-and-governance — `countries/bulgaria/program-clusters/law-governance-international/competitors.md`
- design-and-creative — `countries/bulgaria/program-clusters/design-creative-media/competitors.md`
- other-strategic-programs — add only when Bulgaria-specific demand + competitor set is documented; place under `countries/bulgaria/program-clusters/<cluster>/competitors.md`
