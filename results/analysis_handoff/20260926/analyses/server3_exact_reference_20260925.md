# Server3 exact-reference 실험 결과 분석

분석 기준: 2026-09-25, server3 노드 `ubuntu`, frozen execution SHA
`78fe5d7c1829b67d1bb1416b7205edfa647bb2fa`.

## 1. 실행 상태

- server3의 kimhj Slurm job은 현재 남아 있지 않다.
- LLaDA MATH-500/GSM8K R0/R1/R2 gate는 모두 `PASS`이며, native replay와
  final token/text/answer/correctness/NFE/schedule/RNG 일치 검사를 통과했다.
- 다음 네 bundle은 `SEALED`이고 aggregate는 `MERGED_VALID`다.
  - `llada_math500_base_finalsha`
  - `llada_gsm8k_base_finalsha`
  - `llada_math500_core_finalsha`
  - `llada_math500_temporal_finalsha`
- 따라서 이전 실패·timeout·cancel된 server3 시도는 최종 증거에 섞이지 않는다.

## 2. Reference baseline

| lane | 표본 | 정답 | 실패 | reference trajectory accuracy |
| --- | ---: | ---: | ---: | ---: |
| LLaDA × MATH-500 | 500 | 201 | 299 | 40.20% |
| LLaDA × GSM8K | 1,319 | 1,077 | 242 | 81.6528% |

각 item당 trajectory 1개만 사용했으므로 이 수치는 pass@1이며, 다중 샘플
pass@k가 아니다. MATH-500과 GSM8K의 데이터·프롬프트·decoder recipe가
서로 다르므로 두 정확도를 단순 비교하거나 기존 V2 decoder 결과와 합치면 안 된다.

## 3. LLaDA MATH-500 repairability

### Core subset

- frozen failed pool에서 64개를 선택했다.
- `q_C` 평균: **0.000**
- `q_R` 평균: **0.046875**
- `Delta_R` 평균: **0.046875**
- confirmed repairable: **3/64 = 4.6875%**
- native recoverable: **0/64**
- repair가 확인된 item: **9, 221, 340**
- 확인 checkpoint:
  - item 9: step 63, normalized progress 0.1230
  - item 221, 340: step 191, normalized progress 0.3730

즉, 실패 trajectory 중 일부에서는 canonical repair branch가 정답을 만들었지만,
이 효과는 넓은 평균 효과가 아니라 64개 중 3개에 집중된 sparse effect다.
특히 `q_C=0`이므로 native continuation만으로 우연히 회복된 결과가 아니라,
측정한 사례에서는 intervention branch에서만 회복이 관찰되었다.

### Temporal subset

- 독립적으로 고정한 failed subset 32개를 7개 checkpoint에서 dense confirmation했다.
- confirmed repairable: **1/32 = 3.125%**
- native recoverable: **0/32**
- never-correct-repairable: **1/32 = 3.125%**
- 유일한 positive item: **221**
- 유일한 positive checkpoint: **step 191 / normalized progress 0.3730**
- checkpoint별 평균 `q_R`: 0.123, 0.248, **0.373에서 0.03125**, 0.498, 0.623,
  0.748, 0.873에서 모두 0

이는 적어도 한 실패 사례에서 repairable state가 refinement 중간 지점에
국소적으로 존재한다는 증거다. 그러나 temporal 표본에서 positive가 1개뿐이므로
일반적인 시간적 곡선, monotonicity, peak 위치의 안정성을 주장할 수는 없다.

## 4. 과학적 결론

현재 가장 방어 가능한 결론은 다음과 같다.

> Reference-quality LLaDA decoding으로 생성한 MATH-500 실패 trajectory 중 일부는
> refinement 중간 상태에서 counterfactual repair에 의해 회복 가능했으며, 이 현상은
> 본 실험의 frozen subset에서 드물고 국소적으로 관찰되었다.

반대로 다음 표현은 현재 결과만으로는 과하다.

- “대부분의 실패는 repair 가능하다”
- “repairability가 안정적으로 37% 지점에 집중된다”
- “selector가 일반적으로 높은 성능을 낸다”
- “모든 diffusion backbone/task에 일반화된다”

현재 결과는 `existence + localization hypothesis`를 약하게 지지하지만, 큰 효과나
일반화된 시간 구조를 입증하지는 않는다. 95% binomial 불확실성도 3/64와 1/32처럼
넓으므로, 추가 표본 없이 정밀한 population rate로 해석하면 안 된다.

## 5. 논문/분석 사용 시 주의

- 논문 표에는 먼저 baseline accuracy와 denominator(500, 1,319, 64, 32)를 함께 둔다.
- core와 temporal은 서로 독립적으로 frozen selection된 subset이므로 3/64와 1/32를
  합쳐 하나의 비율로 재계산하지 않는다.
- old V2의 `pred repaired pass@k`, `oracle expected pass@k`, `negative repair` 수치는
  이 exact-reference bundle의 수치가 아니므로 이번 결과와 섞지 않는다.
- server3 exact-reference evidence는 봉인되었지만 paper readiness는 별도 단계이며,
  최종 abstract/conclusion wording과 claim strength는 저자 검토가 필요하다.

## 근거 artifact

- `runs/llada_math500_base_finalsha/aggregate/aggregate.json`
- `runs/llada_gsm8k_base_finalsha/aggregate/aggregate.json`
- `runs/llada_math500_core_finalsha/aggregate/aggregate.json`
- `runs/llada_math500_core_finalsha/compact/selector_summary.csv`
- `runs/llada_math500_temporal_finalsha/aggregate/aggregate.json`
- `runs/llada_math500_temporal_finalsha/compact/temporal_summary.csv`
- `status/v2r/current_status.json`
- `status/v2r/paper_readiness.json`
