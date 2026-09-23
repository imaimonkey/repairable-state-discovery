#!/usr/bin/env python3
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from repairable_diffusion.src.v2r.artifacts import read_json,merge_run
p=argparse.ArgumentParser();p.add_argument('--manifest',type=Path,required=True);p.add_argument('--run-dir',type=Path,required=True);p.add_argument('--gates',type=Path,required=True);a=p.parse_args()
try:
 r=merge_run(read_json(a.manifest),a.run_dir,gates=read_json(a.gates));print(json.dumps({'status':r['status'],'item_count':r['item_count']}))
except Exception as e:print(json.dumps({'status':'AGGREGATION_BLOCKED','error':str(e)}));raise
