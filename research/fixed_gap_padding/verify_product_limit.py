from itertools import product
from pathlib import Path
import json


def multiply(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c


def evaluate(P,x,p):
    v=0
    for a in reversed(P):v=(v*x+a)%p
    return v


rows=[]
for r in range(1,7):
    for B in (1,2,3):
        blocks=[];domain=[]
        for i in range(r):
            choices=[]
            for a,b in ((10*i+1,10*i+4),(10*i+2,10*i+3)):
                F=[0]*(2*B+1);F[0]=a*b;F[B]=-a-b;F[2*B]=1
                choices.append(F);domain += [a,b]
            blocks.append(choices)
        locators=[]
        for selection in product((0,1),repeat=r):
            F=[1]
            for i,j in enumerate(selection):F=multiply(F,blocks[i][j])
            locators.append(F)
        assert len({tuple(F) for F in locators})==2**r
        D=max(j for F in locators[1:] for j,(a,b) in enumerate(zip(F,locators[0])) if a!=b)
        A=2*B*r;K=B*(2*r-1);n=4*B*r;s=A-K
        assert D==2*B*(r-1) and A-D-1==2*B-1 and D<K
        assert r*(s+1)<=A<=n and 4*r*s==n
        if B==1:
            W=[0]*K+locators[0][K:]
            for F in locators:
                P=[a-b for a,b in zip(W,F)]
                assert not any(P[K:])
                assert sum(evaluate(P,x,101)==evaluate(W,x,101) for x in domain)==A
        rows.append(dict(r=r,B=B,n=n,K=K,A=A,selected_list_size=2**r,
                         maximum_difference_degree=D,maximal_prefix_surplus=A-D-1))
result=dict(status='PASS',fixtures=rows,
            scope='Exact independent-product degrees and selected-list identities; finite-field agreement replay for B1 only.')
Path(__file__).with_name('product_limit_verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
