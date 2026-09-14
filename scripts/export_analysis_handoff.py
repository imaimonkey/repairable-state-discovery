#!/usr/bin/env python3
from __future__ import annotations

import argparse, hashlib, json, os, shutil, socket, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

TEXT_SUFFIXES={'.json','.yaml','.yml','.md','.txt','.csv','.tsv'}
HINTS=('analysis','report','summary','metric','manifest','provenance','config','state','receipt','evaluation','eval')
ENV_KEYS=('SLURM_JOB_ID','SLURM_ARRAY_JOB_ID','SLURM_ARRAY_TASK_ID','SLURM_JOB_NAME','SLURM_JOB_PARTITION','SLURM_JOB_NODELIST','SLURM_JOB_GPUS','CUDA_VISIBLE_DEVICES','NVIDIA_VISIBLE_DEVICES')

def cmd(args,cwd):
    try:
        p=subprocess.run(args,cwd=cwd,text=True,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,check=False,timeout=20)
        return p.stdout.strip() if p.returncode==0 else None
    except (OSError,subprocess.TimeoutExpired): return None

def git(root,*args): return cmd(['git',*args],root)
def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''): h.update(chunk)
    return h.hexdigest()
def rel(path,root):
    if path is None:return None
    try:return str(path.resolve().relative_to(root.resolve()))
    except ValueError:return str(path.resolve())
def write_json(path,payload):
    path.parent.mkdir(parents=True,exist_ok=True);tmp=path.with_suffix(path.suffix+'.tmp');tmp.write_text(json.dumps(payload,indent=2,ensure_ascii=False,sort_keys=True),encoding='utf-8');os.replace(tmp,path)
def write_text(path,text):
    path.parent.mkdir(parents=True,exist_ok=True);tmp=path.with_suffix(path.suffix+'.tmp');tmp.write_text(text,encoding='utf-8');os.replace(tmp,path)
def latest(root):
    if not root.exists():return None
    rows=[root]+([p for p in root.iterdir() if not p.name.startswith('.')] if root.is_dir() else [])
    return max(rows,key=lambda p:p.stat().st_mtime,default=None)
def resolve_run(explicit,roots,repo):
    if explicit:
        p=Path(explicit).expanduser();p=p if p.is_absolute() else repo/p
        if p.exists():return p.resolve()
    rows=[]
    for value in roots:
        p=Path(value).expanduser();p=p if p.is_absolute() else repo/p;q=latest(p)
        if q is not None:rows.append(q)
    return max(rows,key=lambda p:p.stat().st_mtime,default=None)
def find_named(root,names):
    if root is None or not root.exists():return None
    if root.is_file():return root if root.name in names else None
    for n in names:
        p=root/n
        if p.is_file():return p
    rows=[]
    for n in names:rows.extend(root.rglob(n))
    return max(rows,key=lambda p:p.stat().st_mtime,default=None)
def resolve_file(explicit,run,repo,names):
    if explicit:
        p=Path(explicit).expanduser();p=p if p.is_absolute() else repo/p
        if p.is_file():return p.resolve()
    return find_named(run,names)
def load_json(path):
    if path is None or not path.is_file() or path.stat().st_size>8*1024*1024:return None
    try:return json.loads(path.read_text(encoding='utf-8'))
    except (OSError,UnicodeDecodeError,json.JSONDecodeError):return None
def metrics(payload):
    if not isinstance(payload,dict):return {}
    keys=('metrics','summary','headline','comparisons','selector_deltas','repairability_summary','compute_matching','research','dataset','predictive','error_detection','within_bin','run')
    out={k:payload[k] for k in keys if k in payload}
    if out:return out
    return {k:v for k,v in payload.items() if isinstance(v,(str,int,float,bool)) or v is None}
def files(run):
    if run is None or not run.exists():return []
    if run.is_file():return [run]
    return sorted((p for p in run.rglob('*') if p.is_file()),key=lambda p:str(p))
def copy_name(path,run):
    if run is not None and run.is_dir():
        try:return '__'.join(path.relative_to(run).parts)
        except ValueError:pass
    return path.name
def tail(path,n):
    if path is None or not path.is_file():return ''
    try:lines=path.read_text(encoding='utf-8',errors='replace').splitlines()
    except OSError:return ''
    return '\n'.join(lines[-n:])+('\n' if lines else '')
def logs(repo,out_arg,err_arg):
    def one(v):
        if not v:return None
        p=Path(v).expanduser();p=p if p.is_absolute() else repo/p
        return p if p.is_file() else None
    out,err=one(out_arg),one(err_arg);job=os.environ.get('SLURM_JOB_ID');root=repo/'logs'
    if not job or not root.exists():return out,err
    rows=[p for p in root.rglob('*') if p.is_file() and job in p.name]
    if out is None:out=max([p for p in rows if p.suffix in {'.out','.log'} or 'out' in p.name.lower()],key=lambda p:p.stat().st_mtime,default=None)
    if err is None:err=max([p for p in rows if p.suffix=='.err' or 'err' in p.name.lower()],key=lambda p:p.stat().st_mtime,default=None)
    return out,err

