# Outbound mobility baseline — Jordan (data gaps flagged)

Last updated: 2026-02-04. This page aligns to [`countries/jordan/reports/2025-12-20 - Jordan Outbound Mobility Baseline.md`](../reports/2025-12-20%20-%20Jordan%20Outbound%20Mobility%20Baseline.md) and highlights what is known vs missing.

## Fast source orientation (what we can cite confidently)
- **Global outbound headline (provisional):** **33,277 Jordan tertiary students abroad (2022)** cited in the U.S. International Trade Administration 2025 guide (attributed to UNESCO) — **treat as provisional until a direct UNESCO UIS extract is pulled.**
- **Host-specific confirmed signal:** **2,643 Jordanian students in the U.S. (2023/24)** with a graduate-heavy mix (Open Doors; cited in the 2025 report). Use as a directional benchmark for postgraduate appetite.
- **Eurostat status (checked 2026-02-04):** The Eurostat `educ_uoe_mobs02` API returns **no observations for partner=Jordan, 2023**; the dataset structure lists reporting geos but the `value` object is empty. This means prior Eurostat-like tables in the report are **not evidence-backed** and must be replaced once a valid extract exists.
- **Methodology anchors:** Degree-mobile students, origin defined by prior education/usual residence; keep host-side vs origin-side sources clearly labeled.

## Immediate data remediation plan
1. **Pull UNESCO UIS outbound totals + Top destinations (latest year available)** to replace the provisional ITA citation and populate Greece/Cyprus visibility.  
2. **Re-attempt Eurostat or alternate EU mobility sources** once partner-level coverage for Jordan is confirmed; if Eurostat remains empty, document that as an explicit limitation.  
3. **Host-side extracts to prioritise:** U.S. Open Doors (already cited), Türkiye YÖK/ÖSYM, Germany (DESTATIS/DAAD), KSA/UAE visa/student permit stats, UK HESA, and Greece/Cyprus student visa/residence permit counts.  
4. **Field-of-study gap:** Collect field splits where hosts publish them (U.S. Open Doors fields, DAAD fields, UK CAH/HECoS where available) to replace the current proxy-only guidance.

## Directional picture to steer recruitment while data is refreshed
- **Primary gravity:** U.S., UK, Canada, Australia, Germany, and Türkiye remain major destinations per counselor/agent feedback and available host stats; Gulf universities and scholarships also capture demand, especially for cost-sensitive families.
- **Greece/Cyprus corridor:** No reliable 2023 counts yet; treat corridor as **to-be-quantified** and track via visa/residence data and agent CRM conversions until official stats are available.
- **Program/level tilt:** Postgraduate and STEM demand is consistently reported by agents; medicine/dentistry interest is high but bounded by recognition/placement constraints.

## How to use this page until the refresh is complete
- **Be transparent with stakeholders:** state that Eurostat currently has **no Jordan data** and that prior tables are placeholders.  
- **Anchor comms on confirmed numbers** (e.g., U.S. 2,643) and on qualitative signals from the premium school/agent network documented elsewhere in `countries/jordan`.  
- **Update this file and the baseline report** once UIS/host-side extractions are complete; keep a changelog in the ticket or `executions/` notes.
