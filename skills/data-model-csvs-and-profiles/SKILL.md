---
name: data-model-csvs-and-profiles
description: Global standard for structured CSV datasets and Markdown profiles for recruiting entities, programs, events, and partners with stable IDs, dedupe discipline, and provenance.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: global
---

# Data model: CSVs + Markdown profiles (global)

Every recruiting object should have two complementary artifacts:

1. **Structured data (CSV)** for filtering, deduping, and downstream ops.
2. **Human-readable profiles (Markdown)** for context, judgement, and engagement guidance.

Use this Skill to decide where files live, how to name them, what columns to capture, how to link CSV rows ↔ profiles, and how to update without creating duplicates.

## Core principles

- **Entity-first**: each school, agent, competitor, regulator, exam, or event organizer has one stable `entity_id`, one profile, and one canonical CSV row in the right dataset.
- **Deterministic IDs**: derive IDs from names/slugs (not random sequences) so they can be rebuilt.
- **Single source of truth**: CSVs hold structured fields; profiles hold narrative and operational nuance.
- **Provenance required**: cite sources and maintain `last_verified` dates for material claims.
- **Ticket boundaries win**: only create/edit files inside paths allowed by the active ticket.

## Default locations and naming

### Paths
- **CSV datasets:** `<country>/data/<domain>/<dataset>.csv` (e.g., `<country>/data/entities/schools.csv`). Keep dictionaries next to the CSV (e.g., `schools-dictionary.md`) and reuse shared standards (field-standards) where available.
- **Entity profiles:** `<country>/entities/<type>/profiles/<slug>.md`.
- **Type folders:** common types include `schools`, `agents`, `competitors`, `government-regulators`, `ngos-sgos`, `exams-and-curricula`, and `fairs-events`. Use existing folders; create new ones only if the ticket allows.

### Slug + ID rules
- lowercase, ASCII, hyphen-separated
- remove punctuation; keep short but unique
- align profile filename, slug, and `entity_id`

Examples: `example-international-school`, `central-education-agency`, `spring-student-fair-athens`.

**Profile filename**: `<country>/entities/<type>/profiles/<slug>.md`

**Entity ID (deterministic)**: `<type>__<slug>` (e.g., `school__example-international-school`, `agent__central-education-agency`).

## CSV standards

### Encoding and formatting
- UTF-8
- comma-separated, header row required
- ISO dates: `YYYY-MM-DD`
- booleans: `TRUE` / `FALSE`
- multi-value fields: pipe-delimited `value1|value2|value3`
- keep phone numbers as strings (retain `+`)

### Required meta-columns (every dataset)
- `entity_id`
- `entity_type`
- `canonical_name_en`
- `canonical_name_local`
- `country`
- `city`
- `website`
- `profile_path`
- `status` (`active|inactive|unknown`)
- `confidence` (`high|medium|low`)
- `last_verified` (ISO date)
- `sources` (pipe-delimited URLs)
- `notes_short` (1–2 sentence summary; longer narrative stays in the profile)

### Dedupe rule
Before adding a row, search existing CSVs for exact domain matches, identical/near names, or same city + similar name. If the entity exists, **update** the existing row instead of creating a near-duplicate. If ambiguity remains (e.g., multi-campus structures), prefer a single parent row unless the repo explicitly models sub-entities; document ambiguity in the profile.

## Recommended datasets

Use the columns below in addition to the required meta-columns.

### Schools
- Path: `<country>/data/entities/schools.csv`
- Columns: `school_type` (`public|private|international`), `curricula` (`local|ib|cambridge|us|other`), `grades_served`, `estimated_grade12_size`, `outbound_orientation` (`high|medium|low`), `english_intensity` (`high|medium|low`), `priority_tier` (`A|B|C`), `program_fit_clusters` (pipe list), `counseling_available` (`TRUE|FALSE|unknown`), `primary_contact_name`, `primary_contact_role`, `primary_contact_email`, `visit_policy_link`, `visit_window_notes`.

### Agents
- Path: `<country>/data/entities/agents.csv`
- Columns: `agent_type` (`generalist|medicine-specialist|school-based|other`), `cities_covered` (pipe list), `services` (pipe list), `events_owned` (pipe list), `commission_notes`, `compliance_risk` (`low|medium|high`), `relationship_status` (`target|contacted|contracted|paused|do-not-use`), `primary_contact_name`, `primary_contact_email`, `primary_contact_phone`.

### Competitors
- Path: `<country>/data/entities/competitors.csv`
- Columns: `competitor_type` (`university|faculty|agency|platform`), `country_based`, `city_based`, `program_clusters_competed` (pipe list), `tuition_range_eur`, `selectivity_signal` (`high|medium|low|unknown`), `key_advantages`, `key_disadvantages`.

### Events & fairs
- Path: `<country>/data/entities/events-and-fairs.csv`
- Columns: `event_name`, `organizer_name`, `cities` (pipe list), `timing_pattern` (`spring|autumn|both|unknown`), `typical_months` (pipe list), `website_event_page`, `audience_type` (`students|parents|counselors|mixed`), `estimated_attendance`, `value_to_unic` (`high|medium|low`), `cost_notes`.

### Exams & curricula
- Path: `<country>/data/entities/exams-and-curricula.csv`
- Columns: `exam_or_credential`, `issuer`, `level` (`secondary|language|other`), `relevance`, `timing`, `official_info_link`.

### Programs (UNIC / UNIC Athens)
- Paths often used: `UNIC/programs/programs-unic-nicosia.csv` and `UNIC/programs/programs-unic-athens.csv` (or ticket-specified equivalents).
- Columns: `program_name`, `degree_level` (`ug|pg|other`), `degree_type` (`BSc|BA|MD|MSc|other`), `language_of_instruction`, `duration_years`, `primary_intakes` (pipe list), `tuition_eur_per_year`, `fees_notes`, `admissions_requirements_link`, `cluster` (primary program cluster), `cluster_secondary` (pipe list, optional).

## Profile standards (Markdown)

Use lightweight YAML frontmatter followed by repeatable sections.

```yaml
---
entity_id: school__example-international-school
entity_type: school
canonical_name_en: Example International School
canonical_name_local: Παράδειγμα Διεθνές Σχολείο
country: <Country>
city: <City>
website: https://example.edu
last_verified: 2025-01-15
sources:
  - https://example.edu
---
```

Recommended sections (keep concise):

- **Snapshot** — 5–10 bullet facts (who/where/what; no marketing copy)
- **Why this matters** — short thesis on why it matters for UNIC / UNIC Athens
- **Operational notes** — how to engage, timing, gatekeepers, compliance risks
- **Data points** — high-signal attributes (do not copy the whole CSV)
- **Open questions** — what to verify next
- **Sources** — focused list of URLs
- **Change log** — dated bullet entries (e.g., `2025-01-15: Created; captured counselor email.`)

## Updating workflow (CSV + profile)

1) **Check if it exists**
   - search CSVs by name and domain
   - search profiles by slug/name
2) **If exists → update**
   - refresh `last_verified`, `sources`, and changed fields
   - append to the profile change log
3) **If new → create**
   - create profile with the template above
   - add CSV row with required meta-columns
   - ensure `profile_path` matches the created file

### Sanity checks
- no duplicates
- sources included
- ISO-formatted dates
- consistent pipe-delimited multi-values

### Quality bar
A dataset/profile set is “good” when a human can quickly understand the entity and what to do next, a spreadsheet filter can answer operational questions (e.g., "Tier A Athens schools with IB + strong outbound for Medicine"), key facts are source-backed and time-stamped, and updates do not break IDs or paths.
