"""Exact prime-field fixtures for anchored, fixed-rate fixed-gap padding."""
from pathlib import Path
from itertools import combinations
from collections import defaultdict
from math import comb,isqrt
from fractions import Fraction
import json,time
def trim(a):
    while len(a)>1 and not a[-1]:a.pop()
    return a


def subtract(a,b,p):
    return trim([((a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0))%p
                 for i in range(max(len(a),len(b)))])


def value(a,x,p):
    answer=0
    for c in reversed(a):answer=(answer*x+c)%p
    return answer


def locator(roots,p):
    out=[1]
    for a in roots:
        nxt=[0]*(len(out)+1)
        for i,c in enumerate(out):
            nxt[i]=(nxt[i]-a*c)%p
            nxt[i+1]=(nxt[i+1]+c)%p
        out=nxt
    return out


def root_quotient(R,a,p):
    out=[0]*(len(R)-1);out[-1]=R[-1]
    for i in range(len(out)-2,-1,-1):out[i]=(R[i+1]+a*out[i+1])%p
    assert (R[0]+a*out[0])%p==0
    return trim(out)


def degree_at_most_on_support(xs,ys,D,p):
    coefficients=ys[:]
    for j in range(1,len(xs)):
        for i in range(len(xs)-1,j-1,-1):
            coefficients[i]=(coefficients[i]-coefficients[i-1])*pow(xs[i]-xs[i-j],-1,p)%p
    return all(c==0 for c in coefficients[D+1:])


def prime(p):
    return p>=2 and all(p%d for d in range(2,isqrt(p)+1))


