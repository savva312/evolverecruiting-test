---
name: program-clusters-and-competitor-sets
description: Define and maintain program clusters and competitive sets for UNIC and UNIC Athens recruiting across markets, including workflows, datasets, and reusable templates.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: global
license: Proprietary (UNIC Evolve internal)
---

# Program clusters and competitor sets (global skill)

This skill defines how EvoBuilder should organize recruiting intelligence by **program cluster** (e.g., Medicine vs CS/Data vs Business) and maintain a **market-relevant competitive set** for each cluster.

It exists because families shortlist **by program**, not by university brand alone. Each cluster has its own competitor set, admissions signals, and channel mix; treating them separately keeps positioning credible and repeatable across markets.

---

## When to use this skill

Use this skill when a ticket asks for any of:

- “Define / refine program clusters”
- “Build competitor set for cluster X”
- “Update UNIC / UNIC Athens program portfolio mapping”
- “Write cluster strategy, positioning, and message”
- “Create competitor profiles for decision makers”
- “Update pricing + language-of-instruction tables by cluster”

---

## Core definitions

### Program cluster
A **program cluster** is a stable grouping of programs that share:

- A similar buyer journey (student/parent motivations, timing, proof needed)
- A similar admissions pathway (tests/interviews/portfolio, documents)
- A similar competitor set (destinations and institutions considered)
- A similar channel mix (schools vs agents vs performance marketing)

A cluster is *not* a faculty org chart. It’s a recruiting segmentation tool.

### Competitive set
A **competitive set** is the short list of institutions/programs families *actually compare* against UNIC Athens / UNIC Nicosia for that cluster.

It should be:
- **Market-relevant** (realistic shortlists for the country in scope)
- **Program-specific** (Medicine set ≠ CS set ≠ Business set)
- **Right-sized** (20–40 meaningful competitors per cluster is usually enough; avoid indexing the world)

### Baseline cluster families (adapt per country)

Use these as a starting point, then localize in each country addendum:

1. **medicine-and-health** — MD and other health/allied health programs
2. **computing-data-ai** — CS, Data Science, AI-adjacent programs, Cybersecurity (if offered)
3. **business-economics-finance** — Business Admin, Accounting, Marketing, Finance, Econ-related
4. **psychology-and-social-sciences** — Psychology and adjacent social science programs
5. **law-and-governance** — Law programs where relevant
6. **design-and-creative** — Design and creative media programs marketed internationally
7. **other-strategic-programs** — Only when there is a clear demand signal and distinct competitor set

**Rule:** If a “cluster” doesn’t change the competitor set or channel strategy, it’s probably not a separate cluster.

Document any country-specific deviations in the country skill note or addendum.

---

## Inputs EvoBuilder should gather (minimum viable)

For each UNIC program in scope (Nicosia and Athens):

- Program name
- Degree type (BSc/BA/MSc/MD/etc.)
- Campus / delivery location
- Language(s) of instruction
- Intake(s) and typical application timing
- Published tuition and required fees
- Admissions requirements (high-level)
- For regulated professions: recognition/licensure path notes (high-level, link-only, no legal claims)

For each competitor program in a cluster:

- Institution + campus/city
- Program name and degree type
- Language of instruction
- Published tuition
- Selection mechanism (exam/interview/portfolio/fixus/other)
- “Why it competes” (the reason local families compare it)
- Source links

**Important:** never “estimate” tuition or admissions rules. Use primary sources.

---

## Where to write outputs

Follow the **ticket’s allowed write paths**.

If not specified, typical locations are:

- Cluster overviews: `<country>/program-clusters/<cluster>/cluster.md`
- Cluster competitive sets: `<country>/program-clusters/<cluster>/competitors.md`
- Competitor institution profiles: `<country>/entities/competitors/profiles/<institution>.md`
- Structured tables:
  - UNIC portfolio (by campus): `data/unic_programs.csv` or `<country>/data/unic_programs.csv`
  - Competitor programs: `<country>/data/competitor_programs.csv`
  - Cluster mapping: `<country>/data/program_cluster_map.csv`

If these folders don’t exist yet, only create them if the ticket explicitly allows path creation.

---

## Step-by-step procedure

### Step 1 — Confirm the ticket boundary
Before writing anything:
- Identify the target cluster(s)
- Identify the allowed write paths
- Identify required outputs (MD vs CSV vs both)
- Identify the “definition of done” for the ticket

Do not write outside the allowed paths.

