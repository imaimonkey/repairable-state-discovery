# Pinned reference decoding sources

These are source pins, not completed reproductions. No reference GPU result is asserted in this document. Recipe JSONs contain exact SHA256 values for every fetched source file, model/tokenizer/dataset revisions and flags.

* LLaDA: [ML-GSAI/LLaDA at9182493](https://github.com/ML-GSAI/LLaDA/tree/9182493720ed723ef8031210d85959364e51cbe0). [Official evaluation instructions](https://github.com/ML-GSAI/LLaDA/blob/9182493720ed723ef8031210d85959364e51cbe0/EVAL.md) and its OpenCompass model wrapper call the repository `generate.py`. The exact GSM256/256/block8 and MATH512/512/block64 recipes, temperature0/CFG0/EOS flags and few-shot messages are source-derived. Model/tokenizer GSAI-ML/LLaDA-8B-Instruct@08b83a6feb34df1a6011b80c3c00c7563e963b07.
* Dream: [DreamLM/Dream at31f94a6](https://github.com/DreamLM/Dream/tree/31f94a60d187e3fd481fee3bbc2c732eb94a879c). [Official instruct evaluation shell](https://github.com/DreamLM/Dream/blob/31f94a60d187e3fd481fee3bbc2c732eb94a879c/eval_instruct/eval.sh), task YAMLs, evaluator modules and HF generation utilities are pinned. Model/tokenizer Dream-org/Dream-v0-Instruct-7B@05334cb9faaf763692dcf9d8737c642be2b2a6ae. The entropy sampler with temperature0.1/top_p0.9/alg_temp0 is distinct from historical V2 origin sampling.

LLaDA GSM uses four fixed conversational demonstrations, Dream GSM zero-shot Q/A. Preserve exact upstream prompt rendering rather than assume all chat adapters are equivalent. LLaDA official wrapper passes no attention mask for batch-size1; preserve this call. Dream uses its native full-attention handling and official completion truncation at EOS/task strings.

LLaDA MATH official evaluator is its version-v2 string normalization, while paper evaluator adds symbolic equivalence. Dream MATH returns both exact_match and math_verify; keep both and identify the chosen metric. Their disagreement is recorded and never hidden by relabeling.

Official full MATH contains5000 test cases; paper MATH-500 contains500. Their headline numbers are NOT_DIRECTLY_COMPARABLE. Latest user reset explicitly authorizes source-native smoke+recipe fidelity → paper-task full bank → reproduction sanity, without a separate full5000 benchmark rerun. GSM direct comparison remains pending exact data identity and full reference bank. One sampled trajectory/item is the baseline unit.

LLaDA passive instrumentation inserts an observation callback immediately after the pinned token assignment; Dream uses its official token hook. This construction does not itself prove equivalence. Only measured real-model R2 reports may authorize reference scientific use. CPU fixtures verify callback RNG preservation and snapshot-resume semantics before GPU smoke. Real native continuation must additionally pass replay checks before R3.

Deadline verified from [ICLR2027 Author Guidelines](https://iclr.cc/Conferences/2027/AuthorGuidelines): Sep25 2026 23:59 AoE = Sep26 20:59 KST. Use the stricter explicit initial main-text nine-page rule; discussion/camera-ready allowance is separate.

CPU bridge fixture discovery: OpenCompass `gsm8k_postprocess` on “The answer is 1,234.” yields234; the paper numeric parser yields1234. The fixture preserves and asserts this exact upstream behavior, rather than changing official code or requiring the two semantically different evaluators to agree. Decimal and negative-number fixtures agree. These known semantic differences do not mean reference sampling changed; reference accuracy must identify its evaluator and both versions are retained.
