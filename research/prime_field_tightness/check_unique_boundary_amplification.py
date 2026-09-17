"""Exhaustive line replay for arbitrary-boundary, unrestricted-padding transfer."""
from collections import Counter
from fractions import Fraction
from itertools import combinations,product
from math import comb,isqrt
from pathlib import Path
import json,random,time
BASE=Path(__file__).resolve().parent


def prime(p):return p>=2 and all(p%d for d in range(2,isqrt(p)+1))

def line_through(x,y,xx,yy,p):
    slope=(yy-y)*pow(xx-x,-1,p)%p
    return ((y-slope*x)%p,slope)

def val(c,x,p):return (c[0]+c[1]*x)%p

def source_pool(domain,word,p):
    polys={line_through(domain[i],word[i],domain[j],word[j],p) for i,j in combinations(range(len(domain)),2)}
    counts={c:sum(val(c,x,p)==v for x,v in zip(domain,word)) for c in polys}
    M=max(counts.values())
    nearest=[c for c,a in counts.items() if a==M]
    T=3
    pool=[c for c,a in counts.items() if a>=T]
    return M,nearest,pool,T

def full_replay(domain,f,g,p,A):
    """For EVERY label, interpolate EVERY determining pair; no bank restriction."""
    pairs=[(i,j,pow(domain[j]-domain[i],-1,p)) for i,j in combinations(range(len(domain)),2)]
    maxima=[];near={}
    for z in range(p):
        word=[(a+z*b)%p for a,b in zip(f,g)]
        candidates=set()
        for i,j,inv in pairs:
            slope=(word[j]-word[i])*inv%p
            candidates.add(((word[i]-slope*domain[i])%p,slope))
        best=0;close=[]
        for c in candidates:
            a=sum(val(c,x,p)==v for x,v in zip(domain,word))
            best=max(best,a)
            if a>=A:close.append(c)
        maxima.append(best)
        if close:near[z]=sorted(close)
    return maxima,near


def fixture(p,old,changed,seed):
    start=time.monotonic();assert prime(p)
    old=[x%p for x in old];N=len(old);k=2;q=N
    w=[pow(x,3,p) for x in old]
    if changed is not None:w[old.index(changed[0]%p)]=changed[1]%p
    M,nearest,pool,T=source_pool(old,w,p)
    assert M>=k+1 and k+1<=T<=M
    L,U=len(nearest),len(pool);A=M+1;n=2*N
    assert p>=N+q+(k-1)*comb(U,2)
    failure=Fraction(q*U+comb(q,2)*U*U,p)+Fraction(comb(n,A),p**(A-T))
    assert failure<1
    added=[]
    for x in range(p):
        if x not in old and len({val(c,x,p) for c in pool})==U:
            added.append(x)
            if len(added)==q:break
    assert len(added)==q
    domain=old+added;g=[0]*N+[1]*q;rng=random.Random(seed)
    attempts=0
    while attempts<100:
        attempts+=1
        offsets=[rng.randrange(p) for _ in added]
        all_labels=[(val(c,x,p)-b)%p for c in pool for x,b in zip(added,offsets)]
        if 0 in all_labels or len(set(all_labels))!=q*U:continue
        f=w+offsets
        maxima,near=full_replay(domain,f,g,p,A)
        predicted={(val(c,x,p)-b)%p:c for c in nearest for x,b in zip(added,offsets)}
        if set(near)!=set(predicted) or any(near[z]!=[predicted[z]] for z in predicted):continue
        assert maxima[0]==M
        assert all(maxima[z]==(A if z in predicted else M) for z in range(p))
        break
    else:raise AssertionError('Failed to find a fixture')
    # Independent Newton divided differences record degree of the arbitrary old word.
    dd=w[:];coeff=[dd[0]]
    for order in range(1,N):
        dd=[(dd[i+1]-dd[i])*pow(old[i+order]-old[i],-1,p)%p for i in range(N-order)]
        coeff.append(dd[0])
    degree=max(i for i,c in enumerate(coeff) if c)
    if changed is not None:assert degree>M
    return dict(p=p,N=N,n=n,k=k,M=M,A=A,T=T,L=L,U=U,q=q,
                failure_bound=str(failure),source_word_degree=degree,domain=domain,
                f=f,g=g,nearest_source_polynomials=nearest,pool=pool,
                nearby={str(z):cs for z,cs in sorted(near.items())},
                maximum_agreement_histogram=dict(Counter(maxima)),
                unique_nearby_count=len(near),far_at_zero=True,
                source_rate=str(Fraction(k,N)),target_rate=str(Fraction(k,n)),
                source_gap=str(Fraction(M-k,N)),target_gap=str(Fraction(A-k,n)),
                all_labels_replayed=p,determining_pairs_per_label=comb(n,k),
                attempts=attempts,seconds=time.monotonic()-start)


def main():
    rows=[fixture(263,[-2,-1,0,1,2],None,41),fixture(2003,[-3,-2,-1,0,1,2,3],(3,99),43)]
    p=7;domain=list(range(6));g=[0,0,0,1,1,1];good=0;bad_outside=0
    for offsets in product(range(p),repeat=3):
        maxima,near=full_replay(domain,[0,0,0]+list(offsets),g,p,4)
        predicted={(-b)%p for b in offsets}
        outside=any(c!=(0,0) for cs in near.values() for c in cs)
        bad_outside+=outside
        if len(predicted)==3 and 0 not in predicted and not outside:
            assert set(near)==predicted
            assert all(near[z]==[(0,0)] for z in near)
            assert all(maxima[z]==(4 if z in near else 3) for z in range(p))
            good+=1
    assert good==96 and bad_outside==42
    small=dict(p=p,all_offset_tuples=p**3,good_two_distance_profiles=good,
               offsets_with_outside_pool_nearby_candidates=bad_outside,
               all_labels_per_offset=p,scope='Exhaustive mechanism check; this small field does not satisfy the sufficient union-bound hypothesis.')
    out=dict(status='passed',fixtures=rows,exhaustive_offsets=small,scope='All scalar labels and all determining pairs replayed, giving complete maximum-agreement and nearby-list profiles. One source word has interpolation degree greater than its maximum agreement. Finite checks supplement the proof.')
    (BASE/'unique_boundary_amplification_verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(status='passed',fixtures=[{key:r[key] for key in ('p','N','n','M','A','L','U','failure_bound','source_word_degree','unique_nearby_count','maximum_agreement_histogram','attempts','seconds')} for r in rows],exhaustive_offsets=small),indent=2))

if __name__=='__main__':main()
