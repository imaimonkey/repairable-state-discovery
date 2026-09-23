# ICLR 2027 Full-Paper Recovery — FINAL MASTER REQUEST

이 요청이 현재 프로젝트의 **최종 실행 지침**이다.

이전의 V2/V2R 관련 임시 요청보다 이 지침을 우선한다.

목표는 단순히 기존 실험을 더 돌리는 것이 아니다.

현재 빠져 있던 **reference baseline reproduction gate**부터 다시 세우고,

```text
reference-quality baseline
→ exact instrumentation equivalence
→ same reference trajectory 위 counterfactual repairability
→ mechanism / temporal / localization
→ cross-backbone validation
→ provenance-sealed evidence
→ paper integration
```

의 일관된 chain을 만들어 ICLR 2027 full paper를 완결하는 것이다.

가장 중요한 현실 제약:

* deadline이 매우 가깝다.
* GPU는 한정되어 있다.
* server1~4의 자원/디스크 상태가 서로 다르다.
* 기존 장시간 V2 jobs가 이미 실행 중이다.
* 따라서 “전체 matrix를 또 무식하게 full rerun”하면 안 된다.
* scientific validity와 GPU efficiency를 동시에 만족해야 한다.

---

# 0. 가장 중요한 연구 원칙

새 **primary evidence**는 반드시:

```text
재현된 reference baseline
위에서
우리 repairability experiment를 수행한 결과
```

여야 한다.

기존 measurement-decoder V2가 자동으로 primary가 되는 것이 아니다.

기존 V2의 최종 역할은 새 reference experiment 결과를 본 뒤 결정한다.

가능한 역할:

* secondary evidence
* decoder-regime robustness
* appendix
* exploratory evidence

새 reference result가 충분히 확보되면 그것을 main scientific evidence로 사용한다.

---

# 1. 기존 결과/잡은 삭제하지 말 것

현재 기존 V2:

* 50668 LLaDA × MATH-500 — RUNNING
* 50669 LLaDA × GSM8K — RUNNING
* 50738 BBH-LD3 — COMPLETED but currently unobserved
* 50752 BBH-LD5 — FAILED_EXCLUDED
* 50753 BBH-LD7 — SEALED
* 50754 MBPP — SEALED
* 50923 Dream-MATH — SEALED
* 50924 Dream-GSM — COMPLETED_UNSEALED

이 artifact를 삭제/overwrite/reset하지 않는다.

현재 실행 중인 50668/50669도 일단 kill하지 않는다.

그러나 새 reference-primary experiment보다 우선한다고 가정하지 않는다.

기존 job 때문에 reference-primary가 deadline 내 완료 불가능하다고 판단되는 경우:

**자동으로 cancel하지 말고**

```text
PREEMPTION_RECOMMENDED
```

상태로 정확한 GPU/ETA/손실량을 보고한다.

사용자 승인 없이 장시간 기존 job을 kill하지 않는다.

---

# 2. 기존 live monitor 유지

현재:

```text
tmux: iclr2027-live-monitor
branch: codex/iclr2027-live-monitor-20260923
```

의 30분 monitoring loop를 절대 종료/교체하지 않는다.

새 reference pipeline은 별도 orchestrator와 별도 branch를 사용한다.

예:

```text
tmux: iclr2027-reference-orchestrator
branch: codex/iclr2027-reference-live-20260923
```

---

# 3. 새 실험 namespace

기존:

```text
v2_measurement
```

와 완전히 분리한다.

새 이름:

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

기존 scientific artifact를 새 실험에 재사용하는 경우에도
원본을 수정하지 않는다.

---

# 4. 결과를 보기 전에 Design Revision freeze

먼저 다음 문서를 작성한다.

```text
docs/V2R_REFERENCE_DESIGN_20260923.md
```

내용:

## Scientific motivation

기존 V2가 replayable counterfactual measurement를 위해 고정된 decoder를 사용했지만,
official/reference benchmark decoding reproduction이 primary experiment 이전에 명시적으로 검증되지 않았다.

따라서 새 primary validation은:

> Does counterfactual repairability persist under a reference-quality decoder whose baseline behavior is first independently reproduced?

