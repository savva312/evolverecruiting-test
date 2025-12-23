# Jordan Outbound Mobility Baseline

## Produced by: UNIC Evolve, December 20, 2025 (updated 2026-02-04 for data-status clarity)

# 1. Executive summary

## What is confirmed right now
- **Provisional global outbound:** **33,277 Jordan tertiary students abroad (2022)** cited by the U.S. International Trade Administration (attributed to UNESCO). Treat this as a placeholder until a direct UNESCO UIS extract is pulled. 
- **Host-specific proof point:** **2,643 Jordanian students in the United States (2023/24)** with a graduate-leaning mix (Open Doors). Use this as a directional benchmark for postgraduate appetite while broader host data is gathered.
- **Methodological anchor:** Degree-mobile students; origin determined by prior education/usual residence. Keep origin-side (UIS) and host-side sources labeled separately.

## What is *not* yet evidenced (critical gaps)
- **Eurostat:** The `educ_uoe_mobs02` API currently returns **no observations for partner=Jordan (2023)**—the value array is empty despite the structure listing reporting geos. Any prior Eurostat-style tables are therefore **unsupported** and must be rebuilt once a valid extract exists.
- **UIS outbound + destination ranks:** No direct UNESCO UIS pull has been completed in this repo. The ITA citation must be validated or replaced with an official UIS extract (latest year available).
- **Field-of-study splits:** No field-level distribution is captured; current program guidance relies on proxies from agents/schools and the U.S. Open Doors sample.
- **Greece/Cyprus corridor visibility:** No official counts are available yet. Visa/residence data and agent CRM conversions need to be used until host-side statistics surface.

## Immediate actions to reach a defensible baseline
1. **Run the UIS extraction** for Jordan outbound totals and Top destinations (latest year), capturing Greece and Cyprus explicitly. Document API queries and summation logic in this report and in `countries/jordan/market/outbound-mobility.md`.
2. **Retry Eurostat** once coverage for partner=Jordan is confirmed. If the dataset continues to return no observations, log that limitation and pivot to host-country sources for EU corridors.
3. **Collect host-side stats for priority markets**: U.S. (Open Doors – already cited), Türkiye (YÖK/ÖSYM), Germany (DESTATIS/DAAD), UK (HESA), KSA/UAE (visa/student permit releases), and any Greek/Cypriot residence-permit data. Add extracts or citations in an appendix.
4. **Add field splits where available** (Open Doors fields, DAAD subject tables, UK CAH/HECoS) to move program guidance from proxy to evidence-backed.
5. **Track interim operational signals** via agents/schools (premium West Amman, King’s Academy) and campaign performance data to inform targeting while official statistics are assembled.

# 2. Outbound volumes and destination structure (status)

| Component | Status | Notes/next step |
| --- | --- | --- |
| UNESCO UIS outbound total + Top destinations | **Missing** | Pull latest UIS tables; replace ITA citation once verified. |
| Eurostat `educ_uoe_mobs02` (ED5–8, partner=Jordan, 2023) | **No data returned** | API call on 2026-02-04 returned an empty `value` object; retry when Eurostat updates coverage. |
| Greece/Cyprus corridor counts | **Missing** | Use visa/residence data and agent CRM until official stats are available. |
| Host-side stats (US, TR, DE, UK, KSA, UAE) | **Partial** | US Open Doors included; others to be extracted and cited. |
| Field-of-study splits | **Missing** | Add from host datasets where available (US/DE/UK first). |

## Current directional picture (qualitative)
- **Primary gravity:** U.S., UK, Canada, Australia, Germany, and Türkiye remain core destinations per agent/counselor feedback; Gulf scholarships attract cost-sensitive families.
- **Postgraduate/STEM tilt:** Agents report strong demand for postgraduate STEM/data/business; medicine/dentistry interest is high but constrained by licensure/placement requirements.
- **Premium affordability pockets:** West Amman schools and King’s Academy show the clearest ability to pay €10k–€27k/year; Irbid/Aqaba segments are more price-sensitive and scholarship-dependent.

## Guidance for Greece/Cyprus positioning (until counts land)
- Lead with **transparent pricing + JOD/EUR equivalents** and publish scholarship grids (10–30% merit, stackable family/early-payment where allowed).
- Emphasise **recognition/licensure clarity** for health programs and **STEM employability** for Athens; use Nicosia when students want the established campus or online/hybrid flexibility.
- Track corridor performance via **agent CRM + visa/residence proxies** and update once official stats are pulled.

## Changelog
- **2026-02-04:** Marked Eurostat data as unavailable, added UIS/host-side extraction plan, aligned operational guidance to qualitative signals only.
