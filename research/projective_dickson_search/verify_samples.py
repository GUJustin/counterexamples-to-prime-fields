"""Independent Vandermonde replay, followed by exact domain-symmetry closure."""
from pathlib import Path
from collections import Counter
import json


def interpolate(xs,ys,p):
    n=len(xs)
    rows=[[pow(x,j,p) for j in range(n)]+[y] for x,y in zip(xs,ys)]
    for j in range(n):
        t=next(t for t in range(j,n) if rows[t][j])
        rows[j],rows[t]=rows[t],rows[j]
        z=pow(rows[j][j],-1,p)
        rows[j]=[v*z%p for v in rows[j]]
        for t in range(n):
            if t!=j:
                z=rows[t][j]
                rows[t]=[(v-z*w)%p for v,w in zip(rows[t],rows[j])]
    return tuple(row[-1] for row in rows)


def evaluate(c,x,p):
    out=0
    for v in reversed(c):out=(out*x+v)%p
    return out


def main():
    folder=Path(__file__).resolve().parent
    source=json.loads((folder/'sampled_lists.json').read_text())
    p=source['p'];n=p-1;k=n//4;A=3*n//8
    xs=list(range(1,p))
    word={x:((1+(1 if pow(x,n//2,p)==1 else -1))//2-pow(x,k,p))%p for x in xs}
    H=[h for h in xs if pow(h,k,p)==1]
    assert len(H)==k
    assert all(word[h*x%p]==word[x] for h in H for x in xs)
    original=set();closure=set()
    for item in source['candidates']:
        S=item['determining_coordinates']
        c=interpolate(S,[word[x] for x in S],p)
        agreements=sum(evaluate(c,x,p)==word[x] for x in xs)
        assert agreements==item['agreements']>=A
        original.add(c)
        for h in H:
            closure.add(tuple(v*pow(h,j,p)%p for j,v in enumerate(c)))
    assert len(original)==source['distinct_candidates']
    remaining=set(closure);orbits=[]
    while remaining:
        c=min(remaining)
        orbit={tuple(v*pow(h,j,p)%p for j,v in enumerate(c)) for h in H}
        assert orbit<=remaining
        remaining-=orbit
        support=[x for x in xs if evaluate(c,x,p)==word[x]]
        assert len(support)>=A
        orbits.append(dict(representative=list(c),size=len(orbit),agreements=len(support),support=support))
    degrees=Counter(max(j for j,v in enumerate(c) if v) for c in closure)
    result=dict(status='passed',p=p,n=n,k=k,A=A,
                independently_verified_sampled_candidates=len(original),
                symmetry_closed_list=len(closure),degrees=dict(degrees),orbits=orbits,
                scope='Certified finite lower bound, closed under the exact multiplicative symmetry of the word. No completeness or growing-family claim.')
    (folder/'sample_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
