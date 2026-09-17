"""Exact finite certificates and exhaustive small-field rational-line checks.
No protocol code or cryptographic verifier is used.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations
from math import comb, factorial, isqrt, prod
from pathlib import Path
import json
BASE=Path(__file__).resolve().parent


def ceil(q): return -((-q.numerator)//q.denominator)
def pairs(objects,bins):
    a,b=divmod(objects,bins)
    return bins*a*(a-1)//2+b*a

def min_bins(objects,budget):
    lo,hi=1,objects
    while lo<hi:
        mid=(lo+hi)//2
        if pairs(objects,mid)<=budget:hi=mid
        else:lo=mid+1
    assert pairs(objects,lo)<=budget
    assert lo==1 or pairs(objects,lo-1)>budget
    return lo

def sqrt_upper(q,scale=10**30):
    z=q*scale*scale
    a=isqrt(z.numerator//z.denominator)
    if a*a<z:a+=1
    answer=F(a,scale)
    assert answer*answer>=q
    return answer

def gram_bound(n,t,m):
    vs=[F(t*(n-t),n-1)*F(prod(n*n-i*i for i in range(1,j+1)),
              (2*j+1)*comb(2*j,j)**2*factorial(j)**2) for j in range(1,m+1)]
    pi=F(355,113)
    volume=(pi**(m//2)/factorial(m//2) if m%2==0 else
            2**m*pi**((m-1)//2)*factorial((m-1)//2)/factorial(m))
    denominator=volume*sqrt_upper((m+2)**m*prod(v+F(1,12) for v in vs))
    return ceil(F(comb(n,t))/denominator),vs,denominator

def ln_bounds(q,terms=48):
    assert 1<=q<=2
    z=(q-1)/(q+1)
    lower=2*sum((z**(2*j+1)/F(2*j+1) for j in range(terms)),F(0))
    tail=2*z**(2*terms+1)/((2*terms+1)*(1-z*z))
    return lower,lower+tail

def log2_bounds(q):
    e=q.numerator.bit_length()-q.denominator.bit_length()
    power=F(2**e) if e>=0 else F(1,2**(-e))
    if q<power:e-=1;power/=2
    mantissa=q/power
    assert 1<=mantissa<2
    lo,hi=ln_bounds(mantissa);l2,h2=ln_bounds(F(2))
    return F(e)+lo/h2,F(e)+hi/l2

def lucas_lehmer(b):
    assert all(b%d for d in range(2,isqrt(b)+1))
    p=2**b-1;s=4
    for _ in range(b-2):s=(s*s-2)%p
    assert s==0
    return p

def certificate(b,n,k,t):
    p=lucas_lehmer(31 if b==124 else b)
    q=p**4 if b==124 else p
    r=t-k;m=r-1
    assert 1<=k<t<n<p and m>=1
    # Exact sufficient characteristic-Elias inequality.
    assert p**r*t**t*(n-t)**(n-t)>n**n
    N,variances,den=gram_bound(n,t,m)
    B=k*comb(N,2)-pairs(N*t,n)
    assert B>=0
    Q=q-n
    J=min_bins(N,B//Q)
    assert J<=q
    ratio=F(J**r*k**k*(n-k)**(n-k),n**(n+r))
    lower,upper=log2_bounds(ratio)
    lower/=r;upper/=r
    decimal_lower=(lower*10**5).__floor__()
    assert (upper*10**5).__floor__()==decimal_lower
    return dict(field_characteristic=p,alphabet_size=q,n=n,k=k,t=t,m=m,
                source_list_lower_bound=N,pair_collision_budget=B,
                admissible_poles=Q,label_lower_bound=J,
                concurrency_upper_bound=(n-k)//r,
                excess_bits_certified_lower=f'{decimal_lower//10**5}.{decimal_lower%10**5:05d}',
                strict_elias_sufficient_inequality=True,
                gram_variances=[str(v) for v in variances],
                concentration_denominator_upper=str(den))

def polynomial(roots,p):
    a=[1]
    for x in roots:
        b=[0]*(len(a)+1)
        for j,c in enumerate(a):b[j]=(b[j]-x*c)%p;b[j+1]=(b[j+1]+c)%p
        a=b
    return a

def evaluate(a,x,p):
    y=0
    for c in reversed(a):y=(y*x+c)%p
    return y

def small_checks():
    fixtures=total_poles=total_members=0
    saved=None
    for n in range(6,13):
      for k in range(1,n-2):
       for r in range(2,min(5,n-k)):
        t=k+r;s=r-1;p=31
        groups=defaultdict(list)
        for A in combinations(range(n),t):
            groups[tuple(sum(comb(x,j) for x in A) for j in range(1,s+1))].append(A)
        supports=max(groups.values(),key=len);N=len(supports)
        if N<2:continue
        fs=[polynomial(A,p) for A in supports]
        assert all(f[k+1:]==fs[0][k+1:] for f in fs)
        W=[0]*(k+1)+fs[0][k+1:]
        candidates=[[(W[j]-f[j])%p for j in range(k+1)] for f in fs]
        incidences=[sum(x in A for A in supports) for x in range(n)]
        exact_B=k*comb(N,2)-sum(comb(i,2) for i in incidences)
        balanced_B=k*comb(N,2)-pairs(N*t,n)
        assert 0<=exact_B<=balanced_B
        rows=[];sum_collisions=0
        for tau in range(n,p):
            groups_at_tau=defaultdict(list)
            for i,P in enumerate(candidates):groups_at_tau[-evaluate(P,tau,p)%p].append(i)
            collision=sum(comb(len(g),2) for g in groups_at_tau.values())
            sum_collisions+=collision
            rows.append((collision,tau,groups_at_tau))
        assert sum_collisions<=exact_B
        collisions,tau,labels=min(rows,key=lambda x:x[0])
        guarantee=min_bins(N,balanced_B//(p-n))
        assert len(labels)>=guarantee
        selected=[]
        for z,indices in labels.items():
            i=indices[0];P=candidates[i]
            # Synthetic division of P(X)-P(tau) by X-tau.
            out=[0]*k;out[-1]=P[-1]
            for j in range(k-2,-1,-1):out[j]=(P[j+1]+tau*out[j+1])%p
            for x in range(n):
                inverse=pow(x-tau,-1,p)
                received=(evaluate(W,x,p)+z)*inverse%p
                assert (received==evaluate(out,x,p))==(x in supports[i])
            selected.append((z,out))
        max_concurrency=1
        for (z1,P1),(z2,P2) in combinations(selected,2):
            slope=[(b-a)*pow(z2-z1,-1,p)%p for a,b in zip(P1,P2)]
            intercept=[(a-z1*b)%p for a,b in zip(P1,slope)]
            occupancy=sum(all(c==(a+z*b)%p for a,b,c in zip(intercept,slope,P)) for z,P in selected)
            max_concurrency=max(max_concurrency,occupancy)
        assert max_concurrency<=(n-k)//r
        fixtures+=1;total_poles+=p-n;total_members+=N
        if saved is None or len(labels)>saved['labels']:
            saved=dict(p=p,n=n,k=k,t=t,N=N,pole=tau,labels=len(labels),guaranteed_labels=guarantee,
                       maximum_concurrency=max_concurrency)
    return dict(fixtures=fixtures,poles=total_poles,bank_members=total_members,largest_example=saved)


def main():
    small=small_checks()
    discovered=json.loads((BASE/'search_results.json').read_text())['best']
    records=[]
    for b in (31,61,124,127):
        best=[]
        for row in discovered[str(b)][:4]:
            best.append(certificate(b,row['n'],row['k'],row['t']))
        records.append(max(best,key=lambda x:float(x['excess_bits_certified_lower'])))
    result=dict(status='PASS',small_field_checks=small,finite_certificates=records,
                scope='Mathematical existence certificates for affine received lines; finite comparison uses c1=c2=1. No global optimization claim.')
    (BASE/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
