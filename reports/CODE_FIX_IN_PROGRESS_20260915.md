# Code fix in progress — 2026-09-15

This marker records an active source-level memory fix for the Dream-v0-Instruct-7B backend after CUDA OOM in trajectory collection job 47521. Existing LLaDA/MATH-500 claim-bearing results are unchanged. The Dream protocol must remain scientifically identical; the fix is limited to inference-memory behavior and must pass repository CI before a full rerun.
