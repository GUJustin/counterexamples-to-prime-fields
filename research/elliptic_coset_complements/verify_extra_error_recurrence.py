#!/usr/bin/env python3
"""Exact RS replay of the moment reduction, not an elliptic counterexample."""
import json
from pathlib import Path

p, n, k, ell = 1009, 264, 173, 23
r = n-k
domain = list(range(n))

def locator(roots):
    out=[1]
    for x in roots:
        new=[0]*(len(out)+1)
        for i,a in enumerate(out):
            new[i]=(new[i]-x*a)%p
            new[i+1]=(new[i+1]+a)%p
        out=new
    return out

def evaluate(poly,x):
    out=0
    for a in reversed(poly): out=(out*x+a)%p
    return out

def solve(matrix, rhs):
    a=[row[:]+[v] for row,v in zip(matrix,rhs)]
    for j in range(len(a)):
        pivot=next(i for i in range(j,len(a)) if a[i][j])
        a[j],a[pivot]=a[pivot],a[j]
        inv=pow(a[j][j],-1,p)
        a[j]=[(v*inv)%p for v in a[j]]
        for i in range(len(a)):
            if i!=j:
                factor=a[i][j]
                a[i]=[(u-factor*v)%p for u,v in zip(a[i],a[j])]
    return [row[-1] for row in a]

phi=locator(domain)
derivative=[i*phi[i]%p for i in range(1,len(phi))]
weights=[pow(evaluate(derivative,x),-1,p) for x in domain]
powers=[[pow(x,j,p) for j in range(r)] for x in domain]

def syndrome(values):
    return [sum(values[x]*weights[x]*powers[x][j] for x in domain)%p
            for j in range(r)]

# Two artificial 23-point blocks test the general RS algebra only.
base=list(range(1,2*ell+1))
L=locator(base)
M=r-2*ell

def transform(s):
    return [sum(a*s[i+j] for i,a in enumerate(L))%p for j in range(M)]

code=[evaluate([(i*i+3*i+7)%p for i in range(k)],x) for x in domain]
assert not any(syndrome(code))
cases=[]
for d in range(6):
    extras=([0]+list(range(100,104)))[:d]
    error=[0]*n
    # Deliberate zeros within both original blocks exercise partial support.
    for x in base:
        if x%3: error[x]=(x*x+17)%p or 1
    for i,x in enumerate(extras): error[x]=i+11
    received=[(a+b)%p for a,b in zip(code,error)]
    s=syndrome(received)
    assert s==syndrome(error)
    c=transform(s)
    J=locator(extras)
    assert all(sum(J[i]*c[i+j] for i in range(d+1))%p==0
               for j in range(M-d))
    eta=[error[x]*evaluate(L,x)*weights[x]%p for x in extras]
    assert all(eta)
    assert all(c[j]==sum(a*pow(x,j,p) for x,a in zip(extras,eta))%p
               for j in range(M))
    if d:
        recovered=solve([[pow(x,j,p) for x in extras] for j in range(d)],c[:d])
        assert recovered==eta
        # A different split domain locator must not pass this exact sequence.
        wrong=locator(extras[:-1]+[200])
        assert any(sum(wrong[i]*c[i+j] for i in range(d+1))%p
                   for j in range(M-d))
    else:
        assert not any(c)
    # Artificially padding a locator is valid algebraically but adds no error.
    padded=locator(extras+[201])
    assert all(sum(padded[i]*c[i+j] for i in range(d+2))%p==0
               for j in range(M-d-1))
    padded_eta=solve([[pow(x,j,p) for x in extras+[201]]
                      for j in range(d+1)],c[:d+1])
    assert padded_eta==eta+[0]
    cases.append({'extra_errors':d,'recurrence_equations':M-d,
                  'zero_coordinate_tested':d>0,'padding_coefficient':0})

receipt={'status':'PASS','construction_established':False,
         'scope':'general RS moment equivalence, zero root, partial block errors, and padding rejection',
         'elliptic_domain':False,'p':p,'n':n,'k':k,'redundancy':r,
         'base_support':2*ell,'transformed_sequence_length':M,'cases':cases}
Path(__file__).with_suffix('.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
