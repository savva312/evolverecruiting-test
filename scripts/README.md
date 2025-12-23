# Scripts

## Markdown canonicalization

Use `scripts/canonicalize_md.py` to enforce the repo’s Markdown guardrails (headings/bullets, trailing whitespace, blank lines, single EOF newline).

- **Default (fix in-place, auto-discover staged/modified Markdown):** `python scripts/canonicalize_md.py`
- **Fix specific files:** `python scripts/canonicalize_md.py --fix path/to/file.md README.md`
- **Check without writing:** `python scripts/canonicalize_md.py --check README.md docs/file.md`

If no mode is provided, the script defaults to `--fix` using `git diff --name-only` (staged + unstaged). New/untracked files are not picked up by git diff; pass their paths explicitly.

### Pre-commit hook

An optional hook is defined in `.pre-commit-config.yaml`:

```yaml
- repo: local
  hooks:
    - id: canonicalize-markdown
      entry: python scripts/canonicalize_md.py --fix
      files: "\\.md$"
      language: system
```

Install and run:

```bash
pip install pre-commit
pre-commit install
# Format staged Markdown
pre-commit run canonicalize-markdown
# Or run on specific files
pre-commit run canonicalize-markdown --files README.md scripts/README.md
```

## ID minter and registry linter

Use `scripts/id_minter.py` to mint deterministic IDs and lint country registries for duplicates and profile alignment issues. IDs follow the `<cc>_<kind>_<slug>__<hash>` format (sha256 → base32, first 10 chars) defined in `skills/id-governance`.

## Setup

- Requires Python 3.10+.
- Install `pyyaml` if you plan to read YAML/frontmatter: `pip install pyyaml`.

## Mint an `entity_id`

```bash
# From repository root
python scripts/id_minter.py mint path/to/entity.yaml --show-canonical

# Override fields if the source data is missing them
python scripts/id_minter.py mint path/to/profile.md --kind school --country bg --slug custom-slug

# Emit machine-readable output for pipelines
python scripts/id_minter.py mint path/to/profile.md --json
```

The minter refuses to regenerate an ID when `entity_id` already exists in the source metadata. Use `--show-canonical` to see the exact canonical string used for hashing.

## Lint registries

```bash
# Lint every country registry (repo root autodetected)
python scripts/id_minter.py lint

# Lint specific countries
python scripts/id_minter.py lint --country bulgaria --country nigeria

# Point at a different checkout
python scripts/id_minter.py lint --repo-root /path/to/repo
```

Checks performed:
- Duplicate canonical keys (name + city) and website/domain collisions.
- Missing `profile_path` values.
- Profile/frontmatter `entity_id` mismatches or missing frontmatter when a profile is referenced.

## Pre-commit / CI usage

- **pre-commit**: add a repo-local hook:

```yaml
- repo: local
  hooks:
    - id: id-mint-lint
      name: Lint entity registries
      entry: python scripts/id_minter.py lint
      language: system
      files: "^countries/.+/(data/entities|data/relationships\\.csv|entities/.+\\.md)$"
```

- **CI**: run the linter in a workflow or job step:

```bash
python -m pip install --no-cache-dir pyyaml
python scripts/id_minter.py lint
```
