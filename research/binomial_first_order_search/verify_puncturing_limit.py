"""Exact algebra and domain accounting for the puncturing-limit proof.

The analytic character-sum input is inherited from the preceding proof;
this checker makes no claim to verify that input by finite sampling.
"""
from fractions import Fraction as Q
from pathlib import Path
import json
import sympy as s


def main():
    r, b = s.symbols('r b')
    F = lambda a: (8-r)*a*a-6*r*a+r*(4*r-5)
    identities = [
        F(Q(1,4)+3*r/4)+(r-1)*(9*r*r-49*r+8)/16,
        F(Q(1,2)+r/4)+(r-2)*(r*r-42*r+16)/16,
    ]
    T = r*(7-2*r)/(4+r)
    identities.append(F(T)+4*r*(r-2)*(r-1)*(r*r-16*r+10)/(r+4)**2)
    assert all(s.cancel(expr)==0 for expr in identities)

    # Negativity of the quadratic factors on the stated rate intervals:
    # each value starts negative and each derivative remains negative.
    assert 9*Q(1,4)**2-49*Q(1,4)+8 < 0
    assert 18*Q(1,2)-49 < 0
    assert Q(1,2)**2-42*Q(1,2)+16 < 0
    assert 2*Q(2,3)-42 < 0
    # 5/8 < 8-3sqrt(6) < 2/3, without rounded square roots.
    assert Q(59,24)**2 > 6 > Q(22,9)**2
    assert 2*Q(5,8)-1-Q(5,8)**2/4 > 0
    assert 2-Q(1,2) > 0  # derivative 2-r/2 stays positive through r=1.
    # sqrt(2^22)=2048: the entire normalized error is below 1/4.
    assert Q(504,2048)+Q(37,2**22) < Q(1,4)
    # Lambda<42sqrt(k) for k>=2: divide by sqrt(k), bound both terms
    # at k=2, and isolate the only cross-term before squaring.
    # (8sqrt(9/2)+24/sqrt(2))=24sqrt(2)<42.
    assert 24**2*2 < 42**2

    cases=0
    for k in range(2,101):
        for n in range(k+1,4*k+1):
            bnd=min(Q(n,2),Q(n,4)+Q(k,2))
            ns=min(n,2*k)
            assert Q(n-ns,4)+Q(ns,2)==bnd
            # Other admissible square/nonsquare allocations only lower
            # this increasing affine function of the nonsquare count.
            assert ns>=max(0,n-2*k)
            cases+=1
    result={
        'status':'passed', 'symbolic_identities':len(identities),
        'domain_size_cases':cases, 'full_bank_list_bound_exclusive':2**23,
        'scope':'Exact algebra and domain accounting; Fourier and character-sum estimates are proved in the referenced notes, not verified by this finite checker.',
    }
    Path(__file__).with_name('puncturing_limit_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
