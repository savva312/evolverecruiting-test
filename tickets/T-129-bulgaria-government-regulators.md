# T-129: Bulgaria government regulator scan

Status: done
Type: content
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-20T20:52:35+00:00
Last-updated: 2025-12-20

---

## Goal

Research and document the Bulgarian ministries and regulators that shape outbound study, student visas, and credential recognition relevant to UNIC and UNIC Athens. Produce agency profiles with mandates, processes, timelines, and contact points in the country’s `government-regulators` section.

---

## Context

- Links to relevant repo files:
  - `ROADMAP.md` — country-first layout and control plane expectations
  - `countries/bulgaria/entities/government-regulators/README.md`
  - `countries/bulgaria/entities/government-regulators/profiles/README.md`
- External constraints (if any): none noted
- Assumptions: focus on agencies affecting recognition/licensure, outbound mobility approvals, visas, and consumer protection for Bulgarian students.

---

## Allowed write paths

- `countries/bulgaria/entities/government-regulators/**`
- `countries/bulgaria/data/entities/**`
- `research/**`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- Country directories other than `countries/bulgaria/**`

---

## Required outputs

- `countries/bulgaria/entities/government-regulators/README.md` updated with coverage summary and open gaps.
- At least three agency profiles in `countries/bulgaria/entities/government-regulators/profiles/*.md` (e.g., Ministry of Education, National Evaluation and Accreditation Agency, visa authority), each with mandate, process notes, timelines, contacts, `last_checked`, and sources.
- If structured data is captured, a CSV or YAML extract in `countries/bulgaria/data/entities/` referencing the same agencies.

---

## Acceptance criteria

- [ ] Required output files exist at the specified paths with current `last_checked` dates and source links.
- [ ] Each profile documents mandate, relevance to UNIC/UNIC Athens, key processes/timelines, contact channels, and any known requirements for recognition or visas.
- [ ] No files were modified outside `Allowed write paths`.
- [ ] Links resolve to official or authoritative sources; assumptions are labeled.

---

## Execution notes (optional)

- What changed (short): Added four regulator profiles (MoES, NACID, NEAA, MFA) with mandates, process notes, contacts, and sources; updated regulators README with coverage/gaps; populated government-regulators.csv with aligned entries.
- Any open questions: Need official SLA timings from MoES/NACID portals (currently behind anti-bot); MFA hotline/contact confirmation pending direct access.
- Follow-up tickets suggested: Create a micro-ticket to capture NACID processing timelines and Cyprus/Greece-specific MFA advisories once accessible.
