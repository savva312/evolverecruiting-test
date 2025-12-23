---
name: competitors
description: Global workflow for documenting competitor institutions, linking their home-base profiles to cross-country competitive presence, and standardizing profile templates.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: global
license: Proprietary (UNIC Evolve internal)
---

# Skill: Competitors (global)

## Purpose

Build consistent competitor intelligence across markets by:
- Creating a **home/base profile** in the country where the university (or branch campus) operates.
- Capturing **cross-country competitive presence** so each market’s list includes both local institutions and strong foreign entrants.
- Applying a repeatable **competitor profile template** with pricing, positioning, and sourcing standards.

Use this skill together with:
- `/skills/program-clusters-and-competitor-sets/SKILL.md` (cluster-level competitor sets)
- `/skills/data-model-csvs-and-profiles/SKILL.md` (CSV + profile metadata standards)
- `/skills/id-governance/SKILL.md` (stable `competitor_id` and slugs)
- `/skills/markdown-authoring/SKILL.md` (formatting + sourcing)

---

## When to use this skill

- A ticket asks for competitor research, profiles, or competitor CSV updates in a given country.
- A competitor from **another country** has meaningful share in the target market and needs to be reflected in that country’s list.
- You need to link a competitor profile to program-cluster competitor sets without duplicating content across countries.

---

## Core concepts

1) **Home/base profile** — The canonical profile that lives in the competitor’s operating country (main campus or branch). It holds identity, accreditation, pricing, admissions, and channel signals. Create or update it **only if the ticket allows writing in that country path**; otherwise log the need in `/executions/` and cite the existing profile if available.

2) **Cross-country competitive presence** — Each country maintains its own competitor roster (and cluster-specific lists) that **pulls from both local institutions and foreign competitors**. Reference the home/base profile via relative link and summarize why it matters locally (overlap to UNIC/UNIC Athens, observed marketing, channels).

3) **Competitor profile document** — The reusable template for describing the competitor itself. Use the same structure whether the competitor is local or foreign; keep pricing, positioning, and sources current.

---

## Storage layout (default paths)

- **Home/base profile**: `<home_country>/entities/competitors/profiles/<institution-slug>.md`.
- **Country competitor roster/index**: `<country>/entities/competitors/README.md` (overview, priorities, and links to relevant profiles—even if the profile lives in another country folder).
- **Program-cluster lists**: `<country>/program-clusters/<cluster>/competitors.md` for cluster-specific competitive sets (link back to profiles instead of rewriting).
- **Structured data**: `<country>/data/entities/competitors.csv` aligned to `skills/data-model-csvs-and-profiles` (`competitor_type`, `country_based`, `city_based`, `program_clusters_competed`, `tuition_range_eur`, `selectivity_signal`, `key_advantages`, `key_disadvantages`, `last_verified`, `sources`).
- **Evidence of presence**: brief notes or links in the roster/cluster files capturing tactics (agents, fairs, ads, scholarships) observed in the target country.

Respect ticket allowed paths. If you need a home/base profile outside scope, leave a TODO in `/executions/` and reference existing intel without writing out-of-scope files.

---

## Inputs to gather (minimum viable)

- **Identity**: official English name, country/city of main campus or branch, website, ownership/governance, recognition/licensure status.
- **Programs & delivery**: flagship programs, language of instruction, delivery locations (campus/online), intakes.
- **Pricing & aid**: published tuition/fees (local currency + EUR), deposit/instalments, scholarships or discounts that shift effective price.
- **Admissions signals**: entry requirements (tests, GPA, interviews/portfolio), selectivity cues.
- **Positioning vs UNIC/UNIC Athens**: how it competes in the target market (program overlap, price/brand leverage, proximity).
- **Channels & presence**: agents/partners, fairs/events, paid media, school visits, articulation pathways used to recruit in the target country.
- **Sources + recency**: URLs and `last_verified` dates for every claim.

---

## Workflow

1) **Confirm scope + IDs**
   - Read the ticket for allowed paths and required outputs.
   - Mint/confirm `competitor_id` using `/skills/id-governance/SKILL.md`; keep slugs consistent across CSVs and profiles.

2) **Check for an existing home/base profile**
   - Search the competitor’s home country folder for an existing profile. If found, reuse and update instead of duplicating.
   - If missing and the ticket allows writing in that country, create the base profile in the home country path. If not allowed, log the gap in `/executions/` and proceed with cross-country notes using the available intel.

3) **Document cross-country competitive presence in the target market**
   - Update the target country’s `entities/competitors/README.md` with a short entry summarizing why the competitor matters locally (program overlap, observed marketing, pricing angle) and link to the base profile.
   - If the ticket covers program clusters, add the competitor to the relevant `<country>/program-clusters/<cluster>/competitors.md` list with cluster-specific rationale.
   - Include both **local competitors** and **foreign competitors** with active presence; avoid “local only” lists.

4) **Author or refresh the competitor profile (home/base)**
   - Use the template below; keep pricing and admissions evidence-based with citations and `last_verified`.
   - Note branch locations and whether the profiled campus is the main one or a transnational/offshore site.
   - Capture any country-specific offers or scholarships driving cross-country competition.

5) **Sync structured data**
   - Update `<country>/data/entities/competitors.csv` for the target market with the competitor’s row (one per institution per country presence). Align fields with the profile and include `sources` + `last_verified`.
   - If you created/updated the home profile in a different country, sync that country’s competitor CSV as well (only if allowed by the ticket scope).

6) **Quality check**
   - Verify profile ↔ CSV consistency (tuition ranges, program clusters, selectivity signals).
   - Ensure every claim has a source and a `last_verified` date; avoid speculative positioning.
   - Confirm links to UNIC program pages instead of duplicating program descriptions.
   - Re-read the ticket’s acceptance criteria and `/skills/markdown-authoring/SKILL.md` for formatting.

---

## Competitor profile template (markdown)

Use this structure inside `<country>/entities/competitors/profiles/<slug>.md` (adapt only if the ticket provides a country-specific template):

```
# <Institution name>

last_verified: YYYY-MM-DD
website: <https://example.edu>

## Snapshot
- What the institution is (public/private; main campus or branch), main teaching languages, and headline programs.

## Pricing and scholarships
- Published tuition/fees (local currency + EUR), deposits/instalments, typical aid/scholarship levers.

## Admissions and selectivity
- Entry requirements (tests, GPA/grade bands, interviews/portfolio) and any visible selectivity signal.

## Presence in <target country>
- Evidence of recruiting in the target country (agents, fairs, school visits, paid media), and the program clusters where it competes.

## Positioning vs UNIC / UNIC Athens
- Overlaps and differentiators (price, brand, delivery mode, proximity, recognition).

## Sources
- Bulleted sources with URLs supporting each claim above.
```

Keep sections concise; longer narratives belong in cluster pages, not in the base profile.

---

## Done checklist

- Competitor has a **home/base profile** or the gap is logged in `/executions/` when out-of-scope.
- Target country roster and relevant cluster competitor lists include both local and foreign competitors, with links back to base profiles.
- CSV rows are updated for every country presence covered by the ticket, matching profile metadata and `competitor_id` slugs.
- Pricing, positioning, channels, and sources are cited with `last_verified` dates.
- All edits stay within the ticket’s allowed paths and follow markdown/ID governance standards.
