# T-133: Lebanon government regulator scan

Status: done
Type: content
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-20T20:53:03Z
Last-updated: 2025-12-20

---

## Goal

Research and document Lebanese ministries and regulators that influence outbound study, student visas, and credential recognition relevant to UNIC and UNIC Athens. Produce agency profiles with mandates, processes, timelines, and contact points in the country’s `government-regulators` section.

---

## Context

- Links to relevant repo files:
  - `ROADMAP.md` — country-first layout and control plane expectations
  - `countries/lebanon/entities/government-regulators/README.md`
  - `countries/lebanon/entities/government-regulators/profiles/README.md`
- External constraints (if any): none noted
- Assumptions: focus on agencies affecting recognition/licensure, outbound mobility approvals, visas, and consumer protection for Lebanese students considering UNIC/UNIC Athens.

---

## Allowed write paths

- `countries/lebanon/entities/government-regulators/**`
- `countries/lebanon/data/entities/**`
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
- Country directories other than `countries/lebanon/**`

---

## Required outputs

- `countries/lebanon/entities/government-regulators/README.md` updated with coverage summary and open gaps.
- At least three agency profiles in `countries/lebanon/entities/government-regulators/profiles/*.md` (e.g., Ministry of Education and Higher Education, recognition body, visa/immigration authority), each with mandate, process notes, timelines, contacts, `last_checked`, and sources.
- If structured data is captured, a CSV or YAML extract in `countries/lebanon/data/entities/` referencing the same agencies.

---

## Acceptance criteria

- [x] Required output files exist at the specified paths with current `last_checked` dates and source links.
- [x] Each profile documents mandate, relevance to UNIC/UNIC Athens, key processes/timelines, contact channels, and any known requirements for recognition or visas.
- [x] No files were modified outside `Allowed write paths`.
- [x] Links resolve to official or authoritative sources; assumptions are labeled.

---

## Execution notes (optional)

- What changed (short): Added three regulator profiles (MEHE/DGHE, GDGS, MFAE consular legalization), updated the Lebanon regulator README with coverage/gaps, and populated `government-regulators.csv`.
- Any open questions: Need to confirm MEHE equivalency SLA and whether GDGS applies different rules/fees for non-religious university students.
- Follow-up tickets suggested: Add profiles for passport issuance/civil status and profession-specific licensing bodies when scoped.
