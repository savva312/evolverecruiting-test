---
name: lebanon-unic-portfolio-pricing-and-language
description: Capture Lebanon-facing messaging on UNIC/UNIC Athens programs, pricing, scholarships, and language positioning.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: lebanon
---

# Lebanon UNIC portfolio, pricing, and language

## Purpose

Equip recruiters with Lebanon-ready facts on program availability (UNIC Nicosia vs UNIC Athens), language of instruction, tuition/fees, and any published scholarships or discounts.

## How to use

- Track program facts in CSVs under `countries/lebanon/data/programs/` (e.g., `unic_programs.csv`, optional `unic_scholarships_and_discounts.csv`) using the global data-model standards.
- Keep Lebanon messaging, FAQs, and positioning by cluster inside `countries/lebanon/program-clusters/<cluster>/` playbooks, linking back to the fact tables instead of duplicating numbers.
- Cite official UNIC/UNIC Athens sources for every tuition or policy reference and add `last_verified` dates; remove unverifiable claims.
- Call out campus differences explicitly (Nicosia vs Athens) and align recognition/licensure references with the Lebanon addendum for that skill.
