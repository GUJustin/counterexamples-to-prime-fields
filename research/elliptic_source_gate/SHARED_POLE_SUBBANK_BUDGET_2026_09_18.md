# Shared-pole Paley subbanks: uniform pair and spectral budgets

September 18, 2026. No scan. This extends the full-bank double-zero argument to arbitrary growing subbanks, at the SAME quarter-rate degree/length scale. It does not infer subbank behavior from the full-bank average.

## Scoped theorem

Use the bank in `SHARED_POLE_PALEY_TRANSLATION_TARGET.md`. Let M=ell² tend to infinity through odd-prime squares, in characteristic zero or ambient characteristic p>5 with p≠ell. Choose ANY L=L(M) distinct nonzero labels modulo sign, with L→∞. On any N=4M distinct affine evaluation coordinates, and for any received word, if all selected degree-at-most-M polynomials have at least A matches, then

    limsup A/M <=(1+sqrt(35))/4.

Consequently no such growing subbank attains the dimension-(M+1) first-order threshold asymptotically: its agreement fraction is at most (1+sqrt(35))/16+o(1)<(3+sqrt(133))/31. A subbank including the zero label has the same conclusion by discarding that one member. No positive density assumption L=Omega(M) is required.

The degree scale is essential: the statement compares with K=M+1, or K/M→1. It does not claim that a substantially different code-degree normalization, new coefficient array, or different rate has been excluded.

## 1. Uniform pairwise double-zero count

Identify the torsion labels with F_M and let chi be its quadratic character, with chi(0)=0. Here chi(−1)=1. For distinct nonzero labels S,T with S≠±T, the values at pole U are, up to a fixed nonzero factor,

    k_U(S)=chi(U−S)+chi(U+S),
    k_U(T)=chi(U−T)+chi(U+T).

Away from U=±S,±T put a=chi(U−S), b=chi(U+S), c=chi(U−T), d=chi(U+T). Their sums agree exactly when the following indicator is one:

    I=3/8+(ac+ad+bc+bd−ab−cd)/8+3abcd/8.

Each of the six pair-character sums over all U∈F_M is −1, since the four shifts are distinct. The quartic character sum C4 satisfies

    |C4+1|<=2sqrt(M).

Indeed z²=(U−S)(U+S)(U−T)(U+T) is a smooth genus-one curve; its monic quartic model has two rational points at infinity, so this is Hasse's bound. Thus the sum of the displayed polynomial indicator over all U is at least

    3M/8−5/8−(3/4)sqrt(M).

At the four excluded shifts the multilinear indicator is between zero and one, so removing them loses at most four. Removing U=0 loses at most one further equality. Equality is invariant under U→−U, and poles are nonzero labels modulo sign. It follows that twice the number of equal-valued poles is at least

    3M/8−(3/4)sqrt(M)−6.

By the cleared rational formula, equality at a pole gives a DOUBLE zero of Q_S−Q_T, as proved in `SHARED_POLE_DOUBLE_ZERO_BUDGET_2026_09_18.md`. Therefore every pair has at most

    Delta=5M/8+(3/4)sqrt(M)+6

offpole equality coordinates. This is a uniform individual-pair bound, not an averaged estimate. The constants are deliberately loose at the four exceptional shifts.

## 2. Pole concentration of an arbitrary subbank

Let C be any L≥2 nonzero labels modulo sign. There are P=(M−1)/2 poles. For pole T define the real sums

    B_T=sum_(S∈C) chi(T²−S²),
    A_T=sum_(S∈C)[chi(T−S)+chi(T+S)].

Away from the diagonal label S=±T, the zero bucket has indicator (1−chi(T²−S²))/2, and the +2 bucket has indicator

    [1+chi(T−S)+chi(T+S)+chi(T²−S²)]/4,

with both linear character signs reversed for the −2 bucket. At the diagonal the actual value is ±1; deleting the spurious half-contribution only lowers the preceding bucket counts. That exceptional bucket has size at most one. Hence the largest selected-subbank bucket at T satisfies

    r_T <=L/2+|B_T|/2+|A_T|/4.

The Paley convolution operator on the additive group F_M has squared operator C*C=M I−J, so its real l2 norm is sqrt(M).

For B_T, use the indicator of the L distinct squares S² as input and restrict the output to the P distinct squares T². This gives

    sum_T |B_T|² <= M L.

For A_T, use the indicator of the 2L labels ±S. Its full-field output has squared norm at most 2ML. This output is even in T, so restriction to one representative of each nonzero ±pair gives

    sum_T |A_T|² <= M L.

Thus for ANY q selected pole coordinates, Cauchy–Schwarz yields

    sum_(selected T) r_T <= qL/2+(3/4)sqrt(qML).

This bound explicitly handles adversarial subbank choice and adversarial selection of pole coordinates. It does not require random subsets or equidistribution assumptions.

## 3. Combine with the offpole incidence budget

Let q≤P chosen domain coordinates be poles and m=4M−q be offpoles. The total offpole pair count is at most binom(L,2)*Delta. If S_off is the number of candidate/word incidences there, then

    S_off² <=m[S_off+L(L−1)Delta].

Together with the pole estimate and the lower bound LA on total incidences, this gives the explicit finite inequality

    A <= q/2 +(3/4)sqrt(qM/L) +m/(2L)
         +sqrt(m²/(4L²)+m(1−1/L)Delta).

Divide by M and let M,L→∞. All errors vanish uniformly for 0≤q≤(M−1)/2. With z=q/M, the remaining expression is

    z/2+sqrt((4−z)*5/8),  0≤z≤1/2.

Its derivative is positive on this interval, so its maximum is attained at z=1/2 and equals (1+sqrt(35))/4. This proves the theorem.

## Interpretation and limitations

Cosmetic deletion, constant-fraction subbanks, and even arbitrarily sparse subbanks with L→∞ cannot rescue this specific shared-pole bank at its quarter-rate degree scale. The proof uses two ingredients missing from the full-bank average: a uniform quartic-character/Hasse estimate for each pair, and real spectral control of every selected coefficient submatrix.

No bound is claimed for a fixed number of candidates; no explicit finite onset in both L and M is optimized. The finite inequality above can be used if a concrete onset is needed. The result also does not address altered character arrays, arbitrary candidate-by-candidate scalar/constant normalizations (which change the pole buckets), or a proven substantial reduction of the common polynomial degree. Those would require new algebraic identities and new ledgers, rather than a subbank deletion of the present model.
