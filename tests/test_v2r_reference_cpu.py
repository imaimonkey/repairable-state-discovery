import copy,json,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
import torch
from types import SimpleNamespace
from repairable_diffusion.src.v2r.reference_sampler import instrument_llada,rng_state,set_seed
from repairable_diffusion.src.v2r.reference_sources import import_file,OfficialEvaluator,ensure_sources
from repairable_diffusion.src.v2r.seeds import build_seed_registry
from repairable_diffusion.src.v2r.schema import ContractError
from repairable_diffusion.src.v2r.planning import map_checkpoints,select_budget
SOURCE=Path('/var/tmp/kimhj-v2r-reference/upstream/llada/generate.py')
class Fake(torch.nn.Module):
 def __init__(self):super().__init__();self.device=torch.device('cpu');self.config=SimpleNamespace(_name_or_path='fixture')
 def forward(self,x,attention_mask=None):
  ids=torch.arange(64).view(1,1,64);pos=torch.arange(x.shape[1]).view(1,-1,1)
  logits=-((ids-(pos+x.sum()%17)%61).float()**2)/20
  logits=logits.expand(x.shape[0],-1,-1).clone();logits[:,:,63]=-1000
  return SimpleNamespace(logits=logits)
class ReferenceCPU(unittest.TestCase):
 def test_actual_upstream_ast_instrumentation_and_resume(self):
  model=Fake();prompt=torch.tensor([[1,2]]);cfg=dict(steps=16,gen_length=16,block_length=8,temperature=.6,mask_id=63)
  native=import_file(SOURCE,'fixture_pinned_source').generate
  set_seed(123);expected=native(model,prompt,**cfg);expected_rng=rng_state();saved=[]
  def observe(v):
   if v['num_block']==0 and v['i']==3:
    saved.append({'x':v['x'].clone(),'plan':v['num_transfer_tokens'].clone(),'block_index':0,'step_in_block':4,'rng':rng_state()})
  set_seed(123);actual=instrument_llada(SOURCE,observe)(model,prompt,**cfg)
  self.assertTrue(torch.equal(expected,actual));self.assertEqual(expected_rng,rng_state());self.assertEqual(len(saved),1)
  from repairable_diffusion.src.v2r.reference_sampler import restore_rng
  state=saved[0];restore_rng(state['rng']);resumed=instrument_llada(SOURCE,lambda x:None,state)(model,prompt,**cfg)
  self.assertTrue(torch.equal(expected,resumed));self.assertEqual(expected_rng,rng_state())
 def test_seed_pairing_and_detected_collision(self):
  base=dict(stage='r3_core',purpose='localization',item_id='1',trajectory_id=0,checkpoint=63,branch=0,rng_role='future',paired_rng_group='matched')
  contexts=[dict(base,operator=x) for x in ['continuation','repair']]
  contexts.append(dict(base,operator='repair',purpose='confirmation'))
  reg=build_seed_registry(contexts,design_seed=20260923,scope='fixture');self.assertEqual(reg['unique_seed_count'],2)
  with patch('repairable_diffusion.src.v2r.seeds.seed_for_group',return_value=1):
   with self.assertRaises(ContractError):build_seed_registry(contexts,design_seed=20260923,scope='fixture')
 def test_active_phase_mapping(self):
  self.assertEqual(map_checkpoints(512,[x for x in range(1,512) if x%64], [.125,.5,.875])[0]['step'],63)
 def test_reset_budget64_and32(self):
  args=dict(seconds_per_item=100,bytes_per_item=1000,available_gpu_hours=70,deadline_hours=70,gpu_count=2,free_bytes=1000000000000,safety_margin_bytes=50000000000,filesystem_used_fraction=.8,pilot_item_count=16,failed_pool_size=300)
  self.assertEqual(select_budget(backbone='llada',purpose='core',**args)['selected_n'],64)
  self.assertEqual(select_budget(backbone='llada',purpose='temporal',**args)['selected_n'],32)
  self.assertEqual(select_budget(backbone='dream',purpose='core',**args)['selected_n'],32)
if __name__=='__main__':unittest.main()
