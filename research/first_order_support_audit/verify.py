"""Independent exact checks of restored first-order support optimization."""
from fractions import Fraction as F
from itertools import product
from math import comb
from pathlib import Path
import json
BASE=Path(__file__).resolve().parent

def rank_formula(H,m):
 S={(u,b) for b,h in enumerate(H) for u in range(h)}
 return sum(min(sum(u<=ell for u,b in S if u+b==q),m-ell)
            for q in range(max((u+b for u,b in S),default=-1)+1) for ell in range(m))

def rank_matrix(H,m,p=1009):
 columns=[];rows={}
 for b,h in enumerate(H):
  for u in range(h):
   for x in range(m):
    col={}
    for j in range(u+1):
     i=x+u-j
     if i+2*j<m:
      key=(i,j,u-j+b)
      if key not in rows:rows[key]=len(rows)
      col[rows[key]]=comb(u,j)%p
    columns.append(col)
 basis={}
 for col in columns:
  while col:
   pivot=min(col)
   if pivot not in basis:
    inv=pow(col[pivot],-1,p);basis[pivot]={i:a*inv%p for i,a in col.items()};break
   f=col[pivot]
   for i,a in basis[pivot].items():
    v=(col.get(i,0)-f*a)%p
    if v:col[i]=v
    elif i in col:del col[i]
 return len(basis)

def clip(poly,a,b,c):
 out=[]
 for P,Q in zip(poly,poly[1:]+poly[:1]):
  v=a*P[0]+b*P[1]+c;w=a*Q[0]+b*Q[1]+c
  if v>=0:out.append(P)
  if (v<0 and w>0) or (v>0 and w<0):
   t=v/(v-w);out.append((P[0]+t*(Q[0]-P[0]),P[1]+t*(Q[1]-P[1])))
 return out

def integrate(poly,a,b,c):
 area=F(0);mx=F(0);my=F(0)
 for P,Q in zip(poly,poly[1:]+poly[:1]):
  cross=P[0]*Q[1]-Q[0]*P[1];area+=cross/2
  mx+=(P[0]+Q[0])*cross/6;my+=(P[1]+Q[1])*cross/6
 return a*mx+b*my+c*area

def column_integral(m,b,Q,p):
 poly=[(F(b),F(b)),(F(Q+1),F(b)),(F(Q+1),F(b+1)),(F(b+1),F(b+1))]
 benefit=integrate(poly,-F(1,4),F(0),p)
 branches=[(F(0),F(0),F(0)),(-F(1),F(0),F(m)),(-F(1,2),F(1,2),F(m,2))]
 rank=F(0)
 for a,bb,c in branches:
  region=poly[:]
  for aa,bbb,cc in branches:
   if (a,bb,c)!=(aa,bbb,cc):region=clip(region,a-aa,bb-bbb,c-cc)
  rank+=integrate(region,a,bb,c)
 return benefit-rank,integrate(poly,0,0,1)

def cert(rho,a,m,B):
 ceil=lambda x:-((-x.numerator)//x.denominator)
 H=[];rank=0;benefit=F(0)
 C=lambda t:(max(0,t)+1)**2//4
 D=lambda t,b:max(0,t-2*b)**2//4
 for b in range((m*B).numerator//(m*B).denominator+1):
  end=min(ceil(m*a/rho)-1,(2*m*a-m-b)//(2*rho-1));h=int(end-b+1)
  assert h>0 and m*a-rho*end>0
  H.append(h);z=max(0,m-h)
  rank+=C(m)-C(z)+D(m,b)-D(z,b)
  benefit+=h*m*a-rho*(h*b+F(h*(h-1),2))
 assert all(H[i]+i>=H[i+1]+i+1 for i in range(len(H)-1))
 qmax=max(h+b-1 for b,h in enumerate(H))
 ell=(qmax*rank)//(benefit-rank)
 assert (ell+1)*benefit>rank*(ell+qmax+1)
 polynomial=(8-rho)*a*a-6*rho*a+rho*(4*rho-5)
 assert polynomial<0 and benefit>rank
 return dict(rho=str(rho),a=str(a),m=m,B=str(B),columns=len(H),monomials=sum(H),rank=rank,
             benefit=str(benefit),surplus=str(benefit-rank),maximum_jet_degree=qmax,
             sufficient_challenge_degree=int(ell),below_DKT_polynomial=str(polynomial))

def main():
 matrix_checks=0;rearrangements=0;column_checks=0
 for H in product(range(4),repeat=3):
  for m in range(1,6):
   assert rank_matrix(H,m)==rank_formula(H,m);matrix_checks+=1
 for H in product(range(5),repeat=4):
  sortedH=sorted(H,reverse=True)
  S={(u,b) for b,h in enumerate(sortedH) for u in range(h)}
  lengths=[sum(u+b==q for u,b in S) for q in range(8)]
  compressed={(q-b,b) for q,ell in enumerate(lengths) for b in range(ell)}
  compressedH=[max((u+1 for u,bb in compressed if bb==b),default=0) for b in range(4)]
  assert {(u,b) for b,h in enumerate(compressedH) for u in range(h)}==compressed
  for m in range(1,7):
   r1=rank_formula(H,m);r2=rank_formula(sortedH,m);r3=rank_formula(compressedH,m)
   assert r3<=r2<=r1
   cell=sum(max(0,m-u-b,(m-u+1)//2) for u,b in compressed)
   assert cell==r3;rearrangements+=1
 for m in range(1,17):
  for b in range(2*m):
   for Q in range(b,2*m):
    integral,area=column_integral(m,b,Q,F(m,2))
    discrete=sum(F(m,2)-F(q,4)-max(0,m-q,(m-q+b+1)//2) for q in range(b,Q+1))
    assert integral>=discrete,(m,b,Q,integral-discrete)
    assert area==Q-b+F(1,2);column_checks+=1
 cases=[cert(F(9,10),F(47389,50000),10000,F(49,500)),cert(F(3,4),F(43049,50000),100000,F(173,1000))]
 assert [(c['monomials'],c['rank'],c['benefit'],c['surplus']) for c in cases]==[
  (9724108,44523829596,'445252935317/10','14639357/10'),
  (1830201539,73254792027652,'293020925834159/4','1757723551/4')]
 out=dict(status='passed',direct_local_matrix_checks=matrix_checks,rearrangement_and_marginal_checks=rearrangements,
          exact_polygon_column_lifts=column_checks,finite_improvement_certificates=cases,
          scope='Independent finite arithmetic checks. The all-support and all-multiplicity statements require the separately audited proof; finite enumeration is not that proof.')
 (BASE/'verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
