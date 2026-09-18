from fractions import Fraction as F
from math import prod,isqrt,factorial,comb
import json,pathlib,time
start=time.monotonic()
def prime(n):return n>1 and all(n%j for j in range(2,isqrt(n)+1))
def fall(n,k):return prod(range(n-k+1,n+1))
def bern(N,x,r):return sum((-1)**j*F(comb(N,j))*x**j for j in range(r+1))
def rat(x):return [str(x.numerator),str(x.denominator)]
L=1500;q=1511;p=18120497;d=3
assert prime(q) and prime(p) and L<=q<=2*L
b=[2*q*i+i*i%q for i in range(L)]
# Integer Sidon property follows from the quotient/remainder proof; no quadratic pair scan.
assert p-1>4*max(b)
A=2*L-2;T=A+d;n=(T*T+2)//2;t=n-L*(L-1);Q=F(1,p-2*L)
assert n<p and T*T<2*n
assert F(3*n,2)<2600**2 and F(3*n,8)<37**4 and 2600+37<T
lo=[];hi=[]
for k in range(1,5):
    N=t-k*d;x=k*Q
    # Odd/even binomial truncations bound (1-x)^N exactly by Bonferroni.
    el=bern(N,x,13);eu=bern(N,x,12)
    assert 0<el<eu<1
    low=F(fall(L,k)*fall(t-6*L-k*d,k*d),factorial(d)**k*p**(k*d))*el
    muprime=t*Q/(1-k*Q)
    assert muprime<d+1
    upper=F(fall(L,k)*fall(t,k*d),factorial(d)**k)*Q**(k*d)*eu*(1-muprime/(d+1))**(-k)
    assert low<upper
    lo.append(low);hi.append(upper)
P=lo[0]-hi[1]+lo[2]/2-hi[3]/6
R=L-1
# binom(t,R)<= (3t/R)^R; follows from R! >=(R/e)^R and e<3.
assert factorial(R)*3**R >= R**R
union=p**4*F(3*t,R*(p-2*L))**R
assert p*union<1
safe=((p-2)*P).numerator//((p-2)*P).denominator-1
assert safe>n
receipt=dict(L=L,q=q,p=p,d=d,n=n,A=A,T=T,t=t,max_exponent=max(b),sidon_modulus_guard=p-1-4*max(b),lower_factorial_moments=list(map(rat,lo)),upper_factorial_moments=list(map(rat,hi)),singleton_probability_lower=rat(P),singleton_probability_lower_decimal=float(P),guaranteed_canonical_singleton_labels=safe,guaranteed_final_singleton_labels=safe+1,guaranteed_ratio_to_n=F(safe+1,n).__float__(),nonbank_union_times_p_less_than_one=True,union_numerator_bits=union.numerator.bit_length(),union_denominator_bits=union.denominator.bit_length(),all_checks_pass=True,seconds=time.monotonic()-start,scope='Existence certificate from exact finite expectations; does not specify a received word or enumerate incidences')
pathlib.Path(__file__).with_suffix('.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({k:v for k,v in receipt.items() if k not in ['lower_factorial_moments','upper_factorial_moments','singleton_probability_lower']}))
