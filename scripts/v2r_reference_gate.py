#!/usr/bin/env python3
"""Run real source-native R0, bridge R1, or exact instrumentation R2 gates."""
from __future__ import annotations
import argparse,datetime,json,os,subprocess,sys,time,traceback
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from repairable_diffusion.src.v2r.schema import canonical_hash,file_hash
from repairable_diffusion.src.v2r.artifacts import atomic_json,read_json
from repairable_diffusion.src.v2r.seeds import build_seed_registry
from repairable_diffusion.src.v2r.reference_sources import ensure_sources,load_records,OfficialEvaluator,bridge_evaluate
from repairable_diffusion.src.v2r.reference_gates import validate_gate_report

def contract(recipe,task):
 return {'design_generation':2,'task':task,'generation':recipe['tasks'][task]['generation'],'checkpoint_grid':recipe['checkpoint_normalized_grid'],'B_loc':4,'B_eval':8,'tau_confirm':0.25,'design_seed':20260923}

def fixtures(backbone,task,sources):
 official=OfficialEvaluator(backbone,task,sources)
 rows=[('The answer is 1,234.', '1234'),('The answer is 12.5.', '12.5'),('The answer is -3.', '-3')] if task=='gsm8k' else [(r'Final Answer: The final answer is $42$. I hope it is correct. \boxed{42}','42'),(r'Final Answer: The final answer is $\frac{1}{2}$. I hope it is correct. \boxed{\frac{1}{2}}',r'\frac{1}{2}')]
 observed=[]
 for text,gold in rows:
  item={'answer':gold};o=official.evaluate(text,item);b=bridge_evaluate(task,text,item)
  observed.append({'text':text,'gold':gold,'official':o,'paper':b})
 # Source-native correctness and paper correctness tested independently.
 for row in observed:
  row['expected_official_correct'] = not (backbone=='llada' and task=='gsm8k' and row['gold']=='1234')
  row['expected_paper_correct'] = True
  if not row['expected_official_correct']:
   row['expected_official_answer']='234'  # pinned upstream regex splits comma-formatted number
 return all(r['official']['correct']==r['expected_official_correct'] and r['paper']['correct']==r['expected_paper_correct'] and ('expected_official_answer' not in r or r['official']['answer']==r['expected_official_answer']) for r in observed),observed

