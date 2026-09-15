# Growing numbers of interval moments: uniform bounds and optimized parameters

Date: 2026-09-15. This note derives consequences of the manuscript's finite
concentration proposition and the classical Gram norm. It does not extend the
fixed-dimensional Gaussian limit to growing dimension. No novelty is claimed
for the norm or concentration inequalities.

## 1. A bound valid for every finite number of moments

Let `1 <= m < t < n`, `k=t-m`, and let `p>n` be prime. Write `L` for the
maximum list size at radius `1-t/n` of the interval-domain Reed--Solomon code
of dimension `k`. For `1<=j<=m` set

\[
 V_j=\frac{t(n-t)}{n-1}
 \frac{\prod_{i=1}^j(n^2-i^2)}
 {(2j+1)\binom{2j}{j}^{2}(j!)^2},\qquad
 h_j=\left\lceil\sqrt{(m+2)V_j}\right\rceil.
\]

The Gram polynomials have leading coefficient `1/j!`, and hence give a
unit triangular rational change of coordinates from the binomial moments.
Their additive constants have no effect on variance or signature classes.
The finite concentration proposition therefore gives

\[
 L\ge\left\lceil\binom nt/D_G\right\rceil,
 \qquad D_G=\frac{m+2}{2}\prod_{j=1}^m(2h_j+1).                 \tag{1}
\]

This has no fixed-`m` assumption. The rational coordinate change is used
over the reals; there is no extra field-denominator condition.

## 2. A uniform growing-dimension estimate

All logarithms in this section are natural. Fix a compact subinterval of
`(0,1)` containing `t/n`. Uniformly for integers `m->infinity` with
`m<=sqrt(n)`,

\[
 \log D_G=
 \frac{m^2}{2}\log\frac nm+
 \left(\frac34-\log2\right)m^2+O(m\log n).                  \tag{2}
\]

The implicit constant depends only on that compact interval. This is a
two-term statement when `m/log(n)->infinity`, as in the headline regime.

### Derivation, including rounding

Put `d_j=sqrt(2j+1)(2j)!/j!`. The exact variance identity gives

\[
 \frac12\sum_{j=1}^m\log V_j
 =\frac m2\log\frac{t(n-t)}{n-1}
  +\frac{m(m+1)}2\log n-\sum_{j=1}^m\log d_j
  +\frac12\sum_{j=1}^m\sum_{i=1}^j\log(1-i^2/n^2).
\]

For `m<=sqrt(n)`, the last double sum is `O(m^4/n^2)`. Stirling's
bounds and integral comparison for `sum j log j` give

\[
 \sum_{j=1}^m\log d_j
 =\frac{m^2}{2}\log m+
   (\log2-3/4)m^2+O(m\log m).
\]

The exact recurrence

\[
 \frac{V_{j+1}}{V_j}
 =\frac{n^2-(j+1)^2}{4(2j+1)(2j+3)}
\]

shows, for all sufficiently large `n` in this range, that `V_j>=V_1`,
while `V_1=t(n-t)(n+1)/12=Theta(n^3)`. Consequently

\[
 \log(2\lceil\sqrt{(m+2)V_j}\rceil+1)
 =\log2+\tfrac12\log(m+2)+\tfrac12\log V_j+O(n^{-3/2}).
\]

Summing and including the prefactor in (1) proves (2). Thus neither an
unproved high-dimensional central limit theorem nor an uncontrolled
fixed-dimension constant is hidden in this estimate.

For comparison, the complete-range denominator of the original finite
moment lemma satisfies, in the same regime,

\[
 \log D_R=\frac{m^2}{2}\log\frac nm+\frac34m^2+O(m\log n).
                                                                    \tag{3}
\]

To verify (3), use
`R_j=binom(n,j+1)-binom(n-t,j+1)-binom(t,j+1)+1`.
The product formula for `binom(n,j+1)` has log error `O(j^2/n)` relative
to `n^(j+1)/(j+1)!`; the two subtracted ratios are bounded by geometric
sequences in `j`, uniformly away from endpoint densities. The resulting
total errors are `O(m^3/n+1)`. Stirling then proves (3).
In particular, if `log(n)<<m<=sqrt(n)`,

\[
 \log(D_R/D_G)=(\log2+o(1))m^2.                             \tag{4}
\]

This is a substantial subleading improvement: a factor
`2^((1+o(1))m^2)` in the unrounded list guarantee. It does not change the
leading entropy loss `(m^2/2)log(n/m)`.

## 3. Consequence for the paper's headline scale

Fix a rational code rate `rho in (0,1)`, take `n` through multiples of
its denominator, and put `k=rho*n`, `t=k+m`. Let `H=H_2(rho)` and

\[
 m=\left\lfloor c\sqrt{n/\log_2 n}\right\rfloor.
\]

For every constant `0<c<2sqrt(H)`, (1)--(2) give

\[
 \log_2 L\ge(H-c^2/4-o(1))n.
\]

