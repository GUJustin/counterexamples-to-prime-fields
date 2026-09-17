"""Independent exhaustive small-field checks for the general boundary compiler."""
from fractions import Fraction
from itertools import product
from pathlib import Path
import json
import random


def ev(c, x, p):
    out = 0
    for a in reversed(c):
        out = (out*x+a) % p
    return out


def fixture(p, N, k, seed):
    rng = random.Random(seed)
    old = tuple(range(N))
    polys = list(product(range(p), repeat=k))
    values = [tuple(ev(c, x, p) for x in old) for c in polys]
    for attempt in range(1000):
        w = tuple(rng.randrange(p) for _ in old)
        agreements = [sum(a == b for a, b in zip(v, w)) for v in values]
        M = max(agreements)
        bank = [c for c, a in zip(polys, agreements) if a == M]
        if M > k and len(bank) >= 3 and M < N-1:
            break
    else:
        raise AssertionError('No suitable fixture')
    anchor = max(old, key=lambda x: sum(ev(c,x,p)==w[x] for c in bank))
    selected = [c for c in bank if ev(c,anchor,p)==w[anchor]]
    core = tuple(x for x in old if x != anchor)
    fcore = tuple((w[x]-w[anchor])*pow(x-anchor,-1,p)%p for x in core)
    small = list(product(range(p), repeat=k-1))
    candidates=[]
    for c in selected:
        # Independently identify each quotient by evaluating the polynomial identity.
        matches=[b for b in small if all(((x-anchor)*ev(b,x,p)+w[anchor]-ev(c,x,p))%p==0 for x in range(p))]
        assert len(matches)==1
        candidates.extend(matches)
    ell=len(candidates)
    assert ell*N >= M*len(bank)
    assert max(sum(ev(c,x,p)==v for x,v in zip(core,fcore)) for c in small)==M-1
    unused=tuple(range(N,p))
    images={x:{ev(c,x,p) for c in candidates} for x in unused}
    R=p-N
    mu=Fraction(ell*R,R+(ell-1)*(k-2))
    assert Fraction(sum(map(len,images.values())),R)>=mu
    q=min(2,p-N,M-k+1)
    added=sorted(unused,key=lambda x:len(images[x]),reverse=True)[:q]
    expected=p*(1-product_fraction(Fraction(p-len(images[x]),p) for x in added))
    lower=p*(1-(1-mu/p)**q)
    assert expected>=lower
    total=0
    best=(-1,None,None)
    for offsets in product(range(p),repeat=q):
        labels=set().union(*({(v-b)%p for v in images[x]} for x,b in zip(added,offsets)))
        total+=len(labels)
        if len(labels)>best[0]:
            best=(len(labels),offsets,labels)
    assert Fraction(total,p**q)==expected
    domain=core+tuple(added)
    f=fcore+best[1]
    g=(0,)*len(core)+(1,)*q
    code=[tuple(ev(c,x,p) for x in domain) for c in small]
    actual_near={z for z in range(p) if max(sum(v==(a+z*b)%p for v,a,b in zip(c,f,g)) for c in code)>=M}
    assert best[2]<=actual_near
    joint=max(sum(a==u and b==v for a,b,u,v in zip(F,G,f,g)) for F in code for G in code)
    assert joint<M
    # Check the source is not covered by a received-polynomial degree <= M shortcut.
    # Divided differences find its exact interpolation degree.
    dd=list(w)
    coefficients=[dd[0]]
    for order in range(1,N):
        dd=[(dd[j+1]-dd[j])*pow(old[j+order]-old[j],-1,p)%p for j in range(N-order)]
        coefficients.append(dd[0])
    degree=max(j for j,c in enumerate(coefficients) if c)
    assert degree>M
    return dict(p=p,N=N,k=k,M=M,L=len(bank),anchor=anchor,ell=ell,q=q,
                source_interpolation_degree=degree,source_word=w,
                image_mean_lower=str(mu),expected_union=str(expected),
                union_bound=str(lower),best_selected_labels=best[0],
                actual_nearby_labels=len(actual_near),max_joint_agreement=joint,
                exhaustive_offset_tuples=p**q,exhaustive_witness_pairs=len(code)**2)


