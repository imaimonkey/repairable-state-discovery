#!/usr/bin/env python3
"""Separate mechanical PDF validity from scientific submission readiness."""
import argparse,datetime,hashlib,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
 p=argparse.ArgumentParser();p.add_argument('--pdf',type=Path,default=ROOT/'paper/build/main.pdf');p.add_argument('--output',type=Path,default=ROOT/'status/v2r/pdf_audit.json');a=p.parse_args()
 import fitz
 doc=fitz.open(a.pdf);text='\n'.join(page.get_text() for page in doc);meta=doc.metadata
 aux=a.pdf.with_suffix('.aux').read_text();log=a.pdf.with_suffix('.log').read_text()
 match=re.search(r'\\newlabel\{main-text-end\}\{\{[^}]*\}\{(\d+)\}',aux);main_pages=int(match[1]) if match else None
 checks={'official_iclr2027_header':'Under review as a conference paper at ICLR 2027' in text,'main_text_within_9_pages':main_pages is not None and main_pages<=9,'anonymous_authors':'Anonymous authors' in text,'empty_pdf_author':not meta.get('author'),'no_identity_paths':not re.search(r'/data/|/home/|kimhj|imaimonkey|mkdirinfinipath',text,re.I),'no_unresolved_references':not re.search(r'There were undefined references|Citation .* undefined|Reference .* undefined',log),'no_parser_question_mark_refs':'??' not in text,'no_todo_markers':not re.search(r'\bTODO\b|\bFIXME\b|\[citation needed\]',text),'ai_use_statement_present':'AI use statement' in text,'nonempty_pages':all(page.get_text().strip() for page in doc),'no_latex_errors':'! LaTeX Error:' not in log}
 scientific={'sealed_llada_math_core':False,'sealed_llada_math_temporal':False,'author_abstract_conclusion_reviewed':False,'openreview_existing_abstract_verified':False}
 report={'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS' if all(checks.values()) else 'FAIL','technical_pdf_audit':'PASS' if all(checks.values()) else 'FAIL','submission_readiness':'BLOCKED','technical_checks':checks,'scientific_readiness':scientific,'main_text_pages':main_pages,'total_pages':len(doc),'pdf_sha256':hashlib.sha256(a.pdf.read_bytes()).hexdigest(),'pdf_metadata':meta,'source_of_page_limit':'https://iclr.cc/Conferences/2027/AuthorGuidelines','note':'Technical PASS does not validate placeholder reference evidence or reserved author prose.'}
 a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2));return 0 if all(checks.values()) else 2
if __name__=='__main__':raise SystemExit(main())