Thus the Gram improvement preserves the same allowed leading constant
`c<2sqrt(H)`, the same gap `Theta(1/sqrt(n log n))`, and the same
below-Elias field-bit scale `Theta(sqrt(n log n))` as the current
theorem. At this scale the improvement in (4) is
`(c^2+o(1))n/log_2 n` **bits**. It does not alone permit
`m` of an asymptotically larger order while keeping this lower bound
exponential in `n`.

This last limitation concerns the guarantee obtained by this argument;
it is not an upper bound on true list sizes or on other constructions.

## 4. A stronger way to state the existing obstruction

The following optimized gap formulation is already available from the
original full-range estimate; Gram concentration improves lower-order
terms. It makes the strength of the obstruction more explicit.

For each sufficiently small real `epsilon>0`, choose `n` to be a multiple
of the denominator of `rho` with

\[
 n=\left(1+o(1)\right)
       \frac{H}{\epsilon^2\log_2(1/\epsilon)},
 \qquad m=\lfloor\epsilon n\rfloor,
 \qquad \eta=m/n.
\]

Then `eta/epsilon->1` and the constructed code has exact rate `rho`.
Substitution into (2), or the original full-range bound, gives

\[
 \boxed{\quad
 \log_2 L\ge
 \left(\frac{H^2}{2}-o(1)\right)
 \frac{1}{\eta^2\log_2(1/\eta)}.
 \quad}                                                        \tag{5}
\]

To see the optimization directly, at a target gap `epsilon` the leading
lower bound as a function of length is
`H*n-(epsilon^2/2)*n^2*log_2(1/epsilon)`. Its maximum occurs at the stated
choice of `n`. Rounding changes `n` by a bounded amount and `m` by less
than one; both are negligible on the displayed scales. No claim of
global optimality over other constructions is intended.

For any fixed `A>H`, let `N=ceil(2^(A/eta))` and choose a prime
`N<p<2N` using Bertrand's postulate.
Then

\[
 \log_2p=A/\eta+O(1),\qquad p>n
\]

for all sufficiently small gaps. The usual entropy inequality
`H_p(theta)<=theta+H_2(theta)/log_2 p`, with
`theta=1-rho-eta`, shows strict below-Elias distance because
`eta*log_2p->A>H_2(rho)`.

Writing `b=log_2p`, (5) becomes

\[
 \log_2L\ge
 \left(\frac{H^2}{2A^2}-o(1)\right)\frac{b^2}{\log_2 b}.        \tag{6}
\]

In particular these examples have lists superpolynomial in the field
size, at lengths `Theta(b^2/log b)`. For any fixed coefficient `a<1/2`,
one can choose `A>H` sufficiently close to `H` so that the coefficient
in (6) exceeds `a` eventually. The choice of `A` is fixed before taking
the limit.

Uniformly over prime fields and evaluation domains, (5) rules out every
bound of the form
`L <= 2^o(eta^(-2)/log(1/eta))` at this fixed rate, including fixed
multiplicative constants. It is stronger than merely ruling out
`exp(O(1/eta))`. The prime fields grow, the gap shrinks, and the domains
are intervals; no fixed-field, fixed-gap, or prescribed-domain claim
follows.

### Stronger quantifiers after independent review

The Gaussian-bound reviewer observed two improvements incorporated in
the paste-ready `proposed_gap.tex`:

1. Taking `m=ceil(epsilon*n)` puts the constructed list at a radius no
   larger than `1-rho-epsilon`. List-size monotonicity therefore gives
   (5) directly at **every sufficiently small prescribed real gap**
   `epsilon`, without changing the target gap to the rounded actual gap.
   The lower bound holds for every prime `p>n`; only the below-Elias
   assertion needs the additional entropy condition on `p`.
2. For **every sufficiently large prime** `p`, let `b=log_2 p`,
   `A_b=H+b^(-1/2)`, and `epsilon=A_b/b`. Use the construction above with
   `m=ceil(epsilon*n)`. Since
   `H_2(1-rho-epsilon)=H+O_rho(1/b)<A_b`, strict below-Elias distance
   holds. The quantitative conclusion is

   \[
   n=(H^{-1}+o(1))b^2/\log_2b,\qquad
   \log_2L\ge(1/2-o(1))b^2/\log_2b.
   \]

Thus the fixed-`A` presentation above is unnecessary in the final
corollary. Uniformity of the original range estimate and elementary
entropy continuity suffice for this explicit vanishing margin; no
diagonal argument or unproved uniform central limit theorem is used.

## 5. Exact calculation artifact

`verify_growing_m.py` checks the Gram normalization and orthogonality on
small grids using rational arithmetic, checks the variance recurrence,
and computes (1) and the original range bound exactly for modest finite
fixtures. Its JSON output gives rigorous integer lower bounds on their
base-two logarithms. These are checks of finite formulas, not proofs of
the asymptotic estimates, and are unrelated to a protocol submission.
