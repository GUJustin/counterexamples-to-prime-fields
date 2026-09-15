# Independent review of the optimized gap and field-size corollary

Date: 2026-09-15. Reviewed `research/growing_m/growing_m_asymptotics.md` and the strengthened `research/growing_m/proposed_gap.tex`, alongside the manuscript's Lemma `im:finite-list` and proof of Theorem `im:all-list`.

**Outcome: the constant `H_2(rho)^2/2` is correct. The stronger paste-ready corollary is valid as written.** It uses the elementary full-range bound already proved in the manuscript and does not require a growing-dimensional Gaussian limit or the new Gram analysis.

## 1. Optimization and rounding

Fix rational `rho in (0,1)`, write `H=H_2(rho)`, and fix the denominator `q` of `rho`. Put `h=log_2(1/epsilon)` and take `n` to be the nearest multiple of `q` to `H/(epsilon^2 h)`. Let `k=rho n`, `m=ceil(epsilon n)`, and `t=k+m`.

Then

\[
n=\frac{H}{\epsilon^2h}+O_\rho(1),\qquad
m=\frac{H}{\epsilon h}+O_\rho(1),\qquad
\frac mn=\epsilon+O(1/n).
\]

In particular, `m -> infinity`, `m/sqrt(n) -> 0`, `m/n -> 0`, and `1<=m<t<n` eventually. The actual code rate is **exactly** `rho`, because `q` divides `n`.

The existing full-range inequality gives, uniformly for these parameters,

\[
\log_2 L\ge Hn-\frac{m^2}{2}\log_2(n/m)
             -O_\rho(m^2+m\log n+\log n).
\]

Here the binomial numerator follows from `log_2 binom(n,t)=n H_2(t/n)+O(log n)` and differentiability of binary entropy near fixed `rho`; its difference from `Hn` is `O_rho(m+log n)`. The two leading terms are

\[
Hn=\frac{H^2+o(1)}{\epsilon^2h},\qquad
\frac{m^2}{2}\log_2(n/m)=\frac{H^2/2+o(1)}{\epsilon^2h}.
\]

The errors are negligible: `m^2=O(n/h)`, `m log n=O(1/epsilon)=o(n)`, and `log n=o(n)`. Hence

\[
\log_2 L\ge\frac{H^2/2-o(1)}{\epsilon^2\log_2(1/\epsilon)}.
\]

For a general leading length `n~B/(epsilon^2 h)`, the leading coefficient is `HB-B^2/2`, uniquely maximized at `B=H`. This checks the optimization **within this lower-bound calculation**, not among all possible constructions.

Rounding upward is useful: the constructed words have distance `1-rho-m/n <= 1-rho-epsilon`. Thus the conclusion holds at **every sufficiently small prescribed real gap** `epsilon`, rather than only along realized rational gaps `m/n`. Rounding the length to a multiple of fixed `q` and rounding `m` each change only negligible terms.

## 2. Field size and strict Elias comparison

For every prime `p>n`, the combinatorial list lower bound holds on the interval domain. Moment equality is established over the integers and survives reduction; it needs no field larger than the integer moment ranges. For `theta=1-rho-epsilon`,

\[
H_p(\theta)\le\theta+\frac{H_2(\theta)}{\log_2p}<1-\rho
\]

whenever `epsilon log_2 p > H_2(theta)`. Since `theta` stays near `1-rho<1`, it lies on the increasing branch of `H_p` for sufficiently large `p`; this proves strict distance below the manuscript's defined characteristic-based Elias radius.

The original fixed-`A` construction with `A>H` and `log_2 p=A/epsilon+O(1)` is valid. But one can state a stronger result on **every sufficiently large prime field**. Given such a prime, write `b=log_2 p`, set

\[
A_b=H+b^{-1/2},\qquad \epsilon=A_b/b,
\]

and use the preceding length construction. Then

\[
n=(H^{-1}+o(1))\frac{b^2}{\log_2 b}<p
\]

eventually. Entropy is differentiable in a neighborhood of fixed `1-rho`, so

\[
H_2(1-\rho-\epsilon)=H+O_\rho(1/b)<H+b^{-1/2}
=\epsilon b.
\]

The explicit vanishing margin therefore preserves strict Elias. Substitution into the gap bound yields

\[
\boxed{\log_2 L\ge(1/2-o(1))\frac{b^2}{\log_2 b}.}
\]

Thus no arbitrary fixed coefficient below `1/2` need appear in the final statement. The explicit choice of `A_b` justifies reaching `1/2-o(1)`; substituting `A=H` without checking the strict entropy inequality would not be justified in general.

## 3. Quantifiers to preserve

- Fix rational `rho` first. Exact irrational rate is impossible for a finite-dimensional code; rounding the dimension would instead give rates converging to an irrational target.
- For each sufficiently small real `epsilon`, one common length `n` works for **all primes `p>n`** for the list lower bound. Only primes satisfying the separate entropy condition have the below-Elias guarantee at that radius.
- The field-size corollary starts from **each sufficiently large prime `p`**, then selects a length and gap depending on `p`. It is stronger than an existential sequence of primes.
- Received words and the large classes may depend on the parameters. This is an existence theorem, not an algorithm finding or enumerating the lists efficiently.
- All little-oh terms fix `rho`; no uniformity as `rho` approaches zero or one is claimed. The gap result's little-oh is independent of `p`, since its lower bound is integer combinatorics.
- The conclusion rules out a uniform bound whose logarithm is `o_rho(epsilon^(-2)/log(1/epsilon))`, even when restricted below Elias, and exhibits lists superpolynomial in `p`.
- It does not resolve a fixed-field, fixed-gap, prescribed transform-domain, or protocol soundness question.

No additional numerical check is needed for this asymptotic review: the rounding and error estimates above are uniform analytic bounds. The finite construction is already covered by the manuscript's exact checks.
