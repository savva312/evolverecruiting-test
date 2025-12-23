---
name: high-school-profile-template
description: "Global, reusable markdown template for high school profiles supporting UNIC and UNIC Athens recruiting."
compatibility: All countries (place final profiles under the relevant country directory).
metadata:
  author: user-provided template adapted for repo-wide use
  version: "1.0"
---

## Purpose
- Provide a single, canonical profile template for high schools (feeder/counselor context).
- Keep structure consistent across countries while allowing local facts to be slotted in.
- Reduce copy/paste drift by pointing teams to one maintained template file.

## When to use
- Creating or refreshing high school profiles under `/<country>/entities/schools/profiles/**/README.md`.
- Preparing outreach/counselor briefings that rely on a current school snapshot.
- Backfilling profile gaps surfaced during ticket work (e.g., school playbooks, counselor mapping).

## How to use the template
1) **Copy the canonical file:** start from `skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md`.  
   - Keep the heading `# {High School Name} (Target School Profile)` as the document title.  
   - Preserve checklist sections; mark items with `[x]` only after verification.
   - If your country needs structured metadata (e.g., `school_id`, `city`, `priority_tier`), add a short YAML block **above** the template heading; do not edit the body sections.
2) **Place it correctly:** save the new profile at `/<country>/entities/schools/profiles/<city-or-cluster>/<school-slug>/README.md`.  
   - Use kebab-case for directory names (e.g., `sofia-american-college`).
3) **Fill it factually:** replace `{ }` placeholders with sourced data; avoid speculation.  
   - If data is missing, leave `{ }` and add to **Open Questions**.  
   - Capture sources in section 15 with dates.
4) **Stay country-agnostic in the template itself:** do not embed country examples or assumptions; keep local nuance in the filled profile.
5) **Link it:** update any relevant indices (city or country-level school lists) after adding a new profile.

## Style and QA notes
- Follow `skills/markdown-authoring` for headings, lists, and tables.
- Keep “Purpose” and “Confidentiality” callouts intact to signal internal use.
- Use relative links when referencing other repo files (e.g., counselor toolkit, playbooks).
- Record updates in section 16 so teams can track changes.
