"""Generate an execution order JSON for tickets marked `on-deck`.

The script scans top-level `tickets/T-*.md` files, filters tickets whose
`Status:` is `on-deck`, and writes a JSON file under
`tickets/executionorders/` named:

    YYYYMMDD - Agent Execution Order - Epoch <epoch>.json

Epoch is derived from 30-minute intervals starting at 00:00 UTC
(`epoch = floor(minutes_since_midnight / 30)`).
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
from pathlib import Path
from typing import Iterable, List, Optional, TypedDict


EVO_RESEARCHER = "EvoResearcher"
EVO_TICKET_RESOLVER = "EvoTicket Resolver"

MODEL_MAPPING = {
    EVO_RESEARCHER: {
        "manager": "GPT 5.2 (H)",
        "analyst": "GPT 5.2 (H)",
    },
    EVO_TICKET_RESOLVER: {
        "agent": "GPT 5.1 Codex",
    },
}


class TicketEntry(TypedDict):
    ticket_id: str
    title: str
    status: str
    agent: str
    models: dict
    body: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Emit a JSON execution order for on-deck tickets."
    )
    parser.add_argument(
        "--tickets-dir",
        type=Path,
        default=Path("tickets"),
        help="Path to the tickets directory (default: ./tickets).",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("tickets/executionorders"),
        help="Directory where the JSON file will be written.",
    )
    parser.add_argument(
        "--timestamp",
        type=str,
        default=None,
        help="Override UTC timestamp (ISO 8601). Defaults to current UTC time.",
    )
    return parser.parse_args()


def parse_timestamp(timestamp_str: Optional[str]) -> dt.datetime:
    if timestamp_str is None:
        return dt.datetime.now(tz=dt.timezone.utc)

    try:
        parsed = dt.datetime.fromisoformat(
            timestamp_str.replace("Z", "+00:00")
        ).astimezone(dt.timezone.utc)
    except ValueError as exc:
        raise SystemExit(f"Invalid timestamp format: {timestamp_str}") from exc
    return parsed


def compute_epoch_index(ts: dt.datetime) -> int:
    minutes_since_midnight = ts.hour * 60 + ts.minute
    return minutes_since_midnight // 30


def find_line_value(text: str, label: str) -> Optional[str]:
    match = re.search(rf"^{re.escape(label)}:\s*(.+)$", text, re.MULTILINE)
    return match.group(1).strip() if match else None


def parse_ticket(path: Path) -> Optional[TicketEntry]:
    content = path.read_text(encoding="utf-8")
    status = find_line_value(content, "Status")
    if not status or status.strip().lower() != "on-deck":
        return None

    agent = find_line_value(content, "Agent") or "Unknown"
    header_match = re.search(r"^#\s+(T-\d+):\s*(.+)$", content, re.MULTILINE)
    if not header_match:
        return None

    ticket_id, title = header_match.group(1), header_match.group(2).strip()
    models = MODEL_MAPPING.get(agent, {})

    return TicketEntry(
        ticket_id=ticket_id,
        title=title,
        status=status.strip(),
        agent=agent,
        models=models,
        body=content.strip(),
    )


def gather_on_deck_tickets(tickets_dir: Path) -> List[TicketEntry]:
    ticket_files: Iterable[Path] = tickets_dir.glob("T-*.md")
    entries: List[TicketEntry] = []
    for path in sorted(ticket_files):
        ticket = parse_ticket(path)
        if ticket:
            entries.append(ticket)
    return entries


def build_output_filename(ts: dt.datetime, epoch_index: int) -> str:
    date_str = ts.strftime("%Y%m%d")
    return f"{date_str} - Agent Execution Order - Epoch {epoch_index}.json"


def main() -> None:
    args = parse_args()
    timestamp = parse_timestamp(args.timestamp)
    epoch_index = compute_epoch_index(timestamp)

    entries = gather_on_deck_tickets(args.tickets_dir)

    payload = {
        "generated_at_utc": timestamp.isoformat().replace("+00:00", "Z"),
        "epoch_index": epoch_index,
        "tickets": entries,
    }

    output_dir: Path = args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / build_output_filename(timestamp, epoch_index)

    output_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"Wrote {output_path} with {len(entries)} on-deck ticket(s).")


if __name__ == "__main__":
    main()
