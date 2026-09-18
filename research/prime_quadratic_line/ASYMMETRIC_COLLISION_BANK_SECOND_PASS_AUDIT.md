# Asymmetric collision bank: independent second-pass audit

September 18, 2026. **PASS** for the asymptotic construction in
`asymmetric_collision_bank.tex`, using the established first-order
upper bound in place of an unneeded assertion of an exact limit. No
finite onset, prescribed evaluation domain, or code-wide list bound
is certified here. No manuscript edits accompany this audit.

## 1. Prime selection is not circular

Choose the integer parameter K first, then

    H = floor(16 K^(2/3) (log K)^(4/3)),
    t = floor(v_H/16),  s = floor(v_K/16),
    R = t²,  L = t²+s²,  M = floor(L/8),  Q0 = R H M,

where v_x counts the integer primes in [x/2,x]. By the prime number
theorem,

    t ~ H/(32 log H),  s ~ K/(32 log K),
    Q0/K⁴ -> 9/8192.

Thus a prime p=1 mod4 in (4096 Q0,8192 Q0), supplied eventually by
the prime number theorem in that fixed progression, satisfies p>K⁴:
the lower endpoint divided by K⁴ tends to 9/2. Also H<K/2 eventually.
All these integer counts are fixed before p is chosen.

For any resulting p, a largest quartic class in each interval has at
least v_x/4 elements. This is enough for the two vertex sets of size t
or s. The two components may use different quartic classes and different
reference primes. No cross-interval character-distribution assumption
is required. Within each component, a reference z permits square
factors alpha_a²=a/z and beta_b²=b/z. The resulting square parameter
theta_ab=alpha_a/beta_b has theta_ab²=a/b, and rectangle products are
exactly equal before squaring.

## 2. Exact asymmetric core

Squaring a pair-product equality and clearing denominators produces
an equality between positive integers at most K⁴<p. Unique factorization
fixes the numerator and denominator multisets. A distinct-edge pair
therefore has one representation, except for the two diagonals of a
rectangle within one component, which give exactly two. Cross-component
pairs have one representation. Repeated-edge products cause no extra
distinct-edge representation.

Give both square roots to the sole pair in a one-pair class; in a
two-pair class give one root to each pair. The two pair sums differ,
since equal sum and product would identify the unordered pairs. At an
assigned root with value theta+phi, a bank parameter eta matches exactly
when (eta-theta)(eta-phi)=0. Every core coordinate has exactly two owners.

