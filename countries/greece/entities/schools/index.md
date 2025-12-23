# Greece school affordability extraction index

Source report: `countries/greece/reports/20251221-Greek High Schools for UNIC Affordability.md` (extracted via T-300 on 2025-12-21).

## How to use this index
- Profiles: one ticket per school (T-301–T-355) uses the global high school profile template.
- Data: `countries/greece/data/entities/schools.csv` stores structured fields for every school in the report.
- Aggregation: T-356 updates this index, README, and CSV after profile work is delivered.
- Tiering: Tier 1 = published high fees/premium international; Tier 2 = international pathway with unclear fees or special programs; Tier 3 = broader private Lyceum coverage requiring screening.

## Coverage snapshot and maintenance (2025-12-21 extraction)

- Total scope: 55 schools extracted from the affordability report; `countries/greece/data/entities/schools.csv` holds 55 rows with unique `school_id` values aligned to these tables.
- Tier mix: 7 Tier 1 (high-fee international/premium), 15 Tier 2 (international pathway, fees not public), 33 Tier 3 (fee-paying Lyceums requiring screening).
- Geography split: 24 Athens/Attica, 13 Thessaloniki metro, and 18 regional (Patras 4, Thessaly 4, Epirus 3, Crete 2, Peloponnese 1, Central Macedonia/Katerini 1, Islands 3).
- Maintenance guardrails: keep `school_id` consistent across CSV, index, and profile slugs; update `notes`/signals and `as_of` dates when new evidence is captured; use T-356 to coordinate any bulk refresh after profile drafting.
- Profile status (2025-02-18): 46/55 schools have draft profiles linked in the `Profile` column below. Pending profiles: `sch-gr-chania-theodoropoulos-001`, `sch-gr-chios-teens-001`, `sch-gr-heraklion-pagkritio-001`, `sch-gr-ioannina-zografio-001`, `sch-gr-kalamata-bougas-001`, `sch-gr-katerini-platon-001`, `sch-gr-larissa-raptou-001`, `sch-gr-rhodes-college-001`, `sch-gr-rhodes-rodion-paideia-001`.

### Attica (Athens metro)

