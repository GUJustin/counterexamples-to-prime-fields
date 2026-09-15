#!/usr/bin/env python3
"""Count an exponential support bank implicitly and construct its real table.

No claim-search or full-proof algorithm is supplied. Output is a finite explicit
M31 table, the exact bank count, and one checked generic-sample quotient witness.
"""
from itertools import combinations
from math import comb
from pathlib import Path
import hashlib
import json
import time
import verify_fixed_claim as ff
import verify_scheduled_transfer as sched

ff.P = 2**31-1
ff.inverse.cache_clear()
F = ff.F
p, n, M, m, h = ff.P, 512, 256, 64, 66
zero, one, i = F(0), F(1), F((0, 1, 0, 0))


def count_bank():
    counts = [[0]*M for _ in range(h+1)]
    first_support = [[None]*M for _ in range(h+1)]
    counts[0][0], first_support[0][0] = 1, 0
    start = time.perf_counter()
    updates = 0
    for j in range(1, M):
        for k in range(min(h, j), 0, -1):
            for residue in range(M):
                previous = (residue-j) % M
                addition = counts[k-1][previous]
                if addition:
                    if counts[k][residue] == 0:
                        first_support[k][residue] = first_support[k-1][previous] | (1 << j)
                    counts[k][residue] += addition
                updates += 1
    assert sum(counts[h]) == comb(M-1, h)
    residue = max(range(M), key=lambda r: (counts[h][r], -r))
    support = [j for j in range(1, M) if first_support[h][residue] & (1 << j)]
    assert len(support) == h and sum(support) % M == residue
    return counts[h], residue, support, updates, time.perf_counter()-start


def polynomial(roots):
    coefficients = [one]
    for root in roots:
        nxt = [zero]*(len(coefficients)+1)
        for j, value in enumerate(coefficients):
            nxt[j] -= value*root
            nxt[j+1] += value
        coefficients = nxt
    return coefficients


def evaluate(coefficients, x):
    result = zero
    for value in reversed(coefficients):
        result = result*x+value
    return result


def divide_exact(numerator, denominator):
    work = numerator[:]
    quotient = [zero]*(len(work)-len(denominator)+1)
    for j in reversed(range(len(quotient))):
        coefficient = work[j+len(denominator)-1]/denominator[-1]
        quotient[j] = coefficient
        for k, value in enumerate(denominator):
            work[j+k] -= coefficient*value
    assert all(value == zero for value in work)
    return quotient


