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
 primary={name:'NOT_STARTED' for name in ['llada_math500','llada_gsm8k','dream_math500','dream_gsm8k']}
 current={'timestamp':now.isoformat(),'goal_status':'IN_PROGRESS','protocol_generation':2,'priority':['llada_math500_deep','llada_gsm8k_replication','dream_math500_replication','dream_gsm8k_optional'],'legacy_jobs':{'50668':'CANCELLED_FOR_REFERENCE_PRIMARY_RESET','50669':'CANCELLED_FOR_REFERENCE_PRIMARY_RESET'},'reference_gates':gates,'primary_evidence':primary,'deadline':deadline.isoformat(),'hours_remaining':round(hours,3),'development_sha':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'final_scientific_execution_sha':None,'scientific_execution_freeze_status':'PENDING_R2_AND_COMPLETE_SCIENTIFIC_EXECUTORS','active_tasks':[t['id'] for t in queue.get('tasks',[]) if t.get('status') in ['RUNNING','SUBMITTED','PENDING']]}
 atomic_json(OUT/'current_status.json',current);atomic_json(OUT/'gate_status.json',gates);atomic_json(OUT/'artifact_index.json',{'timestamp':now.isoformat(),'artifacts':artifacts})
 atomic_json(OUT/'orchestrator_health.json',health)
 atomic_json(OUT/'reference_recipe_status.json',{b:{'source_status':'PINNED','reproduction_status':'NOT_YET_REPRODUCED','recipe_path':f'results/v2r_reference/reference_recipes/{b}.json'} for b in ['llada','dream']})
 atomic_json(OUT/'aggregate_status.json',{'status':'WAITING_FOR_SCIENTIFIC_SHARDS','sealed_reference_runs':[]})
 atomic_json(OUT/'provenance_status.json',{'design_freeze':read(OUT/'design_freeze.json'),'execution_worktrees_immutable':True,'gate_execution_generation':queue.get('execution_git_sha'),'final_scientific_execution_sha':None,'reference_seals':[]})
 paper_root=Path('/data/kimhj/repairable-state-discovery-reference-paper-20260923')
 paper={'status':'NOT_SUBMISSION_READY','branch':'codex/reference-primary-paper-20260923','technical_pdf_audit':read(paper_root/'status/v2r/pdf_audit.json',{'status':'NOT_YET_VERIFIED'}),'scientific_blockers':['No SEALED LLaDA MATH reference core and temporal evidence','Author abstract/conclusion review pending'],'title_timing_claim_allowed':False,'dream_completion_required_for_llada_seal':False}
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