def main():
 p=argparse.ArgumentParser();p.add_argument('--backbone',choices=['llada','dream'],required=True);p.add_argument('--task',choices=['math500','gsm8k'],required=True);p.add_argument('--stage',choices=['R0','R1','R2'],required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--source-cache',type=Path,required=True);p.add_argument('--model-cache',type=Path,required=True);p.add_argument('--execution-sha',required=True);p.add_argument('--prepare-only',action='store_true');a=p.parse_args()
 if 'v2r_reference' not in a.output.resolve().parts:raise ValueError('Isolated namespace required')
 if subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()!=a.execution_sha:raise ValueError('Execution HEAD mismatch')
 if subprocess.run(['git','diff','--quiet'],cwd=ROOT).returncode:raise ValueError('Dirty execution tree')
 recipe=read_json(ROOT/f'results/v2r_reference/reference_recipes/{a.backbone}.json');cfg=contract(recipe,a.task)
 sources=ensure_sources(recipe,a.source_cache)
 records=load_records(recipe,a.task,'bridge',a.source_cache)
 dataset_hash=canonical_hash(records)
 selected=sorted(records,key=lambda row:canonical_hash([20260923,a.backbone,a.task,'gate-items',row['item_id']]))[:32]
 selected=selected[:16] if a.stage in ['R0','R1'] else selected
 scenarios=[20260923,20260924] if a.stage=='R2' else [20260923]
 contexts=[]
 for row in selected:
  for k,scenario in enumerate(scenarios):
   for operator in (['reference','instrumented'] if a.stage=='R2' else ['reference']):
    contexts.append({'stage':a.stage,'purpose':'equivalence' if a.stage=='R2' else 'base','item_id':str(row['item_id']),'trajectory_id':0,'checkpoint':0,'branch':scenario,'operator':operator,'rng_role':'future','paired_rng_group':'reference-equivalence' if a.stage=='R2' else None})
 registry=build_seed_registry(contexts,design_seed=20260923,scope=canonical_hash([a.execution_sha,a.backbone,a.task]))
 stage_dir=a.output/a.stage;stage_dir.mkdir(parents=True,exist_ok=True)
 registry_path=stage_dir/'seed_registry.json'
 if registry_path.exists():
  if read_json(registry_path)!=registry:raise ValueError('Prepared seed registry mismatch')
 elif a.prepare_only:atomic_json(registry_path,registry)
 else:raise ValueError('CPU seed registry must be prepared before Slurm submission')
 if a.prepare_only:
  atomic_json(stage_dir/'prepared.json',{'status':'CPU_PREPARED_NOT_A_GATE_PASS','execution_git_sha':a.execution_sha,'seed_registry_sha256':canonical_hash(registry),'dataset_sha256':dataset_hash})
  print('CPU_PREPARED_NOT_A_GATE_PASS',a.backbone,a.task,a.stage,flush=True);return 0
 report={'gate':a.stage,'status':'RUNNING','evidence_kind':'real_model_reference_gate','backbone':a.backbone,'task':a.task,'execution_git_sha':a.execution_sha,'config_sha256':canonical_hash(cfg),'recipe_sha256':canonical_hash(recipe),'model_revision':recipe['model_revision'],'tokenizer_revision':recipe['tokenizer_revision'],'dataset_revision':recipe['tasks'][a.task]['bridge_dataset']['revision'],'dataset_sha256':dataset_hash,'seed_registry_sha256':canonical_hash(registry),'item_count':len(selected),'item_ids':[r['item_id'] for r in selected],'seed_scenarios':scenarios,'checks':{},'evidence_files':{},'started_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'full_official_benchmark_reproduction':'NOT_RUN_NOT_REQUIRED_FOR_NONIDENTICAL_PAPER_TASK','reported_comparison_status':recipe['tasks'][a.task]['reported_comparison_status']}
 for dependency in ({'R0':[],'R1':['R0'],'R2':['R0','R1']}[a.stage]):
  prior=read_json(a.output/dependency/'gate_report.json');errors=validate_gate_report(prior)
  if errors or prior['execution_git_sha']!=a.execution_sha:raise ValueError('Invalid dependency '+dependency+str(errors))
 atomic_json(stage_dir/'gate_report.json',report)
 try:
  if a.stage=='R1':
   fixture_pass,fixture_rows=fixtures(a.backbone,a.task,sources);atomic_json(stage_dir/'evaluator_fixtures.json',fixture_rows)
   disagreements=[];checked=0
   for path in sorted((a.output/'R0').glob('item-*.json')):
    value=read_json(path);row=value['generation'];item=value['item'];checked+=1
    official=OfficialEvaluator(a.backbone,a.task,sources).evaluate(row['final_text'],item);ours=bridge_evaluate(a.task,row['final_text'],item)
    if official['answer']!=ours['answer'] or official['correct']!=ours['correct']:
     disagreements.append({'item_id':item['item_id'],'official':official,'paper':ours,'classification':'pinned_extraction_or_equivalence_semantics_differ','source_text_sha256':canonical_hash(row['final_text'])})
   dis=stage_dir/'evaluator_disagreements.jsonl';dis.write_text(''.join(json.dumps(x,sort_keys=True)+'\n' for x in disagreements))
   report.update(checks={'fixture_tests_pass':fixture_pass,'same_outputs_dual_evaluated':checked==16,'disagreements_saved':True,'paper_dataset_pinned':True},disagreement_count=len(disagreements))
  else:
   from repairable_diffusion.src.v2r.reference_sampler import ReferenceSampler
   sampler=ReferenceSampler(recipe,a.task,a.source_cache,a.model_cache)
   results=[];replay=[]
   for index,item in enumerate(selected):
    for scenario in scenarios:
     seed=next(r['seed'] for r in registry['records'] if r['context']['item_id']==str(item['item_id']) and r['context']['branch']==scenario and r['context']['operator']=='reference')
     dest=stage_dir/f'item-{index:03d}-scenario-{scenario}.json'
     if dest.exists():
      value=read_json(dest)
      if value['execution_git_sha']!=a.execution_sha or value['seed']!=seed:raise ValueError('Stale gate item')
     else:
      reference=sampler.generate(item,seed,False)
      value={'execution_git_sha':a.execution_sha,'seed':seed,'item':item,'generation':reference}
      if a.stage=='R2':
       inst=sampler.generate(item,seed,True);value['instrumented']=inst
       value['equivalence']={key:reference[key]==inst[key] for key in ['final_token_ids','final_text','final_answer','correct','schedule','nfe','rng_end_sha256']}
       value['snapshot_grid_complete']=set(inst['snapshots'])=={str(x['step']) for x in inst['checkpoint_mapping']}|{str(recipe['tasks'][a.task]['generation']['steps'])}
       if index<8 and scenario==scenarios[0] and a.backbone=='llada':
        replay=[]
        for step,state in inst['snapshots'].items():
         if int(step)==state['total_steps'] or int(step) not in [inst['checkpoint_mapping'][j]['step'] for j in [0,3,6]]:continue
         continued=sampler.continue_llada(item,state)
         replay.append({'step':step,'tokens_exact':continued['final_token_ids']==inst['final_token_ids'],'nfe_exact':continued['nfe']==state['total_steps']-int(step),'mask_exhausted':continued['mask_count']==0,'seconds':continued['seconds'],'nfe':continued['nfe']})
        value['native_replay_checks']=replay
      atomic_json(dest,value)
     results.append(value)
     atomic_json(stage_dir/'progress.json',{'completed_generations':len(results),'expected_comparisons':len(selected)*len(scenarios),'last_item':item['item_id'],'last_seconds':value['generation']['seconds']})
     print(json.dumps({'stage':a.stage,'item_id':item['item_id'],'scenario':scenario,'seconds':value['generation']['seconds'],'completed':len(results)}),flush=True)
   if a.stage=='R0':
    report['checks']={'model_loaded':True,'source_hashes_verified':True,'mask_exhaustion':all(v['generation']['mask_count']==0 for v in results),'nfe_consistent':all(v['generation']['nfe']==cfg['generation']['steps'] for v in results),'output_present':all(bool(v['generation']['final_text'].strip()) for v in results)}
   else:
    mapping={'final_tokens_exact':'final_token_ids','final_text_exact':'final_text','answer_exact':'final_answer','correctness_exact':'correct','schedule_exact':'schedule','nfe_exact':'nfe','rng_exact':'rng_end_sha256'}
    report['checks']={out:all(v['equivalence'][key] for v in results) for out,key in mapping.items()}
    report['checks']['snapshot_grid_complete']=all(v['snapshot_grid_complete'] for v in results)
    replay=[row for v in results for row in v.get('native_replay_checks',[])]
    report['native_replay_status']='PASS' if replay and all(all(r[k] for k in ['tokens_exact','nfe_exact','mask_exhausted']) for r in replay) else 'NOT_VALIDATED'
   report['timing']={'mean_seconds_per_base':sum(v['generation']['seconds'] for v in results)/len(results),'max_gpu_peak_bytes':max(v['generation']['gpu_peak_bytes'] for v in results),'item_count':len(selected),'total_item_output_bytes':sum(p.stat().st_size for p in stage_dir.glob('item-*.json'))}
  report['evidence_files']={str(p.resolve()):file_hash(p) for p in stage_dir.iterdir() if p.is_file() and p.name not in ['gate_report.json','progress.json']}
  report['status']='PASS' if all(report['checks'].values()) else 'NEEDS_REVIEW'
  if report['status']=='PASS':
   errors=validate_gate_report(report)
   if errors:report.update(status='NEEDS_REVIEW',validation_errors=errors)
 except Exception as e:
  report.update(status='NEEDS_REVIEW',error=str(e),traceback=traceback.format_exc())
 finally:
  report['finished_at']=datetime.datetime.now(datetime.timezone.utc).isoformat();atomic_json(stage_dir/'gate_report.json',report)
 print(json.dumps({'gate':a.stage,'status':report['status'],'error':report.get('error')}),flush=True)
 return 0 if report['status']=='PASS' else 2
if __name__=='__main__':raise SystemExit(main())
