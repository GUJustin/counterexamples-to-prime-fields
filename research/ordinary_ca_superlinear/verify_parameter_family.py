"""Exact arithmetic audit of the parameter family, not an existence proof."""
from pathlib import Path
import json
cases=0
for b in (2,3,4,5):
 for d in range(b+7,101):
  assert 4*(d-b-3)*(b+2)**(b-1)<=d**b
  for r in range(40,301):
   for m in sorted({(3*r+1)//2,19*r//12,5*r//3}):
    D=m-r+1;n=d*D;u=(d-b-1)*D-3*r;s=b*D-r+1
    assert r/2+1<=D<=2*r/3+1<=r and u>=0 and s>=1
    N=4*r+u+s;K=r+s;M=m+s
    assert (N,K,M)==((d-1)*D+1,b*D+1,(b+1)*D)
    assert N-1+D==n and K-1==b*D and M-(K-1)==D
    assert b*D-1<4*r+1
    remaining=s-1;currentK=r+1;currentM=m+1;degree=4*(u+1);blocks=0
    while remaining:
     h=min(D,remaining);assert h<=currentM-currentK+1
     degree*=currentK+2*h
     currentK+=h;currentM+=h;remaining-=h;blocks+=1
    assert blocks<=b-1 and (currentK,currentM)==(K,M)
    assert degree<=4*(d-b-3)*(b+2)**(b-1)*D**b<=n**b
    assert M*d>= (b+1)*N
    cases+=1
out=dict(status='passed',cases=cases,b_values=[2,3,4,5],d_up_to=100,r_range=[40,300],m_cases='lower endpoint, middle, new five-thirds upper endpoint',scope='Exact integer identities, characteristic guard, block admissibility and field-degree estimates; no numerical proof of asymptotic existence.')
Path(__file__).with_name('parameter_family_verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
