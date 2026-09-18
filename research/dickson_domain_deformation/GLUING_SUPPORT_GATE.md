# What the smooth p17 seed permits under block gluing

The known smooth seed has n=16, dimension k=4, and eight distinct
nearest candidates, each with six prescribed agreements. Its exact
nearest profile and characteristic-zero lift are established in
`EXACT_PROFILE.md`. This note gives a different, elementary obstruction
to independently amplifying its bank. It does not rule out correlated
constructions or a new family with structured incidence dependencies.

## Exact support data

`verify_gluing_support_gate.py` reconstructs the eight supports directly
from the binomial polynomials over F17 and saves all 28 pair intersections
in `verify_gluing_support_gate.json`. Twenty intersections have size two,
four have size three, and four have size one. Every support has size six.
Candidate labels here are a=1,...,8, representing the eight square
parameters, rather than an ordering inferred from another artifact.

## Independent product obstruction

Take B disjoint copies of these 16 labeled nodes. Suppose every tuple
in {1,...,8}^B is represented by a distinct polynomial of degree at most
4B-1, and agrees with one common word on the union of the six selected
nodes in each block. This is the natural full Cartesian amplification
at rate 1/4 and agreement 3/8.

Choose two tuples equal in B-1 blocks, and differing in the final block
by a pair whose support intersection has size three. Their polynomials
agree with each other on at least

    6(B-1)+3 = 6B-3

distinct nodes. Their nonzero difference has degree at most 4B-1. Thus
6B-3 <= 4B-1, or B<=1. Every B>=2 is impossible over every field.

This argument does not assume CRT interpolation, linear gluing, or any
specific formula for the global polynomials. It applies to any smoothing
whose final distinct nodes retain these incidence patterns. Fat-point
jet agreement alone is not a replacement for exact agreement on the
eventual distinct nodes.

## The precise escape left for correlated tuples

For labels a,b define w(a,b)=6-|S_a intersect S_b|. Equal labels have
weight zero; unequal labels have weight three, four, or five. A selected
tuple bank C can be realized by distinct polynomials of degree <=4B-1
with the prescribed supports only if every distinct a,b in C satisfies

    sum_j w(a_j,b_j) >= 2B+1.

Indeed their shared prescribed agreements number exactly 6B minus the
left side, and cannot exceed 4B-1. This is only a necessary condition.
Constructing a large outer code with this distance would not establish
polynomial realizability, exact nearestness, or a characteristic-zero
lift. No outer-code search was performed.

The existing full-row Jacobian limit is a separate issue. With n=16B,
k=4B and A=6B, that sufficient lifting criterion requires

    L <= (2n-k-4)/(A-k) = 14-2/B.

See `FULL_ROW_LIFT_LIMIT.md` and `SMOOTHNESS_METHOD_LIMIT.md`. This does
not say the reduced realization variety is singular: redundant equations
can describe a smooth variety. A growing correlated bank would require
controlled dependencies or a different lifting argument, rather than
full row rank of the uncompressed incidence equations.

## Outcome

The existing covering/composition construction preserves list size eight
and does not amplify it; the quadratic tower profile already records
that fact. Independent block multiplication is ruled out above. The
remaining positive target is an algebraically realizable correlated
support family with the displayed weighted distance and compatible
equation dependencies. This bounded investigation supplies no such
family and makes no new lower-bound claim.
