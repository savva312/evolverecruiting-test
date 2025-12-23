# T-104: Delete Bulgaria UNIC portfolio, pricing, and language skill

Status: done
Type: content
Priority: P2
Dependencies: (none)
Claimed-by: assistant
Claimed-at: 2026-02-12T00:00:00Z
Last-updated: 2026-02-12

---

## Goal

Remove the outdated `bulgaria-unic-portfolio-pricing-and-language` skill from the Bulgaria skillset so only current, needed procedures remain.

---

## Context

- The referenced skill is no longer required for current recruiting workstreams.
- Cleaning it out prevents drift and keeps the Bulgaria skills index aligned with active content.

---

## Allowed write paths

- `tickets/T-087-delete-bulgaria-unic-portfolio-pricing-and-language-skill.md`
- `bulgaria/skills/bulgaria-unic-portfolio-pricing-and-language/**`
- `bulgaria/skills/README.md`
- `research/**` (optional execution notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**` (global skills)
- Other country directories (e.g., `/nigeria/**`, `/greece/**`, `/serbia/**`, `/romania/**`, `/jordan/**`)
- `tickets/**` (except this ticket)
- `.github/**`
- `scripts/**`

---

## Required outputs

- `bulgaria/skills/bulgaria-unic-portfolio-pricing-and-language/` removed.
- `bulgaria/skills/README.md` updated to reflect the removal.
- This ticket updated with completion notes.

---

## Acceptance criteria

- [x] The `bulgaria-unic-portfolio-pricing-and-language` skill directory no longer exists.
- [x] `bulgaria/skills/README.md` has no reference to the removed skill.
- [x] No files outside Allowed write paths are modified.
- [x] Ticket status updated to `done` with a brief “What changed” summary.

---

## Execution notes (optional)

- What changed (short): Removed the `bulgaria-unic-portfolio-pricing-and-language` skill directory and its reference from the Bulgaria skills index.
- Any open questions: None.
- Follow-up tickets suggested: None.
