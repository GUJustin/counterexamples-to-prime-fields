"""Independent integer replay with a coarser Fourier bound, no helper imports."""
from math import comb,isqrt
from pathlib import Path
import json,time
BASE=Path(__file__).resolve().parent

def replay(b,r,n,m,d,target,prescription):
 assert all(b%j for j in range(2,isqrt(b)+1));p=2**b-1;s=4
 for j in range(b-2):s=(s*s-2)%p
 assert s==0 and p>(4*r+2)**2 and p>2*m*m
 assert n%4==2;K=n//2;D=(K+1)//2;assert (n//2-m)%r==0
 q=(n//2-m)//r;L=comb(m,D);assert q>0 and 1<=D<m
 # lambda <= (4r+2)/sqrt(p), conditioning >=1-2m²/p,
 # hence delta <= p^r/L + ((4r+2)^(2r+2)+2m²)/(p-2m²).
 den=L*(p-2*m*m)
 num=p**r*(p-2*m*m)+L*((4*r+2)**(2*r+2)+2*m*m)
 assert q*num*2**(d+target+1)<den
 assert (p-1)*2**(target+1)<(2**d+1)**q
 u=2*r+1
 assert u*(b-1)>n
 assert n**u*2**(n+u*prescription)<p**u
 return dict(b=b,r=r,n=n,K=K,m=m,D=D,blocks=q,far_fraction=f'{2*r}/{u}',failure_less_than=f'2^-{target}',prescription_less_than=f'2^-{prescription}',gamma=f'2^-{d}')

if __name__=='__main__':
 start=time.monotonic();rows=[]
 for args in [(521,1,1458,685,15,134,24),(521,2,2518,1211,28,128,6),(521,3,3518,1711,39,97,6),(1279,3,8678,4186,31,298,26),(1279,5,13782,6751,56,284,12),(1279,10,26218,12949,84,60,15)]:rows.append(replay(*args))
 out=dict(status='passed',rows=rows,seconds=time.monotonic()-start,scope='No construction-helper imports. Coarser analytic Fourier estimate, exact integer probability terms, independent Lucas-Lehmer and integer Elias/prescription replay. A generator probability certificate, not individual-sample coverage verification.')
 (BASE/'multiblock_independent_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
