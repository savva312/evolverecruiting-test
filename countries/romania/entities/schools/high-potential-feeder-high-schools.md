# High-potential feeder high schools (Romania)

**Sources:** [`20251220-Romania High-School Feeder Map.md`](../../reports/20251220-Romania%20High-School%20Feeder%20Map.md)
**Global reference:** [`skills/schools-and-feeders/SKILL.md`](/skills/schools-and-feeders/SKILL.md) and [`skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md`](/skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md)
**Dataset:** [`romania-high-potential-feeder-high-schools.csv`](../../data/entities/schools/romania-high-potential-feeder-high-schools.csv) (IDs, tiers, pathways, affordability signals, recruitment status, sources)
**Last verified:** 2025-12-21 (all 26 Tier A/B/C profiles live; recruitment statuses and affordability signals aligned to CSV)

## How this list was built
- Pulled exclusively from the **Romania High-School Feeder Map** report, focusing on schools that either (a) charge premium liceu tuition or (b) deliver IB DP/Cambridge Upper Secondary + Advanced (AS/A Levels) pathways.
- Applied the global schools-and-feeders workflow: stable `school_id` slugs, tiering rubric, program-fit tags, `last_verified` dates, and explicit source references. Privacy rules are observed (organizational info only).

### Tiering rubric (aligned to global skill)
- **Tier A (priority now):** Premium private/international liceu with confirmed IB DP or Cambridge AS/A Levels in **Bucharest/Ilfov**, plus the top international operator in **Timișoara**. Clear ability-to-pay and outbound intent signals.
- **Tier B (strong, regional hubs):** Premium/international liceu with verified upper-secondary delivery in **Cluj-Napoca** and **Iași**. Fees or pathways are strong but slightly less dense than Tier A.
- **Tier C (verify then activate):** Single-school cities or lower-fee private liceu that require confirmation of Years 12–13 delivery or updated tuition (Constanța, Brașov area, Oradea; select Bucharest candidates needing validation).

## Priority list (summary by city)
See the CSV for structured fields (school_id, pathway, tier, affordability signal, status, program-fit tags, sources).

### Coverage tracker (aligned to CSV, last_verified 2025-12-21)

**Bucharest/Ilfov (Tier A)**

| School | Tier | Recruitment status | Coverage | Pathway / affordability signal |
| --- | --- | --- | --- | --- |
| [American International School of Bucharest](profiles/sch-ro-bucharest-aisb/README.md) | A | verify_fees | Profile live | IB DP; premium international campus, fees on request. |
| [Cambridge School of Bucharest](profiles/sch-ro-bucharest-csb/README.md) | A | verify_fees | Profile live | IGCSE + A Levels + IB DP; fees shared on request. |
| [International School of Bucharest](profiles/sch-ro-bucharest-isb/README.md) | A | ready | Profile live | IGCSE to IB DP; premium fees (not published). |
| [Mark Twain International School](profiles/sch-ro-bucharest-mtis/README.md) | A | ready | Profile live | IB continuum; 83,985–94,165 RON (Grades 9–12, 2025–2026). |
| [European School of Bucharest](profiles/sch-ro-bucharest-seb/README.md) | A | ready | Profile live | Romanian liceu + IB DP; €14,200–€18,800 (2025–2026). |
| [Lycée Français Anna de Noailles](profiles/sch-ro-bucharest-lycee-francais/README.md) | A | ready | Profile live | French Baccalauréat; €10,150–€11,290 (2025–2026). |
| [Verita International School](profiles/sch-ro-bucharest-verita/README.md) | A | ready | Profile live | IB DP; 71,006 RON DP tuition. |
| [Bucharest-Beirut International School](profiles/sch-ro-bucharest-bbis/README.md) | A | verify_fees | Profile live | IB continuum + Lebanese programme; fees requested. |
| [Genesis College](profiles/sch-ro-bucharest-genesis/README.md) | A | verify_fees | Profile live | Romanian liceu + IB DP; fees on request. |
| [Avenor College](profiles/sch-ro-bucharest-avenor/README.md) | A | verify_fees | Profile live | IGCSE + A Levels; premium fees (confirm schedule). |
| [International Computer High School of Bucharest](profiles/sch-ro-bucharest-ichb/README.md) | A | ready | Profile live | Romanian liceu; €9,400 + €700 enrollment (2025–2026). |
| [Liceul Internațional IOANID](profiles/sch-ro-bucharest-ioanid/README.md) | A | verify_fees | Profile live | Cambridge liceu; €8,825–€10,950 (verify). |
| [Bucharest Christian Academy](profiles/sch-ro-bucharest-bca/README.md) | A | verify_fees | Profile live | US Grades 9–12; tuition on request + published registration/tech fees. |
| [Deutsche Schule Bukarest](profiles/sch-ro-bucharest-deutsche/README.md) | A | verify_fees | Profile live | German Abitur; fees on request. |
| [Maarif International School of Bucharest (candidate)](profiles/sch-ro-bucharest-maarif/README.md) | A | verify_pathway | Profile live (verification) | Candidate liceu; curriculum/fees pending confirmation. |

