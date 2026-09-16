"""Exact checks of the domain-stabilizer and deck-subgroup arguments."""
from collections import Counter
from pathlib import Path
import json


def primes(limit):
    return [p for p in range(5,limit+1)
            if all(p%d for d in range(2,int(p**.5)+1))]


def order(g,p):
    value=1
    for n in range(1,p):
        value=value*g%p
        if value==1:
            return n


def matrices(p):
    # Unique projective representative whose first nonzero entry is 1.
    for b in range(p):
        for c in range(p):
            for d in range(p):
                if (d-b*c)%p:
                    yield 1,b,c,d
    for c in range(1,p):
        for d in range(p):
            yield 0,1,c,d


counts=dict(mobius_domain_checks=0,stabilizer_maps=0,
            reflection_subgroups=0,free_reflection_subgroups=0)
for p in primes(31):
    g=next(x for x in range(2,p) if order(x,p)==p-1)
    for n in range(3,p):
        if (p-1)%n:
            continue
        h=pow(g,(p-1)//n,p)
        D={pow(h,i,p) for i in range(n)}
        found=0
        for a,b,c,d in matrices(p):
            preserves=True
            for x in D:
                denominator=(c*x+d)%p
                if not denominator or (a*x+b)*pow(denominator,-1,p)%p not in D:
                    preserves=False
                    break
            expected=(b==c==0 and a*pow(d,-1,p)%p in D) or (
                a==d==0 and b*pow(c,-1,p)%p in D)
            assert preserves==expected
            found+=preserves
            counts['mobius_domain_checks']+=1
        assert found==2*n
        counts['stabilizer_maps']+=found
        for d in range(1,n+1):
            if n%d:
                continue
            N=n//d
            rotation=[pow(h,N*j,p) for j in range(d)]
            image={pow(x,d,p) for x in D}
            for j in range(N):
                alpha=pow(h,j,p)
                c=pow(alpha,d,p)
                nonsquare=all(u*u%p!=c for u in image)
                free=True
                for x in D:
                    orbit={z*x%p for z in rotation}
                    orbit.update(alpha*z*pow(x,-1,p)%p for z in rotation)
                    if len(orbit)!=2*d:
                        free=False
                assert free==nonsquare==(N%2==0 and j%2==1)
                labels=Counter((pow(x,d,p)+c*pow(pow(x,d,p),-1,p))%p for x in D)
                full=(n%(2*d)==0 and len(labels)==n//(2*d)
                      and set(labels.values())=={2*d})
                assert full==free
                counts['reflection_subgroups']+=1
                counts['free_reflection_subgroups']+=free

result=dict(status='all exact assertions passed',counts=counts,
            scope='PGL_2(F_p) stabilizers for primes5..31; subgroup freeness')
Path(__file__).with_name('galois_fiber_verification.json').write_text(
    json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
