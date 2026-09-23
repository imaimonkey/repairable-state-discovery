"""Reference-bank and LLaDA two-stage counterfactual item executors.

This module contains no result-driven recipe changes. Reference sampler and task
adapters are imported from the independently tested, source-pinned implementation.
"""
from __future__ import annotations
import math,time
from pathlib import Path
from .artifacts import atomic_json,read_json
from .schema import canonical_hash,file_hash,ContractError
from .reference_sources import load_records,bridge_evaluate
from .reference_sampler import ReferenceSampler
_CACHE={}

def runtime(manifest):
 key=canonical_hash([manifest['model'],manifest['dataset'],manifest['recipe']])
 if key not in _CACHE:
  recipe=manifest['recipe'];task=manifest['dataset']['task'];paths=manifest['runtime_paths']
  rows=load_records(recipe,task,'bridge',Path(paths['source_cache']))
  if canonical_hash(rows)!=manifest['dataset']['content_sha256']:raise ContractError('Dataset content differs from frozen bank contract')
  sampler=ReferenceSampler(recipe,task,Path(paths['source_cache']),Path(paths['model_cache']))
  _CACHE[key]=(sampler,{str(r['item_id']):r for r in rows})
 return _CACHE[key]

def execute_base(manifest,item_id,item_output_dir,seed_records):
 sampler,items=runtime(manifest)
 if len(seed_records)!=1:raise ContractError('One base seed per sampled trajectory required')
 row=sampler.generate(items[item_id],seed_records[0]['seed'],True)
 if row['mask_count'] or row['nfe']!=manifest['config']['generation']['steps']:raise ContractError('Base mask exhaustion/NFE failure')
 atomic_json(item_output_dir/'trajectory.json',{'item':items[item_id],'trajectory':row})
 return {'correct':row['correct'],'official_correct':row['official_evaluation']['correct'],'trajectory_id':0,'seed_context_ids':[seed_records[0]['context_id']],'evidence_kind':'reference_scientific','nfe':row['nfe'],'seconds':row['seconds'],'final_token_ids_sha256':canonical_hash(row['final_token_ids']),'trajectory_file':'trajectory.json','trajectory_sha256':file_hash(item_output_dir/'trajectory.json'),'checkpoint_steps':[v['step'] for v in row['checkpoint_mapping']]}

def canonical_positions(snapshot,config):
 if snapshot['step_in_block']>=snapshot['steps_per_block']:return []
 length=config['generation']['block_length'];start=snapshot['block_index']*length;end=start+length
 eligible=[(i,float(snapshot['token_confidences'][i])) for i in range(start,end) if snapshot['token_confidences'][i] is not None]
 low=[v for v in eligible if v[1]<.80] or eligible
 low.sort(key=lambda v:(v[1],v[0]));count=min(len(low),max(4,math.ceil(len(low)*.25)))
 return sorted(i for i,_ in low[:count])

