"""Exact polynomial-matrix and full-support checks for linear differential MCA."""
from pathlib import Path
from itertools import combinations,permutations,product
from math import factorial
import json,random,time
def degree_at_most_on_support(xs,ys,D,p):
    coefficients=ys[:]
    for j in range(1,len(xs)):
        for i in range(len(xs)-1,j-1,-1):
            coefficients[i]=(coefficients[i]-coefficients[i-1])*pow(xs[i]-xs[i-j],-1,p)%p
    return all(c==0 for c in coefficients[D+1:])



def trim(a):
    while len(a)>1 and a[-1]==0:a.pop()
    return a


def add(a,b,p):
    return trim([((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0))%p for i in range(max(len(a),len(b)))])


def scale(a,c,p):return trim([c*x%p for x in a])


def mul(a,b,p):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]=(out[i+j]+x*y)%p
    return trim(out)


def value(a,z,p):
    y=0
    for c in reversed(a):y=(y*z+c)%p
    return y


def determinant(matrix,p):
    n=len(matrix)
    if n==0:return [1]
    out=[0]
    for pi in permutations(range(n)):
        term=[1]
        for i,j in enumerate(pi):term=mul(term,matrix[i][j],p)
        inv=sum(pi[i]>pi[j] for i in range(n) for j in range(i+1,n))
        out=add(out,scale(term,(-1)**inv,p),p)
    return out


def generic_pivot(T,M,p):
    for r in range(min(len(T),M),0,-1):
        for rows in combinations(range(len(T)),r):
            for cols in combinations(range(M),r):
                delta=determinant([[T[i][j] for j in cols] for i in rows],p)
                if delta!=[0]:return r,rows,cols,delta
    return 0,(),(),[1]


def affine_solutions(T,b,M,p):
    mat=[row[:]+[rhs] for row,rhs in zip(T,b)];pivots=[];i=0
    for j in range(M):
        pivot=next((k for k in range(i,len(mat)) if mat[k][j]),None)
        if pivot is None:continue
        mat[i],mat[pivot]=mat[pivot],mat[i]
        inv=pow(mat[i][j],-1,p);mat[i]=[x*inv%p for x in mat[i]]
        for k in range(len(mat)):
            if k!=i and mat[k][j]:
                c=mat[k][j];mat[k]=[(x-c*y)%p for x,y in zip(mat[k],mat[i])]
        pivots.append(j);i+=1
    if any(not any(row[:M]) and row[M] for row in mat):return [],len(pivots)
    free=[j for j in range(M) if j not in pivots];sol=[]
    for values in product(range(p),repeat=len(free)):
        v=[0]*M
        for j,x in zip(free,values):v[j]=x
        for row,j in zip(mat,pivots):v[j]=(row[M]-sum(row[k]*v[k] for k in free))%p
        sol.append(v)
    return sol,len(pivots)


def operator(D,order,p):
    M=D+1;T=[[[0] for _ in range(M)] for _ in range(M)]
    for i in range(M):
        if order==1:
            T[i][i]=[(i-D)%p]
            if i:T[i-1][i]=[0,(-i)%p]
        else:
            T[i][i]=[((i-D)*(i-D+1))%p]
            if i:T[i-1][i]=[0,2*i*(D-i)%p]
            if i>=2:T[i-2][i]=[0,0,i*(i-1)%p]
    return T


