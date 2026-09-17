"""Exact finite-length ratio transfer and a near-critical positive fixture."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
from verify_finite_length import formula
from verify_smaller_certificates import diagonal_rank


def main():
    reductions=positive=0
    for H in product(range(5),repeat=3):
        for N in (12,16,20):
            D=N//4-1
            for A in (N//4+1,N//2,3*N//4):
                for m in range(1,7):
                    S,G,R,pieces=formula(H,m,D,A)
                    low={(u,b) for u,b in S if m*A-(D-1)*(u+b)>=m}
                    g0=sum(m*A-D*(u+b)+b for u,b in low)
                    r0=sum(r for q,L,g,r in pieces if L>=m)
                    assert r0<=R and F(g0,N)-r0>=F(G,N)-R
                    astar=F(A*N-8,N*(N-8))
                    B=sum(m*astar-F(u+b,4) for u,b in low)
                    assert B>=F(g0,N)
                    if G>N*R:
                        assert low and B>r0
                        assert F(R,F(G,N)-R)>=F(r0,F(g0,N)-r0)>=F(r0,B-r0)
                        assert max(u for u,b in low)<=max(u for u,b in S)
                        assert max(b for u,b in low)<=max(b for u,b in S)
                        positive+=1
                    reductions+=1
    N=1000000;A=469000;D=N//4-1;m=2048;C=932;qmax=3842
    G=R=count=0
    for q in range(qmax+1):
        length=min(q+1,C)
        assert m*A-(D-1)*q>=m
        G+=length*(m*A-D*q)+length*(length-1)//2
        R+=diagonal_rank(q,length,m);count+=length
    delta=F(G,N)-R;assert delta>0
    lo=F(4687923417635740609,10**19);hi=lo+F(1,10**19)
    astar=F(A*N-8,N*(N-8));epslo=astar-hi;epshi=astar-lo
    assert 0<epslo<epshi<F(1,2000)
    assert 8*epslo*R>=delta
    assert m*epslo>(1-2*lo)/8
    ell=(F(qmax*R,delta)).__floor__()
    assert (ell+1)*G>N*(ell+qmax+1)*R
    assert ell>m/(32*epslo)-1
    out=dict(status='passed',reduction_checks=reductions,positive_surplus_ratio_checks=positive,fixture=dict(N=N,A=A,m=m,monomials=count,G=G,R=R,normalized_surplus=str(delta),effective_agreement=str(astar),challenge_budget=ell),scope='Exact finite-length proof-ledger cost transfer; no intrinsic list lower bound.')
    Path(__file__).with_name('finite_gap_costs_verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
