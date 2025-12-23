# Romania schools — data dictionary

Schema reference for `schools.csv`. This dataset is aligned to the Romania feeder-map capture and is designed to be filterable for outreach and prioritization.

**Delimiter note:** multi-value fields in this dataset use pipe-separated lists (`value1|value2|value3`).

| Field | Description | Type / allowed values | Example |
| --- | --- | --- | --- |
| `school_id` | Stable unique slug (`sch-ro-<place>-<unique>`). Lowercase, ASCII. | string | `sch-ro-bucharest-aisb` |
| `name_en` | Official/common English name of the school. | string | `American International School of Bucharest` |
| `name_local` | Local-language official name (optional). | string | `Școala Germană București` |
| `city` | City/metro where upper secondary is delivered. | string | `Bucharest` |
| `region` | County/metro area for routing. | string | `Ilfov/Bucharest` |
| `school_type` | Category for targeting. | enum: `international`, `private`, `private-romanian`, `faith`, `candidate` | `international` |
| `curriculum` | Primary upper-secondary pathway(s). | pipe-separated list (free text) | `IGCSE|A Level|IB DP` |
| `languages_of_instruction` | Main teaching languages. | pipe-separated list | `English|Romanian` |
| `ownership` | Governance model. | enum: `private`, `foundation`, `faith`, `international-network` | `foundation` |
| `priority_tier` | Tiering rubric (A/B/C). | enum: `A`, `B`, `C` | `A` |
| `affordability_signal` | Tuition/fee signal or description. | string | `€14,200–€18,800 (2025–2026)` |
| `upper_secondary_pathway` | Confirmed or claimed delivery for Years 11–13/DP/KS5. | string | `IB DP` |
| `program_fit_tags` | Target program clusters for outreach. | pipe-separated list; use `medicine`, `business`, `cs-data-ai`, `design-media`, `psychology`, `law`, `multi` | `medicine|business|cs-data-ai` |
| `recruitment_status` | Actionable state for next steps. | enum: `ready`, `verify_fees`, `verify_pathway`, `monitor` | `verify_fees` |
| `website_url` | School website or official page. | string (url) | `https://isb.ro` |
| `contact_email` | Published organizational email(s) for routing (avoid personal emails when possible). | string; pipe-separated if multiple | `admissions@isb.ro` |
| `contact_phone` | Published phone number(s) for routing. | string | `+40 21 210 2131` |
| `notes_short` | Concise operational context (why the school matters; what to verify next). | string | `Premium IB DP provider; confirm counselor contact.` |
| `sources` | Evidence references (URLs or repo paths). | pipe-separated list | `reports/20251220-Romania High-School Feeder Map.md|https://isb.ro` |
| `last_verified` | Date of last verification (UTC, YYYY-MM-DD). | date | `2025-12-21` |
