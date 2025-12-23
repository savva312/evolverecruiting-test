---
name: id-governance
description: Deterministic ID specification and minting workflow for recruiting entities, partners, and events across markets.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: global
---

# Deterministic ID governance (global)

Use this skill to mint deterministic IDs that survive renames, dedupe cleanly across markets, and stay traceable back to their source data.

## Format

- **Pattern:** `<cc>_<kind>_<slug>__<hash>`
- **`cc`:** lowercase ISO 3166-1 alpha-2 for the entity’s anchor country (e.g., `bg`, `ng`, `gr`). Use `xx` only for global records with no single-country anchor.
- **`kind`:** controlled list (see below).
- **`slug`:** normalized slug that humans can recognize (see normalization).
- **`hash`:** 10-character lowercase base32 (no padding) from the hash method below.

## Controlled kinds

- `school`
- `agent`
- `event`
- `competitor`
- `regulator`
- `ngo-sgo`
- `exam`
- `program`
- `campus`
- `scholarship`
- `funnel-action` (application, offer, enrollment checkpoints when explicitly ticketed)

## Normalization rules (slug + canonical string inputs)

- Lowercase ASCII; strip diacritics and non-ASCII characters.
- Replace `&` with `and`; remove punctuation except hyphens.
- Collapse whitespace/underscores to single hyphens; trim leading/trailing hyphens.
- Keep slugs concise; include city/campus qualifiers only when needed for clarity.
- For canonical string inputs, trim whitespace, lowercase, and use `-` (single dash) for unknown values.

## Canonical inputs by kind (order matters)

Build the canonical string by joining with `|`: `[cc, kind, slug, inputs...]`.

- `school`: `canonical_name_en`, `city`, `website_domain`
- `agent`: `canonical_name_en`, `hq_city_or_region`, `website_domain`
- `event`: `event_name`, `organizer_name`, `anchor_city_or_country`, `timing_pattern` (e.g., `october`, `spring`)
- `competitor`: `canonical_name_en`, `country`, `primary_cluster_or_degree_level`
- `regulator`: `authority_name`, `country`, `scope` (e.g., `higher-ed`, `scholarships`)
- `ngo-sgo`: `org_name`, `country`, `focus_area` (e.g., `youth`, `stem`)
- `exam`: `exam_name`, `issuer`, `country`
- `program`: `campus` (`unic-nicosia|unic-athens`), `program_name`, `degree_level`
- `campus`: `campus_name`, `city`, `country`
- `scholarship`: `scholarship_name`, `country`, `audience` (`ug|pg|mixed`)
- `funnel-action`: `action_name`, `program_or_segment`, `step` (`applied|offer|deposit|enrolled`)

## Hash method

1) Normalize inputs using the rules above.  
2) Build the canonical string: `cc|kind|slug|<input1>|<input2>|...`.  
3) Compute `sha256(canonical_string)`, base32-encode the digest (lowercase, no padding), and take the first 10 characters.  
4) Final ID: `<cc>_<kind>_<slug>__<hash>`.

## How to mint (checklist)

1. Confirm the entity fits a controlled `kind`; if not, stop and request a new ticket to extend the list.
2. Gather canonical inputs for that `kind` (table above); prefer official names/domains over social handles.
3. Normalize the slug from the canonical English name (add city/campus only if needed for clarity).
4. Build the canonical string in the documented order; use `-` for unknown fields.
5. Hash the canonical string (sha256 → base32 → first 10 chars) and assemble the ID.
6. **Dedupe check:** search for the slug, canonical string pieces (name + city/domain), or existing `<kind>` IDs in CSVs/profiles. Reuse an existing ID if the canonical inputs match.
7. Record the final ID in both CSV rows and profile frontmatter; do not change it once minted unless a duplicate is being collapsed.

### CLI helper (Python, `scripts/id_minter.py`)

- **Dependencies:** Python 3.10+; install `pyyaml` for YAML/frontmatter support: `pip install pyyaml`.
- **Mint:** `python scripts/id_minter.py mint path/to/entity.yml --show-canonical [--kind school] [--country bg] [--slug override] [--json]`  
  - Refuses to remint when `entity_id` already exists in the source metadata.  
  - `--show-canonical` prints the canonical string the hash was derived from; `--json` emits a machine-readable payload for pipelines.
- **Lint:** `python scripts/id_minter.py lint [--country bulgaria --country nigeria] [--repo-root /path/to/repo]`  
  - Flags duplicate canonical keys or domains, missing `profile_path`, and CSV ↔ profile `entity_id` mismatches.  
  - Add to pre-commit/CI to keep registries deduped.

## Dedupe policy

- One ID per real-world entity/event per country anchor; campuses or distinct legal entities get their own IDs.
- Before minting, search across the repo for matching names/domains/cities. If a match exists, update that record instead of minting a new one.
- If two minted IDs are duplicates, keep the oldest, mark the duplicate as an alias in notes, and redirect links to the surviving ID.
- Hash collisions are unlikely with 10 base32 characters; if one occurs, extend the hash to 14 characters for the conflicting pair and document the override in the profile change log.

## When not to mint

- Lead lists or unverified names with no city/domain evidence.
- One-off interactions (e.g., a single email contact) without clarity that an organization exists.
- Pure marketing campaigns or temporary event concepts without a scheduled instance.
- Work that falls outside the active ticket’s allowed paths or controlled `kind` list.

## Examples

- **School (BG, American College of Sofia)**  
  - Canonical string: `bg|school|american-college-of-sofia|american college of sofia|sofia|acs.bg`  
  - ID: `bg_school_american-college-of-sofia__ej3ooazdgz`
- **Agent (NG, EduBridge Lagos)**  
  - Canonical string: `ng|agent|edubridge-lagos|edubridge lagos|lagos|edubridgelagos.com`  
  - ID: `ng_agent_edubridge-lagos__anq5bq43xa`
- **Event (GR, Athens International Education Fair by CIEET, October)**  
  - Canonical string: `gr|event|athens-international-education-fair|athens international education fair|cieet|athens|october`  
  - ID: `gr_event_athens-international-education-fair__ymw42ml2jq`
