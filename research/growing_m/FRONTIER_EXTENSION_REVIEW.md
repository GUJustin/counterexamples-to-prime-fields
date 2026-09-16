# Independent review of the frontier growing-m extension

Reviewed 2026-09-15:

- `stwo_port_review/GRAM_GROWING_M_BOUND.md`
- `stwo_port_review/gram_growing_m.proposed.tex`

## Verdict

**The extension is valid as written.** The asymptotic gain
`2^(m^2+o(m^2))` holds throughout `log n << m << n`, provided `t/n`
stays in a fixed compact subset of `(0,1)`. It holds for both the
smoothed ellipsoid denominator used in the frontier note and the
rectangular concentration denominator used in the published paragraph.
These denominators must nevertheless be distinguished when quoting
finite numerical certificates. The existing numerical table contains
rectangular certificates.

The exact finite error envelopes in the frontier note also check out.
The reasoning below independently verifies their constants; numerical
evidence is not needed for this conclusion.

## 1. Why the restriction m <= sqrt(n) can be removed

The variance recurrence is

\[
 V_j/V_{j-1}=\frac{n^2-j^2}{4(2j-1)(2j+1)},\qquad j\ge2.
\]

Thus `17m^2<=n^2+4` ensures monotonicity through degree `m`. This
condition holds eventually for every sequence `m=o(n)`. In the stated
density range,

\[
 \min_{1\le j\le m}V_j=V_1=t(n-t)(n+1)/12=\Theta(n^3).
\]

Consequently the total smoothed-variance correction is

\[
 0\le\frac12\sum_{j=1}^m\log(1+1/(12V_j))
 \le\frac{m}{2t(n-t)(n+1)}=O(m/n^3).
\]

For the rectangular denominator, putting `x_j=sqrt((m+2)V_j)` gives
`2x_j<=2ceil(x_j)+1<2x_j+3`. The total rounding correction is at most
`(3/2)sum_j(1/x_j)=O(sqrt(m)/n^(3/2))`. Both are negligible in the
claimed growing-m regime.

The nonpositive finite-grid correction in the variance product obeys

\[
 \left|\frac12\sum_{i=1}^m(m+1-i)\log(1-i^2/n^2)\right|
 \le\frac{m(m+1)^2(m+2)}{24n^2(1-m^2/n^2)}.
\]

For `m=o(n)` this is `O(m^4/n^2)=o(m^2)`. No assumption
`m<=sqrt(n)` is necessary.

## 2. The two Gram denominators

Use distinct names:

\[
 D_E=\kappa_m(m+2)^{m/2}\prod_j\sqrt{V_j+1/12},\qquad
 D_B=\frac{m+2}{2}\prod_j(2\lceil\sqrt{(m+2)V_j}\rceil+1).
\]

The variance product is common up to the negligible corrections above.
The ellipsoid prefactor has logarithm
`B_m=log(kappa_m)+(m/2)log(m+2)=O(m)`; specifically
`0<=B_m<=(m/2)log(2*pi*e)+1`.
The rectangular prefactor has logarithm `O(m log(m+2))`.
Thus either denominator satisfies

\[
 \log D_\star=
 \frac{m^2}{2}\log(n/m)+(3/4-\log2)m^2
 +O(m\log n+m^4/n^2),\qquad \star\in\{E,B\}.             \tag{1}
\]

This estimate is uniform for density in a fixed compact subset and
`m=o(n)`. One may make it uniformly quantitative on, for example,
`m<=n/5`; every claimed sequence eventually lies there.

The frontier note's explicit envelope applies to `D_E`, not literally
to `D_B`. Their asymptotic expansion (1) agrees because the difference
in prefactor logarithms is only `O(m log m)`.

## 3. Audit of the explicit Gram envelope

Writing
`A_m=sum_j log[sqrt(2j+1)(2j)!/j!]`, Stirling with remainders yields

\[
 \log\left[\sqrt{2j+1}(2j)!/j!\right]
 =j\log j+(\log4-1)j+\tfrac12\log j+\log2+e_j,
 \quad -\frac1{12j}\le e_j\le\frac7{24j}.
\]

