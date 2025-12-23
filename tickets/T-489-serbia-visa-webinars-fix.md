# T-489: Serbia — Fix visa/residence assumptions in offerholder webinar plan

Status: done
Type: content
Priority: P0
Dependencies: (none)
Claimed-by: evoticketresolver_v1skmqaw
Claimed-at: 2025-12-22T20:39:46Z
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Update the Serbia offerholder webinar sequence so the “Visa, docs, housing” webinar is accurate for Serbian nationals and does not embed unsafe assumptions.

---

## Context

- Primary file to fix:
  - `countries/serbia/go-to-market/offerholder-and-yield/webinars.md`
- Related reference material (read-only inputs):
  - `countries/serbia/go-to-market/offerholder-and-yield/housing-and-arrival.md`
  - `UNIC/unicnicosia/visas/README.md`
  - `UNIC/unicathens/visas/README.md`
- Current issues to address:
  - “Assumptions: majority are EU passport holders” is likely incorrect for Serbia and could create compliance risk.
  - Missing Serbia-specific Q&A prompts for common parent objections (timelines, appointments, proof-of-funds, translations).

---

## Allowed write paths

- `countries/serbia/go-to-market/offerholder-and-yield/webinars.md`
- `executions/**` (optional; notes only)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket file for status updates)

---

## Required outputs

- `countries/serbia/go-to-market/offerholder-and-yield/webinars.md`

---

## Acceptance criteria

- [x] Removes the “EU passport holder majority” assumption and replaces it with a Serbia-relevant segmentation statement (Serbian citizens default; EU/EEA and other residents handled as exceptions).
- [x] Adds a “Visa/residence content guardrails” section that tells staff what they can/can’t promise and where to point students for authoritative confirmation (with `last_verified` dates).
- [x] Adds a Serbia-ready Q&A bank (10–15 questions) for the visa/housing webinar, separated by campus where needed.
- [x] No edits outside allowed write paths.

---

## What changed

- Updated `countries/serbia/go-to-market/offerholder-and-yield/webinars.md` to remove EU-passport assumptions, add visa/residence guardrails with `last_verified` dates, and add a Serbia-ready Q&A bank split by campus.
- Added execution note: `executions/evoticketresolver_v1skmqaw/T-489.md`.
