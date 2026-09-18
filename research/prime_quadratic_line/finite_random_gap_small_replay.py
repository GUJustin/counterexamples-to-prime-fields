"""Independent arithmetic replay of upper's small finite gap-three gate."""
from fractions import Fraction
from pathlib import Path
from math import isqrt
import json

here=Path(__file__).parent
a=json.loads((here/'finite_gap3/certificate.json').read_text())
L,p,q,d=(a[x] for x in ('L','p','q','d'))
assert all(p%i for i in range(2,isqrt(p)+1))
assert all(q%i for i in range(2,isqrt(q)+1))
assert L<=q<=2*L
bmax=max(2*q*i+pow(i,2,q) for i in range(L))
assert bmax==a['max_exponent'] and p-1>4*bmax
A=2*L-2; T=A+d; n=T*T//2+1; t=n-L*(L-1)
assert (A,T,n,t)==tuple(a[x] for x in ('A','T','n','t'))
Q=Fraction(1,p-2*L)

def binomial_bounds(N,x):
    term=Fraction(1); total=term
    for j in range(1,14):
        term *= -Fraction(N-j+1,j)*x
        total += term
        if j==12: upper=total
    return total,upper

lo=[];hi=[]
for k in range(1,5):
    low=high=Fraction(1)
    for i in range(k):
        low *= L-i; high *= L-i
    for i in range(k*d):
        low *= Fraction(t-6*L-k*d-i,p)
        high *= (t-i)*Q
    for _ in range(k):
        for j in range(1,d+1):low/=j;high/=j
    el,eu=binomial_bounds(t-k*d,k*Q)
    low *= el
    ratio=t*Q/((1-k*Q)*(d+1))
    assert 0<ratio<1
    high *= eu
    for _ in range(k):high/=1-ratio
    assert low==Fraction(*map(int,a['lower_factorial_moments'][k-1]))
    assert high==Fraction(*map(int,a['upper_factorial_moments'][k-1]))
    lo.append(low);hi.append(high)
prob=lo[0]-hi[1]+lo[2]/2-hi[3]/6
assert prob==Fraction(*map(int,a['singleton_probability_lower']))
R=L-1
assert p**5*(3*t)**R < (R*(p-2*L))**R
safe=((p-2)*prob).__floor__()-1
assert safe==a['guaranteed_canonical_singleton_labels'] and safe>n
assert Fraction(3*n,2)<2600**2
assert Fraction(3*n,8)<37**4
assert 2600+37<T and T*T<2*n
out=dict(status='PASS',p=p,L=L,d=d,n=n,A=A,T=T,
         guaranteed_finite_singleton_labels=safe,
         guaranteed_total_singleton_labels=safe+1,
         excess_over_n=safe+1-n,
         mathematical_audit='Categorical domination, multinomial geometric tail, exact-support lower bound, and finite Bonferroni truncation verified.',
         scope='Exact finite existence; no received word enumerated.')
(here/'finite_random_gap_small_replay.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
