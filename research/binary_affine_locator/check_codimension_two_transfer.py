#!/usr/bin/env python3
"""Check prefix classes, dual incidence, Sidon bounds, and binary controls."""
import itertools
import json
import math
import random
from collections import defaultdict
from pathlib import Path


def subspaces(m):
    n=1<<m
    result=[]
    for a in range(1,n):
        for b in range(a+1,n):
            c=a^b
            if c<=b:continue
            support=tuple(x for x in range(1,n)
                          if (a&x).bit_count()%2==0 and (b&x).bit_count()%2==0)
            assert len(support)==n//4-1
            result.append(((a,b,c),support))
    assert len(result)==(n-1)*(n-2)//6
    return result


def prefix(support,labels,s,p):
    co=[1]+[0]*s
    for index in support:
        x=labels[index]
        for j in range(s,0,-1):co[j]=(co[j]-x*co[j-1])%p
    return tuple(co[1:])


def odd_fixture(m,p,count,seed):
    n=1<<m;s=n//8-1;spaces=subspaces(m)
    assert p>=n
    rng=random.Random(seed);maximum=0;classes=0;pair_tests=0
    bound_m=(1+math.isqrt(4*n-7))//2;bound=(n-1)*bound_m//3
    for run in range(count):
        labels=list(range(n)) if run==0 else [0]+rng.sample(range(p),n-1)
        assert len(set(labels[1:]))==n-1
        groups=defaultdict(list)
        for dual,support in spaces:groups[prefix(support,labels,s,p)].append(dual)
        maximum=max(maximum,max(map(len,groups.values())))
        for group in groups.values():
            classes+=1;assert len(group)<=bound
            stars=defaultdict(set)
            for dual in group:
                for a in dual:
                    b=next(b for b in dual if b!=a)
                    stars[a].add(min(b,b^a))
            assert sum(map(len,stars.values()))==3*len(group)
            for a,points in stars.items():
                assert len(points)<=bound_m
                sums=[u^v for u,v in itertools.combinations(points,2)]
                pair_tests+=len(sums)
                assert 0 not in sums and len(set(sums))==len(sums)
    return dict(m=m,N=n,p=p,relabelings=count,prefix=s,
                tested_classes=classes,checked_star_pairs=pair_tests,
                largest_observed_class=maximum,theorem_bound=bound)


def multiply(a,b,modulus,m):
    c=0
    while b:
        if b&1:c^=a
        b>>=1;a<<=1
        if a&(1<<m):a^=modulus
    return c


def binary_control(m,modulus):
    n=1<<m;s=n//8-1;spaces=subspaces(m)
    # Check every nonzero multiplier is bijective: the chosen quotient is a field.
    for a in range(1,n):
        assert len({multiply(a,b,modulus,m) for b in range(n)})==n
    for dual,support in spaces:
        co=[1]+[0]*s
        for x in support:
            for j in range(s,0,-1):co[j]^=multiply(x,co[j-1],modulus,m)
        assert not any(co[1:])
    bound=(n-1)*((1+math.isqrt(4*n-7))//2)//3
    assert len(spaces)>bound
    return dict(m=m,N=n,binary_field_modulus=modulus,prefix=s,
                common_prefix_class=len(spaces),odd_characteristic_bound=bound)


def small_characteristic_fixture():
    # F_3[X]/(X^4+X+2); integers encode four base-three coefficients.
    q=81;digits=[[(a//(3**j))%3 for j in range(4)] for a in range(q)]
    add=[[sum(((digits[a][j]+digits[b][j])%3)*3**j for j in range(4))
          for b in range(q)] for a in range(q)]
    neg=[sum((-digits[a][j]%3)*3**j for j in range(4)) for a in range(q)]
    mul=[]
    for a in range(q):
        row=[]
        for b in range(q):
            c=[0]*7
            for i in range(4):
                for j in range(4):c[i+j]=(c[i+j]+digits[a][i]*digits[b][j])%3
            for i in range(6,3,-1):
                c[i-4]=(c[i-4]-2*c[i])%3;c[i-3]=(c[i-3]-c[i])%3
            row.append(sum(c[j]*3**j for j in range(4)))
        mul.append(row)
    for a in range(1,q):assert len(set(mul[a]))==q
    spaces=subspaces(5);rng=random.Random(3081);maximum=0;classes=0
    for run in range(20):
        labels=[0]+rng.sample(range(q),31);groups=defaultdict(list)
        for dual,support in spaces:
            co=[1,0,0,0]
            for x in support:
                for j in range(3,0,-1):co[j]=add[co[j]][neg[mul[labels[x]][co[j-1]]]]
            groups[tuple(co[1:])].append(dual)
        maximum=max(maximum,max(map(len,groups.values())))
        for group in groups.values():
            classes+=1;assert len(group)<=62
            stars=defaultdict(set)
            for dual in group:
                for a in dual:
                    b=next(b for b in dual if b!=a);stars[a].add(min(b,b^a))
            assert sum(map(len,stars.values()))==3*len(group)
            for values in stars.values():
                sums=[u^v for u,v in itertools.combinations(values,2)]
                assert len(values)<=6 and len(sums)==len(set(sums))
    return dict(N=32,field_size=q,characteristic=3,prefix=3,relabelings=20,
                tested_classes=classes,largest_observed_class=maximum,theorem_bound=62)


def binary_affine_plane_check():
    count=0
    for m in range(3,7):
        n=1<<m
        # A fixed nonzero a, representatives b with lowest bit zero.
        a=1;quotient=list(range(0,n,2))
        for origin in quotient[1:]:
            for u in quotient[1:]:
                for v in quotient[1:]:
                    if u>=v:continue
                    bs={origin,origin^u,origin^v,origin^u^v}
                    if len(bs)!=4 or 0 in bs:continue
                    masks=[]
                    for b in bs:
                        mask=sum(1<<(x-1) for x in range(1,n)
                                 if not (a&x).bit_count()%2 and not (b&x).bit_count()%2)
                        assert mask.bit_count()==n//4-1
                        masks.append(mask)
                    assert len(set(masks))==4 and masks[0]^masks[1]^masks[2]^masks[3]==0
                    count+=1
    return count


def main():
    result={'status':'PASS',
            'odd_characteristic_fixtures':[odd_fixture(4,p,100,1700+p) for p in (17,19,101)]
            +[odd_fixture(5,p,30,1800+p) for p in (37,101)]
            +[odd_fixture(6,257,10,1964)],
            'binary_negative_controls':[binary_control(4,0b10011),binary_control(5,0b100101)],
            'small_characteristic_fixture':small_characteristic_fixture(),
            'affine_planes_checked':binary_affine_plane_check(),
            'scope':'Finite prefix classes and independent binary controls supplement the counting proof; they do not establish its asymptotic conclusion.'}
    Path(__file__).with_name('codimension_two_transfer_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
