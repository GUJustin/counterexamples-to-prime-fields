#!/usr/bin/env python3
"""Exact isolated first-order classification and nonzero-incidence checks."""
import itertools
import json
import math
import random
from pathlib import Path
from arithmetic import add,mul,scale,deriv,trim,eval_poly


def locator(roots,p):
    R=[1]
    for a in roots:R=mul(R,[-a%p,1],p)
    return R


def quotient(R,a,p):
    Q=[0]*(len(R)-1);Q[-1]=R[-1]
    for j in range(len(Q)-2,-1,-1):Q[j]=(R[j+1]+a*Q[j+1])%p
    assert mul(Q,[-a%p,1],p)==R
    return Q


def pieces(R,P,p):
    T=add(add(mul(R,deriv(P,p),p),mul(deriv(R,p),P,p),p,-1),mul(P,P,p),p)
    U=add(add(scale([0,0]+T,-1,p),scale([0]+mul(R,P,p),2,p),p),scale(mul(R,R,p),-2,p),p)
    return T,U


def expected(R,roots,p):
    Q={a:quotient(R,a,p) for a in roots}
    return {(a*b%p,tuple(add(Q[a],Q[b],p))) for i,a in enumerate(roots) for b in roots[i:]}


def exhaustive(p,roots,good=True):
    D=len(roots)-1;R=locator(roots,p);want=expected(R,roots,p);actual=set()
    for co in itertools.product(range(p),repeat=D+1):
        P=trim(list(co));T,U=pieces(R,P,p)
        if T==[0]:
            if U==[0]:actual.update((z,tuple(P)) for z in range(p))
            continue
        j=next(j for j,a in enumerate(T) if a)
        z=-(U[j] if j<len(U) else 0)*pow(T[j],-1,p)%p
        if add(U,scale(T,z,p),p)==[0]:actual.add((z,tuple(P)))
    assert want<=actual
    if good:assert actual==want
    else:assert actual-want
    local_max=0;checks=0
    if good:
        for x in range(p):
            points=[(z,eval_poly(P,x,p)) for z,P in actual]
            for f,g in itertools.product(range(p),repeat=2):
                hits=sum(y!=0 and y==(f+z*g)%p for z,y in points)
                assert hits<=len(roots)+1;local_max=max(local_max,hits);checks+=1
    return dict(p=p,D=D,roots=roots,polynomials_exhausted=p**(D+1),
                polynomial_challenge_pairs_covered=p**(D+2),
                predicted_pairs=len(want),actual_pairs=len(actual),extra_pairs=len(actual-want),
                all_local_received_values_checked=checks,maximum_nonzero_coordinate_incidence=local_max,
                characteristic_hypothesis=p>D+2)


def prime(p):
    return p>=2 and all(p%d for d in range(2,math.isqrt(p)+1))


