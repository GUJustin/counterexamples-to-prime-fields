"""Exact parameter certificates and exhaustive witnesses for variable-q padding."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json


def ev(c, x, p):
    z=0
    for a in reversed(c):
        z=(z*x+a)%p
    return z


def main():
    p,N,k,A=23,10,3,4
    w=(21,1,16,3,16,6,12,11,16,9)
    source=list(product(range(p),repeat=k))
    bank=[c for c in source if sum(ev(c,x,p)==w[x] for x in range(N))>=A]
    assert len(bank)==11
    anchor=max(range(N),key=lambda x:sum(ev(c,x,p)==w[x] for c in bank))
    selected=[c for c in bank if ev(c,anchor,p)==w[anchor]]
    # Degree-two synthetic division, checked by identities at every field point.
    quotients=[((c[1]+anchor*c[2])%p,c[2]) for c in selected]
    for c,b in zip(selected,quotients):
        assert all(((x-anchor)*ev(b,x,p)+w[anchor]-ev(c,x,p))%p==0 for x in range(p))
    assert len(set(quotients))==len(quotients)
    core=[x for x in range(N) if x!=anchor]
    images={x:{ev(c,x,p) for c in quotients} for x in range(N,p)}
    ordered=sorted(images,key=lambda x:len(images[x]),reverse=True)
    cases=[]
    for q in (1,2,4,11):
        added=ordered[:q]
        covered=set(); offsets=[]; missing=Q(1)
        for x in added:
            b=max(range(p),key=lambda b:len({(v-b)%p for v in images[x]}-covered))
            offsets.append(b)
            covered|={(v-b)%p for v in images[x]}
            missing*=Q(p-len(images[x]),p)
        expectation=p*(1-missing)
        lower=Q(p*q*A*len(bank),N*p+(2*(k-2)+q)*A*len(bank))
        assert len(covered)>=expectation>=lower
        domain=core+added
        f=[(w[x]-w[anchor])*pow(x-anchor,-1,p)%p for x in core]+offsets
        g=[0]*len(core)+[1]*q
        directions=[tuple(ev(c,x,p) for x in domain) for c in source]
        bad=set(); checks=0
        for c in quotients:
            for z in {(ev(c,x,p)-b)%p for x,b in zip(added,offsets)}:
                support=[i for i,x in enumerate(domain) if ev(c,x,p)==(f[i]+z*g[i])%p]
                assert len(support)>=A
                assert not any(all(v[i]==g[i] for i in support) for v in directions)
                bad.add(z); checks+=1
        assert bad==covered
        cases.append(dict(q=q,n=len(domain),bad_labels=len(bad),expectation=str(expectation),lower=str(lower),witness_supports=checks,directions_per_support=len(directions)))
    params=[]
    for rho,a in [(Q(1,4),Q(49,100)),(Q(25,101),Q(49,101))]:
        curve=(8-rho)*a*a-6*rho*a+rho*(4*rho-5)
        johnson=rho-a*a
        branch=(11-rho)**2-117
        assert curve>0 and johnson>0 and branch<0
        params.append(dict(rate=str(rho),agreement=str(a),curve_polynomial=str(curve),johnson_slack=str(johnson),branch_polynomial=str(branch)))
    out=dict(status='passed',source=dict(p=p,N=N,k=k,A=A,L=len(bank)),cases=cases,parameters=params,scope='Variable-q compiler fixtures and exact first-order parameter certificates only; no growing source-list construction.')
    Path(__file__).with_name('sparse_padding_verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__': main()
