---
name: bulgaria-recognition-and-licensure
description: Build Bulgaria-specific regulatory reference docs and entity profiles covering academic recognition (e.g., NACID), credential handling, and regulated-profession pathways (esp. Medicine). Use to produce parent/counselor-ready, citation-backed guidance and to keep recognition claims accurate. Aligns with the global recognition-and-licensure skill.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: bulgaria
license: Proprietary (UNIC Evolve internal)
---

# Bulgaria recognition and licensure (skill)

## How to use this skill
- Follow the global procedure in [`/skills/recognition-and-licensure/SKILL.md`](/skills/recognition-and-licensure/SKILL.md) for workflow, compliance cautions, and dataset schema.
- Use this file as the **Bulgaria addendum** to capture local authorities, regulated-profession pathways, and documentation nuances.
- Keep public-facing overviews in `countries/bulgaria/market/recognition-and-licensure.md` and authority profiles under `countries/bulgaria/entities/government-regulators/profiles/` using the global template.

## Purpose
This skill ensures the repo has **Bulgaria-correct** and **source-backed** guidance on:
- academic recognition of foreign higher-education qualifications in Bulgaria
- credential/document requirements (what is typically needed, how to verify)
- regulated-profession considerations, especially Medicine pathways
- the list of Bulgarian authorities/entities to reference

## When to use
Use when tickets ask for:
- NACID process summaries and checklists
- Bulgaria recognition FAQs for families/counselors
- professional recognition / licensure steps (Medicine-focused)
- identifying Bulgarian ministries, councils, associations involved

## Hard constraints
1) Follow ticket boundaries (allowed write paths) and the global compliance rules.
2) Treat this as **compliance-sensitive**:
   - do not give legal advice
   - do not invent processing times, fees, or requirements
   - always link primary sources with `last_verified` dates
3) Separate:
   - **academic recognition** vs **professional/licensure recognition**
4) Call out when processes differ by campus (UNIC vs UNIC Athens) or applicant nationality.

## Outputs
- Bulgaria recognition overview (parent/counselor readable) aligned to the global structure.
- Medicine pathway note (Bulgaria-specific steps + authoritative links).
- Entity profiles for key authorities (who they are, what they do, contact links) following the global template.

If the ticket requests structured data:
- `regulatory_entities.csv` using the global schema (names, roles, URLs, contacts, last_verified).

## Recommended structure for a “recognition overview” markdown doc (Bulgaria addendum)
- What recognition is (in Bulgaria terms)
- Academic recognition: who handles it, what applicants typically submit, where to apply
- Typical timeline statements **only if sourced**
- Common pitfalls (translations, missing documents, mismatched names)
- How UNIC families should prepare documents (without promising outcomes)
- Sources and last verified

## Step-by-step workflow (Bulgaria)
1) Identify the competent Bulgarian authority(ies) and confirm scope (academic vs professional).
2) Collect and read primary sources.
3) Draft a parent-ready summary with:
   - plain language
   - explicit “always confirm with authority” disclaimer
   - direct links
4) Draft internal notes for admissions staff:
   - what questions recur
   - what documents to request early (e.g., certified translations, apostille if required)
5) Update any structured lists/datasets if required using the global schema.

## Quality bar
- Every key claim links to a primary authority page
- No “hand-wavy” claims about automatic outcomes
- Clear separation between academic vs professional recognition

## Bulgaria authority examples (country addendum)
- **NACID (National Center for Information and Documentation)** — academic recognition of foreign higher-education degrees; maintain profile with scope and links.
- **Ministry of Education and Science** — policy oversight; cite when relevant to recognition guidance.
- **Bulgarian Medical Association / Ministry of Health** — professional recognition and right-to-practice steps for medicine; add other chambers for dentistry, pharmacy, and nursing where sourced.
- **Professional chambers (e.g., Bulgarian Engineering Union)** — regulated-profession pathways; include only sourced steps and contacts.
