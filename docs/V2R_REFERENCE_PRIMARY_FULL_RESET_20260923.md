# ICLR 2027 — REFERENCE-PRIMARY FULL RESET

이 요청을 현재 프로젝트의 **최종 scientific execution directive**로 사용한다.

이전 V2 full-run 계획을 이어서 완주하는 것이 목적이 아니다.

현재 primary experiment execution을 중단하고, **정상적으로 재현된 reference baseline 위에서 전체 paper-critical experiment를 새 execution generation으로 다시 구성하고 실행한다.**

목표:

```text
reference baseline reproduction
→ paper-task bridge validation
→ instrumentation exact-equivalence
→ reference-quality trajectory bank
→ failed-trajectory repairability
→ temporal / mechanism / localization
→ cross-backbone replication
→ provenance sealing
→ paper integration
```

이번에는 처음부터 이 chain을 지킨다.

---

## 1. 기존 진행 중 scientific jobs 정리

현재 우리 프로젝트에서 실행 중인:

* `50668` LLaDA × MATH-500
* `50669` LLaDA × GSM8K

는 더 이상 primary paper execution으로 유지하지 않는다.

먼저 각 job에 대해 다음을 snapshot한다.

* Slurm metadata
* job state
* execution SHA
* config SHA
* workdir
* stdout/stderr path
* 현재 존재하는 artifact 목록
* artifact size/mtime/hash where feasible
* elapsed runtime

그리고 상태를:

```text
CANCELLED_FOR_REFERENCE_PRIMARY_RESET
```

으로 기록한다.

그 후 **우리 소유의 50668/50669를 cancel하여 GPU를 반환한다.**

단:

* artifact 삭제 금지
* worktree reset 금지
* output overwrite 금지

기존 incomplete artifact는 historical/read-only 상태로 보존한다.

---

## 2. 기존 완료 결과의 지위

기존:

* 50753 BBH-LD7 SEALED
* 50754 MBPP SEALED
* 50923 Dream-MATH SEALED
* 기타 old V2 artifacts

는 삭제하지 않는다.

하지만 새 reference-primary 결과가 나오기 전까지 **main-paper primary evidence로 간주하지 않는다.**

분류:

```text
LEGACY_MEASUREMENT_DECODER_EVIDENCE
```

로 둔다.

향후:

* appendix
* decoder-regime comparison
* robustness
* exploratory evidence

로 사용할 수 있다.

기존 결과를 새 reference 결과와 동일 protocol인 것처럼 aggregate하지 않는다.

---

## 3. 50924는 critical path에서 제외

50924 Dream-GSM의 seed/provenance forensic은 보존하되,

새 reference-primary 실행을 기다리게 하지 않는다.

기존 50924를 억지로 seal하지 않는다.

새 pipeline에서는 처음부터 collision-free RNG design을 사용한다.

---

# 4. 새 scientific generation

새 namespace:

```text
v2r_reference
```

를 사용한다.

예:

```text
repairable_diffusion/outputs/v2r_reference/
results/v2r_reference/
status/v2r/
```

기존 `v2_measurement`를 수정하거나 덮어쓰지 않는다.

새 development branch를 만들고,

R0/R1/R2 validation이 끝나면 **scientific execution SHA 하나를 freeze**한다.

예:

```text
codex/v2r-reference-primary-20260923
```

R3 이후 모든 scientific jobs는 exact same SHA에서 실행한다.

---

# 5. 결과 보기 전에 protocol freeze

먼저:

```text
docs/V2R_REFERENCE_PRIMARY_PROTOCOL.md
```

를 작성하고 commit한다.

반드시 freeze:

* models
* model revisions
* datasets
* prompts
* evaluators
* official/reference sampler recipes
* seeds
* trajectory definition
* checkpoint grid
* localization branches
* confirmation branches
* threshold
* failed-trajectory selection
* deep subset size rule
* mechanism subset size rule
* temporal subset size rule
* primary metrics

