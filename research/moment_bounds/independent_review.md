# Independent review of the Gram/Gaussian moment bound

Date: 2026-09-15. Scope: `gram_gaussian.proposed.tex`, checked against
`gram_gaussian_class_bound.md`, `ellipsoid_moment_bound_audit.md`, the Gram
norm derivation, and the corresponding integrated manuscript section.

**Verdict: no mathematical error or unsupported strengthening found in the
reviewed argument.** The Gaussian constant follows from an ordinary
finite-population CLT and lattice counting. The conversion to Reed–Solomon
codewords preserves exact agreement. The fixed-dimension and sequential-limit
qualifications are essential and are stated correctly.

## 1. CLT normalization and asymptotic constant

For fixed nonzero `u`, set
`a_x = sum_j u_j G_j(x)/sqrt(V_j)`. Orthogonality and the subset-sampling
variance identity give exactly

\[
\frac1{n-1}\sum_x a_x^2
=\frac{n\|u\|^2}{t(n-t)},\qquad
\operatorname{Var}\!\left(\sum_{x\in A}a_x\right)=\|u\|^2.
\]

Thus there is no missing sample-size factor when applying a theorem stated
for sample means to these sample sums. For fixed `m` and `t/n -> rho` in
`(0,1)`, the Gram norm gives `V_j = Theta(n^(2j+1))`; the fixed-degree
polynomial bound gives `max_x a_x^2 = O(n^-1)`. Meanwhile
`min(t,n-t) v_n = Theta(1)`. Their ratio tends to zero at rate `O(n^-1)`.
This is precisely the sufficient condition in
[Li–Ding, Theorem 1](https://arxiv.org/pdf/1610.04821), whose finite
populations may vary with `n`. Cramér–Wold therefore gives the stated
standard multivariate Gaussian limit.

The product of standard deviations has exponent
`sum_(j=1)^m (j+1/2) = m(m+2)/2`. Substituting their exact leading constants
gives the displayed factor

\[
\frac{\prod_{j=1}^m\sqrt{2j+1}\binom{2j}{j}j!}
     {(2\pi\rho(1-\rho))^{m/2}}.
\]

## 2. Triangular lattice and finite smoothing

The unit-cube tiling is valid because the coordinate change is **unit lower
triangular**, not merely determinant one. For `Lambda = b + T Z^m`, a point
`x` determines its cube recursively by

\[
z_j=\left\lfloor x_j-b_j-\sum_{i<j}T_{ji}z_i+\tfrac12\right\rfloor.
\]

This determines a unique translate of `[-1/2,1/2)^m`. It remains valid when
the shears depend on `n` or are large. Diagonal standardization makes these
cells boxes of volume `1/prod_j sqrt(V_j)` and circumradius
`epsilon_n = (1/2)sqrt(sum_j V_j^-1)`. Hence the stated ball-count upper
bound follows by disjoint volume comparison. The cubes need not be linear
images of the original integer-lattice cubes.

The finite ellipsoid argument also has the correct normalization: independent
unit-cube smoothing adds variance `1/12` in each coordinate and produces
density at most `L/binom(n,t)`. The signed quadratic-weight integral gives
exactly the denominator
`kappa_m (m+2)^(m/2) prod_j sqrt(V_j+1/12)`.

The phrase “centered unit cubes” in the Gaussian subsection inherits the
half-open convention explicitly given in the preceding finite proof. Reading
them as closed cubes changes only measure-zero boundaries, not the estimate.

## 3. Order of limits

For each fixed positive `R`, the Gaussian assigns zero mass to the boundary
of the radius-`R` ball, so weak convergence determines its limiting mass.
Pigeonhole counting then gives

\[
\liminf_n\frac{L_n\prod_j\sqrt{V_j}}{\binom nt}
\ge \frac{\Pr(\|G\|\le R)}{\kappa_m R^m}.
\]

The left side is independent of `R`; taking `R` down to zero afterward is
legitimate and gives the density at the origin. No unspecified exchange of
limits or local CLT is used. This proves a lower bound on the largest class,
not its asymptotic equality, a prescribed class's probability, a convergence
rate, or uniformity for growing `m`.

## 4. Exact-agreement codewords

Equal integer binomial moments through degree `m`, together with the common
size `t`, imply equal power sums and hence equal elementary symmetric
functions through degree `m`. Thus `F_A(X) = prod_(a in A)(X-a)` share their
coefficients in degrees `t,t-1,...,t-m`. Let `k=t-m` and let `W` be the
common degree-at-least-`k` part. Then `P_A = W-F_A` has degree strictly less
than `k`.

For every prime `p>n`, the evaluation points remain distinct, and
`P_A(x)=W(x)` holds exactly when `x` belongs to `A`. Different subsets give
different degree-less-than-`k` polynomials and different codewords. Thus each
integer moment class supplies its full cardinality of distinct codewords
at distance exactly `1-t/n`. Rational Gram coefficients are used only for
real counting; their denominators are never reduced modulo `p`.

The asymptotic statement permits any sequence of primes `p_n>n`; its bound
is uniform in that choice. It does not require the stronger condition that
prevents different integer moment classes from merging modulo `p`, because
only a list-size lower bound is asserted.

## 5. Independent exact checks

A separate exact-rational enumeration checked `4 <= n <= 10`, every
`2 <= t < n`, and `1 <= m <= min(3,t-1)`: 84 parameter triples, 5,256 subset
instances, and 3,607 moment classes. All Gram population norms, subset
covariances, common leading coefficients, degree bounds, distinct codewords,
and exact agreement sets passed. There were also 21 direct population-norm
checks. These finite checks corroborate the algebra; the CLT conclusion
rests on the proof above. No manuscript or git operations were performed
for this review.
