"""Independent low-degree PRS content profile; no parameter search."""
import json
from pathlib import Path
from flint import nmod_poly
import verify_conic as V
P=Path(__file__).parent

def profile(h,label):
 content=V.zero
 for c in h:content=content.gcd(c)
 primitive=[c//content for c in h]
 assert all(c==z*content for c,z in zip(h,primitive))
 supports=[[i for i in range(c.degree()+1) if c[i]] for c in primitive]
 common_mod7=all(len({i%7 for i in supp})<=1 for supp in supports)
 return {'family':label,'X_degree':len(h)-1,'raw_max_coefficient_degree':max(c.degree() for c in h),
  'content_degree':content.degree(),'primitive_max_coefficient_degree':max(c.degree() for c in primitive),
  'content_coefficients':list(map(int,content.coeffs())),
  'primitive_coefficient_nonzero_terms':sum(len(s) for s in supports),
  'each_coefficient_single_mod7_residue':common_mod7,
  'maximum_degree_after_individual_u_residue_and_u7':max((max(s)-min(s))//7 for s in supports if s) if common_mod7 else None}
res=[profile(V.h,'conic')]
d=V.d;f=[]
for terms in d['residual_coefficient_terms']:
 c=[0]*19
 for (i,j),v in terms:c[i]=(c[i]+v)%29
 f.append(nmod_poly(c,29))
a=f;g=V.trim([f[i]*i for i in range(1,len(f))]);m=len(g)-1;delta=len(a)-len(g)
h=[x*((-1)**(delta+1)) for x in V.prem(a,g)];lc=g[-1];c=-(lc**delta)
while len(h)-1>14:
 k=len(h)-1;a,g,m,delta=g,h,k,m-k
 beta=-lc*c**delta;h=V.exact_div(V.prem(a,g),beta);lc=g[-1]
 if delta>1:c,rem=divmod((-lc)**delta,c**(delta-1));assert not rem
 else:c=-lc
assert len(h)-1==14
res.append(profile(h,'line [1:u:1]'))
(P/'subresultant_content.json').write_text(json.dumps(res,indent=2));print(json.dumps(res,indent=2))
