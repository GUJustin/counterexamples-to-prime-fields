"""Exact algebra replay of excluded-shape moments and inverse Dickson bounds.
No coefficient-bank search. Standard-library arithmetic only.
"""
from collections import Counter
from fractions import Fraction
from math import gcd
from pathlib import Path
import json

def dickson(r,z,p):
    a,b=2,z
    if r==0:return a
    for j in range(1,r):a,b=b,(z*b-a)%p
    return b

rows=[]
for p in (11,17,31,47):
    def chi(x):
        y=pow(x%p,(p-1)//2,p)
        return -1 if y==p-1 else y
    for n in sorted({p-1,(p-1)//2}):
        domain=[x for x in range(1,p) if pow(x,n,p)==1]
        for e in range(3,n):
            k=e-1
            if gcd(k,n)!=1:continue
            def value(t):
                return (4-4*pow(t,k-1,p)*(t-1)**2*pow((pow(t,k,p)-1)**2,-1,p))%p
            vals=[value(t) for t in domain if t!=1]
            assert all(chi(4-v)==1 for v in vals)
            cnt=Counter(v for v in vals if v)
            m=sum(cnt.values()); energy=sum(v*v for v in cnt.values())
            HH=[sum(c*chi(b-v) for v,c in cnt.items()) for b in range(p)]
            JJ=[chi(b)*HH[b] for b in range(p)]
            assert JJ[4]==m
            retained=[JJ[b] for b in range(p) if b not in (0,4)]
            ss=p*energy-2*m*m-HH[0]**2
            assert sum(retained)==-2*m and sum(x*x for x in retained)==ss
            N=p-2
            for K in range(1,n+1):
                bound=Fraction(N*ss-4*m*m,ss+N*K*K+4*K*m)
                hits=sum(x>=K for x in retained)
                assert hits<=bound
                if hits:assert ss>=K*K+Fraction((K+2*m)**2,p-3)
            inv=pow(k,-1,n); r=min(inv,n-inv)
            assert r>=2
            for u in domain:
                if u==1:continue
                t=pow(u,r,p); z=(u+pow(u,-1,p))%p
                sr=(dickson(r,z,p)-2)*pow((z-2)%p,-1,p)%p
                assert value(t)==(4-4*sr)%p
                if r%2:
                    root=(1+sum(dickson(j,z,p) for j in range(1,(r-1)//2+1)))%p
                    assert sr==root*root%p
            assert max(cnt.values(),default=0)<=2*(r-1)
            assert energy<=2*(r-1)*m
            if r==2:assert energy==2*m
            rows.append(dict(p=p,n=n,e=e,inverse_height=r,nonzero_mass=m,energy=energy,excluded_second_moment=ss,passed=True))
out=dict(schema=1,profiles=len(rows),threshold_tests=sum(r['n'] for r in rows),rows=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
