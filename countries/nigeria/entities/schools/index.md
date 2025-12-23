# Nigeria high-priority schools index

Last synced: 2025-12-21 (Ticket: T-365).

This index ties every high-priority Nigerian secondary school profile to the structured roster so CSV, README, and profiles stay in lockstep.

## Snapshot

- Coverage: 61 profiles across 18 cities (Abeokuta, Abuja, Agbara, Asaba, Awka, Benin City, Enugu, Ibadan, Iloko-Ijesa, Jos, Kaduna, Kano, Lagos, Mkpatak, Nnewi, Oko, Onitsha, Port Harcourt).
- Tier distribution: Tier1 (11), Tier2A (24), Tier2B (14), Tier3-proxy (12).
- Sources: `schools.csv` (authoritative roster) + `profiles/**` (qualitative detail). See `../../data/entities/schools.csv` for structured fields and `last_verified` (synced 2025-12-21).

## How to use

- Filter the table by city/tier to target outreach runs.
- Click a school link to open its profile; update the profile and `schools.csv` together when fees/pathways change, and refresh `last_verified`.
- If you add a new profile, insert the row in `schools.csv` and regenerate this table from the CSV to keep navigation current.

## Roster (sorted by city, then tier)

| City | School | Tier | Evidence | Model | Curricula | Last verified |
| --- | --- | --- | --- | --- | --- | --- |
| Abeokuta | [Day Waterman College](profiles/abeokuta/day-waterman-college/README.md) | Tier2A | medium | boarding | british;cambridge-igcse;a-levels | 2025-12-21 |
| Abuja | [American International School of Abuja (AISA)](profiles/abuja/american-international-school-of-abuja-aisa/README.md) | Tier1 | medium | day | american;ap | 2025-12-21 |
| Abuja | [International Community School (ICS) Abuja](profiles/abuja/international-community-school-ics-abuja/README.md) | Tier1 | medium | day | american;cambridge-igcse | 2025-12-21 |
| Abuja | [Lycée Français Marcel-Pagnol d’Abuja (LFMPA)](profiles/abuja/lyc-e-fran-ais-marcel-pagnol-d-abuja-lfmpa/README.md) | Tier1 | high | day | french-bac | 2025-12-21 |
| Abuja | [El-Amin International School Abuja](profiles/abuja/el-amin-international-school-abuja/README.md) | Tier2A | medium | day | british | 2025-12-21 |
| Abuja | [Funtaj International School (Abuja campuses)](profiles/abuja/funtaj-international-school-abuja-campuses/README.md) | Tier2A | opaque | day+boarding | premium | 2025-12-21 |
| Abuja | [Lead British International School (LBIS) Abuja](profiles/abuja/lead-british-international-school-lbis-abuja/README.md) | Tier2A | medium | day+boarding | british;cambridge-igcse;a-levels | 2025-12-21 |
| Abuja | [The Centagon International School](profiles/abuja/the-centagon-international-school/README.md) | Tier2A | opaque | day | british | 2025-12-21 |
| Abuja | [The Regent Secondary School Abuja](profiles/abuja/the-regent-secondary-school-abuja/README.md) | Tier2A | medium | day+boarding | british;cambridge-igcse | 2025-12-21 |
| Abuja | [British Nigerian Academy (BNA)](profiles/abuja/british-nigerian-academy-bna/README.md) | Tier2B | medium | day+boarding | ib;british | 2025-12-21 |
| Abuja | [Nigerian Tulip International College (NTIC) Abuja](profiles/abuja/nigerian-tulip-international-college-ntic-abuja/README.md) | Tier2B | medium | day | cambridge-igcse;a-levels | 2025-12-21 |
| Abuja | [Whiteplains British School (WBS)](profiles/abuja/whiteplains-british-school-wbs/README.md) | Tier2B | medium | day+boarding | british;cambridge-igcse | 2025-12-21 |
| Agbara | [Corona Secondary School (Agbara)](profiles/agbara/corona-secondary-school-agbara/README.md) | Tier2A | medium | boarding | british;cambridge-igcse;a-levels | 2025-12-21 |
| Asaba | [Patricia High School (Patricia Group)](profiles/asaba/patricia-high-school-patricia-group/README.md) | Tier3-proxy | proxy | day | cambridge-igcse;cambridge-as;ossd | 2025-12-21 |
| Awka | [British Spring College](profiles/awka/british-spring-college/README.md) | Tier2B | medium | day+boarding | cambridge-igcse;a-levels | 2025-12-21 |
| Benin City | [Igbinedion Education Centre (IEC)](profiles/benin-city/igbinedion-education-centre-iec/README.md) | Tier2B | medium | day+boarding | cambridge-igcse | 2025-12-21 |
| Benin City | [University of Benin Preparatory Secondary School (UPSS)](profiles/benin-city/university-of-benin-preparatory-secondary-school-upss/README.md) | Tier2B | medium | day | nigerian | 2025-12-21 |
| Enugu | [Adorable British College](profiles/enugu/adorable-british-college/README.md) | Tier3-proxy | medium | boarding | cambridge-igcse | 2025-12-21 |
| Ibadan | [Christ Ambassadors International College (CAIC)](profiles/ibadan/christ-ambassadors-international-college-caic/README.md) | Tier2B | high | day+boarding | british;cambridge-igcse | 2025-12-21 |
| Ibadan | [Lifeforte International High School](profiles/ibadan/lifeforte-international-high-school/README.md) | Tier2B | medium | boarding | british;cambridge-igcse | 2025-12-21 |
| Ibadan | [Ibadan International School (IIS)](profiles/ibadan/ibadan-international-school-iis/README.md) | Tier3-proxy | opaque | day | cambridge-igcse | 2025-12-21 |
| Ibadan | [The International School, University of Ibadan (ISI)](profiles/ibadan/the-international-school-university-of-ibadan-isi/README.md) | Tier3-proxy | opaque | day | a-levels;cambridge-igcse | 2025-12-21 |
| Iloko-Ijesa | [Olashore International School](profiles/iloko-ijesa/olashore-international-school/README.md) | Tier2A | proxy | boarding | british;cambridge-igcse | 2025-12-21 |
| Jos | [Hillcrest School](profiles/jos/hillcrest-school/README.md) | Tier1 | high | day | american;international | 2025-12-21 |
| Kaduna | [Essence International School](profiles/kaduna/essence-international-school/README.md) | Tier3-proxy | proxy | unknown | international | 2025-12-21 |
| Kaduna | [Kadwel International Schools](profiles/kaduna/kadwel-international-schools/README.md) | Tier3-proxy | proxy | boarding | british;sixth-form | 2025-12-21 |
| Kaduna | [Zamani College](profiles/kaduna/zamani-college/README.md) | Tier3-proxy | proxy | unknown | cambridge-igcse;a-levels | 2025-12-21 |
| Kano | [Lebanese Consulate International School Kano (LCISK)](profiles/kano/lebanese-consulate-international-school-kano-lcisk/README.md) | Tier3-proxy | proxy | day+boarding | cambridge-igcse;cambridge-as;a-levels | 2025-12-21 |
| Lagos | [American International School of Lagos (AISL)](profiles/lagos/american-international-school-of-lagos-aisl/README.md) | Tier1 | medium | day | american;ib-dp | 2025-12-21 |
| Lagos | [British International School, Lagos (BIS)](profiles/lagos/british-international-school-lagos-bis/README.md) | Tier1 | medium | day+boarding | british;cambridge-igcse;as-levels;a-levels | 2025-12-21 |
| Lagos | [Charterhouse Lagos](profiles/lagos/charterhouse-lagos/README.md) | Tier1 | high | day+boarding | british;cambridge-igcse;a-levels | 2025-12-21 |
| Lagos | [Children’s International School (CIS)](profiles/lagos/children-s-international-school-cis/README.md) | Tier1 | opaque | day+boarding | british;cambridge-igcse;a-levels | 2025-12-21 |
| Lagos | [Lekki British School (High School)](profiles/lagos/lekki-british-school-high-school/README.md) | Tier1 | opaque | day+boarding | british;cambridge-igcse;a-levels | 2025-12-21 |
| Lagos | [Lycée Français Louis Pasteur](profiles/lagos/lyc-e-fran-ais-louis-pasteur/README.md) | Tier1 | high | day | french-bac | 2025-12-21 |
| Lagos | [Rugby School Nigeria](profiles/lagos/rugby-school-nigeria/README.md) | Tier1 | medium | day+boarding | british;cambridge-igcse;a-levels | 2025-12-21 |
| Lagos | [Atlantic Hall School](profiles/lagos/atlantic-hall-school/README.md) | Tier2A | medium | day+boarding | nigerian;international-exams | 2025-12-21 |
| Lagos | [Caleb British International School](profiles/lagos/caleb-british-international-school/README.md) | Tier2A | opaque | day+boarding | british;cambridge-igcse;sat | 2025-12-21 |
| Lagos | [Dowen College](profiles/lagos/dowen-college/README.md) | Tier2A | opaque | day+boarding | nigerian;international-exams | 2025-12-21 |
| Lagos | [Emerald Schools](profiles/lagos/emerald-schools/README.md) | Tier2A | opaque | day | british;cambridge-igcse | 2025-12-21 |
| Lagos | [Grange School](profiles/lagos/grange-school/README.md) | Tier2A | opaque | day | british;cambridge-igcse | 2025-12-21 |
| Lagos | [Greensprings School (Lekki campus IB DP year)](profiles/lagos/greensprings-school-lekki-campus-ib-dp-year/README.md) | Tier2A | medium | day+boarding | ib-dp | 2025-12-21 |
| Lagos | [Grenville Schools](profiles/lagos/grenville-schools/README.md) | Tier2A | opaque | day+boarding | british;cambridge-igcse | 2025-12-21 |
| Lagos | [Lagos Preparatory & Secondary School (LPSS)](profiles/lagos/lagos-preparatory-secondary-school-lpss/README.md) | Tier2A | medium | day | british;cambridge-igcse | 2025-12-21 |
| Lagos | [Meadow Hall (College section)](profiles/lagos/meadow-hall-college-section/README.md) | Tier2A | opaque | day | british;cambridge-igcse | 2025-12-21 |
| Lagos | [Oxbridge Tutorial College](profiles/lagos/oxbridge-tutorial-college/README.md) | Tier2A | opaque | day | a-levels;sixth-form | 2025-12-21 |
| Lagos | [Rainbow College (day campuses)](profiles/lagos/rainbow-college-day-campuses/README.md) | Tier2A | opaque | day | nigerian;british-blend | 2025-12-21 |
| Lagos | [Temple School (Secondary/College)](profiles/lagos/temple-school-secondary-college/README.md) | Tier2A | opaque | day | british;cambridge-igcse | 2025-12-21 |
| Lagos | [Vivian Fowler Memorial College for Girls](profiles/lagos/vivian-fowler-memorial-college-for-girls/README.md) | Tier2A | opaque | unknown | british;cambridge-igcse | 2025-12-21 |
| Mkpatak | [Topfaith International Secondary School](profiles/mkpatak/topfaith-international-secondary-school/README.md) | Tier2B | high | boarding | cambridge-igcse | 2025-12-21 |
| Nnewi | [St Mikel’s International Schools](profiles/nnewi/st-mikel-s-international-schools/README.md) | Tier3-proxy | medium | day+boarding | british | 2025-12-21 |
| Oko | [Thomas Adewumi International College (TAICO)](profiles/oko/thomas-adewumi-international-college-taico/README.md) | Tier3-proxy | proxy | boarding | british;international | 2025-12-21 |
| Onitsha | [Grundtvig International Secondary School](profiles/onitsha/grundtvig-international-secondary-school/README.md) | Tier2B | medium | boarding | cambridge-igcse | 2025-12-21 |
| Port Harcourt | [Charles Dale Memorial International School](profiles/port-harcourt/charles-dale-memorial-international-school/README.md) | Tier2A | medium | boarding | international;cambridge-igcse | 2025-12-21 |
| Port Harcourt | [Graceland International School](profiles/port-harcourt/graceland-international-school/README.md) | Tier2A | opaque | day+boarding | cambridge-igcse | 2025-12-21 |
| Port Harcourt | [Royalcourt Private School](profiles/port-harcourt/royalcourt-private-school/README.md) | Tier2A | medium | boarding | premium | 2025-12-21 |
| Port Harcourt | [Crestbridge International School (College section)](profiles/port-harcourt/crestbridge-international-school-college-section/README.md) | Tier2B | medium | day | international | 2025-12-21 |
| Port Harcourt | [Greenoak International School (Secondary)](profiles/port-harcourt/greenoak-international-school-secondary/README.md) | Tier2B | medium | day+boarding | international | 2025-12-21 |
| Port Harcourt | [Jephthah Comprehensive Secondary School](profiles/port-harcourt/jephthah-comprehensive-secondary-school/README.md) | Tier2B | medium | day+boarding | cambridge-igcse;us-tests | 2025-12-21 |
| Port Harcourt | [Norwegian International School (NIS) Port Harcourt](profiles/port-harcourt/norwegian-international-school-nis-port-harcourt/README.md) | Tier2B | medium | day+boarding | cambridge-igcse;a-levels | 2025-12-21 |
| Port Harcourt | [St Maria Goretti’s School](profiles/port-harcourt/st-maria-goretti-s-school/README.md) | Tier3-proxy | opaque | unknown | cambridge-igcse | 2025-12-21 |
| Port Harcourt | [Starlets Academy](profiles/port-harcourt/starlets-academy/README.md) | Tier3-proxy | opaque | boarding | international-exams | 2025-12-21 |
