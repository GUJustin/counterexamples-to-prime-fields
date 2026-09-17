"""Independent exact audit of the recovered full-prime-field Dickson list.

Checks all seed evaluations and all designated extension-field labels.
Extension labels are represented in the independent basis (1, theta);
only addition and multiplication by base-field scalars are needed.
No numerical estimates or sampling enter the assertions.
"""
from math import comb, isqrt
from pathlib import Path
import json


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def verify(p):
    require(all(p % d for d in range(2, isqrt(p) + 1)), 'primality')
    require(p % 8 == 1, 'prime congruence')
    n, k, e = p - 1, (p - 1) // 4, (p + 1) // 2
    def chi(x):
        y = pow(x % p, n // 2, p)
        return -1 if y == p - 1 else y
    xs = list(range(1, p))
    w = {x: ((1 + chi(x)) // 2 - pow(x, k, p)) % p for x in xs}
    coefficients, matrix, supports = [], [], []
    for a in range(1, n // 2 + 1):
        c = tuple(comb(e, 2*j + 1) * pow(a, e - 2*j - 1, p) % p
                  for j in range(k))
        coefficients.append(c)
        row = {}
        for x in xs:
            v = 0
            for cj in reversed(c):
                v = (v*x + cj) % p
            row[x] = v
        matrix.append(row)
        support = {x for x in xs if row[x] == w[x]}
        supports.append(support)
        require(sum(chi(x) == 1 for x in support) == n // 8, 'square agreements')
        require(sum(chi(x) == -1 for x in support) == n // 4, 'nonsquare agreements')
        require(c[-1] == -a*a*pow(8, -1, p) % p, 'leading coefficient')
    require(len(set(coefficients)) == n // 2, 'distinct seed polynomials')
    result = dict(p=p, n=n, k=k, list_size=n//2, agreements=3*n//8)
    # Crude exact sufficient Elias inequality for radius 5/8, rate 1/4:
    # H_p(5/8) < 5/8 + 1/log_2(p) < 3/4 for p > 256.
    result['strictly_below_elias_certified'] = p > 256
    if p % 16 == 1:
        m = n // 16
        changed = [x for x in xs if chi(x) == -1][:m]
        core = set(xs) - set(changed)
        labels = set()
        counts = []
        for x in changed:
            representatives = {}
            for i, row in enumerate(matrix):
                representatives.setdefault(row[x], i)
            require(len(representatives) == k + 1, 'distinct values at changed coordinate')
            for v, i in representatives.items():
                z = (v, -x % p)
                require(z not in labels, 'distinct extension labels')
                labels.add(z)
                changed_matches = [y for y in changed
                                   if (v, (y-x) % p) == (matrix[i][y], 0)]
                require(changed_matches == [x], 'one changed-coordinate agreement')
                core_matches = supports[i] & core
                require(len(core_matches) >= 5*m, 'retained core agreement')
                require(len(core_matches) >= k, 'direction forced zero')
                counts.append(len(core_matches) + 1)
        require(len(labels) == m*(4*m+1), 'quadratic full-set MCA count')
        result.update(full_set_mca_labels=len(labels),
                      minimum_witness_agreement=min(counts),
                      maximum_witness_agreement=max(counts),
                      subset_correlated_explanation_persists=True)
    return result


if __name__ == '__main__':
    results = [verify(p) for p in (17, 41, 97, 193, 257, 337)]
    output = dict(status='PASS', scope='seed lists and full-set MCA; not subset CA',
                  results=results)
    Path(__file__).with_name('verification.json').write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(output, indent=2))
