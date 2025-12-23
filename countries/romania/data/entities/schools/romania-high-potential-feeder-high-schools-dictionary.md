# Romania high-potential feeder high schools — data dictionary

Follows the global schools-and-feeders skill. Values are derived from `countries/romania/reports/20251220-Romania High-School Feeder Map.md`. Sources should remain organizational (no personal data) and include `last_verified` dates.

| Field | Description | Type / allowed values | Example |
| --- | --- | --- | --- |
| `school_id` | Stable slug (`sch-ro-<city>-<unique>`). Lowercase, ASCII. | string | `sch-ro-bucharest-aisb` |
| `name_en` | Official/common English name of the school. | string | `American International School of Bucharest` |
| `city` | City/metro where upper secondary is delivered. | string | `Bucharest` |
| `region` | County/metro area for routing. | string | `Ilfov/Bucharest` |
| `school_type` | Category for targeting. | enum: `international`, `private`, `private-romanian`, `faith`, `candidate` | `international` |
| `curriculum` | Primary upper-secondary pathway(s). | pipe-separated list | `IB DP` / `Cambridge IGCSE|A Levels` / `French lycée` |
| `languages_of_instruction` | Main teaching languages. | pipe-separated list | `English` / `French|English` |
| `ownership` | Governance model. | enum: `private`, `foundation`, `faith`, `international-network`, `candidate` | `international-network` |
| `priority_tier` | Tiering rubric (A/B/C). | enum: `A`, `B`, `C` | `A` |
| `affordability_signal` | Tuition/fee signal or description. | string | `€14,200-18,800 (2025-2026)` |
| `upper_secondary_pathway` | Confirmed or claimed delivery for Years 11–13/DP/KS5. | string | `IB DP`; `IGCSE + AS/A Level`; `French lycée (Terminale)` |
| `program_fit_tags` | Target programs for outreach. | pipe-separated list; use `medicine`, `business`, `cs-data-ai`, `design-media`, `psychology`, `law`, `multi` | `medicine|business|cs-data-ai` |
| `recruitment_status` | Actionable state. | enum: `ready`, `verify_fees`, `verify_pathway`, `monitor` | `verify_pathway` |
| `notes_short` | One-line context on why the school is included. | string | `Premium IB DP provider; high outbound intent.` |
| `sources` | Evidence references (URLs or repo paths). | pipe-separated | `reports/20251220-Romania High-School Feeder Map.md` |
| `last_verified` | Date of last verification (UTC, YYYY-MM-DD). | date | `2025-12-20` |

Keep the CSV synchronized with this dictionary and the narrative summary. Update `last_verified` and `recruitment_status` as tuition/pathway confirmations are refreshed.
