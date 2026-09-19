"""Independent stdlib arithmetic replay of a 0=1 original-Jacobian certificate.
No generated field tables, reduced matrix, or Gaussian elimination is trusted.
"""
import json,struct,time,hashlib
from pathlib import Path
start=time.monotonic();MOD=(1<<21)|5;DEG=21

def mul(a,b):
    z=0
    while b:
        if b&1:z^=a
        b>>=1;a<<=1
        if a>>DEG:a^=MOD
    return z

def power(a,n):
    z=1
    while n:
        if n&1:z=mul(z,a)
        a=mul(a,a);n>>=1
    return z

def lift(a):return [(a>>i)&1 for i in range(DEG)]
def ringmul(a,b):
    c=[0]*(2*DEG-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%4
    for i in range(2*DEG-2,DEG-1,-1):
        x=c[i]
        c[i]=0;c[i-DEG]=(c[i-DEG]-x)%4;c[i-DEG+2]=(c[i-DEG+2]-x)%4
    return c[:DEG]
def add(a,b,sign=1):return [(x+sign*y)%4 for x,y in zip(a,b)]
lines=Path('fixture.txt').read_text().splitlines();N,K,M,T=map(int,lines[0].split())
nodes=[tuple(map(int,s.split())) for s in lines[1:N+1]]
banks=[]
for s in lines[N+1:]:
    v=list(map(int,s.split()));banks.append((v[0],v[1],v[2],v[3:3+K],v[3+K:]))
assert len(banks)==M and all(len(v[-1])==T for v in banks)
raw=Path('contradiction.bin').read_bytes();weights=struct.unpack('<'+'I'*(M*T),raw)
assert len({x for x,f,g in nodes})==N
assert len({b[2] for b in banks})==M
coeff=[0]*(3*N+M*(K+1));rhs=0;used=0
for bi,(a,b,z,h,support) in enumerate(banks):
    for ri,idx in enumerate(support):
        w=weights[bi*T+ri]
        if not w:continue
        used+=1;x,f,g=nodes[idx]
        # Binary agreement and ring residual are recomputed from scratch.
        ev=0;rv=[0]*DEG
        for hc in reversed(h):
            ev=mul(ev,x)^hc
            rv=add(ringmul(rv,lift(x)),lift(hc))
        assert ev==f^mul(z,g)
        rv=add(add(rv,lift(f),-1),ringmul(lift(z),lift(g)),-1)
        assert all(v%2==0 for v in rv)
        obstruction=sum((v//2)<<j for j,v in enumerate(rv))
        rhs^=mul(w,obstruction)
        derivative=0
        for j in range(1,K,2):derivative^=mul(h[j],power(x,j-1))
        coeff[idx]^=mul(w,derivative)
        coeff[N+idx]^=w
        coeff[2*N+idx]^=mul(w,z)
        off=3*N+bi*(K+1)
        for j in range(K):coeff[off+j]^=mul(w,power(x,j))
        coeff[off+K]^=mul(w,g)
assert not any(coeff), 'Nonzero weighted Jacobian coefficient'
assert rhs==1, 'Missing contradiction'
result={'PASS':True,'claim':'No unramified mod-4 lift through this specific binary incidence point','N':N,'K':K,'bank_size':M,'retained_matches':T,'original_equations':M*T,'all_variable_columns':len(coeff),'certificate_nonzero_weights':used,'weighted_coefficients_all_zero':True,'weighted_obstruction':rhs,'seconds':time.monotonic()-start,'sha256':{p:hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in ['fixture.txt','contradiction.bin','test.cpp','witness.cpp']}}
Path('independent_verified.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
