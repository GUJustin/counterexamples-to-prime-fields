"""Exhaust all core interpolants to verify unique-nearby line padding."""
from pathlib import Path
from itertools import combinations
from math import comb
import json
import time
import sympy as sym
from verify_anchored_padding import locator,subtract,value,compose_power,root_quotient


def interpolate(xs,ys,p):
    coefficients=ys[:]
    for j in range(1,len(xs)):
        for i in range(len(xs)-1,j-1,-1):
            coefficients[i]=(coefficients[i]-coefficients[i-1])*pow(xs[i]-xs[i-j],-1,p)%p
    out=[coefficients[-1]]
    for i in range(len(xs)-2,-1,-1):
        nxt=[0]*(len(out)+1)
        for j,c in enumerate(out):
            nxt[j]=(nxt[j]-xs[i]*c)%p
            nxt[j+1]=(nxt[j+1]+c)%p
        nxt[0]=(nxt[0]+coefficients[i])%p
        out=nxt
    return tuple(out)


def fixture(B,K,q):
    m,k,t=9,3,5
    N=m*B-1;A=t*B;n=N+q;M=comb(N,K)
    assert K-1+q<A and K>=B*(k-1)
    lower=max(N+1+q+(K-1)*comb(M,2),(q-1)*M*M,1000)
    p=int(sym.nextprime(lower))
    while p%B!=1%B or not all(pow(a,(p-1)//B,p)==1 for a in range(1,m+1)):
        p=int(sym.nextprime(p))
    if B==1:
        all_roots=list(range(1,m+1))
    else:
        assert B==2
        all_roots=[int(x) for a in range(1,m+1) for x in sym.sqrt_mod(a,p,all_roots=True)]
    old=sorted(x for x in all_roots if x!=1)
    assert len(old)==N
    locators=[locator(S,p) for S in ((1,2,5,7,8),(1,3,4,6,9))]
    assert locators[0][k:]==locators[1][k:]
    W=[0]*k+locators[0][k:];W1=value(W,1,p)
    numerator=compose_power(W,B);numerator[0]=(numerator[0]-W1)%p
    core_word=root_quotient(numerator,1,p)
    ys=[value(core_word,x,p) for x in old]
    pool=set()
    for indices in combinations(range(N),K):
        pool.add(interpolate([old[i] for i in indices],[ys[i] for i in indices],p))
    pool=sorted(pool)
    assert len(pool)<=M
    counts=[sum(value(P,x,p)==y for x,y in zip(old,ys)) for P in pool]
    assert max(counts)==A-1
    boundary=[i for i,c in enumerate(counts) if c==A-1]
    assert len(boundary)>=2
    reserved=set(old)|{1};points=[];evaluations=[]
    for x in range(p):
        if x in reserved:
            continue
        values=[value(P,x,p) for P in pool]
        if len(set(values))==len(pool):
            points.append(x);evaluations.append(values)
            if len(points)==q:
                break
    assert len(points)==q
    used=set();offsets=[];nearby={}
    for j,values in enumerate(evaluations):
        b=0
        while used.intersection((v-b)%p for v in values):
            b+=1
        labels=[(v-b)%p for v in values]
        assert len(set(labels))==len(pool) and not used.intersection(labels)
        used.update(labels);offsets.append(b)
        for i in boundary:
            assert labels[i] not in nearby
            nearby[labels[i]]=i
    assert len(used)==q*len(pool) and len(nearby)==q*len(boundary)
    domain=old+points;f=ys+offsets;g=[0]*N+[1]*q
    for z,i in nearby.items():
        assert sum(value(pool[i],x,p)==(y+z*h)%p for x,y,h in zip(domain,f,g))==A
    # Every possible nearby codeword is in the exhaustive pool because
    # A-q>=K; the global injective label map allows it only one pad hit.
    assert A-q>=K and max(A-1,K-1+q)<A
    alternative_words=[]
    for r in range(min(q,len(boundary))+1):
        pad_values=[]
        for j,values in enumerate(evaluations):
            if j<r:
                pad_values.append(values[boundary[j]])
            else:
                excluded=set(values);v=0
                while v in excluded:
                    v+=1
                pad_values.append(v)
        nearby_indices=[i for i in range(len(pool)) if counts[i]+sum(
            evaluations[j][i]==pad_values[j] for j in range(q))>=A]
        assert nearby_indices==boundary[:r]
        if r>=2:
            assert len({(v-b)%p for v,b in zip(pad_values,offsets)})>1
        alternative_words.append(dict(exact_list_size=r,padding_values=pad_values,
                                      nearby_boundary_indices=nearby_indices))
    return dict(B=B,p=p,n=n,K=K,A=A,padding=q,
                determining_subsets=M,distinct_core_interpolants=len(pool),
                entire_boundary_list_size=len(boundary),
                entire_nearby_label_count=len(nearby),maximum_list_size_on_line=1,
                global_joint_agreement_upper=max(A-1,K-1+q),
                domain=domain,f=f,g=g,nearby_labels=sorted(nearby),
                alternative_words=alternative_words,
                boundary_polynomials=[pool[i] for i in boundary])


def main():
    start=time.monotonic()
    result=dict(status='PASS',fixtures=[fixture(1,2,3),fixture(2,5,4)],
                scope='Exhaustive enumeration of every old K-subset interpolant and injectivity of every pool/padding label. These exhaust all potentially nearby candidates, not just the selected seed list.')
    result['seconds']=time.monotonic()-start
    Path(__file__).with_name('unique_padding_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({**result,'fixtures':[{k:v for k,v in row.items() if k not in
        {'domain','f','g','nearby_labels','boundary_polynomials'}} for row in result['fixtures']]},indent=2))


if __name__=='__main__':
    main()
