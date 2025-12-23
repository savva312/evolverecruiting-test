---
name: marp-presentations
description: "Global playbook for building branded MARP decks with reusable themes, templates, and export commands (HTML/PDF/PPTX)."
compatibility: MARP CLI, VS Code Marp extension
metadata:
  author: evobuilder
  version: "1.2"
  tags:
    - presentations
    - branding
    - templates
---

# MARP presentation skill (global)

## What this skill delivers
- A repeatable MARP workflow for agents, including setup, theme management, and exports (HTML/PDF/PPTX).
- Multiple theme provisions, starting with the **UNIC Default** theme that mirrors the supplied reference slide.
- A reusable starter deck wired to the UNIC Default theme.
- A placeholder combined UNIC + Evolve SVG so decks render before the final asset arrives.

## When to use this
- You need PowerPoint-grade branding control while staying in Markdown.
- You want to produce PDF/HTML/PPTX exports from a single `.md` source.
- You need to share theme files and templates across tickets without redefining styles.

## Inputs and outputs
- **Inputs:** Content outline per ticket, approved brand specs (colors, fonts, logo), this skill’s theme files.
- **Outputs:** `*.md` slide sources + exported PDF/HTML/PPTX (keep exports out of the repo unless a ticket demands them).

## Setup
1) Install Marp CLI (local):  
```bash
npm install -g @marp-team/marp-cli
```
2) (Optional) VS Code users: install the Marp extension for live preview.
3) Clone/update this repo to access themes and templates under `skills/marp-presentations/`.
4) Fonts: theme is optimized for **Century Gothic**. If unavailable locally, install it or swap in the nearest approved fallback before export.

## Folder map for themes/templates
- `skills/marp-presentations/themes/` — CSS themes (start with `unic-default.css`; add more themes here as needed).
- `skills/marp-presentations/templates/` — starter decks bound to a theme (e.g., `unic-default.md`).
- `skills/marp-presentations/assets/` — logos and shared art. A placeholder `unic-evolve-placeholder.svg` is provided until the final combined logo arrives.
- `skills/marp-presentations/SKILL.md` — this playbook.

## How to create a new deck (fast path)
1) Copy the starter:
```bash
cp skills/marp-presentations/templates/unic-default.md my-deck.md
```
2) Fill in the title and subtitle on the title slide. Body starts at 14pt Century Gothic by default.
3) Update the `footer:` frontmatter:
   - Keep `<span class='footer-center'>CONFIDENTIAL - DO NOT DISTRIBUTE</span>` if confidentiality is required.
   - Use `<span class='footer-center'></span>` to keep the footer spacing but remove the label.
4) Add slides as Markdown (`---` separates slides); use the layout classes listed below.
5) Export (always allow local assets so the SVG logo is embedded):
```bash
# PDF
marp my-deck.md --theme skills/marp-presentations/themes/unic-default.css --pdf --allow-local-files --output out/my-deck.pdf

# PPTX
marp my-deck.md --theme skills/marp-presentations/themes/unic-default.css --pptx --allow-local-files --output out/my-deck.pptx

# HTML
marp my-deck.md --theme skills/marp-presentations/themes/unic-default.css --html --allow-local-files --output out/my-deck.html
```
6) Spot-check pagination: the `.title` class on the cover slide suppresses page numbers; all other slides should show right-aligned pagination in the footer bar.

## Theme provisions
- **UNIC Default (dark, reference-complete):** mirrors the provided slide.
  - Typeface: Century Gothic (fallbacks: "Century Gothic", "Gill Sans", "Trebuchet MS", "Noto Sans", sans-serif).
  - Sizes: Title 24pt; Subtitle 14pt; Body 14pt base (adjust upward per slide if needed); Footer 6pt.
  - Footer: combined UNIC + Evolve placeholder logo on the left, optional confidentiality label centered, page number on the right (suppressed on the title slide).
  - Divider line above footer; no line between header and subheader.
  - Background: #000; Text: #e6e6e6; Accent red: #c8102e.
