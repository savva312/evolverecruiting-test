# T-130: Nigeria government regulator scan

Status: done
Type: content
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-20T20:53:06Z
Last-updated: 2025-12-20

---

## Goal

Research and document Nigerian ministries and regulators that influence outbound study, student visas, and credential recognition relevant to UNIC and UNIC Athens. Produce agency profiles with mandates, processes, timelines, and contact points in the country’s `government-regulators` section.

---

## Context

- Links to relevant repo files:
  - `ROADMAP.md` — country-first layout and control plane expectations
  - `countries/nigeria/entities/government-regulators/README.md`
  - `countries/nigeria/entities/government-regulators/profiles/README.md` (to create if missing)
- External constraints (if any): none noted
- Assumptions: focus on agencies affecting recognition/licensure, outbound mobility approvals, visas, consumer protection, and education quality for Nigerian students.

---

## Allowed write paths

- `countries/nigeria/entities/government-regulators/**`
- `countries/nigeria/data/entities/**`
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
- Country directories other than `countries/nigeria/**`

---

## Required outputs

- `countries/nigeria/entities/government-regulators/README.md` updated with coverage summary and open gaps.
- At least three agency profiles in `countries/nigeria/entities/government-regulators/profiles/*.md` (e.g., Federal Ministry of Education, NUC, embassies/visa authorities), each with mandate, process notes, timelines, contacts, `last_checked`, and sources.
- If structured data is captured, a CSV or YAML extract in `countries/nigeria/data/entities/` referencing the same agencies.

---

## Acceptance criteria

- [x] Required output files exist at the specified paths with current `last_checked` dates and source links.
- [x] Each profile documents mandate, relevance to UNIC/UNIC Athens, key processes/timelines, contact channels, and any known requirements for recognition or visas.
- [x] No files were modified outside `Allowed write paths`.
- [x] Links resolve to official or authoritative sources; assumptions are labeled.

---

## Execution notes (optional)

- What changed (short): Added three regulator profiles (NUC, MFA legalisation, NIS passports), updated Nigeria regulators README with coverage/gaps, and populated regulators CSV + dictionary with current contacts/links.
- Any open questions: Need Ministry of Education and WAEC/NECO authentication steps clarified from primary sources.
- Follow-up tickets suggested: None beyond capturing those gaps when scoped.
