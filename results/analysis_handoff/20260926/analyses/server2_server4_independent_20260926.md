# Server 2·4 독립 실험 분석 보고서

## Material Passport

- **Origin Skill:** academic-research-suite / experiment-agent
- **Origin Mode:** validate / statistical interpretation
- **Analysis date:** 2026-09-26 (KST)
- **Verification status:** `ANALYZED` — artifact integrity and declared gates verified; full rerun not performed
- **Scientific lineage:** frozen execution repository `/data/kimhj/repairable-state-discovery-v2-exec-20260925`, commit `78fe5d7c1829b67d1bb1416b7205edfa647bb2fa`
- **Role of these runs:** Server 2·4 independent paper-supporting lanes. They are not Server 3 exact-reply evidence and must not be silently pooled with it.

## 1. Scope and source artifacts

분석 대상은 서버 2의 완료 run 4개와 서버 4의 완료 run 6개, 총 10개이다. 원격 산출물은 다음의 읽기 전용 경로에서 확인했다.

- Server 2: `/var/tmp/kimhj-v2r-independent/server2/outputs/v2r_reference/`
- Server 4: `/var/tmp/kimhj-v2r-independent/server4/outputs/v2r_reference/`

모든 대상 run에서 다음이 확인되었다.

- `aggregate/MERGED.json` 상태: `MERGED_VALID`
- `aggregate.json`, `gate_reports.json`, `run_manifest.json`의 해시가 `MERGED.json`에 기록된 artifact hash와 일치
- manifest item 수와 실제 item 수 일치
- 모든 shard의 `DONE.json` count가 선언된 기대치와 일치
- R0, R1, R2 gate 모두 `PASS`

따라서 아래 해석은 “완료 파일이 있는가” 수준을 넘어, 선언된 산출물 결합·무결성·게이트 조건을 통과한 결과에 대한 해석이다. 다만 동일 조건의 새 full rerun으로 재현성을 확인한 것은 아니므로 `REPRODUCIBLE`로 표시하지 않는다.

## 2. 기본 성능 결과

| 서버 | 데이터셋 | n | Correct | Incorrect | Accuracy | mean sec | p95 sec | NFE |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | GSM8K base | 1319 | 1063 | 256 | 80.591% | 95.761 | 100.091 | 256 |
| 4 | GSM8K base | 1319 | 1062 | 257 | 80.516% | 27.429 | 28.237 | 256 |
| 2 | MATH500 base | 500 | 202 | 298 | 40.400% | 66.051 | 82.616 | 512 |
| 4 | MATH500 base | 500 | 193 | 307 | 38.600% | 25.600 | 26.596 | 512 |

### Paired base comparison

동일 item ID를 맞춘 paired 비교 결과는 다음과 같다.

| 데이터셋 | 양쪽 정답 | 서버2만 정답 | 서버4만 정답 | 양쪽 오답 | discordant | 정확도 차이(서버2−서버4) |
|---|---:|---:|---:|---:|---:|---:|
| GSM8K | 1026 | 37 | 36 | 220 | 73 | +0.0768%p |
| MATH500 | 174 | 28 | 19 | 279 | 47 | +1.8000%p |

정확도 차이는 기술통계상 서버 2가 GSM8K에서 1개, MATH500에서 9개 더 맞힌 것이다. exact McNemar 검정의 양측 p-value는 GSM8K 약 `1.000`, MATH500 약 `0.243`이다. 따라서 이 결과만으로 서버 2/4의 하드웨어나 노드 차이가 원인이라고 주장할 수 없다. 특히 실행은 독립 lane이고 runtime/cache 경로도 달랐으므로, 논문에는 “independent lane descriptive comparison”으로 보고하고 causal hardware attribution은 하지 않는다.

## 3. Repairability 결과

`confirmed_repairable`은 사전 정의된 confirmation checkpoint 중 하나에서 `q_R >= 0.25`인 경우이며, `native_recoverable`은 `q_C >= 0.25`인 경우이다. `never_correct_repairable`은 관측 grid에서 correct 상태가 없었지만 intervention으로 확인된 경우이므로, `confirmed_repairable`과 동시에 참일 수 있다.

