# T-135: Serbia government regulator scan

Status: done
Type: content
Priority: P1
Dependencies: (none)
Claimed-by: agent-run-2025-12-20
Claimed-at: 2025-12-20T20:53:22Z
Last-updated: 2025-12-20

---

## Goal

Research and document Serbian ministries and regulators that influence outbound study, student visas, and credential recognition relevant to UNIC and UNIC Athens. Produce agency profiles with mandates, processes, timelines, and contact points in the country’s `government-regulators` section.

---

## Context

- Links to relevant repo files:
  - `ROADMAP.md` — country-first layout and control plane expectations
  - `countries/serbia/entities/government-regulators/README.md`
  - `countries/serbia/entities/government-regulators/profiles/README.md`
- External constraints (if any): none noted
- Assumptions: focus on agencies affecting recognition/licensure, outbound mobility approvals, visas, and consumer protection for Serbian students.

---

## Allowed write paths

- `countries/serbia/entities/government-regulators/**`
- `countries/serbia/data/entities/**`
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
- Country directories other than `countries/serbia/**`

---

## Required outputs

- `countries/serbia/entities/government-regulators/README.md` updated with coverage summary and open gaps.
- At least three agency profiles in `countries/serbia/entities/government-regulators/profiles/*.md` (e.g., Ministry of Education, accreditation/quality agency, visa/immigration authority), each with mandate, process notes, timelines, contacts, `last_checked`, and sources.
- If structured data is captured, a CSV or YAML extract in `countries/serbia/data/entities/` referencing the same agencies.

---

## Acceptance criteria

- [ ] Required output files exist at the specified paths with current `last_checked` dates and source links.
- [ ] Each profile documents mandate, relevance to UNIC/UNIC Athens, key processes/timelines, contact channels, and any known requirements for recognition or visas.
- [ ] No files were modified outside `Allowed write paths`.
- [ ] Links resolve to official or authoritative sources; assumptions are labeled.

---

## Execution notes (optional)

- What changed (short): Added four Serbian regulator profiles (education, ENIC/NARIC, QA, visas/residence), updated coverage summary, and populated structured regulator data.
- Any open questions: Need confirmation on consumer/data-protection authorities’ relevance to outbound recruiting.
- Follow-up tickets suggested: None beyond adding consumer/data-protection coverage if prioritized.