를 검증한다.

## 새 primary scientific object

단위는 **sampled trajectory**이다.

다음과 혼동하지 않는다.

* pass@8 failed item
* item-level oracle
* benchmark-optimized multi-sample pass@k

Primary denominator:

```text
sampled trajectories whose final answer is incorrect
```

이다.

## 결과 보기 전에 freeze

* task
* model
* reference recipe
* trajectory seed
* checkpoint grid
* failed-trajectory selection
* branch counts
* confirmation threshold
* subset-size budgeting rule
* primary metrics

을 R3 결과 보기 전에 commit한다.

---

# 5. 기존 metric naming 오류도 수정

현재 V2의:

```text
base_pass_at_k
failed_items_probed
```

는 새 V2R에서 그대로 사용하지 않는다.

명확히 분리:

```text
reference_trajectory_accuracy
measurement_trajectory_accuracy

pass_at_k
all_k_failed_item_rate

sampled_trajectory_count
sampled_failed_trajectory_count

items_with_at_least_one_failed_trajectory

confirmed_repairable_failed_trajectory_rate
repairable_but_never_correct_failed_trajectory_rate
```

특히:

`failed_items_probed`

처럼 pass@8 failure와 혼동되는 이름은 새 schema에서 금지한다.

---

# 6. R0 — Source-native baseline reproduction

LLaDA / Dream 각각 upstream official source를 직접 조사한다.

추측하지 않는다.

반드시 pin:

* repository
* commit/revision
* model ID
* model revision
* tokenizer
* official evaluation script
* dataset
* dataset split
* prompt/template
* generation length
* steps
* block length
* sampling algorithm
* temperature
* top-p/top-k
* CFG
* special EOS/EOT handling
* evaluator

결과:

```text
results/v2r_reference/reference_recipes/
    llada.json
    dream.json

docs/REFERENCE_REPRODUCTION_SOURCES.md
```

공식 reported result와 정확히 같은 benchmark가 아니라면:

```text
NOT_DIRECTLY_COMPARABLE
```

이라고 기록한다.

비슷하다는 이유로 숫자를 억지 비교하지 않는다.

---

# 7. R0 smoke를 먼저 수행

대규모 job 전에:

각 model × anchor task에서

```text
16~32 items
1 trajectory/item
```

만 돌린다.

확인:

* model load
* tokenizer
* chat template
* completion
* evaluator
* NFE
* GPU memory
* runtime
* mask exhaustion
* output format

여기서 실패하면 full job 금지.

---

# 8. R0 full baseline

reference/source-native baseline은 **1 trajectory/item**로 평가한다.

현재 연구에서는 pass@8을 reference baseline의 primary metric으로 쓰지 않는다.

Primary:

```text
trajectory accuracy / pass@1
```

Anchor:

```text
LLaDA × MATH-500
LLaDA × GSM8K
Dream × MATH-500
Dream × GSM8K
```

단 source-native official benchmark가 정확히 다른 dataset인 경우:

1. source-native official reproduction
2. 우리 exact paper dataset bridge evaluation

를 분리한다.

parameter를 score 맞추기 위해 search/tune하지 않는다.

---

# 9. R1 — Bridge validation

source-native sampler를 유지한 채 우리:

* dataset
* task adapter
* prompt
* evaluator

와 연결한다.

가능하면 동일 generation output에:

```text
official evaluator
our evaluator
```

둘 다 적용한다.

disagreement 저장:

```text
evaluator_disagreements.jsonl
```

특히 MATH:

* boxed extraction
* symbolic equivalence
* normalization

GSM8K:

* numeric extraction
* decimal/comma normalization

을 검증한다.

---

# 10. R2 — Instrumentation equivalence

이 단계가 PASS하기 전 repairability 실행 금지.

동일:

* model
* tokenizer
* prompt
* seed
* reference sampler
* generation config

에서:

```text
uninstrumented reference
vs
instrumented reference
```

를 비교한다.

필수:

```text
final token sequence exact match = 100%
final answer exact match = 100%
correctness match = 100%
schedule match
NFE consistency
```

