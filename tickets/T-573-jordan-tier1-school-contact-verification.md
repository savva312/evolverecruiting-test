# T-573: Jordan — Tier 1 school contact + visit policy verification sprint (4 schools)

Status: open
Type: data
Priority: P1
Dependencies: (none)
Claimed-by:
Claimed-at:
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Reduce school-outreach friction by verifying counselor contacts and visit policies for 4 Tier 1 Jordan schools (high-impact targets) and syncing the findings into both:
- the school profile README(s)
- `countries/jordan/data/entities/schools.csv`

Target schools (already in the Tier 1 index):
- American Community School Amman (ACS)
- Amman Baccalaureate School (ABS)
- International Academy – Amman (IAA)
- New English School (NES)

---

## Context

These Tier 1 profiles contain “contact pending” gaps that prevent scaling outreach:
- `countries/jordan/entities/schools/README.md`
- `countries/jordan/entities/schools/profiles/amman/american-community-school-amman/README.md`
- `countries/jordan/entities/schools/profiles/amman/amman-baccalaureate-school/README.md`
- `countries/jordan/entities/schools/profiles/amman/international-academy-amman-iaa/README.md`
- `countries/jordan/entities/schools/profiles/amman/new-english-school-nes/README.md`
- Dataset: `countries/jordan/data/entities/schools.csv`

---

## Allowed write paths

- `tickets/T-467-jordan-tier1-school-contact-verification.md`
- `countries/jordan/entities/schools/profiles/amman/american-community-school-amman/README.md`
- `countries/jordan/entities/schools/profiles/amman/amman-baccalaureate-school/README.md`
- `countries/jordan/entities/schools/profiles/amman/international-academy-amman-iaa/README.md`
- `countries/jordan/entities/schools/profiles/amman/new-english-school-nes/README.md`
- `countries/jordan/data/entities/schools.csv`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**` (global)
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- `countries/**` (except `countries/jordan/**`)

---

## Required outputs

- Each of the 4 school profile READMEs updated with:
  - at least one verified counselor/university-guidance contact channel (email/phone/form URL) and how to request visits
  - updated `Last updated` / `Last verified` dates and sources
- `countries/jordan/data/entities/schools.csv` updated for the 4 rows:
  - `contact_email` / `counselor_email` / `contact_phone` (as available), `visit_window_notes`, `sources`, `last_verified`

---

## Acceptance criteria

- [ ] No contact info is invented; every new contact channel has a source URL and verification date.
- [ ] CSV remains valid (consistent columns) and updated rows match the corresponding profiles.
- [ ] Visit policy guidance is specific (who to email, what to include) and reflects each school’s published process where available.

