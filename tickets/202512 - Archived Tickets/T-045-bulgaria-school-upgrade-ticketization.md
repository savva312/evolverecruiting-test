# T-045: Bulgaria school upgrade ticketization (Sofia, Plovdiv, Varna)

Status: archived
Type: structure
Priority: P1
Dependencies: T-026-high-school-profile-template
Claimed-by: work
Claimed-at: 2025-12-20T17:52:27+00:00
Last-updated: 2025-12-20

---

## Goal

Create one dedicated ticket per school in Sofia, Plovdiv, and Varna to upgrade each profile to the global high school profile standard defined in `skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md`. Ensure each ticket has clean scope boundaries so upgrades can proceed without path conflicts.

---

## Context

- Work applies the global `high-school-profile-template` skill to Bulgarian school profiles under `bulgaria/entities/schools/profiles/**`.
- Sofia profiles are currently single-file markdowns; Plovdiv/Varna use subdirectories with `README.md`. Future upgrade work may reorganize paths to match the global template structure.
- Per-ticket scoping is needed to avoid parallel edit collisions across city directories.

---

## Allowed write paths

- `tickets/**`
- `research/**` (optional notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `.github/**`
- `scripts/**`

---

## Required outputs

New tickets (Status: open) for each school upgrade:

- `tickets/T-033-sofia-91st-german-language-school-91neg-profile-upgrade.md`
- `tickets/T-034-sofia-9th-french-language-school-9feg-profile-upgrade.md`
- `tickets/T-035-sofia-american-college-of-sofia-profile-upgrade.md`
- `tickets/T-036-sofia-american-english-academy-profile-upgrade.md`
- `tickets/T-037-sofia-american-school-of-bulgaria-profile-upgrade.md`
- `tickets/T-038-sofia-anglo-american-school-of-sofia-profile-upgrade.md`
- `tickets/T-039-sofia-british-school-of-sofia-profile-upgrade.md`
- `tickets/T-040-sofia-cosmos-international-school-sofia-profile-upgrade.md`
- `tickets/T-041-sofia-deutsche-schule-sofia-profile-upgrade.md`
- `tickets/T-042-sofia-first-english-language-school-1aeg-profile-upgrade.md`
- `tickets/T-043-sofia-international-ib-montessori-school-sofia-profile-upgrade.md`
- `tickets/T-044-sofia-international-school-uwekind-profile-upgrade.md`
- `tickets/T-045-sofia-national-high-school-of-math-natural-sciences-npmg-profile-upgrade.md`
- `tickets/T-046-sofia-sofia-mathematical-gymnasium-smg-profile-upgrade.md`
- `tickets/T-047-sofia-st-george-international-school-sofia-profile-upgrade.md`
- `tickets/T-048-sofia-zlatarski-international-school-of-sofia-profile-upgrade.md`
- `tickets/T-049-plovdiv-eg-plovdiv-profile-upgrade.md`
- `tickets/T-050-plovdiv-mg-kiril-popov-profile-upgrade.md`
- `tickets/T-051-plovdiv-classic-private-school-profile-upgrade.md`
- `tickets/T-052-plovdiv-druzhba-private-school-profile-upgrade.md`
- `tickets/T-053-plovdiv-stoyanstroi-stoyan-sariev-profile-upgrade.md`
- `tickets/T-054-plovdiv-french-language-gymnasium-exupery-profile-upgrade.md`
- `tickets/T-055-plovdiv-eg-ivan-vazov-profile-upgrade.md`
- `tickets/T-056-plovdiv-talantite-private-business-school-profile-upgrade.md`
- `tickets/T-057-plovdiv-gikn-private-it-cs-profile-upgrade.md`
- `tickets/T-058-plovdiv-humanities-gymnasium-cyril-methodius-profile-upgrade.md`
- `tickets/T-059-plovdiv-national-gymnasium-stage-screen-arts-profile-upgrade.md`
- `tickets/T-060-plovdiv-national-art-school-tsanko-lavrenov-profile-upgrade.md`
- `tickets/T-061-varna-exupery-antoine-de-saint-exupery-profile-upgrade.md`
- `tickets/T-062-varna-first-foreign-language-high-school-1eg-profile-upgrade.md`
- `tickets/T-063-varna-fourth-language-high-school-frederic-joliot-curie-4eg-profile-upgrade.md`
- `tickets/T-064-varna-george-byron-private-language-school-profile-upgrade.md`
- `tickets/T-065-varna-gpche-yoan-ekzarch-5eg-profile-upgrade.md`
- `tickets/T-066-varna-math-gymnasium-petar-beron-profile-upgrade.md`
- `tickets/T-067-varna-pg-tourism-prof-assen-zlatarov-profile-upgrade.md`
- `tickets/T-068-varna-pghhvt-mendeleev-chem-food-tech-profile-upgrade.md`
- `tickets/T-069-varna-pgit-ivan-bogorov-profile-upgrade.md`
- `tickets/T-070-varna-pgkmks-akad-blagovest-sendov-profile-upgrade.md`
- `tickets/T-071-varna-third-pmg-metodiy-popov-3pmg-profile-upgrade.md`
- `tickets/T-072-varna-varna-maritime-high-school-saint-nicholas-profile-upgrade.md`

---

## Acceptance criteria

- All required ticket files exist under `tickets/` with `Status: open`, `Type`, `Priority`, dependencies, allowed/forbidden paths, required outputs, and acceptance criteria populated.
- Tickets reference the global `high-school-profile-template` as the upgrade standard and scope the relevant school path(s) only.
- No files are modified outside `Allowed write paths`.

---

## Execution notes (optional)

- What changed (short): Added 40 city-specific upgrade tickets for Sofia, Plovdiv, and Varna schools and scoped them to the global high school profile template.
- Follow-ups: Execution of individual tickets to upgrade each profile.
