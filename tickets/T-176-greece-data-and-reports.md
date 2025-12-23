# T-176: Greece data standards and Athens recruitment reports

Status: done
Type: content
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-20T22:04:27Z
Last-updated: 2025-12-20

---

## Goal

Deliver Greece-scoped data standards and starter datasets plus two priority reports for UNIC Athens. Specifically: add a Greece `field-standards.md` aligned to other markets, seed core entity CSVs (agents, schools, regulators) under `countries/greece/data/entities/`, and publish two reports (outbound mobility baseline, UNIC Athens recruitment plan) following the Jordan/Serbia formats.

---

## Context

- Greece now mirrors the Bulgaria country layout but lacks a local data standards file and seeded entity CSVs.
- Jordan and Serbia already carry outbound mobility and UNIC Athens recruitment plan reports; Greece needs matching scaffolds to keep formats consistent.
- Work must stay Greece-scoped and text-first, using the country-first layout described in `AGENTS.md` and `ROADMAP.md`.

---

## Allowed write paths

- `countries/greece/data/**`
- `countries/greece/reports/**`
- `tickets/T-148-greece-data-and-reports.md`
- `research/T-148-greece-data-and-reports/**` (optional run notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- Other country directories (e.g., `countries/bulgaria/**`, `countries/nigeria/**`, etc.)
- `tickets/**` (except this ticket file)
- `.github/**`
- `scripts/**`

---

## Required outputs

- `countries/greece/data/field-standards.md` mirroring the schema used in other markets.
- Seeded CSVs under `countries/greece/data/entities/` for agents, schools, and government regulators (aligned with cross-country headers).
- Two Greece reports under `countries/greece/reports/`: an outbound mobility baseline and a UNIC Athens recruitment plan, following the Jordan/Serbia report formats.
- Ticket status updated with completion notes once work is done.

---

## Acceptance criteria

- [x] The field standards file exists at the specified path and reflects the shared schema used in other markets.
- [x] Agents, schools, and government regulator CSVs exist with Greece-scoped starter rows using consistent headers and `as_of` dates.
- [x] Two reports exist under `countries/greece/reports/` with the expected topics and structure mirroring Jordan/Serbia formats.
- [x] No files outside `Allowed write paths` are modified.
- [x] Ticket status updated when complete with a short “What changed” summary.

---

## Execution notes (optional)

- What changed (short): Added Greece field standards, seeded entity CSVs (agents, schools, regulators) with consistent headers and `as_of` dates, and published two Greece reports (outbound mobility baseline and UNIC Athens recruitment plan) aligned to Jordan/Serbia formats.
- Any open questions:
- Follow-up tickets suggested:
