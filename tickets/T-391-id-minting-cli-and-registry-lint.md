# T-391: Deterministic ID minter CLI and registry lint

Status: done
Type: structure
Priority: P1
Dependencies: T-371
Claimed-by: work
Claimed-at: 2025-12-21T21:03:08Z
Last-updated: 2025-12-21

---

## Goal

Ship a deterministic ID minter CLI (Python) that reads YAML/JSON/frontmatter, applies the ID governance spec (slug normalization + base32 hash), refuses to remint existing IDs, and can lint country registries for duplicate canonical keys and ID/frontmatter mismatches. Document how to run it locally and in CI/pre-commit.

## Context

- `skills/id-governance` defines the deterministic ID standard and must stay in sync with tooling.
- Country registries (CSV + profile frontmatter) need automated checks to catch duplicates, missing profile links, and ID mismatches.
- A small, dependency-light script in `scripts/` should be the supported entrypoint.

## Allowed write paths

- `scripts/**`
- `skills/id-governance/**`
- `tickets/T-372-id-minting-cli-and-registry-lint.md`
- `executions/**` (optional notes)

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- Other `tickets/**`
- `.github/**`
- Country directories except for read-only linting

## Required outputs

- `scripts/id_minter.py` providing ID minting and registry linting commands.
- Usage documentation (either `scripts/README.md` snippet or updates inside `skills/id-governance/SKILL.md`).
- `skills/id-governance/SKILL.md` aligned to the tool (base32 hash detail + CLI usage pointers).
- Ticket updated to `done` with a short “what changed” note.

## Acceptance criteria

- ID minter computes IDs using the documented normalization and base32 hash, refuses to overwrite existing IDs/frontmatter values, and prints the canonical string inputs it used.
- Lint mode scans `countries/*/data/entities.*.csv` and `relationships.csv` for duplicate canonical keys (domain/name+city), missing `profile_path`, and ID/frontmatter mismatches.
- Documentation shows example commands and guidance for pre-commit/CI usage.
- No files outside Allowed write paths are modified; protected files remain untouched.
- Ticket status set to `done` with concise execution notes when complete.

## Execution notes (optional)

- What changed (short): Refreshed id-governance skill with CLI usage/dependency notes and corrected hash wording; expanded `scripts/README.md` with overrides/JSON examples and lint repo-root flag; confirmed CLI minting returns the documented deterministic ID output.
