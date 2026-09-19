# Independent audit: prime-power norm-one subplanes and descent

2026-09-19. Outcome: PASS for the finalized proof note and exact fixture.
No manuscript changes, new benchmark result, or literature novelty claim.

## Prime-power transfer and complete lists

Checked the original two-bank proof as well as the final note. Replacing
p-Frobenius by Q-Frobenius is valid for every odd prime power Q=ell^r:
the semilinear map has third iterate the identity on E=F_(Q³), derivatives
use ell|Q, and the quartic/square classification divides only by nonzero
quantities and 2. It does not require ell=Q or ell>3. At ell=3 the
second bank is still valid; its separation from the at-most-four remainder
requires Q>=5, as stated. The nearest-bank completion follows separately
from the exact Johnson bound, so no exhaustive polynomial census is needed.
The upper comparison based on shortening is characteristic-free. The note
correctly warns that an unrelated characteristic guard must use ell, not Q.

The trace identity is exact: multiplying the agreement equation by
 d^(Q²−1)u yields d^(-1)Tr(du). Scaling u or d by F_Q* has the stated
invariance, and the parameter-to-polynomial map is injective on projective
classes because its kernel is F_Q*. Trace-dual bases exist also in
characteristic three, where Tr(1)=0 but the trace pairing remains
nondegenerate. Restricting coefficient triples to F_q gives an injective
projective subplane, not a potentially collapsing naive subfield map.

Each selected quadratic has exactly 2(q+1) matches on 2(q²+q+1) points.
The already exhibited q²+q+1 polynomials saturate the ordinary Johnson
count and therefore constitute the complete nearest list, including over
larger coefficient fields. The stronger outsider bound is valid: each
matching coordinate belongs to q+1 bank supports, while an outsider can
intersect each bank support in at most two roots of a nonzero quadratic.
Thus (q+1)agr<=2(q²+q+1), whose integer consequence is agr<=2q.
This does not imply the full native two-bank classification after puncturing;
the note correctly avoids that inference at threshold ceil(19q/10).

## Native field intersections

The common-field calculation E intersect F_(ell^m)=F_(ell^g),
g=gcd(3r,m), is correct. With d=gcd(r,m), either g=d or g=3d, according
to the stated comparison of 3-adic valuations. In the first case the
cubic norm restricts to x³ on the common field, giving the gcd(3,ell^d−1)
and gcd(6,ell^d−1) counts. In the second case r/d is prime to 3, so the
three Q-Frobenius conjugates permute the three ell^d-Frobenius conjugates.
The norm restrictions consequently have kernels of size ell^(2d)+ell^d+1,
and the preimage of {±1} has twice that size. This proves the formula
independently of the finite integer checks. The conclusions for extension
degrees 1,2,4,5 and 6 have the stated scope and do not presume E embeds
in the target field.

## Affine and projective descent, including infinity

The two-point affine and three-point projective normalizations are valid
even when the proposed map initially has coefficients in the algebraic
closure: maps normalized on the same two or three points coincide, forcing
all normalized coordinates into the intersection field. This field lies
inside F_Q in the regime under discussion.

For an affine parametrization, the squared norm minus one is a genuine
degree-six polynomial with nonzero leading coefficient, hence at most six
roots. For a projective parametrization with at least seven selected points,
the homogeneous degree-six identity vanishes identically. Odd characteristic
then makes the norm cubics proportional with sign ±1. Equality of their
root multisets excludes a zero numerator or denominator slope and forces
phi=kappa(t−u)/(t−u^Q) or kappa(t−u)/(t−u^(Q²)), where u has degree three
over F_Q and Norm(kappa)=±1.

The two displayed received-word transformations are correct under the
ordinary degree-two action (ct+d)² f(phi(t)). In the first orientation,
subtracting any quadratic gives a binary quartic that is nonzero by
evaluation at u^(Q²); hence the agreement bound is four, including infinity.
The denominator has no zero on the common-field projective line. In the
second orientation the transformed word is exactly C(t−u^Q)². Both
identities have leading section value C at infinity. The inverse degree-two
action gives an original quadratic agreeing on the selected source set;
all other quadratics have at most two agreements there.

Consequently a projectively descended set of at least seven points cannot
retain two distinct quadratics with five or more matches. The complete
subplane bank is therefore excluded from that descent route. This argument
uses the standard degree-two action, not arbitrary GRS column multipliers,
nonlinear maps, or replacement received words; the final note explicitly
states those limitations.

## Exact fixture replay

Read and independently replayed verify_norm_one_prime_power_subplane.py:
PASS. It verifies the irreducible modulus T^6+T+2 over F3 (including the
Rabin degree-six test), the Q=9 native bank, and the proper q=3 subplane.
Results: native 182 coordinates, 91 polynomials, 20 agreements; subplane
26 coordinates, 13 polynomials, 8 agreements; 169 trace checks; coordinate
incidence four and pair intersections two. Both projective orientations
are checked on all nine finite parameters and infinity. All 576 integer
intersection-formula checks pass. This is an exact small fixture, not a
quadratic census or proof by parameter sampling.

## Artifact hashes

SHA256 values of the audited final files:

- `NORM_ONE_PRIME_POWER_SUBPLANE_AND_FIELD_GATE.md`: `6ef6902aa47df9b05a53f0d8ace32293e1cd54c05eba54d5ea917bd1502ad47e`
- `verify_norm_one_prime_power_subplane.py`: `a75a495e5a491d6c5f46efad02fc369dfa03efa9314a5f325ffec90fec54df7f`
- `verify_norm_one_prime_power_subplane.json`: `13b6075614705fd1277f359f932451d4f57087d9dc3c35ea500df2aa32d05ea8`
- `verify_norm_one_prime_power_subplane.resources.json`: `2617664f2f7778c918e8df65ade46df8a14bd1f63d046a350b6c947c5bfea837`
