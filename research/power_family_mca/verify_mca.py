#!/usr/bin/env python3
"""Check the heavy/light and dependence counts for quadratic-power MCA."""
import json
import random
from collections import defaultdict
from itertools import combinations
from math import comb, factorial
from pathlib import Path
from poly import degree_at_most_on_support
from verify_wronskian import echelon


def divisor(a, b, p):
    roots = [x for x in range(p) if (x*x+a*x+b) % p == 0]
    if len(roots) == 2:
        return {("linear", x): 1 for x in roots}
    if len(roots) == 1:
        return {("linear", roots[0]): 2}
    return {("quadratic", a, b): 1}


def dependent(divs):
    keys = sorted(set().union(*(d.keys() for d in divs)))
    rows = [[d.get(k, 0)-divs[0].get(k, 0) for k in keys] for d in divs[1:]]
    # Every relevant minor has size at most three, entries in [-2,2],
    # and absolute value <=48. Reduction modulo 101 preserves rational rank.
    return len(echelon(rows, 101)) < len(rows)


def check_line(p, n, e, A, f, g):
    r, D, B = 2, 2*e, A//2
    assert A>D+1 and B>r and A-r-B+1>0
    inverse_g = [pow(x, -1, p) if x else 0 for x in g]
    Lf = Lg = bad_witnesses = light_witnesses = 0
    heavy_zero, heavy_nonzero, light, bad = set(), set(), set(), set()
    light_by_direction = defaultdict(set)
    bad_by_direction = defaultdict(set)
    fixed_polynomial_bad = defaultdict(set)
    selected_light = {}
    directions = {}
    pair_checks = 0
    for a in range(p):
        for b in range(p):
            key = (a, b)
            H = [pow((x*x+a*x+b) % p, e, p) for x in range(n)]
            inverse_H = [pow(x, -1, p) if x else 0 for x in H]
            dir_Lf = dir_Lg = 0
            pair_labels = defaultdict(set)
            for c in range(1, p):
                P = [c*x % p for x in H]
                close_f = sum(x == y for x, y in zip(P, f)) >= B
                close_g = sum(x == y for x, y in zip(P, g)) >= B
                Lf += close_f
                Lg += close_g
                dir_Lf += close_f
                dir_Lg += close_g
                persistent, labels = [], defaultdict(list)
                for i in range(n):
                    if g[i]:
                        labels[(P[i]-f[i])*inverse_g[i] % p].append(i)
                    elif P[i] == f[i]:
                        persistent.append(i)
                for z, extra in labels.items():
                    if len(extra)+len(persistent)<A:
                        continue
                    support = sorted(persistent+extra)
                    if degree_at_most_on_support(support, [g[i] for i in support], D, p):
                        continue
                    bad.add(z)
                    bad_witnesses += 1
                    bad_by_direction[key].add(z)
                    fixed_polynomial_bad[(key, c)].add(z)
                    groups = defaultdict(list)
                    for i in support:
                        if H[i]:
                            groups[g[i]*inverse_H[i] % p].append(i)
                    heavy = [q for q, positions in groups.items() if len(positions)>=B]
                    if heavy:
                        for q in heavy:
                            if q == 0:
                                assert close_f
                                heavy_zero.add(z)
                            else:
                                assert sum(q*H[i] % p == g[i] for i in range(n))>=B
                                heavy_nonzero.add(z)
                    else:
                        light.add(z)
                        light_witnesses += 1
                        light_by_direction[key].add(z)
                        selected_light.setdefault(z, (key, support))
                    usable = 0
                    for i, j in combinations(support, 2):
                        if H[i] and H[j] and g[i]*inverse_H[i] % p != g[j]*inverse_H[j] % p:
                            usable += 1
                            pair_labels[(i, j)].add(z)
                    if not heavy:
                        assert 2*usable >= (A-r)*(A-r-B+1)
                    pair_checks += 1
            assert dir_Lf <= n//(B-r) and dir_Lg <= n//(B-r)
            assert all(len(zs)<=1 for zs in pair_labels.values())
            if key in light_by_direction:
                directions[key] = divisor(a, b, p)
    T = n*(n-1)//((A-r)*(A-r-B+1))
    assert all(len(zs)<=T for zs in light_by_direction.values())
    direction_bound = r+comb(n, 2)//(A-r-1)
    assert all(len(zs)<=direction_bound for zs in bad_by_direction.values())
    assert all(len(zs)<=n for zs in fixed_polynomial_bad.values())
    assert len(heavy_zero)<=n*Lf and len(heavy_nonzero)<=Lg*direction_bound
    assert bad == heavy_zero | heavy_nonzero | light
    selected = list(selected_light.values())
    dep_counts = {}
    for t in (3, 4):
        count = sum(dependent([directions[key] for key, support in group])
                    for group in combinations(selected, t))
        C = sum(comb((j+1)*r-1, r) for j in range(1, t))
        assert factorial(t)*count <= T*C*len(selected)**(t-1)
        dep_counts[str(t)] = count
    return {"p": p, "n": n, "e": e, "D": D, "A": A, "B": B,
            "Lf": Lf, "Lg": Lg, "bad_labels": len(bad),
            "bad_witnesses": bad_witnesses, "light_witnesses": light_witnesses,
            "heavy_zero_labels": len(heavy_zero), "heavy_nonzero_labels": len(heavy_nonzero),
            "light_labels": len(light), "direction_light_bound": T,
            "usable_pair_checks": pair_checks, "dependent_tuples": dep_counts}


