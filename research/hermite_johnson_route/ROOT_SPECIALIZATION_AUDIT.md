# Independent audit of the implicit-series specialization strategy

2026-09-17. Proof audit while full theorem is being assembled.

Let Q(X,z,Y) have Y-degree B and z-degree H bounded, X-degree T. Work after removing repeated Y-factors and X,z content, and exclude any parameter where a removed factor specializes identically to zero. Such exceptions must be explicitly counted. Assume characteristic zero or p>B for separability in Y; formal power-series recurrences do not require p>T or factorial denominators.

Choose an auxiliary X-coordinate x_* transcendental over the original field. A nonzero discriminant in F[X,z] remains a nonzero polynomial in z at x_*. Its z-degree is O(BH), so outside that many labels the equation Q(x_*,z,u)=0 has only simple roots. The initial plane has bounded total degree B+H.

The implicit branch at a simple root has expansion P(x_*+t)=sum a_j t^j. Its coefficients are rational functions on this initial plane. The expected denominator a_j=N_j/Q_Y(x_*,z,u)^(2j-1) and numerator degree O(j(B+H)) follow from algebraic implicit-series recursion; this degree assertion needs to be proved, not inferred from existence alone.

For a branch not generically polynomial of degree <=D, at least one a_j with D<j<=T+BD is nonzero. Indeed, if all those coefficients vanished, truncating at D would give a polynomial R with Q(X,z,R(X)) vanishing to order at least T+BD+1 at x_*, while its degree is at most T+BD. Then Q(X,z,R)=0 identically, and local uniqueness forces the entire branch to equal R. If T+BD<=D, the same argument already applies to the D-truncation and there is no nonpolynomial branch.

At a special parameter where this branch becomes a degree-D polynomial, its selected nonzero numerator must vanish. Bezout on the bounded-degree initial plane therefore bounds these exceptional initial points by O_{B,H}(T+D), and hence also bounds their parameter labels. There are only boundedly many initial-plane components. Denominator/discriminant exceptions are handled separately.

This avoids assuming that all specialized polynomial roots come from generic polynomial-root families. It also avoids an exponential coefficient-elimination argument. Generic polynomial branches still need the common-pole/curve-degree argument and the full-support incidence argument, being audited separately.
