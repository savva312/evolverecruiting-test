---
name: recognition-and-licensure
description: Global procedure for documenting academic recognition, credential handling, and regulated-profession licensure pathways for UNIC and UNIC Athens candidates.
compatibility: Applies to all countries; pair with country addenda in each `/country/skills/*` folder.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: global
license: Proprietary (UNIC Evolve internal)
---

# Recognition and licensure (global skill)

## Purpose
Create consistent, compliance-aware guidance for how UNIC and UNIC Athens qualifications are recognized academically and what is required for professional licensure in regulated fields. This skill provides the common structure; countries add local regulators and nuances in their own addenda.

## When to use
- Tickets requesting recognition/licensure research, overviews, or FAQs.
- Building or refreshing regulator/authority profiles for a country.
- Producing parent/counselor-ready explanations of recognition pathways.
- Preparing structured datasets of recognition authorities.

## Compliance and scope guardrails
1) Follow ticket boundaries and country scopes.
2) Treat recognition/licensure as **compliance-sensitive**:
   - Do not provide legal advice or guarantee outcomes.
   - Do not invent processing times, fees, or document lists.
   - Always link primary sources and mark `last_verified` dates.
3) Distinguish clearly between **academic recognition** (credential evaluation) and **professional/licensure recognition** (right to practice regulated professions).
4) Call out when requirements depend on nationality, mode of study, or campus (UNIC vs UNIC Athens).

## Required outputs
- **Recognition overview** (parent/counselor readable) explaining academic vs professional recognition, standard caveats, and where to confirm details.
- **Regulated-profession briefing** (e.g., Medicine, Nursing, Engineering) with authoritative links and caution notes.
- **Authority/competent-body profiles** summarizing who handles what, how to contact them, and source links.
- **Structured data** when requested: `regulatory_entities.csv` captured under the relevant country path using the schema below.

## Dataset schema (regulatory_entities.csv)
Use a lightweight table with these columns (expand only if the ticket requires):
- `name` — authority/competent body name.
- `jurisdiction` — country/region covered.
- `scope` — academic recognition | professional/licensure | both.
- `regulated_fields` — fields covered (e.g., Medicine, Engineering); allow multiple values.
- `primary_role` — evaluation | licensing | oversight | information.
- `official_url` — main authoritative link.
- `contact` — email/phone or contact page URL if published.
- `process_notes` — brief nuance such as translation/apostille expectations (no unsourced claims).
- `last_verified` — ISO date of the most recent source check.

## Authority profile template (markdown)
For each authority profile (kept under the country’s `entities/` tree):
- Name and acronym (if any)
- Jurisdiction and scope (academic recognition vs professional licensing)
- What the authority does (concise)
- Who typically applies and when
- Official links (application portal, guidance)
- Contact options (if published)
- Last verified (date) and source links
- Notes and caveats (translations, notarization, apostille, campus considerations)

## Step-by-step workflow
1) **Confirm scope**: determine whether the ticket is academic recognition, professional licensure, or both.
2) **Map authorities**: list competent bodies by domain (education ministry, NARIC/NAPA equivalent, professional chambers). Validate names from primary sources.
3) **Collect sources**: gather official pages for application steps, eligibility, and documentation.
4) **Draft parent-ready overview**: plain language, no promises; emphasize that authorities make final decisions and link to official guidance.
5) **Prepare internal notes**: recurring questions, document pitfalls (translations, apostille), and what evidence admissions should ask for early.
6) **Update structured data**: append or refresh `regulatory_entities.csv` and profile files with `last_verified` dates.
7) **QA**: verify links resolve, separate academic vs professional requirements, and ensure all compliance cautions are present.

## Country addenda pattern
Country skills should:
- Link back to this global skill for the core workflow and dataset schema.
- Add a **country notes** section that lists local authorities, common documentation wrinkles, and any campus-specific considerations.
- Keep regulated-profession examples scoped to that country (e.g., medicine licensing bodies) without duplicating the global workflow.

## Quality bar
- Every key statement links to a primary authority source.
- Academic vs professional recognition is clearly separated.
- No invented processing times, fees, or promises of equivalence.
- Profiles and datasets carry `last_verified` dates and cite sources.
- Country addenda stay concise and defer to this global standard for structure.
