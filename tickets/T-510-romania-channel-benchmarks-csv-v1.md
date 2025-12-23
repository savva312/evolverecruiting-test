# T-510: Romania — populate `countries/romania/data/marketing/channel-benchmarks.csv` (v1)

Status: open
Type: data
Priority: P2
Dependencies: (none)
Claimed-by:
Claimed-at:
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Populate `countries/romania/data/marketing/channel-benchmarks.csv` with initial KPI guardrails for Romania campaigns that are usable for weekly management:
- Meta (FB/IG): CPM/CPC/CPL ranges by objective
- Google Search: CPC/CTR/CPL ranges by intent bucket (brand vs non-brand)
- TikTok: CPM/CPC/CPL and video completion ranges
- YouTube: CPV/CTR and video action conversion notes
- LinkedIn: CPC/CPL ranges for parent/counselor targeting

All ranges must have either a source link or be explicitly labeled as “starting assumption” in `notes` (with a plan to validate).

---

## Context

Related Romania docs:
- `countries/romania/go-to-market/digital-playbook/channel-strategy.md` references this CSV.
- CSV scaffold: `countries/romania/data/marketing/channel-benchmarks.csv`
- Dictionary scaffold: `countries/romania/data/marketing/channel-benchmarks-dictionary.md`

---

## Allowed write paths

- `tickets/T-451-romania-channel-benchmarks-csv-v1.md`
- `countries/romania/data/marketing/channel-benchmarks.csv`
- `countries/romania/data/marketing/channel-benchmarks-dictionary.md`
- `executions/**` (optional for notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `.github/**`
- `scripts/**`
- `tickets/**` (except this ticket file)
- `countries/**` (except `countries/romania/data/marketing/**`)

---

## Required outputs

- Updated `countries/romania/data/marketing/channel-benchmarks.csv` (minimum: 25 rows covering core channels/objectives)
- Updated `countries/romania/data/marketing/channel-benchmarks-dictionary.md`

---

## Acceptance criteria

- [ ] Benchmarks cover Meta, Search, TikTok, YouTube, and LinkedIn with Romania-relevant ranges.
- [ ] Every row has an `as_of` date and a `source` or an explicit “assumption” note.
- [ ] Dictionary matches dataset exactly.
- [ ] No edits outside allowed paths.

