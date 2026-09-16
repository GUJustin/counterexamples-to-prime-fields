#!/usr/bin/env python3
"""Exact higher-order Taylor recurrence and finite substitution checks."""
import json
import math
import random
from pathlib import Path
import sympy as s
from arithmetic import add,mul,scale,deriv

X,z=s.symbols('X z')
u=s.symbols('u0:6')


def power(P,j,p):
    out=[1]
    for _ in range(j):out=mul(out,P,p)
    return out


def run():
    rng=random.Random(2026091618)
    specs=[(2,u[2]**2+z*u[0]*u[2]+u[1]**2+X*u[1]+z*X,2,1,5),
           (3,(1+z*X)*u[3]+u[0]*u[2]+u[1]**2-z*z*X,2,2,6),
           (4,u[4]+u[0]**2+z*u[1]*u[3]+X*u[2],2,1,7),
           (5,u[5]**3+z*u[0]*u[5]+u[2]**2+X*u[1],3,1,7)]
    records=[];tests=0
    for d,Q,B,H,Dmax in specs:
        gens=(X,z,*u[:d+1]);S=s.diff(Q,u[d]);A=s.diff(Q,X)+sum(u[i+1]*s.diff(Q,u[i]) for i in range(d))
        def along(N):return s.diff(N,X)+sum(u[i+1]*s.diff(N,u[i]) for i in range(d))
        def terms(N):return s.Poly(N,*gens).terms()
        def degrees(N):
            ts=terms(N)
            return (max((sum(m[2:]) for m,c in ts if c),default=0),max((m[1] for m,c in ts if c),default=0))
        def ev(ts,vals,p):
            ans=0
            for powers,c in ts:
                term=int(c)%p
                for v,e in zip(vals,powers):term=term*pow(v,e,p)%p
                ans=(ans+term)%p
            return ans
        Ns={j:u[j] for j in range(d+1)};es={j:0 for j in range(d+1)}
        Ns[d+1]=-A;es[d+1]=1
        for j in range(d+1,Dmax):
            N,e=Ns[j],es[j]
            Ns[j+1]=s.expand(S*S*along(N)-A*S*s.diff(N,u[d])-e*N*(S*along(S)-A*s.diff(S,u[d])))
            es[j+1]=e+2
        bounds=[]
        for j in range(d+1,Dmax+1):
            jet,chal=degrees(Ns[j]);e=2*(j-d)-1
            assert jet<=1+e*(B-1) and chal<=e*H
            bounds.append(dict(derivative=j,jet_degree=jet,challenge_degree=chal,denominator_exponent=e))
        for D in range(d,Dmax+1):
            tau=max(0,2*(D-d)-1)
            common={j:s.expand(Ns[j]*S**(tau-es[j])) for j in range(D+1)}
            for N in common.values():
                jet,chal=degrees(N);assert jet<=1+tau*(B-1) and chal<=tau*H
            coeff_terms={j:terms(N) for j,N in common.items()};St=terms(S);Qt=terms(Q)
            for p in (101,1009):
                for _ in range(12):
                    while True:
                        vals=[rng.randrange(p) for _ in gens];ss=ev(St,vals,p)
                        if ss:break
                    P=[ev(coeff_terms[j],vals,p)*pow(ss,-tau,p)*pow(math.factorial(j),-1,p)%p for j in range(D+1)]
                    jets=[P]
                    for _ in range(d):jets.append(deriv(jets[-1],p))
                    assert all(jets[j][0]==vals[j+2] for j in range(d+1))
                    out=[0]
                    for powers,c in Qt:
                        term=scale(power([vals[0],1],powers[0],p),int(c)*pow(vals[1],powers[1],p),p)
                        for j,e in enumerate(powers[2:]):term=mul(term,power(jets[j],e,p),p)
                        out=add(out,term,p)
                    assert out[0]==ev(Qt,vals,p)
                    assert all((out[j] if j<len(out) else 0)==0 for j in range(1,D-d+1))
                    tests+=1
        records.append(dict(order=d,Q=str(Q),B=B,H=H,Dmax=Dmax,numerator_bounds=bounds))
    data=dict(status='PASS',equations=len(specs),finite_taylor_fixtures=tests,records=records,
              scope='Exact higher-order reconstruction and degree checks. The generic intersection argument is a separate written proof.')
    Path(__file__).with_name('reconstruction_verification.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({k:v for k,v in data.items() if k!='records'},indent=2))


if __name__=='__main__':run()
