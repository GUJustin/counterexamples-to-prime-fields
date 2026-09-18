# Independent eleven-cubic and node-exchange audit

## Complete eleven-cubic construction: PASS

`verify_eleven_cubic.py` reuses the independently assembled Fraction/Newton list of all 1,516 old four-point interpolants, not the generator's FLINT interpolation. It checks the two rational nodes −80/163 and −135/262 and the third node defined by

    U²+(4175/3826)U+4525/15304=0.

The discriminant is 55²·39/3826², proving irreducibility and separability. All three nodes are fresh. The prescribed pairwise agreements of the promoted fresh-five cubics Q0,Q2,Q5 hold exactly. Independent polynomial remainders reproduce the nonrational-node word

    3162975/29276552 + (1437663/7319138)U.

The complete old-interpolant agreement histogram on the nineteen-node word is {4:1499,5:6,7:11}. Any cubic with seven matches must match at least four of the original sixteen rational nodes, and hence is one of these rational interpolants, even if competitors are allowed arbitrary algebraic coefficients. Thus maximum agreement seven and complete nearest list eleven are established. The exact degree-thirteen low-branch positivity gap 4666871/1343677407241 is also independently verified at rho=40/247, a=7/19. The receipt is `eleven_cubic_certificate.verified.json`.

## No fresh six-match cubic for either fixed ten- or eleven-word seed

`node_exchange_probe.py/json` gives a complete exact bounded test, not a field scan.

For the ten-word eighteen-node source, a six-match cubic must match at least four rational old nodes. Hence it is rational and belongs to the same exhaustive 1,516-interpolant list. Matching one of the two added conjugate roots is equivalent to matching both, by irreducibility of their quadratic. Exact remainder evaluation finds no fresh six-match cubic (and the only cubics with more matches are the known ten).

For the eleven-word nineteen-node source, the rational interpolant census already has no six-match cubic. A nonrational cubic with six or more matches cannot match four rational old nodes. It must therefore match exactly three old nodes and all three added nodes. Interpolating through the three added nodes and each one of the sixteen old nodes gives a complete set of sixteen potential nonrational cases. Independent arithmetic in Q(sqrt(39)) shows that every one of these interpolants matches exactly one old node, so none has six matches. The same argument includes competitors over the algebraic closure, since any such cubic is determined by these four points in Q(sqrt(39)).

Consequently, deleting one existing coordinate and appending one new coordinate, while retaining all other received values and retaining the incumbent polynomials, cannot introduce a fresh seven-match cubic into either fixed seed. A fresh candidate would need at least six matches on the retained old coordinates and thus on the original word. This does not exclude deformation of nodes/word values, changing incumbent polynomials, or exchanging more than one coordinate.

## Scope of the three-coordinate promotion optimum

`verify_fresh_triple_gcd.py` independently checks all fifty-six triples of the eight fresh FIVE-match cubics. Every common root of Qi−Qj and Qi−Qk is an old source node; after old factors are removed, the gcd is constant. No three leading cubic coefficients coincide, so infinity is not a fresh triple-agreement point. Thus any added coordinate contributes at most two hits among these eight cubics, and three coordinates can promote at most three of them (each requires two hits). The constructed triangle attains this restricted optimum.

This does not by itself prove unrestricted optimality of all three-coordinate padding of the source. A cubic with four old matches could potentially gain three new matches; such cubics are outside that eight-candidate triple-gcd census. A manuscript optimality statement must retain the explicit restriction to promotion of the eight fresh five-match cubics, or omit the claim.