| School | City | Tier | Signal | Ticket | Profile | school_id |
|---|---|---|---|---|---|---|
| International School of Athens (ISA) | Kifisia | Tier 1 | IB DP with published ~€14.5k upper-secondary fees. | [T-301](../../../../tickets/T-301-sch-gr-athens-isa-001-profile.md) | [Profile](profiles/athens/sch-gr-athens-isa-001/README.md) | sch-gr-athens-isa-001 |
| American Community Schools of Athens (ACS Athens) | Chalandri | Tier 1 | US HS + IB DP; published ≈€15.7k. | [T-302](../../../../tickets/T-302-sch-gr-acs-athens-001-profile.md) | [Profile](profiles/athens/sch-gr-acs-athens-001/README.md) | sch-gr-acs-athens-001 |
| Costeas-Geitonas School (CGS) | Pallini | Tier 1 | Greek Lyceum + IB; IB fees €13.3k–€13.6k. | [T-303](../../../../tickets/T-303-sch-gr-pallini-cgs-001-profile.md) | [Profile](profiles/athens/sch-gr-pallini-cgs-001/README.md) | sch-gr-pallini-cgs-001 |
| Pierce - The American College of Greece | Agia Paraskevi | Tier 1 | Greek Lyceum + IB; IB fees ≈€13.9k. | [T-304](../../../../tickets/T-304-sch-gr-pierce-001-profile.md) | [Profile](profiles/athens/sch-gr-pierce-001/README.md) | sch-gr-pierce-001 |
| Athens College (Hellenic-American Educational Foundation) | Psychiko | Tier 1 | Greek Lyceum + IB DP; fees ≈€13.5k–€14k. | [T-305](../../../../tickets/T-305-sch-gr-athens-college-001-profile.md) | [Profile](profiles/athens/sch-gr-athens-college-001/README.md) | sch-gr-athens-college-001 |
| The Moraitis School | Psychiko | Tier 2 | IB DP verified; fees not published. | [T-306](../../../../tickets/T-306-sch-gr-psychiko-moraitis-001-profile.md) | [Profile](profiles/athens/sch-gr-psychiko-moraitis-001/README.md) | sch-gr-psychiko-moraitis-001 |
| Doukas School | Marousi | Tier 2 | IB DP verified; fees not published. | [T-307](../../../../tickets/T-307-sch-gr-marousi-doukas-001-profile.md) | [Profile](profiles/athens/sch-gr-marousi-doukas-001/README.md) | sch-gr-marousi-doukas-001 |
| Ionios School | Filothei | Tier 2 | IB DP verified; fees not published. | [T-308](../../../../tickets/T-308-sch-gr-filothei-ionios-001-profile.md) | [Profile](profiles/athens/sch-gr-filothei-ionios-001/README.md) | sch-gr-filothei-ionios-001 |
| Geitonas School | Koropi | Tier 2 | IB DP verified; fees not published. | [T-309](../../../../tickets/T-309-sch-gr-koropi-geitonas-001-profile.md) | [Profile](profiles/athens/sch-gr-koropi-geitonas-001/README.md) | sch-gr-koropi-geitonas-001 |
| International Metropolitan School (IMS) | Argyroupoli | Tier 2 | IB authorized 2024; fees not published. | [T-310](../../../../tickets/T-310-sch-gr-argyroupoli-ims-001-profile.md) | [Profile](profiles/athens/sch-gr-argyroupoli-ims-001/README.md) | sch-gr-argyroupoli-ims-001 |
| Campion School | Pallini | Tier 2 | British senior school; fees not published in official sources. | [T-311](../../../../tickets/T-311-sch-gr-pallini-campion-001-profile.md) | [Profile](profiles/athens/sch-gr-pallini-campion-001/README.md) | sch-gr-pallini-campion-001 |
| Lycée Franco-Hellénique Eugène Delacroix | Agia Paraskevi | Tier 2 | French lycée pathway; published 2025-2026 fees. | [T-312](../../../../tickets/T-312-sch-gr-agia-paraskevi-lfh-001-profile.md) | [Profile](profiles/athens/sch-gr-agia-paraskevi-lfh-001/README.md) | sch-gr-agia-paraskevi-lfh-001 |
| St Catherine’s British School | Athens | Tier 2 | IGCSE + IB DP; fees not published; confirmation needed. | [T-313](../../../../tickets/T-313-sch-gr-athens-st-catherines-001-profile.md) | [Profile](profiles/athens/sch-gr-athens-st-catherines-001/README.md) | sch-gr-athens-st-catherines-001 |
| Arsakeio Schools (Attica campuses) | Psychiko | Tier 3 | Greek private Lyceum network; published Lyceum fees ≈€6.5k. | [T-314](../../../../tickets/T-314-sch-gr-attica-arsakeio-001-profile.md) | [Profile](profiles/athens/sch-gr-attica-arsakeio-001/README.md) | sch-gr-attica-arsakeio-001 |
| Leonteios School of Athens (Lyceum) | Athens | Tier 3 | Greek private Lyceum; fees not published. | [T-315](../../../../tickets/T-315-sch-gr-athens-leonteios-001-profile.md) | [Profile](profiles/athens/sch-gr-athens-leonteios-001/README.md) | sch-gr-athens-leonteios-001 |
| Greek-French School Jeanne d’Arc (Lyceum) | Piraeus | Tier 3 | Greek private Lyceum; fees not published. | [T-316](../../../../tickets/T-316-sch-gr-piraeus-jeanne-darc-001-profile.md) | [Profile](profiles/athens/sch-gr-piraeus-jeanne-darc-001/README.md) | sch-gr-piraeus-jeanne-darc-001 |
| Ursulines (Neo Psychiko) Lyceum | Neo Psychiko | Tier 3 | Greek private Lyceum; fees not published. | [T-317](../../../../tickets/T-317-sch-gr-neo-psychiko-ursulines-001-profile.md) | [Profile](profiles/athens/sch-gr-neo-psychiko-ursulines-001/README.md) | sch-gr-neo-psychiko-ursulines-001 |
| Athinaiki Agogi & Paideia (Lyceum) | Kifisia | Tier 3 | Greek private Lyceum; fees not published. | [T-318](../../../../tickets/T-318-sch-gr-kifisia-athinaiki-agogi-001-profile.md) | [Profile](profiles/athens/sch-gr-kifisia-athinaiki-agogi-001/README.md) | sch-gr-kifisia-athinaiki-agogi-001 |
| “Themistoklis” Private Lyceum | Piraeus | Tier 3 | Greek private Lyceum; fees not published. | [T-319](../../../../tickets/T-319-sch-gr-piraeus-themistoklis-001-profile.md) | [Profile](profiles/athens/sch-gr-piraeus-themistoklis-001/README.md) | sch-gr-piraeus-themistoklis-001 |
| E.p.S. Private Lyceum | Piraeus | Tier 3 | Greek private Lyceum; fees not published. | [T-320](../../../../tickets/T-320-sch-gr-piraeus-eps-001-profile.md) | [Profile](profiles/athens/sch-gr-piraeus-eps-001/README.md) | sch-gr-piraeus-eps-001 |
| Avgoulea-Linardatou Schools (Lyceum) | Peristeri | Tier 3 | Greek private Lyceum; fees not published. | [T-321](../../../../tickets/T-321-sch-gr-athens-avgoulea-linardatou-001-profile.md) | [Profile](profiles/athens/sch-gr-athens-avgoulea-linardatou-001/README.md) | sch-gr-athens-avgoulea-linardatou-001 |
| Diamantopoulos Schools (Lyceum) | West Athens | Tier 3 | Greek private Lyceum; fees not published. | [T-322](../../../../tickets/T-322-sch-gr-athens-diamantopoulos-001-profile.md) | [Profile](profiles/athens/sch-gr-athens-diamantopoulos-001/README.md) | sch-gr-athens-diamantopoulos-001 |
| “Ioannis Tsiamoulis” Private Lyceum | West Athens | Tier 3 | Greek private Lyceum; fees not published. | [T-323](../../../../tickets/T-323-sch-gr-athens-tsiamoulis-001-profile.md) | [Profile](profiles/athens/sch-gr-athens-tsiamoulis-001/README.md) | sch-gr-athens-tsiamoulis-001 |
| “Nea Paideia” Private Lyceum | West Athens | Tier 3 | Greek private Lyceum; fees not published. | [T-324](../../../../tickets/T-324-sch-gr-athens-nea-paideia-001-profile.md) | [Profile](profiles/athens/sch-gr-athens-nea-paideia-001/README.md) | sch-gr-athens-nea-paideia-001 |

