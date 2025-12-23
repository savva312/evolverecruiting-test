# T-495: Jordan — rebuild Medicine/MD competitor set (correct institutions + sources)

Status: done
Type: content
Priority: P0
Dependencies: (none)
Claimed-by: evoticketresolver_li3uc6_0
Claimed-at: 2025-12-22T20:45:02Z
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Replace inaccurate content in `countries/jordan/program-clusters/medicine-md/competitors.md` with a Jordan-relevant, sourced competitor set for English-taught Medicine/MD decisions.

This should become a doc that admissions + marketing can safely use when counseling Jordanian families.

---

## Context

`countries/jordan/program-clusters/medicine-md/competitors.md` currently contains fabricated “Jordan” institutions (e.g., “Medical University of Amman”) but cites Bulgarian medical university sources (e.g., `mu-sofia.bg`, `mu-varna.bg`, `mu-plovdiv.bg`). This is a high-risk factual error.

In-repo references that should inform the rebuild:
- Jordan market: `countries/jordan/market/recognition-and-licensure.md` (currently a placeholder; treat as gap)
- Jordan competitors data: `countries/jordan/data/entities/competitors.csv`
- Existing competitor profiles: `countries/jordan/entities/competitors/profiles/**`

---

## Allowed write paths

- `tickets/T-495-jordan-medicine-competitor-set-rebuild.md`
- `countries/jordan/program-clusters/medicine-md/competitors.md`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**` (global)
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- `countries/**` (except `countries/jordan/**`)

---

## Required outputs

- `countries/jordan/program-clusters/medicine-md/competitors.md` updated with a correct, sourced competitor set.

---

## Acceptance criteria

- [x] The doc contains **no** fabricated Jordan institutions and **no** Bulgaria-medical-university sources incorrectly tied to Jordan cities.
- [x] Each competitor entry includes: location, language of instruction, admissions requirements (high-level), tuition range (only if sourced), and a Jordan-relevant “why families choose it” note.
- [x] Each entry has at least 1 authoritative source link, with a `last_verified` date (or a single “last updated” section plus inline source links).
- [x] The competitor set includes Jordan-local options and the most common regional alternatives Jordanian families consider (not only CEE/EU).

---

## What changed (2025-12-22)
- Rebuilt `countries/jordan/program-clusters/medicine-md/competitors.md` with a Jordan-relevant competitor set and authoritative source links; removed fabricated “Jordan” institutions and Bulgaria-only sources misattributed to Jordan.
- Note: `countries/jordan/program-clusters/medicine-md/jordan-playbook.md` still references the fabricated institutions; this needs a separate scoped ticket to fix (outside this ticket’s allowed paths).
