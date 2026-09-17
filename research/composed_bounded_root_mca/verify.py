"""Exact composition, repeated-fiber, and full-support incidence fixtures."""
import importlib.util
import itertools
import json
from math import factorial,prod
from pathlib import Path
BASE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('poly_helpers',BASE.parent/'quasilinear_first_order/verify.py')
h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)

def small_spaces():
    rows=[]
    for p,n,B,K in [(7,6,2,1),(11,8,2,2),(13,10,3,2)]:
        D=B*K;A=D+2;ell=K+1
        assert A<=n<p
        xs=list(range(n));ys=[pow(x,B,p) for x in xs]
        assert max(ys.count(y) for y in set(ys))<=B
        f=[(1+y)%p for y in ys];g=[y*y%p if K==2 else y for y in ys]
        for j,i in enumerate(range(A-1,n)):
            f[i]=(f[i]-j)%p;g[i]=(g[i]+1)%p
        assert any((f[i],g[i])!=(f[j],g[j]) for i in range(n) for j in range(i)
                   if ys[i]==ys[j])
        chosen={};nearby=0
        for coeffs in itertools.product(range(p),repeat=ell):
            vals=[h.evaluate(coeffs,y,p) for y in ys]
            for z in range(p):
                support=[i for i in range(n) if vals[i]==(f[i]+z*g[i])%p]
                if len(support)<A:continue
                nearby+=1
                if h.bad_support(xs,g,support,D,p):chosen.setdefault(z,(coeffs,support))
        assert chosen
        tuple_labels={};incidences=0
        for z,(coeffs,support) in chosen.items():
            independent=[J for J in itertools.combinations(support,ell)
                         if len({ys[i] for i in J})==ell]
            assert len(independent)*factorial(ell)>=(A-D)**ell
            incidences+=len(independent)*factorial(ell)
            for J in independent:tuple_labels.setdefault(J,set()).add(z)
        assert all(len(zs)<=n for zs in tuple_labels.values())
        assert len(chosen)*(A-D)**ell<=incidences<=n*prod(range(n-ell+1,n+1))
        rows.append(dict(p=p,n=n,B=B,K=K,D=D,A=A,
                         all_polynomial_label_pairs=p**(ell+1),nearby_pairs=nearby,
                         bad_labels=len(chosen),ordered_determining_incidences=incidences,
                         received_words_not_fiber_invariant=True))
    return rows

def growing_composition():
    rows=[]
    p=65537
    for B in (1,2,4,8,16):
        n,D,A=16*B,5*B,10*B
        xs=list(range(1,n+1));ys=[pow(x,B,p) for x in xs]
        H=[pow(y,4,p) for y in ys]
        F=[2*v%p for v in H];G=[v*y%p for v,y in zip(H,ys)]
        f=F[:];g=G[:]
        for j,i in enumerate(range(A-1,n)):
            f[i]=H[i]*(2-j)%p;g[i]=H[i]*(ys[i]+1)%p
        assert all(H)
        for z in range(n-A+1):
            candidate=[H[i]*(2+z*ys[i])%p for i in range(n)]
            support=[i for i in range(n) if (f[i]+z*g[i])%p==candidate[i]]
            assert support==list(range(A-1))+[A-1+z]
            assert len(support)==A and A-1>D
            assert all(g[i]==G[i] for i in range(A-1))
            assert g[A-1+z]!=G[A-1+z]
        rows.append(dict(p=p,n=n,D=D,A=A,composition_degree=B,
                         quotient_polynomial='Y^4(2+zY)',quotient_root_bound=2,
                         generic_composed_distinct_roots=B+1,exact_bad_labels=n-A+1,
                         justification='The difference on each noncore coordinate is nonzero H_i times z-j. The >D-point core forces direction G; the extra agreement contradicts it.'))
    return rows

def main():
    data=dict(status='PASS',small_spaces=small_spaces(),growing_composition=growing_composition(),
              scope='Exhaustive small coefficient/label spaces with non-fiber-invariant words, determining-tuple counts in the original degree-D code, and five exact linear-size bad-label constructions with growing composition degree. These checks supplement the universal proof; they do not instantiate its very large Wronskian thresholds.')
    (BASE/'verification.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2))

if __name__=='__main__':main()
