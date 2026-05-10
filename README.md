# repairable-state-discovery

Diffusion reasoning trajectory의 실패 경로를 통째로 버리지 않고, 어느 중간 refinement state를 다시 고치면 정답으로 복구되는지를 측정하는 `repairable-state localization and evaluation protocol` 프로젝트입니다.

이 레포의 중심 주장은 `새로운 범용 self-correction method`라기보다, `diffusion reasoning trajectory 내부의 repairability를 측정하고 localize하는 평가 프로토콜`에 가깝습니다.

## 한 줄 요약

- 실패한 diffusion trajectory에도 `repairable intermediate state`가 존재하는가?
- 그 repairability는 특정 checkpoint에 `localize`되는가?
- oracle 없이도 lightweight predictor가 좋은 repair step을 `근사`할 수 있는가?
- 이 현상은 `MATH-500`, `GSM8K`, robustness 변형에서도 반복되는가?

## 연구 가설

이 프로젝트는 아래 가설을 검증합니다.

1. 최종적으로 오답인 diffusion trajectory 안에도, 다시 시작하면 정답으로 복구될 수 있는 중간 state가 존재한다.
2. repairability는 모든 step에 균등하지 않고 특정 checkpoint 근처에 집중된다.
3. oracle로 모든 step을 직접 repair해보지 않아도, state feature만으로 좋은 repair step을 예측할 수 있다.
4. 위 성질은 한 데이터셋의 우연이 아니라 여러 데이터셋과 설정 변형에서 반복 관찰된다.

## 연구 포지셔닝

- 이 레포의 포지셔닝은 `new self-correction method`보다 `repairable-state localization and evaluation protocol for diffusion reasoning trajectories`에 가깝습니다.
- local repair는 그 자체를 강한 방법론적 novelty로 주장하기보다, checkpoint별 local repairability를 측정하기 위한 `operational probe`로 사용합니다.
- oracle은 실패 trajectory의 각 checkpoint에서 실제 복구 가능성을 측정하고, predictor는 그 분포를 근사해 oracle 없이 step selector를 학습합니다.
- 핵심 보고 지표는 `repairable failed rate`, `repair gain curve`, `negative repair`, `predictor-oracle gap`, `expected newly solved`입니다.

## 현재 상태

현재 저장소 스냅샷 기준으로 실험 상태는 아래와 같습니다.

- `protocol_gsm8k_final.yaml`: 완료
- `protocol_math500_submission_robustness.yaml`: 완료
- `protocol_math500_final.yaml`: 완료
- final/submission aggregate report 생성 완료

주의할 점은 `run_protocol.py --families ...` 같은 부분 재실행이 기존 protocol report를 덮어써 diffusion row를 잃을 수 있었다는 점입니다. 현재 코드는 부분 실행 시 기존 report와 병합하도록 수정되어 있으며, `results/final_reports`와 `results/submission_reports`는 이 수정 후 재생성된 상태입니다.

## 현재 결과 스냅샷

아래 숫자는 현재 저장된 artifact만 기준으로 정리한 요약입니다.

### Diffusion Main

| Protocol / run | Dataset | pass@1 | pass@k | predictor repaired pass@k | predictor neg repair | repairable failed rate | peak step |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `gsm8k_final_llada8b_fast` | GSM8K | 0.4900 | 0.7100 | 0.8336 | 0.1788 | 0.6716 | 8 |
| `math500_final_llada8b_fast` | MATH-500 | 0.2300 | 0.3450 | 0.4578 | 0.2050 | 0.3309 | 16 |
| `math500_submit_llada8b_fast_seed29` | MATH-500 robustness | 0.2300 | 0.3350 | 0.4426 | 0.2125 | 0.3341 | 16 |
| `math500_submit_llada8b_fast_stride16` | MATH-500 robustness | 0.2300 | 0.3450 | 0.4759 | 0.2725 | 0.2516 | 16 |
| `math500_submit_llada8b_fast_branch2` | MATH-500 robustness | 0.2300 | 0.3450 | 0.4403 | 0.2275 | 0.2557 | 16 |

### AR Compare

| Run | Dataset | pass@1 | pass@k |
| --- | --- | --- | --- |
| `math500_final_ar_qwen25_7b` | MATH-500 | 0.4450 | 0.5650 |
| `math500_final_ar_llama31_8b` | MATH-500 | 0.3900 | 0.6100 |
| `gsm8k_final_ar_qwen25_7b` | GSM8K | 0.8350 | 0.9550 |
| `gsm8k_final_ar_llama31_8b` | GSM8K | 0.7750 | 0.9350 |

### 현재 결과 해석

- `GSM8K final`은 가설을 가장 강하게 지지합니다.
  실패 trajectory의 상당수가 repairable했고, predictor도 oracle에 비교적 가깝게 따라갑니다.
