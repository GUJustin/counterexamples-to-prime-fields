# A genuine three-dimensional box: exact candidate gate

2026-09-18. Bounded investigation of one candidate: translated integer-box triples (U,V,W), with x²=V/U, g=1/U and f=W/U. The result below is an exact obstruction in the characteristic-zero/no-wrap regime, plus a precise modular escape condition. It does not exclude all three-dimensional constructions at the current smaller field size.

## Candidate and realizability

Take

    U=u0+u, V=v0+v, W=w0+w,
    1≤u,v≤M, 1≤w≤Q,

and retain a set of triples whose nonzero square ratios V/U give evaluation coordinates x. For a fixed ratio there are only two possible coordinates ±x. Consequently a full W-stack is not an evaluation domain: at most two triples for that ratio can be realized with distinct coordinates. One may retain one triple per ratio, or assign different values to the two signs, but the total number of fresh coordinates is at most 2M², independently of Q. Counting M²Q points as distinct evaluations is invalid.

The even bank Pθ=θ+X²/θ has label

    λ=θU+V/θ−W.

The translates u0,v0,w0 affect only a bank-dependent label offset. Fiber multiplicities are governed by integer differences among u,v,w.

## Exact rational-norm obstruction

Use the collision-bank parameters θ²=a/b with distinct primes a,b∈[H/2,H]. If two box triples have the same label for θ, then

    a Δu+b Δv = b θ Δw mod p.

Squaring yields the necessary congruence

    (a Δu+b Δv)²−ab(Δw)² = 0 mod p.             (1)

The integer on the left has absolute value at most H²(4M²+Q²). Therefore if

    p > H²(4M²+Q²),                             (2)

it must be zero as an integer. Since ab is not a rational square, this forces

    Δw=0,       a Δu+b Δv=0.

This is also the exact conclusion over characteristic zero without a field-size condition: the rational and irrational components in the label equation separate.

Thus every bank fiber lies in a SINGLE W-layer, and its (u,v) points run along the old primitive direction (b,−a). The number of such grid pairs is at most 1+2M/H. Allowing both coordinate signs multiplies this by at most two. In particular the extra box direction does not increase the certified fresh agreement beyond O(M/H); with M=O(L), it cannot turn the present gap L/H into a constant fraction of L.

The conclusion holds for arbitrary selections of W within the box and arbitrary ratio-deduplication rules. It does not require random W, generic coefficients, or a root-count heuristic.

## Nonbank control also costs a growing W range

Unlike constant W, arbitrary W selections need not satisfy the old two-roots-per-U outsider bound. A safe replacement is to fix BOTH U and W. For a nonconstant quadratic P, the equation

    U P(x)=W+λ

has at most two roots. Summing over M rows and Q W-values gives at most 2MQ fresh matches. A nonzero constant has at most Q matching rows and at most 2M coordinates per row, giving the same bound. The zero polynomial is exceptional at each of the Q labels λ=−(w0+w); these must be treated separately.

For the regular collision core A~3L/2 and outsider core bound L, choosing M≤L/(16Q) preserves a uniform outsider bound <A after neutral padding. Under this sufficient certificate and (2), the possible fresh fiber multiplicity is only O(L/(HQ)). Increasing Q worsens rather than improves this certified gap. This is a limitation of this explicit box-plus-root-count ledger, not a proof that every special W-selection must obey its crude outsider upper bound tightly.

## What remains possible at the existing field size

The current constant-fraction construction has p=Θ(HM²), whereas (2) asks roughly H times more when Q≤M. Hence the no-wrap obstruction DOES NOT close the actual current-field candidate. At that smaller p, every genuinely new cross-W coincidence must exhibit a nonzero integer multiple of p in (1). Equivalently the modular relation lattice

    Λθ={(u,v,w)∈Z³ : a u+b v−bθw=0 mod p}

must contain a short vector with w≠0, in addition to its known vector (b,−a,0). The norm calculation gives the necessary Euclidean-scale lower bound Ω(sqrt(p)/H) for such a vector, but this is compatible with the current box dimensions. A useful positive construction would have to organize these modular vectors for many banks, preserve distinct coordinates, and control all nonbank quadratics simultaneously. None of those follows from simply adding a third box coordinate.

## Affine surfaces are still planar

For comparison, if W=cU+dV+c0, then f=c+d x²+c0 g. Subtracting the common quadratic c+dX² from both received word and bank reduces the fresh block to W=c0. This is an exact codeword-translation reduction to a planar incidence problem with a translated bank. It is not a proof that every such translated bank has identical arithmetic fiber bounds, so no stronger global exclusion is inferred.

## Route decision

A characteristic-zero lift or a very-large-prime realization of a three-dimensional integer box cannot improve the gap: its fibers stay in individual W-layers. The possible escape at p~HM² is genuinely modular and requires new lattice relations, while arbitrary W choices lose the clean outsider bound unless additional structure is supplied. This note supplies a discriminating algebraic target, not a new larger-gap theorem or a general obstruction to nonconstant f/g. No computation or manuscript edit was performed.
