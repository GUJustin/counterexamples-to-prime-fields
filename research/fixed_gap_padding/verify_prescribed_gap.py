"""Exact arithmetic and finite-field checks for prescribed-gap padding.

The entropy asymptotic is proved in PRESCRIBED_GAP.md, not inferred
from these finite checks. All reported moment lower bounds are integers.
"""
from fractions import Fraction
from math import comb, floor, log2
from pathlib import Path
import json
import time
from verify_anchored_padding import fixture, value


def list_fixture(row):
    B,p,n,K,A=(row[key] for key in ('B','p','n','k','A'))
    old_count=9*B-1
    domain=row['domain'][:old_count]+[1]+row['domain'][old_count:-1]
    assert len(domain)==n and len(set(domain))==n
    def multiply_x_minus_one(poly):
        out=[0]*(len(poly)+1)
        for j,c in enumerate(poly):
            out[j]=(out[j]-c)%p
            out[j+1]=(out[j+1]+c)%p
        return out
    word=multiply_x_minus_one(row['old_word_coefficients'])
    candidates=[multiply_x_minus_one(P) for P in row['candidate_coefficients']]
    assert len(word)-1==A and all(len(P)-1<K for P in candidates)
    counts=[sum(value(P,x,p)==value(word,x,p) for x in domain) for P in candidates]
    assert counts==[A]*len(candidates)
    assert len({tuple(P) for P in candidates})==len(candidates)
    return dict(B=B,p=p,n=n,K=K,A=A,domain=domain,
                word_coefficients=word,candidate_coefficients=candidates,
                exact_agreement_counts=counts,
                scope='Selected list lower bound, not exhaustive list enumeration.')


def ceiling(x):
    return -(-x.numerator//x.denominator)


def parameter_check(rho, eta):
    h=-float(rho)*log2(float(rho))-(1-float(rho))*log2(1-float(rho))
    m=floor(h/(float(eta)**2*log2(1/float(eta))))
    a=rho+eta
    t=ceiling(a*m/(1-eta/2))
    k=floor(rho*t/a)
    s=t-k
    assert 1<=k<t<m
    assert a*m<t<a*m/(1-eta)
    length_per_fiber=Fraction(t,a)
    dimension_per_fiber=rho*length_per_fiber
    B=length_per_fiber.denominator*dimension_per_fiber.denominator
    n=int(B*length_per_fiber)
    K=int(B*dimension_per_fiber)
    A=B*t
    q=n-m*B+1
    assert Fraction(K,n)==rho and Fraction(A-K,n)==eta
    assert q>=1 and B*(k-1)<=K<A
    assert K-1+q<A
    numerator=comb(m-1,t-1)
    denominator=1
    for j in range(1,s+1):
        denominator*=comb(m,j+1)-comb(m-t,j+1)-comb(t,j+1)+1
    L=(numerator+denominator-1)//denominator
    C=(1-Fraction(a*m,t))*L
    # bit lengths give a conservative exact integer lower bound on log2(C).
    log_lower=C.numerator.bit_length()-1-C.denominator.bit_length()
    return dict(rho=str(rho),eta=str(eta),m=m,k=k,t=t,s=s,
                fiber_multiple=B,n=n,K=K,A=A,added=q,
                log2_coefficient_lower=log_lower,
                normalized_log_lower=float(eta)**2*log2(1/float(eta))*log_lower,
                asymptotic_normalized_target=h*h/2)


def main():
    start=time.monotonic()
    rows=[parameter_check(rho,Fraction(1,2**j))
          for rho in (Fraction(1,4),Fraction(1,2),Fraction(3,4))
          for j in range(5,10)]
    fixtures=[fixture(B,retuned=True) for B in (2,4)]
    for row in fixtures:
        assert Fraction(row['k'],row['n'])==Fraction(5,21)
        assert Fraction(row['A']-row['k'],row['n'])==Fraction(5,21)
    result=dict(status='passed',parameter_checks=rows,fixtures=fixtures,
                list_fixtures=[list_fixture(row) for row in fixtures],
                seconds=time.monotonic()-start,
                scope='Exact rational parameter inequalities and moment bounds; two complete prime-field padding fixtures. The all-gap asymptotic and splitting-prime existence use the written proof.')
    Path(__file__).with_name('prescribed_gap_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({**result,'fixtures':[{k:v for k,v in row.items() if k in
        {'B','p','n','k','A','nearby_challenges','global_joint_agreement_upper'}} for row in fixtures]},indent=2))


if __name__=='__main__':
    main()