def run():
    rng = random.Random(2026091605)
    rows = []
    for p, n, e in ((13, 12, 2), (17, 16, 3), (23, 20, 4)):
        A = max(2*e+2, 2*n//3)
        for variant in range(8):
            f = [rng.randrange(p) for _ in range(n)]
            g = [rng.randrange(p) for _ in range(n)]
            a, b, c, z = rng.randrange(p), rng.randrange(p), rng.randrange(1, p), rng.randrange(p)
            H = [pow((x*x+a*x+b) % p, e, p) for x in range(n)]
            if variant<2:
                for i in rng.sample(range(n), A):
                    f[i] = (c*H[i]-z*g[i]) % p
            elif variant<4:
                f = [3*x % p for x in H]
                g = [2*x % p for x in H]
                for i in rng.sample(range(n), 3):
                    f[i], g[i] = rng.randrange(p), rng.randrange(p)
            elif variant<6:
                for i in range(A-1):
                    f[i], g[i] = c*H[i] % p, 0
                f[A-1], g[A-1] = c*H[A-1] % p, 1
            else:
                planted = []
                for _ in range(3):
                    aa, bb, cc = rng.randrange(p), rng.randrange(p), rng.randrange(1, p)
                    planted.append([cc*pow((x*x+aa*x+bb) % p, e, p) % p for x in range(n)])
                for i in range(n):
                    j, k = [j for j in range(3) if j != i % 3]
                    g[i] = (planted[k][i]-planted[j][i])*pow(k-j, -1, p) % p
                    f[i] = (planted[j][i]-j*g[i]) % p
            rows.append(check_line(p, n, e, A, f, g))
    for key in ("bad_witnesses", "light_witnesses", "heavy_zero_labels", "heavy_nonzero_labels"):
        assert sum(r[key] for r in rows)>0
    divisor_fixtures = []
    all_divs = [divisor(a, b, 7) for a in range(7) for b in range(7)]
    for divs, T in [(all_divs, 1), ([d for d in all_divs[:25] for _ in range(2)], 2)]:
        counts = {}
        for t in (3, 4):
            count = sum(dependent(group) for group in combinations(divs, t))
            C = sum(comb((j+1)*2-1, 2) for j in range(1, t))
            assert factorial(t)*count <= T*C*len(divs)**(t-1)
            assert count>0
            counts[str(t)] = count
        divisor_fixtures.append({"labeled_directions": len(divs), "maximum_repetitions": T,
                                 "dependent_tuples": counts})
    result = {"status": "PASS", "fixtures": len(rows),
              "bad_witnesses": sum(r["bad_witnesses"] for r in rows),
              "light_witnesses": sum(r["light_witnesses"] for r in rows),
              "rows": rows, "divisor_fixtures": divisor_fixtures,
              "scope": "Full-support interpolation, fixed-word scale counts, both heavy cases, light-direction pair bounds, and divisor-dependence counts. Does not numerically certify the asymptotic gcd threshold."}
    Path(__file__).with_name("quadratic_power_mca_verification.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({k: v for k, v in result.items() if k != "rows"}, indent=2))


if __name__ == "__main__":
    run()
