# T-118: Global offerholder and yield playbooks

Status: done
Type: content
Priority: P1
Dependencies: T-017, T-020, T-026
Claimed-by: work
Claimed-at: 2025-12-20T20:12:23Z
Last-updated: 2025-02-15

---

## Goal

Add a global skill that standardizes offerholder and yield engagement workflows (cadence, channels, objection handling, SLAs, consent) so countries can add lightweight addenda without duplicating the core process.

---

## Context

- Roadmap and tickets emphasize offerholder/yield workflows (e.g., T-012) but no global skill exists.
- Global skill should define reusable playbook elements: comms cadence, channel mix, data capture, and handoffs.
- Country addenda (future tickets) should only record local compliance or channel nuances.

---

## Allowed write paths

- `skills/offerholder-and-yield-playbooks/**`
- `tickets/T-095-offerholder-and-yield-playbooks.md`
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

- `skills/offerholder-and-yield-playbooks/SKILL.md` defining the global workflow, cadence templates, channel mix, objection handling, consent/logging rules, and required artifacts.

---

## Acceptance criteria

- [x] Global skill documents the end-to-end offerholder/yield process with sample cadences and data fields to log.
- [x] Guidance is country-agnostic; any local differences are deferred to country addenda (not added here).
- [x] No files outside `Allowed write paths` are modified.

---

## Execution notes (optional)

- What changed (short): Added a global offerholder/yield skill covering workflows, cadences, data logging, objection handling, consent, SLAs, and required artifacts for market addenda to extend.
- Any open questions: None noted.
- Follow-up tickets suggested: Country addenda to localize consent, channel availability, and visa specifics per market.
