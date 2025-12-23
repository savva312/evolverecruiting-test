# Outbound mobility baseline — Lebanon (data collection plan)

Last updated: 2025-12-20. This file defines the Lebanon-specific outbound mobility evidence pack we need before crafting channel and program bets for UNIC and UNIC Athens.

## Data to pull (sources)
- **UNESCO UIS outbound students** (latest available year, all hosts). Capture total outbound, top 10 destinations, and field-of-study splits if present.
- **Eurostat `educ_uoe_mobs02`** (if Lebanon is covered) to compare EU-host volumes, especially Greece and Cyprus. Flag coverage gaps.
- **National sources**: Ministry of Education and Higher Education (MEHE) statistics, Banque du Liban student loan data (if published), and press releases on scholarship schemes (e.g., CNRS-L, Eiffel/DAAD/Chevening award counts).
- **Host-side stats**: Greece/Cyprus higher-ed agencies or universities reporting Lebanon enrollments; Erasmus+ mobility calls for Lebanese institutions.

## Working hypotheses to validate
- **Destinations likely to dominate:** France and Canada (language ties and historical migration), Gulf states for vocational/medical pathways, plus Germany/Netherlands/Italy for EU options; validate ranking with UIS/Eurostat pulls.
- **Drivers:** affordability pressures (currency devaluation), desire for employability and residence rights, and existing family/expat networks in Beirut, Tripoli, Saida, Zahle, and Tyre.
- **For UNIC/UNIC Athens:** English-medium delivery, predictable tuition, and Schengen/Cyprus/Greece access are differentiators; need evidence on recognition and residence paperwork for Lebanese passport holders.

## Output format
- **Structured tables** (CSV) summarizing outbound totals, destination ranks, and Greece/Cyprus positioning.
- **Narrative summary** distilling trends, constraints (visa/finance), and program clusters with demand signals.
- **Assumption log** noting any estimates until official data arrives.

## Immediate next steps
1) Extract UIS latest outbound table for Lebanon; log year/version and any suppression flags.  
2) Check Eurostat coverage; if unavailable, document as gap and rely on UIS + host-side stats.  
3) Request/collect Greece and Cyprus enrollment figures for Lebanese students from official sources or recent press.  
4) Draft a 1–2 page summary with destination ranks and implications for program clusters (medicine, business, ICT/data, design/creative media) with clear caveats.  
5) Version outputs in `countries/lebanon/reports/` and cite sources in-line.
