#!/usr/bin/env python3
"""Exhaustive first-layer reconstruction model, not a native FRI test."""
from fractions import Fraction
from itertools import product
from math import log2
from pathlib import Path
import hashlib
import json

N = 8
P = [2]*N  # A genuine constant codeword in every relevant polynomial space.
agreements = {0, 2, 3, 5, 7}
R = [P[j] if j in agreements else 3 for j in range(N)]
rows = []
for fold_step in [1, 2, 3]:
    accepted = 0
    uses_disagreement_complement = 0
    for ordered_queries in product(range(N), repeat=3):
        queries = sorted(set(ordered_queries))
        blocks = sorted({j >> fold_step for j in queries})
        positions = [j for block in blocks
                     for j in range(block << fold_step, (block+1) << fold_step)]
        witness = iter(P[j] for j in positions if j not in queries)
        rebuilt = [R[j] if j in queries else next(witness) for j in positions]
        assert next(witness, None) is None
        # Exact equality models authentication against the committed vector P.
        valid = rebuilt == [P[j] for j in positions]
        assert valid == all(j in agreements for j in ordered_queries)
        if valid:
            accepted += 1
            uses_disagreement_complement += any(j not in agreements for j in positions)
    assert accepted == 5**3 == 125
    assert Fraction(accepted, N**3) == Fraction(5, 8)**3
    assert uses_disagreement_complement > 0
    rows.append(dict(fold_step=fold_step, query_tuples=N**3, accepted=accepted,
                     accepted_with_disagreement_in_block=uses_disagreement_complement))

base = Path(__file__).parent
earlier = json.loads((base/'scheduled_transfer_results.json').read_text())
raw = earlier['large_instance']['power_gap_rows'][-1]
assert raw['power_gap'] == 10
p = 2**31-1
factor = Fraction(33, 128)**70
joint = Fraction(raw['pairs'], p**8)*factor
source_root = Path('/Users/jthaler/Documents/stwo_audit_2026-09-15/repositories/proving_zk')
paths = ['crates/stwo/src/core/fri.rs', 'crates/stwo/src/core/queries.rs',
         'crates/stwo/src/prover/fri.rs']
result = dict(status='passed', cases=rows,
    query_factor_numerator=factor.numerator, query_factor_denominator=factor.denominator,
    query_factor_bits=-log2(factor), joint_sufficient_event_bits=-log2(joint),
    joint_numerator=joint.numerator, joint_denominator=joint.denominator,
    source_commit='cd7bc5f4697fb188a27e09f9242f1dd76df8afdc',
    source_hashes={path:hashlib.sha256((source_root/path).read_bytes()).hexdigest() for path in paths},
    scope='Conditional reconstruction and independent-query probability; no native verifier or attack work estimate.')
(base/'query_survival_results.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
