# RSD Generation 3 Execution Handoff

Status: **DESIGN HANDOFF ONLY — FULL EXECUTION BLOCKED**

This document is the execution boundary for `rsd_ref_v3`. The designated coding assistant owns scientific source/config/contract changes. After this design is frozen and handed off, Codex is execution-only: validate, dry-run, submit, monitor, resume, collect, and aggregate. Codex must not change Generation 3 code, YAML, contracts, tests, or documentation during execution.

## Authoritative state

- Generation: `rsd_ref_v3`.
- Canonical source parent: `227cbcc99c7edfac83de7f34c452db7defd5bdcb`.
- Server1 qualification evidence: `b1e8ab7e3b7c4b9f93995e437da3615bff910390`.
- Server1: `SCIENTIFIC_EXECUTION_QUALIFIED`, `SINGLE_SERVER_ONLY`, `STORAGE_NOT_RESERVED`.
- Immutable design freeze: `status/rsd_ref_v3/design_freeze.json`.
- Mutable runtime readiness: `status/rsd_ref_v3/execution_readiness.json` and
  `status/rsd_ref_v3/storage_plan.json`. These runtime files are deliberately
  excluded from the scientific design fingerprint.

## Pre-execution checks

Run from the exact clean checkout:

```bash
python scripts/audit_rsd_ref_v3.py --mode design
git diff --check
```

The design audit must pass before any source-native bank or confirmatory subset
is created. It remains valid when runtime storage changes. Readiness is
expected to fail while `storage_plan.json` is `STORAGE_NOT_RESERVED`.

The executable entry points are:

```bash
python scripts/run_rsd_ref_v3.py --stage reference --task llada_math --dry-run
python scripts/run_rsd_ref_v3.py --stage reference --task llada_gsm8k --dry-run
python scripts/run_rsd_ref_v3.py --stage materialize-subsets --dry-run
python scripts/run_rsd_ref_v3.py --stage core --task llada_math --dry-run
python scripts/run_rsd_ref_v3.py --stage temporal --task llada_math --dry-run
python scripts/run_rsd_ref_v3.py --stage mechanism --task llada_math --dry-run
python scripts/run_rsd_ref_v3.py --stage successful-harm --task llada_math --dry-run
python scripts/submit_rsd_ref_v3.py --stage reference --task llada_math --shard 0 --dry-run
```

Non-dry-run stages fail closed unless the design fingerprint, clean checkout,
storage reservation, live filesystem gate, and frozen R0/R1/R2 evidence all
match.

Before a single-server run, record all of the following in `status/rsd_ref_v3/storage_plan.json` and the execution manifest:

```text
approved_output_root
reserved_bytes
expected_high_water_bytes
minimum_free_after_run_bytes
owner/quota
persistence and retention policy
archive destination
```

The path must be below 95% filesystem use, retain at least 10% free inodes, and satisfy `max(200 GiB, 3 × projected maximum single-shard raw output)` after including merge/seal and retention-copy high water. No automatic use of `/mnt/raid5` is allowed while it is at 99% use.

## Execution order

Phase 3A, before any full scientific execution:

1. freeze and audit source-native task definitions;
2. obtain and record server1 storage reservation;
3. run only an 8–16 item resource/correctness pilot if the frozen audit permits it;
4. freeze the measured resource-only budget and subset policy;
5. rerun the design/readiness audit.

Phase 3B, only after readiness passes:

1. run the full LLaDA source-native MATH bank, one trajectory per item;
2. run the full LLaDA source-native GSM8K bank, one trajectory per item;
3. aggregate the base bank and materialize deterministic core/temporal/mechanism/successful-harm subsets;
4. execute primary controls and confirmation in the frozen order;
5. aggregate and compact-seal each stage, retaining raw counts, denominators, branch registries, NFE, evaluator identity, and storage seals.

Dream MATH/GSM are secondary replication runs. They never block the LLaDA Tier A path and cannot fill a missing LLaDA cell.

## Single-server versus pooled execution

Server1 may run the primary matrix alone once the source/config SHA, scientific qualification, storage, and protocol freeze gates pass. Cross-server equivalence is required only if shard pooling across server2/server3/server4 is selected. A server2/3 calibration is optional expansion and must not alter the already-frozen single-server protocol.

## Prohibited actions

- Do not start a full reference bank while storage is `STORAGE_NOT_RESERVED`.
- Do not use `limit: 200` or any deadline compromise in a primary reference bank.
- Do not treat MATH-500 calibration as source-native MATH or a confirmatory denominator.
- Do not pool V1/V2/legacy outputs with Generation 3.
- Do not select subsets using repairability outcomes.
- Do not change operators, checkpoints, sample targets, or evaluators after outcomes are visible.
- Do not use venue names in job names or artifact namespaces.
