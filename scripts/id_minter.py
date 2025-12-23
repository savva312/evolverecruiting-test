#!/usr/bin/env python3
"""
Deterministic ID minter and registry linter for UNIC recruiting data.

Features:
- Mint IDs from YAML/JSON/Markdown frontmatter using the id-governance spec.
- Refuse to remint when an entity_id already exists.
- Lint country registries for duplicate canonical keys, missing profile paths,
  and mismatches between CSV rows and profile frontmatter.
"""
from __future__ import annotations

import argparse
import base64
import csv
import hashlib
import json
import re
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple
from urllib.parse import urlparse

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover - optional dependency
    yaml = None

# Controlled kinds from the id-governance skill.
CONTROLLED_KINDS = {
    "school",
    "agent",
    "event",
    "competitor",
    "regulator",
    "ngo-sgo",
    "exam",
    "program",
    "campus",
    "scholarship",
    "funnel-action",
}

COUNTRY_FALLBACK = {
    "bulgaria": "bg",
    "nigeria": "ng",
    "greece": "gr",
    "jordan": "jo",
    "lebanon": "lb",
    "romania": "ro",
    "serbia": "rs",
}

CANONICAL_FIELDS: Dict[str, List[Sequence[str]]] = {
    "school": [("canonical_name_en", "name"), ("city",), ("website_domain", "website", "url")],
    "agent": [("canonical_name_en", "name"), ("hq_city_or_region", "city"), ("website_domain", "website", "url")],
    "event": [("event_name",), ("organizer_name",), ("anchor_city_or_country", "city", "country"), ("timing_pattern",)],
    "competitor": [("canonical_name_en", "name"), ("country",), ("primary_cluster_or_degree_level", "cluster")],
    "regulator": [("authority_name", "canonical_name_en", "name"), ("country",), ("scope",)],
    "ngo-sgo": [("org_name", "canonical_name_en", "name"), ("country",), ("focus_area",)],
    "exam": [("exam_name", "canonical_name_en", "name"), ("issuer",), ("country",)],
    "program": [("campus",), ("program_name", "canonical_name_en", "name"), ("degree_level",)],
    "campus": [("campus_name", "canonical_name_en", "name"), ("city",), ("country",)],
    "scholarship": [("scholarship_name", "canonical_name_en", "name"), ("country",), ("audience",)],
    "funnel-action": [("action_name", "canonical_name_en", "name"), ("program_or_segment",), ("step",)],
}


@dataclass
class LintIssue:
    path: Path
    message: str
    severity: str = "error"

    def format(self) -> str:
        return f"[{self.severity.upper()}] {self.path}: {self.message}"


def strip_diacritics(value: str) -> str:
    return "".join(ch for ch in unicodedata.normalize("NFKD", value) if not unicodedata.combining(ch))


def normalize_slug(value: str) -> str:
    normalized = strip_diacritics(value).lower()
    normalized = normalized.replace("&", " and ")
    normalized = re.sub(r"[^\w\s-]", " ", normalized)
    normalized = normalized.replace("_", " ")
    normalized = re.sub(r"\s+", "-", normalized)
    normalized = re.sub(r"-+", "-", normalized).strip("-")
    return normalized or "-"


def normalize_value(value: Optional[str]) -> str:
    if value is None:
        return "-"
    cleaned = strip_diacritics(str(value)).strip().lower()
    if not cleaned:
        return "-"
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned


def normalize_domain(raw: Optional[str]) -> str:
    normalized = normalize_value(raw)
    if normalized in {"-", ""}:
        return "-"
    candidate = normalized
    if "://" in candidate:
        parsed = urlparse(candidate)
        candidate = parsed.netloc or parsed.path
    candidate = candidate.split("/")[0]
    candidate = re.sub(r"^www\.", "", candidate)
    candidate = re.sub(r":.*$", "", candidate)
    candidate = re.sub(r"[^\w\.-]", "", candidate)
    return candidate or "-"


def extract_first(metadata: Dict[str, object], keys: Sequence[str]) -> Optional[str]:
    for key in keys:
        value = metadata.get(key)
        if value is not None and str(value).strip():
            return str(value)
    return None


def resolve_country_code(metadata: Dict[str, object], override: Optional[str]) -> str:
    if override:
        candidate = override.strip().lower()
    else:
        candidate = (
            str(
                metadata.get("cc")
                or metadata.get("country_code")
                or metadata.get("country")
                or metadata.get("country_iso")
                or ""
            ).strip().lower()
        )
    if len(candidate) == 2:
        return candidate
    if candidate in COUNTRY_FALLBACK:
        return COUNTRY_FALLBACK[candidate]
    raise ValueError("Country code must be a two-letter ISO code (e.g., bg, ng, gr).")


def resolve_kind(metadata: Dict[str, object], override: Optional[str]) -> str:
    kind = (override or metadata.get("kind") or metadata.get("entity_type") or metadata.get("type") or "").strip().lower()
    if not kind:
        raise ValueError("An entity kind is required (e.g., school, agent, event).")
    if kind not in CONTROLLED_KINDS:
        raise ValueError(f"Kind '{kind}' is not in the controlled list: {sorted(CONTROLLED_KINDS)}")
    return kind


