---
name: photo-documentation
description: "Standard for renaming facility photo sets, writing cross-functional per-photo notes, and maintaining a photoindex.md with coverage gaps."
compatibility: Any facility, site, or workspace photo set organized in repo folders.
metadata:
  author: canonical
  version: "1.1"
---

## Purpose and scope
- Use this skill whenever adding or cleaning up photo sets (facilities, events, site visits).
- Applies to text-first workflows: every photo set should have descriptive filenames **and** a markdown index (`photoindex.md`) in the same folder.
- Keep facts observable; mark assumptions (“appears to…”) and log gaps in a wishlist.
- Write indices so they are useful across stakeholders: **architect/designer**, **engineer**, **university facilities/operations**, **marketing/admissions**, and **educator/student experience**.

## File naming standard
### Default (recommended when folder already encodes context)
- Pattern: `YYYYMMDD - <short-slug>.jpeg` or `YYYYMMDD - NN-<short-slug>.jpeg`
  - `YYYYMMDD`: shoot date (local to the site).
  - `<short-slug>`: 3–8 keywords that make the photo findable (`main-entrance-curtainwall`, `boomgate-pedestal`, `rooftop-condensers`, `gas-shutoff-manifold`).
  - `NN-` counter: use when you have many similar angles (walkarounds) or when you want deterministic ordering (`01-...`, `02-...`).
  - Keep names **short** for GitHub browsing: avoid repeating campus/building/room if the folder path already provides that context.

### When context is ambiguous (shared photo folders)
- Pattern: `YYYYMMDD - <campus> - <building/room> - <short-slug>.jpeg`
  - Use this only when the photo folder does not already encode the campus/building/room context.

### Extensions and safety
- Prefer `.jpeg` (or `.jpg`) for consistency; convert HEIC/PNG to `.jpeg` (lossless if possible).
- Rename after copying into the repo; do not overwrite originals without a backup.

## Index file (`photoindex.md`)
- Create `photoindex.md` inside the photo folder (one per photo set).
- Keep filenames in the index identical to disk names (case-sensitive).
- Link filenames so reviewers can click straight to the image:
  - Use `[filename](<./filename>)` (angle brackets allow spaces in filenames).

## Recommended index structure (world-class, cross-functional)
Each `photoindex.md` should follow the same structure:
1) **Title + metadata** (location, date, photo count, and an “evidence style” note)
2) **Scope of this set** (1–3 sentences)
3) **How to use this index** (3 bullets)
4) **Stakeholder perspectives (what to look for)** with short subsections for:
   - Architect / designer
   - Engineer (MEP / structural / civil)
   - Facilities / operations
   - Marketing / admissions
   - Educator / student experience
5) **Photo inventory** (one entry per image; keep the order walkable)
6) **Wishlist / gaps** (specific missing angles/close-ups and retake requests)

### Per-photo entry template
For each photo, include:
- **Observed:** what is visible + (if known) vantage/facing; avoid speculation and use “appears to” when uncertain.
- **Architect:** what this image says about spatial sequence, identity, material transitions, and user experience.
- **Engineer:** what to verify (MEP labels/clearances, drainage/falls, guard/handrail geometry, thresholds) and what follow-up evidence is needed.
- **Facilities:** operations implications (maintenance access, safety, housekeeping, waste, security) and quick wins.
- **Marketing:** whether it’s a hero/public-facing image or internal-only; suggested narrative use.
- **Educator:** how it supports learning delivery and student experience (orientation, workflow, studio/making culture, safety onboarding).
- **Follow-ups:** close-ups, measurements, retakes, or “— (see wishlist)”.

## Ordering and coverage
- Ordering: sort by walking path (entry → interior), then clockwise within a room; keep related detail shots immediately after their wide shot.
- Always add a wishlist even if coverage feels complete.
- Typical asks: electrical panels/labels, MEP above ceilings, close-ups of controls, signage, accessibility clearances, exterior approach, storage, safety gear, egress routes.
- If photos are blurry or blocked, log a retake request with the needed angle or distance.

## Folder structure and metadata
- Store photos in a dedicated `photos/` subfolder for the space; keep shoot-specific subfolders only when multiple shoots exist (e.g., `photos/20251220/`).
- Keep the `photoindex.md` alongside the photos it documents (inside the shoot folder if subfolders are used).
- Preserve EXIF where possible; if stripped, note missing timestamps in the index header.
- Avoid speculative captions; rely on visible evidence or measured notes from the same session.

## Quick checklist
- [ ] Files renamed to a concise scheme (`YYYYMMDD - <short-slug>.jpeg` or `YYYYMMDD - NN-<short-slug>.jpeg`)
- [ ] `photoindex.md` created in the photo folder with standard sections + wishlist
- [ ] Each photo entry includes **Observed** + stakeholder notes (architect/engineer/facilities/marketing/educator)
- [ ] Missing shots or retakes listed in wishlist with specifics
- [ ] No edits outside the designated photo folder
