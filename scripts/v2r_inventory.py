#!/usr/bin/env python3
"""Read-only cluster inventory. Never allocates GPUs or mutates a remote repo."""
from __future__ import annotations
import argparse, concurrent.futures, datetime as dt, json, os, re, shlex, subprocess, tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
HOSTS = {'server1': 'kimhj@10.0.12.120', 'server2': 'kimhj@10.0.12.121', 'server3': None, 'server4': 'kimhj@10.0.12.163'}
NODES = {'server1': 'devbox', 'server2': 'server2', 'server3': 'ubuntu', 'server4': 'server4'}
HISTORICAL_JOBS = ['50668','50669','50738','50752','50753','50754','50923','50924','49256']
# Absolute values use statvfs available bytes (unprivileged reserve excluded).
PROBE = r'''
import csv,glob,io,json,os,socket,subprocess
from pathlib import Path
def cmd(args):
 try:
  p=subprocess.run(args,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=15)
  return {'returncode':p.returncode,'stdout':p.stdout.strip(),'stderr':p.stderr.strip()}
 except Exception as e:return {'returncode':-1,'stderr':str(e),'stdout':''}
fs=[]
for path in ['/','/home','/data','/tmp','/var/tmp','/mnt/raid5']:
 if not os.path.exists(path):continue
 v=os.statvfs(path);total=v.f_blocks*v.f_frsize;free=v.f_bavail*v.f_frsize;used=(v.f_blocks-v.f_bfree)*v.f_frsize
 fs.append({'path':path,'device':os.stat(path).st_dev,'total_bytes':total,'available_bytes':free,'used_bytes':used,'usage_fraction':used/(used+free) if used+free else 1,'inodes_free':v.f_favail,'inodes_total':v.f_files,'writable':os.access(path,os.W_OK)})
gpu=cmd(['nvidia-smi','--query-gpu=index,name,uuid,memory.total,memory.used,memory.free,utilization.gpu','--format=csv,noheader,nounits'])
gpus=[]
if gpu['returncode']==0:
 for r in csv.reader(io.StringIO(gpu['stdout'])):
  r=[x.strip() for x in r]
  gpus.append(dict(zip(['index','name','uuid','memory_total_mib','memory_used_mib','memory_free_mib','utilization_percent'],r)))
apps=cmd(['nvidia-smi','--query-compute-apps=gpu_uuid,pid,process_name,used_memory','--format=csv,noheader,nounits'])
repos=[]
for parent in ['/home/kimhj','/data/kimhj','/mnt/raid5/kimhj']:
 for path in sorted(glob.glob(parent+'/repairable-state-discovery*')):
  if not os.path.isdir(path):continue
  entry={'path':path,'realpath':os.path.realpath(path)}
  if os.path.exists(path+'/.git'):
   entry['head']=cmd(['git','-C',path,'rev-parse','HEAD'])
   entry['worktrees']=cmd(['git','-C',path,'worktree','list','--porcelain'])
  repos.append(entry)
print(json.dumps({'hostname':socket.gethostname(),'cpu_count':os.cpu_count(),'memory':cmd(['free','-b']),'filesystems':fs,'gpus':gpus,'gpu_query':gpu,'gpu_processes':apps,'own_processes':cmd(['ps','-u','kimhj','-o','pid,ppid,etime,comm']),'repos':repos,'mounts':cmd(['findmnt','-J','-o','TARGET,SOURCE,FSTYPE'])}))
'''
def run(args,timeout=40):
    try:
        p=subprocess.run(args,text=True,capture_output=True,timeout=timeout)
        return {'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
    except Exception as e:return {'returncode':-1,'stdout':'','stderr':str(e)}
def atomic_json(path,data):
    path.parent.mkdir(parents=True,exist_ok=True)
    fd,tmp=tempfile.mkstemp(prefix='.'+path.name,dir=path.parent)
    with os.fdopen(fd,'w') as f:
        json.dump(data,f,indent=2,sort_keys=True); f.write('\n'); f.flush(); os.fsync(f.fileno())
    os.replace(tmp,path)
def inspect(server):
    host=HOSTS[server]
    args=['python3','-c',PROBE] if host is None else ['ssh','-o','BatchMode=yes','-o','ConnectTimeout=7',host,'python3 -c '+shlex.quote(PROBE)]
    r=run(args,75)
    result={'server':server,'node':NODES[server],'ssh_host':host,'observed':r['returncode']==0}
    if result['observed']:
        try:result.update(json.loads(r['stdout']))
        except ValueError:result.update(observed=False,error=r)
    else:result['error']=r
    result['slurm_node']=run(['scontrol','show','node',NODES[server],'-o'])
    return server,result

def _field(raw, key):
    """Extract a simple scontrol field without treating command text as a key."""
    m=re.search(rf'(?m)(?:^|\s){re.escape(key)}=([^\s]+)', raw or '')
    return m.group(1) if m else None

def discover_kimhj_jobs():
    """Scheduler source of truth for every current kimhj job, including unknown jobs."""
    listing=run(['squeue','-u','kimhj','-h','-o','%i|%u|%T|%M|%l|%D|%N|%b|%j'])
    jobs=[]
    for line in listing.get('stdout','').splitlines():
        parts=line.split('|',8)
        if len(parts)<9: continue
        jid,user,state,elapsed,limit,nodes,nodelist,tres,name=parts
        raw=run(['scontrol','show','job','-dd',jid],timeout=25)
        text=raw.get('stdout','')
        meta={
            'job_id':jid,'user':user,'job_name':name,'state':state,'elapsed':elapsed,
            'time_limit':limit,'nodes':nodes,'node_list':nodelist,'tres':tres,
            'scontrol_returncode':raw.get('returncode'),
            'workdir':_field(text,'WorkDir'),'command':_field(text,'Command'),
            'stdout':_field(text,'StdOut'),'stderr':_field(text,'StdErr'),
            'partition':_field(text,'Partition'),'qos':_field(text,'QOS'),
            'gres':_field(text,'JOB_GRES'),'dependency':_field(text,'Dependency'),
            'scontrol_raw':text,
        }
        acct=run(['sacct','-n','-P','-X','-j',jid,'--format=JobID,State,Elapsed,Start,End,NodeList,AllocTRES,ExitCode'],timeout=25)
        meta['accounting']=acct
        stat=run(['sstat','-j',jid+'.batch','--format=JobID,MaxRSS,AveRSS,AveCPU,MaxDiskRead,MaxDiskWrite'],timeout=20)
        meta['sstat']=stat
        low=(name+' '+(meta.get('command') or '')+' '+(meta.get('workdir') or '')).lower()
        if jid.startswith('526') or 'v2r-' in name or 'v2r_reference' in low:
            cls='KEEP_REFERENCE_CRITICAL'
        elif jid in HISTORICAL_JOBS or any(k in low for k in ('full_diffusion','v2-50752','v2_50752','repair_bm_')):
            cls='CANCEL_LEGACY_FOR_REFERENCE_REALLOCATION'
        elif user=='kimhj':
            cls='UNKNOWN_NEEDS_FORENSIC'
        else:
            cls='KEEP_UNRELATED'
        meta['classification']=cls
        jobs.append(meta)
    recent=run(['sacct','-u','kimhj','--starttime=2026-09-17','-X','-n','-P','--format=JobID,JobName,State,Elapsed,Start,End,NodeList,AllocTRES,ExitCode'],timeout=35)
    return {'timestamp':dt.datetime.now(dt.timezone.utc).isoformat(),'active_or_pending':jobs,
            'squeue':listing,'recent_accounting':recent,'historical_job_ids':HISTORICAL_JOBS,
            'source_of_truth':['squeue -u kimhj','scontrol show job -dd','sacct','sstat']}

def collect(output):
    now=dt.datetime.now(dt.timezone.utc).isoformat()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        servers=dict(pool.map(inspect,HOSTS))
    job_inventory=discover_kimhj_jobs()
    inventory={'schema_version':'v2r.inventory.2','timestamp':now,'critical_usage_fraction':0.95,'minimum_safety_margin_bytes':50*1024**3,'servers':servers,
      'slurm_jobs':run(['squeue','-h','-o','%i|%u|%T|%M|%l|%D|%N|%b|%j']),
      'job_inventory_summary':{'active_or_pending_count':len(job_inventory['active_or_pending']),
                               'classifications':{c:sum(x['classification']==c for x in job_inventory['active_or_pending']) for c in ['KEEP_REFERENCE_CRITICAL','KEEP_UNRELATED','CANCEL_LEGACY_FOR_REFERENCE_REALLOCATION','UNKNOWN_NEEDS_FORENSIC']}},
      'historical_jobs':run(['sacct','-n','-P','-j',','.join(HISTORICAL_JOBS),'--format=JobID,State,Elapsed,Timelimit,NodeList,AllocTRES,ExitCode']),
      'protected_monitor':run(['tmux','list-panes','-a','-F','#{session_name}|#{pane_pid}|#{pane_current_command}'])}
    for s in servers.values():
        processes=s.get('gpu_processes',{}).get('stdout','')
        # Candidate is not an allocation. Submit must additionally obtain exclusive Slurm GRES.
        s['idle_gpu_candidates']=[g['index'] for g in s.get('gpus',[]) if int(g['memory_used_mib'])<128 and int(g['utilization_percent'])==0 and g['uuid'] not in processes]
        s['safe_filesystem_candidates']=[f['path'] for f in s.get('filesystems',[]) if f['usage_fraction']<0.95 and f['available_bytes']>=50*1024**3 and f['inodes_free']>10000 and f['writable']]
        s['new_scientific_jobs_eligible']=bool(s['observed'] and s['idle_gpu_candidates'] and s['safe_filesystem_candidates'])
    atomic_json(output/'cluster_inventory.json',inventory)
    atomic_json(output/'job_inventory.json',job_inventory)
    lines=['# V2R cluster inventory','',now,'','Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.','', '| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |','|---|---|---|---|']
    for name,s in servers.items():
        lines.append(f"| {name} | {s['observed']} | {s['idle_gpu_candidates']} | {s['safe_filesystem_candidates']} |")
        for f in s.get('filesystems',[]):lines.append(f"\n{name} `{f['path']}`: {f['available_bytes']} available bytes; {f['usage_fraction']:.2%} used; {f['inodes_free']} free inodes.")
    lines+=['','server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.']
    (output/'cluster_inventory.md').write_text('\n'.join(lines)+'\n')
    return inventory
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=ROOT/'status/v2r');a=p.parse_args()
    result=collect(a.output)
    print(json.dumps({s:{k:v[k] for k in ['observed','idle_gpu_candidates','safe_filesystem_candidates','new_scientific_jobs_eligible']} for s,v in result['servers'].items()},indent=2))
