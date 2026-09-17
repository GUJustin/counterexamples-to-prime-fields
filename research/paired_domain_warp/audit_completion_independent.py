"""Independent coarser integer completion certificates, no helper imports."""
from math import comb,isqrt
from pathlib import Path
import json,time
BASE=Path(__file__).resolve().parent

def dyadic(numerator,denominator,budget):
 # Independent bit-interval selection; round down further on equality.
 a=max(0,denominator.bit_length()-numerator.bit_length()-budget)
 while numerator*(1<<(a+budget))>=denominator:
  a-=1
  if a<0:return None
 while numerator*(1<<(a+budget+1))<denominator:a+=1
 return a

def replay(b,r,n,t,prescription,target=None):
 assert all(b%d for d in range(2,isqrt(b)+1));p=(1<<b)-1;ll=4
 for _ in range(b-2):ll=(ll*ll-2)%p
 assert ll==0 and n%4==2
 K=n//2;D=(K+1)//2;m=n//2-r-2*t;d=D-t;assert 1<=d<m
 C=4*r+4 # weaker than the primary4r+2
 assert p>(n+1)**2 and p>C*C and p>2*m*m
 L=comb(m,d);den=L*(p-2*m*m)
 num=p**r*(p-2*m*m)+L*(C**(2*r+2)+2*m*m)
 budget=0 if target is None else target+(t+1).bit_length()
 a=dyadic(num,den,budget);assert a is not None;seq=[a]
 for _ in range(t):
  # p-8 is weaker than the primaryp-4 conditioning denominator.
  num=p+C*C*(1<<a);den=(p-8)*(1<<(2*a))
  a=dyadic(num,den,budget);assert a is not None;seq.append(a)
 assert (p-1)**r<(1<<a)
 if target is not None:assert (t+1)*(1<<target)<(1<<budget)
 u=2*r+1;assert u*(b-1)>n
 assert n**u*(1<<(n+u*prescription))<p**u
 return dict(b=b,r=r,n=n,K=K,base_orbits=m,base_support=d,sprinkling_pairs=t,dyadic_exponents=seq,mode='existence' if target is None else 'randomized',failure_less_than=None if target is None else f'2^-{target}',prescription_less_than=f'2^-{prescription}',direction_weight=2*r)

if __name__=='__main__':
 start=time.monotonic();rows=[]
 for args in [(61,1,158,4,1,None),(127,1,294,5,20,None),(521,2,2518,3,6,None),(521,2,2518,8,6,88),(1279,3,8678,11,26,228),(1279,5,13782,13,12,221),(1279,10,26218,12,15,None),(1279,10,26218,18,15,123)]:rows.append(replay(*args))
 out=dict(status='passed',rows=rows,seconds=time.monotonic()-start,scope='Independent coarser character and conditioning constants, integer dyadic rounding, Lucas-Lehmer primality, strict Elias and numerical prescription. Existence and randomized bounds distinguished; no individual-sample complete-image certification.')
 (BASE/'completion_independent_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
