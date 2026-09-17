"""Exhaust all codewords at the far point for all three parity cases."""
from itertools import combinations,product
from math import prod
from pathlib import Path
import json,time
BASE=Path(__file__).resolve().parent

def coefficients(I,p):
 out=[1]
 for a in I:
  new=[0]*(len(out)+2)
  for j,c in enumerate(out):new[j]=(new[j]-a*a*c)%p;new[j+2]=(new[j+2]+c)%p
  out=new
 return out

def check(epsilon,extra_zero):
 p=11;seed=[1,2,3];D=2;K=2*D-1+epsilon
 domain=[1,10,2,9,3,8,4,7]+([0] if extra_zero else [])
 supports=list(combinations(seed,D));ref=supports[0]
 H=lambda I,x:prod((x*x-a*a)%p for a in I)%p
 f=[pow(x,epsilon,p)*H(ref,x)%p for x in domain]
 g=[pow(x,epsilon,p) if x in [4,7] else 0 for x in domain]
 A=2*D+2+epsilon
 for I in supports:
  coeff=[(x-y)%p for x,y in zip(coefficients(ref,p),coefficients(I,p))]
  if epsilon:coeff=[0]+coeff
  assert not any(coeff[K:])
  candidate=[sum(c*pow(x,j,p) for j,c in enumerate(coeff))%p for x in domain]
  assert sum(a==b for a,b in zip(f,candidate))==A-2
  z=-H(I,4)%p
  assert z and sum((a+z*b)%p==c for a,b,c in zip(f,g,candidate))>=A
 best=0;winners=0
 for coeff in product(range(p),repeat=K):
  count=sum(sum(c*pow(x,j,p) for j,c in enumerate(coeff))%p==v for x,v in zip(domain,f))
  if count>best:best=count;winners=1
  elif count==best:winners+=1
 assert best==A-2
 return dict(epsilon=epsilon,extra_zero=extra_zero,p=p,n=len(domain),K=K,A=A,far_max_agreement=best,far_distance_numerator=len(domain)-best,codewords_checked=p**K,maximizers=winners)

if __name__=='__main__':
 start=time.monotonic();out=dict(status='passed',rows=[check(0,False),check(0,True),check(1,True)],seconds=time.monotonic()-start)
 (BASE/'parity_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
