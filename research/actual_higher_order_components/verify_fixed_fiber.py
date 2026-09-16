#!/usr/bin/env python3
"""Sharp isolated fixed-fiber counts and the affine graph obstruction."""
import itertools,json,math,random
from pathlib import Path
from verify import determinant,matrix_from_columns,power
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


def residual(R,P,d,p,separant=False):
    basis=[[0]*j+[1] for j in range(d+1)]
    cols=[add(mul(R,deriv(v,p),p),mul(P,v,p),p,-1) for v in basis]
    matrix=matrix_from_columns(cols,p)
    if separant:matrix[-1]=[scale(v,-1,p) for v in basis]
    return determinant(matrix,p)


def expected(R,roots,d,p):
    quots={a:quotient(R,a,p) for a in roots};out={(0,)}
    for degree in range(1,d+1):
        for multi in itertools.combinations_with_replacement(roots,degree):
            P=[0]
            for a in multi:P=add(P,quots[a],p)
            out.add(tuple(P))
    assert len(out)==math.comb(len(roots)+d,d)
    return out


def exhaustive(d,D,p):
    roots=list(range(1,D+2));R=locator(roots,p);want=expected(R,roots,d,p);got=set()
    for co in itertools.product(range(p),repeat=D+1):
        P=trim(list(co))
        if residual(R,P,d,p)==[0]:got.add(tuple(P))
    assert want<=got
    if p>D+d:assert got==want
    return dict(order=d,D=D,p=p,roots=roots,polynomials_exhausted=p**(D+1),
                predicted_isolated_points=len(want),actual_points=len(got),extra_points=len(got-want),
                characteristic_hypothesis=p>D+d)


def rational_incidence_checks():
    rng=random.Random(2026091620);rows=[]
    roots=list(range(1,8));p=1009
    for d in range(1,5):
        multis=[m for deg in range(d+1) for m in itertools.combinations_with_replacement(roots,deg)]
        chosen=rng.sample(multis,min(30,len(multis)))
        labels=rng.sample(range(p),len(chosen));cand=[]
        for z,multi in zip(labels,chosen):
            H=locator(multi,p)
            cand.append((z,H,[multi.count(a) for a in roots]))
        count=zero=maxdegree=0
        for triple in itertools.combinations(cand,3):
            z=[c[0] for c in triple];coeffs=[z[1]-z[2],z[2]-z[0],z[0]-z[1]]
            num=[0]
            for i,c in enumerate(coeffs):
                term=deriv(triple[i][1],p)
                for j in range(3):
                    if i!=j:term=mul(term,triple[j][1],p)
                num=add(num,scale(term,c,p),p)
            if num==[0]:zero+=1
            else:assert len(num)-1<=3*d-1;maxdegree=max(maxdegree,len(num)-1)
            count+=1
        largest=0
        for i,j in itertools.combinations(range(len(cand)),2):
            zi,Hi,vi=cand[i];zj,Hj,vj=cand[j]
            hits=sum(all(((zj-zi)*(vk[c]-vi[c])-(zk-zi)*(vj[c]-vi[c]))%p==0 for c in range(len(roots))) for zk,Hk,vk in cand)
            assert hits<=d+1;largest=max(largest,hits)
        # The residue line m/(X-a), labeled by m, attains d+1 points.
        assert len({m%p for m in range(d+1)})==d+1
        rows.append(dict(d=d,p=p,candidates=len(cand),triples_checked=count,
                         collinear_triples=zero,maximum_numerator_degree=maxdegree,
                         maximum_random_labeled_line=largest,attained_residue_line_size=d+1))
    # One candidate reused at several genuinely bad challenges. The first
    # D+1 zero direction values force G=0, contradicting the extra value 1.
    D=3;n=8;p=17;A=5;domain=list(range(n));f=[0]*4+[-j%p for j in range(1,5)];g=[0]*4+[1]*4
    bad=[]
    for z in range(p):
        support=[x for x in domain if (f[x]+z*g[x])%p==0]
        if len(support)>=A:
            assert support[:4]==[0,1,2,3] and len(support)==5
            assert g[support[-1]]==1
            bad.append(z)
    assert bad==[1,2,3,4] and len(bad)<=n
    return dict(triple_fixtures=rows,reused_zero_candidate_control=dict(p=p,D=D,n=n,A=A,bad_labels=bad,full_supports_have_no_direction_interpolant=True))


def main():
    rows=[]
    for d in (1,2,3):
        row=exhaustive(d,3,7);rows.append(row);print(json.dumps(row),flush=True)
    checks=0
    for d in range(1,5):
        D=max(d,4);p=101;R=locator(list(range(1,D+2)),p)
        for P in ([0],[1],[2,3],[1]+[0]*(D-1)+[1]):
            got=residual(R,P,d,p,True)
            target=scale(power(R,d,p),(-1)**(d+1)*math.prod(math.factorial(j) for j in range(1,d+1)),p)
            assert got==target and got!=[0];checks+=1
    data=dict(status='PASS',exhaustive_fixtures=rows,separant_checks=checks,
              rational_incidence_checks=rational_incidence_checks(),
              scope='Exact fixed-equation polynomial classification and separants, including zero. Adding a free challenge gives one degree-one affine graph per solution. No MCA lower bound is inferred.')
    Path(__file__).with_name('fixed_fiber_verification.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'status':'PASS','polynomials_exhausted':sum(x['polynomials_exhausted'] for x in rows),'separant_checks':checks},indent=2))


if __name__=='__main__':main()
