---
name: csv-authoring
description: Global best practices for prompting, generating, and validating CSV outputs with strict schema-locking, quoting, and delimiter discipline.
metadata:
  owner: evobuilder
  version: "1.0"
---

## Purpose and scope
- Provide a reusable, prompt-ready recipe for creating CSVs that stay interoperable across countries and datasets.
- Enforce schema locks, value hygiene, and self-validation to prevent invented data, delimiter drift, or enum violations.

## When to use
- Generating sample or production CSVs from source notes, transcripts, or tables.
- Converting messy inputs into clean, schema-aligned CSV outputs (UTF-8, text-first).
- Pair with `skills/data-model-csvs-and-profiles` for dataset-wide schemas and ID policies.

## Inputs required (declare before generation)
- Target schema with ordered columns, data types, and enum values.
- Delimiter and quoting rules (default: `,` delimiter, double quotes for strings, UTF-8 without BOM).
- Canonical formats: ISO dates (`YYYY-MM-DD`), ISO-3166 country codes, `.` decimal separator, lowercase emails, trimmed strings.
- Missing data policy (e.g., `""` or `NULL`), and row-count expectation.

## Pre-flight checks (lock the surface area)
- Confirm header order and exact column names; forbid extras.
- State delimiter and quoting rules; require escaping of embedded commas, quotes, or newlines.
- Define allowed values for enums; reject anything outside.
- Specify anti-forgery rule: never invent data; use the missing-data policy.
- Remind: output only the fenced CSV block, no prose.

## Prompting pattern (world-class default)
- Instruction: “Produce ONLY a CSV block fenced with ```csv ... ``` and nothing else.”
- Schema lock: list columns in order with data types and enum membership; forbid extra columns.
- Value hygiene: enforce quoting for strings; escape quotes with `""`; trim whitespace; lowercase emails; canonical country codes/dates/numbers.
- Missing data: explicitly say `""` or `NULL` when unknown; never fabricate.
- Row count: specify the expected number of rows.
- Quality gate: require a self-check before output (column count, enums, delimiter, quoting).

## Generation checklist (agent steps)
1) Restate schema, delimiter, quoting, and missing-data policy inside the prompt.
2) Normalize source values to canonical formats (ISO dates, enums, IDs, lowercased emails).
3) Build rows in memory; verify every row matches column count and enum rules.
4) Emit only the fenced CSV block. No lead-in, summary, or trailing text.
5) Re-parse mentally: ensure no stray commas/newlines inside unquoted cells; ensure UTF-8 without BOM.

## Validation checklist (post-output)
- Open with a CSV parser; confirm header casing and consistent column counts.
- Spot-check enums, date formats, and numeric precision (`.` decimal).
- Look for dangerous characters or formulas; if unavoidable, prefix with `'`.
- Ensure no duplicated headers, trailing delimiters, or mixed delimiters.
- Confirm row count matches the specification and missing-data policy is respected.

## Common pitfalls and safeguards
- Mixed delimiters or smart quotes — always lock to `,` and standard double quotes.
- Invented values — prefer `""`/`NULL` over guessing.
- Locale drift — enforce ISO dates and `.` decimal separators.
- Hidden whitespace/BOM — trim cells; keep UTF-8 without BOM.
- Unescaped commas/newlines/quotes — always quote strings and escape embedded quotes with `""`.

## Ready-to-paste prompt snippet
```
You are generating a UTF-8 CSV for <dataset>. Use delimiter "," and wrap all string fields in double quotes.
Columns (in order, no extras):
1) <col_1> (type/enum, required?)
2) <col_2> (type/enum, required?)
3) <col_3> ...
Missing data policy: use "" (or NULL) when unknown. Never invent values.
Formatting: ISO dates YYYY-MM-DD; country codes = ISO-3166 alpha-2; emails lowercase; numbers use "." decimal.
Escaping: escape any double quotes as "" and keep the cell quoted. Avoid commas/newlines in unquoted fields.
Output ONLY the CSV fenced with ```csv ... ``` and nothing else.
Before output: self-check header order, column counts per row, enums valid, strings quoted, delimiter correct.
Provide exactly <N> rows.
```
