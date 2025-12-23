# T-528: Lebanon — offerholder comms sequence (EN + AR/FR placeholders) for yield

Status: open
Type: content
Priority: P1
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

Create a Lebanon-specific comms sequence that moves admitted students from offer → deposit → arrival with clear, consistent messaging and minimal Athens/Nicosia confusion.

---

## Context

Existing yield components (helpful but not a complete comms sequence):
- `countries/lebanon/go-to-market/offerholder-and-yield/deposit-deadlines.md`
- `countries/lebanon/go-to-market/offerholder-and-yield/housing-and-arrival.md`
- `countries/lebanon/go-to-market/offerholder-and-yield/webinars.md`

---

## Allowed write paths

- `tickets/T-456-lebanon-offerholder-comms-sequence.md`
- `countries/lebanon/go-to-market/offerholder-and-yield/comms-sequence.md`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**` (global)
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- `countries/**` (except `countries/lebanon/**`)

---

## Required outputs

- `countries/lebanon/go-to-market/offerholder-and-yield/comms-sequence.md` created with:
  - a 6–10 touch sequence (Email + WhatsApp where compliant) from Day 0 offer through arrival week
  - split logic for: Medicine vs non-Medicine; EU passport vs non-EU; Athens vs Nicosia
  - subject line conventions that include campus tag (`[ATHENS]` / `[NICOSIA]`)
  - short EN templates for each touch + clear placeholders for AR/FR translation blocks

---

## Acceptance criteria

- [ ] Sequence aligns with Lebanon exam timing (June/July results windows) and avoids high-pressure messaging during exam windows.
- [ ] Includes compliance notes (consent required for messaging apps; do not store sensitive docs in chat).
- [ ] No files outside `Allowed write paths` were modified.

