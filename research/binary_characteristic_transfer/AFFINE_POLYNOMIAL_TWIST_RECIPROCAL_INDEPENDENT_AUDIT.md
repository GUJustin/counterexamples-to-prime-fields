# Independent affine-twist reciprocal-pencil audit

PASS, 2026-09-19. Actual frozen source inspected throughout. No corrections needed.

## Reversal and degree edge cases

For F≠0, the strict residual degree bound gives degF≤degG−1; F=0 retains exactly the monic head G^(p−1). Degree-zero locator forces G=A=1 and F=0. Three distinct affine twists must have equal degree: their maximal-degree coefficient is an affine scalar taking only 0 or 1, hence constant at three distinct points. Reversal at that common degree gives a_i=1/g_i modulo Z^(p−n), including roots at zero (which only lower deg g_i). Clearing the reciprocal relation produces degree at most 2e₀, not 3e₀; the strict inequality p−n>2e makes the relation exact. Repeated twists have a unique monic native locator by the fixed-A result, which includes F=0, and then have unique F by injectivity of Frobenius.

## Shared poles and locator count

Factoring G₀=CU and G₁=CV with gcd(U,V)=1 gives the correct denominator numerator W_t=(1−t)V+tU. For interior parameters W_t is monic of degree d and coprime to UV, so it must divide C. Distinct W_t are coprime, including over extension coefficients. This yields 2+floor((e₀−d)/d)≤e₀+1. Shared poles are explicitly allowed; the incorrect bound two is not used. The H/(X−a) example establishes only sharpness of this reciprocal geometry and is properly separated from the Frobenius compiler.

## Common locator on an actual received pencil

A common G gives an affine F pencil after the unique pth-root parameter change in finite E. The common zero set S contains Z(Λ/G), so n−|S|≤e. In the quotient by δ·RS_k, if the residual pencil is constant, two distinct challenge parameters would make g a codeword; any T-agreement witness would then make f and g simultaneously explainable on T coordinates, contradicting CA<T. Thus this case has at most one displayed challenge.

If at least two distinct displayed challenges exist and the residual image is nonconstant, the two affine lines in the quotient coincide and λ is an invertible affine function of the residual parameter. Their two common-zero evaluations on S give codeword explanations of both f and g there, so |S|≤CA<T. Every other coordinate vanishes for at most one residual parameter. The count M(T−|S|)≤n−|S|≤e is therefore valid and yields M≤e. Repeated residuals cannot evade this argument: two distinct λ with the same quotient residual already imply the excluded g-codeword case. The fixed coordinatewise nonzero multiplier is sufficient; it need not be a polynomial.

The zero-locator-degree branch has only the zero residual and at most one challenge under CA<T, agreeing with the bound e+1. Families with only two twists likewise fit the bound (e=0 cannot supply two twists). The practical sufficient condition p≥3n indeed implies p−n>2e for every e<n.

Scope remains displayed witnesses from the stated exact identities, native monic divisors, one affine twist space, a fixed nonvanishing multiplier, and residual degree below n. Higher-dimensional twists or varying denominators are not excluded.

Frozen source SHA256: `a1ee5e57fb6ab2b6f3b8ccbd246acd382248a084f8214a4d195279a8a743ccda`.
