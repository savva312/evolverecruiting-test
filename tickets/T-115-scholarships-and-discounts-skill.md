# T-115: Global scholarships and discounts skill

Status: done
Type: content
Priority: P1
Dependencies: T-017, T-020, T-026
Claimed-by: work
Claimed-at: 2025-02-02
Last-updated: 2025-02-02

---

## Goal

Create a global skill to standardize how scholarships, discounts, and financial incentives are cataloged (eligibility, amount/structure, deadlines, documentation, messaging rules) with reusable CSV/markdown schemas and compliance cautions.

---

## Context

- Tickets like T-015 call for scholarship/discount scans, but there is no global method.
- The skill should define data fields, sourcing checklist, and messaging/compliance guardrails.
- Country addenda can later capture local funding schemes without duplicating the core process.

---

## Allowed write paths

- `skills/scholarships-and-discounts/**`
- `tickets/T-092-scholarships-and-discounts-skill.md`
- `research/**` (optional notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**` (except the path above)
- `tickets/**` (except this ticket file)
- `.github/**`
- `scripts/**`
- Any country directories (e.g., `/bulgaria/**`, `/nigeria/**`, `/greece/**`)

---

## Required outputs

- `skills/scholarships-and-discounts/SKILL.md` outlining the global workflow, CSV/markdown schema, sourcing checklist, and messaging/compliance notes.

---

## Acceptance criteria

- [x] Global skill defines a reusable schema and workflow for scholarship/discount mapping.
- [x] Guidance is country-agnostic; local programs/nuances are deferred to country addenda.
- [x] No files outside `Allowed write paths` are modified.

---

## Execution notes (optional)

- What changed (short): Created global scholarships and discounts skill with reusable schema, workflow, sourcing checklist, and compliance/messaging guardrails; added country addenda pattern.
- Any open questions: None noted.
- Follow-up tickets suggested: Country-level addenda as local funding schemes are scoped.
