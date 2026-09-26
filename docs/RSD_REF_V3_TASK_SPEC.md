# RSD Generation 3 Reference Task Specification

This file freezes the source-native task definitions used by `rsd_ref_v3`. It separates publication/reference populations from the MATH-500 runtime qualification population.

## Pinned source and model identity

- LLaDA repository: `ML-GSAI/LLaDA@9182493720ed723ef8031210d85959364e51cbe0`.
- LLaDA model/tokenizer: `GSAI-ML/LLaDA-8B-Instruct@08b83a6feb34df1a6011b80c3c00c7563e963b07`.
- Recipe record: `results/v2r_reference/reference_recipes/llada.json`.
- Source-native prompt and evaluator code is loaded from verified pinned bytes; it is not reimplemented by the Generation 3 adapter.

## LLaDA MATH primary reference

- Population: pinned OpenCompass `math/math.json` archive.
- Archive SHA256: `cf44a0c065f23dbb96e3239115758f7442b725776f3dedfa4473821a1c98fe03`.
- Split: `test`; count: `5000`.
- Prompt: pinned `math_0shot_gen_11c4b5.py`, zero-shot, chat template, generation prompt enabled.
- Recipe: `steps=512`, `gen_length=512`, `block_length=64`, `temperature=0`, `cfg_scale=0`, low-confidence remasking, no EOS-logit or confidence-EOS override.
- Answer extraction/evaluator: pinned `math_postprocess_v2` and `MATHEvaluator(version=v2)`; string normalization semantics are retained.
- Upstream report: OpenCompass accuracy `42.7`.
- Comparability: `DIRECTLY_COMPARABLE_TO_PINNED_OPENCOMPASS_MATH`; not interchangeable with the 500-row HuggingFace MATH-500 bridge.

## LLaDA GSM8K primary reference

- Population: pinned OpenCompass `gsm8k/test.jsonl` archive.
- Archive SHA256: `5e90449bd5ed9c728dd32fc0c36a21c2cb02fd1fe38cb00fcf5672fcf3dc9378`.
- Split: `test`; count: `1319`; config: `main`.
- Prompt: pinned `gsm8k_gen_1d7fe4.py`, four fixed conversational demonstrations, chat template, generation prompt enabled.
- Recipe: `steps=256`, `gen_length=256`, `block_length=8`, `temperature=0`, `cfg_scale=0`, low-confidence remasking, no EOS-logit or confidence-EOS override.
- Answer extraction/evaluator: pinned `gsm8k_postprocess`, `gsm8k_dataset_postprocess`, and `Gsm8kEvaluator`.
- Upstream report: OpenCompass accuracy `78.9`.
- Comparability: `PENDING_FULL_REPRODUCTION_AND_DATA_IDENTITY`; the source-native definition is frozen, but the upstream metric is not treated as directly comparable until the archive and full-bank reproduction checks pass.

## Calibration-only bridge

`HuggingFaceH4/MATH-500@test@6e4ed1a2a79af7d8630a6b768ec859cb5af4d3be` remains a 500-row runtime/replay calibration and pilot bridge. It must not be labeled as the source-native OpenCompass MATH benchmark and must not enter the Generation 3 confirmatory denominator.

## Secondary Dream replication

Dream uses the pinned `results/v2r_reference/reference_recipes/dream.json` source-native definitions and remains secondary. Its MATH and GSM populations, prompt rendering, entropy sampler, and evaluators are retained exactly in that recipe. Dream results cannot be substituted for missing LLaDA Tier A cells.
