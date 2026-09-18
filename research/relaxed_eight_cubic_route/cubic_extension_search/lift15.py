import json
from fractions import Fraction
from pathlib import Path
P=Path(__file__).parent;s=json.loads((P.parent/'local_search.json').read_text());rs=json.loads((P.parent/'rational_seed.json').read_text());d=json.loads((P/'full15.json').read_text());p=17
class Ring:
 def __init__(self,m):self.m=m
 def a(self,u,v):return ((u[0]+v[0])%self.m,(u[1]+v[1])%self.m)
 def n(self,u):return (-u[0]%self.m,-u[1]%self.m)
 def sub(self,u,v):return self.a(u,self.n(v))
 def mul(self,u,v):return ((u[0]*v[0]+7*u[1]*v[1])%self.m,(u[0]*v[1]+u[1]*v[0])%self.m)
 def inv(self,u):
  z=pow((u[0]*u[0]-7*u[1]*u[1])%self.m,-1,self.m);return(u[0]*z%self.m,-u[1]*z%self.m)
 def pow(self,u,n):
  a=(1,0)
  for _ in range(n):a=self.mul(a,u)
  return a
 def ev(self,c,x):
  a=(0,0)
  for v in c[::-1]:a=self.a(self.mul(a,x),v)
  return a
 def rat(self,x):x=Fraction(x);return(x.numerator*pow(x.denominator,-1,self.m)%self.m,0)
def dec(u):return(u%17,u//17)
def enc(u):return u[0]+17*u[1]
r=Ring(17);R=Ring(289);z=dec(59);nodes=[r.mul((pow(i+1,11,17),0),r.pow(z,j)) for i in range(16) for j in range(3)];word=[(w,0) for w in s['word'] for j in range(3)]
allc={};orbit=[]
for hit in d['hits']:
 c=list(map(dec,hit['coefficients']));assert [i for i,x in enumerate(nodes) if r.ev(c,x)==word[i]]==hit['support'];orb=set()
 for conjugate in [False,True]:
  cc=[(a,-b%17) if conjugate else(a,b) for a,b in c]
  for j in range(3):
   v=tuple(r.mul(a,r.pow(z,j*k)) for k,a in enumerate(cc));orb.add(v);allc[v]=[i for i,x in enumerate(nodes) if r.ev(v,x)==word[i]]
 orbit.append(len(orb))
U=list(map(R.rat,rs['affine_nodes']));W=list(map(R.rat,rs['affine_word']));lifted=[]
for i,x in enumerate(nodes):
 target=R.sub((11,0),R.mul((3,0),U[i//3]));defect=R.sub(R.pow(x,3),target);assert all(a%17==0 for a in defect)
 corr=r.mul(r.n(tuple(a//17 for a in defect)),r.inv(r.mul((3,0),r.pow(x,2))));xx=R.a(x,tuple(17*a for a in corr));assert R.pow(xx,3)==target;lifted.append(xx)
 # Verify exact normalized source is the requested residue chart.
 assert r.rat(rs['affine_nodes'][i//3])==r.mul((pow(3,-1,17),0),r.sub((11,0),(i//3+1,0)))
outs=[]
for c,S in allc.items():
 transformed=[r.mul((10,0),a) for a in c]
 for j,a in enumerate(s['polynomials'][3]):transformed[3*j]=r.sub(transformed[3*j],(10*a%17,0))
 assert all(r.ev(transformed,nodes[i])==r.rat(rs['affine_word'][i//3]) for i in S)
 mat=[[R.pow(lifted[i],j) for j in range(10)]+[W[i//3]] for i in S[:10]]
 for j in range(10):
  k=next(k for k in range(j,10) if any(a%17 for a in mat[k][j]));mat[j],mat[k]=mat[k],mat[j];iv=R.inv(mat[j][j]);mat[j]=[R.mul(a,iv) for a in mat[j]]
  for k in range(10):
   if k!=j:
    t=mat[k][j];mat[k]=[R.sub(a,R.mul(t,b)) for a,b in zip(mat[k],mat[j])]
 coeff=[a[10] for a in mat];assert [tuple(a%17 for a in t) for t in coeff]==transformed
 residual=[R.sub(R.ev(coeff,lifted[i]),W[i//3]) for i in S];assert all(all(a%17==0 for a in t) for t in residual)
 outs.append({'raw_coefficients':list(map(enc,c)),'support':S,'normalized_lift_coefficients':coeff,'residual_div17':[tuple(a//17 for a in t) for t in residual],'fixed_cover_mod289_lifts':all(t==(0,0) for t in residual)})
out={'orbit_sizes':orbit,'distinct_candidates':len(allc),'lifted_nodes':lifted,'cover':'U=(11-T^3)/3','modulus':289,'cases':outs};(P/'lift15.json').write_text(json.dumps(out,indent=2)+'\n');print('orbits',orbit,'distinct',len(allc),'lifts',sum(x['fixed_cover_mod289_lifts'] for x in outs));print([(x['support'],x['residual_div17'][10:]) for x in outs])
