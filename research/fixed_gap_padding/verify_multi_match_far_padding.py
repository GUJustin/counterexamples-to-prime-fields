"""Exhaustive second moments across distinct domains and nonzero directions."""
from fractions import Fraction as F
from itertools import combinations,product
from math import comb,prod
from pathlib import Path
import json,time


def fall(x,a):
 return prod(x-j for j in range(a)) if a<=x else 0


def fixture(p,K,D,core):
 start=time.monotonic();U=p-1;d=K-1
 N=len(core);outside=[x for x in range(p) if x not in core];R=len(outside)
 # w=X^D; subtract each monic support locator.
 from verify_anchored_padding import locator
 Ps=[tuple(-a%p for a in locator(S,p)[:-1]) for S in combinations(core,D)];L=len(Ps)
 assert K==D
 val=lambda P,x:sum(a*pow(x,j,p) for j,a in enumerate(P))%p
 assert len(set(Ps))==L
 assert all(sum(val(P,x)==x**D%p for x in core)==D for P in Ps)
 assert all(val(P,x)!=x**D%p for P in Ps for x in outside)
 collisions=[sum(val(P,x)==val(Q,x) for x in outside) for P,Q in combinations(Ps,2)]
 occup=[sum(val(P,x)==x**D%p for P in Ps) for x in core]
 a,b=divmod(L*D,N);balanced=(N-b)*comb(a,2)+b*comb(a+1,2)
 T=d*comb(L,2)-balanced
 e=d-max(0,2*D-N)
 assert sum(collisions)<=T and any(collisions) and max(collisions)<=e
 assert e>=1
 q=3;total=comb(R,q)*U**q;sums=[0]*q;squares=[0]*q;positive=[0]*q
 best=[None]*q
 best_sizes=[-1]*q
 for xs in combinations(outside,q):
  diffs=[[(val(P,x)-x**D)%p for x in xs] for P in Ps]
  for gs in product(range(1,p),repeat=q):
   matches=[sum(v==g for v,g in zip(row,gs)) for row in diffs]
   label_counts=[]
   for row in diffs:
    counts={}
    for v,g in zip(row,gs):
     z=v*pow(g,-1,p)%p
     counts[z]=counts.get(z,0)+1
    label_counts.append(counts)
   for r in range(1,q+1):
    X=sum(comb(a,r) for a in matches if a>=r)
    sums[r-1]+=X;squares[r-1]+=X*X;positive[r-1]+=X>0
    labels={z for counts in label_counts for z,a in counts.items() if a>=r}
    if len(labels)>best_sizes[r-1]:
     best_sizes[r-1]=len(labels);best[r-1]=(xs,gs,sorted(labels))
  # Enumerating all z for one fixed choice is not needed for the moment identity.
 rows=[]
 for r in range(1,q+1):
  mean=F(L*comb(q,r),U**r)
  ratio=sum(F(comb(r,a)*comb(q-r,r-a),comb(q,r))*U**a*(F(1,L)+
    sum((F(2*fall(c,a),fall(R,a)) for c in collisions),F(0))/L**2)
    for a in range(r+1) if 0<=r-a<=q-r)
  bound=F(0)
  for a in range(r+1):
   if not 0<=r-a<=q-r:continue
   v=F(comb(r,a)*comb(q-r,r-a),comb(q,r))
   bound+=v if a==0 else v*U**a*(F(1,L)+F(2*T*fall(d-1,a-1),L**2*fall(R,a)))
  assert F(sums[r-1],total)==mean
  assert F(squares[r-1],total)/mean**2==ratio<=bound
  assert F(positive[r-1],total)>=1/bound
  uniform_ratio=sum(F(comb(r,a)*comb(q-r,r-a),comb(q,r))*U**a*
    (F(1,L)+F((L-1)*fall(e,a),L*fall(R,a))) for a in range(r+1) if 0<=r-a<=q-r)
  simple_upper=F(U**r,L)+F(U,R-r+1)**r*(1+F(r*(e-1),q-r+1))**r
  assert ratio<=uniform_ratio<=simple_upper
  xs,gs,labels=best[r-1]
  domain=core+list(xs);f=[x**D%p for x in domain];g=[0]*N+list(gs)
  profile=[max(sum(val(P,x)==(f[j]+z*g[j])%p for j,x in enumerate(domain))
               for P in product(range(p),repeat=K)) for z in range(p)]
  assert profile[0]==D and all(profile[z]>=D+r for z in labels)
  assert len(labels)>=U/bound
  rows.append(dict(r=r,threshold=D+r,exact_far_agreement=D,mean=str(mean),
                   selected_labels=labels,domain=domain,f=f,g=g,full_agreement_profile=profile,
                   exact_second_moment_ratio=str(ratio),ratio_upper=str(bound),
                   uniform_cap_ratio=str(uniform_ratio),simple_ratio_upper=str(simple_upper),
                   exact_positive_probability=str(F(positive[r-1],total))))
 identity_cases=0
 for q0 in range(1,25):
  for r0 in range(1,min(q0,8)+1):
   for d0 in range(1,13):
    exact=sum(F(comb(r0,a)*comb(q0-r0,r0-a),comb(q0,r0))*d0**a
              for a in range(r0+1) if 0<=r0-a<=q0-r0)
    expansion=sum(F((d0-1)**j*comb(r0,j)*fall(r0,j),fall(q0,j)) for j in range(r0+1))
    upper=(1+F(r0*(d0-1),q0-r0+1))**r0
    assert exact==expansion<=upper
    identity_cases+=1
 out=dict(hypergeometric_identity_cases=identity_cases,status='passed',p=p,n=N+q,K=K,core=core,L=L,
          outside_pair_collisions=collisions,T=T,uniform_pair_cap=e,domain_direction_choices=total,
          rows=rows,seconds=time.monotonic()-start,
          scope='Exhaustive finite second-moment mechanism check, not an Elias fixture or asymptotic proof.')
 return out


def main():
 out=dict(status='passed',fixtures=[fixture(11,2,2,[0,1,2,3]),fixture(11,3,3,[0,1,2,3,4])])
 Path(__file__).with_name('multi_match_far_verification.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({**out,'fixtures':[{k:v for k,v in row.items() if k not in {'rows','outside_pair_collisions'}} for row in out['fixtures']]},indent=2))
if __name__=='__main__':main()