R3 결과를 보고 이 값을 변경하지 않는다.

---

# 6. R0 — 공식/reference baseline reproduction

LLaDA와 Dream의 upstream official evaluation implementation을 직접 조사한다.

추측하지 않는다.

각 backbone에 대해 pin:

* repository
* source commit/revision
* model ID/revision
* tokenizer
* chat template
* evaluation script
* generation length
* diffusion steps
* block length
* sampling algorithm
* temperature
* top-p/top-k
* CFG
* EOS/EOT semantics
* task-specific flags
* evaluator

결과:

```text
docs/REFERENCE_REPRODUCTION_SOURCES.md

results/v2r_reference/reference_recipes/
    llada.json
    dream.json
```

공식 reported metric과 우리의 dataset이 정확히 동일하지 않으면:

```text
NOT_DIRECTLY_COMPARABLE
```

로 명시한다.

score를 맞추기 위해 parameter tuning하지 않는다.

---

# 7. R0 smoke

각 backbone에서 먼저 16~32 item smoke를 실행한다.

검증:

* model load
* prompt
* tokenizer
* output
* evaluator
* generation termination
* mask exhaustion
* GPU memory
* runtime
* NFE

PASS하지 않으면 full baseline submit 금지.

---

# 8. R1 — 우리 paper task에서 reference decoder 검증

Primary paper tasks:

```text
LLaDA × MATH-500
LLaDA × GSM8K

Dream × MATH-500
Dream × GSM8K
```

reference decoder를 그대로 사용하면서 우리의 exact:

* dataset
* prompt
* evaluator

를 연결한다.

가능하면 동일 generated output에 official evaluator와 our evaluator를 둘 다 적용한다.

evaluator disagreement는 저장한다.

---

# 9. R2 — instrumentation exact equivalence

repairability 실험 전에 반드시 검증한다.

같은:

* item
* prompt
* seed
* model
* reference sampler

에 대해:

```text
uninstrumented generation
vs
snapshot-instrumented generation
```

을 비교한다.

PASS 조건:

```text
final token IDs exact match = 100%
final decoded output exact match = 100%
answer/correctness exact match = 100%
decoder schedule match
NFE consistency
```

snapshot instrumentation이 RNG consumption이나 generation semantics를 바꾸면 R3 submit 금지.

최소:

* 32 items/backbone
* multiple deterministic seeds

에서 확인한다.

---

# 10. R2 PASS 후 scientific SHA freeze

LLaDA와 Dream reference instrumentation이 PASS하면:

* source clean
* tests PASS
* config frozen

상태에서 execution SHA를 freeze한다.

scientific worktree는 실행 중 immutable.

금지:

* pull
* checkout
* commit
* merge
* reset
* artifact commit

---

# 11. Primary baseline은 1 trajectory/item

새 reference-primary experiment에서는 기존의:

```text
8 trajectories per item
```

을 반복하지 않는다.

Primary scientific unit:

```text
one sampled reference-quality trajectory
```

이다.

full task에서:

### LLaDA

MATH-500:

```text
500 items × 1 trajectory
```

GSM8K:

```text
1319 items × 1 trajectory
```

### Dream

동일.

Primary baseline metric:

```text
trajectory accuracy / pass@1
```

이다.

---

# 12. 동일 trajectory bank를 repairability에 사용

baseline sanity용 generation과 scientific generation을 따로 만들지 않는다.

R2를 통과한 instrumented reference decoder로 생성한 **exact same full trajectory bank**를:

```text
baseline evaluation
+
failed trajectory pool
+
state-level counterfactual experiment
```

에 모두 사용한다.

이중 generation 금지.

---

# 13. Deep probing은 실패 trajectory subset에만

full dataset 전체에 branching하지 않는다.

base bank에서 final incorrect trajectory를 모아:

```text
failed trajectory pool
```

을 만든다.

repairability outcome은 보지 않는다.

고정 hash ranking:

```text
SHA256(
  design_seed |
  backbone |
  task |
  item_id |
  trajectory_id
)
```

