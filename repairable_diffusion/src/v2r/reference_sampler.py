"""Pinned source-native generation with passive snapshots and faithful resumes.

LLaDA instrumentation inserts a callback after its exact token assignment; the
upstream arithmetic and sampling are unchanged. Dream uses its official hooks.
GPU equivalence reports, not this construction alone, authorize scientific use.
"""
from __future__ import annotations
import ast, copy, hashlib, json, random, time
from pathlib import Path
from typing import Any
import numpy as np
import torch
from transformers import AutoModel, AutoTokenizer
from .schema import CHECKPOINT_GRID, canonical_hash
from .planning import map_checkpoints
from .reference_sources import ensure_sources, import_file, native_messages, OfficialEvaluator, bridge_evaluate


def rng_state():
    return {'cpu':torch.get_rng_state().tolist(), 'cuda':[x.tolist() for x in torch.cuda.get_rng_state_all()] if torch.cuda.is_available() else []}

def restore_rng(state):
    torch.set_rng_state(torch.tensor(state['cpu'],dtype=torch.uint8))
    if state['cuda']:torch.cuda.set_rng_state_all([torch.tensor(x,dtype=torch.uint8) for x in state['cuda']])

def set_seed(seed):
    random.seed(seed); torch.manual_seed(seed)
    if torch.cuda.is_available():torch.cuda.manual_seed_all(seed)


def instrument_llada(source: Path, callback, resume=None):
    """Only additive callback + explicit resume control flow in a separate function."""
    module=import_file(source,'v2r_pinned_llada_'+hashlib.sha256(source.read_bytes()).hexdigest()[:12])
    tree=ast.parse(source.read_text()); fn=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='generate')
    callback_count=0
    class Observer(ast.NodeTransformer):
        def visit_Assign(self,node):
            nonlocal callback_count
            self.generic_visit(node)
            if len(node.targets)==1 and ast.unparse(node.targets[0])=='x[transfer_index]':
                callback_count+=1
                return [node,ast.parse('_v2r_observe(locals())').body[0]]
            return node
    fn=Observer().visit(fn)
    if callback_count!=1:raise ValueError('Pinned sampler assignment signature changed')
    if resume is not None:
        outer=next(n for n in fn.body if isinstance(n,ast.For) and isinstance(n.target,ast.Name) and n.target.id=='num_block')
        at=fn.body.index(outer)
        fn.body[at:at]=ast.parse('x = _v2r_resume_x.clone()').body
        outer.iter=ast.parse('range(_v2r_resume_block, num_blocks)',mode='eval').body
        for n in outer.body:
            if isinstance(n,ast.For) and isinstance(n.target,ast.Name) and n.target.id=='i':
                n.iter=ast.parse('range(_v2r_resume_step if num_block == _v2r_resume_block else 0, steps)',mode='eval').body
        plan_idx=next(i for i,n in enumerate(outer.body) if isinstance(n,ast.Assign) and ast.unparse(n.targets[0])=='num_transfer_tokens')
        outer.body[plan_idx+1:plan_idx+1]=ast.parse('if num_block == _v2r_resume_block:\n    num_transfer_tokens = _v2r_resume_plan.clone()').body
    env=dict(module.__dict__);env['_v2r_observe']=callback
    if resume is not None:
        env.update(_v2r_resume_x=resume['x'],_v2r_resume_block=resume['block_index'],_v2r_resume_step=resume['step_in_block'],_v2r_resume_plan=resume['plan'])
    exec(compile(ast.fix_missing_locations(ast.Module(body=[fn],type_ignores=[])),str(source)+'[v2r_passive]', 'exec'),env)
    return env['generate']


