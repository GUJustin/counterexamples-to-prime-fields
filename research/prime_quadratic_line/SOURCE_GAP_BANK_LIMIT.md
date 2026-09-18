# Growing source separation: exact bank-padding constraint

This concerns the explicit bank P_i=X²/a_i²+a_i², and does not exclude new witnesses or a different core design.

Suppose M exceptional labels are explained by members of a fixed bank of L polynomials, and the target agreement exceeds actual common agreement by d. At each coordinate with g nonzero, each bank polynomial specifies exactly one label. Coordinates with g zero on which P_i=f contribute to a common explanation (P_i,0), so they do not remove the need for at least d informative matches for an exceptional label explained by P_i. Choosing one bank explanation per exceptional label gives

    M*d <= L * #{coordinates with g nonzero}.

For the current core, L=Theta(sqrt(n)); hence M=O(n^(3/2)/d). A constant-factor n^(3/2) population with d tending to infinity is impossible within this fixed-bank padding mechanism. This does not rule out n^(3/2)/d, nor new witnesses, nor a core with a larger bank.

There is also a precise limit on synchronized fresh blocks. If at two fresh points x,y with nonzero direction every bank polynomial specifies the same respective label, then for all i

    (1/a_i²)*(x²/g(x)-y²/g(y))
       +a_i²*(1/g(x)-1/g(y))
       -f(x)/g(x)+f(y)/g(y)=0.

Any three distinct coefficient points (1/a_i²,a_i²) are noncollinear: they lie on the conic UV=1, which has no line component. Thus all three displayed coefficients vanish, giving g(x)=g(y) and x²=y². A synchronized block therefore contains at most two distinct coordinates. The auditor's fresh ± pairs attain this limit and improve the constant over a whole-domain quadratic pullback; arbitrary growing blocks cannot come from this same symmetry.

For an improved core, a pair-count heuristic identifies the actual needed change. If typical agreement buckets have b bank members, near pair-root saturation gives A approximately 2L/b and a core length approximately 2L²/b². Thus a bank of order d*sqrt(n), needed to offset the incidence loss, calls for growing bucket multiplicity of order d. This is a design target, not an existence theorem. No suitable prime-field quadratic bank was found in this bounded analysis.

The two-coordinate construction in TWO_COORDINATE_GAP_FRESH_PAIRS.md independently checks: n=2L²+2, A=2L-2, T=2L, nonbank agreement at most L+6<=A for L>=8, and nonzero direction witnesses have at most eight matches. Its above-threshold lists remain singletons after the same source-basis conversion.