def export(a):
    repo=Path(a.repo_root).expanduser().resolve();dest=Path(a.dest);dest=dest if dest.is_absolute() else repo/dest
    run=resolve_run(a.run_dir,a.candidate_root,repo)
    analysis=resolve_file(a.analysis_source,run,repo,('analysis.json','report.json','protocol_report.json','run_summary.json','final_state_summary.json','paper_final_summary.json'))
    metric_src=resolve_file(a.metrics_source,run,repo,('metrics.json','run_summary.json','analysis.json','report.json','protocol_report.json'))
    current=git(repo,'rev-parse','HEAD');source=os.environ.get('HANDOFF_SOURCE_GIT_SHA') or current;branch=git(repo,'branch','--show-current');remote=git(repo,'remote','get-url','origin');status=git(repo,'status','--porcelain=v1') or ''
    analysis_payload=load_json(analysis);metric_payload=load_json(metric_src);metric_payload=metric_payload if metric_payload is not None else analysis_payload
    tmp=dest.parent/f'.{dest.name}.tmp-{os.getpid()}';shutil.rmtree(tmp,ignore_errors=True);(tmp/'artifacts').mkdir(parents=True,exist_ok=True)
    index=[];copied=0
    for p in files(run):
        try:size=p.stat().st_size
        except OSError:continue
        entry={'path':rel(p,repo),'size_bytes':size,'sha256':sha(p) if size<=a.max_hash_bytes else None,'hash_omitted_reason':None if size<=a.max_hash_bytes else 'file_too_large','copied_as':None}
        if copied<a.max_copied_files and size<=a.max_copy_bytes and p.suffix.lower() in TEXT_SUFFIXES and any(h in p.name.lower() for h in HINTS):
            t=tmp/'artifacts'/copy_name(p,run);shutil.copyfile(p,t);entry['copied_as']=str(t.relative_to(tmp));copied+=1
        index.append(entry)
    manifest={'schema_version':1,'created_at_utc':datetime.now(timezone.utc).isoformat(),'repo':a.repo_name or repo.name,'source_git_sha':source,'current_git_sha_at_export':current,'branch':branch,'remote':remote,'worktree_dirty_at_export':bool(status),'worktree_status_at_export':status.splitlines(),'source_worktree_dirty':os.environ.get('HANDOFF_SOURCE_GIT_DIRTY'),'run_path':rel(run,repo),'analysis_source':rel(analysis,repo),'metrics_source':rel(metric_src,repo),'command':a.command or os.environ.get('HANDOFF_COMMAND'),'exit_code':a.exit_code,'status':a.status or ('completed' if a.exit_code==0 else 'failed'),'runtime':{'hostname':socket.gethostname(),'python':sys.version,'cwd':os.getcwd()},'environment':{k:os.environ[k] for k in ENV_KEYS if k in os.environ}}
    write_json(tmp/'manifest.json',manifest);write_json(tmp/'metrics.json',metrics(metric_payload));write_json(tmp/'analysis_summary.json',{'source':rel(analysis,repo),'payload':analysis_payload});write_json(tmp/'artifact_index.json',{'artifacts':index})
    outlog,errlog=logs(repo,a.stdout_log,a.stderr_log);write_text(tmp/'stdout_tail.txt',tail(outlog,a.log_tail_lines));write_text(tmp/'stderr_tail.txt',tail(errlog,a.log_tail_lines))
    write_text(tmp/'summary.md','\n'.join(['# Latest experiment handoff','',f"- Repository: `{manifest['repo']}`",f"- Source commit: `{source or 'unknown'}`",f"- Branch: `{branch or 'unknown'}`",f"- Status: **{manifest['status']}** (exit code {a.exit_code})",f"- Slurm job: `{os.environ.get('SLURM_JOB_ID','not-recorded')}`",f"- Run path: `{manifest['run_path'] or 'not-resolved'}`",f"- Analysis source: `{manifest['analysis_source'] or 'not-resolved'}`",'', 'This directory is intentionally Git-trackable. Commit/push it after the run so remote analysis can reconstruct code provenance, metrics, artifact inventory, and scheduler logs without committing large raw artifacts.','']))
    dest.parent.mkdir(parents=True,exist_ok=True);shutil.rmtree(dest,ignore_errors=True);os.replace(tmp,dest);return dest

def parse():
    p=argparse.ArgumentParser();p.add_argument('--repo-root',default=str(Path(__file__).resolve().parent.parent));p.add_argument('--repo-name',default='');p.add_argument('--dest',default='reports/latest_run');p.add_argument('--run-dir',default='');p.add_argument('--candidate-root',action='append',default=[]);p.add_argument('--analysis-source',default='');p.add_argument('--metrics-source',default='');p.add_argument('--stdout-log',default='');p.add_argument('--stderr-log',default='');p.add_argument('--command',default='');p.add_argument('--status',default='');p.add_argument('--exit-code',type=int,default=0);p.add_argument('--log-tail-lines',type=int,default=400);p.add_argument('--max-copy-bytes',type=int,default=2*1024*1024);p.add_argument('--max-hash-bytes',type=int,default=64*1024*1024);p.add_argument('--max-copied-files',type=int,default=30);return p.parse_args()
if __name__=='__main__':print(f'[analysis-handoff] wrote {export(parse())}')
