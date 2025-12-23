# T-134: Romania government regulator scan

Status: done
Type: content
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-20
Completed-at: 2025-12-20
Last-updated: 2025-12-20

---

## Goal

Research and document Romanian ministries and regulators that influence outbound study, student visas, and credential recognition relevant to UNIC and UNIC Athens. Produce agency profiles with mandates, processes, timelines, and contact points in the country’s `government-regulators` section.

---

## Context

- Links to relevant repo files:
  - `ROADMAP.md` — country-first layout and control plane expectations
  - `countries/romania/entities/government-regulators/README.md`
  - `countries/romania/entities/government-regulators/profiles/README.md`
- External constraints (if any): none noted
- Assumptions: focus on agencies affecting recognition/licensure, outbound mobility approvals, visas, and consumer protection for Romanian students considering UNIC/UNIC Athens.

---

## Allowed write paths

- `countries/romania/entities/government-regulators/**`
- `countries/romania/data/entities/**`
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
- Country directories other than `countries/romania/**`

---

## Required outputs

- `countries/romania/entities/government-regulators/README.md` updated with coverage summary and open gaps.
- At least three agency profiles in `countries/romania/entities/government-regulators/profiles/*.md` (e.g., Ministry of Education, ARACIS/CNRED, visa/immigration authority), each with mandate, process notes, timelines, contacts, `last_checked`, and sources.
- If structured data is captured, a CSV or YAML extract in `countries/romania/data/entities/` referencing the same agencies.

---

## Acceptance criteria

- [x] Required output files exist at the specified paths with current `last_checked` dates and source links.
- [x] Each profile documents mandate, relevance to UNIC/UNIC Athens, key processes/timelines, contact channels, and any known requirements for recognition or visas.
- [x] No files were modified outside `Allowed write paths`.
- [x] Links resolve to official or authoritative sources; assumptions are labeled.

---

## Execution notes (optional)

- What changed (short): Added four regulator profiles (Ministry of Education, CNRED, ARACIS, MFA Consular Legalization), updated Romania regulator README with coverage/gaps, and populated government-regulators CSV.
- Any open questions: Need prefecture-level apostille service details and IGI perspective for non-EU students studying in Romania.
- Follow-up tickets suggested: Add prefecture apostille service standards and IGI guidance to the Romania government-regulators section.
