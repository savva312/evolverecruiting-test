# T-114: Global school outreach and counselor engagement skill

Status: done
Type: content
Priority: P1
Dependencies: T-017, T-020, T-026
Claimed-by: work
Claimed-at: 2025-12-20T20:12:08Z
Last-updated: 2025-12-20

---

## Goal

Create a global skill that standardizes school outreach and counselor engagement workflows (targeting, sequencing visits, artifacts, data capture, follow-up) so countries can attach local etiquette and path conventions via addenda.

---

## Context

- Multiple tickets depend on school outreach playbooks (e.g., T-011) and school profiling, but no global workflow exists.
- The skill should cover visit prep, meeting structure, leave-behinds, data to log, and follow-up cadences.
- Local etiquette, language, or holiday calendars belong in country addenda, not the global skill.

---

## Allowed write paths

- `skills/school-outreach-and-counselor-engagement/**`
- `tickets/T-091-school-outreach-and-counselor-engagement.md`
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

- `skills/school-outreach-and-counselor-engagement/SKILL.md` detailing targeting, outreach sequences, meeting/visit agendas, artifacts (decks, one-pagers), data fields to capture, and follow-up playbooks.

---

## Acceptance criteria

- [x] Global skill provides an end-to-end outreach workflow with sample sequences and required artifacts.
- [x] Guidance is country-agnostic; local etiquette/nuances are deferred to country addenda.
- [x] No files outside `Allowed write paths` are modified.

---

## Execution notes (optional)

- What changed (short): Added a global school outreach and counselor engagement skill with end-to-end workflow, artifacts, data fields, sequences, and country addenda guidance reflecting the consolidated `countries/<country>/` paths.
- Any open questions: None.
- Follow-up tickets suggested: Country addenda for priority markets (e.g., Bulgaria, Nigeria, Greece) to capture local etiquette and channels.
