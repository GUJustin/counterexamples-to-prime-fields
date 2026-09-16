#!/usr/bin/env python3
"""Unequal-degree Wronskian accounting with private high-multiplicity roots."""
import json
import sys
from math import comb
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'power_family_mca'))
from poly import add, mul, scale, eval_poly, divmod_poly, gcd_poly
from verify_wronskian import compositions, power, echelon, padded, shifted


def fixture(r, base, m, p):
    t = 4
    N, J = comb(m+3, 3), m+1
    M = N-J
    assert base>comb(N-1, 2)*(t*r-1)
    roots = []
    ps = []
    for i in range(t):
        orders = {i+2: base+7*i}
        if r>=2:
            orders[0] = i+1
        if r>=3:
            orders[1] = 3*(4-i)
        roots.append(orders)
        P = [1]
        for a, exponent in orders.items():
            P = mul(P, power([-a % p, 1], exponent, p), p)
        ps.append(P)
    D = max(len(P)-1 for P in ps)
    assert p>m*D
    S = sorted(set().union(*(set(d) for d in roots)))
    assert all(sum(i+2 in d for d in roots)==1 for i in range(4))
    exps = list(compositions(m, t))
    position = {ex: i for i, ex in enumerate(exps)}
    monos = []
    degrees = []
    for ex in exps:
        P = [1]
        for Q, e in zip(ps, ex):
            P = mul(P, power(Q, e, p), p)
        degrees.append(len(P)-1)
        monos.append(padded(P, m*D+1))
    assert len(echelon(monos, p))==N
    cs = [pow(eval_poly(P, p-1, p), -1, p) for P in ps]
    F, G = [cs[0], -cs[1] % p, 0, 0], [0, 0, cs[2], -cs[3] % p]
    formal = []
    for low in compositions(m-1, t):
        for form in (F, G):
            row = [0]*N
            for i, c in enumerate(form):
                ex = list(low)
                ex[i] += 1
                row[position[tuple(ex)]] = c
            formal.append(row)
    basis = echelon(formal, p)
    assert len(basis)==M
    evaluated = []
    for pivot, row in basis:
        P = [0]*(m*D+1)
        for c, mono in zip(row, monos):
            if c:
                P = [(a+c*b) % p for a, b in zip(P, mono)]
        evaluated.append(P)
    top = echelon([list(reversed(P)) for P in evaluated], p)
    actual_degrees = [m*D-pivot for pivot, _ in top]
    assert sum(actual_degrees)<=sum(sorted(degrees)[-M:])
    wr_degree = sum(actual_degrees)-comb(M, 2)
    root_orders = []
    for a in S:
        local = echelon([padded(shifted(P, a, p), m*D+1) for P in evaluated], p)
        orders = [pivot for pivot, _ in local]
        monomial_orders = [sum(e*d.get(a, 0) for e, d in zip(ex, roots)) for ex in exps]
        lower = sum(monomial_orders)-J*max(monomial_orders)
        assert sum(orders)>=lower
        root_orders.append(sum(orders)-comb(M, 2))
    order_on_S = sum(root_orders)
    assert order_on_S>=sum(degrees)-J*m*sum(len(P)-1 for P in ps)-len(S)*comb(M, 2)
    def form_value(form):
        out = [0]
        for c, P in zip(form, ps):
            out = add(out, scale(P, c, p), p)
        return out
    gcd = gcd_poly(form_value(F), form_value(G), p)
    for a in S:
        while eval_poly(gcd, a, p)==0:
            gcd, rem = divmod_poly(gcd, [-a % p, 1], p)
            assert rem==[0]
    outside = len(gcd)-1
    assert outside>=1
    assert wr_degree>=order_on_S+M*outside
    assert 2*M*outside<=8*J*m*D+(4*r-1)*M*(M-1)
    return {'r': r, 'm': m, 'p': p, 'D': D, 'private_multiplicity_min': base,
            'candidate_degrees': [len(P)-1 for P in ps], 'N': N, 'M': M,
            'wronskian_degree': wr_degree, 'wronskian_order_on_S': order_on_S,
            'outside_gcd_degree': outside}


def run():
    rows = [fixture(*args) for args in [(1, 10, 1, 101), (2, 253, 2, 1009),
                                       (3, 397, 2, 2003)]]
    p, D, m = 1009, 30, 2
    ps = [mul(power([0, 1], D-1, p), [-a % p, 1], p) for a in (1, 2, 3, 4)]
    monos = []
    for ex in compositions(m, 4):
        P = [1]
        for Q, e in zip(ps, ex):
            P = mul(P, power(Q, e, p), p)
        monos.append(padded(P, m*D+1))
    assert len(echelon(monos, p))==3<comb(m+3, 3)
    result = {'status': 'PASS', 'fixtures': rows,
              'negative_control': 'Four candidates with the same heavy root and distinct simple roots have monomial rank 3, not 10.',
              'scope': 'Unequal-degree monomial independence, degree and valuation filtrations, and gcd accounting; not the full asymptotic MCA theorem by enumeration.'}
    Path(__file__).with_name('bounded_root_wronskian_verification.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    run()
