"""Exhaustive F_9 polynomial classification and full-support line checks."""
from itertools import product,combinations
from pathlib import Path
import json,random
BASE=Path(__file__).resolve().parent
p,q,D=3,9,2

def add(a,b):return ((a%3+b%3)%3)+3*((a//3+b//3)%3)
def neg(a):return (-a%3)+3*(-(a//3)%3)
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    a0,a1=a%3,a//3;b0,b1=b%3,b//3
    return (a0*b0-a1*b1)%3+3*((a0*b1+a1*b0)%3)
def power(a,n):
    out=1
    while n:
        if n&1:out=mul(out,a)
        a=mul(a,a);n//=2
    return out
def inv(a):assert a;return power(a,7)
def trim(P):
    P=list(P)
    while len(P)>1 and P[-1]==0:P.pop()
    return P
def plus(P,Q):return trim([add(P[j] if j<len(P) else 0,Q[j] if j<len(Q) else 0) for j in range(max(len(P),len(Q)))])
def times(P,Q):
    R=[0]*(len(P)+len(Q)-1)
    for j,a in enumerate(P):
        for k,b in enumerate(Q):R[j+k]=add(R[j+k],mul(a,b))
    return trim(R)
def derivative(P):return trim([mul(j%3,P[j]) for j in range(1,len(P))] or [0])
def evaluate(P,x):
    out=0
    for a in reversed(P):out=add(mul(out,x),a)
    return out
def scaled(P,a):return trim([mul(x,a) for x in P])
def interpolate(xs,ys):
    out=[0]
    for i,(x,y) in enumerate(zip(xs,ys)):
        basis=[1];den=1
        for j,u in enumerate(xs):
            if i!=j:basis=times(basis,[neg(u),1]);den=mul(den,sub(x,u))
        out=plus(out,scaled(basis,mul(y,inv(den))))
    return out

def main():
    assert all(mul(a,inv(a))==1 for a in range(1,q))
    U,V=[1,1,1],[0,1,1]
    a=times(U,V);b1=derivative(a)
    b2=plus(times(derivative(U),V),scaled(times(U,derivative(V)),2))
    candidates=[]
    for coefficients in product(range(q),repeat=D+1):
        P=trim(coefficients)
        residual=plus(times(a,derivative(P)),scaled(plus(times(b1,P),times(b2,times(P,P))),2))
        if residual==[0]:candidates.append(P)
    assert len(candidates)==5 and len(candidates)<=2*D+2
    xs=list(range(q));values=[[evaluate(P,x) for x in xs] for P in candidates]
    rng=random.Random(20260917)
    lines=[([rng.randrange(q) for _ in xs],[rng.randrange(q) for _ in xs]) for _ in range(80)]
    for row in values:
        f=row[:];g=[0]*3+[1]*6
        for j in range(3,q):f[j]=sub(row[j],j-3)
        lines.append((f,g))
    counts=nonempty=max_bad=0
    for f,g in lines:
      for A in range(D+1,q+1):
        bad=set()
        for z in range(q):
            supports=[[j for j in xs if row[j]==add(f[j],mul(z,g[j]))] for row in values]
            selected=[S for S in supports if len(S)>=A]
            assert len(selected)*(A-D)<=q
            for S in selected:
                fit=interpolate(S[:D+1],[g[j] for j in S[:D+1]])
                if any(evaluate(fit,j)!=g[j] for j in S):bad.add(z)
        assert len(bad)*(A-D)<=2*q*(q+2*D+2)
        max_bad=max(max_bad,len(bad));nonempty+=bool(bad);counts+=1
    result=dict(status='PASS',field='F_3[w]/(w^2+1)',degree=D,
                polynomials_enumerated=q**(D+1),solutions=candidates,
                received_lines=len(lines),line_threshold_cases=counts,
                nonempty_bad_cases=nonempty,maximum_observed_bad_labels=max_bad,
                scope='Extension-domain check at p=D+1, including the ordinary-list and fixed-equation full-support inequalities.')
    (BASE/'boundary_extension_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
