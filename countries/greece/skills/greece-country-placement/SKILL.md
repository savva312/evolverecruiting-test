---
name: greece-country-placement
description: Procedure for identifying, relocating, and maintaining Greece-specific content in the `countries/greece/` country tree while keeping global skills untouched.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: greece
---

# Greece country placement

Use this skill whenever a ticket requires creating or migrating **Greece-only** materials. It keeps Greece content under the `countries/greece/` subtree and ensures reports and skills stay discoverable.

## Before you start

1) Read the ticket and confirm it explicitly allows writing inside `countries/greece/**` and, if needed, `countries/greece/skills/**`.
2) Skim existing Greece files under `countries/greece/` to avoid duplicate structures; reuse folders where possible.
3) Check for protected files (e.g., `README.md`, `AGENTS.md`, `ROADMAP.md`) and do not edit them unless the ticket is a structure change that allows it.

## Inputs

You may receive:
- Existing Greece documents to relocate (reports, playbooks, entity profiles).
- New Greece research or execution notes to add.
- Link targets that must be updated after a move.

## Procedure

1) **Inventory Greece materials**
   - List files that are Greece-only (content about Greece market, Athens operations, Greek regulators, etc.).
   - Note current paths and any inbound links that will need updating.

2) **Choose target locations under `countries/greece/`**
   - Reports → `countries/greece/reports/` using `YYYYMMDD-topic.md` filenames.
   - Market intel → `countries/greece/market/` (create subfolders like `recognition/`, `affordability/` if needed).
   - Entities → `countries/greece/entities/` with `profiles/` as needed.
   - Playbooks → `countries/greece/go-to-market/` or `countries/greece/program-clusters/` by discipline.

3) **Move or create files**
   - Create missing directories with `mkdir -p` inside `countries/greece/`.
   - When relocating existing files, preserve filenames where practical and carry over `last_updated` stamps.
   - If the ticket forbids touching the source path, flag a blocker instead of moving the file.

4) **Update links and references**
   - Adjust relative links in Greece files so they point to the new `countries/greece/` paths.
   - Avoid altering Bulgaria or global links unless the ticket allows it.

5) **Skill placement**
   - Put Greece-only procedures in `countries/greece/skills/**` with accurate metadata (`scope: greece`).
   - Keep global, reusable guidance in the root `/skills/` folder.

6) **Quality checks**
   - Run through the ticket’s acceptance criteria.
   - Ensure no Greece content remains outside `countries/greece/**` unless explicitly exempted.
   - Confirm new folders include short README/index files for navigation where helpful.

## Done checklist

- [ ] All Greece-only materials live under `countries/greece/**` in the correct subfolder.
- [ ] Reports sit in `countries/greece/reports/` with clear filenames and metadata.
- [ ] Any Greece links inside the country tree resolve correctly after moves.
- [ ] Global skills remain untouched; Greece procedures live in `countries/greece/skills/**`.
- [ ] Changes stay within ticket allowed paths.