A rich edge has (t-1)² opposite partners in rectangles, each costing
one of its two potential matches. A filler edge has (s-1)² such partners.
Consequently the exact agreements and core size are

    A  = 2(L-1)-(t-1)² = t²+2s²+2t-3,
    A' = 2(L-1)-(s-1)² = 2t²+s²+2s-3,
    A-A' = (s-t)(s+t-2) ~ s²,
    N0 = (t² A+s² A')/2 ~ s⁴/2.

In particular, N0 is not LA/2 in the asymmetric construction. Every
outside quadratic has at most L core matches: count each matching
coordinate against both its owners, while each bank polynomial differs
from the outsider at at most two roots.

## 3. Grid retention and rich-only collision screening

For a uniformly translated M-by-M grid, retain nonzero square ratios
V/U, one square root per ratio, one representative of repeated ratios,
and no core ratio. For its size X, the exact elementary lower bound is

    E X >= M²(p-1)²/(2p²)
           - binom(M²,2)/p - M² binom(L,2)/p.

The last two losses follow from nontrivial affine equations in the two
translation variables. Since L²/p=O((log K)^(-4)), this is
(1/2-o(1))M², and P[X>=M²/4]>=1/3-o(1).

For a rich bank, the integer sums a*u+b*v have at most 3HM possible
values and each fiber has at most 1+2M/H<=3M/H points. There is no
modular wraparound, since 3HM<p. At

    d=floor(M/(64H)),

the fibers with fewer than d points account for at most 3M²/64 points.
Therefore X>=M²/4 forces at least 13HM/192>=HM/16 rich labels per
rich bank. Restricting to retained coordinates only reduces fiber sizes.

For two different rich bank parameters, equality of any two raw
interval labels is a nontrivial affine equation in the translation.
Thus, if C counts these cross-bank collisions,

    E C <= binom(R,2)(3HM)²/p,
    P[C>RHM/64] <=288 RHM/p <288/4096 <1/3.

Probability subtraction, with no independence assertion, supplies a
translation satisfying both conditions eventually. Removing both
bank-label pairs at each collision leaves at least RHM/32 labels with
a unique rich owner.

Screening against filler labels is unnecessary. A filler fiber has at
most 1+2M/K points, because its distinct coprime prime coefficients lie
in [K/2,K] and 3KM<p. Uniformly over every label,

    filler agreement <= A'+1+2M/K < A

eventually. Neutral padding adds no bank matches. This strict uniform
bound is the step that allows only R, rather than L, in the collision
estimate and field-size requirement.

## 4. Padding, exact endpoints, and common agreement

Take T=A+d and n=floor(T²/2)+1. There is ample room for the core and
retained grid:

    n ~ 2s⁴,  N0 ~ s⁴/2,  M² ~ s⁴/64.

Since p/n grows like a positive multiple of (log K)^4, fill to n with
coordinates carrying f=X³ and g=0, excluding the roots of X³-P_theta
for every bank member. Banks gain no matches and outsiders gain at
most three.

On the grid, f=c0/U and g=1/U. A nonconstant quadratic has at most two
matches for each fixed U, hence at most 2M. A nonzero constant can
match in only one U-row. The zero polynomial is the sole exception,
at lambda=-c0. Away from it, an outsider has at most L+2M+3<A total
matches. Since the screened labels have exactly one rich owner and
fillers remain below A, they have singleton lists at threshold T.

The rich raw-label union has size at most 3RHM<p-2. Outside it and
the zero exception, every line member has exact agreement A, attained
by all R rich banks. There are at least two such finite labels, so
they may be chosen as endpoints. They are not among the successful
threshold labels.

For common agreement, a zero polynomial explaining the direction
restricts common matches to the core and padding, whose maximum is
exactly A. A nonzero quadratic explaining the direction has at most
two matches on that zero-direction block and at most 2M on the grid,
strictly fewer than A. Thus ordinary common agreement is exactly A.
The invertible linear change from intercept/direction to the chosen
endpoints preserves this quantity and bijects the affine parameters.

After deleting the zero exception, at least

    RHM/32-1 > p/2^18-1 >= p/2^19

successful interior labels remain eventually. At threshold A, fillers
and nonzero outsiders are absent at every label; only the R rich bank
words and possibly the zero polynomial occur. The resulting bound R+1
is line-local, not a bound for arbitrary received words of the code.

## 5. Scales and first-order comparison

The exact ledgers yield

    n = Theta(K⁴/(log K)^4),
    d = Theta(K^(4/3)/(log K)^(10/3))
      = Theta(n^(1/3)/(log n)^2),
    p = Theta(n(log n)^4),
    R = Theta(n^(1/3)(log n)^2).

Both A/sqrt(n) and T/sqrt(n) tend to sqrt(2). The sufficient, already
established first-order comparison is

    n*a1(3/n) <= sqrt(3n/2)+(3n/8)^(1/4).

Its right side divided by sqrt(n) tends to sqrt(3/2)<sqrt(2), so the
source lies strictly above first order eventually. No exact limit
formula for a1 is needed. The definition of n gives T²<2n exactly.
The proof should use this bound in its last paragraph, as the symmetric
theorem already does.

The rate is 3/n, and the source loss divided by the capacity margin
still tends to zero. The result is a stronger growing-gap tradeoff
within this mechanism, not a fixed-rate or practical-parameter claim.
Its gap exponent is sharp up to logarithms for one translated grid
with a constant fraction of prime-field labels; the precise scoped
ceiling is appended to `TRANSLATED_GRID_CONSTANT_LOSS_GATE.md`.
