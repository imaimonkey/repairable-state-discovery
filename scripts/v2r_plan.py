#!/usr/bin/env python3
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from repairable_diffusion.src.v2r.artifacts import atomic_json,read_json
from repairable_diffusion.src.v2r.planning import make_plan
p=argparse.ArgumentParser();p.add_argument('--spec',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();m=make_plan(read_json(a.spec))
if a.output.exists() and read_json(a.output)!=m:raise ValueError('Refusing manifest overwrite')
atomic_json(a.output,m);print(json.dumps({'run_id':m['run_id'],'run_fingerprint':m['run_fingerprint'],'shards':len(m['shards']),'seed_contexts':m['seed_registry']['context_count']}))
