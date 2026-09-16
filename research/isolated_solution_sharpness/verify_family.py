#!/usr/bin/env python3
"""Exact fixed-order Wronskian classification, separant, and triple checks."""
import itertools
import json
import math
from pathlib import Path
from arithmetic import add,mul,scale,deriv,trim,eval_poly


def locator(roots,p):
    R=[1]
    for a in roots:R=mul(R,[-a%p,1],p)
    return R


def quotient(R,a,p):
    Q=[0]*(len(R)-1);Q[-1]=R[-1]
    for j in range(len(Q)-2,-1,-1):Q[j]=(R[j+1]+a*Q[j+1])%p
    assert mul(Q,[-a%p,1],p)==R
    return Q


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


def residual(R,P,r,z,p):
    columns=[add(mul(R,deriv(phi,p),p),mul(P,phi,p),p,-1) for phi in phis(r,z,p)]
    return determinant(matrix_from_columns(columns,p),p)


def candidates(R,roots,r,p):
    quots={a:quotient(R,a,p) for a in roots};out=[]
    for multi in itertools.combinations_with_replacement(roots,r):
        P=[0];H=[1]
        for a in multi:
            P=add(P,quots[a],p);H=mul(H,[-a%p,1],p)
        assert mul(P,H,p)==mul(R,deriv(H,p),p)
        out.append((H[0],tuple(P),tuple(H),multi))
    assert len({P for z,P,H,m in out})==len(out)==math.comb(len(roots)+r-1,r)
    return out


def exhaustive(D,r,p,roots):
    R=locator(roots,p);want={(z,P) for z,P,H,m in candidates(R,roots,r,p)};actual=set();affine_checks=0
    for co in itertools.product(range(p),repeat=D+1):
        P=trim(list(co));Q0=residual(R,P,r,0,p)
        Q1=add(residual(R,P,r,1,p),Q0,p,-1)
        # Independent third challenge evaluation checks affine dependence.
        assert residual(R,P,r,2,p)==add(Q0,scale(Q1,2,p),p);affine_checks+=1
        if Q1==[0]:
            if Q0==[0]:actual.update((z,tuple(P)) for z in range(p))
            continue
        j=next(j for j,c in enumerate(Q1) if c)
        z=-(Q0[j] if j<len(Q0) else 0)*pow(Q1[j],-1,p)%p
        if add(Q0,scale(Q1,z,p),p)==[0]:actual.add((z,tuple(P)))
    good=p>D+r
    assert want<=actual
    if good:assert actual==want,(D,r,p,actual-want)
    return dict(D=D,order=r-1,p=p,roots=roots,polynomials_exhausted=p**(D+1),
                polynomial_challenge_pairs_covered=p**(D+2),predicted_pairs=len(want),
                actual_pairs=len(actual),extra_pairs=len(actual-want),
                affine_challenge_checks=affine_checks,characteristic_hypothesis=good)


def separant_checks():
    count=0;rows=[]
    for r in range(2,7):
        D=max(r-1,3);p=101;R=locator(list(range(1,D+2)),p)
        for z in (0,1,13):
            P=[(3*j*j+7*j+11)%p for j in range(D+1)]
            phi=phis(r,z,p)
            columns=[add(mul(R,deriv(v,p),p),mul(P,v,p),p,-1) for v in phi]
            matrix=matrix_from_columns(columns,p)
            # Highest jet appears only in the final derivative row.
            matrix[-1]=[scale(v,-1,p) for v in phi]
            got=determinant(matrix,p)
            C=math.prod(math.factorial(j) for j in range(1,r))%p
            expected=scale(mul(power(R,r-1,p),[(-1)**(r-1)*z%p]+[0]*(r-1)+[1],p),(-1)**r*C,p)
            assert got==expected and got!=[0];count+=1
        rows.append(dict(order=r-1,D=D,p=p,checks=3))
    return dict(total=count,fixtures=rows)


