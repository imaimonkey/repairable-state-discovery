#!/usr/bin/env python3
"""Create and submit resource-gated scientific shard plans after R2.

The module is deliberately conservative: it only unlocks a base bank after
the matching LLaDA R2 report is PASS, uses the frozen one-trajectory executor,
and leaves merge/seal decisions to the same single orchestrator.
"""
from __future__ import annotations
import datetime as dt, json, os, shlex, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
sys.path.insert(0,str(ROOT/'scripts'))
from repairable_diffusion.src.v2r.artifacts import atomic_json, read_json, merge_run, validate_shard
from repairable_diffusion.src.v2r.planning import make_plan, select_budget, freeze_failed_subset
from repairable_diffusion.src.v2r.reference_sources import load_records
from repairable_diffusion.src.v2r.schema import canonical_hash, file_hash
from v2r_submit import storage_gate, environment, PYTHON, RUNTIME

OUT=Path('/var/tmp/kimhj-v2r-reference/outputs/v2r_reference')
SOURCE_CACHE=Path('/var/tmp/kimhj-v2r-reference/upstream')
MODEL_CACHE=Path('/var/tmp/kimhj-v2r-reference/model-cache')
DESIGN_SHA=canonical_hash(read_json(ROOT/'status/v2r/design_freeze.json'))
EXECUTOR='repairable_diffusion.src.v2r.science:execute_base'

def _gate_paths(backbone, task):
 base=OUT/f'gate-78fe5d7-llada-{task}'
 return {stage:read_json(base/stage/'gate_report.json') for stage in ('R0','R1','R2')}

def gates_for(backbone, task):
 try:gates=_gate_paths(backbone,task)
 except (FileNotFoundError,json.JSONDecodeError):return None
 return gates if all(g.get('status')=='PASS' for g in gates.values()) else None

def base_spec(backbone, task, seconds_per_item):
 recipe=read_json(ROOT/f'results/v2r_reference/reference_recipes/{backbone}.json')
 rows=load_records(recipe,task,'bridge',SOURCE_CACHE)
 model={'backbone':backbone,'id':recipe['model_id'],'revision':recipe['model_revision'],'tokenizer_revision':recipe['tokenizer_revision']}
 dataset={'id':recipe['tasks'][task]['bridge_dataset']['path'],'revision':recipe['tasks'][task]['bridge_dataset']['revision'],'split':recipe['tasks'][task]['bridge_dataset']['split'],'task':task,'content_sha256':canonical_hash(rows)}
 # The gate reports bind to this exact contract; scientific stages reuse it
 # instead of introducing a post-gate config hash.
 config={'design_generation':2,'task':task,'generation':recipe['tasks'][task]['generation'],'checkpoint_grid':[.125,.25,.375,.5,.625,.75,.875],'B_loc':4,'B_eval':8,'tau_confirm':.25,'design_seed':20260923}
 return {'run_id':f'{backbone}_{task}_base_finalsha','stage':'base','design_seed':20260923,'design_sha256':DESIGN_SHA,
  'execution_git_sha':'78fe5d7c1829b67d1bb1416b7205edfa647bb2fa','model':model,'dataset':dataset,'recipe':recipe,'config':config,
  'item_ids':[str(r['item_id']) for r in rows],'executor':EXECUTOR,
  'runtime_paths':{'source_cache':str(SOURCE_CACHE),'model_cache':str(MODEL_CACHE)},
  'execution_worktree':'/var/tmp/kimhj-v2r-reference/execution/gates-78fe5d7',
  'timing':{'seconds_per_item':float(seconds_per_item),'target_shard_hours':4.0},
  'seed_plan':[{'purpose':'base','checkpoints':[0],'branches':1,'operators':['reference'],'rng_role':'future'}]}

def ensure_base_tasks(queue):
 """Append base shard tasks exactly once for every newly passing LLaDA R2."""
 tasks=queue.setdefault('tasks',[]); changed=False
 for task_name in ('math500','gsm8k'):
  r2=next((t for t in tasks if t.get('id')==f'llada-{task_name}-r2-finalsha'),None)
  if not r2 or r2.get('status')!='PASS': continue
  if any(t.get('kind')=='science_shard' and t.get('task')==task_name and t.get('stage')=='base' for t in tasks): continue
  gates=gates_for('llada',task_name)
  if gates is None: continue
  timing=float(gates['R0'].get('timing',{}).get('mean_seconds_per_base',20.0))
  spec=make_plan(base_spec('llada',task_name,timing))
  manifest_path=OUT/f'plans/{spec["run_id"]}.json'; gates_path=OUT/f'plans/{spec["run_id"]}.gates.json'
  atomic_json(manifest_path,spec); atomic_json(gates_path,gates)
  run_dir=OUT/f'runs/{spec["run_id"]}'; run_dir.mkdir(parents=True,exist_ok=True)
  for shard in spec['shards']:
   sid=shard['shard_id']
   tasks.append({'id':f'{spec["run_id"]}-shard-{sid:03d}','kind':'science_shard','backbone':'llada','task':task_name,'stage':'base','priority':20 if task_name=='math500' else 30,
    'status':'READY','depends_on':[r2['id']],'execution_git_sha':spec['execution_git_sha'],'execution_worktree':str(ROOT),'manifest':str(manifest_path),'gates':str(gates_path),'run_dir':str(run_dir),'shard':sid,'server':'server3','walltime':'04:00:00'})
  changed=True
 return changed

