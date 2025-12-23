#!/usr/bin/env python3
"""
Create/update an EventBridge schedule rule and attach a Lambda target by calling the AWS CLI.

This script uses `--cli-input-json` for both calls to avoid shell-escaping issues.

Example (config file):

  python scripts/schedules/create_eventbridge_rule.py \
    --config scripts/schedules/evolverecruiting-schedule.json
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
from typing import Any, Dict


def _run(cmd: list[str], *, dry_run: bool) -> None:
    if dry_run:
        print("[dry-run]", " ".join(cmd))
        return
    subprocess.run(cmd, check=True)


def _load_config(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        cfg = json.load(f)
    if not isinstance(cfg, dict):
        raise ValueError("Config must be a JSON object")
    return cfg


def _run_json(cmd: list[str], *, dry_run: bool) -> Dict[str, Any]:
    if dry_run:
        print("[dry-run]", " ".join(cmd))
        return {}
    out = subprocess.check_output(cmd)
    if not out:
        return {}
    parsed = json.loads(out)
    if not isinstance(parsed, dict):
        raise ValueError("AWS CLI JSON output was not an object")
    return parsed


def main() -> int:
    p = argparse.ArgumentParser(
        description="Create/update an EventBridge schedule rule and attach a Lambda target (via AWS CLI)."
    )
    p.add_argument(
        "--config",
        required=True,
        help="Path to JSON config containing rule and targets (see scripts/schedules/*.config.json)",
    )
    p.add_argument(
        "--update",
        action="store_true",
        help="Update mode: require the rule to exist and reconcile targets (remove targets not in config) before applying config",
    )

    p.add_argument(
        "--region",
        default=os.environ.get("AWS_REGION") or os.environ.get("AWS_DEFAULT_REGION"),
        help="AWS region (defaults to AWS_REGION/AWS_DEFAULT_REGION env var)",
    )
    p.add_argument(
        "--profile",
        help="AWS CLI profile name (optional)",
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="Print AWS CLI commands but do not execute them",
    )

    args = p.parse_args()

    try:
        cfg = _load_config(args.config)
    except Exception as e:
        print(f"Error: invalid config JSON: {e}", file=sys.stderr)
        return 2

    if "rule" not in cfg or "targets" not in cfg:
        print(
            "Error: config must contain top-level keys: 'rule' and 'targets'",
            file=sys.stderr,
        )
        return 2
    if not isinstance(cfg["rule"], dict) or not isinstance(cfg["targets"], dict):
        print("Error: 'rule' and 'targets' must be JSON objects", file=sys.stderr)
        return 2

    rule_payload: Dict[str, Any] = dict(cfg["rule"])
    targets_payload: Dict[str, Any] = dict(cfg["targets"])

    if "Name" not in rule_payload:
        print("Error: config.rule.Name is required", file=sys.stderr)
        return 2

    rule_name = rule_payload["Name"]
    event_bus_name = rule_payload.get("EventBusName", "default")

    # Ensure targets payload has the required envelope keys.
    targets_payload.setdefault("Rule", rule_name)
    targets_payload.setdefault("EventBusName", event_bus_name)

    targets = targets_payload.get("Targets")
    if not isinstance(targets, list) or not targets:
        print(
            "Error: config.targets.Targets must be a non-empty array", file=sys.stderr
        )
        return 2

    # EventBridge expects each target's Input to be a JSON string.
    for i, t in enumerate(targets):
        if not isinstance(t, dict):
            print(
                f"Error: config.targets.Targets[{i}] must be an object", file=sys.stderr
            )
            return 2
        if "Id" not in t or not isinstance(t["Id"], str) or not t["Id"]:
            print(
                f"Error: config.targets.Targets[{i}].Id is required",
                file=sys.stderr,
            )
            return 2
        if "Input" in t and not isinstance(t["Input"], str):
            t["Input"] = json.dumps(
                t["Input"], ensure_ascii=False, separators=(",", ":")
            )

    aws_base = ["aws"]
    if args.region:
        aws_base += ["--region", args.region]
    if args.profile:
        aws_base += ["--profile", args.profile]

    try:
        with tempfile.TemporaryDirectory() as td:
            rule_path = os.path.join(td, "put_rule.json")
            targets_path = os.path.join(td, "put_targets.json")
            with open(rule_path, "w", encoding="utf-8") as f:
                json.dump(rule_payload, f, ensure_ascii=False, indent=2)
            with open(targets_path, "w", encoding="utf-8") as f:
                json.dump(targets_payload, f, ensure_ascii=False, indent=2)

            if args.update:
                # Ensure the rule exists, then remove any targets not present in config.
                _run(
                    aws_base
                    + [
                        "events",
                        "describe-rule",
                        "--name",
                        str(rule_name),
                        "--event-bus-name",
                        str(event_bus_name),
                    ],
                    dry_run=args.dry_run,
                )

                desired_ids = {
                    t["Id"] for t in targets if isinstance(t, dict) and "Id" in t
                }
                list_out = _run_json(
                    aws_base
                    + [
                        "events",
                        "list-targets-by-rule",
                        "--rule",
                        str(rule_name),
                        "--event-bus-name",
                        str(event_bus_name),
                    ],
                    dry_run=args.dry_run,
                )
                existing = list_out.get("Targets", [])
                existing_ids = {
                    t.get("Id")
                    for t in existing
                    if isinstance(t, dict) and isinstance(t.get("Id"), str)
                }
                to_remove = sorted(
                    i for i in existing_ids if i and i not in desired_ids
                )
                if to_remove:
                    _run(
                        aws_base
                        + [
                            "events",
                            "remove-targets",
                            "--rule",
                            str(rule_name),
                            "--event-bus-name",
                            str(event_bus_name),
                            "--ids",
                            *to_remove,
                        ],
                        dry_run=args.dry_run,
                    )

            _run(
                aws_base
                + ["events", "put-rule", "--cli-input-json", f"file://{rule_path}"],
                dry_run=args.dry_run,
            )
            _run(
                aws_base
                + [
                    "events",
                    "put-targets",
                    "--cli-input-json",
                    f"file://{targets_path}",
                ],
                dry_run=args.dry_run,
            )
    except FileNotFoundError:
        print(
            "Error: AWS CLI not found. Install/configure `aws` and try again.",
            file=sys.stderr,
        )
        return 127
    except subprocess.CalledProcessError as e:
        print(
            f"Error: AWS CLI command failed with exit code {e.returncode}",
            file=sys.stderr,
        )
        return e.returncode

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