def splitting_prime(B,m,minimum):
    p=minimum+1
    p+= (1-p)%B
    while True:
        if prime(p) and all(pow(a,(p-1)//B,p)==1 for a in range(1,m+1)):return p
        p+=B


def compose_power(P,B):
    out=[0]*((len(P)-1)*B+1)
    for i,c in enumerate(P):out[i*B]=c
    return out


def fixture(B,tight_dimension=False):
    m,k,t,r=9,3,5,2 if tight_dimension else 1
    code_k=k-1 if tight_dimension else k
    subsets=[(1,2,5,7,8),(1,3,4,6,9)]
    L=len(subsets);n=B*(m+r);K=B*code_k;A=B*t;added=B*r+1
    lower=max(m*B+(K-1)*comb(L,2)+added,(added-1)*L*L,1000)
    p=splitting_prime(B,m,lower)
    roots=defaultdict(list)
    for x in range(p):
        a=pow(x,B,p)
        if 1<=a<=m:roots[a].append(x)
    assert all(len(roots[a])==B for a in range(1,m+1))
    old=sorted(x for group in roots.values() for x in group if x!=1)
    assert len(old)==m*B-1
    locators=[locator(S,p) for S in subsets]
    assert locators[0][k:]==locators[1][k:]
    W=[0]*k+locators[0][k:];G=[subtract(W,F,p) for F in locators]
    W1=value(W,1,p)
    assert all(value(P,1,p)==W1 for P in G)
    numerator=compose_power(W,B);numerator[0]=(numerator[0]-W1)%p
    F_old=root_quotient(numerator,1,p)
    family=[]
    for P in G:
        numerator=compose_power(P,B);numerator[0]=(numerator[0]-W1)%p
        family.append(root_quotient(numerator,1,p))
    assert len(F_old)-1==A-1 and all(len(P)-1<K for P in family)
    old_values=[value(F_old,x,p) for x in old]
    for P in family:
        assert sum(value(P,x,p)==y for x,y in zip(old,old_values))==A-1
    excluded=set(old)|{1};points=[]
    for x in range(p):
        if x not in excluded and len({value(P,x,p) for P in family})==L:
            points.append(x)
            if len(points)==added:break
    assert len(points)==added
    labels=set();offsets=[];witnesses=[]
    for x in points:
        values=[value(P,x,p) for P in family]
        b=next(b for b in range(p) if not ({(v-b)%p for v in values}&labels))
        offsets.append(b)
        for i,v in enumerate(values):
            z=(v-b)%p
            assert z not in labels;labels.add(z);witnesses.append((z,i))
    domain=old+points;f=old_values+offsets;g=[0]*len(old)+[1]*added
    assert len(domain)==n and len(set(domain))==n
    # The global common-agreement bound includes every pair of codewords.
    common_bound=max(A-1,K-1+added)
    assert common_bound<A
    for z,i in witnesses:
        P=family[i]
        support=[j for j,x in enumerate(domain) if value(P,x,p)==(f[j]+z*g[j])%p]
        assert len(support)==A
        assert not degree_at_most_on_support([domain[j] for j in support],[g[j] for j in support],K-1,p)
    assert len(labels)==L*added
    # Directly scan all challenges for the two exhibited candidates.
    direct=set()
    for z in range(p):
        if any(sum(value(P,x,p)==(y+z*h)%p for x,y,h in zip(domain,f,g))>=A for P in family):direct.add(z)
    assert direct==labels
    return dict(B=B,tight_dimension=tight_dimension,p=p,n=n,k=K,A=A,seed_list_size=L,
                added_points=added,nearby_challenges=len(labels),
                global_joint_agreement_upper=common_bound,
                exact_rate=[K,n],exact_gap=[A-K,n],
                labels=sorted(labels),domain=domain,f=f,g=g,
                candidate_coefficients=family,old_word_coefficients=F_old)


def anchor_count_checks():
    checked=0
    for m in range(5,12):
        for t in range(3,m):
            for s in range(1,min(3,t)):
                classes=defaultdict(int)
                for rest in combinations(range(2,m+1),t-1):
                    S=(1,)+rest
                    key=tuple(sum(comb(a-1,j) for a in S) for j in range(1,s+1))
                    classes[key]+=1
                ranges=[comb(m,j+1)-comb(m-t,j+1)-comb(t,j+1)+1 for j in range(1,s+1)]
                denominator=1
                for x in ranges:denominator*=x
                lower=(comb(m-1,t-1)+denominator-1)//denominator
                assert max(classes.values())>=lower
                checked+=1
    return checked


def concrete_coefficient_checks():
    rows=[]
    for m,k,t,L0,r in [(64,32,34,5552914238035,2),
                       (157,63,68,28169451256663519418,5)]:
        anchored=(t*L0+m-1)//m
        coefficient=Fraction(r*anchored,m+r)
        assert 1<=r<=t-k and (anchored-1)*m<t*L0<=anchored*m
        rows.append(dict(m=m,k=k,t=t,r=r,source_class_lower_bound=L0,
                         anchored_class_lower_bound=anchored,
                         coefficient_numerator=coefficient.numerator,
                         coefficient_denominator=coefficient.denominator,
                         code_seed_dimension=k-1,final_rate=[k-1,m+r],final_gap=[t-k+1,m+r]))
    assert rows[0]['anchored_class_lower_bound']==2949985688957
    assert rows[1]['anchored_class_lower_bound']==12200781436007129430
    assert Fraction(rows[1]['coefficient_numerator'],rows[1]['coefficient_denominator'])>376000000000000000
    # Integer affine transformation with an arbitrary anchor, including
    # negative transformed domain points, preserves monicity and avoids 0.
    affine_checks=0
    for m in range(3,9):
        for S in combinations(range(m),3):
            # Integer locator coefficients, without modular reduction.
            F=[1]
            for a in S:
                nxt=[0]*(len(F)+1)
                for i,c in enumerate(F):nxt[i]-=a*c;nxt[i+1]+=c
                F=nxt
            t=len(S)
            for anchor in S:
                points=[2*(a-anchor)+1 for a in range(m)]
                assert 1 in points and 0 not in points
                transformed=[sum(F[h]*comb(h,j)*(2*anchor-1)**(h-j)*2**(t-h)
                                 for h in range(j,t+1)) for j in range(t+1)]
                assert transformed[-1]==1
                for a in S:
                    x=2*(a-anchor)+1
                    assert sum(c*x**j for j,c in enumerate(transformed))==0
                affine_checks+=1
    return rows,affine_checks


def main():
    started=time.monotonic()
    fixtures=[fixture(B) for B in (1,2,4)]
    # Same exact rate and positive gap across fiber sizes.
    assert all(10*r['k']==3*r['n'] and 5*(r['A']-r['k'])==r['n'] for r in fixtures)
    tight_fixtures=[fixture(B,True) for B in (1,2,4)]
    assert all(11*r['k']==2*r['n'] and 11*(r['A']-r['k'])==3*r['n'] for r in tight_fixtures)
    fixtures+=tight_fixtures
    concrete,affine_checks=concrete_coefficient_checks()
    result=dict(status='passed',fixtures=fixtures,anchored_pigeonhole_checks=anchor_count_checks(),
                concrete_coefficients=concrete,integer_affine_checks=affine_checks,
                seconds=time.monotonic()-started,
                scope='Exact integer/finite-field checks of the anchored quotient and padding construction. Splitting-prime infinitude and the asymptotic moment estimate are supplied by the written proof.')
    Path(__file__).with_name('anchored_padding_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({**result,'fixtures':[{k:v for k,v in row.items() if k in {'B','p','n','k','A','nearby_challenges','global_joint_agreement_upper'}} for row in fixtures]},indent=2))


if __name__=='__main__':main()
