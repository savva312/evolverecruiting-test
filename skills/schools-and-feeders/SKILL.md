---
name: schools-and-feeders
description: Global workflow for building school feeder profiles, counselor mapping, and CSV datasets that feed UNIC and UNIC Athens recruiting.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: global
---

# Skill: Schools and feeders (global)

## Purpose

Standardize how we map high-school feeders, counselor ecosystems, and outreach logistics across markets. This skill produces:
- Human-readable school profiles using the global template.
- Structured CSVs that match profile metadata.
- Privacy-safe counselor/contact notes that can be shared across teams.

Always pair this skill with the ticket you are executing and the **global high school profile template** in `skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md`.

---

## Before you start

1) Read the ticket for scope, allowed write paths, and required outputs.
2) Review repo guardrails if needed:
   - `/skills/ticket-boundaries/SKILL.md`
   - `/skills/assets-and-sources/SKILL.md`
   - `/skills/markdown-authoring/SKILL.md`
3) Check the relevant **country skill** for local tiering, city priorities, or naming conventions (e.g., `/countries/bulgaria/skills/**`, `/countries/greece/skills/**`).

---

## Required outputs (unless the ticket overrides)

1) **School profiles (Markdown)**
   - Start from the global template at `skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md`.
   - Default path: `<country>/entities/schools/profiles/<city>/<school-slug>/README.md`.

2) **Structured CSV dataset**
   - One row per school that aligns with the profile metadata.
   - Default path: `<country>/data/entities/schools/<country>-feeder-schools.csv`.

3) **Index/overview (Markdown)**
   - Tiering logic, city coverage, and links to each profile.
   - Default path: `<country>/entities/schools/README.md`.

---

## CSV / data standard

Minimum columns (extend only if the ticket requests):
- `school_id` (stable slug)
- `name_local` and `name_en`
- `city`, `region`
- `school_type` (e.g., language, math-science, international, private, vocational)
- `curricula` (IB DP, Cambridge, AP, national, etc.)
- `languages_of_instruction`
- `priority_tier` (A/B/C or numeric rubric)
- `program_fit_tags` (medicine, cs-data-ai, business, etc.)
- `recommended_outreach_formats` (assembly, workshop, parent-evening, counselor-1to1)
- `visit_window_notes`
- `website_url`
- `contact_email`, `contact_phone` (organizational; no personal mobiles)
- `counselor_email` (only if publicly listed)
- `notes_short`
- `sources` (pipe- or comma-separated URLs)
- `last_verified` (YYYY-MM-DD)

Keep CSV fields and profile front-matter synchronized. Long narrative stays in the profile, not the CSV.

---

## Privacy and data handling

- Prefer role-based or departmental contacts; avoid personal phone numbers or private emails.
- Counselor names may be captured **only if** published on official school channels.
- Never store student data or scrape gated communities.
- Cite every contact/source and record `last_verified` dates.

---

## Profile instructions

- Copy the canonical template from `skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md`.
- Optional YAML front matter may include `school_id`, `city`, `region`, `priority_tier`, and `last_verified` to mirror the CSV.
- Fill sections with actionable recruiting details: access model, visit logistics, counselor notes, and program-fit signals for UNIC Nicosia vs UNIC Athens.

---

## Workflow (canonical)

1) **Scope + seed list**: Confirm cities and tiers with the ticket; gather credible seed lists (official sites, fair participants, known international schools).
2) **Build/refresh the CSV first**: Assign `school_id` slugs, fill required columns, add sources + `last_verified`.
3) **Draft the index**: Summarize tiering logic, city coverage, and link targets for profiles.
4) **Write/update profiles**: One per school using the global template; keep contacts organizational.
5) **Counselor/visit mapping**: Add outreach formats, visit windows, and counselor endpoints to both CSV and profiles.
6) **Quality check**: Ensure profile ↔ CSV consistency, sources cited, and privacy rules met.

---

## Tiering and prioritization (general rubric)

Keep the rubric simple and explicit; document it in the index. Example weighting (0–100 total):
- Outbound orientation / counseling capacity (0–25)
- English intensity or international curriculum alignment (0–25)
- Program fit with priority clusters (Medicine, CS/Data/AI, Business, etc.) (0–20)
- Access and receptivity (published visits, fairs, counselor responsiveness) (0–15)
- City/affluence or pipeline proxy (0–15)

---

## Done checklist

- Profiles exist/updated for scoped schools using the global template.
- CSV fields are complete, sourced, and aligned with profile metadata.
- Index documents tiering logic and links to profiles.
- Privacy constraints are respected; no personal data stored.
- All writing stays inside ticket-allowed paths.