The bounds follow by writing
`e_j=delta_(2j)-delta_j+(1/2)log(1+1/(2j))`, with
`0<delta_j<1/(12j)`.
Integral comparison gives

\[
 \frac14\le
 \sum_{j=1}^m j\log j-left(\frac{m^2}{2}\log m-\frac{m^2}{4}\right)
 \le\frac14+m\log m.
\]

Therefore the remainder `R_A` in the frontier note is nonnegative and
at most

\[
 \frac32m\log m+(2\log2-\tfrac12)m+\frac14+\frac7{24}H_m.
\]

This proves the claimed coefficient and error. The other terms in its
exact decomposition are bounded as stated:

- `0<=(m/2)log(n*t(n-t)/(n-1))<=m log n` for `1<=t<n`.
- A cube inside the radius-`sqrt(m+2)` ball gives `B_m>=0`.
  Integrating the standard Gaussian over the radius-`sqrt(m)` ball
  gives `kappa_m<=(2*pi*e/m)^(m/2)`, hence its stated upper bound.
- The grid and dither terms have the bounds in Section 1.

Thus both sides of the note's fully explicit Gram envelope (4) are
valid under its sufficient condition `17m^2<=n^2+4`. Its density
qualification is only needed for the simplified uniform asymptotics,
not for that finite envelope.

## 4. Exact complete-range comparison

For `R_(l-1)=binom(n,l)-binom(n-t,l)-binom(t,l)+1`,
the two removed binomial ratios are at most `(1-r)^l` and `r^l`,
where `r=t/n`. For `l>=2` their sum is at most `1-2r(1-r)`.
Applying `-log(1-x)<=x/(1-x)` and summing geometric series gives
exactly the note's lower range-correction constant

\[
 C(r)=\frac{r^2/(1-r)+(1-r)^2/r}{2r(1-r)}.
\]

The `+1` term only helps that lower bound. For `m<=n-3`, all relevant
binomial coefficients are at least `binom(n,2)`, giving the stated
upper correction `m/binom(n,2)`.

The total falling-factorial correction is bounded in magnitude by
`m(m+1)(m+2)/(6n(1-m/n))=O(m^3/n)` for `m=o(n)`.
For `M=m+1`, the factorial sum has remainder

\[
 0\le\sum_{l=1}^{M}\log(l!)-
   \left(\frac{M^2}{2}\log M-\frac34M^2\right)
 \le\frac14+\frac32M\log M+
       \frac{\log(2\pi)-1}{2}M+\frac{H_M}{12}.
\]

This follows from the same integral comparison and Stirling bounds.
Translating from `M` to `m` uses
`(M^2 log M-m^2 log m)/2<=M log M+M/2`.
These inequalities imply both explicit range envelopes (10) in the
frontier note, including their loose but valid constants. Hence

\[
 \log D_R=\frac{m^2}{2}\log(n/m)+\frac34m^2
             +O(m\log n+m^3/n).                              \tag{2}
\]

With `log n=o(m)` and `m=o(n)`, the errors in (1)--(2) are `o(m^2)`.
Thus `D_R/D_E=2^(m^2+o(m^2))`, and the same holds with `D_B`.

## 5. Second-order and density qualifications

The frontier note's natural-log and base-two expansions are correct.
At `m=floor(c*sqrt(n/log_2 n))`, rounding changes the leading term by
`O(sqrt(n log n))=o(n/log n)`, and all errors above are also
`o(n/log n)`. In bits the improvement over exact ranges is
`c^2*n/log_2 n+o(n/log n)`.

Retaining `n*H_2(t/n)` is necessary when the density merely converges
without a rate. Replacing it by `n*H_2(rho)` requires an error
`o(n/log n)`; the stated sufficient condition
`t/n-rho=o(1/log n)` supplies this by entropy differentiability in
the interior. The manuscript choice `t=rho*n+m` satisfies it.

## Suggested integration

`proposed_frontier_extension.tex` replaces the published paragraph up
to the numerical table. It names both denominators and preserves the
meaning of the existing table. The original exact finite checker and
JSON remain valid; their values should not be relabeled as ellipsoid
certificates. No larger gap order, stronger fixed-field conclusion, or
growing-dimensional central limit theorem follows from this extension.
