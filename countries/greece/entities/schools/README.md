# Schools

Maintain profiles of Greek secondary schools, lyceums, and language schools that can influence outbound recruitment to UNIC and UNIC Athens. Capture counselor contacts (organization-level), curriculum, graduating class size, and any history of university placements.

- `profiles/` – one folder per city plus an `other/` catch-all. Place individual school profiles within the relevant city folder and include `last_verified` dates and sources.

Current city folders follow the 20 largest metro areas (Athens, Thessaloniki, Patras, Heraklion, Larissa, Volos, Ioannina, Chania, Rhodes, Kavala, Kalamata, Serres, Komotini, Xanthi, Alexandroupoli, Tripoli, Rethymno, Katerini, Corfu, Lamia) plus `other` for edge cases.

## 2025-12-21 affordability-report extraction

- Source: `countries/greece/reports/20251221-Greek High Schools for UNIC Affordability.md`.
- Coverage: every fee-paying or international-pathway high school listed in the report is captured in `countries/greece/entities/schools/index.md` with ticket links and school_ids, and structured in `countries/greece/data/entities/schools.csv`.
- Execution: T-300 generated tickets T-301–T-355 (one profile per school) using the global high school profile template. T-356 will refresh this README, the index, and the CSV once profiles are drafted.

### 2025-02-18 profile refresh (T-356)

- Profile delivery: 46 of 55 affordability-report schools now have draft profiles under `profiles/<city>/<school_id>/README.md`; the new `Profile` column in `index.md` links directly to each draft alongside the ticket IDs.
- Pending profiles (9): `sch-gr-chania-theodoropoulos-001`, `sch-gr-chios-teens-001`, `sch-gr-heraklion-pagkritio-001`, `sch-gr-ioannina-zografio-001`, `sch-gr-kalamata-bougas-001`, `sch-gr-katerini-platon-001`, `sch-gr-larissa-raptou-001`, `sch-gr-rhodes-college-001`, `sch-gr-rhodes-rodion-paideia-001`.
- CSV alignment: `countries/greece/data/entities/schools.csv` remains the canonical 55-row register with `school_id` slugs matching the profile and ticket names; update `as_of` and `notes` there when new evidence is validated.

## Navigation and upkeep

- Index and tickets: see `countries/greece/entities/schools/index.md` for the extraction tables and links to T-301–T-355; consolidation is tracked in T-356 (`tickets/`).
- Data file: `countries/greece/data/entities/schools.csv` is the canonical register for the 2025-12-21 affordability extraction; keep `school_id` values identical across CSV, index, and profile slugs.
- Profile drafting: follow `skills/schools-and-feeders/SKILL.md` plus the global template at `skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md` when writing the city/campus profiles.
- Update workflow: when new evidence arrives (fees, programs, contacts), update the CSV and index in tandem, refresh `last_verified`, and push the change to the relevant profile ticket; defer bulk clean-up and navigation refresh to T-356 once profiles are delivered.

## Coverage snapshot (as extracted 2025-12-21)

- 55 total schools captured from the affordability report; 55 unique `school_id` values mirrored in the CSV.
- Geography split: 24 in Athens/Attica, 13 in Thessaloniki metro, and 18 across regional municipalities (Patras 4, Thessaly 4, Epirus 3, Crete 2, Peloponnese 1, Central Macedonia/Katerini 1, Islands 3).
- Tier mix (per index tables): 7 Tier 1 premium international/high-fee schools, 15 Tier 2 international-pathway schools with limited fee transparency, and 33 Tier 3 fee-paying Lyceums requiring student-level screening.
- Use the CSV and index as the single source for `school_id` slugs when creating profiles under `profiles/<city>/<school-slug>/`.