def sidon_case(D):
    N=D+1;p=next(p for p in range(2*N**3+1,4*N**3) if prime(p))
    roots=[];products=set();a=1
    while len(roots)<N:
        if a not in roots and a*a%p not in products and all(a*b%p not in products for b in roots):
            products.update(a*b%p for b in roots);products.add(a*a%p);roots.append(a)
        a+=1;assert a<p
    assert len(products)==N*(N+1)//2
    R=locator(roots,p);solns=expected(R,roots,p)
    assert len(solns)==len(products)==len({z for z,P in solns})
    for z,P in solns:
        T,U=pieces(R,list(P),p);assert add(U,scale(T,z,p),p)==[0]
    n=2*D;A=(5*D+3)//4
    return dict(p=p,D=D,roots=roots,distinct_regular_isolated_labels=len(solns),
                n=n,agreement=A,linear_nearby_pair_bound=(D+2)*n//(A-D),
                greedy_forbidden_upper_bound=((N**3+N)//2),
                smallest_root=min(roots),largest_root=max(roots))


def derivative_identity_checks():
    rng=random.Random(1742);count=0
    for D in range(1,10):
        p=101;roots=list(range(1,D+2));R=locator(roots,p)
        for _ in range(12):
            P=trim([rng.randrange(p) for _ in range(D+1)]);z=rng.randrange(p)
            A=add(mul([z,0,1],P,p),scale([0]+R,2,p),p,-1)
            C=add(R,[0]+P,p,-1)
            wr=add(mul(deriv(A,p),C,p),mul(A,deriv(C,p),p),p,-1)
            T,U=pieces(R,P,p);assert wr==add(U,scale(T,z,p),p)
            count+=1
    return count


def triple_checks(p,roots):
    """Independently clear denominators for every distinct-label triple."""
    candidates=[(a*b%p,[-(a+b)%p,2],[a*b%p,-(a+b)%p,1])
                for i,a in enumerate(roots) for b in roots[i:]]
    checked=skipped=0; max_degree=0
    for triple in itertools.combinations(candidates,3):
        z=[row[0] for row in triple]
        if len(set(z))<3:
            skipped+=1;continue
        coefficients=[(z[1]-z[2])%p,(z[2]-z[0])%p,(z[0]-z[1])%p]
        assert sum(coefficients)%p==0
        assert sum(c*t for c,t in zip(coefficients,z))%p==0
        numerator=[0]
        for i,c in enumerate(coefficients):
            term=triple[i][1]
            for j in range(3):
                if i!=j:term=mul(term,triple[j][2],p)
            numerator=add(numerator,scale(term,c,p),p)
        assert numerator!=[0] and len(numerator)-1<=4
        max_degree=max(max_degree,len(numerator)-1);checked+=1
    return dict(p=p,roots=roots,distinct_label_triples=checked,
                skipped_label_collision_triples=skipped,maximum_numerator_degree=max_degree)


def integer_triple_bound(m,t,cap):
    """Avoid floating cube roots when evaluating the necessary inequality."""
    if t**3<=4*m*m:return None
    def allowed(L):return max(t*L-2*m,0)**3<=4*m*m*L**3
    lo,hi=0,cap+1
    while hi-lo>1:
        mid=(lo+hi)//2
        if allowed(mid):lo=mid
        else:hi=mid
    assert allowed(lo) and (lo==cap or not allowed(lo+1))
    return lo


def triple_incidence_checks():
    # Exhaust every multiplicity vector at small m and L to verify the
    # integer form of the convex lower bound, independent of the family.
    count=0
    for m in range(1,7):
        for L in range(1,7):
            for v in itertools.product(range(L+1),repeat=m):
                lhs=6*m*m*sum(math.comb(x,3) for x in v)
                rhs=max(sum(v)-2*m,0)**3
                assert lhs>=rhs;count+=1
    rows=[]
    for D in (64,256,512,1024,4096,1000000):
        n=2*D;A=(5*D+3)//4;r0=D+1;m=n-r0;t=A-r0
        rows.append(dict(D=D,n=n,agreement=A,root_coordinates=r0,
                         outside_domain_size=m,outside_agreement=t,
                         candidate_count=(D+1)*(D+2)//2,
                         nearby_label_upper_bound=integer_triple_bound(m,t,(D+1)*(D+2)//2)))
    return dict(exhausted_multiplicity_vectors=count,parameter_examples=rows)


def main():
    data={'status':'PASS','derivative_identity_checks':derivative_identity_checks(),
          'exhaustive_fixtures':[exhaustive(5,[1,2]),exhaustive(7,[1,2,3]),
                                 exhaustive(7,[1,2,3,4]),exhaustive(11,[1,2,3,4])],
          'characteristic_negative_control':exhaustive(3,[1,2],False)}
    rows=[]
    for D in (8,16,32,64):
        row=sidon_case(D);rows.append(row)
        print(json.dumps({k:v for k,v in row.items() if k!='roots'}),flush=True)
    data['prime_field_sidon_fixtures']=rows
    data['triple_checks']=[triple_checks(rows[0]['p'],rows[0]['roots']),
                          triple_checks(11,[1,2,3,4]),triple_checks(7,[1,2,3,4])]
    data['triple_incidence_checks']=triple_incidence_checks()
    data['scope']='Exact polynomial classification, separated prime-field labels, all local nonzero incidences on small fields, rational triple identities, and integer incidence bounds. This is not a quadratic proximity-gap lower bound.'
    Path(__file__).with_name('quadratic_isolated_verification.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({k:v for k,v in data.items() if k!='prime_field_sidon_fixtures'},indent=2))


if __name__=='__main__':main()
