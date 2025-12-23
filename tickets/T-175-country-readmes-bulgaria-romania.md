# T-175: Country README setup for Bulgaria and Romania

Status: done
Type: content
Priority: P2
Dependencies: (none)
Claimed-by: develop
Claimed-at: 2025-12-20T22:12:25+00:00
Last-updated: 2025-12-20
Completed-at: 2025-12-20T22:20:00+00:00

---

## Goal

Create concise country-level README files for Bulgaria and Romania to explain scope, directory layout, and contribution rules so future ticket work stays aligned with the country-first structure.

---

## Context

- Bulgaria and Romania directories follow the country-first layout but currently lack entry-point README files.
- Greece and Nigeria already have country README pages that set expectations for contributions and navigation.
- Adding READMEs will give contributors quick orientation and reinforce ticket scoping.

---

## Allowed write paths

- `tickets/T-148-country-readmes-bulgaria-romania.md`
- `countries/bulgaria/README.md`
- `countries/romania/README.md`
- `research/T-148-country-readmes-bulgaria-romania/**` (optional notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- Any country directories other than Bulgaria and Romania
- Any tickets other than this file

---

## Required outputs

- `countries/bulgaria/README.md` describing the Bulgaria workspace scope, directory map, and contribution rules aligned to the country-first layout.
- `countries/romania/README.md` with the same structure tailored to Romania.
- Ticket updated to `done` with a brief summary once READMEs are added.

---

## Acceptance criteria

- Both README files exist at the specified paths and mirror the clarity/structure of existing country READMEs (e.g., Greece, Nigeria).
- Content reflects Bulgaria- or Romania-specific naming without cross-country leakage.
- Guidance reinforces ticket scoping and points to the country skills subtree where applicable.
- No files outside Allowed write paths are modified.

---

## Execution notes (optional)

- What changed (short): Added Bulgaria and Romania country README files with directory maps, contribution guardrails, and pointers to country skills.
- Follow-ups: None.
