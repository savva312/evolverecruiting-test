# Template: High-school deep profile (EvoResearcher ticket prompt)

## Customize these fields
- `<SCHOOL_NAME_OFFICIAL>`:
- `<SCHOOL_COMMON_NAME>`:
- `<CITY>` / `<REGION>` / `<COUNTRY>`:
- `<WEBSITE>` (if known):
- `<PROFILE_DIR>` (repo folder, e.g., `countries/<country>/entities/schools/profiles/<city>/<school-id>/`):
- `<PROFILE_README_PATH>` (usually `<PROFILE_DIR>/README.md`):
- `<RESEARCH_REPORT_PATH>` (recommended, e.g., `<PROFILE_DIR>/research/<slug>-report.md`):
- `<AS_OF_DATE_YYYY_MM_DD>`:
- `<ANY_TICKET_CONSTRAINTS>` (e.g., “do not edit CSVs/index pages”):

## Suggested ticket metadata (edit in the ticket header, not here)
- `Research rounds`: 7
- `Research sections`: 7
- `Research output path`: `<PROFILE_DIR>`

---

## Paste into the ticket under `## Research prompt (EvoResearcher)`

You are **EvoResearcher**. Produce a **deep, comprehensive high-school profile** to support UNIC + UNIC Athens recruiting.

### Write boundary (must respect)
- Only write to files explicitly allowed by this ticket.
- `<ANY_TICKET_CONSTRAINTS>`

### Deliverables (write directly to the repo)
1. Create a **long-form research report** at: `<RESEARCH_REPORT_PATH>`.
   - This can be overly long and detailed. Capture all useful findings, citations, and extracted data snippets.
2
### Evidence and citation rules
- Prefer **official/primary sources** (school website and official documents, exam boards, accreditation bodies, regulators, reputable media as secondary).
- Every non-trivial claim should be source-backed with **URL + access date**.
- Do **not** fabricate facts (especially: tuition, outcomes, enrollment, contact names).
- If sources disagree, state the conflict and explain which source you trust and why.

### Privacy and safety
- Do not include secrets/tokens.
- Avoid personal data. Use only **publicly listed organizational** contact details (e.g., main phone, admissions office email). Do not include personal emails/phones or private WhatsApp numbers.

### Required profile content (minimum)
Fill the template sections with evidence-based content, focusing on what matters for recruiting.

1) **Identity and verification**
- Official name(s) and local-language name
- Location(s): address, city/region, map link if available
- Governance/operator (if published)
- Grades served, student mix (co-ed / single-sex), day/boarding
- Official website and official social channels

2) **Curriculum and pathways**
- National curriculum specifics (upper-secondary track names, exam structure)
- International pathways (IB DP/MYP, Cambridge, Pearson, AP, dual diploma, etc.)
- Accreditation/authorizations (include IDs where applicable, e.g., IB school code)
- Languages of instruction by pathway

3) **Student profile and cohorts (as available)**
- Approximate total enrollment and upper-secondary cohort sizes
- Selectivity/admissions approach (exam-based, interviews, rolling)
- Scholarships/financial aid positioning (published only)

4) **Academic calendar and outreach windows**
- Term structure and key dates (start/end, holidays if published)
- Major exam windows relevant to cohorts (national exams, IB, A-Level, AP)
- “Best outreach months” with rationale (avoid exams; align to school events)

5) **Fees and affordability**
- Tuition and fee schedule(s) by grade/pathway (published only, with currency and year)
- Scholarships/discounts, payment plans, admission/application fees
- If not published: provide evidence-based affordability signals (pricing positioning vs peers) and a verification plan

6) **University counseling / placement**
- Structure of counseling/placement function (names only if publicly listed; otherwise roles)
- Any published destinations/outcomes, competitions, scholarships, alumni stories (cite)
- If outcomes aren’t public: document what was searched and propose verification steps (request a counselor pack, destinations list, etc.)

7) **Recruitment relevance for UNIC / UNIC Athens**
- Fit indicators (program clusters, language readiness, exam pathways)
- Top 5 opportunities (actionable)
- Top 5 risks/constraints (actionable)
- 3–5 recommended next actions for UNIC outreach (owner placeholders + due-by dates)

### Output quality bar
- The research report can be as long as needed.
- The profile should be internally usable without additional rewriting.
- Keep tables consistent, date formats stable (`YYYY-MM-DD`), and include a “Last verified” / “Last updated” date set to `<AS_OF_DATE_YYYY_MM_DD>`.
