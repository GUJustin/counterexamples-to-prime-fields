import json,itertools
from pathlib import Path
from collections import Counter
P=Path('research/hadamard_locator_family');d=json.loads((P/'design_gate.json').read_text());H=frozenset(d['L8_blocks_as_masks'][:14]);K=frozenset(d['L8_blocks_as_masks'][14:])
def act(B,p):return sum(1<<p[i]for i in range(8)if B>>i&1)
G=[];copies={}
for p in itertools.permutations(range(8)):
 h=frozenset(act(B,p)for B in H);copies.setdefault(h,p)
 if h==H:G.append(p)
common=[p for p in G if frozenset(act(B,p)for B in K)==K]
def order(p):
 t=tuple(range(8));q=t
 for n in range(1,100):
  q=tuple(p[q[i]]for i in range(8))
  if q==t:return n
def orbits(S,group,action):
 S=set(S);r=[]
 while S:
  x=min(S);o={action(x,p)for p in group};r.append(sorted(o));S-=o
 return r
ocs=orbits(copies,G,lambda h,p:frozenset(act(B,p)for B in h))
out={'AGL_order':len(G),'double_cosets':[{'copies':len(o),'intersection':len(H&o[0])}for o in ocs], 'common_group_order':len(common),'common_orders':dict(Counter(map(order,common))),'candidate_orbits':orbits(range(8),common,lambda i,p:p[i]),'block_orbits':orbits(H|K,common,act),'common_group':common}
(P/'groups.json').write_text(json.dumps(out,indent=2));print({k:v for k,v in out.items()if k!='common_group'})
U=H|K;full=[]
for p in itertools.permutations(range(8)):
 if all(act(B,p)in U for B in U):full.append(p)
cc=Counter((order(p),sum(act(B,p)==B for B in U))for p in full)
out['full_union_group']=full
out['union_order_fixed_histogram']=[{'order':a,'fixed_nodes':b,'count':c}for(a,b),c in sorted(cc.items())]
assert len(full)==336
assert all(sum(p[i]==i for i in range(8))==2 for p in full if order(p)==2 and sum(act(B,p)==B for B in U)==0)
(P/'groups.json').write_text(json.dumps(out,indent=2))
print('full union group336 and outer-involution two-fixed-candidate guard PASS')
