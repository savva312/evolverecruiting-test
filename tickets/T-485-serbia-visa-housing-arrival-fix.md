# T-485: Serbia — Fix visa/residence assumptions in housing & arrival playbook

Status: open
Type: content
Priority: P0
Dependencies: (none)
Claimed-by:
Claimed-at:
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Make `housing-and-arrival.md` safe, accurate, and Serbia-specific by correcting visa/residence assumptions and adding an operational checklist split by campus (UNIC Nicosia vs UNIC Athens).

---

## Context

- Primary file to fix:
  - `countries/serbia/go-to-market/offerholder-and-yield/housing-and-arrival.md`
- Related reference material (read-only inputs):
  - `UNIC/unicnicosia/housing/README.md`
  - `UNIC/unicathens/housing/README.md`
  - `UNIC/unicnicosia/visas/README.md`
  - `UNIC/unicathens/visas/README.md`
- Current issues to address:
  - Incorrect “Serbian/EU passport holders: visa-free entry” assumptions.
  - Placeholder contact emails and missing campus-specific “what admissions ops must issue by when”.

---

## Allowed write paths

- `countries/serbia/go-to-market/offerholder-and-yield/housing-and-arrival.md`
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

- `countries/serbia/go-to-market/offerholder-and-yield/housing-and-arrival.md`

---

## Acceptance criteria

- [ ] Replaces the “Assumptions (visa/residence)” section with sourced, Serbia-relevant branching (Serbian citizen vs EU/EEA citizen vs non-EU resident in Serbia) and clearly separates:
  - [ ] **Entry** requirements
  - [ ] **Long-stay** / residence permit requirements for study
- [ ] Adds a campus-split checklist table (“Nicosia” vs “Athens”) that specifies:
  - [ ] documents the student must provide
  - [ ] documents UNIC must issue (letter types, proof of enrolment, housing confirmation)
  - [ ] recommended timing buffers (sourced or clearly labeled as internal operational targets)
- [ ] Removes placeholder contact emails; replaces with either real internal contacts (if available in repo) or a neutral pattern (“use campus admissions ops mailbox”) without inventing addresses.
- [ ] No edits outside allowed write paths.