class ReferenceSampler:
    def __init__(self,recipe:dict,task:str,cache:Path,model_cache:Path|None=None,device='cuda'):
        self.recipe,self.task,self.device=recipe,task,device
        self.backbone=recipe['backbone'];self.generation=recipe['tasks'][task]['generation']
        self.sources=ensure_sources(recipe,cache)
        kwargs={'revision':recipe['model_revision'],'trust_remote_code':True,'torch_dtype':torch.bfloat16}
        model_source=recipe['model_id']
        if model_cache:
            snapshot=model_cache/('models--'+recipe['model_id'].replace('/','--'))/'snapshots'/recipe['model_revision']
            if not snapshot.is_dir():raise FileNotFoundError(f'Pinned model snapshot missing: {snapshot}')
            model_source=str(snapshot);kwargs['local_files_only']=True
        self.model=AutoModel.from_pretrained(model_source,**kwargs).to(device).eval()
        self.tokenizer=AutoTokenizer.from_pretrained(model_source,revision=recipe['tokenizer_revision'],trust_remote_code=True,local_files_only=bool(model_cache))
        self.tokenizer.padding_side='left'
        self.official=OfficialEvaluator(self.backbone,task,self.sources)
        steps=self.generation['steps']
        if self.backbone=='llada':
            self.native=import_file(self.sources['generate.py'],'v2r_upstream_llada').generate
            local=steps//(self.generation['gen_length']//self.generation['block_length'])
            valid=[s for s in range(1,steps) if s%local!=0]
        else:valid=list(range(1,steps))
        self.mapping=map_checkpoints(steps,valid,CHECKPOINT_GRID)
        self.checkpoints={r['step'] for r in self.mapping}

    def prompt(self,item):
        messages=native_messages(self.backbone,self.task,item['question'],self.sources)
        rendered=self.tokenizer.apply_chat_template(messages,add_generation_prompt=True,tokenize=False)
        # Mirrors official batch_encode/tokenizer defaults (tokenizers have no extra BOS).
        encoded=self.tokenizer(rendered,return_tensors='pt').to(self.device)
        return rendered,encoded

    def decode(self,tokens,prompt_len):
        if self.backbone=='llada':return self.tokenizer.decode(tokens[0,prompt_len:],skip_special_tokens=True)
        text=self.tokenizer.decode(tokens[0,prompt_len:])
        if self.tokenizer.eos_token:text=text.split(self.tokenizer.eos_token)[0]
        for stop in self.recipe['tasks'][self.task]['official_stop_strings']:text=text.split(stop)[0]
        return text

    def _snapshot(self,x,logits_or_probs,step,prompt_len,*,probabilities=False,extra=None):
        before=rng_state()
        # Only compact token and selected probability state is retained.
        tokens=x.detach().clone(); gen=tokens[0,prompt_len:]
        matrix=logits_or_probs[0,prompt_len:]
        if not probabilities:matrix=torch.softmax(matrix.float(),dim=-1)
        conf=matrix.gather(-1,gen.unsqueeze(-1)).squeeze(-1).detach().cpu().tolist()
        mask=self.recipe['special_token_handling']['mask_id']
        conf=[None if int(t)==mask else float(c) for t,c in zip(gen,conf)]
        state={'step_index':step,'total_steps':self.generation['steps'],'prompt_len':prompt_len,'full_token_ids':tokens[0].cpu().tolist(),'token_confidences':conf,'rng_state':before,'backbone':self.backbone,**(extra or {})}
        if rng_state()!=before:raise RuntimeError('Snapshot callback changed RNG')
        return state

    def generate(self,item,seed,instrumented:bool):
        rendered,encoded=self.prompt(item); prompt_len=encoded.input_ids.shape[1]
        snapshots={}; schedule=[]
        set_seed(seed);start_rng=rng_state();start=time.perf_counter()
        if torch.cuda.is_available():torch.cuda.reset_peak_memory_stats()
        def forward_pre(module,args,kwargs):
            x=args[0] if args else kwargs['input_ids']
            schedule.append({'input_tokens_sha256':canonical_hash(x.detach().cpu().tolist()),'masked_count':int((x==self.recipe['special_token_handling']['mask_id']).sum())})
        handle=self.model.register_forward_pre_hook(forward_pre,with_kwargs=True)
        try:
            with torch.no_grad():
                if self.backbone=='llada':
                    def callback(state):
                        step=state['num_block']*state['steps']+state['i']+1
                        if step in self.checkpoints or step==self.generation['steps']:
                            snapshots[str(step)]=self._snapshot(state['x'],state['p'],step,prompt_len,probabilities=True,extra={'block_index':state['num_block'],'step_in_block':state['i']+1,'active_plan':state['num_transfer_tokens'][0].cpu().tolist(),'steps_per_block':state['steps']})
                    sampler=instrument_llada(self.sources['generate.py'],callback) if instrumented else self.native
                    tokens=sampler(self.model,encoded.input_ids,**self.generation)
                else:
                    kwargs=dict(self.generation)
                    if instrumented:
                        def token_hook(i,x,logits):
                            if i is not None and (i+1 in self.checkpoints or i+1==self.generation['steps']):
                                snapshots[str(i+1)]=self._snapshot(x,logits,i+1,prompt_len)
                            return x
                        kwargs['generation_tokens_hook_func']=token_hook
                    tokens=self.model.diffusion_generate(encoded.input_ids,attention_mask=encoded.attention_mask,**kwargs).sequences
        finally:handle.remove()
        elapsed=time.perf_counter()-start;end_rng=rng_state()
        text=self.decode(tokens,prompt_len); official=self.official.evaluate(text,item);ours=bridge_evaluate(self.task,text,item)
        mask_count=int((tokens[:,prompt_len:]==self.recipe['special_token_handling']['mask_id']).sum())
        return {'item_id':str(item['item_id']),'trajectory_id':0,'seed':seed,'prompt':rendered,'prompt_token_ids':encoded.input_ids[0].cpu().tolist(),'final_token_ids':tokens[0].cpu().tolist(),'final_text':text,'final_answer':ours['answer'],'correct':ours['correct'],'official_evaluation':official,'paper_evaluation':ours,'snapshots':snapshots,'checkpoint_mapping':self.mapping,'schedule':schedule,'nfe':len(schedule),'mask_count':mask_count,'seconds':elapsed,'gpu_peak_bytes':torch.cuda.max_memory_allocated() if torch.cuda.is_available() else 0,'rng_start_sha256':canonical_hash(start_rng),'rng_end_sha256':canonical_hash(end_rng),'evidence_kind':'reference_scientific'}

    def continue_llada(self,item,snapshot,*,seed=None,modified_positions=None):
        if self.backbone!='llada':raise NotImplementedError('Dream continuation requires separate native schedule validation')
        _,encoded=self.prompt(item);device=self.device
        x=torch.tensor(snapshot['full_token_ids'],device=device,dtype=torch.long).unsqueeze(0)
        plan=torch.tensor(snapshot['active_plan'],device=device,dtype=torch.long).unsqueeze(0)
        if modified_positions:
            x[0,[snapshot['prompt_len']+i for i in modified_positions]]=self.generation['mask_id']
            start=snapshot['prompt_len']+snapshot['block_index']*self.generation['block_length'];end=start+self.generation['block_length']
            remaining=snapshot['steps_per_block']-snapshot['step_in_block']
            if remaining<=0:raise ValueError('Cannot reopen completed block')
            module=import_file(self.sources['generate.py'],'v2r_llada_plan')
            plan[:,snapshot['step_in_block']:]=module.get_num_transfer_tokens(x[:,start:end]==self.generation['mask_id'],remaining)
        resume={'x':x,'plan':plan,'block_index':snapshot['block_index'],'step_in_block':snapshot['step_in_block']}
        fn=instrument_llada(self.sources['generate.py'],lambda state:None,resume)
        if seed is None:restore_rng(snapshot['rng_state'])
        else:set_seed(seed)
        count=[];started=time.perf_counter()
        handle=self.model.register_forward_pre_hook(lambda module,args:count.append(1))
        try:
            tokens=fn(self.model,encoded.input_ids,**self.generation)
        finally:handle.remove()
        text=self.decode(tokens,snapshot['prompt_len']);evaluation=bridge_evaluate(self.task,text,item)
        return {'final_token_ids':tokens[0].cpu().tolist(),'final_text':text,'correct':evaluation['correct'],'answer':evaluation['answer'],'nfe':len(count),'seconds':time.perf_counter()-started,'mask_count':int((tokens[:,snapshot['prompt_len']:]==self.generation['mask_id']).sum())}
