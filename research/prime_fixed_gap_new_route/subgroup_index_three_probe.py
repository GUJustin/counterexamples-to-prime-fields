"""Bounded p<=500 native Dickson restriction survey; exact finite fields."""
from collections import Counter
from math import comb, isqrt
from pathlib import Path
import json

def prime(p):
    return p >= 2 and all(p % d for d in range(2, isqrt(p)+1))

def evaluate(cs, x, p):
    v = 0
    for c in reversed(cs):
        v = (v*x+c) % p
    return v

rows = []
total = 0
for p in range(5, 501, 4):
    if not prime(p):
        continue
    k = (p-1)//4
    native = [comb(2*k+1, 2*j+1) % p for j in range(k)]
    squares = sorted({a*a % p for a in range(1, p)})
    for n in range(4, p, 4):
        if (p-1) % n or ((p-1)//n) % 4 != 3:
            continue
        xs = [x for x in range(1, p) if pow(x, n, p) == 1]
        assert len(xs) == n
        q = n//4
        word = [((1+pow(x, 2*k, p))*pow(2, -1, p)-pow(x, k, p)) % p
                for x in xs]
        hist = Counter()
        low = []
        minimum = n
        min_examples = []
        for t in squares:
            coeffs = [0]*n
            tj = pow(t, k, p)
            inv = pow(t, -1, p)
            for j, c in enumerate(native):
                coeffs[j % n] = (coeffs[j % n]+c*tj) % p
                tj = tj*inv % p
            degree = max((j for j, c in enumerate(coeffs) if c), default=-1)
            hist[degree] += 1
            total += 1
            if degree < minimum:
                minimum = degree
                min_examples = []
            if degree == minimum and len(min_examples) < 4:
                min_examples.append(t)
            if degree < q:
                agreement = sum(evaluate(coeffs, x, p) == w for x, w in zip(xs, word))
                low.append(dict(t=t, degree=degree, agreement=agreement,
                                coefficients=coeffs[:degree+1]))
        rows.append(dict(p=p,n=n,index=(p-1)//n,k=k,
                         target_dimension=q,parameter_count=len(squares),
                         minimum_degree=minimum,minimum_parameter_examples=min_examples,
                         degree_histogram=dict(sorted(hist.items())),
                         quarter_rate_candidates=low,
                         zero_candidate_agreement=sum(w == 0 for w in word)))
out = dict(scope='All primes p<=500, n divisible by4, subgroup index3mod4; nonzero square parameters. No nearestness or general nonexistence claim.',
           cases=len(rows), parameter_cases=total,
           quarter_rate_candidates=sum(len(r['quarter_rate_candidates']) for r in rows),
           rows=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
