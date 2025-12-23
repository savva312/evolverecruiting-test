---
name: serbia-recognition-and-licensure
description: Build Serbia-specific regulatory reference docs and entity profiles covering academic recognition (e.g., ENIC-NARIC Serbia), credential handling, and regulated-profession pathways (esp. Medicine). Use to produce parent/counselor-ready, citation-backed guidance and to keep recognition claims accurate. Aligns with the global recognition-and-licensure skill.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: serbia
license: Proprietary (UNIC Evolve internal)
---

# Serbia recognition and licensure (skill)

## How to use this skill
- Follow the global procedure in [`/skills/recognition-and-licensure/SKILL.md`](/skills/recognition-and-licensure/SKILL.md) for workflow, compliance cautions, and dataset schema.
- Use this file as the **Serbia addendum** to capture local authorities, regulated-profession pathways, and documentation nuances.
- Keep public-facing overviews in `countries/serbia/market/recognition-and-licensure.md` and authority profiles under `countries/serbia/entities/government-regulators/profiles/` using the global template.

## Purpose
This skill ensures the repo has **Serbia-correct** and **source-backed** guidance on:
- academic recognition of foreign higher-education qualifications in Serbia
- credential/document requirements (what is typically needed, how to verify)
- regulated-profession considerations, especially Medicine pathways
- the list of Serbian authorities/entities to reference

## When to use
Use when tickets ask for:
- ENIC-NARIC Serbia process summaries and checklists
- Serbia recognition FAQs for families/counselors
- professional recognition / licensure steps (Medicine-focused)
- identifying Serbian ministries, councils, associations involved

## Hard constraints
1) Follow ticket boundaries (allowed write paths) and the global compliance rules.
2) Treat this as **compliance-sensitive**:
   - do not give legal advice
   - do not invent processing times, fees, or requirements
   - always link primary sources with `last_verified` dates
3) Separate:
   - **academic recognition** vs **professional/licensure recognition**
4) Note differences by campus (UNIC vs UNIC Athens) or applicant type only when sourced.

## Outputs
- Serbia recognition overview (parent/counselor readable) aligned to the global structure.
- Medicine pathway note (Serbia-specific steps + authoritative links).
- Entity profiles for key authorities (who they are, what they do, contact links) following the global template.

If the ticket requests structured data:
- `regulatory_entities.csv` using the global schema (names, roles, URLs, contacts, last_verified).

## Recommended structure for a “recognition overview” markdown doc (Serbia addendum)
- What recognition is (in Serbia terms)
- Academic recognition: who handles it, what applicants typically submit, where to apply
- Typical timeline statements **only if sourced**
- Common pitfalls (translations, missing documents, mismatched names)
- How UNIC families should prepare documents (without promising outcomes)
- Sources and last verified

## Step-by-step workflow (Serbia)
1) Identify the competent Serbian authority(ies) and confirm scope (academic vs professional).
2) Collect and read primary sources.
3) Draft a parent-ready summary with:
   - plain language
   - explicit “always confirm with authority” disclaimer
   - direct links
4) Draft internal notes for admissions staff:
   - what questions recur
   - what documents to request early (e.g., certified translations, apostille when required)
5) Update any structured lists/datasets if required using the global schema.

## Quality bar
- Every key claim links to a primary authority page
- No “hand-wavy” claims about automatic outcomes
- Clear separation between academic vs professional recognition

## Serbia authority examples (country addendum)
- **ENIC-NARIC Serbia (Ministry of Education)** — academic recognition/evaluation; maintain profile with scope and links.
- **Commission for Accreditation and Quality Assurance (CAQA)** — higher-ed quality assurance context; reference where relevant.
- **Serbian Medical Chamber / Ministry of Health** and other professional chambers (dental, pharmacy, nursing) — professional recognition and licensing; include sourced steps and contacts.
- **Chamber of Engineers of Serbia** — engineering practice recognition; document only sourced requirements.