instrumentation이 random-number consumption을 바꾸면 안 된다.

snapshot 저장 때문에 decoder output이 달라지면 R3를 돌리지 않는다.

검증:

* 최소 32 fixed items
* multiple fixed seeds
* early/mid/late trajectories

---

# 11. 중요: Reference Primary는 기존 8 trajectories/item을 복제하지 않는다

새 primary experiment에서 무조건:

```text
8 base trajectories × 모든 item
```

를 반복하지 않는다.

우리 핵심 question은:

> 최종적으로 실패한 trajectory의 중간 state에 recovery potential이 있는가?

이므로 reference primary에서는:

```text
1 reference-quality trajectory / item
```

를 기본 단위로 한다.

이게:

* official/reference accuracy와 직접 연결되고
* denominator가 명확하며
* GPU를 크게 절약하고
* trajectory-level scientific question에도 더 직접적이다.

기존 pass@8 analysis는 기존 V2/secondary analysis로 남긴다.

---

# 12. Base trajectory bank

각 full anchor dataset에 대해:

```text
1 trajectory/item
```

reference-quality generation을 수행한다.

즉:

```text
MATH-500: 500 trajectories
GSM8K: 1319 trajectories
```

per backbone.

여기서:

* correct
* failed

trajectory pool을 생성한다.

trajectory generation 때부터 snapshot instrumentation을 켜되,
R2에서 output equivalence가 검증된 exact implementation만 사용한다.

따라서 baseline용 trajectory를 나중에 다시 생성하지 않는다.

**same exact trajectory bank를 R3에서 사용한다.**

---

# 13. Failed trajectory subset 선택

deep probing은 full dataset 전체에 수행하지 않는다.

reference base trajectory bank가 완성된 뒤:

```text
failed trajectory pool
```

에서 deterministic selection한다.

repairability 결과는 전혀 참조하지 않는다.

예:

```text
rank = SHA256(
    design_seed |
    backbone |
    task |
    item_id |
    trajectory_id
)
```

순으로 failed trajectory를 정렬한다.

그 후 predeclared budget만큼 선택한다.

---

# 14. GPU-budget-aware deep sample size

무조건 N=128을 고정해서 deadline을 넘기지 않는다.

R2 timing pilot에서:

* sec/base trajectory
* sec/checkpoint continuation
* sec/branch
* storage/item
* NFE

를 계산한다.

그 뒤 **effect를 보기 전에** 다음 규칙으로 N을 결정한다.

Primary LLaDA anchors:

```text
target = 128 failed trajectories / task
minimum acceptable = 64 / task
```

Dream validation:

```text
target = 64 failed trajectories / task
minimum acceptable = 32 / task
```

N 선택은:

```text
available GPU-hours
deadline
measured throughput
```

만 사용한다.

qR / repairability outcome을 보고 N을 변경하면 안 된다.

선택된 N과 계산 근거를 manifest에 freeze한다.

---

# 15. Checkpoint grid

reference decoder의 step 수가 기존 64와 다를 수 있다.

절대 step 번호를 강제로 맞추지 않는다.

normalized grid:

```text
0.125
0.250
0.375
0.500
0.625
0.750
0.875
```

* final endpoint metadata

를 사용한다.

각 값에 가장 가까운 valid decoder state를 deterministic하게 선택한다.

paper에서는 normalized refinement progress로 비교한다.

---

# 16. R3 core repairability

모든 selected failed trajectory에서:

```text
o_t
q_C
q_R
Delta_R
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

Canonical:

```text
tau_confirm = 0.25
```

Sensitivity:

```text
0.125
0.25
0.5
```

Primary metrics:

```text
confirmed_repairable_failed_trajectory_rate

repairable_but_never_correct_failed_trajectory_rate

native_recoverable_failed_trajectory_rate

mean q_C

mean q_R

mean Delta_R

T_last^R

