#!/usr/bin/env python3
"""Check the high-power gcd proof's spaces and Wronskian orders."""
import json
from math import comb
from pathlib import Path
from poly import add, mul, scale, trim, eval_poly
from poly import divmod_poly, gcd_poly


def compositions(total, length):
    if length == 1:
        yield (total,)
        return
    for a in range(total+1):
        for tail in compositions(total-a, length-1):
            yield (a,)+tail


def power(P, e, p):
    out = [1]
    for _ in range(e):
        out = mul(out, P, p)
    return out


def echelon(rows, p):
    basis = []
    for original in rows:
        row = [x % p for x in original]
        for pivot, earlier in basis:
            c = row[pivot]
            if c:
                for j in range(pivot, len(row)):
                    row[j] = (row[j]-c*earlier[j]) % p
        pivot = next((j for j, c in enumerate(row) if c), None)
        if pivot is not None:
            inv = pow(row[pivot], -1, p)
            row = [c*inv % p for c in row]
            basis.append((pivot, row))
            basis.sort(key=lambda a: a[0])
    return basis


def shifted(P, a, p):
    out = [0]
    for coeff in reversed(P):
        new = [0]*(len(out)+1)
        new[0] = (a*out[0]+coeff) % p
        for i in range(1, len(out)):
            new[i] = (out[i-1]+a*out[i]) % p
        new[-1] = out[-1]
        out = trim(new)
    return out


def padded(P, length):
    return P+[0]*(length-len(P))


def fixture(t, r, m, e, p, root_mode="disjoint"):
    N = comb(m+t-1, t-1)
    J = comb(m+t-3, t-3)
    M = N-J
    assert e > comb(N-1, 2)*(t*r-1) and p > r*m*e
    root_sets = []
    Hs = []
    for i in range(t):
        if r == 1:
            roots = [i+2]
        elif root_mode == "common":
            roots = [0, i+2]
        elif root_mode == "double":
            roots = [i+2, i+2]
        else:
            roots = [i+2, pow(i+2, -1, p)]
        root_sets.append(roots)
        H = [1]
        for a in roots:
            H = mul(H, [-a % p, 1], p)
        Hs.append(H)
    S = sorted(set(a for roots in root_sets for a in roots))
    assert len(S) <= t*r
    # Each H has a private root i+2, certifying affine independence.
    assert all(sum(i+2 in roots for roots in root_sets) == 1 for i in range(t))
    exps = list(compositions(m, t))
    pos = {ex: i for i, ex in enumerate(exps)}
    L = r*m*e
    monomials = []
    for ex in exps:
        base = [1]
        for H, a in zip(Hs, ex):
            base = mul(base, power(H, a, p), p)
        monomials.append(padded(power(base, e, p), L+1))
    assert len(echelon(monomials, p)) == N
    planted_point = -1 % p if root_mode == "common" else 0
    assert planted_point not in S
    cs = [pow(eval_poly(H, planted_point, p), -e, p) for H in Hs]
    F = [cs[0], -cs[1] % p]+[0]*(t-2)
    G = [cs[0], 0, -cs[2] % p] if t == 3 else [0, 0, cs[2], -cs[3] % p]
    generators = []
    for low in compositions(m-1, t):
        for form in (F, G):
            row = [0]*N
            for i, c in enumerate(form):
                ex = list(low)
                ex[i] += 1
                row[pos[tuple(ex)]] = c
            generators.append(row)
    formal_basis = echelon(generators, p)
    assert len(formal_basis) == M
    psis = []
    for _, row in formal_basis:
        out = [0]*(L+1)
        for c, mono in zip(row, monomials):
            if c:
                out = [(a+c*b) % p for a, b in zip(out, mono)]
        psis.append(out)
    descending = echelon([list(reversed(P)) for P in psis], p)
    assert len(descending) == M
    degrees = [L-pivot for pivot, _ in descending]
    wr_degree = sum(degrees)-comb(M, 2)
    assert wr_degree <= M*L-comb(M, 2)
    total_wr_at_S = 0
    local = []
    for a in S:
        local_basis = echelon([padded(shifted(P, a, p), L+1) for P in psis], p)
        assert len(local_basis) == M
        orders = [pivot for pivot, _ in local_basis]
        wr_order = sum(orders)-comb(M, 2)
        alpha_orders = [e*sum(roots.count(a)*v for roots, v in zip(root_sets, ex))
                        for ex in exps]
        filtered_bound = sum(alpha_orders)-J*max(alpha_orders)
        assert sum(orders) >= sum(sorted(alpha_orders)[:M]) >= filtered_bound
        assert wr_order >= filtered_bound-comb(M, 2)
        total_wr_at_S += wr_order
        local.append({"root": a, "adapted_orders": orders,
                      "sum_bound": filtered_bound, "wronskian_order": wr_order})
    assert total_wr_at_S >= N*L-J*t*L-len(S)*comb(M, 2)
    He = [power(H, e, p) for H in Hs]
    def evaluated(form):
        out = [0]
        for c, P in zip(form, He):
            out = add(out, scale(P, c, p), p)
        return out
    gcd = gcd_poly(evaluated(F), evaluated(G), p)
    total_gcd = len(gcd)-1
    for a in S:
        while eval_poly(gcd, a, p) == 0:
            gcd, rem = divmod_poly(gcd, [-a % p, 1], p)
            assert rem == [0]
    outside_gcd = len(gcd)-1
    assert outside_gcd >= 1  # the normalizations plant a common zero outside S.
    assert wr_degree >= total_wr_at_S+M*outside_gcd
    numerator = 2*(t-1)*J*L+(t*r-1)*M*(M-1)
    assert 2*M*outside_gcd <= numerator
    return {"t": t, "r": r, "m": m, "e": e, "p": p, "root_mode": root_mode,
            "N": N, "J": J, "M": M, "degree_cap": L,
            "wronskian_degree": wr_degree, "wronskian_order_on_S": total_wr_at_S,
            "total_gcd_degree": total_gcd, "outside_gcd_degree": outside_gcd,
            "gcd_bound_numerator": numerator, "gcd_bound_denominator": 2*M,
            "local": local}


