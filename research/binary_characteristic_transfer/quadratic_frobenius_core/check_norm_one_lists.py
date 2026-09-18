"""Exhaustive quadratic agreement census for the cubic norm-one word."""
import itertools
import json
from collections import Counter
from pathlib import Path

rows = []
for p in (3, 5, 7):
    q = p**3
    bb, aa = next((b, a) for b in range(1, p) for a in range(p)
                  if all((x**3+a*x+b) % p for x in range(p)))
    elements = list(itertools.product(range(p), repeat=3))
    index = {v: i for i, v in enumerate(elements)}
    zero, one, four = index[(0, 0, 0)], index[(1, 0, 0)], index[(4 % p, 0, 0)]

    def multiply(x, y):
        h = [0]*5
        for i in range(3):
            for j in range(3):
                h[i+j] += elements[x][i]*elements[y][j]
        for i in (4, 3):
            h[i-3] -= bb*h[i]
            h[i-2] -= aa*h[i]
        return index[tuple(v % p for v in h[:3])]

    M = [[multiply(x, y) for y in range(q)] for x in range(q)]
    sub = [[index[tuple((a-b) % p for a, b in zip(x, y))]
            for y in elements] for x in elements]

    def power(x, n):
        r = one
        while n:
            if n & 1:
                r = M[r][x]
            x = M[x][x]
            n //= 2
        return r

    domain = [x for x in range(q) if x != zero and power(x, 2*(p*p+p+1)) == one]
    assert len(domain) == 2*(p*p+p+1)
    xx = [M[x][x] for x in domain]
    word = [power(x, 2*p+2) for x in domain]
    histogram = Counter()
    maximum_outside_bank = 0
    bank_count = 0
    minus_one = sub[zero][one]
    for a in range(q):
        axx = [M[a][y] for y in xx]
        for b in range(q):
            counts = Counter(sub[sub[f][ax2]][M[b][x]]
                             for x, f, ax2 in zip(domain, word, axx))
            histogram[0] += q-len(counts)
            for c, count in counts.items():
                histogram[count] += 1
                is_bank = (b == zero and power(a, p*p+p+1) == minus_one
                           and c == sub[zero][power(a, p*p+1)])
                if is_bank:
                    assert count == 2*p+2
                    bank_count += 1
                else:
                    maximum_outside_bank = max(maximum_outside_bank, count)
                    assert count <= p+3
    assert bank_count == p*p+p+1
    assert sum(histogram.values()) == q**3
    rows.append(dict(p=p, cubic=[bb, aa, 0, 1], domain_size=len(domain),
                     all_quadratics_covered=q**3, bank_size=bank_count,
                     maximum_outside_bank=maximum_outside_bank,
                     agreement_histogram=dict(sorted(histogram.items())), passed=True))
Path(__file__).with_suffix('.json').write_text(json.dumps(rows, indent=2)+'\n')
print(json.dumps(rows, indent=2))
