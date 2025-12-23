---
name: education-system-and-calendar
description: Global procedure for documenting a country’s education system and recruiting-relevant academic calendar (windows, blackouts, credential context) in reusable Markdown and CSV formats.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: global
---

# Education system and calendar (global)

## Goal

Create country-level reference materials that tell recruiting teams:

- **How the local secondary system works** (school types, credentials, grading).
- **When students and schools are available** (term structure, breaks, national and international exam windows, holidays).
- **Operational implications** for UNIC / UNIC Athens outreach, visits, and deadlines.

Use this skill as the canonical workflow; add only country-specific notes in the corresponding `/country/skills/<country>-education-system-and-calendar` file.

---

## Before you start

1) **Read the ticket you’re executing** for allowed paths, outputs, and intake years.
2) Review supporting skills as needed:
   - `/skills/ticket-boundaries/SKILL.md`
   - `/skills/assets-and-sources/SKILL.md`
   - `/skills/markdown-authoring/SKILL.md`

If any required inputs are missing, escalate in the ticket before proceeding.

---

## Inputs

- Target intake cycle(s) (e.g., Fall 2026, Spring 2027).
- Target segments (UG, Graduate, Medicine, etc.).
- Target geographies or feeder schools (if any).
- Program portfolio considerations (if provided).

Assume at least the current school year plus the next recruiting cycle if not specified.

---

## Outputs

Create the following unless the ticket narrows scope:

1) **Education system note (Markdown)** — recruiter-facing explainer of pathways, school types, credentials, and grading.
2) **Academic calendar dataset (CSV)** — structured events and date ranges to power planning and automation.
3) **Windows & blackouts note (Markdown)** — concise operational guidance derived from the dataset.

### Default file patterns (adjust if the ticket specifies others)

- `/{{country}}/market/education-system.md`
- `/{{country}}/market/education-calendar.md`
- `/{{country}}/data/calendar/{{country}}-academic-calendar.csv`

> Keep file names stable so dashboards and downstream scripts can rely on them.

---

## What to capture (content checklist)

### A) Education system essentials

- **Structure and terminology:** what grades define upper secondary; typical graduation ages; local naming for school stages.
- **School types relevant to recruiting:** public vs. private, specialist schools (language, STEM, vocational), international schools.
- **Common curricula:** national curriculum plus any IB/Cambridge/other international tracks used by target feeders.
- **Credentials and grading:** diploma/transcript names, grading scales, any official descriptors for performance bands.
- **Key national assessments:** names, grade levels affected, and why they matter for scheduling.

### B) Calendar items (recruiting impact)

- School year start/end.
- Official breaks/vacations.
- National exam windows and results release periods.
- International curriculum exam windows (IB, Cambridge, AP where relevant).
- Public holidays that materially affect attendance.
- Resulting **best visit windows** and **blackout/limited windows**.

---

## Sources and evidence rules

- Prefer **primary sources** (education ministries, exam boards, official school calendars).
- For each event record:
  - `source_url`
  - `publisher` (authority name)
  - `last_verified` (ISO date)
- If only PDFs are available:
  - Link the PDF as the source.
  - Extract the minimum dates into CSV/MD (no large verbatim pastes).
- Do not invent dates or translations; capture uncertainty in `notes` and flag gaps in the ticket.

---

## Dataset specification (CSV)

File name: `{{country}}-academic-calendar.csv` in `/{{country}}/data/calendar/` unless the ticket states otherwise.

Recommended columns:

- `academic_year` (e.g., `2025-2026`)
- `event_id` (stable slug, e.g., `winter-break`, `ib-may-exams`)
- `event_name_en`
- `event_name_local` (if available; copy exact local script, do not guess)
- `event_type` (enum suggestion: `school-year`, `break`, `exam`, `holiday`, `results-release`, `administrative-deadline`, `other`)
- `date_start` (YYYY-MM-DD)
- `date_end` (YYYY-MM-DD; same as start if single-day)
- `affected_grades` (free text; e.g., `12`, `all`, `IB DP`)
- `impact_on_recruiting` (suggested: `blackout`, `limited`, `normal`, `opportunity`)
- `notes` (short operational context or uncertainty)
- `source_name`
- `source_url`
- `last_verified` (YYYY-MM-DD)

Conventions:

- Use ISO dates. If only a month is known, reflect uncertainty in `notes` rather than fabricating exact days.
- Keep `event_id` stable across updates so dashboards remain consistent.

---

## Markdown output specification

### Education system note (`education-system.md`)

Recommended sections:

- Summary for recruiters (bullets, not narrative)
- System structure (levels, terminology)
- Feeder school types
- Credentials & grading (what documents look like; scale and descriptors)
- Exam landscape (national/international exams and why they matter)
- Operational implications (timing, messaging angles, risk windows)

### Education calendar note (`education-calendar.md`)

Recommended sections:

- Calendar snapshot for Academic Year YYYY–YYYY
- Blackout windows (with rationale)
- Best recruiting windows (2–3 windows, with rationale)
- International curriculum overlaps (IB/Cambridge/AP timing vs. national calendar)
- Update log (what changed, when verified)

---

## Workflow

1) **Set the planning horizon** for the relevant intake(s) and academic years.
2) **Collect authoritative sources** for term dates, breaks, national exams, and international exam windows used locally.
3) **Populate the CSV first,** ensuring each row has source metadata and a clear `impact_on_recruiting`.
4) **Draft the education calendar note** from the dataset (blackouts, limited periods, best windows).
5) **Draft/update the education system note** focusing on what affects targeting, messaging, and admissions conversations.
6) **Quality check**:
   - Every date has a source + `last_verified`.
   - Event ranges make sense (no overlaps that defy the source).
   - Operational guidance aligns with the data (no contradictions).

---

## Country-specific add-ons

Use each country skill file to capture:

- **Authoritative source list** (ministry/exam board URLs).
- **Local naming conventions** (event_id patterns, translation expectations).
- **Any path deviations** if the ticket requires non-default locations.

Keep the global workflow here; avoid duplicating it in country files.