repairability survival
```

---

# 17. Seed design은 새로 수정

기존:

```python
hash(...) % (2**31 - 1)
```

방식으로 stage independence를 가정하지 않는다.

새 V2R에서는 **unintended collision이 수학적으로 불가능하거나 사전 검출되는 scheme**을 사용한다.

각 RNG context:

```text
stage
item
trajectory
checkpoint
branch
paired_rng_group
```

을 deterministic하게 encode한다.

matched stochastic continuation과 repair operator가 같은 future noise를 공유해야 하는 paired comparison에서는 의도적으로 동일 RNG group을 사용한다.

하지만:

```text
localization
confirmation
fresh sampling
independent control
```

사이에는 절대 seed 재사용 금지.

모든 job 제출 전 CPU에서 full expected seed registry를 생성하고:

```text
assert no unintended collisions
```

한다.

---

# 18. RQ2 mechanism controls — 제한된 budget으로 수행

LLaDA reference anchors에서만 우선 수행한다.

전체 failed set에 모든 control을 돌리지 않는다.

별도 deterministic mechanism subset:

```text
target 64 failed trajectories/task
minimum 32
```

을 predeclare한다.

비교:

* exact native continuation
* matched stochastic continuation
* canonical low-confidence remask
* random-position remask
* CoRe snapshot
* actual fresh sampling compute control

필수 metric:

* failed recovery
* qR-qC
* harm / degradation
* modified positions
* NFE

Dream에서는 external mechanism factorial을 우선순위 낮게 둔다.

---

# 19. Temporal confirmation

제목의 “When Does … Become Irrecoverable?”를 유지하려면 필수.

LLaDA anchors에서 deterministic temporal subset:

```text
target 64 failed trajectories/task
minimum 32
```

에 대해 normalized checkpoint 전체에서 independent confirmation을 수행한다.

출력:

```text
T_last
survival curve
qC(t)
qR(t)
Delta(t)
```

단 monotonicity를 강제하지 않는다.

---

# 20. RQ3 localization은 새 reference trajectory에서 재평가

reference primary에서도 frozen OOF state-value estimator를 평가한다.

단 결과가 약하면 그대로 보고한다.

post-hoc selector 교체 금지.

trajectory-level prospective policy를 primary로 사용한다.

즉:

```text
one base trajectory/item
→ selected checkpoint intervention
→ prospective trajectory accuracy
```

를 평가한다.

원래 pass@8 policy를 억지로 다시 만들기 위해 8 trajectories/item을 생성하지 않는다.

성공 trajectory에서의 harm도 포함해야 한다.

필요하면 successful trajectory policy evaluation은 deterministic subset에서 수행한다.

---

# 21. Primary experiment 우선순위

GPU가 부족하므로 다음 순서를 강제한다.

## P0 — 반드시 확보

1. LLaDA R0/R1/R2
2. Dream R0/R1/R2
3. LLaDA MATH reference base full
4. LLaDA GSM8K reference base full
5. LLaDA MATH core repairability
6. LLaDA GSM8K core repairability
7. LLaDA temporal subset
8. basic mechanism controls

## P1 — 매우 중요

9. Dream MATH reference base/full repairability subset
10. Dream GSM8K reference base/full repairability subset
11. OOF localization
12. fresh-sampling controls

## P2 — 시간이 남을 때

* additional seeds
* more mechanism rows
* additional decoder-regime robustness
* extra breadth datasets
* optional operators

P2가 P0 GPU를 절대 막지 않는다.

---

# 22. 기존 BBH/MBPP를 reference-primary로 다시 돌리지 않는다

deadline 전에는:

* BBH-LD3/5/7
* MBPP

를 reference decoder로 다시 full rerun하지 않는다.

현재 이미 확보된 breadth evidence는 secondary evidence로 보존한다.

새 primary matrix는 우선:

```text
LLaDA MATH
LLaDA GSM8K
Dream MATH
Dream GSM8K
```

의 4 anchor다.

---

# 23. 서버 1~4 resource inventory부터 수행

job 제출 전에 모든 서버를 read-only inventory한다.

필수:

* GPU count/model
* GPU util
* VRAM used/free
* active processes
* Slurm allocations
* CPU/RAM
* disk/free bytes
* inode
* repo paths
* worktrees
* active scientific jobs
* safe output filesystem

결과:

```text
status/v2r/cluster_inventory.json
status/v2r/cluster_inventory.md
```

---

# 24. GPU allocation 원칙

“4대 서버니까 4대 모두 사용”하지 않는다.

사용 조건:

```text
idle GPU
+
sufficient VRAM
+
safe disk
+
safe worktree
```

를 모두 만족해야 한다.

기존 다른 사용자의 process 위에 겹쳐 실행하지 않는다.

Slurm이 있으면 Slurm allocation을 우선한다.

GPU memory가 남는다는 이유로 자동 multi-process packing하지 않는다.

기본:

```text
1 model process / GPU
```

---

# 25. 서버별 현재 보호 규칙

## server1

50668/50669 실행 중.

기존 execution worktree:

```text
/home/kimhj/repairable-state-discovery-v2-exec
```

절대 수정하지 않는다.

새 reference experiment는:

* idle GPU가 실제 존재하고
* 별도 worktree를 만들 수 있고
* storage가 안전한 경우

에만 submit.

## server2

breadth artifacts가 있으므로 기존 worktree 보호.

새 clean worktree만 사용.

현재 가장 먼저 reference workload를 배치할 후보가 될 수 있으나 실제 GPU inventory 후 결정.

## server3

현재 storage가 critical/full에 가까운 것으로 알려져 있다.

새 raw trajectory/snapshot write-heavy job은 기본 금지.

충분한 별도 filesystem을 확인한 경우에만 사용.

## server4

/data 사용량이 매우 높은 상태.

대용량 raw trajectory를 새로 쓸 수 있는지 반드시 free-space gate 확인.

안전한 별도 filesystem이 없다면:

* CPU analysis
* compact aggregation

정도만 사용.

자동 파일 삭제 금지.

---

# 26. Storage gate

new shard 예상 output size의 최소:

```text
2 × projected output
```

여유 공간 + safety margin이 있어야 한다.

filesystem usage가 임계 상태면 job 제출 금지.

삭제 후보만 보고한다.

자동 cleanup 금지.

---

# 27. Monolithic job 금지

새 V2R은 giant 2~5일 job으로 만들지 않는다.

item-level deterministic sharding을 구현한다.

필요한 scripts 예:

```text
scripts/v2r_inventory.py
scripts/v2r_plan.py
scripts/v2r_submit.py
scripts/v2r_worker.py
scripts/v2r_merge.py
scripts/v2r_seal.py
scripts/v2r_status.py
```

---

# 28. shard planning

각 backbone/config에서 먼저 8~16 item timing pilot 수행.

측정:

* sec/item
* sec/branch
* GPU memory
* output bytes/item
* NFE/item

그 후:

```text
target shard walltime = 2~6 hours
```

정도로 shard size 결정.

가능하면 하나의 scientific shard가 8시간을 넘지 않게 한다.

deadline risk를 줄이는 것이 목적.

---

# 29. deterministic shard assignment

shard assignment는 outcome independent.

예:

```text
hash(run_fingerprint | item_id) % num_shards
```

혹은 contiguous deterministic partition.

보장:

* no duplicate
* no missing
* stable assignment
* rerun reproducible

assignment hash를 manifest에 저장.

---

# 30. shard-local atomic output

각 shard:

```text
outputs/v2r_reference/<run>/shards/shard-XXX/
```

에만 기록.

필수:

```text
shard_manifest.json
progress.json
DONE.json
artifact hashes
```

item 단위 atomic completion을 지원한다.

preemption 후 completed item을 재사용 가능하게 한다.

단 fingerprint mismatch면 stale artifact reuse 금지.

---

# 31. cross-server raw artifact 전략

shared disk가 있다고 가정하지 않는다.

raw trajectory/snapshot은 해당 server에 둔다.

중앙에는 compact artifact만 모은다.

raw artifact는:

```text
server
absolute path
size
sha256
mtime
execution sha
config sha
```

로 index한다.

필요한 merge input만 rsync/scp하고 반드시 SHA256 검증.

Git에는 대용량 raw artifact를 넣지 않는다.

---

# 32. Single-writer aggregation

worker/shard는 aggregate file에 직접 쓰지 않는다.

controller 하나만 merge한다.

merge 전에:

* all expected shards DONE
* matching execution SHA
* config SHA
* model revision
* dataset hash
* no duplicate item
* no missing item
* no unintended seed overlap
* row counts
* artifact hashes

전부 검증.

하나라도 실패하면:

```text
AGGREGATION_BLOCKED
```

---

# 33. execution worktree immutable

scientific job 실행 중인 worktree에서:

* checkout
* pull
* commit
* merge
* reset
* artifact commit

금지.

50924와 같은 mutable-HEAD provenance 문제를 반복하지 않는다.

start-time:

```text
execution_git_sha
```

를 freeze.

final report도 그 값을 사용.

종료 시 현재 `git rev-parse HEAD`를 scientific execution SHA로 다시 읽지 않는다.

필요하면:

```text
execution_git_sha
finalization_worktree_sha
```

를 별도로 기록.

---

# 34. New execution generation freeze

R0/R1/R2 implementation과 tests 완료 후:

새 exact execution commit을 만든다.

예:

```text
codex/v2r-reference-execution-20260923
```

R3 scientific jobs는 모두 이 exact SHA에서 실행.

scientific code 수정이 필요하면:

* 기존 generation은 그대로 보존
* new SHA
* new output namespace

로 간다.

---

# 35. Persistent orchestrator

Codex 대화가 끝나도 계속 동작해야 한다.

별도 tmux:

```text
iclr2027-reference-orchestrator
```

구성.

loop:

```text
inventory
→ job status
→ shard status
→ gate validation
→ eligible merge
→ eligible seal
→ dependent next-stage submission
→ compact status generation
→ git commit/push
→ sleep
```

30분 주기.

중요 event는 즉시 push.

---

# 36. Gate dependency

자동 다음 단계:

```text
R0 PASS
→ R1

