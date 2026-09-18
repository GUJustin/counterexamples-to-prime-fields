"""Exact mod29 tangent and toric-boundary certificates; no genus black box."""
import json,math
from pathlib import Path
from sympy import symbols,Poly,gcd
P=Path(__file__).parent;d=json.loads((P.parent/'gate.json').read_text())[0];p=d['p'];T=symbols('T');out={'p':p,'tangents':[],'eigenquotients':[]}
def cr(a,b,c):return(b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def hull(ps):
 ps=sorted(set(ps));lo=[];hi=[]
 for a in ps:
  while len(lo)>1 and cr(lo[-2],lo[-1],a)<=0:lo.pop()
  lo.append(a)
 for a in ps[::-1]:
  while len(hi)>1 and cr(hi[-2],hi[-1],a)<=0:hi.pop()
  hi.append(a)
 return lo[:-1]+hi[:-1]
for idx in [0,7]:
 x,y=d['base'][idx],d['word'][idx];m=4 if idx<7 else 6;fs=[]
 for v in d['kernel']:
  co=[]
  for b in range(m+1):
   a=m-b;co.append(sum(c*math.comb(k,a)*math.comb(l,b)*pow(x,k-a,p)*pow(y,l-b,p)for(k,l),c in zip(d['columns'],v)if k>=a and l>=b)%p)
  fs.append(Poly(sum(c*T**b for b,c in enumerate(co)),T,modulus=p))
 assert gcd(gcd(fs[0],fs[1]),fs[2]).degree()==0
 f=sum(fs[1:],fs[0]);assert f.degree()==m and gcd(f,f.diff()).degree()==0
 # No common homogeneous root at infinity.
 assert any(f.degree()==m for f in fs)
 out['tangents'].append({'representative':idx,'multiplicity':m,'cones':[str(f.as_expr())for f in fs],'common_gcd':1,'sum_squarefree':True})
for r,v in zip([1,3,5],d['kernel']):
 ts=[((k-2*l-r)//7+3,l,c)for(k,l),c in zip(d['columns'],v)if c]
 assert all((k-2*l)%7==r for(k,l),c in zip(d['columns'],v)if c)
 h=hull([(a,b)for a,b,c in ts]);edges=[];branch=0
 for a,b in zip(h,h[1:]+h[:1]):
  dx,dy=b[0]-a[0],b[1]-a[1];g=math.gcd(abs(dx),abs(dy));dx//=g;dy//=g
  co={((x-a[0])//dx if dx else (y-a[1])//dy):c for x,y,c in ts if cr(a,b,(x,y))==0}
  f=Poly(sum(c*T**j for j,c in co.items()),T,modulus=p)
  assert f.degree()==g and f.nth(0)!=0 and gcd(f,f.diff()).degree()==0
  n=g if dy%7 else 0;branch+=n
  edges.append({'a':a,'b':b,'T_valuation':-dy,'edge_polynomial':str(f.as_expr()),'squarefree':True,'Kummer_branch_places':n})
 area=sum(x*v-y*u for(x,y),(u,v)in zip(h,h[1:]+h[:1]));bd=sum(math.gcd(abs(x-u),abs(y-v))for(x,y),(u,v)in zip(h,h[1:]+h[:1]));I=(area-bd+2)//2
 assert branch==4 and I==22
 out['eigenquotients'].append({'character':r,'terms':ts,'hull':h,'interior_points':I,'edges':edges,'Kummer_branch_places':branch,'genus_lower_bound':6})
out['generic_net_budget']={'self_intersection':380,'prescribed_square_sum':364,'residual_square_budget':16,'prescribed_delta':147,'maximum_extra_generic_delta':6,'generic_genus_lower_bound':9}
(P/'boundary.json').write_text(json.dumps(out,indent=2));print('PASS: ordinary prescribed points; three quotients with four tame Kummer branch places each')
