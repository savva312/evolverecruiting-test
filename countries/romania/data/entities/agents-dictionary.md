# Education agents data dictionary

Schema reference for `agents.csv`. Apply shared standards from `../field-standards.md`.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| agent_id | Stable unique identifier for the agency. | string | `ag-ro-bucharest-integraledu` | Lowercase, ASCII; format `ag-ro-{city}-{slug}`. |
| name | Agency brand name. | string | `IntegralEdu Romania` | Use registered/brand name. |
| tier | Recruiting priority tier. | enum | `tier_1` | `tier_1` (ready), `tier_2` (needs enablement), `tier_3` (pilot/watch). |
| relationship_status | Operational status/action. | enum | `ready_to_activate` | `ready_to_activate`, `training_required`, `pilot_only`, `monitor`. |
| compliance_risk | Quick compliance risk view. | enum | `moderate` | `low`, `moderate`, `high`. |
| hq_city | Main Romanian office city. | string | `Bucharest` | Free text; follow Romanian spellings. |
| coverage_cities | Cities regularly covered (travel/webinars). | multi-enum | `Bucharest;Cluj-Napoca;Iasi;Timisoara` | Semicolon-separated list; order densest cities first. |
| services | Services provided. | multi-enum | `placements;visa_support;events` | Semicolon-separated; examples: `placements`, `visa_support`, `application_editing`, `events`, `test_prep`, `scholarship_guidance`, `accommodation`. |
| primary_markets | Destination markets promoted. | multi-enum | `CY;GR;UK;NL` | Use ISO alpha-2 country codes; semicolon-separated. |
| program_focus | Priority program clusters. | multi-enum | `medicine;business;cs_it` | Semicolon-separated lowercase tags; recommended values: `medicine`, `health_sciences`, `business`, `finance`, `cs_it`, `data_ai`, `design_creative`, `law`, `hospitality`, `aviation`. |
| profile_path | Relative path to the agent profile. | string | `countries/romania/entities/agents/profiles/integraledu-romania.md` | Must point to `.md` profile file. |
| notes | One-line relationship/commercial notes. | string | `Fair engine; ensure GDPR-compliant lead capture.` | Capture enablement steps, risk call-outs, or dependencies. |
| as_of | Snapshot date for the row. | date (YYYY-MM-DD) | `2025-12-22` | Required for all rows; update when materially changing data. |