R1 PASS
→ R2

R2 PASS
→ reference trajectory bank

trajectory bank complete
→ failed-pool deterministic freeze

failed-pool freeze
→ R3 shard submit

all R3 shards complete
→ merge

merge valid
→ seal

SEALED
→ paper artifact export
```

gate 실패 시 config를 자동 변경해서 결과를 맞추지 않는다.

```text
NEEDS_REVIEW
```

로 둔다.

다른 독립 run은 계속 진행 가능.

---

# 37. 기존 50668/50669 처리

계속 모니터링한다.

완료되면 기존 V2 evidence로 seal 시도.

그러나 reference-primary보다 우선하지 않는다.

새 resource planner에서:

```text
reference primary cannot finish by cutoff
AND
50668/50669 are occupying required GPUs
```

라고 판단하면:

```text
PREEMPTION_RECOMMENDED
```

를 보고한다.

자동 cancel은 하지 않는다.

---

# 38. 50924 forensic은 별도

50924 seed collision forensic은 계속 별도 처리한다.

새 reference experiment를 기다리게 하지 않는다.

V2R에서는 처음부터 corrected seed namespace 사용.

validator를 느슨하게 만들어 50924를 억지 seal하지 않는다.

---

# 39. Paper 구조도 reference-primary 중심으로 준비

현재 paper integration branch는 보존한다.

새 branch:

```text
codex/reference-primary-paper-20260923
```

를 만든다.

reference result가 SEALED되기 전에는 final numerical claim을 쓰지 않는다.

하지만 다음 구조 수정은 미리 가능하다.

## Experiment section

명시:

```text
Reference decoder
Measurement decoder
```

## Main baseline metric

reference:

```text
trajectory accuracy / pass@1
```

## Existing V2

```text
measurement-decoder pass@8
```

로 구분.

둘을 같은 baseline metric처럼 표현하지 않는다.

---

# 40. Main-paper evidence hierarchy

최종적으로 목표하는 hierarchy:

## Main

Reference-quality:

```text
LLaDA MATH
LLaDA GSM8K
Dream MATH
Dream GSM8K
```

## Main deep mechanism

Reference LLaDA:

```text
MATH
GSM8K
```

## Secondary / appendix

기존 measurement-decoder V2:

```text
BBH
MBPP
Dream
기존 LLaDA
```

단 새 결과가 실제로 이 hierarchy를 지지할 때만 사용한다.

---

# 41. 현재 paper의 RQ는 유지

RQ1:
failed reference-quality trajectory에 repairable state가 존재하는가?

RQ2:
recovery가 native continuation인지 intervention lift인지?

RQ3:
observable signal로 prospective localization 가능한가?

RQ4:
task/backbone에 걸쳐 유지되는가?

새 baseline reproduction은 별도 headline RQ가 아니다.

scientific validity prerequisite다.

---

# 42. Title gate

현재 title:

```text
When Does Diffusion Reasoning Become Irrecoverable?
Repairable States in Diffusion Language Models
```

은 reference LLaDA temporal evidence가 SEALED된 경우에만 유지 가능하도록 표시한다.

temporal evidence가 submission 전 충분하지 않으면 fallback:

```text
Repairable States in Diffusion Reasoning Trajectories
```

Astra가 자동으로 title을 바꾸지는 말고 readiness에서 flag만 한다.

---

# 43. Current PDF audit도 CPU-side로 즉시 해결

현재 paper branch는:

* source audit PASS
* LaTeX compile PASS
* post-build PDF audit FAIL

상태.

GPU와 무관하므로 원인을 즉시 분석하고 수정.

scientific result와 무관한:

* page limit
* unresolved refs
* anonymity
* PDF metadata
* parser/whitespace
* TODO marker

등을 병렬로 정리한다.

---

# 44. Deadline policy

현재 deadline이 매우 가깝다.

자동 priority:

## T-24h

* 새 P2 job 제출 금지
* P0/P1 완료 가능한 shard만 실행
* partial sealed evidence aggregation 시작
* paper figure/table integration 시작

## T-12h

* new scientific protocol/code modification 금지
* new long GPU job 제출 금지
* SEALED evidence만 manuscript에 사용
* final prose / build / audit / package 집중

## T-6h

* submitted scientific evidence freeze
* PDF / anonymity / source package / OpenReview upload readiness만 처리

active job 자동 kill 금지.

---

# 45. Monitoring outputs

새 branch에서 최소:

```text
status/v2r/current_status.json
status/v2r/cluster_inventory.json
status/v2r/resource_plan.json
status/v2r/reference_recipe_status.json
status/v2r/gate_status.json
status/v2r/shard_matrix.csv
status/v2r/artifact_index.json
status/v2r/aggregate_status.json
status/v2r/provenance_status.json
status/v2r/paper_readiness.json
status/v2r/attention_required.md
status/v2r/event_history.jsonl
status/v2r/progress_history.jsonl
status/v2r/orchestrator_health.json
```

유지.

---

# 46. attention_required.md

ChatGPT가 remote에서 이 파일 하나만 읽어도 되게 한다.

형식:

```text
Timestamp