### Thessaloniki metro

| School | City | Tier | Signal | Ticket | Profile | school_id |
|---|---|---|---|---|---|---|
| Pinewood American International School of Thessaloniki | Thermi | Tier 1 | US HS + AP + IB DP with boarding; €13.45k–€13.75k fees. | [T-325](../../../../tickets/T-325-sch-gr-thermi-pinewood-001-profile.md) | [Profile](profiles/thessaloniki/sch-gr-thermi-pinewood-001/README.md) | sch-gr-thermi-pinewood-001 |
| Anatolia College / Anatolia High School | Pylaia | Tier 1 | Greek Lyceum + IB DP; boarding ecosystem; premium positioning. | [T-326](../../../../tickets/T-326-sch-gr-anatolia-college-001-profile.md) | [Profile](profiles/thessaloniki/sch-gr-anatolia-college-001/README.md) | sch-gr-anatolia-college-001 |
| German School of Thessaloniki (DST) | Pylaia-Chortiatis | Tier 2 | German international pathway; fees not published. | [T-327](../../../../tickets/T-327-sch-gr-pylaia-dst-001-profile.md) | [Profile](profiles/thessaloniki/sch-gr-pylaia-dst-001/README.md) | sch-gr-pylaia-dst-001 |
| French School of Thessaloniki (EFT) | Thessaloniki | Tier 2 | French lycée pathway; fees not published. | [T-328](../../../../tickets/T-328-sch-gr-thessaloniki-eft-001-profile.md) | [Profile](profiles/thessaloniki/sch-gr-thessaloniki-eft-001/README.md) | sch-gr-thessaloniki-eft-001 |
| Hellenic College of Thessaloniki | Thermi | Tier 2 | Greek Lyceum + US dual diploma marketing; fees not published. | [T-329](../../../../tickets/T-329-sch-gr-thermi-hellenic-college-001-profile.md) | [Profile](profiles/thessaloniki/sch-gr-thermi-hellenic-college-001/README.md) | sch-gr-thermi-hellenic-college-001 |
| Mandoulides Schools | Thermi | Tier 3 | Greek private Lyceum; fees not published. | [T-330](../../../../tickets/T-330-sch-gr-thermi-mandoulides-001-profile.md) | [Profile](profiles/thessaloniki/sch-gr-thermi-mandoulides-001/README.md) | sch-gr-thermi-mandoulides-001 |
| Vassiliadis Schools | Thermi | Tier 3 | Greek private Lyceum; fees not published. | [T-331](../../../../tickets/T-331-sch-gr-thermi-vassiliadis-001-profile.md) | [Profile](profiles/thessaloniki/sch-gr-thermi-vassiliadis-001/README.md) | sch-gr-thermi-vassiliadis-001 |
| De La Salle College Thessaloniki | Neapoli-Sykies | Tier 3 | Greek private Lyceum; fees not published. | [T-332](../../../../tickets/T-332-sch-gr-neapoli-delasalle-001-profile.md) | [Profile](profiles/thessaloniki/sch-gr-neapoli-delasalle-001/README.md) | sch-gr-neapoli-delasalle-001 |
| Fryganioti Schools | Pavlos Melas | Tier 3 | Greek private Lyceum; fees not published. | [T-333](../../../../tickets/T-333-sch-gr-pavlos-melas-fryganioti-001-profile.md) | [Profile](profiles/thessaloniki/sch-gr-pavlos-melas-fryganioti-001/README.md) | sch-gr-pavlos-melas-fryganioti-001 |
| Aristoteleio College (Thessaloniki) | Thermi | Tier 3 | Greek private Lyceum; fees not published. | [T-334](../../../../tickets/T-334-sch-gr-thermi-aristoteleio-001-profile.md) | [Profile](profiles/thessaloniki/sch-gr-thermi-aristoteleio-001/README.md) | sch-gr-thermi-aristoteleio-001 |
| American Farm School (General High School) | Pylaia-Chortiatis | Tier 3 | Greek private Lyceum; boarding/agro focus; fees not published. | [T-335](../../../../tickets/T-335-sch-gr-pylaia-american-farm-001-profile.md) | [Profile](profiles/thessaloniki/sch-gr-pylaia-american-farm-001/README.md) | sch-gr-pylaia-american-farm-001 |
| Arsakeio Schools Thessaloniki (Lyceum) | Pylaia-Chortiatis | Tier 3 | Greek private Lyceum; published Lyceum fee ≈€5.355k. | [T-336](../../../../tickets/T-336-sch-gr-pylaia-arsakeio-001-profile.md) | [Profile](profiles/thessaloniki/sch-gr-pylaia-arsakeio-001/README.md) | sch-gr-pylaia-arsakeio-001 |
| “O Apostolos Pavlos” Schools | Pylaia | Tier 3 | Greek private Lyceum; fees not published. | [T-337](../../../../tickets/T-337-sch-gr-pylaia-apostolos-pavlos-001-profile.md) | [Profile](profiles/thessaloniki/sch-gr-pylaia-apostolos-pavlos-001/README.md) | sch-gr-pylaia-apostolos-pavlos-001 |

