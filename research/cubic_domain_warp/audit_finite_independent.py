"""Independent complete-coverage replay using elementary moment boxes.

Imports no construction verifier. Uses the general Cafure–Matera bound
with the coarser integer remainder 5*t^5, not the characteristic-refined
3*t^4 bound used by the primary certificate.
"""
from math import comb,isqrt,prod
from pathlib import Path
import json,time
BASE=Path(__file__).resolve().parent


def prime(b):
 assert all(b%d for d in range(2,isqrt(b)+1))
 p=(1<<b)-1;x=4
 for _ in range(b-2):x=(x*x-2)%p
 assert x==0
 return p


def audit(b,n,m,s):
 p=prime(b);K=n//2;t=K+s+1;N=m-1;R=p-N;U=p-1;q=n-N
 assert n==2*K and p>2*m*m and 1<=3*s<t<m
 ranges=[comb(m,j+1)-comb(m-t,j+1)-comb(t,j+1)+1 for j in range(1,3*s+1)]
 support=comb(m-1,t-1);den=prod(ranges);L=(support+den-1)//den
 assert L>1
 Bnum=p+(t-1)*(t-2)*(isqrt(p)+1)+5*t**5
 Bden=p-comb(m,2)
 assert 4*L*R*Bden>3*U*(R*Bden+(L-1)*Bnum)
 if 2*q>=b:
  assert U<(1<<(2*q))
 else:
  assert q*p.bit_length()<100000
  # M/U is numerator/denominator; compare the missing expectation
  # entirely as integers, independently of the Fraction-based replay.
  image_num=L*R*Bden
  image_den=U*(R*Bden+(L-1)*Bnum)
  assert U*(image_den-image_num)**q<image_den**q
 gap=t-K
 assert p**gap*t**t*(n-t)**(n-t)>n**n
 # Compare directly against the exact nonzero-label count.
 assert U**gap>n**gap*(1<<n)
 return dict(prime_exponent=b,n=n,K=K,m=m,threshold=t,
             integer_moment_box_order=3*s,anchored_list_bits=L.bit_length(),
             image_fraction_proven_above='3/4',padding=q,
             expected_missing_nonzero_labels_less_than_one=True,
             exact_relative_far_fraction=f'1/{gap}',strict_elias=True)

if __name__=='__main__':
 start=time.monotonic();rows=[audit(127,214,202,1),audit(1279,3834,2556,3),audit(9689,18162,12108,1)]
 out=dict(status='passed',certificates=rows,seconds=time.monotonic()-start,
          scope='Independent finite arithmetic and primality replay; geometry remains a written proof and the point-count estimate a cited theorem.')
 (BASE/'independent_finite_audit.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2))
