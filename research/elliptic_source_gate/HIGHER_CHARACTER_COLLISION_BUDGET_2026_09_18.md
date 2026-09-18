# Higher-order character arrays: first unexcluded order is five

September 18, 2026. Exact root-of-unity collision distribution and asymptotic degree-budget audit; no fixture scan or construction claim.

Let M=ell² and let chi:F_M*→mu_h have fixed order h≥2, with chi(−1)=1, extended by chi(0)=0. Thus h divides (M−1)/2. Replace the quadratic-character coefficients in the shared-pole bank by c_T=chi(T). The coefficient field must contain mu_h and the elliptic torsion data. Assume characteristic zero or a noncollapsing reduction as specified below, and characteristic different from ell.

## 1. Exact finite distribution of two character values

Let zeta be a complex primitive h-th root. For a sum z, let m_z be the number of ordered pairs (i,j) modulo h with zeta^i+zeta^j=z. Two chords of the unit circle with the same nonzero midpoint have the same unordered endpoints. The only additional collisions are antipodal pairs at midpoint zero. Therefore:

* h odd: h diagonal sums have multiplicity1; h(h−1)/2 offdiagonal sums have multiplicity2.
* h even: the zero sum has multiplicity h; h diagonal sums have multiplicity1; h(h−2)/2 nonantipodal offdiagonal sums have multiplicity2.

Consequently the exact collision probability for two independent sums is

    kappa_h=sum_z m_z²/h⁴
       =(2h−1)/h³                     (h odd),
       =3(h−1)/h³                     (h even).

The largest individual bucket probability is

    beta_h=max_z m_z/h²
       =2/h²                          (h odd, h≥3),
       =1/h                           (h even).

In particular h=3 gives multiplicities 1×3 and 2×3, with 15 ordered equal-sum quadruples; h=4 gives 4×1,1×4,2×4, with36 quadruples; h=5 gives 1×5,2×10, with45 quadruples. These are exact finite combinatorial distributions, not simulations of field values.

## 2. Ambient-characteristic guard

Reduction can create extra additive relations among roots of unity. Let Delta_h be the product of the nonzero algebraic norms of zeta^i+zeta^j−zeta^k−zeta^l over all nonidentical complex sums. Excluding ambient primes dividing h*Delta_h preserves exactly the distribution above. A crude sufficient guard is ambient characteristic p>4^phi(h): every such nonzero integral norm has absolute value at most4^phi(h). One must also have p≠ell and a primitive order-h root after reduction.

This is a finite exclusion for fixed h, not an assumption that every finite field has the complex sum pattern. Additional modular collisions otherwise change both kappa and beta and require a separate ledger.

## 3. Pair-degree and spectral estimates

For distinct nonzero labels S≠±T, the four shifts U±S,U±T are distinct. Expanding the four character-value indicators and applying the multiplicative-character Weil bound gives each prescribed four-tuple of nonzero values M/h⁴+O_h(sqrt(M)) occurrences. No nonconstant Fourier term is a perfect character-order power: some exponent at one of the four distinct roots is nonzero. Removing the four exceptional shifts and U=0 costs O_h(1).

It follows that equal pole coefficients for Q_S,Q_T consume double-zero degree

    kappa_h M+O_h(sqrt(M)),

so each pair has at most

    (1−kappa_h)M+O_h(sqrt(M))

offpole intersections. The double-zero argument is the same exact pole cancellation as before.

The pole bound also holds for arbitrary selected subbanks, rather than only the full bank. For each possible sum z, expand its two-value indicator in the h² Fourier monomials chi^i(U−S)chi^j(U+S). Its constant term is mu_z=m_z/h².

For (i,j)≠(0,0), on U,S∈F_M* the corresponding matrix factors as a unitary diagonal matrix times multiplicative convolution: put t=U/S to obtain

    chi^(i+j)(S) * chi^i(t−1)chi^j(t+1).

Multiplicative Fourier diagonalizes this convolution. Each Mellin coefficient is a character sum with possible singularities 0,1,−1; at least one exponent at 1 or −1 is nonzero. The Weil bound is O(sqrt(M)), uniformly in the Mellin character. Thus each centered bucket matrix has operator norm O_h(sqrt(M)). Restricting to nonzero ±representatives, and treating diagonal zero-character exceptions, preserves this bound up to fixed factors and O_h(1).

For an arbitrary L-subbank and q selected poles, summing the centered bucket errors by Cauchy–Schwarz gives

    total pole incidences <= beta_h*q*L
                             +O_h(sqrt(qML)+q).

The finitely many possible sum values permit the same bound for the maximum bucket at each pole. Hence for any L→∞ subbank the normalized error vanishes. This is the spectral analogue needed to avoid silently transferring full-bank averages to subbanks.

The character-sum input is the standard Weil bound for a non-perfect-power polynomial with a bounded number of distinct roots; see, for example, the explicit statement in [the explicit Weil-bound statement, Theorem3.7](https://people.cs.uchicago.edu/~laci/papers/span1.pdf). Only three or four distinct roots occur here, independent of the Mellin-character order.

## 4. Quarter-rate budget and smallest surviving order

At N=4M, K/M→1, let z=q/M∈[0,1/2]. The pair-count inequality and the pole estimate yield, for any growing subbank,

    limsup A/M <= C_h,
    C_h=max_(0≤z≤1/2) [beta_h*z+sqrt((4−z)(1−kappa_h))].

The limiting first-order requirement is A/M>4(3+sqrt(133))/31, approximately1.8751.

|h|kappa_h|beta_h|maximizing z|C_h|Budget conclusion|
|--|--|--|--|--|--|
|2|3/8|1/2|1/2|(1+sqrt35)/4≈1.7290|excluded|
|3|5/27|2/9|0|2sqrt(22/27)≈1.8053|excluded|
|4|9/64|1/4|1/2|1/8+sqrt(385/128)≈1.8593|excluded|
|5|9/125|2/25|0|2sqrt(116/125)≈1.9267|not excluded|

These extrema follow directly by differentiating the displayed concave function. Thus h=5 is the smallest character order for which this specific degree/incidence budget leaves room. For h=5 one may choose ell≡±1 mod5, so the required even character exists for arbitrarily large odd ell. No conclusion here optimizes growing h; all error constants treat h as fixed.

## 5. What identity actually survives

A natural algebraic identity remains available:

    c_chi * c_(chi^-1) = M delta0−1.

On augmentation-zero arrays it supplies an inverse, proving distinctness of the symmetrized-translate bank and its familiar one-dimensional constant-array dependency. It does NOT produce large equal-value fibers away from poles.

For h=5, an actual positive result still requires offpole common-remainder identities G_j | gcd_(S∈B_j)(Q_S−Q_(S_j)), with squarefree disjoint G_j, balanced coverage and the degree budget from the surviving target. Pole buckets now have density at most2/25 of the full bank asymptotically, so poles themselves provide little help. An offpole agreement word must supply buckets close to half the bank on Theta(M) coordinates. The fact that residual pair-degree is roughly0.928M, rather than0.625M in the quadratic case, makes this no longer numerically impossible; it does not supply the factors.

Conclusion: orders three and four are cosmetic changes for the same quarter-rate target and are excluded asymptotically under the noncollapse guard. Order five is a genuine escape from the CURRENT resource inequality, with an explicit convolution identity and a precise missing offpole factor identity. It is not yet a positive construction, and no larger torsion census is warranted without a proposed factor formula.
