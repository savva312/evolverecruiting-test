# Skills

This repository uses the **Agent Skills** format: each skill is a folder under `/skills/` containing a required `SKILL.md` file with YAML frontmatter and instructions.

## Scope
- `/skills/` is now limited to **global, cross-country skills** only.
- Country-specific skills live inside each country namespace (e.g., `/countries/bulgaria/skills/`, `/countries/greece/skills/`, `/countries/nigeria/skills/`).

## What to do first (for agents)
1. Read `README.md` and `AGENTS.md` at the repo root.
2. Read `ROADMAP.md` and the relevant ticket(s) in `/tickets/`.
3. Use `/skills/*/SKILL.md` only when you need the procedure, templates, or rules.

## Global skill index
- `agents-and-partner-ecosystem`: global taxonomy, workflow, and templates for mapping education agents and partner entities
- `assets-and-sources`: how to store non-text assets and record research sources
- `competitors`: build home/base competitor profiles, record cross-country presence, and standardize profile templates
- `country-setup`: layered ticket playbook to onboard a new country (scaffold, discovery, profiling, QA)
- `csv-authoring`: world-class prompting and self-checks for generating clean, schema-locked CSVs
- `data-model-csvs-and-profiles`: schema standards and authoring workflow for CSV datasets and profile tables
- `education-system-and-calendar`: approach for mapping education structures, calendars, and term patterns by market
- `email-ses-outbound`: build RFC 822 `.eml` messages and companion Markdown briefs for AWS SES SendRawEmail
- `evobuilder-workflow`: end-to-end workflow for working tickets safely
- `git-pr-hygiene`: clean diffs, commits, and PR notes practices
- `high-school-profile-template`: canonical high school profile template (global)
- `id-governance`: deterministic ID pattern (`<cc>_<kind>_<slug>__<hash>`), normalization, hashing, and dedupe checkpoints for entities and events
- `infrastructure-building-folders`: scaffold campus building folders without creating empty directories; expand architecture/engineering/ops only when populated
- `markdown-authoring`: house style for markdown docs and data notes (includes canonical formatting checklist: headings, bullets, blank lines, EOF newline)
- `marp-presentations`: MARP workflow plus UNIC Default theme, template starter, and export guidance (HTML/PDF/PPTX)
- `photo-documentation`: naming, description, and per-folder index standards for facility photo sets
- `research-request-briefs`: Markdown and email-ready briefs for EvoResearcher (title, report output path, sections, rounds; model fixed to GPT-5.2 (H))
- `multi-channel-messaging`: API-ready, consent-safe messaging schema plus channel rendering/downgrade, opt-out, and QA/logging for SMS, Signal, WhatsApp, Telegram, and email
- `paid-media-and-channel-playbooks`: building channel playbooks for paid/digital acquisition
- `program-clusters-and-competitor-sets`: how to build program clusters and benchmark competitors
- `recognition-and-licensure`: global workflow for recognition/licensure research and authority profiling
- `repo-conventions`: canonical repo conventions (files, folders, naming)
- `roadmap-tickets`: formats and rules for `ROADMAP.md` and `/tickets/*.md`
- `schools-and-feeders`: profiling schools and feeder networks with sourcing signals
- `ticket-creation`: prompt-style guide for drafting, claiming, and closing parallel-safe tickets
- `ticket-archiving`: explicit process for setting `Status: archived`, relocating tickets into monthly archive folders, and updating indices
- `ticket-boundaries`: strict “where you may write” rules for parallelization
