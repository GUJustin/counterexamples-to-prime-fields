#!/usr/bin/env python3
"""Finite checks only; the accompanying note gives the general proof."""
import hashlib
import json
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
from random import Random

P, N, T, TRIALS, SEED = 11, 9, 4, 30, 1909
D = list(range(N))
R = Fraction((N-1)*(T-2), (T-1)**2-(N-1))
b = Fraction(T*T, N)-1
rng = Random(SEED)
cases = 0
list_sizes = []
triangle_count = 0
involutions = [v for v in product(range(P), repeat=3)
               if any(v) and next(x for x in v if x) == 1
               and (v[1]*v[1]-v[0]*v[2]) % P != 0]
assert len(involutions) == 121
for trial in range(TRIALS):
    # Sample words, exhaustively enumerate all quadratic polynomials for each.
    f = [rng.randrange(P) for _ in D]
    qs = []
    for A, B, C in product(range(P), repeat=3):
        matches = [x for x in D if (A*x*x+B*x+C-f[x]) % P == 0]
        if len(matches) >= T:
            qs.append(((A,B,C), set(matches[:T])))
    list_sizes.append(len(qs))
    for alpha, beta, gamma in involutions:
        h, groups = {}, {}
        for x, y in combinations(D, 2):
            if (alpha*x*y+beta*(x+y)+gamma) % P:
                continue
            # Native pairs have neither pole nor infinity. Include beta=0.
            assert (alpha*x+beta) % P != 0
            assert (alpha*y+beta) % P != 0
            assert (-(beta*x+gamma)*pow(alpha*x+beta,-1,P)-y) % P == 0
            lam = (-beta-alpha*y)*pow(x-y,-1,P) % P
            mu = (alpha-lam) % P
            assert lam and mu
            assert (lam*x*x+mu*y*y-gamma) % P == 0
            tau = (lam*f[x]+mu*f[y]) % P
            h[tau] = h.get(tau,0)+1
        assert sum(h.values()) <= N//2
        for q, S in qs:
            A,B,C = q
            tau = (gamma*A-beta*B+alpha*C) % P
            groups.setdefault(tau,[]).append((q,S))
        total = Fraction(0)
        for tau, items in groups.items():
            r, ht = len(items), h.get(tau,0)
            assert b*r*r-(T-1)*r <= ht*R*(R-1)
            H = 0
            for (_,S1),(_,S2),(_,S3) in combinations(items,3):
                pairs = [S1&S2,S2&S3,S3&S1]
                if all(len(s)==2 for s in pairs) and len(set.union(*pairs))==6:
                    H += 1
            assert H <= ht*(ht-1)*(ht-2)//6
            triangle_count += H
            total += max(0,b*r*r-(T-1)*r)
        assert total <= (N//2)*R*(R-1)
        cases += 1
assert cases == 3630
here = Path(__file__).resolve().parent
note = here/'FIXED_INVOLUTION_PARALLEL_PLANE_PACKING.md'
receipt = {
    'status':'PASS', 'field_prime':P, 'domain':D, 'threshold':T,
    'received_words_sampled':TRIALS, 'python_random_seed':SEED,
    'quadratics_exhausted_per_word':P**3,
    'projective_involutions_exhausted_per_word':len(involutions),
    'word_involution_cases':cases,
    'selected_support_rule':'First T matching coordinates in ascending order; not all support choices.',
    'list_sizes':list_sizes, 'six_root_triangles_counted':triangle_count,
    'scope':'Finite checks; sampled received words, exhaustive quadratics and involutions for each word. Not an exhaustive proof over words or support choices.',
    'note_sha256':hashlib.sha256(note.read_bytes()).hexdigest(),
    'verifier_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
output = here/'fixed_involution_packing_receipt.json'
output.write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
