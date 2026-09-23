#!/usr/bin/env python3
"""Import only SEALED V2R compact evidence into the reference tables."""
from __future__ import annotations
import datetime as dt, hashlib, json, csv
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BUNDLES=Path('/var/tmp/kimhj-v2r-reference/outputs/v2r_reference/bundles')
OUT=ROOT/'paper/reference_generated/tables'

def read_json(path):
    try:return json.loads(Path(path).read_text())
    except (FileNotFoundError,json.JSONDecodeError):return None

def bundle(name):
    p=BUNDLES/name; seal=read_json(p/'SEALED.json')
    return {'path':p,'sealed':bool(seal and seal.get('status')=='SEALED'),'seal':seal}

def csv_rows(path):
    try:
        with Path(path).open(newline='',encoding='utf-8') as f:return list(csv.DictReader(f))
    except FileNotFoundError:return []

def fmt(v):
    if v in (None,''):return '---'
    try:return f'{float(v):.4f}'
    except (TypeError,ValueError):return str(v).replace('_',r'\_')

def main():
    specs=[('LLaDA','MATH-500','llada_math500_base_finalsha','llada_math500_core_finalsha','llada_math500_temporal_finalsha'),('LLaDA','GSM8K','llada_gsm8k_base_finalsha','llada_gsm8k_core_finalsha','llada_gsm8k_temporal_finalsha'),('Dream','MATH-500','dream_math500_base_finalsha','dream_math500_core_finalsha','dream_math500_temporal_finalsha'),('Dream','GSM8K','dream_gsm8k_base_finalsha','dream_gsm8k_core_finalsha','dream_gsm8k_temporal_finalsha')]
    rows=[];import_hashes={}
    for backbone,task,base_name,core_name,temp_name in specs:
        base,core,temp=map(bundle,(base_name,core_name,temp_name))
        base_report=read_json(base['path']/'base_report.json') if base['sealed'] else None
        existence=csv_rows(base['path']/'existence.csv') if base['sealed'] else []
        temporal=csv_rows(temp['path']/'temporal_summary.csv') if temp['sealed'] else []
        for b in (base,core,temp):
            if b['sealed']:import_hashes[b['path'].name]=hashlib.sha256((b['path']/'SEALED.json').read_bytes()).hexdigest()
        failed=len([r for r in existence if r.get('correct','').lower()=='false']) if existence else None
        native=sum(float(r.get('native_recoverable',0) or 0) for r in temporal)/len(temporal) if temporal else None
        confirmed=sum(float(r.get('confirmed_repairable',0) or 0) for r in temporal)/len(temporal) if temporal else None
        vals=[float(r['T_last_R']) for r in temporal if r.get('T_last_R') not in (None,'')]
        rows.append({'backbone':backbone,'task':task,'accuracy':(base_report or {}).get('reference_trajectory_accuracy'),'failed':failed,'native':native,'confirmed':confirmed,'never':None,'tlast':sum(vals)/len(vals) if vals else None,'base':base['sealed'],'core':core['sealed'],'temporal':temp['sealed']})
    OUT.mkdir(parents=True,exist_ok=True)
    lines=[r'\begin{table}[t]',r'\caption{Reference baseline and independently confirmed repairability. Dashes denote evidence that is not yet sealed.}',r'\label{tab:reference-existence}',r'\centering\scriptsize',r'\resizebox{\linewidth}{!}{\begin{tabular}{llrrrrrr}',r'\toprule',r'Backbone & Task & Accuracy & Failed probed & Native recoverable & Confirmed repairable & Never-correct repairable & $T_{\rm last}^{R}$ \\',r'\midrule']
    for row in rows:
        lines.append(f"{row['backbone']} & {row['task']} & {fmt(row['accuracy'])} & {fmt(row['failed'])} & {fmt(row['native'])} & {fmt(row['confirmed'])} & {fmt(row['never'])} & {fmt(row['tlast'])} " + r'\\')
    lines += [r'\bottomrule',r'\end{tabular}}',r'\end{table}','']
    (OUT/'table1_existence.tex').write_text('\n'.join(lines))
    (OUT/'table2_mechanism.tex').write_text(r'''\begin{table}[t]
\caption{Reference LLaDA mechanism reporting. Unsupported controls remain unreported until sealed.}
\label{tab:reference-mechanism}
\centering\small
\begin{tabular}{lrrrr}
\toprule
Control & Recovery & Harm & Modified positions & NFE \\
\midrule
Matched continuation & --- & --- & --- & --- \\
Canonical repair & --- & --- & --- & --- \\
Random remask & --- & --- & --- & --- \\
CoRe-snapshot & --- & --- & --- & --- \\
Native replay & --- & --- & --- & --- \\
Actual fresh sampling & --- & --- & --- & --- \\
\bottomrule
\end{tabular}
\end{table}
''')
    (OUT/'table3_localization.tex').write_text(r'''\begin{table}[t]
\caption{Prospective reference localization reporting. Unsupported selectors remain unreported until sealed.}
\label{tab:reference-localization}
\centering\scriptsize
\resizebox{\linewidth}{!}{\begin{tabular}{lrrrrrr}
\toprule
Selector & Confirmed recovery & Accuracy change & Harm & Coverage & Oracle gap & NFE \\
\midrule
Frozen OOF state value & --- & --- & --- & --- & --- & --- \\
Predeclared temporal priors & --- & --- & --- & --- & --- & --- \\
Observable confidence & --- & --- & --- & --- & --- & --- \\
Independently confirmed oracle & --- & --- & --- & --- & --- & --- \\
\bottomrule
\end{tabular}}
\end{table}
''')
    facts=['% Generated only from SEALED V2R compact bundles.']
    for prefix,key in [('math','LLaDA/MATH-500'),('gsm','LLaDA/GSM8K')]:
        row=next(x for x in rows if f"{x['backbone']}/{x['task']}"==key)
        for macro,val in [(f'{prefix}BasePassK',row['accuracy']),(f'{prefix}RepairableFailed',row['confirmed']),(f'{prefix}NegativeRepair',row['never']),(f'{prefix}PeakStep',row['tlast'])]:facts.append(f'\\newcommand{{\\{macro}}}{{{fmt(val)}}}')
    (ROOT/'paper/generated/facts.tex').write_text('\n'.join(facts)+'\n')
    state={'schema_version':'v2r.paper_import.1','timestamp':dt.datetime.now(dt.timezone.utc).isoformat(),'status':'SEALED_ONLY_IMPORT','bundles':import_hashes,'rows':rows,'author_review_required':True}
    (ROOT/'status/v2r/reference_import.json').write_text(json.dumps(state,indent=2,sort_keys=True)+'\n')
    print(json.dumps(state,sort_keys=True))

if __name__=='__main__':main()