으로 deterministic ordering한다.

---

# 14. GPU-budget-aware primary sample

R2 timing pilot로 실제 throughput을 측정한다.

효과 크기를 보지 않고:

* available GPUs
* sec/branch
* deadline

만으로 sample size를 freeze한다.

Target:

### LLaDA MATH

```text
64 failed trajectories
```

### LLaDA GSM8K

```text
64 failed trajectories
```

minimum:

```text
32 / task
```

### Dream MATH

target:

```text
32 failed trajectories
```

### Dream GSM8K

target:

```text
32 failed trajectories
```

GPU 여유가 충분하면 Dream 64까지 확대 가능.

sample size 변경은 outcome을 근거로 하지 않는다.

---

# 15. Core checkpoint design

reference sampler가 몇 step을 쓰든 normalized refinement grid를 사용한다.

```text
0.125
0.250
0.375
0.500
0.625
0.750
0.875
```

각 normalized location과 가장 가까운 valid snapshot을 deterministic하게 저장한다.

final endpoint는 별도 metadata로 보존.

---

# 16. Core counterfactual measurement

모든 selected failed trajectory에서:

```text
o_t
q_C(x_t)
q_R(x_t)
Delta_R(x_t)
```

를 측정한다.

Localization:

```text
B_loc = 4
```

Independent confirmation:

```text
B_eval = 8
```

Canonical threshold:

```text
tau_confirm = 0.25
```

Sensitivity:

```text
0.125
0.25
0.5
```

---

# 17. 계산 절약: two-stage probing

모든 checkpoint에 B_eval=8을 사용하지 않는다.

각 failed trajectory에서:

### Stage 1

7 normalized checkpoints에:

```text
B_loc=4
```

cheap localization.

### Stage 2

predeclared selector/oracle-selected candidate에만:

```text
B_eval=8
```

independent confirmation.

dense temporal confirmation은 별도 subset에서만 수행.

---

# 18. Temporal subset

제목의 timing claim을 위해 LLaDA에서만 우선 수행.

각 task:

```text
32 failed trajectories
```

target.

모든 normalized checkpoints에서 independent confirmation.

산출:

```text
qC(t)
qR(t)
Delta(t)
T_last
repairability survival
```

monotonicity 강제 금지.

---

# 19. Mechanism subset

LLaDA anchors 각각:

```text
32 failed trajectories
```

에서 수행.

비교:

* matched stochastic continuation
* canonical low-confidence repair
* random-position remask
* CoRe snapshot
* native exact continuation
* actual fresh-sampling compute control where feasible

산출:

* recovery
* intervention lift
* harm
* modified token count
* NFE

Dream에서 full mechanism factorial은 요구하지 않는다.

---

# 20. Localization

reference-primary trajectory에서도 frozen OOF selector를 평가한다.

post-hoc selector tuning 금지.

Primary policy evaluation은:

```text
one reference trajectory/item
→ pre-intervention observable selector
→ intervention
→ prospective trajectory correctness
```

로 한다.

successful trajectories에 대한 harm도 반드시 포함한다.

---

# 21. 새 seed design

기존 31-bit hashed stage seed collision 문제를 반복하지 않는다.

각 RNG event에 대해:

```text
stage
item
trajectory
checkpoint
branch
paired_rng_group
```

을 deterministic하게 encode한다.

다음 stage는 반드시 disjoint:

```text
localization
confirmation
fresh
independent control
```

paired matched-vs-repair branch만 의도된 동일 future-noise RNG group을 공유할 수 있다.

job 제출 전에 모든 예정 seed registry를 CPU에서 생성하여:

```text
no unintended collision
```

을 assert한다.

---

# 22. GPU를 제한적으로 가장 효율적으로 사용

새 scientific priority:

```text
1. LLaDA MATH
2. LLaDA GSM8K
3. Dream MATH
4. Dream GSM8K
5. optional anything else
```

