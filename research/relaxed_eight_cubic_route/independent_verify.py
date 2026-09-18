#!/usr/bin/env python3
"""Independent stdlib incidence/Jacobian/nearest-list audit, no search imports."""
import json,itertools,hashlib,time,math
from fractions import Fraction
from pathlib import Path
P=Path(__file__).resolve().parent;raw=(P/'local_search.json').read_bytes();d=json.loads(raw);p=17
assert d['p']==p and d['n']==16 and d['degree']==3
x=d['nodes'];w=d['word'];F=d['polynomials'];S=d['selected_supports'];assert len(set(x))==16 and len({tuple(v) for v in F})==8
assert all(0<=z<p for z in x+w) and all(len(c)==4 and c[3]%p for c in F)
def ev(c,z):
 a=0
 for v in reversed(c):a=(a*z+v)%p
 return a
start=time.time();actual=[[j for j,z in enumerate(x) if ev(c,z)==w[j]] for c in F];assert actual==S and all(len(v)==7 for v in S)
J=[]
for i,c in enumerate(F):
 for j in S[i]:
  z=x[j];row=[0]*64
  for k in range(4):row[4*i+k]=pow(z,k,p)
  row[32+j]=(c[1]+2*c[2]*z+3*c[3]*z*z)%p;row[48+j]=-1%p;J.append(row)
assert len(J)==56
cols=d['pivot_columns'];assert len(set(cols))==56 and all(0<=j<64 for j in cols)
A=[[r[j] for j in cols] for r in J];det=1
for i in range(56):
 k=next(j for j in range(i,56) if A[j][i])
 if k!=i:A[k],A[i]=A[i],A[k];det=-det
 z=A[i][i];det=det*z%p;iv=pow(z,-1,p)
 for j in range(i+1,56):
  c=A[j][i]*iv%p
  for k in range(i+1,56):A[j][k]=(A[j][k]-c*A[i][k])%p
  A[j][i]=0
assert det%p
# Rebuild all degree<=3 interpolants by small Vandermonde solves.
def interp(I):
 A=[[1,x[i],x[i]**2%p,x[i]**3%p,w[i]] for i in I]
 for j in range(4):
  k=next(k for k in range(j,4) if A[k][j]);A[j],A[k]=A[k],A[j];v=pow(A[j][j],-1,p);A[j]=[v*z%p for z in A[j]]
  for k in range(4):
   if k!=j:
    v=A[k][j];A[k]=[(a-v*b)%p for a,b in zip(A[k],A[j])]
 return tuple(A[j][4] for j in range(4))
C={interp(I) for I in itertools.combinations(range(16),4)};counts={c:sum(ev(c,z)==v for z,v in zip(x,w)) for c in C};maximum=max(counts.values());nearest=sorted(c for c,n in counts.items() if n==maximum)
assert maximum==7 and nearest==sorted(map(tuple,F))
rho=Fraction(7,32);a=Fraction(14,32);margin=(8-rho)*a*a-6*rho*a+rho*(4*rho-5);assert margin==Fraction(105,8192)
assert (11-rho)**2<117
out=dict(status='PASS',input_sha256=hashlib.sha256(raw).hexdigest(),method='stdlib reconstruction and modular determinant; exhaustive four-support Vandermonde decoding',prime=p,distinct_nodes=16,distinct_polynomials=8,actual_supports=actual,incidence_equations=56,variables=64,jacobian_minor_columns=cols,jacobian_minor_determinant_mod17=det%p,jacobian_rank=56,free_variables=[j for j in range(64) if j not in cols],all_four_point_supports=math.comb(16,4),distinct_interpolants=len(C),maximum_agreement=maximum,complete_nearest_list_size=len(nearest),nearest_polynomials=nearest,square_pullback_parameters=dict(n=32,k=7,agreement=14,list_size_lower_bound=8,complete_nearest_list_claim=False),first_order_polynomial_margin=str(margin),seconds=time.time()-start)
(P/'independent_verify.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