def triple_checks(r,roots,p,label_mode="product"):
    R=locator(roots,p);cand=candidates(R,roots,r,p);checked=collinear=skipped=0;maxdeg=0
    if label_mode=="multiplicity":
        assert len(roots)==2
        cand=[(multi.count(roots[-1]),P,H,multi) for z,P,H,multi in cand]
    for triple in itertools.combinations(cand,3):
        z=[v[0] for v in triple]
        if len(set(z))<3:skipped+=1;continue
        c=[(z[1]-z[2])%p,(z[2]-z[0])%p,(z[0]-z[1])%p]
        num=[0]
        for i in range(3):
            term=deriv(list(triple[i][2]),p)
            for j in range(3):
                if i!=j:term=mul(term,list(triple[j][2]),p)
            num=add(num,scale(term,c[i],p),p)
        if num==[0]:collinear+=1
        else:
            assert len(num)-1<=3*r-2;maxdeg=max(maxdeg,len(num)-1)
        checked+=1
    # Check the affine-line occupancy through every distinct-labeled pair
    # directly in residue-vector space, including all candidate multiplicities.
    vec=[([m.count(a) for a in roots],z) for z,P,H,m in cand]
    maxline=0
    for i in range(len(vec)):
        vi,zi=vec[i]
        for j in range(i+1,len(vec)):
            vj,zj=vec[j]
            if zi==zj:continue
            hits=[]
            for k,(vk,zk) in enumerate(vec):
                if all(((zj-zi)*(vk[c]-vi[c])-(zk-zi)*(vj[c]-vi[c]))%p==0 for c in range(len(roots))):hits.append(k)
            assert len(hits)<=r+1;maxline=max(maxline,len(hits))
    assert collinear*3<=(r-1)*math.comb(len(cand),2)
    return dict(r=r,p=p,roots=roots,label_mode=label_mode,candidates=len(cand),distinct_label_triples=checked,
                collinear_triples=collinear,skipped_collision_triples=skipped,
                maximum_nonzero_numerator_degree=maxdeg,maximum_labeled_line_size=maxline)


def prime_sidon(r,N):
    # Uniform explicit loose bound for all stages k<=N-1, derived by
    # summing collision polynomial root bounds over product cardinalities.
    def forbidden(k):
        def multiset_count(s):return math.comb(k+s-1,s) if s else 1
        return (k+1+sum(j*multiset_count(r-j)*multiset_count(r) for j in range(1,r+1))
                +sum((j-i)*multiset_count(r-i)*multiset_count(r-j)
                     for i in range(1,r+1) for j in range(i+1,r+1)))
    bound=max(forbidden(k) for k in range(1,N))
    p=next(q for q in range(max(bound,N+r)+1,2*max(bound,N+r)+2) if prime(q))
    roots=[1];a=2
    def products(roots):
        return [math.prod(m)%p for m in itertools.combinations_with_replacement(roots,r)]
    while len(roots)<N:
        prods=products(roots+[a])
        if len(prods)==len(set(prods)):roots.append(a)
        a+=1;assert a<p
    R=locator(roots,p);cand=candidates(R,roots,r,p)
    assert len({z for z,P,H,m in cand})==len(cand)
    # Evaluate the full Wronskian for a representative subset, and the
    # underlying polynomial identity for every candidate (above).
    sample=cand[::max(1,len(cand)//12)]
    for z,P,H,m in sample:assert residual(R,list(P),r,z,p)==[0]
    return dict(D=N-1,r=r,order=r-1,p=p,roots=roots,greedy_forbidden_bound=bound,
                distinct_regular_isolated_labels=len(cand),wronskians_checked=len(sample),
                identities_checked=len(cand))


def main():
    data={'status':'PASS','separant_checks':separant_checks()}
    rows=[]
    for args in [(1,2,5,[1,2]),(1,3,7,[1,2]),(2,3,7,[1,2,3]),(2,4,7,[1,2,3])]:
        row=exhaustive(*args);rows.append(row);print(json.dumps(row),flush=True)
    data['exhaustive_fixtures']=rows
    data['characteristic_negative_controls']=[exhaustive(1,2,3,[1,2]),exhaustive(2,3,5,[1,2,3])]
    data['triple_checks']=[triple_checks(3,[1,99],101),triple_checks(3,[1,2,3,4],101),
                           triple_checks(4,[1,2,3],101),triple_checks(4,[1,2],101,"multiplicity")]
    assert data['triple_checks'][0]['collinear_triples']>=1
    assert data['triple_checks'][-1]['maximum_labeled_line_size']==5
    assert data['triple_checks'][-1]['collinear_triples']==10
    data['prime_field_sidon_fixtures']=[prime_sidon(3,5),prime_sidon(4,5),prime_sidon(5,4),
                                        prime_sidon(3,17),prime_sidon(4,9),prime_sidon(5,7)]
    data['scope']='Actual isolated solution-count sharpness at fixed derivative order, separants, polynomial-size prime labels, and finite triple-incidence structure. Not a proximity-gap lower bound.'
    Path(__file__).with_name('higher_isolated_verification.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2),flush=True)


if __name__=='__main__':main()
