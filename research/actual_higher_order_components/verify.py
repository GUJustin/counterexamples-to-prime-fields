#!/usr/bin/env python3
"""Full power-component classification, separants, and reduced degree sections."""
import itertools,json,math
from pathlib import Path
from arithmetic import add,mul,scale,deriv,trim,eval_poly


def prime(p):
    return p>=2 and all(p%d for d in range(2,math.isqrt(p)+1))


def power(a,k,p):
    out=[1]
    for _ in range(k):out=mul(out,a,p)
    return out


def determinant(matrix,p):
    r=len(matrix);out=[0]
    for perm in itertools.permutations(range(r)):
        sign=(-1)**sum(perm[i]>perm[j] for i in range(r) for j in range(i+1,r))
        term=[sign%p]
        for i,j in enumerate(perm):term=mul(term,matrix[i][j],p)
        out=add(out,term,p)
    return out


def matrix_from_columns(columns,p):
    rows=[columns]
    for _ in range(len(columns)-1):rows.append([deriv(f,p) for f in rows[-1]])
    return rows


def phis(r,z,p):
    out=[[0]*j+[1] for j in range(1,r)]
    out.append([z%p]+[0]*(r-1)+[1])
    return out



def residual(P,r,e,z,p):
    columns=[add(scale(mul(P,deriv(phi,p),p),e,p),mul(deriv(P,p),phi,p),p,-1)
             for phi in phis(r,z,p)]
    return determinant(matrix_from_columns(columns,p),p)


def expected(r,e,p):
    out={(z,(0,)) for z in range(p)}
    for deg in range(1,r+1):
        for co in itertools.product(range(p),repeat=deg):
            if deg<r and co[0]!=0:continue
            H=list(co)+[1];base=power(H,e,p)
            labels=[co[0]] if deg==r else range(p)
            for c in range(1,p):
                P=tuple(scale(base,c,p))
                out.update((z,P) for z in labels)
    assert len(out)==p**(r+1)
    return out


def exhaustive(r,e,p):
    D=r*e;want=expected(r,e,p);got=set();tested=0
    for co in itertools.product(range(p),repeat=D+1):
        P=trim(list(co));Q0=residual(P,r,e,0,p);Qz=add(residual(P,r,e,1,p),Q0,p,-1)
        if Qz==[0]:
            if Q0==[0]:got.update((z,tuple(P)) for z in range(p))
        else:
            j=next(j for j,c in enumerate(Qz) if c)
            z=-(Q0[j] if j<len(Q0) else 0)*pow(Qz[j],-1,p)%p
            if add(Q0,scale(Qz,z,p),p)==[0]:got.add((z,tuple(P)))
        tested+=1
    good=p>D+r-1
    assert want<=got
    if good:assert got==want,(r,e,p,got-want)
    return dict(order=r,e=e,D=D,p=p,polynomials_exhausted=tested,
                polynomial_label_pairs_covered=tested*p,predicted_pairs=len(want),
                actual_pairs=len(got),extra_pairs=len(got-want),characteristic_hypothesis=good)


def separants():
    rows=[]
    for r in range(1,6):
        for e in (1,2,3):
            D=r*e;p=101
            H=[j+1 for j in range(r)]+[1];P=scale(power(H,e,p),7,p)
            for z in (0,1,17):
                phi=phis(r,z,p)
                cols=[add(scale(mul(P,deriv(v,p),p),e,p),mul(deriv(P,p),v,p),p,-1) for v in phi]
                M=matrix_from_columns(cols,p);M[-1]=[scale(v,-1,p) for v in phi]
                value=determinant(M,p)
                Cr=math.prod(math.factorial(j) for j in range(1,r))
                expected=scale(mul(power(scale(P,e,p),r-1,p),[(-1)**(r-1)*z%p]+[0]*(r-1)+[1],p),(-1)**r*Cr,p)
                assert value==expected and value!=[0]
            # Actual member at H(0); and a boundary solution not covered by
            # the initial monic-degree-r chart (first column zero for r>=2).
            assert residual(P,r,e,H[0],p)==[0]
            if r>=2:
                for z in (0,1,17):assert residual([0]*e+[1],r,e,z,p)==[0]
            rows.append(dict(order=r,e=e,D=D,p=p,separants=3,actual_members=1,boundary_checks=3 if r>=2 else 0))
    return rows


def inverse_matrix(M,p):
    n=len(M);a=[[v%p for v in row]+[int(i==j) for j in range(n)] for i,row in enumerate(M)]
    for j in range(n):
        pivot=next(i for i in range(j,n) if a[i][j]);a[j],a[pivot]=a[pivot],a[j]
        inv=pow(a[j][j],-1,p);a[j]=[v*inv%p for v in a[j]]
        for i in range(n):
            if i!=j:
                c=a[i][j];a[i]=[(u-c*v)%p for u,v in zip(a[i],a[j])]
    assert [row[:n] for row in a]==[[int(i==j) for j in range(n)] for i in range(n)]
    return [row[n:] for row in a]


def degree_section(r,e,fiber=False):
    D=r*e;p=next(p for p in range(max(101,D+r+1),10000) if prime(p) and (p-1)%e==0)
    unity=[a for a in range(1,p) if pow(a,e,p)==1];assert len(unity)==e
    points=list(range(1,r+1 if fiber else r+2))
    M=[[pow(a,j,p) for j in range(r+1)] for a in points]
    if fiber:M.append([1]+[0]*(r-1)+[-1]) # H(0)=leading(H), i.e. z=1
    inv=inverse_matrix(M,p);seen=set();jacobians=0
    dim=r-1 if fiber else r
    for tail in itertools.product(unity,repeat=dim):
        values=[1,*tail]+([0] if fiber else [])
        H=trim([sum(a*b for a,b in zip(row,values))%p for row in inv])
        P=power(H,e,p)
        assert all(eval_poly(P,a,p)==1 for a in points)
        if fiber:assert H[0]==(H[r] if r<len(H) else 0)
        assert tuple(P) not in seen;seen.add(tuple(P))
        # In evaluation coordinates, the section equations are independent
        # U_i^e=1; all derivatives are nonzero (reduced intersection).
        assert all(e*pow(v,e-1,p)%p for v in tail);jacobians+=1
    assert len(seen)==e**dim
    return dict(order=r,e=e,D=D,p=p,fixed_challenge_fiber=fiber,
                reduced_section_points=len(seen),predicted_degree=e**dim,
                reduced_jacobian_checks=jacobians)


def main():
    data=dict(status='PASS',separant_fixtures=separants())
    rows=[]
    for args in [(1,4,7),(2,1,5),(2,2,7),(3,1,7)]:
        row=exhaustive(*args);rows.append(row);print(json.dumps(row),flush=True)
    data['exhaustive_full_fixtures']=rows
    data['characteristic_boundary_fixture']=exhaustive(2,2,5)
    data['characteristic_negative_control']=exhaustive(2,2,3)
    assert data['characteristic_negative_control']['extra_pairs']>0
    data['power_image_degree_sections']=[degree_section(r,e,fiber) for r in range(1,5) for e in range(1,6) for fiber in (False,True)]
    data['scope']='Full actual power-component classification, exact separants, and reduced sections of the projected power image and fixed-label fibers. No generic-component upper bound or MCA lower bound is certified by these finite checks.'
    Path(__file__).with_name('positive_components_verification.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'status':'PASS','separant_fixtures':len(data['separant_fixtures']),
                      'degree_sections':len(data['power_image_degree_sections']),
                      'negative_control':data['characteristic_negative_control']},indent=2),flush=True)


if __name__=='__main__':main()
