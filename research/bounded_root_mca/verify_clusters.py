#!/usr/bin/env python3
"""Full-support cluster fixtures and the bounded-root theorem's thresholds."""
import json
import sys
from fractions import Fraction
from itertools import combinations
from math import ceil, comb
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'power_family_mca'))
from poly import degree_at_most_on_support


def pencil_fixture():
    p, D, n, A, r = 65537, 1024, 4096, 3072, 2
    a = Fraction(A, n)
    delta = a**3/(128*r)
    w = int(delta*D)+1
    lower = ((D-1)//w)*w
    K = D-lower
    assert K+1 <= a**3*n/16
    assert 1 <= r*delta*D
    assert 1 < delta*D <= D-1
    H = [pow(x, D-1, p) for x in range(n)]
    G = [h*x % p for x, h in enumerate(H)]
    f = [2*h % p for h in H]
    g = G[:]
    for j, i in enumerate(range(A-1, n)):
        f[i] = H[i]*(2-j) % p
        g[i] = H[i]*(i+1) % p
    assert sum(h!=0 for h in H[:A-1])>D
    checks = 0
    for z in range(n-A+1):
        support = [x for x in range(n)
                   if (f[x]+z*g[x]-H[x]*(2+z*x)) % p == 0]
        assert support == list(range(A-1))+[A-1+z]
        assert len(support)==A
        assert all(g[x]==G[x] for x in range(A-1))
        assert g[A-1+z]!=G[A-1+z]
        # >D core coordinates force any degree-D interpolant to g to be G;
        # its disagreement at the extra coordinate proves full-support badness.
        checks += 1
    assert checks==n-A+1 and checks<=n
    return {'p': p, 'D': D, 'n': n, 'A': A, 'bad_labels': checks,
            'root_count_bound': r, 'delta': str(delta), 'box_width': w,
            'common_factor_degree': lower, 'residual_degree_cap': K,
            'candidate_degrees': [D-1, D],
            'scope': 'All labels and full supports checked; interpolation impossibility certified by a >D-point core plus one disagreeing coordinate.'}


def noncollinear_fixture():
    p, n, D, A = 257, 120, 12, 80
    H = [pow(x, 11, p) for x in range(n)]
    qs = [[1]*n, list(range(n)), [(2*x+2) % p for x in range(n)]]
    f, g = [], []
    for x, h in enumerate(H):
        j, k = [v for v in range(3) if v != x % 3]
        slope = (qs[k][x]-qs[j][x])*pow(k-j, -1, p) % p
        f.append(h*(qs[j][x]-j*slope) % p)
        g.append(h*slope % p)
    supports = []
    for z in range(3):
        support = [x for x in range(n) if (f[x]+z*g[x]-H[x]*qs[z][x]) % p==0]
        assert len(support)>=A
        assert not degree_at_most_on_support(support, [g[x] for x in support], D, p)
        supports.append(set(support))
    assert set.intersection(*supports)=={0}
    assert 2 <= Fraction(A, n)**3*n/16
    return {'p': p, 'n': n, 'D': D, 'A': A, 'bad_labels': 3,
            'full_support_sizes': [len(s) for s in supports],
            'triple_intersection': 1, 'determinant_after_common_factor': 3}


def tuple_checks():
    threshold, r = 5, 2
    roots = [{a: e, b: 1} for a, b, e in
             [(0, 4, 9), (0, 5, 10), (1, 6, 11), (1, 7, 9),
              (2, 8, 12), (3, 9, 10), (4, 5, 3), (5, 6, 2)]]
    counts = {'nondegenerate': 0, 'degenerate': 0}
    for group in combinations(roots, 4):
        missing = []
        for i, P in enumerate(group):
            others = set().union(*(set(Q) for j, Q in enumerate(group) if j!=i))
            heavy = {a for a, e in P.items() if e>=threshold}
            if heavy <= others:
                assert sum(e for a, e in P.items() if a not in others)<=r*threshold
                missing.append(i)
        counts['degenerate' if missing else 'nondegenerate'] += 1
    assert min(counts.values())>0
    return counts


def parameters():
    rows = []
    for r in (1, 2, 4):
        for a in (Fraction(2, 5), Fraction(1, 2), Fraction(3, 4), Fraction(1)):
            delta = a**3/(128*r)
            m = ceil(1536/a**4-5)
            N, J = comb(m+3, 3), m+1
            M = N-J
            beta = Fraction((4*r-1)*(M-1), 2)
            Dmin = int(Fraction(comb(N-1, 2)*(4*r-1), delta))+1
            nmin = ceil(max(96*r/a**3, 64*(beta+4*r)/a**4))
            D = max(Dmin, ceil(Fraction(nmin, 4)))
            n = 4*D
            assert delta*D>comb(N-1, 2)*(4*r-1)
            assert 3*r<=a**3*n/32
            assert Fraction(24*D, m+5)+beta+4*r<=a**4*n/32
            B0 = (1+ceil(1/delta))**(3*r)
            C = 16*B0/a**3
            assert 128*C/a**4==2048*B0/a**7
            rows.append({'r': r, 'a': str(a), 'm': m, 'D': D, 'n': n,
                         'p_must_exceed': m*D, 'linear_coefficient': str(2048*B0/a**7)})
    return rows


def run():
    result = {'status': 'PASS', 'pencil': pencil_fixture(),
              'noncollinear': noncollinear_fixture(), 'tuple_counts': tuple_checks(),
              'parameter_fixtures': parameters(),
              'scope': 'Cluster and full-support ingredients with exact arithmetic; asymptotic theorem still requires the written proof.'}
    Path(__file__).with_name('bounded_root_clusters_verification.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='parameter_fixtures'}, indent=2))


if __name__ == '__main__':
    run()