NEW EVENTS

REFERENCE GATES
LLaDA R0:
LLaDA R1:
LLaDA R2:
Dream R0:
Dream R1:
Dream R2:

PRIMARY EVIDENCE
LLaDA MATH:
LLaDA GSM:
Dream MATH:
Dream GSM:

ACTIVE SHARDS

GPU / SERVER STATUS

FAILED/BLOCKED

NEW SEALED EVIDENCE

PAPER STATUS

DEADLINE STATUS

WHAT CHATGPT SHOULD READ NEXT
```

---

# 47. Paper-ready artifact

각 sealed reference run마다 compact bundle 생성:

```text
reference_recipe.json
run_manifest.json
scientific_provenance.json
base_report.json
existence.csv
temporal_summary.csv
mechanism_summary.csv
selector_summary.csv
decoder_regime_summary.json
SHA256SUMS
```

raw trajectories는 Git에 commit하지 않는다.

---

# 48. Final paper tables

최소 생성 가능하도록 준비:

### Table 1

Reference baseline + existence:

```text
Backbone
Task
Reference accuracy
# failed sampled trajectories
Native recoverable
Confirmed repairable
Never-correct repairable
T_last summary
```

### Table 2

Reference LLaDA mechanism:

```text
Matched continuation
Canonical repair
Random remask
CoRe
Fresh sampling
Recovery
Harm
NFE
```

### Table 3

Localization:

```text
Selector
Confirmed recovery
Prospective trajectory accuracy delta
Harm
Coverage
Oracle gap
NFE
```

### Appendix

Measurement-decoder vs reference-decoder comparison.

---

# 49. Scientific claim을 자동 결정하지 않는다

Astra는:

* implementation
* reproduction
* execution
* aggregation
* provenance
* raw factual result
* tables/figures
* build

까지 수행한다.

다음은 최종 author/ChatGPT 판단으로 남긴다.

* title
* strength of claim
* mechanism interpretation
* decoder-dependence interpretation
* generalization statement
* final Abstract/Conclusion wording

---

# 50. 첫 실행에서 해야 할 순서

Astra는 이 요청을 받자마자 다음 순서로 수행한다.

```text
1. server1~4 full inventory
2. existing jobs/worktrees protection map
3. official/reference recipe pinning
4. V2R design revision 작성 + commit
5. new metric schema
6. collision-free seed namespace
7. sharded worker/merge/seal/orchestrator 구현
8. CPU tests
9. GPU R0 smoke
10. R1 bridge smoke
11. R2 instrumentation equivalence
12. PASS한 backbone/task부터 reference base shards 제출
13. 동시에 persistent monitoring 시작
14. base 완료되는 즉시 failed pool freeze
15. R3 repairability shards 제출
16. temporal/mechanism controls를 priority대로 제출
17. completed shard 자동 merge/seal
18. paper-ready compact artifact 생성
19. paper build/audit 병렬 수행
```

대규모 R3를 1~8 gate보다 먼저 제출하지 않는다.

---

# 51. 첫 보고 형식

첫 구축과 smoke submission이 끝나면:

```text
Development branch:
Development commit:

