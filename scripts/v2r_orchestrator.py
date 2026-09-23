#!/usr/bin/env python3
"""Single controller for prepared gates; never modifies a scientific worktree."""
from __future__ import annotations
import argparse,datetime as dt,fcntl,json,os,subprocess,sys,time,traceback
from pathlib import Path
from v2r_inventory import atomic_json,collect
from v2r_submit import submit,command,environment,DEADLINE
from v2r_status import write_status,read
from v2r_science_controller import ensure_base_tasks,ensure_deep_tasks,submit_science,finalize_base
from v2r_reduce import reduce_stage
from repairable_diffusion.src.v2r.artifacts import read_json,validate_shard
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'status/v2r';RUNTIME=Path('/var/tmp/kimhj-v2r-reference/runtime')

def sync_remote_shard(task):
    """Pull a completed remote shard into the authoritative local run tree.

    Remote execution is admitted only for tasks whose deployment and provenance
    were recorded by the relocation controller.  The scientific worker still
    runs at the immutable execution SHA; this copy step only makes its sealed
    shard visible to the local reducer.
    """
    if not task.get('remote_execution'):
        return
    host=str(task.get('remote_host') or '')
    if not host:
        raise RuntimeError('REMOTE_TASK_MISSING_HOST')
    shard=f"shard-{int(task['shard']):03d}"
    local=Path(task['run_dir'])/'shards'/shard
    local.mkdir(parents=True,exist_ok=True)
    remote=f"{host}:{task['run_dir']}/shards/{shard}/"
    r=subprocess.run(['rsync','-a',remote,str(local)+'/'],text=True,capture_output=True,timeout=120)
    if r.returncode:
        raise RuntimeError('REMOTE_SHARD_SYNC_FAILED: '+(r.stderr[-1000:] or r.stdout[-1000:]))

def event(name,payload):
 with (OUT/'event_history.jsonl').open('a') as f:f.write(json.dumps({'timestamp':dt.datetime.now(dt.timezone.utc).isoformat(),'event':name,**payload},sort_keys=True)+'\n')

def publish():
 subprocess.run(['git','add','status/v2r'],cwd=ROOT,check=True)
 subprocess.run(['git','add','-f','status/v2r/event_history.jsonl','status/v2r/progress_history.jsonl'],cwd=ROOT,check=True)
 if subprocess.run(['git','diff','--cached','--quiet'],cwd=ROOT).returncode:
  subprocess.run(['git','commit','-m','Update reference-primary gate and resource status'],cwd=ROOT,check=True,capture_output=True)
 return subprocess.run(['git','push','origin','codex/iclr2027-reference-live-20260923'],cwd=ROOT,text=True,capture_output=True,timeout=45).returncode

def integrate_paper():
 paper=Path('/data/kimhj/repairable-state-discovery-reference-paper-20260923')
 script=paper/'scripts/import_v2r_reference.py'
 if not script.is_file(): return {'status':'MISSING_IMPORTER'}
 r=subprocess.run([sys.executable,str(script)],cwd=paper,text=True,capture_output=True,timeout=60)
 if r.returncode:return {'status':'IMPORT_FAILED','stderr':r.stderr[-2000:]}
 subprocess.run(['git','add','paper/generated','paper/reference_generated/tables','status/v2r/reference_import.json'],cwd=paper,check=True)
 if subprocess.run(['git','diff','--cached','--quiet'],cwd=paper).returncode==0:return {'status':'NO_CHANGE'}
 subprocess.run(['git','commit','-m','Import sealed reference evidence'],cwd=paper,check=True,capture_output=True)
 push=subprocess.run(['git','push','origin','codex/reference-primary-paper-20260923'],cwd=paper,text=True,capture_output=True,timeout=45)
 return {'status':'IMPORTED','push_returncode':push.returncode}

