# T-305: Global MARP presentation skill and UNIC default theme

Status: done
Type: structure
Priority: P1
Dependencies: T-020
Claimed-by: work
Claimed-at: 2025-12-21T10:20:59+00:00
Last-updated: 2025-12-21T10:22:56+00:00

---

## Goal

Create a global, production-grade skill for authoring MARP decks with multiple theme provisions, including a branded “UNIC Default” theme and starter templates that match the provided branding reference.

## Context

- Agents need a repeatable, ticket-friendly workflow for MARP slide creation with strong branding control and export guidance (HTML/PDF/PPTX).
- Branding requirements include UNIC Default typography, footer treatments, page numbering, confidentiality toggle, and combined UNIC + Evolve logo placement (placeholder logo acceptable until final asset is provided).
- Skills are protected; a structure ticket is required to add new global skills and update the global skills index.

## Allowed write paths

- `skills/marp-presentations/**`
- `skills/README.md`
- `tickets/T-273-marp-presentation-skill.md`
- `executions/**` (optional notes)

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- Country directories (e.g., `/countries/**`)
- Other tickets in `/tickets/**` (except status updates to this file)
- `.github/**`
- `scripts/**`
- Any path not listed in Allowed write paths

## Required outputs

- `skills/marp-presentations/SKILL.md` (global MARP skill with multiple template provisions and UNIC Default instructions)
- `skills/marp-presentations/themes/unic-default.css` (branded theme)
- `skills/marp-presentations/templates/unic-default.md` (starter deck wired to the theme)
- `skills/marp-presentations/assets/unic-evolve-placeholder.svg` (temporary combined logo for footer)
- `skills/README.md` updated to list the new skill
- `tickets/T-273-marp-presentation-skill.md` updated to `Status: done` with completion notes

## Acceptance criteria

- Skill describes MARP setup, export commands, theme structure, and how to add additional templates beyond UNIC Default.
- UNIC Default theme matches requested specs: Century Gothic (title 24, subtitle 14, body ≥14), optional “Confidential - Do Not Distribute” footer label, line above footer, no line between header/subheader, footer with combined logo placeholder and right-aligned page number on non-title slides.
- Starter template uses the UNIC Default theme, demonstrates pagination rules (page number hidden on title), and references the placeholder logo.
- Placeholder SVG is present and referenced in the theme.
- Global skills index lists the new skill.
- No files modified outside Allowed write paths.

## Execution notes (optional)

- What changed (short): Refined the MARP skill with explicit Century Gothic guidance, allow-local-files export commands, and a clearer template wiring section; expanded the starter deck with column layouts and updated helper styles/pagination so the footer holds the logo, confidentiality toggle, and right-aligned page numbers.
- Open questions: None.
- Follow-up tickets suggested: Replace placeholder logo SVG with the final asset when available; add light/print theme variants if required.
