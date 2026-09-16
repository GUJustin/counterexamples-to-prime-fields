"""Intersection- and unit-circle-aware evaluation collision bounds.

Exhaustively verifies a small F_31^2 example; large M31 conclusions use only
integer counting and the proved root bound, with no large support enumeration.
"""
from collections import Counter, defaultdict
from itertools import combinations
from math import comb, log2
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent


def minimum_pairs(items,bins):
    a,b=divmod(items,bins)
    return (bins-b)*comb(a,2)+b*comb(a+1,2)


def bank_from_pairs(items,pairs):
    lo,hi=1,items
    while lo<hi:
        mid=(lo+hi)//2
        if minimum_pairs(items,mid)<=pairs:hi=mid
        else:lo=mid+1
    assert minimum_pairs(items,lo)<=pairs
    assert lo==1 or minimum_pairs(items,lo-1)>pairs
    return lo


def certificate(p,m,h,d,n,extension):
    assert 1<=h<=m<=p+1 and (p+1)%m==0 and n>=1
    common_roots=comb(n,2)+minimum_pairs(n*(h-1),m-1)
    unit_rest=(p+1-m)*minimum_pairs(n,p)
    budget=d*comb(n,2)-common_roots-unit_rest
    assert budget>=0
    pole_count=p*p-p-1 if extension==2 else p**4-p*p
    old_poles=p*p-m if extension==2 else pole_count
    old=(n*old_poles+old_poles+(d-1)*(n-1)-1)//(old_poles+(d-1)*(n-1))
    pairs=budget//pole_count
    bank=bank_from_pairs(n,pairs)
    cauchy=(n*n+n+2*pairs-1)//(n+2*pairs)
    assert bank>=cauchy>=old
    return dict(p=p,M=m,h=h,d=d,N=str(n),extension_degree=extension,
                common_root_pair_sum_lower=str(common_roots),
                remaining_unit_circle_collisions_lower=str(unit_rest),
                total_allowed_pole_collisions_upper=str(budget),
                allowed_poles=str(pole_count),some_pole_pairs_upper=str(pairs),
                previous_bank=str(old),cauchy_bank=str(cauchy),new_bank=str(bank),
                gain_bits=log2(bank)-log2(old))


def toy():
    p=31;m=16;h=9;d=h-2
    def add(x,y):return ((x%p+y%p)%p)+p*((x//p+y//p)%p)
    def neg(x):return ((-(x%p))%p)+p*((-(x//p))%p)
    def mul(x,y):
        a,b=x%p,x//p;c,e=y%p,y//p
        return ((a*c-b*e)%p)+p*((a*e+b*c)%p)
    def power(x,n):
        out=1
        while n:
            if n&1:out=mul(out,x)
            x=mul(x,x);n//=2
        return out
    def frobenius(x):return x%p+p*((-(x//p))%p)
    unit=[x for x in range(1,p*p) if mul(x,frobenius(x))==1]
    assert len(unit)==p+1
    generator=next(x for x in unit if power(x,16)!=1)
    g=power(generator,2)
    domain=[power(g,j) for j in range(m)]
    assert len(set(domain))==m
    classes=defaultdict(list)
    for rest in combinations(range(1,m),h-1):
        subset=(0,)+rest
        classes[sum(subset)%m].append(subset)
    supports=max(classes.values(),key=len)
    n=len(supports)
    polynomials=[];constants=[]
    for support in supports:
        coeff=[1]
        for j in support:
            root=domain[j];new=[0]*(len(coeff)+1)
            for i,c in enumerate(coeff):
                new[i]=add(new[i],neg(mul(root,c)))
                new[i+1]=add(new[i+1],c)
            coeff=new
        constants.append(coeff[0])
        polynomials.append([neg(c) for c in coeff[1:-1]])
    assert len(set(constants))==1 and len(set(map(tuple,polynomials)))==n
    constant=constants[0]
    inv_constant=power(constant,p*p-2)
    def evaluate(poly,x):
        out=0
        for c in reversed(poly):out=add(mul(out,x),c)
        return out
    support_masks=[sum(1<<j for j in support) for support in supports]
    exact_intersections=sum((a&b).bit_count() for a,b in combinations(support_masks,2))
    incidence=Counter(j for support in supports for j in support)
    assert exact_intersections==sum(comb(v,2) for v in incidence.values())
    cert=certificate(p,m,h,d,n,2)
    assert exact_intersections>=int(cert['common_root_pair_sum_lower'])
    collision_sum=0;unit_rest_sum=0;all_sum=0;max_bank=0;min_pairs=None
    histogram=Counter();unit_set=set(unit);domain_set=set(domain)
    for x in range(p*p):
        values=[evaluate(poly,x) for poly in polynomials]
        counts=Counter(values)
        pairs=sum(comb(v,2) for v in counts.values())
        all_sum+=pairs
        if x in unit_set:
            assert len(counts)<=p
            phase=mul(inv_constant,power(x,(-d)%(p+1)))
            assert all(frobenius(v)==mul(phase,v) for v in values)
            if x not in domain_set:
                assert pairs>=minimum_pairs(n,p)
                unit_rest_sum+=pairs
        else:
            collision_sum+=pairs
            max_bank=max(max_bank,len(counts))
            min_pairs=pairs if min_pairs is None else min(min_pairs,pairs)
            histogram[len(counts)]+=1
    assert all_sum<=d*comb(n,2)
    assert unit_rest_sum>=int(cert['remaining_unit_circle_collisions_lower'])
    assert collision_sum<=int(cert['total_allowed_pole_collisions_upper'])
    assert min_pairs<=int(cert['some_pole_pairs_upper'])
    assert max_bank>=int(cert['new_bank'])
    return dict(certificate=cert,supports=n,polynomial_degree=d,
                enumerated_field_points=p*p,enumerated_off_circle_points=p*p-len(unit),
                actual_common_root_pair_sum=exact_intersections,
                actual_remaining_unit_collisions=unit_rest_sum,
                actual_all_field_collisions=all_sum,
                actual_off_circle_collisions=collision_sum,
                actual_minimum_pole_collisions=min_pairs,actual_maximum_bank=max_bank,
                bank_histogram=dict(sorted(histogram.items())))


if __name__=='__main__':
    small=toy()
    p=2**31-1
    large=[]
    for m,h,r,extension in [(128,19,0,2),(64,35,0,2),(256,37,1,2),
                             (256,37,1,4),(1024,545,15,4)]:
        numerator=comb(m-1,h-1);denominator=m*p**(2*r)
        n=(numerator+denominator-1)//denominator
        large.append(certificate(p,m,h,h-2*r-2,n,extension))
    result=dict(status='passed',toy=small,large=large,
                scope='Coding-theory label-bank lower bounds; no protocol transcript claim')
    (ROOT/'circle_collision_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(toy=small,large=large),indent=2),flush=True)
