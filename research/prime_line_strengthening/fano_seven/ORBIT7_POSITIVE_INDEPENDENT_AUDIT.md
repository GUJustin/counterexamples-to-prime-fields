# Independent audit: positive seven-cubic construction

Verdict: PASS. The construction is over the cubic number field K=Q(w), where
w^3+2w^2-w-1=0. The cubic is irreducible by the rational-root test.

`orbit7_independent_field_audit.py` uses an independent implementation of
arithmetic in the basis 1,w,w^2 over Python Fractions. It imports neither
SymPy nor the constructing program. The seven cubic coefficient arrays and
fourteen nodes are transcribed explicitly, and it checks all 91 pairwise
node distinctions and all fourteen exact agreement masks. Each candidate
has exactly seven agreements. Its output records the complete finite affine
certificate, not only a Boolean result.

For affine conversion use X=2+1/T and Q_i(T)=T^3 P_i(2+1/T). None of the
thirteen finite original nodes equals 2: each displayed difference is a
nonzero polynomial of degree less than three in w. The old point at infinity
becomes T=0, with its received value equal to the common leading coefficient
of candidates 3,5,6,7. All other received values are multiplied by T^3.
The independent script verifies the transformed fourteen finite nodes and
all exact masks again. It also verifies seven distinct leading coefficients,
so every pair difference remains a nonzero cubic in this affine chart.

The complete number-field certificate survives reduction at every completely
split prime outside a finite set: exclude the denominators and nonzero
norms of node differences, polynomial differences, and nonagreement values.
Thus it yields examples over arbitrarily large prime fields. The bounded
script `orbit7_prime_realizations.py` additionally verifies all three roots
of the field polynomial at each of eight fixed primes 97,113,127,139,167,
181,223,239. All 24 reductions preserve the exact masks. This finite check
supplements, rather than replaces, the number-field reduction argument.

The nearest degree-at-most-three agreement is exactly seven. Any distinct
candidate with eight agreements would have at least 3*8=24 intersections,
counted across the seven displayed cubics, whereas the pairwise degree bound
allows at most 7*3=21. The displayed candidates themselves have seven. A
possible further candidate with seven agreements would have to agree at
all seven triple nodes and none of the quadruple nodes; the independent five-point test in `orbit7_eighth_independent.py/json`
excludes this possibility. The first three triple targets are zero, so the
candidate is a scalar times their locator. The fourth fixes the scalar to
(1-4w-2w^2)/4; the fifth has nonzero error 486-390w-270w^2.
Consequently the complete degree-at-most-three list at agreement seven is
exactly the seven displayed candidates. This also persists outside finitely
many bad reduction primes.

This audit establishes a fixed seven-member bank on fourteen nodes. It does
not assert an unbounded list, proximity-gap tightness, or a better.codes
improvement.