def cycle():
 queue=read(OUT/'orchestrator_queue.json',{'tasks':[]});changed=False
 inventory=read(OUT/'cluster_inventory.json',{})
 if not inventory or time.time()-dt.datetime.fromisoformat(inventory['timestamp']).timestamp()>1800:inventory=collect(OUT)
 byid={t['id']:t for t in queue['tasks']}
 for task in sorted(queue['tasks'],key=lambda t:t['priority']):
  old=task.get('status','READY')
  if task.get('kind')=='science_shard':
   # Preserve the hard critical path: a pending GSM replication shard must not
   # consume the next Slurm slot before LLaDA MATH core and temporal evidence.
   # Running shards are never migrated or cancelled; this gate applies after a
   # pending shard has been explicitly relocated with a durable lineage record.
   if (task.get('task')=='gsm8k' and task.get('stage')=='base' and int(task.get('shard',0))>0
       and not task.get('job_id')):
    math_deep=[x for x in queue['tasks'] if x.get('kind')=='science_shard'
               and x.get('task')=='math500' and x.get('stage') in {'r3_core','temporal'}]
    if not math_deep or not all(x.get('status')=='SEALED' for x in math_deep):
     task['status']='WAITING_PRIORITY'
     if task['status']!=old: changed=True; event('TASK_STATE_CHANGE',{'task':task['id'],'old':old,'new':task['status'],'job_id':task.get('job_id'),'error':'Held for LLaDA MATH deep critical path'})
     continue
   deps=[byid[k]['status'] for k in task.get('depends_on',[])]
   if task.get('job_id'):
    s=subprocess.run(['sacct','-n','-X','-P','-j',task['job_id'],'--format=JobID,State,ExitCode'],text=True,capture_output=True,timeout=15)
    state=next((l.split('|')[1] for l in s.stdout.splitlines() if l.split('|')[0]==task['job_id']),'UNKNOWN');task['slurm_state']=state
    if state in ['RUNNING','PENDING','CONFIGURING','COMPLETING']:task['status']=state
    elif state=='COMPLETED':
     try:
      sync_remote_shard(task)
      manifest=read_json(task['manifest']);gates=read_json(task['gates']);validate_shard(Path(task['run_dir'])/'shards'/f"shard-{int(task['shard']):03d}",manifest,int(task['shard']),gates=gates);task['status']='SEALED' if Path(task['run_dir'],'SEAL_RECORD.json').exists() else 'DONE';task['error']=None
     except Exception as exc:task.update(status='NEEDS_REVIEW',error=str(exc))
    elif state!='UNKNOWN':task.update(status='NEEDS_REVIEW',error='Terminal scientific Slurm state: '+state)
   elif all(s in {'PASS','SEALED'} for s in deps):
    inventory=collect(OUT)
    try:task.update(submit_science(task,inventory));task['status']='SUBMITTED'
    except RuntimeError as e:task.update(status='RESOURCE_WAIT',error=str(e))
   else:task['status']='WAITING_DEPENDENCY'
   if task['status']!=old:changed=True;event('TASK_STATE_CHANGE',{'task':task['id'],'old':old,'new':task['status'],'job_id':task.get('job_id'),'error':task.get('error')})
   continue
  report=read(Path(task['output'])/task['stage']/'gate_report.json')
  if report and report.get('status') in ['PASS','NEEDS_REVIEW']:
   task['status']=report['status'];task['error']=report.get('error')
  elif task.get('job_id'):
   s=subprocess.run(['sacct','-n','-X','-P','-j',task['job_id'],'--format=JobID,State,ExitCode'],text=True,capture_output=True,timeout=15)
   state=next((l.split('|')[1] for l in s.stdout.splitlines() if l.split('|')[0]==task['job_id']),'UNKNOWN')
   task['slurm_state']=state
   if state in ['RUNNING','PENDING','CONFIGURING']:task['status']=state
   elif state!='UNKNOWN':task.update(status='NEEDS_REVIEW',error='Terminal Slurm state without PASS: '+state)
  elif task.get('status') in ['READY','RESOURCE_WAIT','WAITING_DEPENDENCY']:
   dependencies=[byid[k]['status'] for k in task.get('depends_on',[])]
   if all(s=='PASS' for s in dependencies):
    if dt.datetime.now(dt.timezone.utc)>=DEADLINE-dt.timedelta(hours=12):task['status']='DEADLINE_BLOCKED'
    elif task['stage']=='R1':
     # R1 is CPU-only, run in its immutable execution tree and preserve log.
     env=os.environ.copy();env.update(environment());log=Path(task['output'])/'R1'/'cpu.log'
     with log.open('a') as f:r=subprocess.run(command(task),cwd=task['execution_worktree'],env=env,stdout=f,stderr=f,timeout=240)
     task['status']='PASS' if r.returncode==0 else 'NEEDS_REVIEW'
    else:
     inventory=collect(OUT)
     try:task.update(submit(task,inventory));task['status']='SUBMITTED'
     except RuntimeError as e:task.update(status='RESOURCE_WAIT',error=str(e))
   else:task['status']='WAITING_DEPENDENCY'
  if task['status']!=old:changed=True;event('TASK_STATE_CHANGE',{'task':task['id'],'old':old,'new':task['status'],'job_id':task.get('job_id'),'error':task.get('error')})
 # Unlock one-trajectory base banks as soon as matching R2 is sealed.
 if ensure_base_tasks(queue):
  changed=True;event('SCIENCE_QUEUE_UNLOCKED',{'stage':'base','execution_sha':queue.get('execution_git_sha')})
 # Merge and seal complete scientific stages with strict provenance; never infer missing items.
 groups={}
 for task in queue.get('tasks',[]):
  if task.get('kind')=='science_shard':groups.setdefault(task['run_dir'],[]).append(task)
 for run_dir,tasks in groups.items():
  if not tasks or not all(t.get('status') in {'DONE','MERGED','SEALED'} for t in tasks):continue
  try:
   # Crash-safe recovery: a prior cycle may have published the aggregate and
   # seal record before queue persistence. Those immutable markers are enough
   # to restore the durable task state without rerunning or mutating evidence.
   if Path(run_dir,'SEAL_RECORD.json').exists():
    for task in tasks: task['status']='SEALED'; task['error']=None
    changed=True
   if not Path(run_dir,'aggregate','MERGED.json').exists():
    aggregate=finalize_base(tasks); event('SCIENCE_STAGE_MERGED',{'run_dir':run_dir,'stage':tasks[0]['stage'],'item_count':aggregate['item_count']})
    for task in tasks:task['status']='MERGED'
    changed=True
   if all(t.get('status')=='MERGED' for t in tasks) and not Path(run_dir,'SEAL_RECORD.json').exists():
    bundle=Path('/var/tmp/kimhj-v2r-reference/outputs/v2r_reference/bundles')/Path(run_dir).name
    record=reduce_stage(tasks[0]['manifest'],run_dir,tasks[0]['gates'],bundle)
    atomic_json(Path(run_dir)/'SEAL_RECORD.json',record)
    for task in tasks:task['status']='SEALED'
    changed=True;event('SCIENCE_STAGE_SEALED',{'run_dir':run_dir,'stage':tasks[0]['stage'],'bundle':str(bundle)})
  except Exception as exc:
   for task in tasks:task['error']='MERGE_OR_SEAL_BLOCKED: '+str(exc)
   event('SCIENCE_MERGE_OR_SEAL_BLOCKED',{'run_dir':run_dir,'stage':tasks[0].get('stage'),'error':str(exc)})
  if all(t.get('status')=='SEALED' for t in tasks) and any(not t.get('paper_imported') for t in tasks):
   result=integrate_paper(); event('PAPER_REFERENCE_IMPORT',{'run_dir':run_dir,'result':result})
   if result.get('status') in {'IMPORTED','NO_CHANGE'}:
    for task in tasks:task['paper_imported']=True
    changed=True
 if ensure_deep_tasks(queue):
  changed=True;event('SCIENCE_QUEUE_UNLOCKED',{'stage':'r3_core_temporal','execution_sha':queue.get('execution_git_sha')})
 atomic_json(OUT/'orchestrator_queue.json',queue)
 now=dt.datetime.now(dt.timezone.utc);health={'timestamp':now.isoformat(),'pid':os.getpid(),'tmux':'iclr2027-reference-orchestrator','status':'RUNNING','inventory_cycle_seconds':1800,'event_poll_seconds':60,'next_poll':(now+dt.timedelta(seconds=60)).isoformat(),'last_error':None}
 write_status(queue,health)
 return changed

def main():
 p=argparse.ArgumentParser();p.add_argument('--once',action='store_true');a=p.parse_args();RUNTIME.mkdir(parents=True,exist_ok=True)
 with (RUNTIME/'orchestrator.lock').open('a') as lock:
  fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB);last_publish=0
  while True:
   try:
    changed=cycle()
    if changed or time.time()-last_publish>=1800:
     code=publish();last_publish=time.time()
     if code:event('PUSH_FAILED',{'returncode':code})
   except Exception as e:
    event('CONTROLLER_ERROR',{'error':str(e),'traceback':traceback.format_exc()})
    atomic_json(OUT/'orchestrator_health.json',{'status':'DEGRADED_RETRY','pid':os.getpid(),'error':str(e),'timestamp':dt.datetime.now(dt.timezone.utc).isoformat()})
   if a.once or dt.datetime.now(dt.timezone.utc)>DEADLINE+dt.timedelta(hours=1):break
   time.sleep(60)
if __name__=='__main__':main()
