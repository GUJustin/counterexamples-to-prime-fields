"""Bounded tangent probe on the already certified smooth p17 seed."""
from pathlib import Path
from itertools import combinations
from math import comb
from collections import Counter
import json
from verify import value,interpolate
BASE=Path(__file__).resolve().parent

def main():
 row=json.loads((BASE/'pilot.json').read_text())['fixtures'][0]
 p=17;n=16;k=4;polys=row['polynomials'];xs=list(range(1,p));v=n+len(polys)*k
 word=[((1+(1 if pow(x,8,p)==1 else -1))//2-pow(x,k,p))%p for x in xs]
 inc=[[i for i,c in enumerate(polys) if value(c,x,p)==y] for x,y in zip(xs,word)]
 assert all(inc)
 def derivative(c,x):return sum(t*c[t]*pow(x,t-1,p) for t in range(1,len(c)))%p
 J=[]
 for u,i,ref in row['equations']:
  r=[0]*v;x=xs[u];r[u]=(derivative(polys[i],x)-derivative(polys[ref],x))%p
  for t in range(k):r[n+i*k+t]=pow(x,t,p);r[n+ref*k+t]=-pow(x,t,p)%p
  J.append(r)
 R=[r[:] for r in J];pivots=[];rank=0
 for j in range(v):
  z=next((z for z in range(rank,len(R)) if R[z][j]),None)
  if z is None:continue
  R[rank],R[z]=R[z],R[rank];inv=pow(R[rank][j],-1,p);R[rank]=[x*inv%p for x in R[rank]]
  for z in range(len(R)):
   if z!=rank:
    f=R[z][j];R[z]=[(a-f*b)%p for a,b in zip(R[z],R[rank])]
  pivots.append(j);rank+=1
  if rank==len(R):break
 basis=[]
 for j in range(v):
  if j in pivots:continue
  z=[0]*v;z[j]=1
  for r,t in enumerate(pivots):z[t]=-R[r][j]%p
  assert all(sum(a*b for a,b in zip(r,z))%p==0 for r in J)
  basis.append(z)
 pool={interpolate([xs[i] for i in I],[word[i] for i in I],p) for I in combinations(range(n),k)}
 selected=set(map(tuple,polys));out=[];hist=Counter();unwanted=Counter()
 for c in sorted(pool):
  support=[i for i,(x,y) in enumerate(zip(xs,word)) if value(c,x,p)==y]
  if len(support)<k+1:continue
  hist[len(support)]+=1
  if c in selected:continue
  for S in combinations(support,k+1):
   grad=[0]*v
   for u in S:
    x=xs[u];den=1
    for j in S:
     if j!=u:den=den*(x-xs[j])%p
    lam=pow(den,-1,p);ref=inc[u][0]
    grad[u]=lam*(derivative(polys[ref],x)-derivative(c,x))%p
    for t in range(k):grad[n+ref*k+t]=(grad[n+ref*k+t]+lam*pow(x,t,p))%p
   derivatives=[sum(a*b for a,b in zip(grad,z))%p for z in basis]
   status='breakable_to_first_order' if any(derivatives) else 'tangent_inconclusive'
   unwanted[status]+=1
   out.append(dict(polynomial=c,source_agreement=len(support),support=S,status=status,kernel_derivatives=derivatives))
 result=dict(status='completed_probe',p=p,jacobian_rank=rank,kernel_dimension=len(basis),
  source_above_capacity_profile=dict(hist),unwanted_support_status=dict(unwanted),kernel_basis=basis,supports=out,
  scope='First-order nonvanishing can exclude an unwanted support generically on this smooth lifting branch. Zero first derivative is inconclusive, not evidence that the support persists.')
 (BASE/'extra_support_probe.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({key:result[key] for key in ['status','jacobian_rank','kernel_dimension','source_above_capacity_profile','unwanted_support_status']},indent=2))
if __name__=='__main__':main()
