# T-454: Romania — counselor toolkit pack (replace placeholders; add RO parent FAQ + email templates)

Status: done
Type: content
Priority: P1
Dependencies: T-449
Claimed-by: codex-run-20251222-1
Claimed-at: 2025-12-22T15:00:00Z
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Turn `countries/romania/go-to-market/schools-playbook/counselor-toolkit.md` into a usable counselor pack by:
- replacing “placeholder” links with real repo links (UNIC Nicosia/Athens admissions, programs, scholarships, housing, visas)
- adding a Romania-ready **parent FAQ** (RO + EN text) and a **counselor intro email template** (RO + EN)

Deliverables must be text-first (no PDFs required).

---

## Context

Current file contains placeholders and an undefined owner, which blocks school-based conversion.

Useful repo references:
- `UNIC/unicnicosia/**`
- `UNIC/unicathens/**`
- Romania playbooks: `countries/romania/go-to-market/**`

---

## Allowed write paths

- `tickets/T-454-romania-counselor-toolkit-pack.md`
- `countries/romania/go-to-market/schools-playbook/counselor-toolkit.md`
- `countries/romania/go-to-market/schools-playbook/templates/**` (new files allowed)
- `executions/**` (optional for notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `.github/**`
- `scripts/**`
- `tickets/**` (except this ticket file)
- `countries/**` (except `countries/romania/go-to-market/**`)

---

## Required outputs

- Updated `countries/romania/go-to-market/schools-playbook/counselor-toolkit.md`
- New templates:
  - `countries/romania/go-to-market/schools-playbook/templates/parent-faq-ro-en.md`
  - `countries/romania/go-to-market/schools-playbook/templates/counselor-intro-email-ro-en.md`

---

## Acceptance criteria

- [x] Counselor toolkit has no placeholder links; all links resolve to existing repo files.
- [x] Parent FAQ includes: costs, scholarships, safety, housing, recognition/degree acceptance (with careful wording), timelines, and contacts.
- [x] Email template exists in RO + EN, with clear subject lines and short CTA.
- [x] No edits outside allowed paths.

## What changed
- Added bilingual parent FAQ + counselor intro email template under `countries/romania/go-to-market/schools-playbook/templates/`.
- Rebuilt counselor toolkit quick links with live UNIC resources, visa/housing references, and embedded links to the new templates.
