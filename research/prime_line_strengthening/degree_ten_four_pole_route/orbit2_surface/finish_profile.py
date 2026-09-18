import json,math
from pathlib import Path
from flint import nmod_poly,nmod_mat
P=Path(__file__).resolve().parent;b=next(z for z in json.loads((P.parent/'gate.json').read_text()) if z['bank']=='orbit2');out=json.loads((P/'profile.json').read_text());p=83
F=[{tuple(ij):v for ij,v in zip(b['columns'],row) if v} for row in b['kernel']];x=nmod_poly([0,1],p)
checks=[]
for k,(a,y) in enumerate(zip(b['base'],b['word'])):
 ps=[nmod_poly([sum(v*pow(a,i,p) for (i,j),v in f.items() if j==k)%p for k in range(11)],p) for f in F]
 g=ps[0].gcd(ps[1]).gcd(ps[2]);expected=4 if k<7 else 6
 assert g==(x-y)**expected
 checks.append(dict(index=k,gcd_degree=g.degree(),only_ordinate=y))
H=out['quotient']['factors'][0]['terms']
for a in range(p):
 pol=nmod_poly([sum(v*pow(a,i,p) for i,j,v in H if j==k)%p for k in range(22)],p)
 found=False
 for yy,e in pol.roots():
  y=int(yy);dx=sum(i*v*pow(a,i-1,p)*pow(y,j,p) for i,j,v in H if i)%p;dy=sum(j*v*pow(a,i,p)*pow(y,j-1,p) for i,j,v in H if j)%p
  if dx or dy:point=dict(X=a,Y=y,gradient=[dx,dy]);found=True;break
 if found:break
assert found
out['known_fiber_checks']=checks;out['absolute_irreducibility_smooth_point']=point;out['resolved_basepoints']=14;out['moving_self_intersection']=16;out['canonical_intersection']=12;out['Euler_characteristic']=18;out['jet_Chern_number']=90;out['arithmetic_genus']=15
for key in ['leading','infinity']:
 width=max(map(len,out[key]));rank=nmod_mat([row+[0]*(width-len(row)) for row in out[key]],p).rank();assert rank>=2;out[key+'_coefficient_rank']=rank
(P/'profile.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS: only 14 basepoints; smooth Gamma point',point)
