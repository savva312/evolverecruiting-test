# Schools

Profiles and data for Nigerian secondary-school feeders that drive UNIC Nicosia and UNIC Athens recruiting. Use together with:
- Global workflow: [`skills/schools-and-feeders/SKILL.md`](../../../../skills/schools-and-feeders/SKILL.md)
- Nigeria guidance: [`countries/nigeria/skills/nigeria-schools-and-feeders/SKILL.md`](../../skills/nigeria-schools-and-feeders/SKILL.md)
- Template: [`skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md`](../../../../skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md)

## December 20, 2025 ingest (Nigeria Premium Secondary School Pipeline)

The entire feeder roster from the December 20, 2025 report has been ingested:
- Source report: [`20251220-Nigeria Premium Secondary School Pipeline.md`](../../reports/20251220-Nigeria%20Premium%20Secondary%20School%20Pipeline.md)
- Coverage: 61 schools across Lagos (20), Abuja (11), Port Harcourt (9), Benin City (2), Ibadan (4), South-East hubs (Awka/Onitsha/Enugu/Nnewi), Delta (Asaba), Kano/Kaduna, and national premium boarders (Jos, Ogun, Osun, Kwara, Akwa Ibom).
- Evidence/tier labels mirror the report’s rubric:
  - **Tier1**: Hard-currency or ultra-premium NGN fees at/above overseas tuition bands.
  - **Tier2A**: High-premium NGN (typically ₦2m+/term) with international pathways.
  - **Tier2B**: Premium NGN with clear international pathways; likely fit for \$10k–\$15k programs.
  - **Tier3-proxy**: Fee opacity; included because of strong Cambridge/IB/AP/boarding signals.
  - Evidence levels: `high`, `medium`, `proxy`, `opaque` (fee on request).

**2025-12-21 sync (T-365):** Deduplicated `schools.csv` back to 61 unique school IDs, regenerated `index.md` from the cleaned roster, refreshed `last_verified`, and reconfirmed counts/tier distribution: Tier1 (11), Tier2A (24), Tier2B (14), Tier3-proxy (12) across 18 cities (Abeokuta, Abuja, Agbara, Asaba, Awka, Benin City, Enugu, Ibadan, Iloko-Ijesa, Jos, Kaduna, Kano, Lagos, Mkpatak, Nnewi, Oko, Onitsha, Port Harcourt).

**2025-12-21 sync (T-274):** Regenerated the navigation index from `schools.csv`, refreshed `last_verified` across all 61 profiled schools, and rechecked alignment between profiles, CSV, and README. Current tier distribution: Tier1 (11), Tier2A (24), Tier2B (14), Tier3-proxy (12). Coverage spans 18 cities (Abeokuta, Abuja, Agbara, Asaba, Awka, Benin City, Enugu, Ibadan, Iloko-Ijesa, Jos, Kaduna, Kano, Lagos, Mkpatak, Nnewi, Oko, Onitsha, Port Harcourt).

## Key assets

- Navigation index: [`index.md`](index.md) — city/tier table linking each profile to the roster
- Data roster (aligned to `schools-dictionary.md`): [`schools.csv`](../../data/entities/schools.csv)
- Schema: [`schools-dictionary.md`](../../data/entities/schools-dictionary.md)
- Profiles: [`profiles/`](profiles/) — one stub per school following the global template, tagged with tier, evidence, fee notes, and open questions.

## How to use

1) Start at `index.md` to browse all high-priority schools by city and tier, then use `schools.csv` to filter by attributes (city, tier, evidence level, program fit).  
2) Open the corresponding profile under `profiles/<city>/<school>/README.md` for outreach notes, risks, and open questions.  
3) Update profiles and CSV together when fees, contacts, or pathways are verified; keep `last_verified` current.  
4) Respect privacy guidance in the global skill (no personal mobiles; prefer role-based contacts).
