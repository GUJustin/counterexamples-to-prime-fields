#!/usr/bin/env python3
"""Pure Reed--Solomon list-size construction and exact finite audits."""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json
import random


def multiply(a,b,p):
    out = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j] = (out[i+j]+x*y) % p
    while len(out)>1 and out[-1]==0:
        out.pop()
    return out


def evaluate(poly,x,p):
    result = 0
    for c in reversed(poly):
        result = (result*x+c) % p
    return result


def construct(domain,k,s,p,counts):
    n,a = len(domain),len(domain)-k
    assert k>=2 and 1<=s<=a and len(set(domain))==n
    L = max(1,(a-1)//s)
    if L==1:
        center = [0]*n
        return [tuple([0])],center,L
    t = L-1
    common,x = domain[:k-2],domain[k-2:]
    A,B = x[:2]
    zero_points = x[:s+2]
    z = [x[s+2]]
    received = {u:0 for u in zero_points}
    received[z[0]] = 1
    lines = [(0,0)]
    offset = s+3
    for j in range(1,t+1):
        anchor = A if j%2 else B
        slope = received[z[j-1]]*pow((z[j-1]-anchor)%p,-1,p) % p
        assert slope != 0
        line = ((-slope*anchor)%p,slope)
        fresh = x[offset:offset+s]
        assert len(fresh)==s
        for u in fresh:
            assert u not in received
            received[u] = evaluate(line,u,p)
        z.append(fresh[0])
        assert all(evaluate(line,u,p)==received[u]
                   for u in [anchor,z[j-1]]+fresh)
        lines.append(line)
        offset += s
    assert offset == L*s+3
    assert len(x)-offset == (a-1)%s
    for u in x[offset:]:
        received[u] = 0
    for i in range(1,t+1):
        for j in range(i+1,t+1):
            if (j-i)%2:
                assert lines[i]!=lines[j]
                continue
            first=second=1
            for r in range(i,j):
                anchor = A if r%2 else B
                other = B if r%2 else A
                first = first*(z[r]-anchor)%p
                second = second*(z[r]-other)%p
            assert (first==second)==(lines[i]==lines[j])
            if j-i==2:
                assert lines[i]!=lines[j]
            counts['same_anchor_collision_identities'] += 1
    F = [1]
    for h in common:
        F = multiply(F,[-h%p,1],p)
    polynomials = [tuple(multiply(F,list(line),p)) for line in lines]
    center = [0]*(k-2)+[evaluate(F,u,p)*received[u]%p for u in x]
    for polynomial in polynomials:
        assert len(polynomial)<=k
        agree = sum(evaluate(polynomial,u,p)==v for u,v in zip(domain,center))
        assert agree>=k+s
        counts['polynomial_agreement_checks'] += 1
        counts['coordinate_evaluations_checked'] += n
    assert len(set(polynomials))==len(set(lines))
    return polynomials,center,L


def interpolate(xs,ys,p):
    result = [0]*len(xs)
    for i,(x,y) in enumerate(zip(xs,ys)):
        basis,denominator = [1],1
        for j,z in enumerate(xs):
            if i==j:
                continue
            basis = multiply(basis,[-z%p,1],p)
            denominator = denominator*(x-z)%p
        scale = y*pow(denominator,-1,p)%p
        for j,c in enumerate(basis):
            result[j] = (result[j]+scale*c)%p
    while len(result)>1 and result[-1]==0:
        result.pop()
    return tuple(result)


def entire_list_at_center(domain,center,k,s,p):
    candidates = set()
    for positions in combinations(range(len(domain)),k):
        candidates.add(interpolate([domain[i] for i in positions],
                                   [center[i] for i in positions],p))
    return {poly for poly in candidates
            if sum(evaluate(poly,x,p)==y for x,y in zip(domain,center))>=k+s}


def main():
    rng = random.Random(2026091518)
    counts = Counter()
    for n in range(4,31):
        for k in range(2,n-1):
            a = n-k
            p = 2147483647
            domain = rng.sample(range(p),n)
            for s in range(1,a):
                polynomials,center,L = construct(domain,k,s,p,counts)
                assert len(set(polynomials))==L
                counts['large_field_fixtures'] += 1
                counts['nondivisible_surplus_fixtures'] += int(a%s!=0)
                counts['fixtures_with_k_below_2s'] += int(k<2*s)
            counts['large_field_domains_with_all_surpluses'] += 1
    first_collision = None
    for p,n,k,s in [(11,9,2,1),(17,15,2,2),(31,25,3,3)]:
        for trial in range(150):
            domain = rng.sample(range(p),n)
            polynomials,center,L = construct(domain,k,s,p,counts)
            counts['small_field_fixtures'] += 1
            if len(set(polynomials))<L:
                counts['small_field_repetition_fixtures'] += 1
                if first_collision is None and s>=2:
                    first_collision = dict(p=p,n=n,k=k,s=s,domain=domain,
                                           target_list_size=L,
                                           distinct_constructed_polynomials=len(set(polynomials)))
    assert first_collision is not None
    exact_centers = []
    for n,k,s in [(9,2,2),(10,2,2),(11,2,3),(12,2,3),(12,3,2),
                  (14,4,3),(14,6,3),(8,3,5)]:
        p = 65537
        domain = rng.sample(range(p),n)
        polynomials,center,L = construct(domain,k,s,p,counts)
        actual = entire_list_at_center(domain,center,k,s,p)
        assert set(polynomials)<=actual
        exact_centers.append(dict(p=p,n=n,k=k,s=s,target_list_size=L,
                                  exact_list_at_constructed_center=len(actual)))
    mobius_checks = 0
    for p in [5,7,11]:
        for A in range(p):
            for B in range(p):
                if A==B:
                    continue
                values = [(z-A)*pow((z-B)%p,-1,p)%p for z in range(p) if z!=B]
                assert len(values)==len(set(values))==p-1
                mobius_checks += 1
    arithmetic = grouped_arithmetic = 0
    for n in range(4,81):
        for k in range(2,n-1):
            a=n-k
            summed_pairs=0
            for s in range(1,a):
                L=(a-1)//s
                t=L-1
                u,v=(t+1)//2,t//2
                summed_pairs += u*(u-1)//2+v*(v-1)//2
                assert (L+1)*(a-s)<=L*a
                assert L*s+3<=a+2
                assert (a+2)-(L*s+3)==(a-1)%s
                old=a//s-1
                assert L==old+int(a%s!=0)
                # Logarithmic certificates; never construct the enormous field bound.
                assert 1+(L*k).bit_length() <= (8*a-L-2)*n
                assert (a*a).bit_length() <= 8*a*n
                assert 2*n-1 < 8*a*n
                assert (2*a-1).bit_length() <= 2*a*n
                arithmetic += 1
            assert 2*summed_pairs < (a-1)**2
            grouped_arithmetic += 1
    result = dict(status='all assertions passed',counts=dict(counts),
                  exact_center_lists=exact_centers,
                  mobius_injectivity_checks=mobius_checks,
                  allocation_and_probability_profiles=arithmetic,
                  combined_lower_failure_profiles=grouped_arithmetic,
                  genuine_small_field_repetition=first_collision,
                  scope='Pure coding theory. Finite center lists are exhaustive at those centers; generic global upper bounds use the cited rank theorem.')
    target=Path(__file__).with_name('astra_rs_all_surplus_verified.json')
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
