#!/usr/bin/env python3
"""Finite checks for the spectral Riccati rigidity lemma; stdlib only."""
import itertools
import json
import random
from pathlib import Path


def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b, p, sign=1):
    c = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        c[i] += x
    for i, x in enumerate(b):
        c[i] += sign * x
    return trim([x % p for x in c])


def mul(a, b, p):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] = (c[i+j] + x*y) % p
    return trim(c)


def deriv(a, p):
    return trim([i*a[i] % p for i in range(1, len(a))] or [0])


def scale(a, c, p):
    return trim([c*x % p for x in a])


def power_linear(a, e, p):
    ans = [1]
    for _ in range(e):
        ans = mul(ans, [-a % p, 1], p)
    return ans


def eval_poly(a, x, p):
    ans = 0
    for c in reversed(a):
        ans = (ans*x+c) % p
    return ans


def compositions(total, length):
    if length == 1:
        yield (total,)
    else:
        for k in range(total+1):
            for tail in compositions(total-k, length-1):
                yield (k,) + tail


def residual(R, P, p):
    return add(add(mul(R, deriv(P, p), p),
                   mul(deriv(R, p), P, p), p, -1), mul(P, P, p), p)


def get_label(R, P, p):
    if P == [0]:
        return None
    Q = residual(R, P, p)
    d = len(P)-1
    z = (Q[d] if d < len(Q) else 0) * pow(P[-1], -1, p) % p
    return z if Q == scale(P, z, p) else None


def run():
    rng = random.Random(20260916)
    cases = []
    for D, p in [(1, 7), (2, 7), (3, 11), (4, 13), (5, 17),
                 (6, 19), (7, 23), (8, 29)]:
        for _ in range(3):
            cases.append((p, D, sorted(rng.sample(range(p), D+1)), "random split"))
    for D, p in [(2, 1009), (3, 1009), (4, 1009), (5, 101),
                 (6, 1009), (7, 1009), (8, 1009)]:
        roots = [x for x in range(p) if (pow(x, D+1, p)-x) % p == 0]
        assert len(roots) == D+1
        cases.append((p, D, roots, "X^(D+1)-X"))
    cases.append((11, 3, [0, 1, 2, 3], "sharp cubic-candidate example"))
    rows = []
    tested = 0
    all_polynomials = 0
    for p, D, roots, name in cases:
        R = [1]
        for a in roots:
            R = mul(R, [-a % p, 1], p)
        solutions = []
        zero_label_count = 0
        powers = [[power_linear(a, e, p) for e in range(D+1)] for a in roots]
        for exps in compositions(D, D+1):
            P = [1]
            for i, e in enumerate(exps):
                P = mul(P, powers[i][e], p)
            tested += 1
            z = get_label(R, P, p)
            if z is None:
                continue
            if z == 0:
                zero_label_count += 1
                assert sorted(exps) == [0] + [1]*D
                continue
            assert D >= 2
            assert sum(e > 0 for e in exps) == 1
            a = roots[exps.index(D)]
            assert z == (D-1)*eval_poly(deriv(R, p), a, p) % p
            # Determine c by the X^D coefficient, and check the entire identity.
            top = power_linear(a, D+1, p)
            c = (R[D]-top[D]) % p
            formula = add(add(top, scale(power_linear(a, D, p), c, p), p),
                          scale([-a % p, 1], z*pow(D-1, -1, p) % p, p), p)
            assert R == formula
            solutions.append({"root": a, "label": z})
        assert zero_label_count == D+1
        bound = 0 if D == 1 else 3 if D == 2 else 2 if D == 3 else 1
        assert len(solutions) <= bound
        # Enumerate EVERY degree <=D polynomial for small fields, not only
        # supported monic candidates, to test the preliminary reductions.
        if D <= 3 and p <= 11:
            found = set()
            for coeffs in itertools.product(range(p), repeat=D+1):
                P = trim(list(coeffs))
                all_polynomials += 1
                if P == [0]:
                    continue
                z = get_label(R, P, p)
                if z is None:
                    continue
                assert len(P) == D+1 and P[-1] == 1
                if z:
                    assert any(P == power_linear(s["root"], D, p)
                               and z == s["label"] for s in solutions)
                else:
                    assert sum(eval_poly(P, a, p) == 0 for a in roots) == D
                found.add((tuple(P), z))
            assert len(found) == zero_label_count + len(solutions)
        rows.append({"p": p, "D": D, "family": name, "roots": roots,
                     "nonzero_solutions": solutions, "bound": bound})
    sharp = rows[-1]
    assert len(sharp["nonzero_solutions"]) == 2
    assert len({s["label"] for s in sharp["nonzero_solutions"]}) == 2
    # The proof only needs deg gcd(R,P)>=1: squarefreeness of R is
    # unnecessary. Exhaust every monic R and monic degree-D P over F_5,
    # including nonsplit R and repeated roots, through D=3.
    arbitrary_R_cases = 0
    arbitrary_R_candidates = 0
    arbitrary_R_solutions = 0
    for D in (1, 2, 3):
        p = 5
        for rcoeffs in itertools.product(range(p), repeat=D+1):
            R = list(rcoeffs)+[1]
            arbitrary_R_cases += 1
            found = []
            for pcoeffs in itertools.product(range(p), repeat=D):
                P = list(pcoeffs)+[1]
                arbitrary_R_candidates += 1
                z = get_label(R, P, p)
                if z is None:
                    continue
                arbitrary_R_solutions += 1
                if z == 0:
                    assert any(R == mul(P, [-a % p, 1], p) for a in range(p))
                else:
                    assert D >= 2
                    roots = [a for a in range(p) if P == power_linear(a, D, p)]
                    assert len(roots) == 1
                    a = roots[0]
                    assert eval_poly(R, a, p) == 0
                    assert eval_poly(deriv(R, p), a, p) != 0
                    top = power_linear(a, D+1, p)
                    c = (R[D]-top[D]) % p
                    assert R == add(add(top, scale(P, c, p), p),
                                    scale([-a % p, 1], z*pow(D-1, -1, p) % p, p), p)
                found.append((tuple(P), z))
            zero_count = sum(z == 0 for P, z in found)
            assert zero_count == sum(eval_poly(R, a, p) == 0 for a in range(p))
            assert sum(z != 0 for P, z in found) <= (0 if D == 1 else 3 if D == 2 else 2)
    result = {"status": "PASS", "cases": len(rows),
              "supported_candidates_checked": tested,
              "all_degree_bounded_polynomials_checked": all_polynomials,
              "nonzero_solutions": sum(len(r["nonzero_solutions"]) for r in rows),
              "arbitrary_monic_R_cases": arbitrary_R_cases,
              "arbitrary_R_candidates_checked": arbitrary_R_candidates,
              "arbitrary_R_solutions": arbitrary_R_solutions,
              "rows": rows}
    out = Path(__file__).with_name("spectral_riccati_verification.json")
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "rows"}, indent=2))


if __name__ == "__main__":
    run()