### Western Greece

| School | City | Tier | Signal | Ticket | Profile | school_id |
|---|---|---|---|---|---|---|
| Arsakeio General Lyceum of Patras | Patras | Tier 3 | Greek private Lyceum; fees not published. | [T-338](../../../../tickets/T-338-sch-gr-patras-arsakeio-001-profile.md) | [Profile](profiles/patras/sch-gr-patras-arsakeio-001/README.md) | sch-gr-patras-arsakeio-001 |
| Anagennisi Private General Lyceum (Patras) | Patras | Tier 3 | Greek private Lyceum; fees not published. | [T-339](../../../../tickets/T-339-sch-gr-patras-anagennisi-001-profile.md) | [Profile](profiles/patras/sch-gr-patras-anagennisi-001/README.md) | sch-gr-patras-anagennisi-001 |
| Themelio EDU Private Lyceum | Patras | Tier 3 | Greek private Lyceum; fees not published. | [T-340](../../../../tickets/T-340-sch-gr-patras-themelio-001-profile.md) | [Profile](profiles/patras/sch-gr-patras-themelio-001/README.md) | sch-gr-patras-themelio-001 |
| Trianteio Evening EPAL (Private) | Patras | Tier 3 | Private EPAL; evening program; fees not published. | [T-341](../../../../tickets/T-341-sch-gr-patras-trianteio-001-profile.md) | [Profile](profiles/patras/sch-gr-patras-trianteio-001/README.md) | sch-gr-patras-trianteio-001 |

### Thessaly

