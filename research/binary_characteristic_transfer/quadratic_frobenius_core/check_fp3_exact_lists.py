"""Exact physical-fiber and label census; no enumeration of all quadratics.

The separate proved quadratic classification excludes competitors.
These small primes test the spectrum, not the p>=4099 uniform certificate.
"""
import json
from collections import Counter
from math import isqrt
from pathlib import Path


def check(p):
    aa, bb = next((a, b) for a in range(p) for b in range(1, p)
                  if all((t**3+a*t+b) % p for t in range(p)))
    zero, one, eta = (0, 0, 0), (1, 0, 0), (0, 0, 1)

    def sub(x, y):
        return tuple((a-b) % p for a, b in zip(x, y))

    def mul(x, y):
        c0, c1, c2 = x[0]*y[0], x[0]*y[1]+x[1]*y[0], x[0]*y[2]+x[1]*y[1]+x[2]*y[0]
        c3, c4 = x[1]*y[2]+x[2]*y[1], x[2]*y[2]
        return ((c0-bb*c3) % p, (c1-aa*c3-bb*c4) % p, (c2-aa*c4) % p)

    def power(x, n):
        r = one
        while n:
            if n & 1:
                r = mul(r, x)
            x = mul(x, x)
            n //= 2
        return r

    W = [(a, b, 0) for a in range(p) for b in range(p)]
    yp = {y: power(y, p) for y in W}
    weight = {y: (0 if y == zero else 2*int(power(y, (p**3-1)//2) == one)) for y in W}
    assert sum(weight.values()) == p*p-1
    deleted = [y for y in W if mul(eta, y)[2] == 0]
    assert len(deleted) == p and sum(weight[y] for y in deleted) == p-1
    ceilroot = isqrt(16*p)+int(isqrt(16*p)**2 < 16*p)
    A = 2*p-ceilroot-2
    assert (A-p)**2 > 4*p and A > p and A > 16
    # Endpoint surgery: all choices in b + Lambda0 share the same witness.
    u0 = next(y for y in deleted if y != zero)
    astar = power(mul(eta, u0), p-1)
    special = {y: sub(yp[y], mul(astar, y)) for y in W}
    cstar, fstar = Counter(), Counter()
    for y in W:
        cstar[special[y]] += weight[y]
        if y not in deleted:
            fstar[special[y]] += weight[y]
    bstar = min((b for b in cstar if b != zero), key=lambda b: (cstar[b], b))
    vs = sorted(cstar, key=lambda v: (fstar[v], v))[:2]
    removed_core = [y for y in W if special[y] == bstar]
    removed_fresh = []  # The stronger theorem only deletes the core fiber.
    removed_size = sum(weight[y] for y in removed_core+removed_fresh)
    assert removed_size <= p
    excluded_plane = {sub(b, mul(eta, v)) for b in cstar for v in cstar}
    endpoints = [sub(bstar, mul(eta, v)) for v in vs]
    far_coset = {sub(bstar, mul(eta, v)) for v in cstar}
    post_lists = Counter()
    lists, best = Counter(), {}
    for u in [one]+[(a, 1, 0) for a in range(p)]:
        a = power(u, p-1)
        core, removed = Counter(), Counter()
        for y in W:
            b = sub(yp[y], mul(a, y))
            core[b] += weight[y]
        for y in deleted:
            removed[sub(yp[y], mul(a, y))] += weight[y]
        assert len(core) == p
        fresh = {v: count-removed[v] for v, count in core.items()}
        punctured_core, punctured_fresh = Counter(), Counter()
        for y in removed_core:
            punctured_core[sub(yp[y], mul(a, y))] += weight[y]
        for y in removed_fresh:
            punctured_fresh[sub(yp[y], mul(a, y))] += weight[y]
        for b, c0 in core.items():
            for v, c1 in fresh.items():
                lam = sub(b, mul(eta, v))
                agreement = c0+c1
                best[lam] = max(best.get(lam, 0), agreement)
                if agreement >= A:
                    lists[lam] += 1
                loss = punctured_core[b]+punctured_fresh[v]
                if lam not in excluded_plane:
                    assert loss <= 2
                if agreement-loss >= A-2:
                    post_lists[lam] += 1
    assert len(lists) == p**3
    histogram = Counter(lists.values())
    assert histogram == {1: p**3-p, p: p}
    assert sum(lam not in excluded_plane and size == 1
               for lam, size in post_lists.items()) == p**3-p*p
    assert all(post_lists[lam] == 0 for lam in endpoints)
    assert all(post_lists[lam] == 0 for lam in far_coset)
    assert Counter(post_lists.values()) == {1: p**3-2*p, p: p}
    return dict(p=p, defining_cubic=[bb, aa, 0, 1], eta=eta,
                N=2*p*p-p-1, A=A, label_count=len(lists),
                list_size_histogram=dict(histogram),
                minimum_best_canonical_agreement=min(best.values()),
                maximum_best_canonical_agreement=max(best.values()),
                puncturing=dict(deleted_coordinates=removed_size,
                                remaining_length=2*p*p-p-1-removed_size,
                                threshold=A-2, endpoints=endpoints,
                                exact_empty_labels=len(far_coset),
                                exact_canonical_bank_singletons=p**3-2*p,
                                all_quadratic_exclusion_applies=(A-2>p and (A-2-p)**2>4*p and A-2>16),
                                retained_bank_list_histogram=dict(Counter(post_lists.values())),
                                scope='canonical bank census; full exclusion requires the recorded threshold guard'),
                passed=True)


if __name__ == '__main__':
    rows = [check(p) for p in (47, 53)]
    Path(__file__).with_suffix('.json').write_text(json.dumps(rows, indent=2)+'\n')
    print(json.dumps(rows, indent=2))
