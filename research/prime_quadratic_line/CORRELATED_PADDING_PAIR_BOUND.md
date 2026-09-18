# Correlated padding: an exact pair-incidence constraint

This concerns the existing bank P_i(X)=X²/a_i²+a_i² over an odd field,
with distinct a_i². It imposes no degree, independence, or distribution
assumption on the fresh received values f(x),g(x).

Let E be t distinct fresh coordinates on which g is nonzero. For a bank
index i and parameter lambda, write

    S(i,lambda)={x in E: P_i(x)=f(x)+lambda g(x)}.

For distinct x,y, an index i can share one parameter at both coordinates
only if

    (g(y)x²−g(x)y²)/a_i² + (g(y)−g(x))a_i²
       = g(y)f(x)−g(x)f(y).

Unless all three coefficients vanish, this equation has at most two values
of a_i²: multiply by a_i² to obtain a nonzero quadratic. Each index then
determines exactly one parameter. If all three coefficients vanish, the
nonzero-direction hypothesis forces g(y)=g(x), x²=y² and f(y)=f(x).
Thus exceptional pairs must be y=−x, and there are at most floor(t/2).

Consequently, for any selected M distinct parameters, each supplied with
one bank witness that gains at least d≥2 fresh matches,

    M binom(d,2) ≤ 2 binom(t,2)+(L−2)floor(t/2).

Proof: count coordinate pairs inside the selected witness match sets.
Every ordinary coordinate pair occurs in at most two (index,parameter)
pairs; an exceptional pair occurs in at most L. Selecting only one witness
per parameter can only decrease this count.

In particular, for t=Theta(n) and L=Theta(sqrt(n)), this gives

    M=O(n²/d²).

Thus any superlinear exceptional count obtained solely by padding this
fixed bank requires d=o(sqrt(n)). More quantitatively M≥n^(1+epsilon)
forces d=O(n^((1−epsilon)/2)). This bound covers correlated padding and
arbitrary programmed values, unlike the independent-sampling bound.
It leaves substantial room between logarithmic and square-root gaps.

## Why synchronizing partial banks into long identical blocks is limited

Suppose three distinct bank indices are assigned fixed distinct parameters
lambda_i and all match at every point of a block. Eliminating f and g gives

    det [[1,lambda_i,P_i(X)]]_(i in the triple)=0

at every block coordinate. This is a polynomial of degree at most two.
It is not identically zero: that would put the three coefficient points
(a_i^(−2),a_i²) on an affine line, whereas they lie on a nonsingular conic.
Therefore a block supporting the same three assigned bank/parameter pairs
has at most two coordinates. Arbitrarily long blocks can synchronously
promote at most two fixed bank/parameter pairs. Disjoint such blocks provide
only O(n/d) promoted parameters, not a superlinear family.

This does not exclude overlapping blocks with changing promoted subsets.
The concrete remaining incidence target is to realize many match sets of
size d→infinity whose coordinate-pair multiplicities are at most two and
whose per-coordinate values are affine images of the conic bank values.
The latter affine-image requirement, absent from abstract block designs,
is the unresolved algebraic constraint. No positive construction beyond
the logarithmic random-padding gap is asserted here.
