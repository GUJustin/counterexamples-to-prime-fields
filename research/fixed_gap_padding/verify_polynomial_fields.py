"""Exact finite checks of shifted fibers and the selected padding witnesses."""
from pathlib import Path
from math import comb, isqrt
from itertools import combinations
import json,time
from verify_anchored_padding import (prime,locator,subtract,value,compose_power,
                                    root_quotient,degree_at_most_on_support)


def shifts(p,B,nodes):
    powers={pow(x,B,p) for x in range(1,p)}
    assert len(powers)==(p-1)//B
    good=[c for c in range(p) if all((c+a)%p in powers for a in nodes)]
    # Conservative exact version of the character-sum lower bound.
    lower=p//(B**len(nodes))-len(nodes)*(isqrt(p)+1)-len(nodes)
    assert len(good)>=lower
    return good,lower


def fixture(p,B):
    assert prime(p) and (p-1)%B==0
    m,k,t=9,3,5
    supports=[(1,2,5,7,8),(1,3,4,6,9)]
    good,lower=shifts(p,B,range(1,m+1))
    assert good
    c=good[0]
    roots={a:[x for x in range(p) if pow(x,B,p)==(a+c)%p]
           for a in range(1,m+1)}
    assert all(len(xs)==B for xs in roots.values())
    alpha=roots[1][0]
    Fs=[locator([(a+c)%p for a in S],p) for S in supports]
    assert Fs[0][k:]==Fs[1][k:]
    W=[0]*k+Fs[0][k:]
    Gs=[subtract(W,F,p) for F in Fs]
    anchor=value(W,(1+c)%p,p)
    # W here is the high-degree part after translation, differing from
    # W(Y-c) only by degree<k. This changes all candidates by the same
    # low-degree polynomial and preserves every construction invariant.
    assert all(value(G,(1+c)%p,p)==anchor for G in Gs)
    def quotient(P):
        num=compose_power(P,B);num[0]=(num[0]-anchor)%p
        return root_quotient(num,alpha,p)
    oldword=quotient(W);Ps=[quotient(G) for G in Gs]
    n,K,A,q=10*B,3*B,5*B,B+1
    assert len(oldword)-1==A-1 and all(len(P)-1<K for P in Ps)
    full=sorted(x for xs in roots.values() for x in xs)
    old=[x for x in full if x!=alpha]
    assert len(old)==m*B-1 and len(set(full))==m*B
    assert all(sum(value(P,x,p)==value(oldword,x,p) for x in old)==A-1 for P in Ps)
    assert p>m*B+(K-1)*comb(len(Ps),2)+(A-1)*len(Ps)+q
    assert p-1>(q-1)*len(Ps)**2
    points=[]
    for x in range(p):
        if (x not in full and len({value(P,x,p) for P in Ps})==len(Ps)
                and all(value(P,x,p)!=value(oldword,x,p) for P in Ps)):
            points.append(x)
            if len(points)==q:break
    assert len(points)==q
    labels=set();directions=[];witnesses=[]
    for x in points:
        vals=[(value(P,x,p)-value(oldword,x,p))%p for P in Ps]
        h=next(h for h in range(1,p) if not labels.intersection(
            v*pow(h,-1,p)%p for v in vals))
        directions.append(h)
        for i,v in enumerate(vals):
            z=v*pow(h,-1,p)%p;assert z and z not in labels
            labels.add(z);witnesses.append((z,i))
    domain=old+points;f=[value(oldword,x,p) for x in domain]
    g=[0]*len(old)+directions
    assert len(domain)==n and max(A-1,K-1+q)<A
    # Degree bounds the agreement of f with every codeword by A-1;
    # the selected candidates attain that bound on the core.
    assert all(sum(value(P,x,p)==y for x,y in zip(domain,f))==A-1 for P in Ps)
    for z,i in witnesses:
        S=[j for j,x in enumerate(domain) if value(Ps[i],x,p)==(f[j]+z*g[j])%p]
        assert len(S)==A
        assert not degree_at_most_on_support([domain[j] for j in S],[g[j] for j in S],K-1,p)
    # Unanchored list: keep all full fibers and q-1 padding points.
    list_domain=full+points[:-1]
    assert len(list_domain)==n
    assert all(sum(value(compose_power(G,B),x,p)==value(compose_power(W,B),x,p)
                   for x in list_domain)==A for G in Gs)
    return dict(p=p,B=B,shift=c,anchor=alpha,number_of_shifts=len(good),
                n=n,K=K,A=A,labels=sorted(labels),domain=domain,f=f,g=g,
                candidates=Ps,exact_far_agreement=A-1,
                common_agreement_upper=A-1)


def main():
    start=time.monotonic()
    counts=[]
    for p,B,nodes in [(257,2,[1,3]),(65537,4,[1,2,3]),(1009,3,[0,2])]:
        assert prime(p) and (p-1)%B==0
        good,lower=shifts(p,B,nodes)
        assert lower>0 and good
        counts.append(dict(p=p,B=B,nodes=nodes,count=len(good),integer_lower=lower))
    fixtures=[fixture(1009,2),fixture(65539,3)]
    result=dict(status='passed',shift_counts=counts,fixtures=fixtures,
                seconds=time.monotonic()-start,
                scope='Finite character-count and shifted-anchor mechanism checks; asymptotic polynomial field size uses Weil and Linnik, not finite testing. No whole-line uniqueness assertion.')
    Path(__file__).with_name('polynomial_fields_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status=result['status'],shift_counts=counts,
                         fixtures=[{k:r[k] for k in ('p','B','shift','anchor','n','K','A','common_agreement_upper')} for r in fixtures],seconds=result['seconds']),indent=2))

if __name__=='__main__':main()