counts, residue, base_support, updates, seconds = count_bank()
bank_size = counts[residue]
assert bank_size >= (comb(M-1, h)+M-1)//M
# Independent roots-of-unity filter: verify every count against Ramanujan sums.
character_coefficients = {d: (-1)**(h//d)*comb(M//d-1, h//d)
                          for d in [2, 4, 8, 16, 32, 64, 128, 256]}
for r in range(M):
    numerator = comb(M-1, h)
    for d, coefficient in character_coefficients.items():
        ramanujan = d//2 if r % d == 0 else (-d//2 if r % (d//2) == 0 else 0)
        numerator += ramanujan*coefficient
    assert numerator % M == 0 and numerator//M == counts[r]
assert bank_size == (comb(255, 66)+comb(127, 33))//256
assert sum((d//2)*abs(value) for d, value in character_coefficients.items() if d >= 4) < 2*comb(127, 33)
assert sum(count == bank_size for count in counts) == 128
assert base_support == sorted(set(range(2, 69))-{40})
generator = F((2, 1268011823, 0, 0))
rotation = generator**((p+1)//(2*n))
step = rotation*rotation
fiber_generator = step*step
assert rotation**(2*n) == one and rotation**n == -one
assert fiber_generator**M == one and fiber_generator**(M//2) != one
constant = fiber_generator**residue  # h is even, so (-1)^h=1.
scale = one+one/constant if constant != -one else i
assert scale != zero and scale**p/scale == constant
base_poly = polynomial([fiber_generator**j for j in base_support])
assert base_poly[0] == constant and base_poly[-1] == one

# Produce two further explicit supports by replacing pairs of equal modular sum.
outside = sorted(set(range(1, M))-set(base_support))
outside_pairs = {}
for pair in combinations(outside, 2):
    outside_pairs.setdefault(sum(pair) % M, []).append(pair)
supports = [base_support]
for pair in combinations(base_support, 2):
    for replacement in outside_pairs.get(sum(pair) % M, []):
        candidate = sorted((set(base_support)-set(pair)) | set(replacement))
        assert len(candidate) == h and sum(candidate) % M == residue
        supports.append(candidate)
        if len(supports) == 3:
            break
    if len(supports) == 3:
        break
assert len(supports) == 3
polynomials = [polynomial([fiber_generator**j for j in support]) for support in supports]
assert all(poly[0] == constant and poly[-1] == one for poly in polynomials)

relative_domain = [step**j for j in range(n)]
domain = [sched.circle(rotation*u) for u in relative_domain]
table = [scale*u**(-h)*evaluate(base_poly, u*u) for u in relative_domain]
assert all(value[1:] == (0, 0, 0) for value in table)
assert all(x[1:] == (0, 0, 0) and y[1:] == (0, 0, 0) for x, y in domain)

# For each support, u^m F_U is an even degree-at-most-128 polynomial.
Fs = []
for poly in polynomials:
    diff = [scale*(a-b) for a, b in zip(base_poly, poly)]
    assert diff[0] == diff[-1] == zero
    centered = [zero]*(2*m+1)
    for k, coefficient in enumerate(diff[1:-1]):
        centered[2*k] = coefficient
    Fs.append(centered)
    agreements = sum(table[j] == u**(-m)*evaluate(centered, u)
                     for j, u in enumerate(relative_domain))
    assert agreements == 132

# A generic physical sample and one fixed claim for a nonzero cubic label.
physical_a = F((7, 11, 13, 17))
assert sched.admissible(physical_a) and sched.admissible(step*physical_a)
a = physical_a/rotation
z = sched.circle(physical_a)
beta = a**(-m)*evaluate(Fs[1], a)
challenge = F((1, 1, 0, 0))
phi = challenge+challenge**3
claim = beta-phi
X0, X1 = ff.parts(z[0])
Y0, Y1 = ff.parts(z[1])
slope = X1/Y1
denominator = [(one-i*slope)/(4*rotation), (-X0+slope*Y0)/2,
               (one+i*slope)*rotation/4]
assert evaluate(denominator, a) == zero
B0, B1 = ff.parts(beta)
ell_slope = B1/Y1
ell = [-ell_slope/(2*i*rotation), B0-ell_slope*Y0, ell_slope*rotation/(2*i)]
numerator = Fs[1][:]
for j, value in enumerate(ell):
    numerator[m-1+j] -= value
witness = divide_exact(numerator, denominator)
assert len(witness) == 2*m-1
assert all(value[2:] == (0, 0) for value in witness)
agreements, checked = 0, 0
for j, u in enumerate(relative_domain):
    q0 = sched.raw(table[j], claim, z, domain[j])
    q1 = sched.raw(zero, one, z, domain[j])
    Pj = u**(1-m)*evaluate(witness, u)
    U = evaluate(denominator, u)/u
    expected_residual = scale*u**(-h)*evaluate(polynomials[1], u*u)/U
    assert q0+phi*q1-Pj == expected_residual
    agreements += int(q0+phi*q1 == Pj)
    checked += 1
assert agreements == 132

artifact = dict(field=p, n=n, K=2*m, T=132,
    canonical_rotation=list(rotation), canonical_step=list(step),
    support_modulus=M, support_size=h, chosen_residue=residue,
    support_count=bank_size, residue_counts=counts,
    explicit_supports=supports, scaling_constant=list(scale),
    table_in_canonical_coset_order=[value[0] for value in table],
    fixture=dict(physical_circle_parameter=list(physical_a), fixed_claim=list(claim),
                 batching_challenge=list(challenge), normalized_witness_coefficients=[list(v) for v in witness],
                 witness_laurent_shift=1-m, coordinate_identities=checked, agreements=agreements),
    limits='The fixed claim here verifies one selected sample/challenge; it is NOT identified as the favorable claim from the averaging theorem.')
out = Path(__file__).parent
artifact_path = out/'explicit_m31_bank.json'
artifact_path.write_text(json.dumps(artifact, indent=2)+'\n')
summary = dict(status='passed', n=n, K=2*m, T=132, exact_bank_size=bank_size,
    residue=residue, explicit_table_entries=len(table),
    dp_integer_updates=updates, dp_elapsed_seconds=seconds,
    independent_character_filter_counts=256, maximizing_residues='all 128 odd residues',
    witness_identities=checked, fixture_agreements=agreements,
    artifact_sha256=hashlib.sha256(artifact_path.read_bytes()).hexdigest(),
    scope='Efficient construction of the fixed table and implicit bank; no favorable-claim search or full proof.')
(out/'explicit_m31_bank_summary.json').write_text(json.dumps(summary, indent=2)+'\n')
print(json.dumps(summary, indent=2))