**Cluj-Napoca (Tier B)**

| School | Tier | Recruitment status | Coverage | Pathway / affordability signal |
| --- | --- | --- | --- | --- |
| [Royal School in Transylvania](profiles/sch-ro-cluj-royal/README.md) | B | verify_fees | Profile live | IGCSE + AS/A Levels; ~€12,330 (verify current schedule). |
| [Transylvania College](profiles/sch-ro-cluj-transylvania/README.md) | B | verify_fees | Profile live | Cambridge IGCSE/AS/A Level; fees on request. |
| [ELF School](profiles/sch-ro-cluj-elf/README.md) | B | verify_fees | Profile live | Romanian liceu; ~28,600 RON/year (reported). |
| [Spectrum International College (Cluj)](profiles/sch-ro-cluj-spectrum/README.md) | B | verify_fees | Profile live | Romanian liceu with Cambridge English prep; fees to verify. |

**Iași metro (Tier B)**

| School | Tier | Recruitment status | Coverage | Pathway / affordability signal |
| --- | --- | --- | --- | --- |
| [Spectrum International College (Iași)](profiles/sch-ro-iasi-spectrum/README.md) | B | ready | Profile live | Romanian liceu + Cambridge English; €4,500/year (2025–2026). |
| [Școala Varlaam Mitropolitul](profiles/sch-ro-iasi-varlaam/README.md) | B | ready | Profile live | Romanian liceu; 22,200 RON/year (2025–2026). |
| [EVISS High School (Valea Adâncă)](profiles/sch-ro-iasi-eviss/README.md) | B | monitor | Profile live | Romanian liceu; ≈1,500 RON/month (2025–2026). |

**Single-school cities and Tier C verifications**

| School | Tier | Recruitment status | Coverage | Pathway / affordability signal |
| --- | --- | --- | --- | --- |
| [British International School of Timișoara](profiles/sch-ro-timisoara-bist/README.md) | A | ready | Profile live | IGCSE + Cambridge KS5 + IB DP; €13,140/year KS5. |
| [Cambridge School of Constanța](profiles/sch-ro-constanta-cambridge/README.md) | C | verify_pathway | Profile live | IGCSE + AS/A Levels (verify onsite); fees on request. |
| [Transylvania International School (Brașov area)](profiles/sch-ro-brasov-transylvania/README.md) | C | monitor | Profile live | Romanian liceu; 1,860 RON (Grades 9–10) + 1,500 RON reg. |
| [International School of Oradea](profiles/sch-ro-oradea-isor/README.md) | C | verify_pathway | Profile live | IGCSE; confirm onsite KS5/A Level delivery. |

## Next actions (per global skill)
1) **Fee verification sprint:** Confirm tuition bands for AISB, CSB, BBIS, Genesis, Avenor, IOANID, BCA, Deutsche Schule, and the four Cluj schools; update `affordability_signal` + `last_verified` in the CSV.
2) **Pathway validation:** Close open questions for Maarif (authorization), Cambridge Constanța (onsite AS/A Levels), and ISOr (KS5 delivery) to move them from `verify_pathway` to `ready/verify_fees`.
3) **Monitor lower-fee entries:** Track EVISS and Brașov Transylvania for XI–XII delivery and counselor contacts before elevating outreach intensity.
4) **Data hygiene:** Keep the CSV in lockstep with profile updates (sources, `recruitment_status`, `last_verified`) and surface any material changes in this coverage tracker.