def run():
    rows = [fixture(*args) for args in [(3, 1, 1, 3, 101), (3, 1, 2, 21, 101),
                                       (3, 2, 2, 51, 1009), (4, 1, 2, 109, 1009),
                                       (4, 2, 2, 253, 2003),
                                       (3, 2, 2, 51, 1009, "common"),
                                       (3, 2, 2, 51, 1009, "double")]]
    # Frobenius breaks monomial independence without the characteristic bound.
    p = 7
    rows_bad = [padded(power([-a % p, 1], p, p), p+1) for a in (1, 2, 3)]
    assert len(echelon(rows_bad, p)) == 2
    # A four-cycle gives an exact multiplicative relation among four quadratics.
    H = [mul([-a % 101, 1], [-b % 101, 1], 101)
         for a, b in ((0, 1), (1, 2), (2, 3), (3, 0))]
    assert mul(H[0], H[2], 101) == mul(H[1], H[3], 101)
    result = {"status": "PASS", "fixtures": rows,
              "negative_controls": ["Frobenius rank collapse", "multiplicative four-cycle"],
              "scope": "Exact ideal dimensions, monomial independence, valuation filtrations, Wronskian orders, and gcd inequalities. Small m gives weak numerical bounds; no finite MCA asymptotic regime is certified by these fixtures."}
    Path(__file__).with_name("power_wronskian_verification.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "PASS", "fixtures": len(rows),
                      "largest_coefficient_degree": max(r["degree_cap"] for r in rows),
                      "negative_controls": result["negative_controls"]}, indent=2))


if __name__ == "__main__":
    run()
