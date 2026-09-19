"""Exact normalized census for two specified nonadjacent k=2 offsets."""
from collections import Counter
import json
from itertools import combinations

def one(p,n,h,r,m,target):
 D=[x for x in range(1,p) if pow(x,n,p)==1]
 assert len(D)==n and n==h*r and m==2*h+1
 words=[pow(x,m,p) for x in D]
 normalized=Counter(); full=Counter(); witnesses={}
 for a in range(p):
  for b in range(p):
   c=(1-a-b)%p
   A=sum((a*x*x+b*x+c)%p==y for x,y in zip(D,words))
   normalized[A]+=1
   if a*b*c:
    full[A]+=1;witnesses.setdefault(A,[a,b,c])
 def recover(counts,total):
  result={}
  for A,H in counts.items():
   assert A>0 and n*H%A==0
   result[A]=n*H//A
  result[0]=total-sum(result.values())
  assert result[0]>=0
  return result
 all_hist=recover(normalized,p**3)
 full_hist=recover(full,(p-1)**3)
 assert sum(A*L for A,L in all_hist.items())==n*p*p
 assert sum(A*(A-1)//2*L for A,L in all_hist.items())==n*(n-1)//2*p
 assert sum(A*(A-1)*(A-2)//6*L for A,L in all_hist.items())==n*(n-1)*(n-2)//6
 best=max(A for A,L in full_hist.items() if L)
 outside=max(A for A,L in all_hist.items() if L-(full_hist.get(A,0) if A==best else 0)>0)
 verification=None
 if best>=target:
  # Independent three-point interpolation: each polynomial appears C(A,3) times.
  support=Counter()
  for inds in combinations(range(n),3):
   coeff=[0,0,0]
   for t in range(3):
    i=inds[t];j=inds[(t+1)%3];k=inds[(t+2)%3]
    scale=words[i]*pow((D[i]-D[j])*(D[i]-D[k])%p,-1,p)%p
    coeff[0]=(coeff[0]+scale)%p
    coeff[1]=(coeff[1]-scale*(D[j]+D[k]))%p
    coeff[2]=(coeff[2]+scale*D[j]*D[k])%p
   support[tuple(coeff)]+=1
  recovered=Counter()
  cube={A*(A-1)*(A-2)//6:A for A in range(3,n+1)}
  for coeff,multiplicity in support.items():
   assert multiplicity in cube
   if all(coeff):recovered[cube[multiplicity]]+=1
  assert all(recovered[A]==full_hist.get(A,0) for A in range(3,n+1))
  verification={'method':'independent three-point interpolation','status':'PASS'}
 return dict(p=p,n=n,h=h,r=r,m=m,target=target,all_histogram=dict(sorted(all_hist.items())),full_coefficient_histogram=dict(sorted(full_hist.items())),full_max=best,bank_size=full_hist[best],outside_bank_max=outside,gap=best-outside,seed_abc=witnesses[best],above_sqrt_1_5_n=2*best*best>3*n,target_reached=best>=target,moment_checks='PASS',independent_positive_verification=verification)

print(json.dumps({'status':'PASS','scope':'Exactly two prescribed profiles; normalized census with exact orbit division and interpolation moments.','profiles':[one(71,35,5,7,11,8),one(131,65,5,13,11,10)]},indent=2))
