#!/usr/bin/env python3
"""Strict reducers for compact, stage-specific reference evidence bundles."""
from __future__ import annotations
import argparse,csv,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from repairable_diffusion.src.v2r.artifacts import merge_run,read_json,seal_run,atomic_json
from repairable_diffusion.src.v2r.schema import canonical_hash,manifest_binding

def _write_csv(path, fields, rows):
 path.parent.mkdir(parents=True,exist_ok=True)
 with path.open('w',newline='',encoding='utf-8') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)

def reduce_stage(manifest_path,run_dir,gates_path,bundle_dir):
 manifest=read_json(manifest_path); gates=read_json(gates_path); run_dir=Path(run_dir); bundle_dir=Path(bundle_dir)
 aggregate=merge_run(manifest,run_dir,gates=gates)
 binding=manifest_binding(manifest); fp=manifest['run_fingerprint']; rows=[x['result']|{'item_id':x['item_id']} for x in aggregate['items']]
 compact={}; work=run_dir/'compact'; work.mkdir(parents=True,exist_ok=True)
 decoder={'binding':binding,'stage':manifest['stage'],'status':'MEASURED','run_fingerprint':fp,'item_count':len(rows),'execution_git_sha':manifest['execution_git_sha'],'gate_reports_sha256':canonical_hash(gates)}
 atomic_json(work/'decoder_regime_summary.json',decoder);compact['decoder_regime_summary.json']=work/'decoder_regime_summary.json'
 existence=[]
 for r in rows:
  existence.append({'run_fingerprint':fp,'item_id':r['item_id'],'stage':manifest['stage'],'status':'MEASURED','correct':r.get('correct',r.get('confirmed_repairable')),'nfe':r.get('nfe',''),'seconds':r.get('seconds','')})
 _write_csv(work/'existence.csv',['run_fingerprint','item_id','stage','status','correct','nfe','seconds'],existence);compact['existence.csv']=work/'existence.csv'
 if manifest['stage']=='base':
  base=aggregate.get('base_report',{});base.update({'binding':binding,'status':'MEASURED','run_fingerprint':fp})
  atomic_json(work/'base_report.json',base);compact['base_report.json']=work/'base_report.json'
 elif manifest['stage']=='r3_core':
  sel=[]
  for r in rows:
   confirmation=r.get('confirmation') or [{}]; chosen=confirmation[0] if confirmation else {}
   sel.append({'run_fingerprint':fp,'item_id':r['item_id'],'stage':'r3_core','status':'MEASURED','selected_checkpoint':r.get('selected_checkpoint',''),'q_C':chosen.get('q_C',''),'q_R':chosen.get('q_R',''),'Delta_R':chosen.get('Delta_R','')})
  _write_csv(work/'selector_summary.csv',['run_fingerprint','item_id','stage','status','selected_checkpoint','q_C','q_R','Delta_R'],sel);compact['selector_summary.csv']=work/'selector_summary.csv'
 elif manifest['stage']=='temporal':
  temporal=[]
  for r in rows:
   temporal.append({'run_fingerprint':fp,'item_id':r['item_id'],'stage':'temporal','status':'MEASURED','T_last_R':r.get('T_last_R',''),'confirmed_repairable':r.get('confirmed_repairable',''),'native_recoverable':r.get('native_recoverable',''),'never_correct_repairable':r.get('never_correct_repairable','')})
  _write_csv(work/'temporal_summary.csv',['run_fingerprint','item_id','stage','status','T_last_R','confirmed_repairable','native_recoverable','never_correct_repairable'],temporal);compact['temporal_summary.csv']=work/'temporal_summary.csv'
 else: raise ValueError('No reducer for stage '+manifest['stage'])
 seal=seal_run(manifest,run_dir,bundle_dir,gates=gates,compact_artifacts=compact)
 return {'status':seal['status'],'bundle':str(bundle_dir),'manifest':str(manifest_path),'stage':manifest['stage'],'item_count':len(rows)}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--manifest',type=Path,required=True);ap.add_argument('--run-dir',type=Path,required=True);ap.add_argument('--gates',type=Path,required=True);ap.add_argument('--bundle',type=Path,required=True);a=ap.parse_args();print(json.dumps(reduce_stage(a.manifest,a.run_dir,a.gates,a.bundle),sort_keys=True))
if __name__=='__main__':main()
