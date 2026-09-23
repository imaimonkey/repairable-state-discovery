#!/usr/bin/env python3
"""Single controller for prepared gates; never modifies a scientific worktree."""
from __future__ import annotations
import argparse,datetime as dt,fcntl,json,os,subprocess,time,traceback
from pathlib import Path
from v2r_inventory import atomic_json,collect
from v2r_submit import submit,command,environment,DEADLINE
from v2r_status import write_status,read
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'status/v2r';RUNTIME=Path('/var/tmp/kimhj-v2r-reference/runtime')

def event(name,payload):
 with (OUT/'event_history.jsonl').open('a') as f:f.write(json.dumps({'timestamp':dt.datetime.now(dt.timezone.utc).isoformat(),'event':name,**payload},sort_keys=True)+'\n')

def publish():
 subprocess.run(['git','add','status/v2r'],cwd=ROOT,check=True)
 subprocess.run(['git','add','-f','status/v2r/event_history.jsonl','status/v2r/progress_history.jsonl'],cwd=ROOT,check=True)
 if subprocess.run(['git','diff','--cached','--quiet'],cwd=ROOT).returncode:
  subprocess.run(['git','commit','-m','Update reference-primary gate and resource status'],cwd=ROOT,check=True,capture_output=True)
 return subprocess.run(['git','push','origin','codex/iclr2027-reference-live-20260923'],cwd=ROOT,text=True,capture_output=True,timeout=45).returncode

def cycle():
 queue=read(OUT/'orchestrator_queue.json',{'tasks':[]});changed=False
 inventory=read(OUT/'cluster_inventory.json',{})
 if not inventory or time.time()-dt.datetime.fromisoformat(inventory['timestamp']).timestamp()>1800:inventory=collect(OUT)
 byid={t['id']:t for t in queue['tasks']}
 for task in sorted(queue['tasks'],key=lambda t:t['priority']):
  old=task.get('status','READY');report=read(Path(task['output'])/task['stage']/'gate_report.json')
  if report and report.get('status') in ['PASS','NEEDS_REVIEW']:
   task['status']=report['status'];task['error']=report.get('error')
  elif task.get('job_id'):
   s=subprocess.run(['sacct','-n','-X','-P','-j',task['job_id'],'--format=JobID,State,ExitCode'],text=True,capture_output=True,timeout=15)
   state=next((l.split('|')[1] for l in s.stdout.splitlines() if l.split('|')[0]==task['job_id']),'UNKNOWN')
   task['slurm_state']=state
   if state in ['RUNNING','PENDING','CONFIGURING']:task['status']=state
   elif state!='UNKNOWN':task.update(status='NEEDS_REVIEW',error='Terminal Slurm state without PASS: '+state)
  elif task.get('status') not in ['PASS','NEEDS_REVIEW']:
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
