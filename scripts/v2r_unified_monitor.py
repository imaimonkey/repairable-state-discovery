#!/usr/bin/env python3
"""Read-only reconciliation monitor for Slurm, V2R, legacy state, and paper readiness.

This process never submits or cancels jobs.  The reference orchestrator is the
single execution authority; this monitor only observes and writes durable
status for recovery after either process restarts.
"""
from __future__ import annotations
import argparse, datetime as dt, hashlib, json, os, subprocess, time
from pathlib import Path

from v2r_inventory import atomic_json, collect

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'status/v2r'
LEGACY=Path('/data/kimhj/repairable-state-discovery-live-monitor-20260923')
DEADLINE=dt.datetime.fromisoformat('2026-09-26T20:59:00+09:00')

def read(path, default=None):
    try: return json.loads(Path(path).read_text())
    except (FileNotFoundError, json.JSONDecodeError, OSError): return default

def command(args):
    try:
        p=subprocess.run(args,text=True,capture_output=True,timeout=20)
        return {'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
    except Exception as e: return {'returncode':-1,'stdout':'','stderr':str(e)}

def legacy_snapshot():
    panes=command(['tmux','list-panes','-t','iclr2027-live-monitor','-F','#{session_name}|#{pane_pid}|#{pane_current_command}'])
    return {
        'session':'iclr2027-live-monitor',
        'tmux':panes,
        'branch':command(['git','-C',str(LEGACY),'branch','--show-current']),
        'head':command(['git','-C',str(LEGACY),'rev-parse','HEAD']),
        'worktree':str(LEGACY),
        'status_files':sorted(str(p.relative_to(LEGACY)) for p in (LEGACY/'status').rglob('*') if p.is_file())[:500],
    }

def reconcile():
    now=dt.datetime.now(dt.timezone.utc)
    inventory=collect(OUT)
    jobs=read(OUT/'job_inventory.json',{})
    old_current=read(LEGACY/'status/live/current_status.json',{}) or {}
    old_health=read(LEGACY/'status/live/monitor_health.json',{}) or {}
    queue=read(OUT/'orchestrator_queue.json',{'tasks':[]}) or {'tasks':[]}
    orchestrator=read(OUT/'orchestrator_health.json',{}) or {}
    paper=read(OUT/'paper_readiness.json',{}) or {}
    current=read(OUT/'current_status.json',{}) or {}
    old_text=json.dumps(old_current,sort_keys=True)
    drift=[]
    for job in jobs.get('active_or_pending',[]):
        jid=str(job.get('job_id'))
        if jid and jid not in old_text:
            drift.append({'type':'MONITOR_DRIFT','message':f'Slurm job {jid} exists but legacy monitor state does not mention it.','job_id':jid})
    # Preserve the already confirmed historical miss as a durable integrity fact.
    cancel=read(OUT/'legacy_reset/49256_forensic_snapshot_20260923/cancellation_record.json',{}) or {}
    if cancel and not any(x.get('job_id')=='49256' for x in jobs.get('active_or_pending',[])):
        drift.append({'type':'MONITOR_DRIFT_HISTORICAL','message':'Legacy monitor missed active job 49256 before it was cancelled; scheduler discovery is authoritative.','job_id':'49256'})
    drift_unique={json.dumps(x,sort_keys=True):x for x in drift}
    drift=list(drift_unique.values())
    digest=hashlib.sha256(json.dumps(drift,sort_keys=True).encode()).hexdigest()
    previous=read(OUT/'monitor_last_drift.json',{}) or {}
    if drift and previous.get('digest')!=digest:
        with (OUT/'event_history.jsonl').open('a') as f:
            for item in drift: f.write(json.dumps({'timestamp':now.isoformat(),'event':'INTEGRITY_ALERT',**item},sort_keys=True)+'\n')
    atomic_json(OUT/'monitor_last_drift.json',{'timestamp':now.isoformat(),'digest':digest,'alerts':drift})
    servers=inventory.get('servers',{})
    atomic_json(OUT/'gpu_inventory.json',{'timestamp':now.isoformat(),'servers':{k:{'node':v.get('node'),'observed':v.get('observed'),'gpus':v.get('gpus',[]),'gpu_processes':v.get('gpu_processes',{}),'slurm_node':v.get('slurm_node')} for k,v in servers.items()}})
    unified={
        'schema_version':'v2r.unified_monitor.1','timestamp':now.isoformat(),
        'source_of_truth':['Slurm scheduler','actual GPU/process observation','filesystem observation'],
        'legacy_monitor':legacy_snapshot(),
        'legacy_monitor_health':old_health,
        'slurm_jobs':jobs,
        'inventory_summary':inventory.get('job_inventory_summary',{}),
        'servers':servers,
        'orchestrator':orchestrator,
        'queue':queue,
        'paper':paper,
        'integrity_alerts':drift,
    }
    atomic_json(OUT/'unified_status.json',unified)
    health={'schema_version':'v2r.monitor_health.1','status':'RUNNING','timestamp':now.isoformat(),'pid':os.getpid(),'tmux':'iclr2027-unified-monitor','poll_interval_seconds':90,'last_successful_cycle':now.isoformat(),'legacy_monitor_preserved':True,'legacy_monitor_health':old_health,'integrity_alert_count':len(drift)}
    atomic_json(OUT/'monitor_health.json',health)
    hours=(DEADLINE-now.astimezone(DEADLINE.tzinfo)).total_seconds()/3600
    lines=[now.isoformat(),f'HOURS TO DEADLINE: {hours:.2f}','CURRENT MODE: AUTONOMOUS REFERENCE-PRIMARY EXECUTION','','OVERALL GOAL','reference baseline → instrumentation equivalence → repairability → full paper','','NEW EVENTS', 'Unified monitor reconciled scheduler, GPU, filesystem, legacy monitor, orchestrator, artifacts, and paper state.']
    if drift:
        lines += ['','INTEGRITY ALERTS']+[f"{x['type']}: {x['message']}" for x in drift]
    else: lines += ['','INTEGRITY ALERTS','None in current active-job reconciliation.']
    lines += ['','ALL ACTIVE KIMHJ JOBS']
    active=jobs.get('active_or_pending',[])
    lines += [f"{j.get('job_id')} {j.get('job_name')} {j.get('state')} {j.get('node_list')} {j.get('classification')}" for j in active] or ['None']
    for name,s in servers.items():
        lines += ['',name.upper(),f"observed={s.get('observed')} idle_gpu_candidates={s.get('idle_gpu_candidates')} safe_filesystems={s.get('safe_filesystem_candidates')}"]
    lines += ['','LEGACY V2','See legacy monitor and legacy_reset snapshots; old evidence is not reference-primary evidence.','','REFERENCE GATES']
    gates=read(OUT/'gate_status.json',{}) or {}
    for key,val in sorted(gates.items()): lines.append(f"{key}: "+', '.join(f'{k}={v.get("status")}' for k,v in val.items()))
    lines += ['','REFERENCE PRIMARY']
    for key,val in (current.get('primary_evidence') or {}).items(): lines.append(f'{key}: {val}')
    lines += ['','ACTIVE SHARDS']+[f"{t.get('id')}: {t.get('status')} job={t.get('job_id')}" for t in queue.get('tasks',[])]
    science=[t for t in queue.get('tasks',[]) if t.get('kind')=='science_shard']
    math=[t for t in science if t.get('task')=='math500']
    math_base=[t for t in math if t.get('stage')=='base']
    math_core=[t for t in math if t.get('purpose')=='core']
    math_temporal=[t for t in math if t.get('purpose')=='temporal']
    if not math_base or any(t.get('status') in {'READY','SUBMITTED','PENDING','RUNNING','RESOURCE_WAIT'} for t in math_base):
        p0='Complete LLaDA MATH base and freeze the shared trajectory bank.'
    elif not math_core or any(t.get('status') in {'READY','SUBMITTED','PENDING','RUNNING','RESOURCE_WAIT'} for t in math_core):
        p0='Complete LLaDA MATH core repairability and seal its reference bundle.'
    elif not math_temporal or any(t.get('status') in {'READY','SUBMITTED','PENDING','RUNNING','RESOURCE_WAIT'} for t in math_temporal):
        p0='Complete LLaDA MATH temporal evidence and seal its reference bundle.'
    else:
        p0='Import sealed LLaDA evidence, build the PDF, and close author review.'
    lines += ['','PAPER',f"status={paper.get('status')}",f"technical_pdf_audit={paper.get('technical_pdf_audit',{}).get('status')}",'','ORCHESTRATOR',f"status={orchestrator.get('status')} pid={orchestrator.get('pid')} heartbeat={orchestrator.get('timestamp')}",'','MONITOR',f"heartbeat={now.isoformat()}",'','CURRENT P0',p0,'','NEXT AUTONOMOUS ACTIONS','Reconcile actual Slurm jobs every 90 seconds; keep only FREE_SAFE GPUs for reference shards; unlock downstream work only after sealed gates.','','TRUE USER-REQUIRED BLOCKERS','None currently.']
    (OUT/'attention_required.md').write_text('\n'.join(lines)+'\n')
    return unified

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--once',action='store_true'); ap.add_argument('--interval',type=int,default=90); a=ap.parse_args()
    while True:
        try: reconcile()
        except Exception as e:
            atomic_json(OUT/'monitor_health.json',{'schema_version':'v2r.monitor_health.1','status':'DEGRADED_RETRY','timestamp':dt.datetime.now(dt.timezone.utc).isoformat(),'pid':os.getpid(),'error':str(e)})
        if a.once: break
        time.sleep(max(30,a.interval))

if __name__=='__main__': main()