Design revision:
Frozen before R3 results: YES/NO

Reference pins
LLaDA:
Dream:

Cluster
server1:
server2:
server3:
server4:

Protected jobs:
50668:
50669:
existing live monitor:

Safe GPUs:
Safe filesystems:

New metric schema:
Seed namespace:
Shard architecture:

CPU tests:
GPU tests:

R0
LLaDA:
Dream:

R1
LLaDA:
Dream:

R2
LLaDA:
Dream:

Submitted base shards:

Persistent orchestrator:
tmux:
PID:
status branch:
next cycle:

Paper branch:
PDF audit:

Current blockers:
```

---

# 52. 최종 성공 조건

성공은 job을 많이 돌린 것이 아니다.

다음을 만족해야 한다.

1. reference recipe가 source-level로 pin됨
2. source-native reproduction 상태가 명확함
3. bridge evaluator가 검증됨
4. instrumentation exact equivalence PASS
5. same reference-quality trajectory bank가 scientific base가 됨
6. failed trajectory subset이 outcome-independent rule로 freeze됨
7. 그 위에서 qC/qR/Delta/T_last 측정
8. localization/confirmation RNG가 collision-free
9. limited GPU에서 deterministic shard 분산
10. hash-verified single-writer aggregation
11. SEALED artifact만 paper에 사용
12. 기존 V2와 reference V2R을 혼동하지 않음
13. LLaDA deep anchor를 우선 완결
14. Dream으로 backbone validation
15. PDF build/audit/package까지 submission-ready
16. 모든 상태가 GitHub remote에서 ChatGPT가 검증 가능

최종 목표는:

```text
“낮거나 임의적인 decoder에서 repairability를 발견했다”
```

가 아니라,

```text
“먼저 정상 reference baseline을 재현했고,
그 동일 decoder의 동일 trajectory를 instrumentation했으며,
그 실패 trajectory들에서도 counterfactual repairability를 측정했다.”
```

라고 말할 수 있는 full-paper evidence chain을 만드는 것이다.

GPU가 부족하면 실험의 scientific depth를 우선하고 breadth를 줄인다.

즉 우선순위는:

```text
correct reference chain
> deep LLaDA anchors
> Dream validation
> extra breadth
> extra seeds/operators
```

이다.