def product_fraction(xs):
    out=Fraction(1)
    for x in xs: out*=x
    return out


def arbitrary_list_fixture(source):
    p,N,k=source['p'],source['N'],source['k']
    w=source['source_word']
    A=source['M']-1
    assert A>=k
    bank=[c for c in product(range(p),repeat=k)
          if sum(ev(c,x,p)==w[x] for x in range(N))>=A]
    anchor=max(range(N),key=lambda x:sum(ev(c,x,p)==w[x] for c in bank))
    selected=[c for c in bank if ev(c,anchor,p)==w[anchor]]
    small=list(product(range(p),repeat=k-1))
    candidates=[]
    for c in selected:
        matches=[b for b in small if all(((x-anchor)*ev(b,x,p)+w[anchor]-ev(c,x,p))%p==0 for x in range(p))]
        assert len(matches)==1
        candidates.extend(matches)
    ell=len(candidates)
    assert ell*N>=A*len(bank)
    core=tuple(x for x in range(N) if x!=anchor)
    fcore=tuple((w[x]-w[anchor])*pow(x-anchor,-1,p)%p for x in core)
    images={x:{ev(c,x,p) for c in candidates} for x in range(N,p)}
    mu=Fraction(ell*(p-N),p-N+(ell-1)*(k-2))
    q=2
    added=sorted(images,key=lambda x:len(images[x]),reverse=True)[:q]
    expected=p*(1-product_fraction(Fraction(p-len(images[x]),p) for x in added))
    lower=p*(1-(1-mu/p)**q)
    assert expected>=lower
    total=0
    best=(-1,None,None)
    for offsets in product(range(p),repeat=q):
        labels=set().union(*({(v-b)%p for v in images[x]} for x,b in zip(added,offsets)))
        total+=len(labels)
        if len(labels)>best[0]: best=(len(labels),offsets,labels)
    assert Fraction(total,p**q)==expected
    domain=core+tuple(added)
    f=fcore+best[1]
    g=(0,)*len(core)+(1,)*q
    code=[tuple(ev(c,x,p) for x in domain) for c in small]
    bad=set()
    witnesses=0
    for c in candidates:
        for z in {(ev(c,x,p)-b)%p for x,b in zip(added,best[1])}:
            support=[i for i,x in enumerate(domain) if ev(c,x,p)==(f[i]+z*g[i])%p]
            assert len(support)>=A
            assert not any(all(G[i]==g[i] for i in support) for G in code)
            bad.add(z)
            witnesses+=1
    assert bad==best[2]
    ordinary_joint=max(sum(a==u and b==v for a,b,u,v in zip(F,G,f,g)) for F in code for G in code)
    return dict(p=p,N=N,k=k,A=A,source_maximum=source['M'],L=len(bank),ell=ell,
                expected_union=str(expected),union_lower=str(lower),bad_labels=len(bad),
                checked_bad_witnesses=witnesses,max_ordinary_joint_agreement=ordinary_joint,
                ordinary_CA_present=ordinary_joint>=A)


def exact_halving_fixture():
    p=101
    old=tuple(x%p for x in (-2,-1,0,1,2))
    N,k,A=5,2,3
    w={x:pow(x,3,p) for x in old}
    source=list(product(range(p),repeat=k))
    bank=[c for c in source if sum(ev(c,x,p)==w[x] for x in old)>=A]
    assert len(bank)==2
    assert p>=4*N*len(bank)
    anchor=0
    assert all(ev(c,anchor,p)==0 for c in bank)
    candidates=[(c[1],0) for c in bank]
    core=tuple(x for x in old if x!=anchor)
    added=tuple(range(3,9))
    offsets=tuple(10*i for i in range(N+1))
    domain=core+added
    f=tuple(pow(x,2,p) for x in core)+offsets
    g=(0,)*len(core)+(1,)*len(added)
    assert len(domain)==2*N and len(set(domain))==2*N
    labels=set()
    for c in candidates:
        for z in {(ev(c,x,p)-v)%p for x,v in zip(added,offsets)}:
            support=[i for i,x in enumerate(domain) if ev(c,x,p)==(f[i]+z*g[i])%p]
            assert len(support)>=A
            assert not any(all(ev(G,domain[i],p)==g[i] for i in support) for G in source)
            labels.add(z)
    assert len(labels)==12
    lower=Fraction(p*A*len(bank),p+3*A*len(bank))
    assert len(labels)>=lower
    return dict(p=p,source_length=N,target_length=2*N,dimension=k,threshold=A,
                list_size=len(bank),source_rate=str(Fraction(k,N)),
                target_rate=str(Fraction(k,2*N)),source_gap=str(Fraction(A-k,N)),
                target_gap=str(Fraction(A-k,2*N)),bad_labels=len(labels),
                theorem_lower=str(lower),directions_checked_per_support=len(source))


