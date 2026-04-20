# Competitors data dictionary

Schema reference for `competitors.csv`. Apply shared standards from `../field-standards.md`.

| Field | Description | Type | Sample | Allowed values / notes |
| --- | --- | --- | --- | --- |
| competitor_id | Stable unique identifier for the competitor. | string | `comp-ro-bucharest-carol-davila-university-of-medicine-and-pharmacy` | Lowercase, ASCII; keep stable across datasets (joins to competitor-programs). |
| name | Institution/provider name. | string | `Carol Davila University of Medicine and Pharmacy` | Full brand name. |
| competitor_type | What kind of competitor this row represents. | enum | `university` | Suggested: `university`, `faculty`, `agency`, `platform`, `other`. |
| country | Country where the competitor is based. | string (ISO 3166-1 alpha-2) | `RO` | Uppercase codes. |
| city | City where the competitor is based. | string | `Bucharest` | Free text; use Romanian spellings in English. |
| website | Primary website for the competitor. | string (url) | `https://umfcd.ro/en/` | Use `https://`-prefixed URLs. |
| program_clusters | UNIC recruiting cluster(s) this competitor competes in (Romania taxonomy). | multi-enum | `medicine-and-health` | Semicolon-separated list; use Romania GTM taxonomy: `medicine-and-health`, `computing-data-ai`, `business-economics-finance`, `psychology-and-social-sciences`, `law-and-governance`, `design-and-creative`, `other-strategic-programs` (add new values via ticket only). |
| key_programs | High-level programs that drive competition (not a program price table). | multi-enum | `medicine;dentistry` | Semicolon-separated lowercase tags (free list but keep 2-4); reuse tags such as `medicine`, `dentistry`, `pharmacy`, `law`, `business`, `nursing`. |
| language_of_instruction | Language(s) offered in the competed programs. | multi-enum | `english` | Semicolon-separated; restrict to `english`, `greek`, `romanian`, `french`, `german`, `spanish`, `other`. |
| tuition_min_eur | Lowest annual tuition signal (EUR) for the competed programs. | number | `7500` | Numeric only; per-year unless stated in `tuition_notes`. Leave blank if unknown. |
| tuition_max_eur | Highest annual tuition signal (EUR) for the competed programs. | number | `10000` | Numeric only; per-year unless stated in `tuition_notes`. Leave blank if unknown. |
| tuition_notes | Scope/assumptions for tuition signals (program/language/audience). | string | `International: English Medicine €10,000/year (2025-2026).` | Cite academic year + audience (e.g., "International, English MD 2025-26"); point to the profile for source links. |
| admissions_mechanism | Primary admissions mechanism signal. | enum | `entrance_exam` | Allowed: `entrance_exam` (written/science tests), `file_review` (documents + language check), `interview` (panel-driven), `mixed` (exam + interview/file), `unknown`. |
| selectivity_signal | Quick selectivity signal for funnel modeling. | enum | `high` | `high` (competitive exam/limited seats), `medium` (file review with screens), `low` (open intake), `unknown` (insufficient data); expand nuance inside `notes`. |
| profile_path | Relative path to the competitor profile. | path | `countries/romania/entities/competitors/profiles/ovidius-university-of-constanta.md` | Must point to an existing `.md` file. |
| notes | One-line positioning/pricing/admissions takeaways for recruiters. | string | `Value-priced English MD/DDS; file-based admission; price anchor vs UNIC.` | Keep concise; put full detail in the profile. |
| as_of | Snapshot date for the row. | date (YYYY-MM-DD) | `2025-12-22` | Required for all rows. |