def load_metadata(input_path: Path) -> Dict[str, object]:
    if not input_path.exists():
        raise FileNotFoundError(f"Input not found: {input_path}")
    suffix = input_path.suffix.lower()
    if suffix in {".json"}:
        return json.loads(input_path.read_text(encoding="utf-8"))
    if suffix in {".yml", ".yaml"}:
        if yaml is None:
            raise ImportError("pyyaml is required to read YAML inputs. Install with `pip install pyyaml`.")
        return yaml.safe_load(input_path.read_text(encoding="utf-8")) or {}
    if suffix in {".md", ".markdown"}:
        return extract_frontmatter(input_path)
    raise ValueError("Unsupported input format. Use JSON, YAML, or Markdown with YAML frontmatter.")


def extract_frontmatter(path: Path) -> Dict[str, object]:
    content = path.read_text(encoding="utf-8").lstrip()
    if not content.startswith("---"):
        return {}
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}
    fm = parts[1]
    if yaml is None:
        raise ImportError("pyyaml is required to parse Markdown frontmatter. Install with `pip install pyyaml`.")
    return yaml.safe_load(fm) or {}


def canonical_inputs(kind: str, metadata: Dict[str, object]) -> List[str]:
    fields = CANONICAL_FIELDS.get(kind)
    if not fields:
        raise ValueError(f"No canonical field mapping configured for kind '{kind}'.")

    normalized_inputs: List[str] = []
    for field_options in fields:
        value = extract_first(metadata, field_options)
        if field_options and "website" in field_options[0]:
            normalized_inputs.append(normalize_domain(value))
        else:
            normalized_inputs.append(normalize_value(value))
    return normalized_inputs


def derive_slug(kind: str, metadata: Dict[str, object], override: Optional[str]) -> str:
    if override:
        return normalize_slug(override)
    slug_value = (
        metadata.get("slug")
        or extract_first(metadata, CANONICAL_FIELDS.get(kind, [()])[0])
        or metadata.get("canonical_name_en")
        or metadata.get("name")
    )
    if not slug_value:
        raise ValueError("A slug or canonical name is required to mint an ID.")
    return normalize_slug(str(slug_value))


def compute_hash(canonical: str, length: int = 10) -> str:
    digest = hashlib.sha256(canonical.encode("utf-8")).digest()
    encoded = base64.b32encode(digest).decode("utf-8").rstrip("=").lower()
    return encoded[:length]


def build_entity_id(metadata: Dict[str, object], *, country_override: Optional[str], kind_override: Optional[str], slug_override: Optional[str]) -> Tuple[str, str, List[str]]:
    if metadata.get("entity_id"):
        raise ValueError("entity_id already present; refusing to remint.")
    kind = resolve_kind(metadata, kind_override)
    cc = resolve_country_code(metadata, country_override)
    slug = derive_slug(kind, metadata, slug_override)
    inputs = canonical_inputs(kind, metadata)
    canonical_string = "|".join([cc, kind, slug, *inputs])
    hash_part = compute_hash(canonical_string)
    entity_id = f"{cc}_{kind}_{slug}__{hash_part}"
    return entity_id, canonical_string, inputs


def lint_entities_csv(path: Path, repo_root: Path, known_ids: set[str]) -> List[LintIssue]:
    issues: List[LintIssue] = []
    with path.open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        headers = reader.fieldnames or []
        id_field = "entity_id" if "entity_id" in headers else next((h for h in headers if h.endswith("_id")), None)
        name_field = "canonical_name_en" if "canonical_name_en" in headers else "name" if "name" in headers else None
        city_field = "city" if "city" in headers else "hq_city_or_region" if "hq_city_or_region" in headers else None
        domain_field = "website" if "website" in headers else "website_domain" if "website_domain" in headers else None
        profile_field = "profile_path" if "profile_path" in headers else None

        domain_keys: Dict[str, str] = {}
        name_city_keys: Dict[Tuple[str, str], str] = {}

        for idx, row in enumerate(reader, start=2):  # header is row 1
            row_id = (row.get(id_field) or "").strip() if id_field else ""
            if row_id:
                known_ids.add(row_id)
            identifier = row_id or f"{path.name}#{idx}"

            name_val = normalize_value(row.get(name_field)) if name_field else "-"
            city_val = normalize_value(row.get(city_field)) if city_field else "-"
            domain_val = normalize_domain(row.get(domain_field)) if domain_field else "-"

            if domain_val not in {"-", ""}:
                if domain_val in domain_keys and domain_keys[domain_val] != identifier:
                    issues.append(
                        LintIssue(
                            path,
                            f"Duplicate website/domain '{domain_val}' for {domain_keys[domain_val]} and {identifier}.",
                        )
                    )
                else:
                    domain_keys[domain_val] = identifier

            if name_val not in {"-", ""} and city_val not in {"-", ""}:
                key = (name_val, city_val)
                if key in name_city_keys and name_city_keys[key] != identifier:
                    issues.append(
                        LintIssue(
                            path,
                            f"Duplicate name+city '{name_val} / {city_val}' for {name_city_keys[key]} and {identifier}.",
                        )
                    )
                else:
                    name_city_keys[key] = identifier

            if profile_field:
                profile_path = (row.get(profile_field) or "").strip()
                if not profile_path:
                    issues.append(LintIssue(path, f"Missing profile_path for {identifier}."))
                else:
                    profile_file = (repo_root / profile_path).resolve()
                    if not profile_file.exists():
                        issues.append(LintIssue(path, f"Profile path not found for {identifier}: {profile_path}."))
                    else:
                        fm = extract_frontmatter(profile_file)
                        if not fm:
                            issues.append(LintIssue(profile_file, f"No frontmatter found (expected for {identifier})."))
                        else:
                            front_id = str(fm.get("entity_id") or "").strip()
                            if front_id and row_id and front_id != row_id:
                                issues.append(
                                    LintIssue(
                                        profile_file,
                                        f"Frontmatter entity_id '{front_id}' does not match CSV '{row_id}'.",
                                    )
                                )
                            elif row_id and not front_id:
                                issues.append(
                                    LintIssue(profile_file, f"Frontmatter missing entity_id (CSV has '{row_id}').")
                                )
    return issues


