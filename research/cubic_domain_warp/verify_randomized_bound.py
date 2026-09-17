"""Exact failure bound for the direct randomized cubic construction."""
from fractions import Fraction as F
from math import comb,isqrt,prod
from pathlib import Path
import json,time
from audit_finite_independent import prime
BASE=Path(__file__).resolve().parent


def bits_below(x):
 assert x>0
 bits=x.denominator.bit_length()-x.numerator.bit_length()
 while bits>=0 and x.numerator*(1<<bits)>=x.denominator:bits-=1
 return bits


def bound(b,n,m,s,hbits,d):
 p=prime(b);K=n//2;t=K+s+1;N=m-1;R=p-N;U=p-1;q=n-N
 assert n==2*K and p>2*m*m and 1<=t<m<n
 Q=comb(m-1,t-1)
 V=prod(comb(m,j+1)-comb(m-t,j+1)-comb(t,j+1)+1 for j in range(1,3*s+1))
 mu=F(Q,V);H=p*(1<<hbits);gamma=F(1,1<<d)
 # Use the larger integer remainder from the unrestricted point-count
 # theorem, so this certificate does not rely on the sharper Cor5.6.
 B=F(p+(t-1)*(t-2)*(isqrt(p)+1)+5*t**5,p-comb(m,2))
 delta=F(U,H)+F(U,R)*B-1
 parts=(F(H,1)/mu,delta/gamma,U*(gamma/(1+gamma))**q)
 failure=sum(parts,F(0));assert delta>0
 gap=t-K
 assert p**gap*t**t*(n-t)**(n-t)>n**n
 prescription_bits=b-(n+gap-1)//gap-n.bit_length()
 assert prescription_bits>=0
 assert n**gap*2**(n+prescription_bits*gap)<p**gap
 out=dict(prime_exponent=b,n=n,K=K,m=m,threshold=t,s=s,padding=q,
          class_threshold_extra_bits=hbits,tolerance_denominator_bits=d,
          failure_probability_less_than_power_two=-bits_below(failure),
          component_failure_bits=[bits_below(x) for x in parts],
          exact_failure_numerator=str(failure.numerator),
          exact_failure_denominator=str(failure.denominator),
          prescription_fraction_less_than_power_two=-prescription_bits,
          exact_relative_far_fraction=f'1/{gap}',strict_elias=True)
 return out

if __name__=='__main__':
 start=time.monotonic();rows=[]
 for hbits in (140,145,150,155,160):
  for d in (7,8,9,10):
   rows.append(bound(521,990,900,1,hbits,d))
 best=min(rows,key=lambda r:r['failure_probability_less_than_power_two'])
 assert best['failure_probability_less_than_power_two']<=-128
 out=dict(status='passed',best=best,parameter_trials=len(rows),seconds=time.monotonic()-start,
          scope='Exact upper bound on the randomized generator failure probability, assuming the written sampling theorem. This does not certify any particular sample has complete coverage.')
 (BASE/'randomized_bound_verification.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({**out,'best':{k:v for k,v in best.items() if not k.startswith('exact_failure_')}},indent=2))