| 서버 | 데이터셋 / stage | n | confirmed repairable | rate | native recoverable | never-correct repairable | T_last_R present |
|---|---|---:|---:|---:|---:|---:|---:|
| 2 | MATH500 / r3_core | 35 | 2 | 5.714% | 0 | 1 | 0 |
| 4 | MATH500 / r3_core | 64 | 3 | 4.688% | 0 | 2 | 0 |
| 4 | GSM8K / r3_core | 64 | 5 | 7.812% | 0 | 5 | 0 |
| 4 | GSM8K / temporal | 32 | 3 | 9.375% | 0 | 3 | 3 |
| 2 | MATH500 / temporal | 32 | 0 | 0.000% | 0 | 0 | 0 |
| 4 | MATH500 / temporal | 32 | 0 | 0.000% | 0 | 0 | 0 |

### 세부 관찰

- Server 2 MATH500 core: item `173`은 early checkpoint (`0.123046875`)에서, item `461`은 mid checkpoint (`0.498046875`)에서 `q_R=1`, `q_C=0`, `Delta_R=1`로 확인되었다. 이 중 item `461`은 never-correct에도 해당한다.
- Server 4 MATH500 core: item `173`은 `0.123046875`, item `289`는 `0.123046875`, item `340`은 `0.373046875`에서 같은 형태의 repair signal을 보였다. item `289`, `340`은 never-correct에 해당한다.
- Server 4 GSM8K core: 11개 shard, 64개 item 모두 `DONE`이고 `MERGED_VALID`이다. item `1141`, `587`, `898`은 `0.12109375`, item `822`, `347`은 `0.24609375`에서 `q_R=1`, `q_C=0`, `Delta_R=1`로 확인되었고 5개 모두 never-correct였다. `T_last_R`는 core stage에서 산출하지 않는다.
- Server 4 GSM8K temporal: item `1011`은 `T_last_R=0.87109375`, item `1159`는 `0.49609375`, item `201`은 `0.62109375`에서 repair가 확인되었고 모두 never-correct였다.
- 두 MATH500 temporal run은 각 32 item, 7 checkpoint의 224 confirmation row에서 repairability가 0이었다. 이는 해당 사전 정의 subset에서의 음성 결과이지, 전체 현상 부재를 뜻하지 않는다.
- 모든 core/temporal lane에서 관측된 `q_C`는 0이었다. 즉 이 완료 산출물에서는 native continuation recoverability가 검출되지 않았고, 관측된 양성은 canonical repair intervention 쪽에만 있었다.

## 4. Scientific interpretation

이 결과는 다음처럼 정리하는 것이 안전하다.

1. 서버 2·4 결과는 모두 무결성·게이트 조건을 만족한 독립 실험이다. 분석 대상으로 사용할 수 있으며, 단순히 “실험 실패”로 폐기할 근거는 없다.
2. 기본 GSM8K 성능은 서버 간 사실상 동일한 수준이다. MATH500은 서버 2가 1.8%p 높지만 paired 검정에서 유의한 차이로 확인되지 않았다. 서버/하드웨어 원인으로 해석하지 않는다.
3. repairability는 서버 4 GSM8K core/temporal과 양쪽 MATH500 core에서 관찰되었다. 따라서 “서버 2 또는 4에서 full-paper에 사용할 과학적 신호가 없다”는 결론은 부정확하다.
4. 서버 2와 서버 4의 MATH500 core 표본 크기와 shard 구성은 각각 35와 64이므로, 두 rate를 직접적인 replication effect size처럼 비교하지 않는다. 서버별 독립 결과로 병렬 제시하고, 필요하면 사전에 정한 통합 분석 계획을 별도로 만든다.
5. Server 3 exact reply와의 정합성은 별도 축이다. 서버 2·4의 결과가 Server 3의 exact reply와 다르더라도, frozen lineage와 gate를 만족한 독립 paper lane이라는 사실은 유지된다. 반대로 서버 2·4 결과를 Server 3 exact reply의 재현으로 표현해서도 안 된다.

