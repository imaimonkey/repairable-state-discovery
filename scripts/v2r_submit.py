#!/usr/bin/env python3
"""Explicit, inventory-gated Slurm submission of prepared reference gate tasks."""
from __future__ import annotations
import datetime as dt,hashlib,json,os,shlex,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DEADLINE=dt.datetime.fromisoformat('2026-09-26T20:59:00+09:00')
PYTHON='/data/kimhj/llada8b_basic/.venv/bin/python'
RUNTIME=Path('/var/tmp/kimhj-v2r-reference/runtime')

def storage_gate(path,projected=2*1024**3):
 p=Path(path);p.mkdir(parents=True,exist_ok=True);v=os.statvfs(p)
 available=v.f_bavail*v.f_frsize;used=(v.f_blocks-v.f_bfree)*v.f_frsize
 if used/(used+available)>=.95 or available<2*projected+50*1024**3 or v.f_favail<10000:raise RuntimeError('STORAGE_GATE_FAILED')
 return {'available_bytes':available,'projected_bytes':projected,'usage_fraction':used/(used+available)}

def command(task):
 return [PYTHON,str(Path(task['execution_worktree'])/'scripts/v2r_reference_gate.py'),'--backbone',task['backbone'],'--task',task['task'],'--stage',task['stage'],'--output',task['output'],'--source-cache','/var/tmp/kimhj-v2r-reference/upstream','--model-cache',task.get('model_cache','/var/tmp/kimhj-v2r-reference/model-cache'),'--execution-sha',task['execution_git_sha']]

def environment():
 return {'HF_DATASETS_CACHE':'/var/tmp/kimhj-v2r-reference/datasets','HF_MODULES_CACHE':'/var/tmp/kimhj-v2r-reference/modules','HF_HUB_CACHE':'/var/tmp/kimhj-v2r-reference/hub','OMP_NUM_THREADS':'4','TOKENIZERS_PARALLELISM':'false','PYTHONDONTWRITEBYTECODE':'1'}

def audit_prepared_registries():
 owners={};count=0
 for path in Path('/var/tmp/kimhj-v2r-reference/outputs/v2r_reference').glob('gate-*/*/seed_registry.json'):
  registry=json.loads(path.read_text())
  for row in registry['records']:
   key=(registry['scope'],row['group_id'])
   if row['seed'] in owners and owners[row['seed']]!=key:raise RuntimeError('UNINTENDED_CROSS_JOB_SEED_COLLISION')
   owners[row['seed']]=key;count+=1
 if not count:raise RuntimeError('NO_PREPARED_SEED_REGISTRIES')
 return {'context_count':count,'unique_seed_count':len(owners),'unintended_collisions':0}

def submit(task,inventory,dry_run=False):
 hours=(DEADLINE-dt.datetime.now(dt.timezone.utc)).total_seconds()/3600
 if hours<=12:raise RuntimeError('DEADLINE_NO_NEW_LONG_SCIENTIFIC_JOB')
 if task['server']!='server3':raise RuntimeError('Remote execution requires verified code/cache deployment first')
 node=inventory['servers'][task['server']]
 if not node['observed'] or not node['idle_gpu_candidates']:raise RuntimeError('NO_OBSERVED_IDLE_GPU')
 checked=dt.datetime.fromisoformat(inventory['timestamp'])
 if (dt.datetime.now(dt.timezone.utc)-checked).total_seconds()>300:raise RuntimeError('INVENTORY_TOO_OLD')
 storage=storage_gate(task['output']); seed_audit=audit_prepared_registries()
 prepared=Path(task['output'])/task['stage']/'prepared.json'
 if not prepared.is_file():raise RuntimeError('CPU_SEED_PREPARATION_REQUIRED')
 prep=json.loads(prepared.read_text())
 if prep['execution_git_sha']!=task['execution_git_sha']:raise RuntimeError('PREPARED_SHA_MISMATCH')
 repo=Path(task['execution_worktree'])
 if subprocess.check_output(['git','rev-parse','HEAD'],cwd=repo,text=True).strip()!=task['execution_git_sha']:raise RuntimeError('IMMUTABLE_SHA_MISMATCH')
 if subprocess.run(['git','diff','--quiet'],cwd=repo).returncode:raise RuntimeError('DIRTY_EXECUTION_TREE')
 # Avoid model/process overlap even if an unmanaged process evades Slurm.
 precheck="import subprocess; p=subprocess.run(['nvidia-smi','--query-compute-apps=pid','--format=csv,noheader'],capture_output=True,text=True); assert p.returncode==0 and not p.stdout.strip(), 'CONFLICTING_GPU_PROCESS'"
 lines=['#!/usr/bin/env bash','set -euo pipefail',f'cd {shlex.quote(str(repo))}']
 lines += [f'export {k}={shlex.quote(v)}' for k,v in environment().items()]
 lines += [shlex.join([PYTHON,'-c',precheck]),'exec '+shlex.join(command(task))]
 script=RUNTIME/(task['id']+'.sbatch');script.parent.mkdir(parents=True,exist_ok=True)
 script.write_text('\n'.join(lines)+'\n')
 logdir=Path(task['output'])/task['stage'];logdir.mkdir(parents=True,exist_ok=True)
 args=['sbatch','--parsable','--partition=gpu','--qos=lab_gpu_s3','--nodelist=ubuntu','--gres=gpu:h200:1','--cpus-per-task=4','--mem=48G','--time='+task.get('walltime','04:00:00'),'--job-name=v2r-'+task['id'],'--chdir='+str(repo),'--output='+str(logdir/'slurm-%j.out'),'--error='+str(logdir/'slurm-%j.err'),str(script)]
 if dry_run:return {'command':args,'storage':storage}
 r=subprocess.run(args,text=True,capture_output=True)
 if r.returncode:raise RuntimeError(r.stderr)
 job=r.stdout.strip().split(';')[0]
 if not job.isdigit():raise RuntimeError('Invalid sbatch job id '+r.stdout)
 return {'job_id':job,'submitted_at':dt.datetime.now(dt.timezone.utc).isoformat(),'storage':storage,'script':str(script),'submission_args':args,'seed_audit':seed_audit}
