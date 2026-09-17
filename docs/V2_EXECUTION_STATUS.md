# V2 execution package status

This file is intentionally short. The authoritative execution boundaries are in `AGENTS.md` and `docs/CODEX_V2_FINAL_EXECUTION.md`.

The V2 implementation is considered ready for Codex handoff only when:

1. `bash scripts/run_v2_suite.sh preflight` passes;
2. `python scripts/validate_v2_backends.py` passes on a CUDA worker;
3. both frozen pilot runs complete;
4. `python scripts/audit_v2_design.py --mode full` reports `FULL SUBMISSION READY`.

Codex must then use `scripts/submit_v2_suite.py` or `scripts/run_v2_suite.sh full-local` without changing scientific configs.
