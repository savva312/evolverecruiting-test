---
name: greece-recognition-and-licensure
description: Track credential recognition, professional licensure, and regulatory considerations for Greek students considering UNIC or UNIC Athens.
metadata:
  owner: evobuilder
  version: "0.1"
  scope: greece
---

# Greece recognition and licensure

## How to use this skill
- Start with the global procedure in [`/skills/recognition-and-licensure/SKILL.md`](/skills/recognition-and-licensure/SKILL.md) for workflow, compliance cautions, and dataset schema.
- Use this file as the **Greece addendum** to list local authorities, regulated-profession pathways, and documentation wrinkles.
- House public-facing summaries in `countries/greece/market/recognition-and-licensure.md` and keep regulator profiles under `countries/greece/entities/government-regulators/profiles/`.

## Country notes — Greece regulators and pathways
- **Academic recognition**: DOATAP (Hellenic NARIC) evaluates foreign higher-education degrees. Confirm scope for UNIC vs UNIC Athens programmes and link to DOATAP guidance and application forms.
- **Professional licensure** (examples):
  - Ministry of Health and relevant professional chambers for medicine, dentistry, nursing, and pharmacy.
  - Technical Chamber of Greece (TEE) for engineering practice recognition.
  - Ministry of Education, Religious Affairs and Sports for teaching-related recognition.
- **Documentation norms**: flag translation/notarization/apostille expectations only when sourced; avoid stating timelines or fees without official confirmation.
- **Campus clarity**: specify when processes differ between studying at UNIC (Cyprus) vs UNIC Athens and remind readers to cite primary Greek authority links.

## Deliverables to keep updated
- Greece recognition overview aligned to the global structure, separating academic vs professional recognition and citing DOATAP or professional bodies.
- Authority profiles that follow the global template and sit in `countries/greece/entities/government-regulators/profiles/` with `last_verified` dates.
- Structured data for regulators using the global `regulatory_entities.csv` schema when tickets request datasets.

## Quality and compliance reminders
- No legal advice or promises of equivalence; authorities make final decisions.
- Cite primary Greek sources for every substantive claim and record verification dates.
- Keep regulated-profession examples Greece-specific while deferring to the global skill for overall workflow.
