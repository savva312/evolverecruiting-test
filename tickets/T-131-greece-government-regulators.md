# T-131: Greece government regulator scan

Status: done
Type: content
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-20T20:53:07+00:00
Last-updated: 2025-12-20

---

## Goal

Research and document Greek ministries and regulators that influence outbound study, student visas, and credential recognition relevant to UNIC and UNIC Athens. Produce agency profiles with mandates, processes, timelines, and contact points in the country’s `government-regulators` section.

---

## Context

- Links to relevant repo files:
  - `ROADMAP.md` — country-first layout and control plane expectations
  - `countries/greece/entities/government-regulators/README.md`
  - `countries/greece/entities/government-regulators/profiles/README.md` (to create if missing)
- External constraints (if any): none noted
- Assumptions: focus on agencies affecting recognition/licensure, outbound mobility approvals, visas, and consumer protection for Greek students considering UNIC/UNIC Athens.

---

## Allowed write paths

- `countries/greece/entities/government-regulators/**`
- `countries/greece/data/entities/**`
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
- Country directories other than `countries/greece/**`

---

## Required outputs

- `countries/greece/entities/government-regulators/README.md` updated with coverage summary and open gaps.
- At least three agency profiles in `countries/greece/entities/government-regulators/profiles/*.md` (e.g., Ministry of Education, DOATAP, visa/immigration authority), each with mandate, process notes, timelines, contacts, `last_checked`, and sources.
- If structured data is captured, a CSV or YAML extract in `countries/greece/data/entities/` referencing the same agencies.

---

## Acceptance criteria

- [ ] Required output files exist at the specified paths with current `last_checked` dates and source links.
- [ ] Each profile documents mandate, relevance to UNIC/UNIC Athens, key processes/timelines, contact channels, and any known requirements for recognition or visas.
- [ ] No files were modified outside `Allowed write paths`.
- [ ] Links resolve to official or authoritative sources; assumptions are labeled.

---

## Execution notes (optional)

- What changed (short): Added Greece regulator coverage for Ministry of Education, DOATAP, SAEP, and Migration Ministry; created profiles and structured CSV; updated Greece regulators index.
- Any open questions: Track evolving DOATAP/SAEP processing timelines and any immigration code updates affecting study permits.
- Follow-up tickets suggested: Consider profiles for consumer protection/competition regulators if education marketing risks rise.
