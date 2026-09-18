from itertools import product,combinations
from sympy.polys.galoistools import gf_irreducible_p
from sympy.polys.domains import ZZ
import json,time
from pathlib import Path
start=time.time();p=3;e=5;q=p**e
for tail in product(range(p),repeat=e):
 if tail[-1] and gf_irreducible_p([1]+list(tail),p,ZZ):break
mod=list(reversed(tail))+[1]
def digits(a):
 ds=[]
 for _ in range(e):ds.append(a%p);a//=p
 return ds
D=[digits(a) for a in range(q)]
def enc(ds):return sum(c*p**i for i,c in enumerate(ds))
add=[[enc([(x+y)%p for x,y in zip(D[a],D[b])]) for b in range(q)] for a in range(q)]
neg=[enc([(-x)%p for x in D[a]]) for a in range(q)]
def sub(a,b):return add[a][neg[b]]
def mm(a,b):
 c=[0]*(2*e-1)
 for i,x in enumerate(D[a]):
  for j,y in enumerate(D[b]):c[i+j]=(c[i+j]+x*y)%p
 for k in range(2*e-2,e-1,-1):
  for j in range(e):c[k-e+j]=(c[k-e+j]-c[k]*mod[j])%p
 return enc(c[:e])
mul=[[mm(a,b) for b in range(q)] for a in range(q)]
def power(a,n):
 r=1
 while n:
  if n&1:r=mul[r][a]
  a=mul[a][a];n//=2
 return r
inv=[0]+[power(a,q-2) for a in range(1,q)]
nodes=[add[t][u] for t in [p,p*p,p*p*p] for u in range(p)]
assert len(set(nodes))==9 and 0 not in nodes
f0=[power(x,p**4-1) for x in nodes];f1=[power(x,p**3-1) for x in nodes];g=[power(x,p*p-1) for x in nodes]
rows=[[1,x,mul[x][x],neg[gg],a,b] for x,gg,a,b in zip(nodes,g,f0,f1)]
candidates={};singular=[];inconsistent=0
for support in combinations(range(9),4):
 a=[rows[i][:] for i in support];pivs=[];r=0
 for c in range(4):
  t=next((i for i in range(r,4) if a[i][c]),None)
  if t is None:continue
  a[r],a[t]=a[t],a[r];scale=inv[a[r][c]];a[r]=[mul[scale][v] for v in a[r]]
  for i in range(4):
   if i!=r and a[i][c]:
    fac=a[i][c];a[i]=[sub(x,mul[fac][y]) for x,y in zip(a[i],a[r])]
  pivs.append(c);r+=1
 if any(not any(row[:4]) and any(row[4:]) for row in a):inconsistent+=1;continue
 if r<4:singular.append({'support':support,'rank':r});continue
 solution=tuple((a[j][4],a[j][5]) for j in range(4));hits=[]
 for i,row in enumerate(rows):
  vals=[0,0]
  for j in range(4):
   for k in range(2):vals[k]=add[vals[k]][mul[row[j]][solution[j][k]]]
  if vals==[row[4],row[5]]:hits.append(i)
 candidates[solution]=hits
hist={};best=[]
for sol,hits in candidates.items():
 hist[len(hits)]=hist.get(len(hits),0)+1
 if len(hits)>=5:best.append({'solution':sol,'support':hits})
result={'p':p,'field_modulus':mod,'nodes':nodes,'f0':f0,'f1':f1,'g':g,'coefficient_convention':'h0,h1,h2,z solve h-z*g=f0+theta*f1; theta outside F243','tested_four_subsets':126,'inconsistent':inconsistent,'singular':singular,'candidate_histogram':hist,'five_match_candidates':best,'seconds':time.time()-start}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2));print(json.dumps({k:v for k,v in result.items() if k not in ['f0','f1','g','nodes','five_match_candidates']},indent=2));print('five-match candidates',len(best))
