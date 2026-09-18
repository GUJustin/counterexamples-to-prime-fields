# Exact padding target and counting budget

**Update:** the structured-padding question posed below is now resolved by `scaled_fiber_padding.tex`, with independent audit in `TWO_BLOCK_INDEPENDENT_AUDIT.md`. The original seed/target analysis is retained below as provenance.

September 18, 2026. This is a necessary-conditions ledger, not a new line counterexample.

Use the core proved in PROOF.md, with n0=2(p²−1), maximal core agreement A=2p, and L=p²−1 maximal witnesses. Append t distinct fresh coordinates, with direction g nonzero at every fresh coordinate and zero on the core. Seek threshold T=A+d, d>0. Each qualifying maximal-bank witness must gain at least d fresh matches at one label.

For each fixed witness and fresh coordinate, the equation f(x)+z g(x)=Q(x) determines exactly one label. Therefore the total number of (witness,label) pairs with at least d fresh matches is at most L t/d. This also bounds the number of distinct labels explained by the maximal bank. Counting witnesses and fresh coordinates without dividing by d would overstate the attainable population by a factor of order p in the desired regime.

The secondary bank contains p+1 witnesses of core agreement A−2. It requires d+2 fresh matches, and contributes at most (p+1)t/(d+2) additional witness-label pairs. Every other quadratic has at most p core matches and needs at least p+d fresh matches. Controlling this last class is required for an exhaustive or singleton conclusion.

For K=3, retaining threshold strictly below the Johnson agreement sqrt(2n) requires

    (2p+d)² < 2(2(p²−1)+t),
    t > 2pd + d²/2 + 2.

Thus d=c p for constant c>0 requires t>(2c+c²/2)p²+2. A construction with t=Theta(p²), d=Theta(p), and M=Theta(p³) must exploit a constant fraction of the maximal bank's entire fresh incidence budget AND prevent extensive collisions between labels from different witnesses. Random fresh values over a field of size at least p⁴ do not supply this automatically.

For example, if fresh f(x) values are independent uniform in the ambient field of size q and g(x) are fixed nonzero, a fixed witness-label pair has Binomial(t,1/q) fresh matches. A union bound gives at most L q binomial(t,d) q^(-d) expected maximal-bank qualifying pairs. For t=O(p²), d=Theta(p), q>=p⁴, this tends to zero. The binomial bound is at most L q (e t/(d q))^d; it is decreasing in q for d>1. Independent random padding therefore misses this target, even before nonbank and singleton constraints. A structured common identity is essential for this approach.

The existing projective_quadratic_line.tex already proves K=3, M=Omega(n^(3/2)), and source gap Theta(sqrt(n)), with characteristic p=Theta(n^(1/4)). Matching those exponents here would only improve the characteristic scale to Theta(sqrt(n)); it would not establish a new count or gap exponent, a prime ambient field, fixed positive rate, or generic tightness of the prime-field proximity bounds.
