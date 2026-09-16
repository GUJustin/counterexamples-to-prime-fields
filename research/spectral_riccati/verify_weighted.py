#!/usr/bin/env python3
"""Check weighted Riccati label counts, including nonsplit/repeated R."""
import itertools
import json
import math
import random
from pathlib import Path
from verify_constant import add, mul, deriv, scale, trim, residual, eval_poly


def divmod_poly(a, b, p):
    a = trim(a[:])
    q = [0]*max(1, len(a)-len(b)+1)
    while a != [0] and len(a) >= len(b):
        k = len(a)-len(b)
        c = a[-1]*pow(b[-1], -1, p) % p
        q[k] = c
        for i, v in enumerate(b):
            a[k+i] = (a[k+i]-c*v) % p
        trim(a)
    return trim(q), a


def power(a, e, p):
    ans = [1]
    for _ in range(e):
        ans = mul(ans, a, p)
    return ans


def nth_derivative(a, k, p):
    for _ in range(k):
        a = deriv(a, p)
    return a


def valuation(a, factor, p):
    assert a != [0]
    count = 0
    while True:
        q, r = divmod_poly(a, factor, p)
        if r != [0]:
            return count
        count += 1
        a = q


def weighted_compositions(total, weights):
    if len(weights) == 1:
        if total >= weights[0] and total % weights[0] == 0:
            yield (total//weights[0],)
        return
    for e in range(1, (total-sum(weights[1:]))//weights[0]+1):
        for tail in weighted_compositions(total-e*weights[0], weights[1:]):
            yield (e,)+tail


def gcd_poly(a, b, p):
    while b != [0]:
        a, b = b, divmod_poly(a, b, p)[1]
    return scale(a, pow(a[-1], -1, p), p)


def pow_mod(a, e, modulus, p):
    ans = [1]
    a = divmod_poly(a, modulus, p)[1]
    while e:
        if e & 1:
            ans = divmod_poly(mul(ans, a, p), modulus, p)[1]
        e >>= 1
        if e:
            a = divmod_poly(mul(a, a, p), modulus, p)[1]
    return ans


def equal_degree_factors(F, d, p, rng):
    if len(F)-1 == d:
        return [F]
    for _ in range(1000):
        a = trim([rng.randrange(p) for _ in range(len(F)-1)])
        g = gcd_poly(a, F, p)
        if len(g) in (1, len(F)):
            b = pow_mod(a, (p**d-1)//2, F, p)
            g = gcd_poly(add(b, [1], p, -1), F, p)
        if 1 < len(g) < len(F):
            other, rem = divmod_poly(F, g, p)
            assert rem == [0]
            return (equal_degree_factors(g, d, p, rng)
                    + equal_degree_factors(other, d, p, rng))
    raise AssertionError("deterministic-seed equal-degree split did not finish")


def factor_list(R, p, cap):
    """All irreducible factors of degree <=cap; higher degrees cannot occur in P."""
    assert cap <= 3
    common = gcd_poly(R, deriv(R, p), p)
    remaining, rem = divmod_poly(R, common, p)
    assert rem == [0]  # char > deg R, so this quotient is the radical.
    h = [0, 1]
    factors = []
    rng = random.Random(sum(c*p**i for i, c in enumerate(R)))
    for d in range(1, cap+1):
        if remaining == [1]:
            break
        h = pow_mod(h, p, remaining, p)
        block = gcd_poly(add(h, [0, 1], p, -1), remaining, p)
        if block != [1]:
            factors.extend(equal_degree_factors(block, d, p, rng))
            remaining, rem = divmod_poly(remaining, block, p)
            assert rem == [0]
            if remaining != [1]:
                h = divmod_poly(h, remaining, p)[1]
    # Independent irreducibility and completeness checks in this degree range.
    assert len({tuple(f) for f in factors}) == len(factors)
    for f in factors:
        assert f[-1] == 1 and 1 <= len(f)-1 <= cap
        if len(f)-1 in (2, 3):
            assert all(eval_poly(f, a, p) != 0 for a in range(p))
    if remaining != [1]:
        for d in range(1, cap+1):
            assert gcd_poly(add(pow_mod([0, 1], p**d, remaining, p),
                                [0, 1], p, -1), remaining, p) == [1]
    return [(f, valuation(R, f, p)) for f in sorted(factors)]


def planted(p, D, b, root_mults, c):
    P = [1]
    E = [1]
    for a, e, m in root_mults:
        P = mul(P, power([-a % p, 1], e, p), p)
        E = mul(E, power([-a % p, 1], m, p), p)
    assert len(P)-1 == D and len(E)-1 == b+1
    R = add(mul([c, 1], P, p), E, p)
    C, rem = divmod_poly(add(mul(E, deriv(P, p), p), mul(deriv(E, p), P, p), p, -1), P, p)
    assert rem == [0] and len(C)-1 == b
    return R, P, C


def run():
    rng = random.Random(2026091603)
    cases = []
    for D, b in [(3, 0), (7, 1), (8, 1), (11, 1), (13, 2), (14, 2)]:
        p = 101
        for _ in range(2):
            roots = rng.sample(range(p), D+1)
            R = [1]
            for a in roots:
                R = mul(R, [-a % p, 1], p)
            cases.append((p, D, b, R, None, "random split"))
    for D in (7, 8, 11, 14):
        for e in (2, D//2, D-1):
            p, b = 101, 1
            R, P, C = planted(p, D, b, [(0, e, 1), (1, D-e, 1)], 3)
            cases.append((p, D, b, R, (P, C), "planted two roots"))
    for D in (13, 14, 17):
        for spec in ([(0, D-4, 1), (1, 2, 1), (2, 2, 1)],
                     [(0, D//2, 2), (1, D-D//2, 1)]):
            p, b = 101, 2
            R, P, C = planted(p, D, b, spec, 5)
            cases.append((p, D, b, R, (P, C), "planted repeated or three roots"))
    # Explicit nonsplit candidate P=(X^2+2)^4 over F_5, with R=(X+1)P+E.
    # F_5 is too small for the characteristic hypothesis, so use F_101
    # and an irreducible quadratic found deterministically instead.
    p, D, b = 101, 8, 1
    nonresidue = next(a for a in range(2, p) if pow(a, (p-1)//2, p) == p-1)
    E = [-nonresidue % p, 0, 1]
    P = power(E, 4, p)
    R = add(mul([1, 1], P, p), E, p)
    C = scale(deriv(E, p), 3, p)
    cases.append((p, D, b, R, (P, C), "nonsplit candidate"))
    for D in (3, 4, 5, 6, 7):
        p, b = 11, 1
        for roots in itertools.combinations(range(p), D+1):
            R = [1]
            for a in roots:
                R = mul(R, [-a % p, 1], p)
            cases.append((p, D, b, R, None, "all split R over F_11"))
    records = []
    candidates = solutions = local_checks = charge_checks = 0
    for p, D, bcap, R, expected, name in cases:
        fs = factor_list(R, p, bcap+1)
        assert len(R)-1 == D+1 and p>D+1
        powers = [[power(f, e, p) for e in range(D//(len(f)-1)+1)] for f, m in fs]
        log_terms = []
        for f, m in fs:
            q, rem = divmod_poly(R, f, p)
            assert rem == [0]
            log_terms.append(mul(q, deriv(f, p), p))
        base = scale(deriv(R, p), -1, p)
        groups = {}
        planted_found = expected is None
        case_candidates = 0
        case_solutions = 0
        for count in range(1, min(bcap+1, len(fs))+1):
            for indices in itertools.combinations(range(len(fs)), count):
                weights = [len(fs[i][0])-1 for i in indices]
                root_count = sum(weights)
                if root_count > bcap+1:
                    continue
                for es in weighted_compositions(D, weights):
                    candidates += 1
                    case_candidates += 1
                    P = [1]
                    C = base[:]
                    for i, e in zip(indices, es):
                        P = mul(P, powers[i][e], p)
                        C = add(C, scale(log_terms[i], e, p), p)
                    C = add(C, P, p)
                    if C == [0] or len(C)-1 > bcap:
                        continue
                    b = len(C)-1
                    zz = C[-1]
                    B = scale(C, pow(zz, -1, p), p)
                    assert residual(R, P, p) == mul(C, P, p)
                    quotient, E = divmod_poly(R, P, p)
                    assert len(quotient) == 2 and quotient[-1] == 1
                    assert len(E)-1 == b+1 and root_count <= b+1
                    if expected is not None and P == expected[0] and C == expected[1]:
                        planted_found = True
                    solutions += 1
                    case_solutions += 1
                    key = tuple(B)
                    groups.setdefault(key, set()).add(zz)
                    if D > (b+1)*(b+2):
                        high = [(i, e) for i, e in zip(indices, es) if e >= b+3]
                        assert high
                        derivR = nth_derivative(R, b+2, p)
                        for i, e in high:
                            f, m = fs[i]
                            assert 1 <= m <= b+1 < e
                            M = valuation(derivR, f, p)
                            assert M >= e-b-2
                            assert valuation(B, f, p) == m-1
                            Rm = scale(nth_derivative(R, m, p), pow(math.factorial(m), -1, p), p)
                            Bm = scale(nth_derivative(B, m-1, p), pow(math.factorial(m-1), -1, p), p)
                            local = add(scale(Bm, zz, p), scale(Rm, e-m, p), p, -1)
                            assert divmod_poly(local, f, p)[1] == [0]
                            local_checks += len(f)-1
                        charge_checks += 1
        for B, labels in groups.items():
            b = len(B)-1
            if D > (b+1)*(b+2):
                assert len(labels) <= D-b-1
        assert planted_found
        records.append({"p": p, "D": D, "weight_degree_cap": bcap, "family": name,
                        "R": R, "eligible_factor_degrees_and_multiplicities":
                        [[len(f)-1, m] for f, m in fs],
                        "candidates": case_candidates, "solutions": case_solutions,
                        "weight_groups": [{"B": list(B), "labels": sorted(labels)}
                                          for B, labels in sorted(groups.items())]})
    violations = [
        {"D": row["D"], "p": row["p"], "R": row["R"], **g}
        for row in records for g in row["weight_groups"]
        if row["D"] <= len(g["B"])*(len(g["B"])+1)
        and len(g["labels"]) > row["D"]-len(g["B"])]
    assert violations, "negative control for dropping the large-D hypothesis"
    result = {"status": "PASS", "fixtures": len(records), "candidates_checked": candidates,
              "nonzero_solutions": solutions, "local_identity_checks": local_checks,
              "high_multiplicity_charges": charge_checks,
              "largest_label_group": max(len(g["labels"]) for row in records for g in row["weight_groups"]),
              "below_threshold_violations_count": len(violations),
              "below_threshold_examples": sorted(violations, key=lambda a: -len(a["labels"]))[:3],
              "scope": "All supported candidates with <=b+1 algebraic roots; written proof justifies this reduction",
              "records": records}
    header = json.dumps({k: val for k, val in result.items() if k != "records"}, indent=2)
    output = (header[:-2] + ',\n  "records": [\n'
              + ',\n'.join('    '+json.dumps(row, sort_keys=True, separators=(',', ':'))
                           for row in records) + '\n  ]\n}\n')
    Path(__file__).with_name("weighted_spectral_riccati_verification.json").write_text(output)
    print(json.dumps({k: v for k, v in result.items()
                      if k not in ("records", "below_threshold_examples")}, indent=2))


if __name__ == "__main__":
    run()
