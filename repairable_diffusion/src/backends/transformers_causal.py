from __future__ import annotations

from typing import Any

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from repairable_diffusion.src.utils.math_eval import answers_match, build_ar_math_prompt, extract_boxed_answer
from repairable_diffusion.src.utils.seed import seed_everything


class TransformersCausalBackend:
    def __init__(self, cfg: dict[str, Any]):
        self.cfg = cfg
        self.model = None
        self.tokenizer = None

    def load(self) -> None:
        if self.model is not None:
            return
        torch_dtype = getattr(torch, self.cfg.get("torch_dtype", "bfloat16"))
        model_path = self.cfg["model_path"]
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path,
            torch_dtype=torch_dtype,
            device_map=self.cfg.get("device_map", "auto"),
            trust_remote_code=bool(self.cfg.get("trust_remote_code", True)),
        )
        self.model.eval()
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_path,
            trust_remote_code=bool(self.cfg.get("trust_remote_code", True)),
        )
        if self.tokenizer.pad_token_id is None and self.tokenizer.eos_token_id is not None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

    def generate_samples(
        self,
        item: dict[str, Any],
        *,
        sample_count: int,
        base_seed: int,
    ) -> dict[str, Any]:
        self.load()
        question = item["question"]
        gold = item["answer"]
        prompt_text, prompt = build_ar_math_prompt(question, self.tokenizer)
        enc = self.tokenizer(prompt, return_tensors="pt")
        input_ids = enc.input_ids.to(self.model.device)
        attention_mask = enc.attention_mask.to(self.model.device)

        rows = []
        do_sample = float(self.cfg.get("temperature", 0.0)) > 0
        sample_batch_size = max(1, int(self.cfg.get("sample_batch_size", 2)))
        max_new_tokens = int(self.cfg.get("max_new_tokens", 512))
        temperature = float(self.cfg.get("temperature", 0.0))
        top_p = float(self.cfg.get("top_p", 1.0))

        sample_index = 0
        while sample_index < sample_count:
            current_batch = min(sample_batch_size, sample_count - sample_index)
            seed_everything(base_seed + sample_index)
            batch_input_ids = input_ids.repeat(current_batch, 1)
            batch_attention_mask = attention_mask.repeat(current_batch, 1)
            output = self.model.generate(
                input_ids=batch_input_ids,
                attention_mask=batch_attention_mask,
                max_new_tokens=max_new_tokens,
                do_sample=do_sample,
                temperature=temperature,
                top_p=top_p,
                pad_token_id=self.tokenizer.pad_token_id,
                eos_token_id=self.tokenizer.eos_token_id,
            )
            texts = self.tokenizer.batch_decode(output[:, input_ids.shape[1] :], skip_special_tokens=True)
            for offset, text in enumerate(texts):
                final_answer = extract_boxed_answer(text)
                rows.append(
                    {
                        "sample_index": sample_index + offset,
                        "final_text": text,
                        "final_answer": final_answer,
                        "correct": answers_match(final_answer, gold),
                    }
                )
            sample_index += current_batch

        return {
            "item_id": item["item_id"],
            "question": question,
            "gold_answer": gold,
            "prompt_text": prompt_text,
            "samples": rows,
        }
