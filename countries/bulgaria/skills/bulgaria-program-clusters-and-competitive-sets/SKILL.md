---
name: bulgaria-program-clusters-and-competitive-sets
description: Define and maintain Bulgaria-specific program clusters and competitive sets for recruiting, including competitor mapping and portfolio alignment.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: bulgaria
---

# Bulgaria Program Clusters and Competitive Sets

This skill defines how EvoBuilder should organize Bulgaria recruitment intelligence by **program cluster** (e.g., Medicine vs CS/Data vs Business) and maintain a **Bulgaria-relevant competitive set** for each cluster.

It exists because Bulgarian families do not “choose a university” in the abstract — they shortlist **by program**, and the competitor set for Medicine is completely different from the competitor set for CS/Data, Psychology, Business, etc.

---

## How this relates to the global skill

Use the global workflow in [`skills/program-clusters-and-competitor-sets/SKILL.md`](/skills/program-clusters-and-competitor-sets/SKILL.md) for definitions, steps, and templates. This Bulgaria file serves as a country addendum: keep Bulgaria-specific cluster taxonomy choices and any Bulgaria-only nuances here, and point tickets to the global skill for the end-to-end process.

---

## When to use this skill

Use this skill when a ticket asks for any of:

- “Define / refine program clusters”
- “Build competitor set for cluster X”
- “Update UNIC / UNIC Athens program portfolio mapping”
- “Write cluster strategy, positioning, and message”
- “Create competitor profiles for Bulgaria decision makers”
- “Update pricing + language-of-instruction tables by cluster”
- “Compare UNIC Athens vs UNIC Nicosia vs competitors (Bulgaria lens)”

---

## Core definitions

### Program cluster
A **program cluster** is a stable grouping of programs that share:

- A similar Bulgaria buyer journey (student/parent motivations, timing, proof needed)
- A similar admissions pathway (tests/interviews/portfolio, documents)
- A similar competitor set (destinations and institutions considered)
- A similar channel mix (schools vs agents vs performance marketing)

A cluster is *not* a faculty org chart. It’s a recruitment segmentation tool.

### Competitive set
A **competitive set** is the small list of institutions/programs Bulgarian families *actually compare* against UNIC Athens / UNIC Nicosia for that cluster.

It should be:
- **Bulgaria-relevant** (realistic shortlists for Bulgarian candidates)
- **Program-specific** (Medicine set ≠ CS set ≠ Business set)
- **Right-sized** (20–40 meaningful competitors per cluster is usually enough; don’t try to index the world)

---

## Recommended cluster set for Bulgaria recruiting repos

See the country addendum below for the Bulgaria-specific cluster taxonomy currently in use. Use the global baseline unless Bulgaria-specific demand signals require a different grouping.

---

## Inputs EvoBuilder should gather (minimum viable)

For each program in scope (UNIC Nicosia and UNIC Athens):

- Program name
- Degree type (BSc/BA/MSc/MD/etc.)
- Campus / delivery location (Nicosia vs Athens)
- Language(s) of instruction (English/Greek/etc.)
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
- “Why it competes” (the reason BG families compare it)
- Source links

**Important:** never “estimate” tuition or admissions rules. Use primary sources.

---

## Where to write outputs

Follow the **ticket’s allowed write paths**.

If not specified, typical locations in this repo type are:

- Cluster overviews: `program-clusters/<cluster>.md`
- Competitor institution profiles: `entities/competitors/<institution>.md`
- Structured tables:
  - UNIC portfolio (by campus): `data/unic_programs.csv`
  - Competitor programs: `data/competitor_programs.csv`
  - Cluster mapping: `data/program_cluster_map.csv`

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

### Step 3 — Define Bulgaria decision logic for the cluster
Write (briefly, but concretely):

- Bulgaria student persona(s) for this cluster
- What “proof” they demand (e.g., clinical placements for MD; internships for CS; portfolio outcomes for Design)
- Typical timing constraints (exam periods, counselor scheduling, decision deadlines)
- Common objections and what evidence resolves them

