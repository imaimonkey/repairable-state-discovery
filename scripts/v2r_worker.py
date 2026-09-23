#!/usr/bin/env python3
import argparse,importlib,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from repairable_diffusion.src.v2r.artifacts import read_json,verify_execution_checkout,run_worker
p=argparse.ArgumentParser();p.add_argument('--manifest',type=Path,required=True);p.add_argument('--shard',type=int,required=True);p.add_argument('--run-dir',type=Path,required=True);p.add_argument('--gates',type=Path,required=True);a=p.parse_args()
m=read_json(a.manifest);verify_execution_checkout(ROOT,m);module,function=m['executor'].split(':');executor=getattr(importlib.import_module(module),function)
print(json.dumps(run_worker(m,a.shard,a.run_dir,executor,gates=read_json(a.gates)),sort_keys=True))
