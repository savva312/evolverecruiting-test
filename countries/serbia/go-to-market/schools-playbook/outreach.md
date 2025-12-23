# School outreach playbook (Serbia)
Last updated: 2025-12-20 | Owner: School outreach lead (TBD)

## Targeting priorities (use T-007 profiles)
- **Belgrade (international & language schools)** — first wave; pull counselor names and past notes from `entities/schools/profiles/belgrade/README.md`.
- **Novi Sad bilingual/STEM schools** — second wave; confirm program fit via `entities/schools/profiles/novi-sad/README.md`.
- **Niš language/STEM schools** — third wave; pair with fairs/agent events; see `entities/schools/profiles/nis/README.md`.
- **Other cities (Subotica, Kragujevac, Kraljevo)** — opportunistic; log findings in `entities/schools/profiles/other/README.md`.

## Channel mix & 4-week sequence
- **Week 0 (Day 0-2) — Intro email + Viber ping**  
  - Actions: send dual-campus intro email, attach UNIC/UNIC Athens one-pagers, include 2 proposed visit dates.  
  - Owners: Outreach lead drafts; Design supports assets.
- **Week 0 (Day 3-4) — Phone call follow-up**  
  - Actions: confirm counselor availability, validate student cohorts (IB, A-level, language schools), request permission for student session.  
  - Owners: Outreach lead; note call outcomes in CRM + `/executions/`.
- **Week 1 — Schedule + agent coordination**  
  - Actions: lock visit date/time, align with local agent partner (if assigned) for co-hosting; request room + AV.  
  - Owners: Outreach lead + Agent manager.
- **Week 2 — Student promo**  
  - Actions: send student-facing invite email/poster; share short video (placeholder link) and application timeline; create Viber/WhatsApp broadcast list if counselor agrees.  
  - Owners: Outreach lead; Marketing shares assets.
- **Week 3 — Visit execution**  
  - Actions: run 1-hour session (see visit template), gather opt-ins, capture counselor feedback.  
  - Owners: Visiting rep + Agent (if co-hosting).
- **Week 4 — Post-visit conversion push**  
  - Actions: send recap, application starter kit, book 1:1 virtual slots; invite counselors to quarterly UNIC counselor hour.  
  - Owners: Outreach lead; Admissions rep for virtual 1:1s.

## Messaging angles (tailor per city/school type)
- **Academic outcomes** — EU-recognized degrees; employability stats; internship pipelines in Cyprus/Greece.  
- **Affordability** — outline tuition vs. UK/EU comparables; highlight scholarships/discounts for Serbian students (placeholder link).  
- **Mobility & safety** — 1-hour flight from Belgrade to Larnaca/Athens; campus safety; housing support.  
- **Program fit** — Medicine/MD, CS/AI, Business with English delivery; Athens options for students preferring mainland EU context.  
- **Process clarity** — rolling admissions, document list, English language requirements; emphasize counselor support and fast offer timelines.

## Travel cadence & coverage
- **Belgrade** — weekly half-days; cluster 3–4 schools per trip; prioritize schools with past interest in T-007 profiles.  
- **Novi Sad** — 1x per month; bundle with agent check-ins; aim for Thursday/Friday slots for student attendance.  
- **Nis/coastal** — every 6–8 weeks; stack with fairs; pre-book two school stops per trip.  
- **Virtual** — monthly counselor update call (zoom); invite all regions to reduce travel gaps.

## Tracker & reporting hygiene
- **Live tracker:** `../../data/operations/school-outreach-tracker.csv` holds one row per priority school with stage, last touch, next touch, owner, and notes.
- **Schema + PII guardrails:** `../../data/operations/school-outreach-tracker-dictionary.md`; follow the enum set and keep dates in ISO format.
- **Operating rule:** update the tracker immediately after every outreach touch (email, call, visit, event). Roll the `stage` forward, refresh `last_touch_date`, set the next action and role owner, and document context in `notes` without PII.
- **QA cadence:** Ops support spot-checks the tracker each Monday to ensure no blank `next_touch_date` fields for active schools and archives screenshots to `/executions/` if issues arise.

## Next actions
- Lock top 10 Belgrade/Novi Sad targets from T-007 profiles and secure January/February dates. **Owner:** Outreach lead.  
- Finalize dual-campus one-pagers + short intro video links (placeholders acceptable). **Owner:** Marketing.  
- Keep the tracker above current; Ops support audits weekly and drives clean handoffs before each trip. **Owner:** Ops support.
