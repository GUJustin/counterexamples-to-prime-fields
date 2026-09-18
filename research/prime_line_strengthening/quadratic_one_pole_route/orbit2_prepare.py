import json,itertools
from fractions import Fraction as Q
from pathlib import Path
P=Path(__file__).parent;D=json.loads((P.parent/'fano_seven/orbit2_independent_field_audit.json').read_text());p=83;q=4
assert (q**3-10*q*q+3*q+1)%p==0
def value(v):
 return sum((Q(c).numerator*pow(Q(c).denominator,-1,p)%p)*pow(q,j,p) for j,c in enumerate(v))%p
xs=list(map(value,D['affine_nodes']));ys=list(map(value,D['affine_word']));polys=[list(map(value,row)) for row in D['affine_polynomials']]
assert len(set(xs))==14
masks=[[i for i,c in enumerate(polys) if sum(v*pow(x,j,p) for j,v in enumerate(c))%p==y] for x,y in zip(xs,ys)]
assert masks==[[i-1 for i in row] for row in D['agreement_masks']]
patterns=[];counts=[]
for f in range(4):
 for F in itertools.combinations(range(14),f):
  for E in itertools.combinations([j for j in range(14) if j not in F],f):
   if all(sum(i in masks[j] for j in F)<=sum(i in masks[j] for j in E) for i in range(7)):patterns.append(dict(full=F,empty=E))
 counts.append(sum(len(x['full'])==f for x in patterns))
out=dict(p=p,field_root=q,base=xs,word=ys,polynomials=polys,masks=masks,patterns=patterns)
(P/'orbit2_bank83.json').write_text(json.dumps(out,indent=2));print(counts)
s=(P/'all_fiber_norm_gate.py').read_text().replace("'fiber_patterns.json'","'orbit2_bank83.json'").replace('p=29;','p=83;').replace("'all_fiber_norm_gate.json'","'orbit2_norm_gate.json'")
(P/'orbit2_norm_gate.py').write_text(s)
