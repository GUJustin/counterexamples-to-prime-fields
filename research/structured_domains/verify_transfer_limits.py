"""Small-field checks of coding-theory transfer lemmas; standard library only."""
from itertools import combinations
from math import comb
import json
from pathlib import Path


def primes(limit):
    return [p for p in range(5, limit + 1)
            if all(p % d for d in range(2, int(p ** .5) + 1))]


def order(g, p):
    z = 1
    for n in range(1, p):
        z = z * g % p
        if z == 1:
            return n


def mul(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] = (out[i+j] + x*y) % p
    return out


def roots_poly(roots, p):
    out = [1]
    for a in roots:
        out = mul(out, [-a % p, 1], p)
    return out


def evaluate(poly, x, p):
    out = 0
    for a in reversed(poly):
        out = (out*x + a) % p
    return out


counts = dict(affine_cosets=0, prouhet=0, interpolation=0,
              fiber_maps=0, transferred_words=0)
for p in primes(101):
    primitive = next(g for g in range(2, p) if order(g, p) == p-1)
    for n in range(2, p):
        if (p-1) % n:
            continue
        g = pow(primitive, (p-1)//n, p)
        H = sorted(pow(g, i, p) for i in range(n))
        if 3 <= n < p-1:
            for c in range(1, p):
                coset = {c*x % p for x in H}
                assert sum(coset) % p == sum(x*x for x in coset) % p == 0
                # Sum zero forces the center; test every remaining scale.
                for b in range(1, p):
                    a = -b*(n-1)*pow(2, -1, p) % p
                    assert {(a+b*i) % p for i in range(n)} != coset
                counts['affine_cosets'] += 1
        for m in range(1, 5):
            if 2**(m+1) > n:
                continue
            A = [i for i in range(2**(m+1)) if i.bit_count() % 2 == 0]
            B = [i for i in range(2**(m+1)) if i.bit_count() % 2 == 1]
            for j in range(m+1):
                assert sum(i**j for i in A) == sum(i**j for i in B)
            diff = (sum(pow(g,i,p) for i in A)-sum(pow(g,i,p) for i in B)) % p
            prod = 1
            for r in range(m+1):
                prod = prod*(1-pow(g,2**r,p)) % p
            assert diff == prod != 0
            counts['prouhet'] += 1
        for i in range(n):
            assert sum(pow(g-1,j,p)*comb(i,j) for j in range(i+1)) % p == pow(g,i,p)
        factorial = 1
        for j in range(1,n):
            factorial = factorial*j % p
        assert pow(g-1,n-1,p)*pow(factorial,-1,p) % p != 0
        counts['interpolation'] += 1
        for d in range(1,n+1):
            if n % d:
                continue
            image = sorted({pow(x,d,p) for x in H})
            assert len(image) == n//d
            assert all(sum(pow(x,d,p)==y for x in H)==d for y in image)
            counts['fiber_maps'] += 1
            # Exact scalar list signatures on small quotient domains.
            N = len(image)
            if not 3 <= N <= 7:
                continue
            t, k = N-1, N-2
            classes = {}
            for A in combinations(image,t):
                F = roots_poly(A,p)
                classes.setdefault(tuple(F[k:]), []).append((A,F))
            for signature, members in classes.items():
                W = [0]*k+list(signature)
                lifted_words = set()
                for A,F in members:
                    P = [(W[j]-F[j]) % p for j in range(k)]
                    lifted = [0]*(d*(k-1)+1)
                    for j,a in enumerate(P):
                        lifted[d*j] = a
                    assert len(lifted)-1 < d*k
                    assert sum(evaluate(W,pow(x,d,p),p)==evaluate(lifted,x,p)
                               for x in H) == d*t
                    lifted_words.add(tuple(evaluate(lifted,x,p) for x in H))
                    counts['transferred_words'] += 1
                assert len(lifted_words)==len(members)

result = {'status': 'all exact assertions passed', 'counts': counts,
          'scope': 'coding theory on primes at most 101; no protocol experiments'}
Path(__file__).with_name('verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