def submit_science(task, inventory):
 node=inventory['servers'].get(task['server'],{})
 if not node.get('observed') or not node.get('idle_gpu_candidates'): raise RuntimeError('NO_OBSERVED_IDLE_GPU_FOR_SCIENCE')
 storage=storage_gate(task['run_dir'],projected=4*1024**3)
 manifest=read_json(task['manifest']); gates=read_json(task['gates'])
 if manifest.get('execution_git_sha')!='78fe5d7c1829b67d1bb1416b7205edfa647bb2fa': raise RuntimeError('SCIENCE_SHA_MISMATCH')
 script=RUNTIME/(task['id']+'.sbatch'); script.parent.mkdir(parents=True,exist_ok=True)
 execution_worktree=Path(manifest['execution_worktree']) if manifest.get('execution_worktree') else Path('/var/tmp/kimhj-v2r-reference/execution/gates-78fe5d7')
 # Worker and imported executor must come from the same immutable SHA as the gate.
 cmd=[PYTHON,str(execution_worktree/'scripts/v2r_worker.py'),'--manifest',task['manifest'],'--shard',str(task['shard']),'--run-dir',task['run_dir'],'--gates',task['gates']]
 lines=['#!/usr/bin/env bash','set -euo pipefail',f'cd {shlex.quote(str(execution_worktree))}']+[f'export {k}={shlex.quote(v)}' for k,v in environment().items()]
 lines += ['exec '+shlex.join(cmd)]; script.write_text('\n'.join(lines)+'\n')
 logdir=Path(task['run_dir'])/'logs';logdir.mkdir(parents=True,exist_ok=True)
 args=['sbatch','--parsable','--partition=gpu','--qos=lab_gpu_s3','--nodelist=ubuntu','--gres=gpu:h200:1','--cpus-per-task=4','--mem=48G','--time='+task.get('walltime','04:00:00'),'--job-name=v2r-'+task['id'],'--chdir='+str(ROOT),'--output='+str(logdir/'slurm-%j.out'),'--error='+str(logdir/'slurm-%j.err'),str(script)]
 r=subprocess.run(args,text=True,capture_output=True)
 if r.returncode:raise RuntimeError(r.stderr)
 jid=r.stdout.strip().split(';')[0]
 if not jid.isdigit():raise RuntimeError('Invalid scientific sbatch id '+r.stdout)
 return {'job_id':jid,'submitted_at':dt.datetime.now(dt.timezone.utc).isoformat(),'submission_args':args,'script':str(script),'storage':storage}

def finalize_base(task_group):
 first=task_group[0];manifest=read_json(first['manifest']);gates=read_json(first['gates']);run_dir=Path(first['run_dir'])
 aggregate=merge_run(manifest,run_dir,gates=gates)
 return aggregate

def _bank_for_base(task_group):
 first=task_group[0]; manifest=read_json(first['manifest']); run_dir=Path(first['run_dir'])
 aggregate=read_json(run_dir/'aggregate/aggregate.json')
 shard_for={item:shard['shard_id'] for shard in manifest['shards'] for item in shard['item_ids']}
 bank=[]; index={}
 for row in aggregate['items']:
  item=str(row['item_id']); shard=shard_for[item]
  path=run_dir/'shards'/f'shard-{shard:03d}'/'items'/canonical_hash(item)/'trajectory.json'
  entry={'item_id':item,'trajectory_id':0,'correct':bool(row['result']['correct']),'path':str(path),'sha256':file_hash(path)}
  bank.append(entry); index[item]={'path':str(path),'sha256':entry['sha256']}
 bank.sort(key=lambda x:x['item_id'])
 bank_sha=canonical_hash(bank)
 atomic_json(run_dir/'bank.json',{'status':'FROZEN_INPUT','bank_sha256':bank_sha,'items':bank})
 return manifest,run_dir,bank,bank_sha,index

def _budget(bank, purpose, base_seconds):
 failed=sum(not x['correct'] for x in bank)
 now=dt.datetime.now(dt.timezone.utc); deadline=dt.datetime.fromisoformat('2026-09-26T20:59:00+09:00')
 fs=Path('/var/tmp/kimhj-v2r-reference/outputs/v2r_reference'); v=os.statvfs(fs); free=v.f_bavail*v.f_frsize; used=(v.f_blocks-v.f_bfree)*v.f_frsize; frac=used/(used+free)
 multiplier=79 if purpose=='core' else 112
 return select_budget(backbone='llada',purpose=purpose,seconds_per_item=max(1.0,base_seconds*multiplier),bytes_per_item=16*1024*1024,available_gpu_hours=max(1.0,(deadline-now).total_seconds()/3600),deadline_hours=max(1.0,(deadline-now).total_seconds()/3600),gpu_count=1,free_bytes=free,safety_margin_bytes=50*1024**3,filesystem_used_fraction=frac,pilot_item_count=8,failed_pool_size=failed,reserve_hours=6.0)

