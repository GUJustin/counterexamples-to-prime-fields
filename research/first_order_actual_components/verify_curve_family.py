#!/usr/bin/env python3
"""Exact classification and projective-section checks for an actual joint curve."""
import itertools
import json
from pathlib import Path
from arithmetic import add, mul, deriv, trim, eval_poly


def candidate(a,D,p):
    return [pow(a,-1,p)]+[pow(a,D-j,p) for j in range(1,D+1)]


def residual(P,z,D,p):
    R=[-1%p,z]+[0]*(D-1)+[1]
    return add(add(mul(R,deriv(P,p),p),mul(deriv(R,p),P,p),p,-1),mul(P,P,p),p)


def exhaustive(p,D,expect_classification):
    expected={(z,(0,)) for z in range(p)}
    for a in range(1,p):
        z=(pow(a,-1,p)-pow(a,D,p))%p
        expected.add((z,tuple(candidate(a,D,p))))
    actual=set();tested=0
    for coeff in itertools.product(range(p),repeat=D+1):
        P=trim(list(coeff))
        for z in range(p):
            tested+=1
            if residual(P,z,D,p)==[0]:actual.add((z,tuple(P)))
    assert expected<=actual
    if expect_classification:assert actual==expected
    else:assert actual-expected
    return dict(p=p,D=D,tested_pairs=tested,actual_solutions=len(actual),
                predicted_solutions=len(expected),extra_solutions=len(actual-expected),
                characteristic_hypothesis=p>D+1)


def prime(p):
    return p>=2 and all(p%d for d in range(2,int(p**0.5)+1))


def section(D):
    # Choose a prime with all (D+1)st roots of unity and a split,
    # reduced hyperplane section P(0)+lambda*z=0.
    p=next(p for p in range(2*(D+1)+1,20000,D+1) if prime(p))
    s=next(s for s in range(1,p) if pow(s,D+1,p)!=1)
    lam=pow(pow(s,D+1,p)-1,-1,p)
    roots=[]
    for a in range(1,p):
        z=(pow(a,-1,p)-pow(a,D,p))%p;P=candidate(a,D,p)
        assert residual(P,z,D,p)==[0]
        if (P[0]+lam*z)%p==0:roots.append(a)
    assert len(roots)==D+1
    assert all(pow(a,D+1,p)==pow(s,D+1,p) for a in roots)
    # The section polynomial is (1+lambda)-lambda*a^(D+1).
    assert lam and (1+lam)%p and (D+1)%p
    assert all((-lam*(D+1)*pow(a,D,p))%p for a in roots)
    # The coordinate of X^(D-1) recovers a, so this is a birational
    # parametrization. Its homogenized coordinates span every power
    # 1,a,...,a^(D+1), the rational normal curve of degree D+1.
    assert all(candidate(a,D,p)[D-1]==a for a in roots)
    return dict(D=D,p=p,lambda_value=lam,section_points=len(roots),
                total_curve_degree_including_zero=D+2,
                proposed_bound=3*(1+2*(1+2*max(0,2*D-3))))


def main():
    result={'status':'PASS',
            'exhaustive_classifications':[exhaustive(7,2,True),exhaustive(7,3,True),exhaustive(11,2,True)],
            'characteristic_negative_control':exhaustive(3,2,False),
            'split_reduced_sections':[section(D) for D in range(2,41)],
            'scope':'Checks the explicit nonlinear curve family and characteristic cutoff; the general component-degree theorem requires its geometric proof.'}
    for row in result['split_reduced_sections']:
        assert row['total_curve_degree_including_zero']<=row['proposed_bound']
    Path(__file__).with_name('first_order_curve_family_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='split_reduced_sections'},indent=2))
    print('Split reduced sections:',len(result['split_reduced_sections']))


if __name__=='__main__':main()
