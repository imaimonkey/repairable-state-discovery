#!/usr/bin/env python3
"""Compact factual status; pending work never becomes evidence by file creation."""
from __future__ import annotations
import csv,datetime as dt,json,os,subprocess
from pathlib import Path
from v2r_inventory import atomic_json
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'status/v2r'
def read(path,default=None):
 try:return json.loads(Path(path).read_text())
 except (FileNotFoundError,json.JSONDecodeError):return default

def write_status(queue,health):
 now=dt.datetime.now(dt.timezone.utc);deadline=dt.datetime.fromisoformat('2026-09-26T20:59:00+09:00');hours=(deadline-now).total_seconds()/3600
 gates={}; artifacts=[]
 for task in queue.get('tasks',[]):
  task_output=task.get('output')
  report=read(Path(task_output)/task['stage']/'gate_report.json') if task_output else None
  key=task['backbone']+'_'+task['task'];report_path=str(Path(task_output)/task['stage']/'gate_report.json') if task_output else None
  gates.setdefault(key,{})[task['stage']]={'status':report['status'] if report else task.get('status','NOT_RUN'),'path':report_path,'job_id':task.get('job_id'),'error':report.get('error') if report else task.get('error')}
  if report:artifacts.append({'kind':'gate_report','server':task['server'],'path':gates[key][task['stage']]['path'],'execution_sha':task['execution_git_sha'],'status':report['status']})
 bundle_root=Path('/var/tmp/kimhj-v2r-reference/outputs/v2r_reference/bundles')
 sealed_runs=[]
 if bundle_root.is_dir():
  for marker in sorted(bundle_root.glob('*/SEALED.json')):
   doc=read(marker,{}) or {}
   if doc.get('status')=='SEALED': sealed_runs.append(marker.parent.name)
 primary={name:'NOT_STARTED' for name in ['llada_math500','llada_gsm8k','dream_math500','dream_gsm8k']}
 for run in sealed_runs:
  if run.startswith('llada_math500_base'): primary['llada_math500']='BASE_SEALED'
  elif run.startswith('llada_math500_core'): primary['llada_math500']='CORE_SEALED'
  elif run.startswith('llada_math500_temporal'): primary['llada_math500']='TEMPORAL_SEALED'
  elif run.startswith('llada_gsm8k_base'): primary['llada_gsm8k']='BASE_SEALED'
  elif run.startswith('llada_gsm8k_core'): primary['llada_gsm8k']='CORE_SEALED'
  elif run.startswith('llada_gsm8k_temporal'): primary['llada_gsm8k']='TEMPORAL_SEALED'
  elif run.startswith('dream_math500'): primary['dream_math500']='SEALED'
  elif run.startswith('dream_gsm8k'): primary['dream_gsm8k']='SEALED'
 r2_pass=all(gates.get(k,{}).get('R2',{}).get('status')=='PASS' for k in ['llada_math500','llada_gsm8k'])
 current={'timestamp':now.isoformat(),'goal_status':'IN_PROGRESS','protocol_generation':2,'priority':['llada_math500_deep','llada_gsm8k_replication','dream_math500_replication','dream_gsm8k_optional'],'legacy_jobs':{'50668':'CANCELLED_FOR_REFERENCE_PRIMARY_RESET','50669':'CANCELLED_FOR_REFERENCE_PRIMARY_RESET','49256':'CANCELLED_FOR_REFERENCE_PRIMARY_REALLOCATION','49257':'CANCELLED_FOR_REFERENCE_PRIMARY_REALLOCATION','52594':'CANCELLED_FOR_REFERENCE_PRIMARY_REALLOCATION','52595':'CANCELLED_FOR_REFERENCE_PRIMARY_REALLOCATION'},'reference_gates':gates,'primary_evidence':primary,'deadline':deadline.isoformat(),'hours_remaining':round(hours,3),'development_sha':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'final_scientific_execution_sha':'78fe5d7c1829b67d1bb1416b7205edfa647bb2fa' if r2_pass else None,'scientific_execution_freeze_status':'FROZEN_AFTER_LLADA_R2_PASS' if r2_pass else 'PENDING_R2_AND_COMPLETE_SCIENTIFIC_EXECUTORS','active_tasks':[t['id'] for t in queue.get('tasks',[]) if t.get('status') in ['RUNNING','SUBMITTED','PENDING']]}
 atomic_json(OUT/'current_status.json',current);atomic_json(OUT/'gate_status.json',gates);atomic_json(OUT/'artifact_index.json',{'timestamp':now.isoformat(),'artifacts':artifacts})
 atomic_json(OUT/'orchestrator_health.json',health)
 atomic_json(OUT/'reference_recipe_status.json',{b:{'source_status':'PINNED','reproduction_status':'NOT_YET_REPRODUCED','recipe_path':f'results/v2r_reference/reference_recipes/{b}.json'} for b in ['llada','dream']})
 aggregate_state='SEALED_REFERENCE_EVIDENCE_AVAILABLE' if sealed_runs else 'WAITING_FOR_SCIENTIFIC_SHARDS'
 atomic_json(OUT/'aggregate_status.json',{'status':aggregate_state,'sealed_reference_runs':sealed_runs})
 atomic_json(OUT/'provenance_status.json',{'design_freeze':read(OUT/'design_freeze.json'),'execution_worktrees_immutable':True,'gate_execution_generation':queue.get('execution_git_sha'),'final_scientific_execution_sha':'78fe5d7c1829b67d1bb1416b7205edfa647bb2fa' if r2_pass else None,'reference_seals':sealed_runs})
 paper_root=Path('/data/kimhj/repairable-state-discovery-reference-paper-20260923')
 core_sealed=any(x.startswith('llada_math500_core') for x in sealed_runs)
 temporal_sealed=any(x.startswith('llada_math500_temporal') for x in sealed_runs)
 blockers=[]
 if not core_sealed: blockers.append('No SEALED LLaDA MATH reference core evidence')
 if not temporal_sealed: blockers.append('No SEALED LLaDA MATH temporal evidence')
 blockers.append('Author abstract/conclusion review pending')
 paper_status='REFERENCE_EVIDENCE_SEALED_AUTHOR_REVIEW_PENDING' if core_sealed and temporal_sealed else 'NOT_SUBMISSION_READY'
 paper={'status':paper_status,'branch':'codex/reference-primary-paper-20260923','technical_pdf_audit':read(paper_root/'status/v2r/pdf_audit.json',{'status':'NOT_YET_VERIFIED'}),'scientific_blockers':blockers,'title_timing_claim_allowed':False,'dream_completion_required_for_llada_seal':False,'sealed_reference_runs':sealed_runs}
 atomic_json(OUT/'paper_readiness.json',paper)
 plan={'timestamp':now.isoformat(),'deadline_hours':hours,'raw_output_filesystem':'server3:/var/tmp/kimhj-v2r-reference','storage_critical_threshold':.95,'shard_target_hours':[2,4],'max_planned_hours':6,'llada_core_target':64,'llada_core_minimum':32,'temporal_target':32,'mechanism_target':32,'dream_target':32,'budget_freeze':'PENDING_MEASURED_BRANCH_TIMING','preemption':'AUTHORIZED_LEGACY_RESET_COMPLETED','automatic_job_cancellation':False}
 atomic_json(OUT/'resource_plan.json',plan)
 with (OUT/'shard_matrix.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=['id','backbone','task','stage','priority','status','job_id','execution_git_sha']);w.writeheader()
  for t in queue.get('tasks',[]):w.writerow({k:t.get(k) for k in w.fieldnames})
 lines=[now.isoformat(),'','NEW EVENTS','50668/50669 archived and cancelled by explicit reset authorization. Legacy artifacts preserved.','','REFERENCE GATES']
 for b in ['llada','dream']:
  for g in ['R0','R1','R2']:lines.append(f'{b} {g}: '+str({task:values.get(g,{}).get('status','NOT_RUN') for task,values in gates.items() if task.startswith(b)}))
 lines+=['','PRIMARY EVIDENCE']+[k+': '+v for k,v in primary.items()]+['','ACTIVE SHARDS']+[t['id']+': '+t.get('status','NOT_RUN')+' job='+str(t.get('job_id')) for t in queue.get('tasks',[])]+['','GPU / SERVER STATUS','See cluster_inventory.json; server3 root filesystem selected; critical /data rejected.','','FAILED/BLOCKED','Final scientific execution SHA/base/R3/temporal workers and measured resource budget still pending validation.','Parallel development agents stopped by usage limit; partial code is retained and checked locally.','','NEW SEALED EVIDENCE','None.','','PAPER STATUS',paper['status'],'','DEADLINE STATUS',f'{hours:.2f}h remaining; T-24 strongest completed evidence import; Dream cannot delay LLaDA.','','WHAT CHATGPT SHOULD READ NEXT','current_status.json, gate_status.json, legacy_reset/reset_state.json, docs/V2R_REFERENCE_PRIMARY_PROTOCOL.md']
 # The read-only unified monitor owns the human-readable attention file.  Keep
 # this render in memory for callers, but do not race the observer by writing it
 # from the execution authority.
 with (OUT/'progress_history.jsonl').open('a') as f:f.write(json.dumps({'timestamp':now.isoformat(),'active_tasks':current['active_tasks'],'hours_remaining':hours})+'\n')
 return current
