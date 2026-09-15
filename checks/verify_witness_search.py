#!/usr/bin/env python3
"""Exact fresh-query witness search on a small valid circle-code instance.

The claim is zero before sample generation. Challenges exhaust H and include
eight outside-H controls per sample. This is not a uniform E-challenge trial.
"""
from itertools import combinations
from math import comb, log2
from pathlib import Path
import json
import random
import time
import verify_fixed_claim as ff
import verify_scheduled_transfer as sched

ff.P = 23
ff.inverse.cache_clear()
F, p, M, h, m, n = ff.F, 23, 12, 4, 2, 24
zero, one = F(0), F(1)
assert F((2, 1, 0, 0))**((p*p-1)//2) == -one
step = next(F((x, y, 0, 0)) for x in range(p) for y in range(p)
            if (x*x+y*y) % p == 1
            and F((x, y, 0, 0))**12 != one
            and F((x, y, 0, 0))**8 != one)
lam = step**2
roots = {j: lam**j for j in range(1, M)}
supports = [u for u in combinations(range(1, M), h) if sum(u) % M == 1]
base = supports[0]
scale = one+one/lam
assert scale**p/scale == lam
claim = zero  # Fixed before generating or inspecting samples or queries.


def prod(values):
    answer = one
    for value in values:
        answer *= value
    return answer


def poly(support):
    coeff = [one]
    for j in support:
        nxt = [zero]*(len(coeff)+1)
        for k, value in enumerate(coeff):
            nxt[k] -= value*roots[j]
            nxt[k+1] += value
        coeff = nxt
    return coeff


def evaluate(coeff, x):
    answer = zero
    for value in reversed(coeff):
        answer = answer*x+value
    return answer


def divide_exact(numerator, denominator):
    work = numerator[:]
    quotient = [zero]*(len(work)-len(denominator)+1)
    for j in reversed(range(len(quotient))):
        quotient[j] = work[j+len(denominator)-1]/denominator[-1]
        for k, value in enumerate(denominator):
            work[j+k] -= quotient[j]*value
    assert all(value == zero for value in work)
    return quotient


def entries(indices, factors):
    return [(len(u), sum(u) % M, prod(factors[j] for j in u), u)
            for k in range(min(h, len(indices))+1)
            for u in combinations(indices, k)]


def prepare(factors):
    left = entries(range(1, 6), factors)
    right = entries(range(6, 12), factors)
    buckets = {}
    for k, residue, value, u in right:
        buckets.setdefault((k, residue, value), []).append(u)
    return [(k, r, ff.inverse(value), u) for k, r, value, u in left], buckets, len(right)


def search(target, left, right):
    if target == zero:
        return set()
    found = set()
    for k, residue, inverse_value, u in left:
        key = (h-k, (1-residue) % M, target*inverse_value)
        for v in right.get(key, []):
            found.add(tuple(sorted(u+v)))
    return found


domain_u = [step**j for j in range(n)]
domain = [sched.circle(u) for u in domain_u]
base_poly = poly(base)
table = [scale*u**(-h)*evaluate(base_poly, u*u) for u in domain_u]
assert all(value[1:] == (0, 0, 0) for value in table)
challenges = [F((x, y, 0, 0)) for x in range(p) for y in range(p)]
challenges += [F((j, 0, 1, 0)) for j in range(8)]
rng = random.Random(20260915)
samples = []
while len(samples) < 128:
    a = F(tuple(rng.randrange(p) for _ in range(4)))
    if a not in samples and sched.admissible(a) and a*a not in roots.values():
        samples.append(a)

start = time.perf_counter()
queries = successes = nonzero_successes = witnesses = identities = lookups = 0
records = []
for a in samples:
    factors = {j: a*a-root for j, root in roots.items()}
    assert all(value != zero for value in factors.values())
    multiplier = scale*a**(-h)
    base_product = prod(factors[j] for j in base)
    exhaustive = {}
    for u in supports:
        value = multiplier*(base_product-prod(factors[j] for j in u))
        exhaustive.setdefault(value, set()).add(u)
    left, right, right_count = prepare(factors)
    assert len(left) == 31 and right_count == 57
    assert search(zero, left, right) == set()
    for alpha in challenges:
        beta = claim+alpha
        target = base_product-beta/multiplier
        found = search(target, left, right)
        assert found == exhaustive.get(beta, set())
        queries += 1
        lookups += len(left) if target != zero else 0
        successes += bool(found)
        nonzero_successes += bool(found) and alpha != zero
        witnesses += len(found)
        for u in found:
            assert alpha[2:] == (0, 0), 'Outside-H search success requires a separate quotient schedule.'
            # Every returned support is independently rechecked on all coordinates.
            coeff = poly(u)
            assert multiplier*(base_product-evaluate(coeff, a*a)) == beta
            z = sched.circle(a)
            X0, X1 = ff.parts(z[0]); Y0, Y1 = ff.parts(z[1])
            B0, B1 = ff.parts(beta)
            i = F((0, 1, 0, 0))
            slope, ell_slope = X1/Y1, B1/Y1
            denominator = [(one-i*slope)/4, (-X0+slope*Y0)/2, (one+i*slope)/4]
            numerator = [zero]*(2*m+1)
            assert base_poly[0] == coeff[0] and base_poly[-1] == coeff[-1]
            for k in range(1, h):
                numerator[2*(k-1)] = scale*(base_poly[k]-coeff[k])
            ell_coeff = [-ell_slope/(2*i), B0-ell_slope*Y0, ell_slope/(2*i)]
            for k, value in enumerate(ell_coeff):
                numerator[m-1+k] -= value
            witness_coeff = divide_exact(numerator, denominator)
            assert len(witness_coeff) == 2*m-1
            assert all(value[2:] == (0, 0) for value in witness_coeff)
            agreements = 0
            for j, t in enumerate(domain_u):
                x, y = domain[j]
                U = (x-X0)/2-(X1/Y1)*(y-Y0)/2
                ell = B0+(B1/Y1)*(y-Y0)
                Fu = scale*t**(-h)*(evaluate(base_poly, t*t)-evaluate(coeff, t*t))
                Pj = t**(1-m)*evaluate(witness_coeff, t)
                assert Pj == (Fu-ell)/U
                residual = sched.raw(table[j], claim, z, domain[j])+alpha*sched.raw(zero, one, z, domain[j])-Pj
                assert residual == scale*t**(-h)*evaluate(coeff, t*t)/U
                agreements += residual == zero
                identities += 1
            assert agreements == 2*h
        if found and alpha != zero:
            records.append(dict(sample=list(a), challenge=list(alpha), supports=sorted(found)))

L = sum(comb(127, k) for k in range(67))
R = sum(comb(128, k) for k in range(67))
result = dict(status='passed', p=p, n=n, K=2*m, T=2*h,
    fixed_claim=list(claim), support_count=len(supports), defining_support=base,
    samples=len(samples), queries=queries, successful_queries=successes,
    nonzero_successful_queries=nonzero_successes, recovered_witnesses=witnesses,
    coordinate_identities=identities, left_entries_per_sample=31,
    right_entries_per_sample=57, hash_lookups=lookups,
    elapsed_seconds=time.perf_counter()-start, nonzero_success_records=records,
    m31_left_entries=L, m31_right_entries=R,
    m31_right_entries_log2=log2(R),
    scope='Exhaustive H challenges and eight outside-H controls per deterministic admissible sample; not uniform E challenges, native verification, or a practical M31 decoder.')
out = Path(__file__).with_name('witness_search_results.json')
out.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({k: v for k, v in result.items() if k != 'nonzero_success_records'}, indent=2))
