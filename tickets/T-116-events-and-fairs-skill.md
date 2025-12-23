# T-116: Global events and fairs skill

Status: done
Type: content
Priority: P1
Dependencies: T-017, T-020, T-026
Claimed-by: work
Claimed-at: 2025-12-20T20:12:20Z
Last-updated: 2025-12-20

---

## Goal

Add a global skill that standardizes planning, executing, and capturing education fairs/events (targeting, booth/asset prep, lead capture with consent, staffing checklists, post-event follow-up cadence).

---

## Context

- Tickets like T-016 depend on fairs/events workflows, but there is no global standard.
- The skill should include pre-event checklists, lead capture schema, and post-event follow-up sequences.
- Country addenda can later add venue norms or regulatory nuances without duplicating the core workflow.

---

## Allowed write paths

- `skills/events-and-fairs/**`
- `tickets/T-093-events-and-fairs-skill.md`
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

- `skills/events-and-fairs/SKILL.md` detailing pre/during/post event workflows, asset/staffing checklists, lead capture (fields + consent), and follow-up cadence.

---

## Acceptance criteria

- [x] Global skill documents the end-to-end fairs/events workflow with required checklists and lead capture schema.
- [x] Guidance is country-agnostic; local nuances are deferred to country addenda.
- [x] No files outside `Allowed write paths` are modified.

---

## Execution notes (optional)

- What changed (short): Added global events-and-fairs skill with pre/during/post workflows, staffing and asset checklists, consent-safe lead schema, reporting, and guidance for country addenda using the updated country path.
- Any open questions: None.
- Follow-up tickets suggested: Create country-level events-and-fairs addenda (e.g., Bulgaria, Nigeria, Greece) once local consent language and organizer norms are collected.
