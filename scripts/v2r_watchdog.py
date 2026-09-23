#!/usr/bin/env python3
"""Keep the observer and single execution authority alive without submitting work."""
from __future__ import annotations
import argparse, datetime as dt, json, os, subprocess, time
from pathlib import Path
from v2r_inventory import atomic_json

ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'status/v2r'; PY='/data/kimhj/llada8b_basic/.venv/bin/python'

def read(path,default=None):
 try:return json.loads(Path(path).read_text())
 except (FileNotFoundError,json.JSONDecodeError,OSError):return default

def has_session(name):
 return subprocess.run(['tmux','has-session','-t',name],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode==0

def start(name,command):
 if not has_session(name):
  subprocess.Popen(['tmux','new-session','-d','-s',name,command],start_new_session=True)

def cycle():
 now=dt.datetime.now(dt.timezone.utc)
 if not has_session('iclr2027-unified-monitor'):
  start('iclr2027-unified-monitor',f'cd {ROOT} && exec {PY} scripts/v2r_unified_monitor.py --interval 90')
 if not has_session('iclr2027-reference-orchestrator'):
  start('iclr2027-reference-orchestrator',f'cd {ROOT} && exec {PY} scripts/v2r_orchestrator.py')
 health={'schema_version':'v2r.watchdog_health.1','status':'RUNNING','timestamp':now.isoformat(),'pid':os.getpid(),'tmux':'iclr2027-reference-watchdog','monitor_session_alive':has_session('iclr2027-unified-monitor'),'orchestrator_session_alive':has_session('iclr2027-reference-orchestrator'),'monitor_health':read(OUT/'monitor_health.json',{}),'orchestrator_health':read(OUT/'orchestrator_health.json',{})}
 atomic_json(OUT/'watchdog_health.json',health)

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--interval',type=int,default=120);ap.add_argument('--once',action='store_true');a=ap.parse_args()
 while True:
  try:cycle()
  except Exception as e:atomic_json(OUT/'watchdog_health.json',{'status':'DEGRADED_RETRY','timestamp':dt.datetime.now(dt.timezone.utc).isoformat(),'error':str(e)})
  if a.once:break
  time.sleep(max(60,a.interval))

if __name__=='__main__':main()