새 BBH/MBPP reference rerun은 deadline 전 수행하지 않는다.

---

# 23. 서버 1~4 전체 inventory

기존 jobs cancel 이후 다시 inventory한다.

각 서버:

* GPU model/count
* utilization
* VRAM
* active allocations/processes
* Slurm status
* CPU/RAM
* filesystem free space
* inode
* worktree
* usable output path

결과:

```text
status/v2r/cluster_inventory.json
```

---

# 24. GPU allocation

무조건 server1~4 모두 사용하지 않는다.

다음을 만족하는 GPU만:

```text
idle
+
no conflicting allocation
+
enough VRAM
+
enough storage
```

사용.

다른 사용자의 GPU/process에는 손대지 않는다.

기본:

```text
1 model process / GPU
```

---

# 25. storage protection

server3/server4처럼 disk가 임계인 곳에 raw snapshot job을 무작정 제출하지 않는다.

new shard의 projected output ×2 이상 free space가 없으면 submit하지 않는다.

파일 자동 삭제 금지.

---

# 26. 모든 새 실험 shard화

multi-day monolithic job 금지.

timing pilot 후:

```text
target shard time = 2~4 hours
hard preference < 6 hours
```

으로 나눈다.

예:

```text
MATH base:
shard00
shard01
shard02
shard03
...

MATH repair:
shard00
shard01
...
```

GPU가 여러 개면 병렬 실행.

---

# 27. Shard는 deterministic / resumable

assignment:

```text
hash(run_fingerprint | item_id) % num_shards
```

등 outcome-independent deterministic rule.

보장:

* no overlap
* no missing
* resumable
* reproducible

각 shard:

```text
shard_manifest.json
progress.json
DONE.json
hashes
```

보유.

---

# 28. Single-writer merge

worker가 aggregate를 수정하지 않는다.

controller 하나만 merge.

merge gate:

* expected shards all DONE
* SHA identical
* config hash identical
* model revision identical
* dataset hash identical
* no duplicate item
* no missing item
* no seed collision
* expected row counts
* artifact hashes valid

실패 시:

```text
AGGREGATION_BLOCKED
```

---

# 29. Persistent autonomous orchestration

별도 tmux:

```text
iclr2027-reference-orchestrator
```

를 구성한다.

Astra chat session이 끝나도 계속 실행.

loop:

```text
resource inventory
→ job/shard status
→ validate gates
→ submit eligible next shards
→ merge completed shards
→ seal eligible runs
→ generate compact artifacts
→ update paper readiness
→ Git commit/push status
```

30분 주기.

중요 event는 즉시 push.

---

# 30. 기존 monitor

현재 `iclr2027-live-monitor`는 기존 V2 cancellation snapshot까지 유지한다.

새 reference orchestrator가 안정화되면 old V2 monitor는 scientific execution을 변경하지 않는 범위에서 historical monitor 상태로 둘 수 있다.

자동으로 kill하지 않아도 된다.

---

# 31. provenance

모든 run/shard에:

* execution SHA
* config SHA
* model revision
* tokenizer revision
* dataset/subset hash
* trajectory-bank hash
* reference recipe ID/hash
* evaluator version
* RNG registry hash
* artifact hashes

를 기록한다.

SEALED artifact만 manuscript evidence로 사용한다.

---

# 32. Main-paper 목표

새 reference-primary result가 완료되면 main evidence를 다음 구조로 생성한다.

## Table 1

```text
Backbone
Task
Reference accuracy
Failed trajectories probed
Native recoverable
Confirmed repairable
Never-correct repairable
T_last
```

## Table 2

LLaDA reference mechanism controls.

## Table 3

Reference prospective localization.

## Figure 2

Reference temporal recoverability.

## Appendix

기존 measurement-decoder V2 comparison.

---

# 33. 기존 V2와 새 V2R 절대 혼합 금지

논문에서는 필요하면:

```text
Reference-decoder regime
Measurement-decoder regime
```

으로 명확히 구분한다.

