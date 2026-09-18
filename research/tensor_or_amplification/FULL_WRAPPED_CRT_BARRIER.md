# Full wrapped CRT discrepancy-product obstruction

This supersedes the nonzero-constant restriction and exceptional-chart caveat in WRAPPED_CRT_RECTANGLE_BARRIER.md. The proof includes arbitrary vanishing orders, arbitrary correlated tuple families, and reduction modulo the domain locator. It is a theorem about this explicit CRT product mechanism, not all realizations of OR incidence patterns.

## Theorem

Let n_i>1 be pairwise coprime, N=∏n_i, and work over a field containing μ_N, of characteristic not dividing N. Fix degrees1≤h_i<n_i. At coordinate i, every permitted factor f_(i,s)(Z) has degree h_i and the SAME nonzero leading coefficient. Its constant and intermediate coefficients may vanish arbitrarily. Put

    ε=max_i h_i/n_i.

For an arbitrary correlated set C of tuples define

    P_s(X) = H(X) − ∏_i f_(i,s_i)(X^(N/n_i))  mod (X^N−1),

with the unique degree<N representative. Suppose these reduced polynomials have degree≤D<N and that at least two tuples have different factor vectors. Set ρ=D/N. For EVERY tuple s, its exact agreement fraction a_s with the word H on μ_N satisfies

    a_s−ρ ≤ 2ε.                                      (1)

Consequently a common agreement threshold A obeys A/N−(D+1)/N≤2ε. In particular no choice of positive-rate or positive-distance outer code, no per-label valuation pattern, and no modular wrapping yields a fixed positive capacity gap when ε→0. A fixed positive first-order margin is then impossible as well.

## Step1: unique reduced coefficient addresses

Every multiindex0≤e_i≤h_i has exponent E=Σe_i N/n_i. Distinct such multiindices have distinct residues modulo N. Indeed equality modulo N implies equality modulo each n_i; since N/n_i is a unit modulo n_i and0≤e_i<n_i, this determines e_i exactly.

Thus the coefficient of a product at the residue corresponding to e is exactly ∏_i f_(i,s_i)[e_i], not a sum of several multivariate coefficients. For any pair s,t, these product coefficients agree whenever the residue exponent exceeds D: subtracting their reduced polynomials cancels H and has degree≤D.

## Step2: arbitrary-phase circular prefix lemma

Let an open arc I on R/Z have length g>ε, and let y_0,...,y_m be a lifted monotone sequence with0≤y_(j+1)−y_j≤ε. If y_m−y_0>1−g, at least one y_j modulo1 lies in I.

Proof: lifts of the closed complementary arc are disjoint closed intervals of length1−g, separated by open gaps of length g. A step of size≤ε<g cannot pass from one complementary interval to a later one while avoiding I. If every sample avoided I, all samples would lie in the same complementary interval, contradicting the span. Strict inequalities handle every endpoint and any number of windings.

## Step3: choose anchors from the first tuple only

Fix a tuple s, and write ℓ_j=ord_(Z=0) f_(j,s_j). Put

    w_j=h_j/n_j,   δ_j=(h_j−ℓ_j)/n_j,   0≤δ_j≤w_j≤ε.

The monomial factor Z^ℓ_j has no roots on μ_(n_j). Hence the root fraction a_j of f_(j,s_j) on that inner domain is at most δ_j. The CRT map μ_N→∏μ_(n_i) is a bijection, so its exact OR agreement is

    a_s=1−∏(1−a_j) ≤ Σ a_j ≤ Σ δ_j.                 (2)

Suppose a_s>ρ+2ε. Choose any other tuple t and fix coordinate i. In every other coordinate j, use either exponent ℓ_j or exponent h_j. These are NONZERO coefficients for the first tuple. Start with all ℓ_j; successively replace them by h_j in any order. The corresponding anchor phases are

    β_i + Σ_(j in prefix) δ_j  (mod1),
    β_i=Σ_(j≠i) ℓ_j/n_j.

Every step is at most ε. Their total lifted span is

    Σ_(j≠i)δ_j ≥ a_s−δ_i > ρ+2ε−δ_i ≥ ρ+w_i,

because δ_i+w_i≤2ε. The allowed anchor arc is

    I_i=(ρ,1−w_i),

whose complementary length is ρ+w_i. Its length is greater than ε: from a_s≤1 and a_s>ρ+2ε, we get1−ρ>2ε and thus1−ρ−w_i>2ε−w_i≥ε. Step2 therefore supplies an anchor phase inside I_i.

## Step4: one high coefficient line recovers a whole factor

Keep that choice of other-coordinate exponents, and let the i-th exponent vary through all integers0,...,h_i. All resulting residue exponents divided by N are the anchor phase plus e_i/n_i. They lie STRICTLY betweenρ and1, with no wrap. By Step1 their coefficients agree for tuples s and t.

For s these coefficients are K_s times the coefficient vector of f_(i,s_i), with K_s nonzero. For t they are K_t times the coefficient vector of f_(i,t_i); K_t is initially allowed to vanish. At e_i=h_i, the common nonzero leading coefficient gives K_s=K_t, and therefore K_t is nonzero. Dividing the other coefficient equalities gives

    f_(i,s_i)=f_(i,t_i).

This argument applies to every coordinate i, so t has exactly the same factor vector as s. Since at least one different tuple exists, the supposition a_s>ρ+2ε is impossible. This proves (1).

## Scope and quantitative consequence

The proof neither discards zero-constant labels nor assumes their valuation patterns agree. It never treats multiplication by a common monomial as degree-preserving. Instead the arbitrary phase β_i is retained and the circular prefix lemma finds a usable high-frequency coefficient line.

The agreement count is exact for the received word H: over a field the discrepancy product vanishes if and only if at least one factor vanishes. Reduction modulo X^N−1 preserves all those values. No hypothetical extra coincidences are hidden in the argument.

The small parameter is h_i/n_i for the FULL factor polynomial, including the received-polynomial degree. Diluting a fixed candidate bank with arbitrary new received values need not keep h_i small and is not automatically covered. If h_i are bounded while all n_i grow, however, the gap vanishes uniformly, regardless of the number of factors or tuple correlations.

The same theorem gives the sharp obstruction required by the proposed low-density CRT mechanism. Abstract correlated OR incidence patterns may still satisfy pairwise degree bounds and first-order numerics; this explicit factor realization cannot realize them with a fixed positive gap in the diluted regime. An entirely different polynomial embedding, a nonproduct formula, non-coprime coordinate orders, or a received word other than H remains outside this theorem.
