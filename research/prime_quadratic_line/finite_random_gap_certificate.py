"""Exact finite existence certificate; no sampled word or fresh matrix."""
from fractions import Fraction as F
from math import factorial, isqrt
from pathlib import Path
import json
import time

start=time.monotonic()
L,d=250000,3
A=2*L-2
T=A+d
n=T*T//2+1
N0=L*(L-1)
t=n-N0

def prime_trial(v):
    if v<2 or (v>2 and v%2==0): return False
    return all(v%j for j in range(3,isqrt(v)+1,2))

def nextprime(v):
    if v<=2:return 2
    v += not(v%2)
    while not prime_trial(v):v+=2
    return v

# Choose p at or just above the real root p^d=t^d L/d!.
target=t**d*L
lo,hi=0,t*L
while hi-lo>1:
    mid=(lo+hi)//2
    if mid**d*factorial(d)<target:lo=mid
    else:hi=mid
p=nextprime(hi)
q=nextprime(L)
assert L<=q<=2*L and q%2==1
assert p-1>32*L*L
assert p>N0+t+1 and p>2*L+4
assert T*T<2*n and N0>=T and A>5

# Sidon certificate: the proof reconstructs unordered pairs from sum and
# sum of squares modulo q. This checks the finite range, without L^2 pairs.
max_b=max(2*q*i+(i*i%q) for i in range(L))
assert max_b<8*L*L and 4*max_b<p-1

def falling(v,k):
    z=1
    for j in range(k):z*=v-j
    return z

moments=[]
for k in range(1,5):
    kd=k*d
    assert t-6*L-kd>=kd
    # Bernoulli is a lower bound for the no-additional-hit factor.
    bernoulli=1-F(k*(t-kd),p-2*L)
    assert bernoulli>0
    lower=F(falling(L,k)*falling(t-6*L-kd,kd),
            factorial(d)**k*p**kd)*bernoulli
    upper=F(falling(L,k)*falling(t,kd),
            factorial(d)**k*(p-2*L)**kd)
    assert 0<lower<=upper
    moments.append((lower,upper))
singleton= moments[0][0]-moments[1][1]+moments[2][0]/2-moments[3][1]/6
assert singleton>F(1,4)

# binom(t,s)<= (e*t/s)^s < (3*t/s)^s. All nonbank
# (lambda,h) pairs are excluded already at total agreement A+1.
s=L-1
assert F(3*t,(p-2*L)*s)<=F(1,2)
# This exact bit-length inequality implies 2^s>p^6 and hence
# p^4*2^(-s)<p^(-2), without materializing a huge rational.
assert s>6*p.bit_length()
good_expectation=(p-2)*singleton-F(1,p)
guaranteed=good_expectation.numerator//good_expectation.denominator
assert guaranteed>n

# Entire first-order upper estimate is bounded by 7T/8+3sqrt(T)/4<T.
# These three checks use rational powers only.
assert F(3*n,2)<F(49*T*T,64)
assert F(3*n,8)<F(81*T*T,256)
assert T>36

def encode(x):return {'numerator':str(x.numerator),'denominator':str(x.denominator)}
out=dict(status='PASS', L=L,d=d,p=p,q=q,n=n,N0=N0,t=t,A=A,T=T,
         prime_checks={'method':'exhaustive odd trial division',
                       'p_limit':isqrt(p),'q_limit':isqrt(q)},
         sidon={'max_b':max_b,'guard_32L2':32*L*L,
                'four_max_b':4*max_b},
         factorial_moments=[{'k':k+1,'lower':encode(a),'upper':encode(b)}
                            for k,(a,b) in enumerate(moments)],
         singleton_probability_lower=encode(singleton),
         nonbank_failure_upper='1/p^2 (strict)',
         good_singleton_expectation_lower=encode(good_expectation),
         guaranteed_singleton_finite_labels=guaranteed,
         ratio_to_n_lower=encode(F(guaranteed,n)),
         note='Existence certificate using exact rational probability bounds; not an explicit received word.',
         seconds=time.monotonic()-start)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['factorial_moments','good_singleton_expectation_lower','singleton_probability_lower']}))
