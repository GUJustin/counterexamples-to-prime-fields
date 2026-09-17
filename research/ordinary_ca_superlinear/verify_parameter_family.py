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
    assert D<=r-1 and 1<=s<=(b-1)*D
    assert D<=r-b and s<=(b-1)*(D-1)
    assert (s+D-2)//(D-1)<=b-1
    assert (s+D-1)//D<=b-1
    assert 2*2**((s+D-1)//D)<=2**b
    remaining=s-1;currentK=r+1;currentM=m+1;degree=4*(u+1);blocks=0
    while remaining:
     h=min(D,remaining);assert h<=currentM-currentK+1
     degree*=currentK+2*h
     currentK+=h;currentM+=h;remaining-=h;blocks+=1
    assert blocks<=b-1 and (currentK,currentM)==(K,M)
    assert degree<=4*(d-b-3)*(b+2)**(b-1)*D**b<=n**b
    assert M*d>= (b+1)*N
    cases+=1
noise_cases=0
for b in (2,3,4,5):
 for d in range(b+7,101):
  for r in (2**d,2**d+1):
   for m in ((3*r+1)//2,5*r//3):
    D=m-r+1;u=(d-b-1)*D-3*r;q=(4*r+1)**2
    assert 2*(D-1)>=r and D<=r and (d-1)*D+1<=q
    # log_2(failure bound) <= (d-5-2 floor(log_2 r))*r+d+1.
    # Uses log_2 Q>=8+4 floor(log_2 r), Delta>=r/2,
    # and -u log_2(1-1/q)<=3u/q<d.
    assert 3*u<d*q
    assert (d-5-2*(r.bit_length()-1))*r+d+1<0
    noise_cases+=1
out=dict(status='passed',cases=cases,constant_degree_noise_bound_cases=noise_cases,b_values=[2,3,4,5],d_up_to=100,r_range=[40,300],m_cases='lower endpoint, middle, new five-thirds upper endpoint',scope='Exact integer identities, characteristic guard, old and new block admissibility, constant extension-degree accounting, and sufficient logarithmic noise-bound inequalities; no numerical proof of asymptotic source existence.')
Path(__file__).with_name('parameter_family_verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
