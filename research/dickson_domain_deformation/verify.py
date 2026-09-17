"""Independent stdlib replay of corrections, a rank minor, and an obstruction."""
from itertools import combinations
from math import comb,isqrt
from pathlib import Path
import json
BASE=Path(__file__).resolve().parent

def value(c,x,m):return sum(a*pow(x,j,m) for j,a in enumerate(c))%m

def determinant(a,p):
 a=[r[:] for r in a];out=1
 for j in range(len(a)):
  pivot=next((i for i in range(j,len(a)) if a[i][j]%p),None)
  if pivot is None:return 0
  if pivot!=j:a[j],a[pivot]=a[pivot],a[j];out=-out
  v=a[j][j]%p;out=out*v%p;inv=pow(v,-1,p)
  for i in range(j+1,len(a)):
   f=a[i][j]*inv%p
   for t in range(j,len(a)):a[i][t]=(a[i][t]-f*a[j][t])%p
 return out%p

def interpolate(xs,ys,p):
 c=[0]*len(xs)
 for i,x in enumerate(xs):
  poly=[1];den=1
  for j,xx in enumerate(xs):
   if i==j:continue
   nxt=[0]*(len(poly)+1)
   for t,a in enumerate(poly):nxt[t]=(nxt[t]-xx*a)%p;nxt[t+1]=(nxt[t+1]+a)%p
   poly=nxt;den=den*(x-xx)%p
  scalar=ys[i]*pow(den,-1,p)%p
  c=[(a+scalar*b)%p for a,b in zip(c,poly)]
 return tuple(c)

def main():
 data=json.loads((BASE/'pilot.json').read_text());assert data['status']=='complete';results=[]
 for row in data['fixtures']:
  p=row['p'];n=p-1;k=n//4;L=n//2;e=(p+1)//2
  assert all(p%d for d in range(2,isqrt(p)+1))
  nodes=list(range(1,p))
  polys=[[comb(e,2*j+1)*a**(e-2*j-1)%p for j in range(k)] for a in range(1,L+1)]
  assert nodes==row['nodes'] and polys==row['polynomials']
  w=[((1+(1 if pow(x,(p-1)//2,p)==1 else -1))//2-pow(x,k,p))%p for x in nodes]
  incidences=[[i for i,c in enumerate(polys) if value(c,x,p)==y] for x,y in zip(nodes,w)]
  equations=[[u,i,ids[0]] for u,ids in enumerate(incidences) for i in ids[1:]]
  assert equations==row['equations']
  J=[];b=[]
  for u,i,ref in equations:
   x=nodes[u];r=[0]*(n+L*k)
   r[u]=sum(t*(polys[i][t]-polys[ref][t])*pow(x,t-1,p) for t in range(1,k))%p
   for t in range(k):r[n+i*k+t]=pow(x,t,p);r[n+ref*k+t]=-pow(x,t,p)%p
   delta=(value(polys[i],x,p*p)-value(polys[ref],x,p*p))%(p*p)
   assert delta%p==0
   J.append(r);b.append((-delta//p)%p)
  if row['status']=='obstructed_mod_p_squared':
   v=row['left_kernel']
   assert len(v)==len(J)
   assert all(sum(v[i]*J[i][j] for i in range(len(J)))%p==0 for j in range(len(J[0])))
   obstruction=sum(x*y for x,y in zip(v,b))%p
   assert obstruction==row['obstruction']!=0
   results.append(dict(p=p,status='obstruction_verified',equations=len(J),variables=len(J[0]),nonzero_witness_entries=sum(x!=0 for x in v),obstruction=obstruction,scope='No unramified mod-p-squared lift of this exact incidence seed; ramified lifts are not excluded.'))
  else:
   correction=row['correction']
   assert all(sum(x*y for x,y in zip(r,correction))%p==bb for r,bb in zip(J,b))
   lifted_nodes=[x+p*correction[u] for u,x in enumerate(nodes)]
   lifted_polys=[[a+p*correction[n+i*k+t] for t,a in enumerate(c)] for i,c in enumerate(polys)]
   assert all(value(lifted_polys[i],lifted_nodes[u],p*p)==value(lifted_polys[ref],lifted_nodes[u],p*p) for u,i,ref in equations)
   cols=row['pivot_columns'];minor=[[r[j] for j in cols] for r in J]
   det=determinant(minor,p);assert det
   # Independently exhaust every determining support for the original received word.
   pool={interpolate([nodes[i] for i in I],[w[i] for i in I],p) for I in combinations(range(n),k)}
   agreements={c:sum(value(c,x,p)==y for x,y in zip(nodes,w)) for c in pool}
   M=max(agreements.values());nearest=sum(a==M for a in agreements.values())
   assert M==6 and nearest==22
   results.append(dict(p=p,status='smooth_finite_lift_verified',equations=len(J),variables=len(J[0]),minor_determinant=det,source_maximum_agreement=M,source_complete_nearest_list=nearest,lifted_selected_candidates=L,determining_supports=comb(n,k),scope='Full row rank gives an all-orders unramified lift for this finite bank. Source maximum agreement persists, because interpolation denominators are units. No growing-family conclusion.'))
 out=dict(status='passed',fixtures=results)
 (BASE/'verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

if __name__=='__main__':main()
