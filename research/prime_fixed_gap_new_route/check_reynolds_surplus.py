"""Bounded exact survey; finite evidence, not an asymptotic obstruction."""
from pathlib import Path
from collections import Counter
import json


def prime(n):
    return n >= 2 and all(n % d for d in range(2, int(n**0.5) + 1))


def generator(p):
    q, factors, d = p - 1, [], 2
    while d * d <= q:
        if q % d == 0:
            factors.append(d)
            while q % d == 0:
                q //= d
        d += 1
    if q > 1:
        factors.append(q)
    return next(g for g in range(2, p) if all(pow(g, (p - 1)//q, p) != 1 for q in factors))


rows = []
for r in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47):
    for d in range(2, 101):
        p = 4*d*r + 1
        if not prime(p):
            continue
        e = 2*d*r + 1
        fact = [1]*(e+1)
        for j in range(1, e+1):
            fact[j] = fact[j-1]*j % p
        invfact = [1]*(e+1)
        invfact[e] = pow(fact[e], p-2, p)
        for j in range(e, 0, -1):
            invfact[j-1] = invfact[j]*j % p
        coeff = [fact[e]*invfact[2*d*h+1]*invfact[e-2*d*h-1] % p for h in range(r)]
        root = pow(generator(p), d, p)
        assert pow(root, 4*r, p) == 1 and pow(root, 2*r, p) != 1 and pow(root, 4, p) != 1
        inverse_two = (p+1)//2
        matches = []
        coset_values = [Counter() for _ in range(4)]
        y = 1
        for t in range(4*r):
            value = 0
            for c in reversed(coeff):
                value = (value*y+c) % p
            target = ((1+pow(y, 2*r, p))*inverse_two-pow(y, r, p)) % p
            coset_values[t % 4][value] += 1
            if value == target:
                matches.append(t)
            y = y*root % p
        modal_counts = [max(c.values()) for c in coset_values]
        modal_values = [[v for v,m in c.items() if m == peak] for c,peak in zip(coset_values,modal_counts)]
        def distinct_representatives(options, used=frozenset()):
            return not options or any(v not in used and distinct_representatives(options[1:], used | {v}) for v in options[0])
        rows.append(dict(r=r, d=d, p=p, agreement=len(matches), surplus=len(matches)-r,
                         optimal_bank_agreement=sum(modal_counts), modal_counts=modal_counts,
                         distinct_modal_values_possible=distinct_representatives(modal_values),
                         matching_exponents=matches))
out = dict(scope="prime r <=47 in displayed list; 2<=d<=100; prime p=4dr+1",
           cases=len(rows), positive_surplus_cases=sum(t['surplus'] > 0 for t in rows),
           maximum_surplus=max(t['surplus'] for t in rows),
           modal_surplus_cases=sum(t['optimal_bank_agreement'] > t['r'] for t in rows),
           modal_surplus_maximum_r=max((t['r'] for t in rows if t['optimal_bank_agreement']>t['r']),default=None), rows=rows)
Path(__file__).with_name('reynolds_surplus_checks.json').write_text(json.dumps(out, indent=2)+'\n')
print({k:v for k,v in out.items() if k != 'rows'})
print('Best normalized surplus:', sorted(rows, key=lambda t:t['surplus']/t['r'], reverse=True)[:8])