| School | City | Tier | Signal | Ticket | Profile | school_id |
|---|---|---|---|---|---|---|
| Private Lyceum "M. N. Raptou, Center for Greek Education" | Larissa | Tier 3 | Greek private Lyceum; fees not published. | [T-342](../../../../tickets/T-342-sch-gr-larissa-raptou-001-profile.md) | Pending profile | sch-gr-larissa-raptou-001 |
| N. Bakogianni Private Lyceum | Larissa | Tier 3 | Greek private Lyceum; fees not published. | [T-343](../../../../tickets/T-343-sch-gr-larissa-bakogianni-001-profile.md) | [Profile](profiles/larissa/sch-gr-larissa-bakogianni-001/README.md) | sch-gr-larissa-bakogianni-001 |
| Promitheas Private General Lyceum of Volos | Volos | Tier 3 | Greek private Lyceum; fees not published. | [T-344](../../../../tickets/T-344-sch-gr-volos-promitheas-001-profile.md) | [Profile](profiles/volos/sch-gr-volos-promitheas-001/README.md) | sch-gr-volos-promitheas-001 |
| Athena Educational Institutions, Private Lyceum of Trikala | Trikala | Tier 3 | Greek private Lyceum; fees not published. | [T-345](../../../../tickets/T-345-sch-gr-trikala-athena-001-profile.md) | [Profile](profiles/other/sch-gr-trikala-athena-001/README.md) | sch-gr-trikala-athena-001 |

### Epirus

| School | City | Tier | Signal | Ticket | Profile | school_id |
|---|---|---|---|---|---|---|
| Arsakeio General Lyceum of Ioannina | Ioannina | Tier 3 | Greek private Lyceum; published fees around €6.5k. | [T-346](../../../../tickets/T-346-sch-gr-ioannina-arsakeio-001-profile.md) | [Profile](profiles/ioannina/sch-gr-ioannina-arsakeio-001/README.md) | sch-gr-ioannina-arsakeio-001 |
| Dodonaia Educational Institutions (Lyceum) | Ioannina | Tier 3 | Greek private Lyceum; fees not published. | [T-347](../../../../tickets/T-347-sch-gr-ioannina-dodonaia-001-profile.md) | [Profile](profiles/ioannina/sch-gr-ioannina-dodonaia-001/README.md) | sch-gr-ioannina-dodonaia-001 |
| Zografio Private Lyceum | Ioannina | Tier 3 | Greek private Lyceum; fees not published. | [T-348](../../../../tickets/T-348-sch-gr-ioannina-zografio-001-profile.md) | Pending profile | sch-gr-ioannina-zografio-001 |

### Crete

| School | City | Tier | Signal | Ticket | Profile | school_id |
|---|---|---|---|---|---|---|
| Pagkritio School, Private Lyceum | Heraklion | Tier 2 | Greek private Lyceum with international pathway signals; published A’ Lyceum fee ≈€7k. | [T-349](../../../../tickets/T-349-sch-gr-heraklion-pagkritio-001-profile.md) | Pending profile | sch-gr-heraklion-pagkritio-001 |
| Theodoropoulos Private Schools, Lyceum | Chania | Tier 3 | Greek private Lyceum; fees not published. | [T-350](../../../../tickets/T-350-sch-gr-chania-theodoropoulos-001-profile.md) | Pending profile | sch-gr-chania-theodoropoulos-001 |

### Peloponnese

| School | City | Tier | Signal | Ticket | Profile | school_id |
|---|---|---|---|---|---|---|
| Bougas Educational Institutions | Kalamata | Tier 3 | Greek private Lyceum; fees not published. | [T-351](../../../../tickets/T-351-sch-gr-kalamata-bougas-001-profile.md) | Pending profile | sch-gr-kalamata-bougas-001 |

### Central Macedonia (regional)

| School | City | Tier | Signal | Ticket | Profile | school_id |
|---|---|---|---|---|---|---|
| Platon Lyceum | Katerini | Tier 3 | Greek private Lyceum; fees not published. | [T-352](../../../../tickets/T-352-sch-gr-katerini-platon-001-profile.md) | Pending profile | sch-gr-katerini-platon-001 |

### Islands

| School | City | Tier | Signal | Ticket | Profile | school_id |
|---|---|---|---|---|---|---|
| Rhodes College (Private Lyceum) | Rhodes | Tier 2 | Premium branding noted; fees not captured. | [T-353](../../../../tickets/T-353-sch-gr-rhodes-college-001-profile.md) | Pending profile | sch-gr-rhodes-college-001 |
| Rodion Paideia Educational Group, General Lyceum | Rhodes | Tier 2 | Private Lyceum; premium island option; fees not captured. | [T-354](../../../../tickets/T-354-sch-gr-rhodes-rodion-paideia-001-profile.md) | Pending profile | sch-gr-rhodes-rodion-paideia-001 |
| TEENS (Tsakos Hellenic Training Ship School) Private EPAL | Chios | Tier 2 | Private maritime EPAL; specialized pathway; fees not published. | [T-355](../../../../tickets/T-355-sch-gr-chios-teens-001-profile.md) | Pending profile | sch-gr-chios-teens-001 |
