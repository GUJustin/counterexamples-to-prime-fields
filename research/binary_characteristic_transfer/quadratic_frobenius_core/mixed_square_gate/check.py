"""Exhaustive quadratic histograms on an Fp-plane, for three mixed words."""
import itertools
import json
from collections import Counter
from pathlib import Path

rows = []
for p in (3, 5):
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

    W = [index[(a, b, 0)] for a in range(p) for b in range(p)]
    xp = [power(x, p) for x in W]
    xx = [M[x][x] for x in W]
    squares = {M[x][x] for x in range(q)}
    t = index[(0, 1, 0)]
    nonsquare = next(a for a in range(1, p) if pow(a, (p-1)//2, p) == p-1)
    d = index[(nonsquare, 0, 0)]
    # Force a rational anisotropic homogeneous conic, exercising the even branch.
    special_s = M[sub[power(t, p+1)][d]][power(sub[M[t][t]][d], q-2)]
    for s in (zero, one, t, special_s):
        linear = [sub[y][M[s][x]] for x, y in zip(W, xp)]
        word = [M[y][y] for y in linear]
        rich = Counter()
        even_slopes = set()
        maximum = 0
        for a in range(q):
            axx = [M[a][y] for y in xx]
            for c in range(q):
                counts = Counter(sub[sub[f][ax2]][M[c][x]]
                                 for x, f, ax2 in zip(W, word, axx))
                for b, count in counts.items():
                    maximum = max(maximum, count)
                    if count <= 4:
                        continue
                    discriminant = sub[M[c][c]][M[four][M[a][b]]]
                    square = ((a != zero and discriminant == zero and a in squares)
                              or (a == zero and c == zero and b in squares))
                    kind = 'square' if square else 'even_nonsquare' if c == zero else 'non_even_nonsquare'
                    rich[kind] += 1
                    if kind == 'even_nonsquare':
                        even_slopes.add(a)
        assert rich['non_even_nonsquare'] == 0
        assert rich['square'] <= p*(p+1)
        assert rich['even_nonsquare'] <= p and len(even_slopes) <= 1
        assert sum(rich.values()) <= p*p+2*p
        rows.append(dict(p=p, cubic=[bb, aa, 0, 1], s=elements[s],
                         all_quadratics_covered=q**3, rich_threshold='strictly more than four',
                         rich_counts=dict(rich), maximum_agreement=maximum, passed=True))
Path(__file__).with_suffix('.json').write_text(json.dumps(rows, indent=2)+'\n')
print(json.dumps(rows, indent=2))