- `MATH500 final`도 predictor repair gain과 step-16 localize 양상을 보입니다.
- `MATH500 robustness`는 seed/stride/branching을 바꿔도 repair gain이 유지된다는 점에서 좋지만, negative repair와 predictor-oracle gap이 여전히 큽니다.

## 지금 바로 논문 집필에 들어가도 되는가

`초안 작성`은 지금 바로 시작해도 됩니다.

- 연구 문제 정의
- protocol framing
- GSM8K final
- MATH500 final diffusion-only result
- MATH500 robustness
- oracle / predictor / negative repair 서사

위 재료만으로도 Introduction, Method, 초기 Results 섹션 초안은 충분히 쓸 수 있습니다.

다만 `최종 제출용 완성본` 단계로 보기에는 아직 이르며, 아래가 남아 있습니다.

1. seed 반복과 bootstrap confidence interval 추가
2. predictor feature ablation 추가
3. negative repair 완화 실험
4. cost-normalized comparison 추가
5. 추가 diffusion backbone / dataset 일반화

## 논문 완성도를 높이기 위해 더 필요한 것

탑티어 메인트랙 수준으로 끌어올리려면 아래를 우선순위로 권장합니다.

### 필수

1. seed 반복과 confidence interval 추가
2. predictor feature ablation 추가
3. negative repair를 줄이는 selection/abstention ablation 추가
4. cost-normalized comparison 추가
5. qualitative case study 추가

### 매우 권장

1. diffusion backbone 1개 이상 추가
2. dataset 1~2개 추가
3. negative repair를 줄이는 repair rule ablation
4. 성공/실패 사례의 질적 분석

### 프레이밍상 주의

- `새로운 self-correction method`로 프레이밍하면 방어가 어렵습니다.
- `state-level repairability protocol`과 `measurement framework`로 프레이밍하는 편이 훨씬 강합니다.
- method novelty보다 `what is measurable`, `how to localize it`, `how to compare selectors`, `how to quantify safety via negative repair`에 초점을 두는 편이 좋습니다.

## 레포 구조

```text
repairable-state-discovery/
├── README.md
├── requirements.txt
├── pyproject.toml
├── scripts/
│   ├── run_phase1_oracle.sh
│   ├── run_protocol_phase1.sh
│   ├── run_protocol_repairability_pilot.sh
│   ├── run_protocol_repairability_stage2.sh
│   ├── run_protocol_repairability_final.sh
│   ├── build_final_report.sh
│   ├── build_submission_report.sh
│   ├── submit_final_suite.sh
│   └── submit_submission_ready_suite.sh
├── results/
│   └── generated_configs/
└── repairable_diffusion/
    ├── configs/
    │   ├── default.yaml
    │   ├── model_profiles.yaml
    │   ├── protocol_phase1.yaml
    │   ├── protocol_repairability_pilot.yaml
    │   ├── protocol_repairability_stage2.yaml
    │   └── final/
    │       ├── math500_diffusion_final.yaml
    │       ├── gsm8k_diffusion_final.yaml
    │       ├── protocol_math500_final.yaml
    │       ├── protocol_gsm8k_final.yaml
    │       └── protocol_math500_submission_robustness.yaml
    ├── outputs/
    │   └── runs/
    └── src/
        ├── run_pipeline.py
        ├── run_ar_baseline.py
        ├── run_protocol.py
        ├── backends/
        ├── collect/
        ├── repair/
        ├── analysis/
        ├── data/
        └── utils/
```

## 의존 관계

이 프로젝트는 diffusion backend 구현을 새로 복제하지 않고, 별도 `rfba` 저장소의 LLaDA 구현을 재사용합니다.

기본적으로 아래 환경 변수를 설정하는 것을 권장합니다.

```bash
export RFBA_ROOT=/absolute/path/to/rfba
```

## 설치

```bash
cd repairable-state-discovery
uv venv .venv --python 3.11
source .venv/bin/activate
uv pip install -r requirements.txt
```

## 빠른 실행

### Dry run

```bash
cd repairable-state-discovery
python -m repairable_diffusion.src.run_protocol \
  --protocol repairable_diffusion/configs/final/protocol_math500_final.yaml \
  --dry-run
python -m repairable_diffusion.src.run_protocol \
  --protocol repairable_diffusion/configs/final/protocol_gsm8k_final.yaml \
  --dry-run
python -m repairable_diffusion.src.run_protocol \
  --protocol repairable_diffusion/configs/final/protocol_math500_submission_robustness.yaml \
  --dry-run
```

### Final protocols