old V2 결과를 새 reference experiment의 missing cell에 채워 넣지 않는다.

---

# 34. Paper 작업도 병렬 수행

GPU 실험 동안 CPU-side로:

* reference vs measurement terminology 수정
* `failed_items_probed` naming 문제 수정
* pass@1 vs pass@8 구분
* result importer 수정
* new table generators
* new figure generators
* claim ledger
* provenance import
* PDF audit failure 수정

을 수행한다.

final numerical claim은 SEALED result 이후 채운다.

---

# 35. 최소 제출 성공선

GPU/시간이 매우 부족해도 우선 다음을 확보한다.

### MUST

```text
LLaDA MATH:
reference reproduction
R2 equivalence
core repairability
temporal subset

LLaDA GSM8K:
reference reproduction
R2 equivalence
core repairability
```

### NEXT

```text
Dream MATH:
reference reproduction
core repairability replication

Dream GSM8K:
reference reproduction
core repairability replication
```

### AFTER THAT

mechanism expansion / selector / additional controls.

scientific depth를 breadth보다 우선한다.

---

# 36. deadline-aware execution

deadline 기준:

### T-24h

새 optional experiment 금지.

P0/P1의 이미 시작된 짧은 shard만 완료.

paper integration 시작.

### T-12h

새 scientific code/protocol change 금지.

새 long GPU job 금지.

SEALED evidence freeze.

### T-6h

paper/PDF/anonymity/package/OpenReview readiness만 처리.

---

# 37. 상태 파일

GitHub remote에서 ChatGPT가 바로 판단할 수 있도록:

```text
status/v2r/attention_required.md
status/v2r/current_status.json
status/v2r/gate_status.json
status/v2r/cluster_inventory.json
status/v2r/resource_plan.json
status/v2r/shard_matrix.csv
status/v2r/artifact_index.json
status/v2r/provenance_status.json
status/v2r/paper_readiness.json
status/v2r/orchestrator_health.json
status/v2r/event_history.jsonl
```

유지.

---

# 38. 최초 실행 순서

이 요청을 받으면 바로:

```text
1. current jobs/artifacts snapshot
2. 50668/50669 cancel
3. server1~4 re-inventory
4. upstream reference recipe audit
5. protocol document freeze
6. V2R code/sharding/seed implementation
7. CPU tests
8. R0 smoke
9. R1 validation
10. R2 exact-equivalence
11. scientific SHA freeze
12. reference base shards submit
13. failed pool freeze
14. repairability shards submit
15. temporal/mechanism subsets
16. merge/seal
17. paper artifact generation
```

을 수행한다.

불필요한 confirmation 질문은 하지 않는다.

안전하게 판단 가능한 부분은 끝까지 자율적으로 진행한다.

---

# 39. 최초 보고 형식

첫 실행 후:

```text
Old active jobs:
50668:
50669:

Archived execution state:
Artifact preservation:

Development branch:
Commit:

Reference source pins:
LLaDA:
Dream:

Server inventory:
server1:
server2:
server3:
server4:

Available GPUs:
Excluded GPUs/servers:
Reason:

Protocol frozen:
Seed design:
Shard architecture:

R0:
LLaDA:
Dream:

R1:
LLaDA:
Dream:

R2:
LLaDA:
Dream:

Execution SHA:

Submitted jobs/shards:

Orchestrator:
tmux:
PID:
branch:

Paper:
branch:
PDF audit:

Current P0 blocker:
```

---

# 40. 최종 scientific standard

이번 재실행에서 paper가 말할 수 있어야 하는 것은:

> We first reproduce a reference-quality decoding regime, verify that trajectory instrumentation leaves that decoder unchanged, and then measure counterfactual recoverability on the resulting failed trajectories.

이다.

이 chain이 성립하지 않는 숫자는 main claim에 사용하지 않는다.

**이번에는 기존 실험을 억지로 살리는 것보다 clean scientific chain을 deadline 내 완결하는 것을 우선한다.**