## 5. 재현성 및 실행환경 한계

- 공통 binding: execution/config/dataset/design/model/recipe SHA가 동일하다.
- 독립성: run fingerprint와 bank hash가 서로 다르며, Server 2는 주로 `/home/kimhj/.cache/huggingface/hub`, Server 4는 `/var/tmp/kimhj-v2r-reference/model-cache`를 runtime cache로 사용했다.
- recipe에는 deterministic temperature 0과 qC degenerate 조건이 기록되어 있지만, 이번 분석에서는 full rerun을 수행하지 않았다.
- 따라서 현재 상태는 **artifact-integrity verified + declared gates passed + full rerun not performed**이다. 논문 표기에서는 `reproducibility: CANNOT_VERIFY` 또는 이에 준하는 문구가 적절하다.
- R0/R1/R2가 PASS라는 사실은 이 reference task의 선언된 검증 조건을 통과했다는 뜻이며, 모든 공식 benchmark를 다시 실행했다는 뜻은 아니다. gate report의 `full_official_benchmark_reproduction: NOT_RUN_NOT_REQUIRED_FOR_NONIDENTICAL_PAPER_TASK`를 공개한다.

## 6. Fallacy scan (11/11)

| 점검 항목 | 판정 | 해석상 조치 |
|---|---|---|
| Simpson's paradox | N/A | 서버·데이터셋 층을 분리해 보고하며 숨은 그룹 통합을 하지 않음 |
| Ecological fallacy | N/A | item-level 결과를 group-level 원인으로 일반화하지 않음 |
| Berkson's paradox | NOTE | 고정 benchmark와 사전 정의 subset의 선택 구조를 명시 |
| Collider bias | N/A | outcome 기반 covariate adjustment 없음 |
| Base-rate fallacy | N/A | 진단검사 PPV/NPV 주장이 아님 |
| Regression to the mean | N/A | pre/post 선택 효과를 추정하는 설계가 아님 |
| Survivorship bias | NOTE | 계획된 item/shard가 모두 결합되었는지와 dropout 부재를 확인했으나, 관측 grid 밖 상태를 주장하지 않음 |
| Look-elsewhere effect | CAUTION | 다중 checkpoint를 전체 grid로 보고하며 유리한 한 셀만 선택하지 않음 |
| Garden of forking paths | CAUTION | frozen config/design/seed/hash binding으로 자유도를 줄였지만 full rerun 전에는 완전 제거로 표현하지 않음 |
| Correlation ≠ causation | CAUTION | 서버 간 accuracy 차이를 하드웨어 인과로 말하지 않음 |
| Reverse causality | N/A | 방향성 인과모형이 아님 |

## 7. 논문 반영 권고

본문에서는 서버 2·4를 다음 역할로 사용한다.

- base benchmark: 서버별 accuracy와 paired discordance를 기술통계로 보고
- repairability: 서버별 `n`, confirmed rate, native rate, never-correct rate, checkpoint 위치를 함께 보고
- independent validation: “same frozen lineage, independently executed on Server 2 and Server 4”로 표현하고 GSM8K core도 별도 lane으로 포함
- limitation: runtime/cache 차이, full rerun 미수행, core 표본 크기 차이, Server 3 exact reply와의 분리 명시

권장 문장:

> Under the frozen V2R reference lineage, the independent Server 2 and Server 4 lanes passed all declared artifact and gate checks. Repair signals were observed in the Server 4 GSM8K core and temporal lanes and in both MATH500 core lanes, while neither MATH500 temporal lane yielded a confirmed repairable item. The lanes are reported as independent supporting evidence; the present artifacts do not establish a hardware-causal difference or full rerun reproducibility.

이 보고서 기준으로 서버 2·4 완료 실험은 **분석 완료 상태**이며, 논문에 반영 가능한 evidence로 분류한다. 다만 “완전 재현 완료” 또는 “서버 차이의 원인 규명 완료”로 분류하지 않는다.