### Step 4 — Build the competitive set (cluster-specific)
Create a competitor list using these buckets (adapt per cluster):

- **Bulgaria domestic** options (when they truly compete)
- **Greece** (especially Athens/Thessaloniki) options
- **Cyprus** options
- **CEE** options (common for Medicine especially)
- **Western Europe** options (Germany/NL/etc.) when capacity/brand makes them appear on Bulgarian shortlists
- **Private EU English-taught** institutions that Bulgaria families actually consider

For each competitor, record:
- why it competes for this cluster (one sentence)
- a source link for tuition + admissions mechanism

Avoid “random lists”. Every competitor must be justified by Bulgaria relevance.

### Step 5 — Write the cluster overview MD
Create or update `program-clusters/<cluster>.md` with:

- What’s in this cluster (programs at UNIC Athens / UNIC Nicosia)
- Bulgaria buyer journey summary
- Competitive set summary (with categories)
- Positioning notes (what UNIC can credibly claim)
- Messaging angles (Bulgarian parent/student-ready themes)
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

### Template: Cluster overview (`program-clusters/<cluster>.md`)

## Cluster: <name>

### 1) What’s in scope (UNIC Athens + UNIC Nicosia)
| Program | Campus | Degree | Language | Intakes | Tuition | Source |
|---|---|---|---|---|---|---|

### 2) Bulgaria decision journey (what matters)
- Personas:
- Proof required:
- Timing constraints:
- Objections:

### 3) Competitive set (Bulgaria-relevant)
#### A) Greece
- ...
#### B) Cyprus
- ...
#### C) CEE / Other EU
- ...
#### D) Bulgaria domestic (only if relevant)
- ...

### 4) Positioning and messaging (Bulgaria lens)
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

### Template: Competitor profile (`entities/competitors/<institution>.md`)

# <Institution name> (Competitor)

## Why it matters for Bulgaria (cluster-specific)
- Cluster(s):
- Why Bulgarian students compare it:

## Programs that compete (Bulgaria-relevant only)
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
- A competitive set exists with justified, Bulgaria-relevant competitors
- Top competitors have profiles (as required by ticket)
- CSVs are updated so the repo can be queried and maintained
- Sources are included for all factual claims

---

## Common failure modes to avoid

- Using one generic competitor list for every program
- Mixing “Europe recruiting” generalities into Bulgaria-specific artifacts
- Listing competitors without explaining why Bulgarians compare them
- Writing strategy without updating CSVs (the repo becomes non-operational)
- Writing outside ticket boundaries

---

## Bulgaria addendum: cluster taxonomy and notes

Use this grouping when working in Bulgaria unless a ticket specifies otherwise:

1. **medicine-and-health**
   - Includes MD and any health/allied health programs marketed to Bulgaria.
2. **computing-data-ai**
   - CS, Data Science, AI-adjacent programs, Cybersecurity (if offered).
3. **business-economics-finance**
   - Business Admin, Accounting, Marketing, Finance, Econ-related.
4. **psychology-and-social-sciences**
   - Psychology and closely adjacent social science programs.
5. **law-and-governance**
   - Law programs where Athens/Nicosia differences matter for Bulgaria prospects.
6. **design-and-creative**
   - Design and creative programs marketed to Bulgaria.
7. **other-strategic-programs**
   - Only when a Bulgaria demand signal and distinct competitor set are documented (e.g., Pharmacy if actively marketed).

If a proposed “cluster” would not change the competitive set or channel strategy for Bulgaria, keep it inside an existing cluster.

---

## Notes for EvoBuilder behavior

- Always prefer **small, correct, well-sourced** competitor sets over huge lists.
- Bulgaria relevance is the filter: if you can’t explain why it competes, omit it.
- Write in a way a recruiter can act on: contacts, deadlines, differences, proof points.
- Keep cluster artifacts stable; iterate via tickets rather than rewriting everything.
