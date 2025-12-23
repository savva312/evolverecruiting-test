# T-530: Nigeria — Expand regulator/exam-body profiles + CSV

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

Expand Nigeria’s regulator coverage so enrollment has authoritative references for credential handling, legalization, exams, and licensure bodies.

---

## Context

- Current regulator coverage is thin:
  - CSV: `countries/nigeria/data/entities/government-regulators.csv` (3 rows)
  - Profiles: `countries/nigeria/entities/government-regulators/profiles/` (3 profiles)
- Nigeria recruiting operations frequently touch:
  - exam bodies (WAEC, NECO, JAMB)
  - education governance (Federal Ministry of Education; accreditation bodies)
  - professional councils (medicine, pharmacy, nursing, engineering, law)

---

## Allowed write paths

- `countries/nigeria/data/entities/government-regulators.csv`
- `countries/nigeria/entities/government-regulators/profiles/**`
- `countries/nigeria/entities/government-regulators/README.md` (optional; only to link new profiles)
- `executions/T-456-nigeria-regulators-and-exam-bodies-expand/**` (optional notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket for status updates)
- `countries/**` (except `countries/nigeria/**`)

---

## Required outputs

- `countries/nigeria/data/entities/government-regulators.csv`
- At least **8 new** profiles under `countries/nigeria/entities/government-regulators/profiles/` for (suggested minimum set):
  - WAEC
  - NECO
  - JAMB
  - Federal Ministry of Education
  - Medical and Dental Council of Nigeria (MDCN)
  - Pharmacists Council of Nigeria (PCN)
  - Nursing and Midwifery Council of Nigeria (NMCN)
  - Council for the Regulation of Engineering in Nigeria (COREN)

---

## Acceptance criteria

- [ ] `government-regulators.csv` has **≥ 11 total rows** (existing + new) with valid `regulator_id` and `as_of`
- [ ] Each new profile includes mandate, relevance, key processes, official links, and `last_checked`
- [ ] No personal contact details are added; only official role-based contacts (or blank)
- [ ] Links in profiles resolve and are credible (official domains preferred)

