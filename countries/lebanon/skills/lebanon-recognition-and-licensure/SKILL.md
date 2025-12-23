---
name: lebanon-recognition-and-licensure
description: Lebanon addendum to the global recognition-and-licensure skill, focused on local authorities, paths, and storage locations.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: lebanon
license: Proprietary (UNIC Evolve internal)
---

# Lebanon recognition and licensure

## How to use this skill
- Start with the global procedure in [`/skills/recognition-and-licensure/SKILL.md`](/skills/recognition-and-licensure/SKILL.md) for workflow, compliance cautions, and dataset schema.
- Use this file as the **Lebanon addendum** to list local authorities, regulated-profession examples, and documentation nuances.
- Keep campus distinctions (UNIC Nicosia vs UNIC Athens) explicit when writing Lebanon-facing summaries.

## Lebanon authorities and focus areas (source-backed only)
- **Academic recognition:** Ministry of Education and Higher Education (Directorate General of Higher Education / Equivalence Committee). Link to official equivalency pages before summarizing process steps.
- **Professional/licensure examples:** Orders and professional bodies such as the Order of Physicians, Order of Pharmacists, Order of Engineers and Architects, or nursing associations. Cite official sites and avoid implying outcomes.
- **Documentation norms:** Note translation/notarization/apostille requirements only when explicitly published by the authority. Do not state timelines or fees without a primary source.

## Where to store Lebanon outputs (if the ticket allows)
- Recognition overview: `countries/lebanon/market/recognition-and-licensure.md`
- Regulator profiles: `countries/lebanon/entities/government-regulators/profiles/<slug>.md`
- Structured data (when requested): `countries/lebanon/data/regulators/regulatory_entities.csv` following the global schema.

## Compliance reminders
- No legal advice or promises of equivalence; authorities make final decisions.
- Separate academic recognition from professional/licensure notes.
- Every claim must link to a primary source with `last_verified` dates; defer unsourced items to a “to verify” list rather than speculating.