```bash
cd repairable-state-discovery
PROTOCOL_PATH=repairable_diffusion/configs/final/protocol_math500_final.yaml \
  sbatch scripts/run_protocol_repairability_final.sh

PROTOCOL_PATH=repairable_diffusion/configs/final/protocol_gsm8k_final.yaml \
  sbatch scripts/run_protocol_repairability_final.sh

PROTOCOL_PATH=repairable_diffusion/configs/final/protocol_math500_submission_robustness.yaml \
  sbatch scripts/run_protocol_repairability_final.sh
```

### Submission-ready suite

```bash
cd repairable-state-discovery
bash scripts/submit_submission_ready_suite.sh
```

## 집계 리포트 생성

### Final aggregate report

아래 스크립트는 `protocol_math500_final_report.json`과 `protocol_gsm8k_final_report.json`이 모두 있어야 동작합니다.

```bash
cd repairable-state-discovery
bash scripts/build_final_report.sh
```

### Submission aggregate report

아래 스크립트는 `protocol_math500_final_report.json`, `protocol_gsm8k_final_report.json`, `protocol_math500_submission_robustness_report.json`이 모두 있어야 동작합니다.

```bash
cd repairable-state-discovery
bash scripts/build_submission_report.sh
```

현재 저장소 스냅샷에서는 세 protocol report가 모두 생성되어 있으므로 바로 실행할 수 있습니다.

## 재실행 / 복구 방식

- `run_pipeline.py`는 이미 있는 `trajectories.pkl`, `oracle_repair.json`, `repair_predictor.json`, `repair_selection_eval.json`을 자동 재사용합니다.
- `run_protocol.py`는 run directory 안에 `report.json`이 있으면 diffusion run을 다시 collect하지 않습니다.
- `run_ar_baseline.py`는 item 단위 progress를 `ar_baseline.progress.pkl`에 저장하고, 재실행 시 이어서 진행합니다.
- AR baseline이 완주되면 `run_protocol.py`가 자동으로 `protocol_math500_final_report.json`까지 다시 생성합니다.

### 권장 복구 명령

기존 diffusion artifact를 재사용하면서 `MATH500 final`의 AR compare만 다시 돌리려면:

```bash
cd repairable-state-discovery
PROTOCOL_PATH=repairable_diffusion/configs/final/protocol_math500_final.yaml \
PROTOCOL_FAMILIES=ar \
  sbatch scripts/run_protocol_repairability_final.sh
```

특정 AR baseline 하나만 따로 다시 돌리려면:

```bash
cd repairable-state-discovery
PROTOCOL_PATH=repairable_diffusion/configs/final/protocol_math500_final.yaml \
PROTOCOL_FAMILIES=ar \
PROTOCOL_RUN_NAMES=math500_final_ar_qwen25_7b \
  sbatch scripts/run_protocol_repairability_final.sh
```

## 산출물

### Run-level artifact

```text
repairable_diffusion/outputs/runs/<run_name>/
  config.snapshot.json
  trajectories.pkl
  trajectories.light.jsonl
  trajectory_summary.json
  oracle_repair.json
  repair_predictor.json
  repair_selection_eval.json
  report.json
```

### Protocol-level artifact

```text
results/generated_configs/
  protocol_gsm8k_final_report.json
  protocol_math500_final_report.json
  protocol_math500_submission_robustness_report.json
```

### Aggregate artifact

```text
results/final_reports/
  aggregate_report.json
  diffusion_summary.csv
  ar_summary.csv
  tables/
    diffusion_markdown.md
    ar_markdown.md
    diffusion_latex.tex
    ar_latex.tex

results/submission_reports/
  aggregate_report.json
  diffusion_summary.csv
  ar_summary.csv
  tables/
    diffusion_markdown.md
    ar_markdown.md
    diffusion_latex.tex
    ar_latex.tex
```

## 구현 포인트

- submission-ready diffusion main은 `GSAI-ML/LLaDA-8B-Instruct` 기반 `repairable-state localization and evaluation`을 수행합니다.
- AR baseline은 `transformers` causal LM backend를 사용합니다.
- final stable suite는 `MATH-500`, `GSM8K`, `MATH-500 robustness` 세 프로토콜로 구성됩니다.
- repair operation은 `anchored remask + multi-branch restart probe`입니다.
- predictor는 logistic regression 기반 multi-signal step scorer입니다.
- summary metric은 sample accuracy 외에 `item pass@1`, `item pass@k`, `expected newly solved`, `negative repair rate`, `peak repair step`, `repairable failed rate`, `predictor-oracle gap`까지 저장합니다.

## 알려진 한계

- 현재 로컬 `.venv`는 저장소 안에 포함되어 있지 않습니다.
- 테스트는 매우 제한적이며, protocol/aggregation/reporting 경로에 대한 회귀 테스트가 없습니다.
- run-level heavy artifacts는 GitHub에 올리지 않습니다. `repairable_diffusion/outputs/`와 `.hf_home/`은 `.gitignore`에 포함되어 있으며, repo에는 source/config/report summary만 versioning합니다.