def fixture(name,p,D,n,A,T,b,rng):
    M=D+1;H=max([len(a)-1 for row in T for a in row]+[len(a)-1 for a in b]+[0])
    r,rows,cols,Delta=generic_pivot(T,M,p);ell=M-r
    augmented=[row+[rhs] for row,rhs in zip(T,b)]
    ra,_,_,_=generic_pivot(augmented,M+1,p)
    evaluated=[]
    for z in range(p):
        sols,rank=affine_solutions([[value(a,z,p) for a in row] for row in T],[value(a,z,p) for a in b],M,p)
        if ra==r and value(Delta,z,p):assert rank==r and len(sols)==p**ell
        evaluated.append(sols)
    if ra>r:
        labels=[z for z,sols in enumerate(evaluated) if sols]
        assert len(labels)<=H*(r+1)
        return dict(name=name,generically_inconsistent=True,consistent_labels=labels,H=H,r=r)
    tuples=list(combinations(range(n),ell));curves={}
    for J in tuples:
        C=[T[i] for i in rows]+[[[pow(x,j,p)] for j in range(M)] for x in J]
        det=determinant(C,p)
        assert len(det)-1<=H*r
        if det!=[0]:curves[J]=(C,det)
    line_rows=[];degree_checks=0;branches={'root_count':0,'affine_graph':0};tuple_checks=0
    for variant in range(4):
        f=[rng.randrange(p) for _ in range(n)];g=[rng.randrange(p) for _ in range(n)]
        if variant<2:
            z=next(z for z,sols in enumerate(evaluated) if sols)
            v=rng.choice(evaluated[z])
            for x in rng.sample(range(n),A):f[x]=(value(v,x,p)-z*g[x])%p
        elif variant==2:
            # Persistent zero graph with accidental zeros; homogeneous cases
            # then exercise the h>D branch of the proof.
            f=[0]*(A-1)+[rng.randrange(p) for _ in range(n-A+1)]
            g=[0]*(A-1)+[1]*(n-A+1)
        bad={};all_bad_pairs=0
        for z,sols in enumerate(evaluated):
            for v in sols:
                S=[x for x in range(n) if value(v,x,p)==(f[x]+z*g[x])%p]
                if len(S)>=A and not degree_at_most_on_support(S,[g[x] for x in S],D,p):
                    all_bad_pairs+=1
                    if z not in bad:bad[z]=(v,S)
        E=H*r+1;Q=max(n-D-1,E*(n-D)//(A-D))
        bound=H*r+factorial(n)//factorial(n-ell)*Q//((A-D)**ell)
        assert len(bad)<=bound
        for z,(v,S) in bad.items():
            if not value(Delta,z,p):continue
            good=sum(set(J)<=set(S) and value(det,z,p)!=0 for J,(_,det) in curves.items())
            assert factorial(ell)*good>=(A-D)**ell
            tuple_checks+=1
        for J,(C,det) in curves.items():
            rhs=[b[i] for i in rows]+[[f[x],g[x]] for x in J]
            numerators=[]
            for j in range(M):
                replaced=[[rhs[i] if k==j else C[i][k] for k in range(M)] for i in range(M)]
                N=determinant(replaced,p);assert len(N)-1<=E;numerators.append(N)
            residuals=[]
            for x in range(n):
                R=[0]
                for j,N in enumerate(numerators):R=add(R,scale(N,pow(x,j,p),p),p)
                R=add(R,scale(mul(det,[f[x],g[x]],p),-1,p),p)
                assert len(R)-1<=E;residuals.append(R);degree_checks+=1
            h=sum(R==[0] for R in residuals)
            branches['root_count' if h<=D else 'affine_graph']+=1
            covered=[]
            for z in range(p):
                dz=value(det,z,p)
                if not dz:continue
                v=[value(N,z,p)*pow(dz,-1,p)%p for N in numerators]
                S=[x for x,R in enumerate(residuals) if value(R,z,p)==0]
                assert S==[x for x in range(n) if value(v,x,p)==(f[x]+z*g[x])%p]
                if len(S)>=A and not degree_at_most_on_support(S,[g[x] for x in S],D,p):covered.append(z)
            assert len(covered)<=Q
        line_rows.append(dict(variant=variant,bad_labels=len(bad),bad_witnesses=all_bad_pairs,bound=bound))
    return dict(name=name,p=p,D=D,n=n,A=A,H=H,r=r,ell=ell,
                exceptional_labels=[z for z in range(p) if not value(Delta,z,p)],
                lines=line_rows,residual_degree_checks=degree_checks,
                determining_tuple_checks=tuple_checks,branches=branches)


def main():
    started=time.monotonic();rng=random.Random(202609161500);out=[]
    for p in (7,11):
        D=2;n=6;A=4
        cases=[('one_row',[[[1],[0,1],[0,0,1]]],[[1,1]]),
               ('rank_drop_consistent',[[[-2%p,1],[0,-2%p,1],[0]]],[[-2%p,-1%p,1]]),
               ('rank_drop_inconsistent',[[[-2%p,1],[0,-2%p,1],[0]]],[[1]]),
               ('two_rows',[[[1],[0,1],[0]],[[0],[1],[0,1]]],[[1],[1,1]]),
               ('generic_inconsistent',[[[1],[0,1],[0]],[[2],[0,2],[0]]],[[0],[-2%p,1]]),
               ('unique_rational',[[[-2%p,1],[0],[0]],[[0],[1],[0]],[[0],[0],[1]]],[[0,1],[0,0,1],[1]])]
        for name,T,b in cases:out.append(fixture(name,p,D,n,A,T,b,rng))
        for D,order in ((2,1),(3,1),(3,2)):
            T=operator(D,order,p);b=[[0] for row in T]
            out.append(fixture(f'order_{order}_homogeneous',p,D,6 if p==7 else 8,D+2,T,b,rng))
            # Affine shift by X^D+z X^(D-1), retaining bounded z-degree.
            shift=[[0] for _ in range(D+1)];shift[D]=[1];shift[D-1]=[0,1]
            b=[]
            for row in T:
                rhs=[0]
                for a,v in zip(row,shift):rhs=add(rhs,mul(a,v,p),p)
                b.append(rhs)
            out.append(fixture(f'order_{order}_inhomogeneous',p,D,6 if p==7 else 8,D+2,T,b,rng))
    # Characteristic hypothesis is necessary for the ODE kernel dimension.
    p=3;D=4;T=[[[0] for _ in range(D+1)] for _ in range(D)]
    for i in range(1,D+1):T[i-1][i]=[i%p]
    r,*_=generic_pivot(T,D+1,p)
    assert D+1-r==2 # constants and X^3 solve P'=0
    result=dict(status='passed',fixtures=out,characteristic_negative_control=True,
                seconds=time.monotonic()-started,
                scope='Finite polynomial-matrix checks, including exact generic minors, rank drops, inhomogeneous systems, determining-tuple counts, Cramer residual degrees, full-support witnesses, and both proof branches. These supplement the written theorem.')
    Path(__file__).with_name('linear_differential_mca_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status='passed',fixtures=len(out),
        lines=sum(len(x.get('lines',[])) for x in out),
        residual_degree_checks=sum(x.get('residual_degree_checks',0) for x in out),
        determining_tuple_checks=sum(x.get('determining_tuple_checks',0) for x in out),
        branches={k:sum(x.get('branches',{}).get(k,0) for x in out) for k in ('root_count','affine_graph')},
        seconds=result['seconds']),indent=2))


if __name__=='__main__':main()