def execute_probe(manifest,item_id,item_output_dir,seed_records):
 if manifest['model']['backbone']!='llada':raise ContractError('Dream continuation has not passed native replay validation')
 sampler,items=runtime(manifest);item=items[item_id]
 source=manifest['trajectory_index'][item_id]
 if file_hash(source['path'])!=source['sha256']:raise ContractError('Original bank snapshot hash mismatch')
 stored=read_json(source['path']);trajectory=stored['trajectory']
 if trajectory['correct'] is not False:raise ContractError('Failed-trajectory probe received successful base')
 states={int(k):v for k,v in trajectory['snapshots'].items() if int(k)<v['total_steps']}
 expected=[r['step'] for r in trajectory['checkpoint_mapping']]
 if sorted(states)!=sorted(expected):raise ContractError('Missing reference checkpoint')
 lookup={(r['context']['purpose'],r['context']['checkpoint'],r['context']['branch'],r['context']['operator']):r for r in seed_records}
 consumed=set();rows=[];native=[];observations=[];start=time.perf_counter()
 for step in sorted(states):
  snap=states[step];text=sampler.decode(__import__('torch').tensor(snap['full_token_ids']).unsqueeze(0),snap['prompt_len'])
  observations.append({'step':step,'normalized_progress':step/snap['total_steps'],'observed_correct':bridge_evaluate(sampler.task,text,item)['correct']})
  # Native fidelity is measured for each actual scientific trajectory and state.
  replay=sampler.continue_llada(item,snap)
  ok=replay['final_token_ids']==trajectory['final_token_ids'] and replay['nfe']==snap['total_steps']-step and replay['mask_count']==0
  native.append({'step':step,'exact_tokens':ok,'nfe':replay['nfe']})
  if not ok:raise ContractError('Exact native replay failed on scientific trajectory')
 def branches(step,purpose,count):
  snap=states[step];positions=canonical_positions(snap,manifest['config'])
  for branch in range(count):
   for operator in ['matched_continuation','canonical_repair']:
    rec=lookup[(purpose,step,branch,operator)]
    modified=positions if operator=='canonical_repair' else []
    outcome=sampler.continue_llada(item,snap,seed=rec['seed'],modified_positions=modified)
    if outcome['mask_count']:raise ContractError('Counterfactual continuation left masked tokens')
    consumed.add(rec['context_id'])
    rows.append({'step':step,'normalized_progress':step/snap['total_steps'],'purpose':purpose,'branch':branch,'operator':operator,'seed_context_id':rec['context_id'],'rng_group_id':rec['group_id'],'seed':rec['seed'],'correct':outcome['correct'],'answer':outcome['answer'],'final_tokens_sha256':canonical_hash(outcome['final_token_ids']),'nfe':outcome['nfe'],'seconds':outcome['seconds'],'modified_positions':modified,'applicable':bool(positions) if operator=='canonical_repair' else True})
 def summarize(step,purpose):
  selected=[r for r in rows if r['step']==step and r['purpose']==purpose]
  estimates={op:sum(r['correct'] for r in selected if r['operator']==op)/sum(r['operator']==op for r in selected) for op in ['matched_continuation','canonical_repair']}
  return {'step':step,'normalized_progress':step/trajectory['snapshots'][str(step)]['total_steps'],'q_C':estimates['matched_continuation'],'q_R':estimates['canonical_repair'],'Delta_R':estimates['canonical_repair']-estimates['matched_continuation']}
 if manifest['stage']=='r3_core':
  for step in sorted(states):branches(step,'localization',4)
  localized=[summarize(step,'localization') for step in sorted(states)]
  chosen=min(localized,key=lambda r:(-r['q_R'],r['step']))['step']
  branches(chosen,'confirmation',8);confirmed=[summarize(chosen,'confirmation')]
 elif manifest['stage']=='temporal':
  for step in sorted(states):branches(step,'confirmation',8)
  localized=[];chosen=None;confirmed=[summarize(step,'confirmation') for step in sorted(states)]
 else:raise ContractError('Unsupported probe stage')
 never_correct=not any(o['observed_correct'] for o in observations)
 sensitivity={str(tau):any(r['q_R']>=tau for r in confirmed) for tau in [.125,.25,.5]}
 confirmed_repairable=sensitivity['0.25'];native_recoverable=any(r['q_C']>=.25 for r in confirmed)
 tlast=max([r['normalized_progress'] for r in confirmed if r['q_R']>=.25],default=None) if manifest['stage']=='temporal' else None
 raw={'item_id':item_id,'trajectory_id':0,'bank_sha256':manifest['failed_pool_freeze']['bank_sha256'],'native_fidelity':native,'observed_grid':observations,'localization':localized,'confirmation':confirmed,'branches':rows,'selected_checkpoint':chosen,'deterministic_reference':True}
 atomic_json(item_output_dir/'counterfactual.json',raw)
 unused=[r['context_id'] for r in seed_records if r['context_id'] not in consumed]
 if unused and manifest['stage']!='r3_core':raise ContractError('Unexpected unused temporal context')
 return {'evidence_kind':'reference_scientific','trajectory_id':0,'bank_sha256':manifest['failed_pool_freeze']['bank_sha256'],'seed_context_ids':sorted(consumed),'unused_seed_context_ids':sorted(unused),'unused_seed_context_reason':'not_selected_checkpoint' if unused else None,'confirmed_repairable':confirmed_repairable,'never_correct_repairable':confirmed_repairable and never_correct,'native_recoverable':native_recoverable,'confirmation':confirmed,'T_last_R':tlast,'sensitivity':sensitivity,'selected_checkpoint':chosen,'nfe':sum(r['nfe'] for r in rows)+sum(r['nfe'] for r in native),'seconds':time.perf_counter()-start,'counterfactual_file':'counterfactual.json','counterfactual_sha256':file_hash(item_output_dir/'counterfactual.json'),'deterministic_reference':True,'independent_bernoulli_replicates_claimed':False}
