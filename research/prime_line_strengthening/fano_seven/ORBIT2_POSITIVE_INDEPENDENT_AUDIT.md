# Independent audit of the second positive seven-cubic bank

Verdict: PASS. `orbit2_independent_field_audit.py` implements exact rational
arithmetic in Q(q), q^3-10q^2+3q+1=0, independently of the constructing
SymPy program. The cubic has no rational root. An exact AST parser reads
polynomial expressions without floating-point constants. The verification
subtracts the common first polynomial and multiplies by221646235, an
invertible normalization, to simplify coefficients.

All fourteen projective nodes are distinct, every displayed triple and
quadruple mask is exact, and each of the seven distinct cubics has seven
matches. The affine transformation X=2+1/T is legal and all fourteen affine
masks are rechecked. Full affine data is exported in
`orbit2_independent_field_audit.json`.

The complete cubic list is exactly seven. The pair-count argument forces
any eighth candidate to match all seven triple coordinates. Interpolation
through the first four such affine coordinates already fails at the fifth:
the exact error is

    (-4586458734 -22669168074 q +1962753873 q^2)/125,

which is nonzero in the irreducible cubic field.

The immediate one-pole extension also fails. `orbit2_one_pole.py` applies
the complete algorithm proved in ONE_POLE_COMPLETE_TEST.md to all3432
seven-node supports. It finds no proper numerator-degree-at-most-four
finite pole off the domain, and no degree-four polynomial with seven
matches (the pole-at-infinity case). The result covers coefficient-field
extensions too, by the five-point interpolation formula. The bounded run
completed in2.17seconds with less than14MiB RSS.

These are statements about this second explicit bank. The finite
construction remains positive and transfers to arbitrarily large split
prime fields; the one-pole exclusion does not rule out other extension
operations or other seven-word banks.
