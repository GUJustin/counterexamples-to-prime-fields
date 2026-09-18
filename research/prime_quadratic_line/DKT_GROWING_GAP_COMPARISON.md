# Candid finite DKT comparison for the quadratic prime-field lines

Source checked: local `tmp/eprint-2056/paper.txt`, Proposition5.10 (Eq63), Lemma5.6 (Eqs54–56), ordinary transfer (Eq38), and first-order theorem statements. No main-manuscript changes.

## What is uniform and what is not

The message dimension is K=3 and degree D=2, so rho=3/n→0. The threshold satisfies T²=2n−O(1), hence
  a=T/n~sqrt(2rho/3),
  a_1(rho)~sqrt(rho/2),
  a−a_1(rho)~(sqrt(2/3)−1/sqrt2)sqrt(rho).
Thus agreement is a fixed multiplicative factor above the first-order curve, but its absolute normalized margin vanishes. The source/common agreement is C=T−d. Its normalized gap is d/n, also vanishing, even when d~c logn/loglogn grows unboundedly in coordinates.

The eta_1 appearing in DKT's first-order asymptotic theorem measures agreement above the first-order rate curve. It is NOT the gap between the target and source/common agreement. Substituting d/n for eta_1 would be incorrect. The O_rho constants are not uniform along this family; one must use the finite certificate.

## Explicit finite certificate

The already-audited support m=4, derivative cap2, B=2T and H=48B applies unchanged for growing d, because n is chosen from T and the support is independent of C. Its reconstruction characteristic guard is only p>2. The coefficient count is G=3B², local rank23, and B²=8n−delta with delta∈{4,8}. For all sufficiently large n, the same inequalities give list budget≤18n and full-agreement-set MCA budget<31000n². Parity changes only bounded terms; this is a uniform bound with no hidden dependence on rho or d/n.

There is a straightforward smaller valid certificate, if a constant is needed: the exact graded moments are
  W_source=B³+(3/2)B²−(3/2)B,
  W_rank=43.
The all-active row test allows
  H=max(B,floor((W_source−43n)/(3B²−23n)))=8B+O(1).
With the published squarefree counting formulas,
  F_reg=5B−6, S=3B−4, H_s=3H,
  J=H(16B−21)+10B−12.
The ordinary tail at its smallest incidence threshold3 is O(n^(3/2)). Writing the regular incidence threshold as xT, its leading n² coefficient is
  512/(1−x)+10/x.
Its minimum is (sqrt512+sqrt10)²≈665.108, giving a valid asymptotic upper certificate
  E≤(sqrt512+sqrt10)² n²+O(n^(3/2)).
This is an improvement of the chosen certificate's constant, NOT a proof that all possible DKT supports or transfers require quadratic size. No exhaustive finite-parameter optimization is asserted.

Crucially, Eq55 uses C only indirectly: once C<T, its full-common-witness conclusion makes all threshold-bad challenges exceptional. The numerical budget itself does not depend on d=T−C. Choosing a near-T auxiliary incidence threshold to insert d in a denominator worsens the budget and is not a published source-gap-sensitive improvement.

## Growing-gap and positive-density fields: the bound is vacuous

For fixed0<c≤1/2 the growing-gap construction has
  p/n~e/(2c)·(logn)^(1/(2c)−1)loglogn,
  d~c logn/loglogn,
and at least(1/e−o(1))p singleton bad challenges (or the elementary four-moment constant1/3).
For every such fixed c, p=o(n²). Therefore the actual available counting bound after intersecting with the finite challenge field is
  #bad≤min(p,E_DKT)=p
for all sufficiently large n. The finite DKT certificate gives NO nontrivial failure-probability bound in these fields. Our lower bound is tight up to constants against the ambient field cardinality; it is NOT a matching quadratic DKT lower bound.

The explicit finite gap-three existence receipt likewise has n=4,503,001 and p=18,120,497; any displayed O(n²) certificate is enormously larger than p. Its value is a rigorously finite superlinear-in-n singleton population with positive coordinate gap, not near-saturation of the DKT count.

## The original n^(3/2) construction is a different comparison

The distinct-label quadratic-bank construction has Theta(n^(3/2)) singleton bad challenges and can be realized over every sufficiently large prime after fixing the rational data, or by the finite greedy proof once its field-size guard holds. In particular one may choose p much larger than n², or p>31000n². Then the same DKT n² count is genuinely smaller than the field: it gives a nonvacuous probability upper bound, and the construction gives a nonzero lower bound against it.

However the exponents still differ by one half: n^(3/2) versus n². This establishes a superlinear obstruction in a uniform finite first-order regime, not quadratic-order tightness. Its source gap is one coordinate and its rate tends to zero. The growing-gap positive-density result improves absolute source separation and bad probability, but its bad-count exponent is1+o(1), not3/2 or2.

## What the examples do and do not establish

They rule out a universal O(n) exceptional-count claim with a constant independent of the vanishing rate and source gap, including when the coordinate gap grows nearly logarithmically. They give actual singleton threshold lists at many bad challenges, so those challenges are not explained by a large attained list at that same word. They do not establish fixed-rate/fixed-relative-gap tightness, a quadratic bad-count lower bound, or a matching dependence on DKT's normalized rate-curve margin. Describing the raw n² comparison as spiritually tight without these qualifications would overstate what has been proved.
