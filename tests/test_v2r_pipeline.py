import copy,json,tempfile,unittest
from pathlib import Path
from repairable_diffusion.src.v2r.planning import make_plan
from repairable_diffusion.src.v2r.schema import ContractError
from repairable_diffusion.src.v2r.artifacts import run_worker,merge_run

def manifest(items=('a','b')):
 return make_plan(dict(run_id='cpu_fixture',stage='r0_smoke',execution_git_sha='a'*40,design_sha256='b'*64,design_seed=20260923,model={'id':'fixture','revision':'c'*40},dataset={'id':'fixture','revision':'d'*40,'split':'test'},recipe={'fixture':True},config={'fixture':True},item_ids=list(items),executor='tests.fixture:execute',timing={'seconds_per_item':7200,'target_shard_hours':2},seed_plan=[{'purpose':'base','checkpoints':[0],'branches':1,'operators':['reference']}]))
def executor(m,item,d,records):
 (d/'payload.txt').write_text('fixture '+item)
 return {'correct':item=='a','seed_context_ids':[r['context_id'] for r in records],'evidence_kind':'cpu_fixture'}
class Pipeline(unittest.TestCase):
 def test_atomic_resume_merge_and_corruption(self):
  with tempfile.TemporaryDirectory() as temp:
   root=Path(temp)/'v2r_reference'/'fixture';m=manifest()
   run_worker(m,0,root,executor,gates={})
   with self.assertRaises(ContractError):merge_run(m,root,gates={})
   run_worker(m,1,root,executor,gates={})
   result=merge_run(m,root,gates={});self.assertEqual(result['base_report']['reference_trajectory_accuracy'],.5)
   # Completed items are reused without an executor call.
   run_worker(m,0,root,lambda *a: (_ for _ in ()).throw(RuntimeError('must not execute')),gates={})
   next((root/'shards').rglob('payload.txt')).write_text('corrupt')
   with self.assertRaises(ContractError):merge_run(m,root,gates={})
 def test_duplicate_items_fail(self):
  with self.assertRaises(ContractError):manifest(('a','a'))
 def test_missing_actual_context_is_rejected(self):
  with tempfile.TemporaryDirectory() as temp:
   def bad(*args):return {'correct':True,'seed_context_ids':[]}
   with self.assertRaises(ContractError):run_worker(manifest(),0,Path(temp)/'v2r_reference',bad,gates={})
if __name__=='__main__':unittest.main()
