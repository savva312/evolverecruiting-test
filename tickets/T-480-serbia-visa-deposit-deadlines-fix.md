# T-480: Serbia — Fix visa/residence assumptions in deposit deadlines playbook

Status: done
Type: content
Priority: P0
Dependencies: (none)
Claimed-by: exec-20251222T2039Z
Claimed-at: 2025-12-22T20:39:54Z
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Correct Serbia-specific immigration assumptions in the deposit timeline playbook so it is safe to use for real offerholders (both UNIC Nicosia and UNIC Athens).

---

## Context

- Primary file to fix:
  - `countries/serbia/go-to-market/offerholder-and-yield/deposit-deadlines.md`
- Related reference material (read-only inputs):
  - `UNIC/unicnicosia/visas/README.md`
  - `UNIC/unicathens/visas/README.md`
- Current issues to address:
  - The playbook implies many Serbian students are “EU passport holders” and/or “visa-free” in ways that are likely incorrect for **study** purposes.
  - Missing clear branching for: **Serbian citizens**, **EU/EEA citizens resident in Serbia**, and **non-Serbian/non-EU residents in Serbia**.

---

## Allowed write paths

- `countries/serbia/go-to-market/offerholder-and-yield/deposit-deadlines.md`
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

- `countries/serbia/go-to-market/offerholder-and-yield/deposit-deadlines.md`

---

## Acceptance criteria

- [x] Removes/rewrites any claims that Serbian students are generally “EU passport holders” or “visa-free” without qualification.
- [x] Adds a Serbia-ready “immigration branching” section that clearly distinguishes:
  - [x] Serbian citizens (default case)
  - [x] EU/EEA citizens resident in Serbia
  - [x] Non-EU residents in Serbia
- [x] For each branch, states what deposit timing must protect (e.g., when unconditional offer letter is needed) **with citations to official sources** and `last_verified` dates.
- [x] Includes a prominent disclaimer: “requirements change; confirm with the relevant embassy/consulate and campus visa team”.
- [x] No edits outside allowed write paths.

---

## What changed

- Updated `countries/serbia/go-to-market/offerholder-and-yield/deposit-deadlines.md` to remove inaccurate “EU passport/visa-free” assumptions and add Serbia-specific immigration branching for UNIC Nicosia and UNIC Athens with official-source links and `last_verified` dates.
