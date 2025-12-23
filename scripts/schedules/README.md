# scripts/schedules

This folder contains:
- `*.json` schedule configs (EventBridge rule + targets)
- `create_eventbridge_rule.py` which applies a config by calling the AWS CLI

## Prerequisites

- **AWS CLI** installed (`aws`)
- Credentials configured (one of):
  - default credential chain (env vars, shared config/credentials, SSO, etc.)
  - or pass an explicit profile with `--profile <name>`
- Correct IAM permissions to:
  - `events:PutRule`, `events:PutTargets`
  - (optional update mode) `events:DescribeRule`, `events:ListTargetsByRule`, `events:RemoveTargets`
  - and the ability for EventBridge to invoke your Lambda via the configured target role

## Config JSON format

Each config file is a single JSON object with two top-level keys:

- `rule`: payload for `aws events put-rule`
- `targets`: payload for `aws events put-targets` (the script will fill `Rule` and `EventBusName` from `rule` if you omit them)

Example keys you’ll typically edit:

- **Rule**
  - `rule.Name` (rule name)
  - `rule.ScheduleExpression` (cron/rate expression)
  - `rule.State` (`ENABLED` or `DISABLED`)
  - `rule.Description`
  - `rule.EventBusName` (usually `default`)

- **Targets**
  - `targets.Targets[]` list (one or more targets)
  - For each target:
    - `Id` (**required**, must be stable)
    - `Arn` (Lambda ARN)
    - `RoleArn` (IAM role EventBridge assumes)
    - `Input` (the event payload)

### About `Targets[].Input`

In your JSON config, `Targets[].Input` can be either:
- a JSON **object** (recommended for readability), or
- a JSON **string** (if you already have it pre-serialized).

EventBridge expects `Input` to be a string; the script will automatically convert objects into a compact JSON string before calling the AWS CLI.

## Schedule expression: every 30 minutes starting 00:00 UTC

Use:

- `cron(0/30 * * * ? *)`

This triggers at minute **00** and **30** of every hour, in **UTC**.

## How to run

From repo root:

### Create / upsert (idempotent)

This always calls:
- `aws events put-rule`
- `aws events put-targets`

```bash
python scripts/schedules/create_eventbridge_rule.py \
  --config scripts/schedules/savva.c-evolverecruiting-schedule.json
```

### Update mode (reconcile targets)

Use `--update` when you want the rule’s targets to match your JSON exactly:
- verifies the rule exists (`describe-rule`)
- removes any existing targets whose `Id` is **not** present in your config (`remove-targets`)
- then applies the config (`put-rule`, `put-targets`)

```bash
python scripts/schedules/create_eventbridge_rule.py \
  --config scripts/schedules/savva.c-evolverecruiting-schedule.json \
  --update
```

### Dry-run (print commands only)

```bash
python scripts/schedules/create_eventbridge_rule.py \
  --config scripts/schedules/savva.c-evolverecruiting-schedule.json \
  --dry-run
```

### Region and profile

- `--region` overrides the AWS region (otherwise uses `AWS_REGION` / `AWS_DEFAULT_REGION`)
- `--profile` is optional; if omitted, AWS CLI uses its normal default credential resolution

```bash
python scripts/schedules/create_eventbridge_rule.py \
  --config scripts/schedules/savva.c-evolverecruiting-schedule.json \
  --region eu-central-1 \
  --profile default
```


