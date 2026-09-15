#!/usr/bin/env python3
"""M31 canonical-coset check of the source schedule and codeword backgrounds."""
from pathlib import Path
import json
import verify_fixed_claim as ff
import verify_scheduled_transfer as sched

ff.P = 2**31-1
ff.inverse.cache_clear()
F = ff.F
p = ff.P
zero, one, w = F(0), F(1), F((0, 0, 1, 0))
n = 8
generator = F((2, 1268011823, 0, 0))
rotation = generator**((p+1)//(2*n))
step = rotation*rotation
assert rotation**(2*n) == one and rotation**n == -one
us = [rotation*step**j for j in range(n)]
domain = [sched.circle(u) for u in us]
assert len(set(domain)) == n
assert all(x[1:] == (0, 0, 0) and y[1:] == (0, 0, 0) for x, y in domain)
c = domain[0][0]
second = [x-c for x, _ in domain]
nonzero_positions = [j for j, v in enumerate(second) if v != zero]
assert len(nonzero_positions) == 6
f = [zero]*n
for j in nonzero_positions[:3]:
    f[j] = second[j]
assert sum(v == zero for v in f) == 5
assert sum(v == b for v, b in zip(f, second)) == 5

# Select one claim and keep it fixed across every test sample and challenge.
a0 = (one+w)/(one-w)
challenge0 = F((1, 1, 0, 0))
fixed_claim = sched.circle(a0)[0]-c-challenge0-challenge0**3
samples = [a0, F((7, 11, 13, 17)), F((3, 5, 7, 9)), F((11, 1, 3, 2))]
challenges = [zero, one, challenge0, F((7, 11, 13, 17)), F((3, 5, 7, 9)), -one]
identities, agreements = 0, 0
for a in samples:
    assert sched.admissible(a) and sched.admissible(step*a)
    z, zprev = sched.circle(a), sched.circle(step*a)
    # A third column carries x and claims its true value z.x.
    # Its normalized raw quotient is the constant codeword 2.
    columns = [[(z, fixed_claim)], [(zprev, zero), (z, one)], [(z, z[0])]]
    terms = sched.power_schedule(columns)
    assert [e for _, _, _, e in terms] == [0, 1, 2, 3, 4]
    for j, pt in enumerate(domain):
        q0 = sched.raw(f[j], fixed_claim, z, pt)
        q1 = sched.raw(zero, one, z, pt)
        background = sched.raw(pt[0], z[0], z, pt)
        assert background == F(2)
        for challenge in challenges:
            values = [f[j], zero, pt[0]]
            actual = sum((challenge**e*sched.raw(values[col], claim, point, pt)
                          for col, point, claim, e in terms), zero)
            expected = q0+(challenge+challenge**3)*q1+F(2)*challenge**4
            assert actual == expected
            identities += 1
            if a == a0 and challenge == challenge0:
                # F_1=x-c has quotient witness 2. Add background 2 alpha^4.
                agreements += int(actual == F(2)+F(2)*challenge**4)
assert agreements == 5
result = dict(status='passed', p=p, n=n, canonical_coset=True,
    fixed_claim=list(fixed_claim), sample_fixtures=len(samples),
    challenges_per_fixture=len(challenges), coordinate_schedule_identities=identities,
    nonzero_label_witness_agreements=agreements,
    added_codeword='2 alpha^4',
    scope='Exact M31 model of pinned raw quotient schedule; not native Stwo execution.')
Path(__file__).with_name('m31_schedule_results.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