def saturated_halving_fixture():
    p,N,k,A=23,10,3,4
    rng=random.Random(19)
    old=tuple(range(N))
    source=list(product(range(p),repeat=k))
    source_values=[tuple(ev(c,x,p) for x in old) for c in source]
    for attempt in range(100):
        w=tuple(rng.randrange(p) for _ in old)
        bank=[c for c,v in zip(source,source_values) if sum(a==b for a,b in zip(v,w))>=A]
        if len(bank)>=6: break
    else: raise AssertionError('No saturated fixture')
    anchor=max(old,key=lambda x:sum(ev(c,x,p)==w[x] for c in bank))
    selected=[c for c in bank if ev(c,anchor,p)==w[anchor]]
    quotient_pool=list(product(range(p),repeat=k-1))
    candidates=[]
    for c in selected:
        matches=[b for b in quotient_pool if all(((x-anchor)*ev(b,x,p)+w[anchor]-ev(c,x,p))%p==0 for x in range(p))]
        assert len(matches)==1
        candidates.extend(matches)
    ell=len(candidates)
    assert N*ell>=A*len(bank)
    core=tuple(x for x in old if x!=anchor)
    images={x:{ev(c,x,p) for c in candidates} for x in range(N,p)}
    added=sorted(images,key=lambda x:len(images[x]),reverse=True)[:N+1]
    covered=set()
    offsets=[]
    for x in added:
        b=max(range(p),key=lambda b:len({(v-b)%p for v in images[x]}-covered))
        offsets.append(b)
        covered|={(v-b)%p for v in images[x]}
    expected=p*(1-product_fraction(Fraction(p-len(images[x]),p) for x in added))
    lower=Fraction(p*A*len(bank),p+3*A*len(bank))
    assert len(covered)>=expected>=lower
    domain=core+tuple(added)
    f=tuple((w[x]-w[anchor])*pow(x-anchor,-1,p)%p for x in core)+tuple(offsets)
    g=(0,)*len(core)+(1,)*len(added)
    assert len(domain)==2*N
    code=[tuple(ev(c,x,p) for x in domain) for c in source]
    bad=set()
    for c in candidates:
        for z in {(ev(c,x,p)-b)%p for x,b in zip(added,offsets)}:
            support=[i for i,x in enumerate(domain) if ev(c,x,p)==(f[i]+z*g[i])%p]
            assert len(support)>=A
            assert not any(all(G[i]==g[i] for i in support) for G in code)
            bad.add(z)
    assert bad==covered
    return dict(p=p,source_length=N,target_length=2*N,k=k,A=A,L=len(bank),ell=ell,
                source_word=w,theorem_lower=str(lower),union_expectation=str(expected),
                bad_labels=len(bad),directions_checked_per_support=len(code),
                field_smaller_than_NL=p<N*len(bank))


if __name__=='__main__':
    fixtures=[fixture(11,7,2,3),fixture(11,7,3,7),fixture(13,8,3,13)]
    generic=[arbitrary_list_fixture(f) for f in fixtures]
    result=dict(status='passed',fixtures=fixtures,arbitrary_list_fixtures=generic,exact_halving=exact_halving_fixture(),saturated_halving=saturated_halving_fixture(),scope='Exhaustive source lists, all padding translations for small fixtures, independent quotient identities, joint witness pairs and full-support direction checks. Exact rate/gap halving checked over F101 and F23, including saturation. Asymptotics rely on the written proof.')
    Path(__file__).with_name('prime_boundary_amplification_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
