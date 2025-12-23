# T-588: Research-request skill defaults + remove .eml + clarify report-as-artifact

Status: done
Type: structure
Priority: P1
Dependencies: (none)
Claimed-by: evoticketresolver_518kcxli
Claimed-at: 2025-12-22T22:10:55Z
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Update the global `research-request-briefs` skill guidance to:
- Default to **5** research rounds (1–3 for easy topics, 10–15 for hard topics, rarely above that).
- Treat the “report” as a detailed **artifact**, with separate extracted outputs as the primary repo deliverables when appropriate.
- Remove all `.eml` / email brief concepts (ticket-only workflow).
- Clarify that report length should be **whatever length is needed** (no artificial compression).

---

## Allowed write paths

- `tickets/T-588-research-request-skill-defaults-and-remove-eml.md`
- `skills/research-request-briefs/**`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**` (except `skills/research-request-briefs/**`)
- `tickets/**` (except this ticket file)
- `.github/**`
- `scripts/**`

---

## Required outputs

- `skills/research-request-briefs/SKILL.md` (updated)
- `skills/research-request-briefs/prompt-templates/high-school-profile.md` (updated if needed)

---

## Acceptance criteria

- [ ] `skills/research-request-briefs/SKILL.md` defaults `Research rounds` to **5** and documents 1–3 (easy) and 10–15 (hard) guidance
- [ ] The skill explicitly states report length is unconstrained (“whatever length is needed”)
- [ ] The skill clarifies “report” is an artifact and primary deliverables may be extracted/curated outputs (e.g., entity profiles)
- [ ] No `.eml` / email brief workflow remains in the skill
- [ ] No files were modified outside `Allowed write paths`

---

## Execution notes (optional)

- What changed (short):
  - Updated `skills/research-request-briefs/SKILL.md` to default to 5 research rounds, clarify reports as long-form artifacts with extracted primary deliverables, and remove all `.eml`/email brief workflow.
  - Updated prompt templates to match (high-school profile now produces a research report artifact plus a curated profile).
