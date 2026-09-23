"""Fail-closed validation of measured reference gate evidence."""
from pathlib import Path
from .schema import file_hash

def validate_gate_report(report):
    errors=[]
    if report.get('status')!='PASS':errors.append('status is not PASS')
    if report.get('evidence_kind')!='real_model_reference_gate':errors.append('not a real model gate')
    for field,size in [('execution_git_sha',40),('config_sha256',64),('recipe_sha256',64),('dataset_sha256',64),('seed_registry_sha256',64)]:
        v=report.get(field,'')
        if len(v)!=size or any(c not in '0123456789abcdef' for c in v):errors.append('invalid '+field)
    gate=report.get('gate');checks=report.get('checks',{})
    required={'R0':['model_loaded','source_hashes_verified','mask_exhaustion','nfe_consistent','output_present'],
              'R1':['fixture_tests_pass','same_outputs_dual_evaluated','disagreements_saved','paper_dataset_pinned'],
              'R2':['final_tokens_exact','final_text_exact','answer_exact','correctness_exact','schedule_exact','nfe_exact','rng_exact','snapshot_grid_complete']}
    if gate not in required:errors.append('unknown gate')
    elif any(checks.get(key) is not True for key in required[gate]):errors.append('required measured checks failed')
    if gate=='R0' and report.get('item_count',0)<16:errors.append('R0 requires16items')
    if gate=='R2' and (report.get('item_count',0)<32 or len(report.get('seed_scenarios',[]))<2):errors.append('R2 requires32items and multiple seeds')
    evidence=report.get('evidence_files',{})
    if not evidence:errors.append('missing evidence files')
    for path,digest in evidence.items():
        p=Path(path)
        if not p.is_file() or file_hash(p)!=digest:errors.append('evidence hash mismatch '+path)
    return errors