### Step 2 — Build the UNIC program-to-cluster map
Create a simple mapping table for the cluster:

- Include **both** UNIC Nicosia and UNIC Athens when relevant
- If a program exists in one campus only, note that explicitly
- Capture language-of-instruction and tuition (published)

This table becomes the anchor for everything else.

### Step 3 — Define the local decision logic for the cluster
Write (briefly, but concretely):

- Student persona(s) for this cluster
- What “proof” they demand (e.g., clinical placements, internships, portfolio outcomes)
- Typical timing constraints (exam periods, counselor scheduling, decision deadlines)
- Common objections and what evidence resolves them

### Step 4 — Build the competitive set (cluster-specific)
Create a competitor list using locally relevant buckets (adapt per country), such as:

- Domestic options (only if they truly compete)
- Neighboring or regional options
- Cyprus and Greece options
- Western Europe / other international options where brand/capacity make them appear on shortlists
- Private English-taught institutions that the target market actually considers

For each competitor, record:
- why it competes for this cluster (one sentence)
- a source link for tuition + admissions mechanism

Avoid “random lists”. Every competitor must be justified by market relevance.

### Step 5 — Write the cluster overview MD
Create or update `<country>/program-clusters/<cluster>/cluster.md` with:

- What’s in this cluster (programs at UNIC Athens / UNIC Nicosia)
- Local buyer journey summary
- Competitive set summary (with categories)
- Positioning notes (what UNIC can credibly claim)
- Messaging angles (parent/student-ready themes)
- Data gaps / next research tickets to open

### Step 6 — Create competitor profiles (only for top competitors)
Do not create profiles for every competitor immediately.

Instead:
- Pick the top ~10–20 “most compared” competitors for the cluster
- Create one MD profile per institution, with program-specific sections where needed

### Step 7 — Update structured CSVs
Update the relevant CSV(s) so we can:

- filter competitor set by cluster
- sort by tuition
- see language-of-instruction quickly
- maintain a durable dataset as the repo grows

### Step 8 — Quality checks
Before finishing:

- Check that every tuition and admissions claim has a source
- Check that the competitor list is cluster-specific (not copy/paste)
- Check that Athens vs Nicosia differences are explicit
- Check file naming, links, and cross-references

---

## Templates

### Template: Cluster overview (`<country>/program-clusters/<cluster>/cluster.md`)

## Cluster: <name>

### 1) What’s in scope (UNIC Athens + UNIC Nicosia)
| Program | Campus | Degree | Language | Intakes | Tuition | Source |
|---|---|---|---|---|---|---|

### 2) Local decision journey (what matters)
- Personas:
- Proof required:
- Timing constraints:
- Objections:

### 3) Competitive set (market-relevant)
#### A) Neighboring / regional options
- ...
#### B) Cyprus and/or Greece
- ...
#### C) Western Europe / other international
- ...
#### D) Domestic (only if relevant)
- ...

### 4) Positioning and messaging
- Where UNIC Athens wins:
- Where UNIC Nicosia wins:
- What not to claim (or needs verification):

### 5) Operational implications
- Best channels:
- School/agent implications:
- Content assets needed:

### 6) Open questions / next tickets
- T-XXX: ...
- T-YYY: ...

---

### Template: Competitor profile (`<country>/entities/competitors/profiles/<institution>.md`)

# <Institution name> (Competitor)

## Why it matters for <country> (cluster-specific)
- Cluster(s):
- Why students compare it:

## Programs that compete (market-relevant only)
| Program | Degree | Language | City | Tuition | Admissions mechanism | Source |
|---|---|---|---|---|---|---|

## Notes for recruiters
- Strengths vs UNIC:
- Weaknesses / friction:
- Common misconceptions to correct:
- What evidence is needed to compare fairly:

## Source log
- <link 1>
- <link 2>

---

## Done criteria (for a “good” ticket outcome)

A ticket using this skill is complete when:

- A cluster file exists/updated with a clean UNIC program mapping table
- A competitive set exists with justified, market-relevant competitors
- Top competitors have profiles (as required by the ticket)
- CSVs are updated so the repo can be queried and maintained
- Sources are included for all factual claims

---

## Common failure modes to avoid

- Using one generic competitor list for every program
- Mixing multiple countries into one artifact without clear scoping
- Listing competitors without explaining why they compete
- Writing strategy without updating CSVs (the repo becomes non-operational)
- Writing outside ticket boundaries
