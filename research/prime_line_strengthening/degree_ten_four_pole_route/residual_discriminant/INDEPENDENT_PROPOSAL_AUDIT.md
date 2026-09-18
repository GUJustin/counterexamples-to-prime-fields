# Independent audit of the residual-discriminant proposal

The mathematical necessary condition and triangular reconstruction algorithm pass, with precisely the open guards stated in `PROPOSAL.md`. This audit performs no new discriminant computation and does not certify that the proposed subresultant locus is empty or nonempty.

## Degree and divisibility

For a degree-ten polynomial in Y, the discriminant is homogeneous of coefficient degree18 and weighted coefficient-index degree90. Since coefficient a_j has X-degree at most34-3j, its X-degree is at most18*34-3*90=342. Its parameter degree is at most18 on the affine parameter chart.

On the nonempty dense open set where each prescribed point is ordinary and its tangent directions are nonvertical, its m smooth local branches have pairwise intersection at least one. Their discriminant contribution is at least m(m-1). Thus the fixed factors of exponents12 and30 divide the universal discriminant on that open set. Division by the monic fixed polynomial T is valid over the parameter ring; the remainder coefficients vanish on a dense open set and hence identically. Divisibility therefore persists even at parameter exceptions where the degree drops, a leading coefficient vanishes, or the whole discriminant becomes zero. The total removed degree is7*12+7*30=294, leaving degree at most48 without increasing parameter degree.

## Boundary and genus accounting

The guards are essential, not cosmetic. At a simple zero of the leading coefficient B with Y9 coefficient C nonzero, the reciprocal chart is B+Cq+..., so its infinity branch is smooth and X-unramified. The powers of B in the polynomial discriminant cancel the escaping root's poles; it contributes no extra discriminant order. The other nine finite branches are locally represented by a unit-leading polynomial, so the usual different-plus-twice-index formula applies.

At X=infinity, the weighted chart t^34 F(1/t,Z/t³) has ten distinct roots and nonzero degree-ten coefficient by hypothesis. All ten branches are X-unramified. Equivalently the discriminant leading term is nonzero of degree342: leading-coefficient degree4 contributes18*4=72 and root-difference scaling contributes3*90=270.

For an irreducible rational normalization the X-map has degree10. In characteristic zero, or characteristic29, its total different is18 by Riemann--Hurwitz; in characteristic29 it is tame because all ramification indices are at most10. The selected branches are assumed smooth and X-unramified, but may have coincident tangents. Their index contribution is at least147; any extra tangency remains in the residual index. Other ramification in the same X fibers is retained as well. Removing T therefore gives a residual discriminant of degree48 whose summed excess normalization index is15.

Locally its exponent is e=2k+r with k,r nonnegative. For k≥1, e-1≥k; for k=0 the desired lower bound is zero. The derivative gcd contributes at least e-1, and contributes even more if the characteristic divides e. Summing yields degree gcd(D,D_X)≥15. In particular, repeated tangents do not invalidate the bound, while a ramified selected branch or an exceptional boundary point requires a separate stratum.

## Reconstruction code

On the chart F0+sF1+tF2, the Y10 coefficient has the nonzero constant term25, so every evaluation still has degree ten in Y. A zero discriminant is handled by the zero residual polynomial. The190 pairs (a,b) with a+b≤18 are unisolvent over F29 for total degree≤18. In the displayed order, each newly added falling-factorial basis element vanishes at all earlier nodes and equals a!b! at its own node. These factorials are units. The recursive interpolation in `reconstruct.sage.py` therefore reconstructs every X coefficient exactly, and its190 evaluation checks are appropriate.

The reconstruction describes the whole algebraic-closure parameter chart in characteristic29; it is not a190-point candidate census. The code does not yet compute subresultants, and its proposed indexing still needs checking against the chosen CAS convention. Degree48 saturation is required for the fixed-degree gcd criterion.

Operational recommendation: resumable checkpoints should bind their data to an input SHA-256 and assert the expected prime, chart, and degree metadata. Otherwise an output file from another input could be reused accidentally. This does not affect the mathematics of a fresh run.

No transfer from modular emptiness to characteristic-zero emptiness is automatic. Such a claim would require the separately stated integral certificate and control of all discarded parameter strata.