def lint_relationships(path: Path, known_ids: set[str]) -> List[LintIssue]:
    issues: List[LintIssue] = []
    with path.open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        id_columns = [h for h in (reader.fieldnames or []) if "entity_id" in h]
        if not id_columns:
            return issues
        for idx, row in enumerate(reader, start=2):
            for col in id_columns:
                value = (row.get(col) or "").strip()
                if value and value not in known_ids:
                    issues.append(
                        LintIssue(
                            path,
                            f"Unknown entity_id '{value}' in column '{col}' at row {idx}.",
                        )
                    )
    return issues


def lint_repo(repo_root: Path, countries_filter: Optional[List[str]]) -> List[LintIssue]:
    issues: List[LintIssue] = []
    countries_path = repo_root / "countries"
    known_ids: set[str] = set()
    country_dirs = [p for p in countries_path.iterdir() if p.is_dir()]
    if countries_filter:
        allowed = {c.lower() for c in countries_filter}
        country_dirs = [p for p in country_dirs if p.name.lower() in allowed]

    for country_dir in country_dirs:
        entities_dir = country_dir / "data" / "entities"
        if not entities_dir.exists():
            continue
        for csv_path in entities_dir.glob("*.csv"):
            issues.extend(lint_entities_csv(csv_path, repo_root, known_ids))

        relationships = country_dir / "data" / "relationships.csv"
        if relationships.exists():
            issues.extend(lint_relationships(relationships, known_ids))
    return issues


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Mint deterministic IDs and lint entity registries.")
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="Path to the repository root (defaults to script parent).",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    mint = subparsers.add_parser("mint", help="Mint a deterministic entity_id.")
    mint.add_argument("input", type=Path, help="YAML/JSON/Markdown input containing entity metadata.")
    mint.add_argument("--kind", dest="kind_override", help="Override entity kind (defaults to entity_type/kind in input).")
    mint.add_argument("--country", dest="country_override", help="Override country code (defaults to cc/country in input).")
    mint.add_argument("--slug", dest="slug_override", help="Provide a slug override.")
    mint.add_argument("--json", dest="as_json", action="store_true", help="Emit JSON instead of text.")
    mint.add_argument("--show-canonical", action="store_true", help="Print canonical string inputs used for hashing.")

    lint = subparsers.add_parser("lint", help="Lint country registries for duplicates and ID mismatches.")
    lint.add_argument(
        "--country",
        action="append",
        dest="countries",
        help="Limit linting to specific country directories (repeatable). Defaults to all.",
    )

    return parser.parse_args(argv)


def command_mint(args: argparse.Namespace) -> int:
    metadata = load_metadata(args.input)
    try:
        entity_id, canonical, inputs = build_entity_id(
            metadata,
            country_override=args.country_override,
            kind_override=args.kind_override,
            slug_override=args.slug_override,
        )
    except Exception as exc:  # pragma: no cover - user facing
        sys.stderr.write(f"Mint failed: {exc}\n")
        return 1

    if args.as_json:
        payload = {"entity_id": entity_id, "canonical_string": canonical, "inputs": inputs}
        print(json.dumps(payload, indent=2))
    else:
        print(f"entity_id: {entity_id}")
        if args.show_canonical:
            print(f"canonical: {canonical}")
    return 0


def command_lint(args: argparse.Namespace) -> int:
    repo_root: Path = args.repo_root.resolve()
    issues = lint_repo(repo_root, args.countries)
    if issues:
        for issue in issues:
            print(issue.format())
        print(f"\nFound {len(issues)} issue(s).")
        return 1
    print("No lint issues found.")
    return 0


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    if args.command == "mint":
        return command_mint(args)
    if args.command == "lint":
        return command_lint(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