def _deep_spec(base_manifest, run_dir, bank, bank_sha, index, purpose, budget):
 recipe=base_manifest['recipe']; task=base_manifest['dataset']['task']; items=[x['item_id'] for x in bank if not x['correct']]
 failed=freeze_failed_subset(bank,bank_sha256=bank_sha,budget=budget,design_seed=20260923,backbone='llada',task=task,purpose=purpose)
 selected=failed['item_ids']; trajectory_index={item:index[item] for item in selected}
 sample=read_json(index[selected[0]]['path'])['trajectory']; checkpoints=[x['step'] for x in sample['checkpoint_mapping']]
 stage='r3_core' if purpose=='core' else 'temporal'
 config={'design_generation':2,'task':task,'generation':recipe['tasks'][task]['generation'],'checkpoint_grid':[.125,.25,.375,.5,.625,.75,.875],'B_loc':4,'B_eval':8,'tau_confirm':.25,'design_seed':20260923}
 if purpose=='core':
  plan=[{'purpose':'localization','checkpoints':checkpoints,'branches':4,'operators':['matched_continuation','canonical_repair'],'rng_role':'future','paired_rng_group':'matched-future'}, {'purpose':'confirmation','checkpoints':checkpoints,'branches':8,'operators':['matched_continuation','canonical_repair'],'rng_role':'future','paired_rng_group':'matched-future'}]
 else:
  plan=[{'purpose':'confirmation','checkpoints':checkpoints,'branches':8,'operators':['matched_continuation','canonical_repair'],'rng_role':'future','paired_rng_group':'matched-future'}]
 return {'run_id':f'llada_{task}_{purpose}_finalsha','stage':stage,'design_seed':20260923,'design_sha256':DESIGN_SHA,'execution_git_sha':base_manifest['execution_git_sha'],'model':base_manifest['model'],'dataset':base_manifest['dataset'],'recipe':recipe,'config':config,'item_ids':selected,'executor':'repairable_diffusion.src.v2r.science:execute_probe','runtime_paths':base_manifest['runtime_paths'],'execution_worktree':base_manifest['execution_worktree'],'trajectory_index':trajectory_index,'failed_pool_freeze':failed,'budget':budget,'timing':{'seconds_per_item':budget['inputs']['seconds_per_item'],'target_shard_hours':4.0},'seed_plan':plan}

def ensure_deep_tasks(queue):
 tasks=queue.setdefault('tasks',[]); changed=False
 groups={}
 for task in tasks:
  if task.get('kind')=='science_shard' and task.get('stage')=='base':groups.setdefault(task['run_dir'],[]).append(task)
 for run_dir,base_tasks in groups.items():
  if not base_tasks or not all(t.get('status') in {'MERGED','SEALED'} for t in base_tasks):continue
  base_manifest=read_json(base_tasks[0]['manifest']); task_name=base_manifest['dataset']['task']
  if any(t.get('kind')=='science_shard' and t.get('run_dir','').endswith('_core_finalsha') and t.get('task')==task_name for t in tasks):continue
  bank_manifest=Path(run_dir)/'bank.json'
  if bank_manifest.exists():
   bank_doc=read_json(bank_manifest); bank=bank_doc['items']; bank_sha=bank_doc['bank_sha256']; index={x['item_id']:{'path':x['path'],'sha256':x['sha256']} for x in bank}
  else:
   base_manifest,run_dir,bank,bank_sha,index=_bank_for_base(base_tasks)
  gates=gates_for('llada',task_name)
  if gates is None:continue
  base_seconds=float(gates['R0'].get('timing',{}).get('mean_seconds_per_base',20.0))
  for purpose in ('core','temporal'):
   budget=_budget(bank,purpose,base_seconds)
   if budget['status']!='FROZEN':continue
   spec=_deep_spec(base_manifest,run_dir,bank,bank_sha,index,purpose,budget)
   manifest_path=OUT/f'plans/{spec["run_id"]}.json'; gates_path=OUT/f'plans/{spec["run_id"]}.gates.json'; atomic_json(manifest_path,spec);atomic_json(gates_path,gates)
   deep_dir=OUT/f'runs/{spec["run_id"]}';deep_dir.mkdir(parents=True,exist_ok=True)
   for shard in spec['shards']:
    sid=shard['shard_id']; tasks.append({'id':f'{spec["run_id"]}-shard-{sid:03d}','kind':'science_shard','backbone':'llada','task':task_name,'stage':spec['stage'],'purpose':purpose,'priority':21 if purpose=='core' else 22,'status':'READY','depends_on':[t['id'] for t in base_tasks],'execution_git_sha':spec['execution_git_sha'],'execution_worktree':spec['execution_worktree'],'manifest':str(manifest_path),'gates':str(gates_path),'run_dir':str(deep_dir),'shard':sid,'server':'server3','walltime':'04:00:00'})
   changed=True
 return changed