- **Future formats:** add new CSS files under `themes/` (e.g., `unic-light.css`, `reporting-minimal.css`) and pair each with a starter template under `templates/`. Keep typography, footer logic, and logo hooks consistent so templates stay interchangeable.

## UNIC Default slide kit (template layouts)
- **Title + subtitle + pagination suppression:** use the `.title` class on the cover slide to hide the page number.
- **Agenda:** standard numbered list.
- **Section break:** apply `_class: section-break` and an optional `.eyebrow` label for clean transitions.
- **Problem / solution split:** `.split-5050` grid with `.card` blocks; add `.accent` to highlight the solution.
- **KPI grid:** `.stats-grid` with `.stat` children using `.label`, `.value`, and `.note`.
- **Timeline / roadmap:** `.timeline` container with `.step` items and `data-step` attributes (e.g., `data-step="Q1"`).
- **Competitive table:** Markdown tables inherit dark styling with alternating row shading.
- **Quote / proof:** `.quote-card` with `.source`.
- **Checklist:** `ul.checklist` renders with accent checkmarks.
- **Process steps:** `.steps` grid with `.step` items and `data-step` numbering.
- **Persona pills:** `.pills` container with `.pill` tags.
- **CTA:** `.cta` block with an optional `.btn` link/button treatment.
- **Two/three column grids:** `.cols-2` and `.cols-3` for balanced text columns.
- **Cards with emphasis:** `.card` and `.card.accent` for problem/solution or insight/highlight pairs.

## Customizing the UNIC Default theme
- Update colors or typography in `skills/marp-presentations/themes/unic-default.css`.
- Replace `assets/unic-evolve-placeholder.svg` with the final combined logo, keeping the same filename or updating the theme path.
- Footer label: set `footer:` in frontmatter to `"<span class='footer-center'>CONFIDENTIAL - DO NOT DISTRIBUTE</span>"`; to suppress the label while keeping the footer/logo layout, use `footer: "<span class='footer-center'></span>"`.
- Page numbers: auto-increment on non-title slides; hide them by adding the `.title` class to the cover slide (as in the starter template).
- Body sizing: base 14pt; adjust per slide with inline HTML or local classes if the content is dense (avoid dropping below 12pt).

## Template wiring notes
- Each template should:
  - Reference the correct theme path in frontmatter.
  - Include `paginate: true`.
  - Use `.title` class on the cover slide to suppress page numbering.
  - Keep a footer block (even if empty) so spacing is preserved.
- Body content adapts to prompt needs—bullet spacing and column alignment are handled by the theme; use Markdown lists for bullets as in the reference slide.

## Adding new themes and templates
1) Duplicate `themes/unic-default.css` and adjust color tokens, fonts, or spacing; preserve the footer hooks (`footer::before` logo, `footer::after` pagination).
2) Create a paired starter under `templates/` that:
   - Points to the new theme path.
   - Includes a title slide using `_class: title`.
   - Demonstrates key layouts you expect creators to reuse.
3) Update `skills/README.md` to surface the new skill/theme if it’s general-purpose.

## Quality checks before export
- Titles/subtitles respect specified sizes and spacing (no extra rule between header and subheader).
- Footer line present; page number appears on non-title slides only and sits inside the footer bar.
- Logo renders crisply (SVG preferred); if replacing the placeholder, ensure the asset is high-contrast on black.
- Confidential label is present only when requested.
- PDF/PPTX exports show consistent padding and column alignment.

## Troubleshooting
- **Fonts look off:** Ensure the system has Century Gothic or update the theme fallbacks. For web-safe preview, import a similar Google Font in the CSS, but keep Century Gothic as the primary face to meet brand specs.
- **Logos blurry:** Use the SVG placeholder or a ≥2x PNG; verify the path in `unic-default.css`.
- **Page number on title:** Confirm the cover slide uses the `.title` class; the theme hides pagination for that class.
- **Footer overlapping content:** Keep bottom padding in slides or reduce body content. The theme reserves footer space, but overflowing content can still collide if slides are overloaded.
