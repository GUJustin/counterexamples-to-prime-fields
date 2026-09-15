# Gaussian signature classes: audit and stronger sampling quantifier

Date: 2026-09-15. Scope: pure finite-population probability and Reed–Solomon list lower bounds. No manuscript edits. The original Gaussian constant is correct. The main improvement below extends its sampling regime; the Gaussian weighting argument also gives a finite-size inequality without counting ellipsoids.

## 1. Strengthened theorem

Fix an integer `m >= 1`. Let `1 <= t=t_n <= n-1` satisfy only

\[
\min(t,n-t)\longrightarrow\infty.
\]

For a uniformly sampled `t`-subset `S` of `{0,...,n-1}`, let `M(S)` be the vector of sums of `binom(x,j)`, `1<=j<=m`. Write `L_n` for the largest class with one value of `M(S)`. Let `B_j` be the mean-zero Gram polynomial with leading coefficient `1/j!`, and set

\[
\sigma_{j,n}^2=\frac{\prod_{i=1}^j(n^2-i^2)}{(2j+1)\binom{2j}{j}^{2}(j!)^2},
\qquad V_{j,n}=\frac{t(n-t)}{n-1}\sigma_{j,n}^2.
\]

Then

\[
\boxed{\liminf_{n\to\infty}\frac{L_n\prod_{j=1}^m\sqrt{V_{j,n}}}{\binom nt}\ge(2\pi)^{-m/2}.}
\tag{A}
\]

In particular, no limiting sampling density is required, and densities tending to zero or one are permitted. Equivalently, with

\[
K_m=\prod_{j=1}^m\sqrt{2j+1}\binom{2j}{j}j!,
\]

\[
L_n\ge\left(\frac{K_m}{(2\pi)^{m/2}}-o(1)\right)
\frac{\binom nt}{n^{m(m+1)/2}[t(n-t)/(n-1)]^{m/2}}.
\tag{B}
\]

For example, when `t -> infinity` and `t=o(n)`, the denominator is `n^{m(m+1)/2} t^{m/2}` up to a factor tending to one. The original fixed-density formula follows immediately.

### Proof of the stronger CLT hypothesis

Put `Y_j=sum_{x in S} B_j(x)` and `Z_j=Y_j/sqrt(V_j)`. Exact sampling covariance gives `Cov(Z)=I_m`. For fixed nonzero `u in R^m`, use population values

\[
a_x=\sum_j u_jB_j(x)/\sqrt{V_j}.
\]

Their mean is zero and their sample-variance convention is

\[
v_n=\frac1{n-1}\sum_x a_x^2=\frac{n\lVert u\rVert^2}{t(n-t)}.
\]

Define the quantity independent of `t`

\[
H_{m,n}=\max_{0\le x<n}\sum_{j=1}^m B_j(x)^2/\sigma_{j,n}^2.
\]

Cauchy–Schwarz gives the useful exact inequality

\[
\frac{\max_x a_x^2}{\min(t,n-t)v_n}
\le\frac{n-1}{n}\frac{H_{m,n}}{\min(t,n-t)}.
\tag{C}
\]

For fixed `m`, the Gram formula gives `sigma_j^2=Theta_m(n^{2j})` and `max_x |B_j(x)|=O_m(n^j)`, so `H_{m,n}=O_m(1)`. Thus (C) tends to zero under the strengthened hypothesis. The finite-population CLT and Cramér–Wold prove `Z_n => N(0,I_m)`.

The original proof's bound `O(1/n)` under fixed density is replaced by `O_m(1/min(t,n-t))`. This is the only substantive change needed in its proof. Also `min_j V_{j,n}->infinity`, so its lattice mesh still tends to zero. The original fixed-radius argument, followed by the separate limit in radius, proves (A); its diagonal argument still permits classes whose standardized signatures tend to zero.

The precise external theorem used here is [Li–Ding, arXiv:1610.04821v1, Theorem 1](https://arxiv.org/pdf/1610.04821), checked directly in the primary PDF on 2026-09-15. It is a classical Hájek finite-population CLT. This note makes no novelty claim for that theorem or the Gram identity.

## 2. Alternative proof using Gaussian weights

This argument avoids ellipsoid lattice counts and yields a finite-size inequality. Suppose a random variable `Y` has finite support in `A Z^m+b`, where `A` is real unit lower triangular. Its atom probabilities are `p_y`, and `max_y p_y = L/C` when its distribution comes from `C` equally likely subsets. For arbitrary `V_j>0`, let `Z_j=Y_j/sqrt(V_j)`. For every `lambda>0`,

\[
\boxed{\frac LC\ge
\frac{\mathbb E\exp(-\lambda\lVert Z\rVert^2)}
{\prod_{j=1}^m(1+\sqrt{\pi V_j/\lambda})}.}
\tag{D}
\]

Indeed, a nonnegative weighting gives `E w(Y) <= (L/C) sum_{y in A Z^m+b}w(y)`. For every real shift `c` and `a>0`,

\[
\sum_{r\in\mathbb Z}e^{-a(r+c)^2}\le1+\sqrt{\pi/a}.
\tag{E}
\]

For completeness, apply the layer-cake identity to `f(x)=exp(-a x^2)`: at level `s in (0,1)`, its superlevel set is an interval of length `2 sqrt(-log(s)/a)`, and a shifted integer lattice has at most this length plus one points in the interval. Integrating over `s` proves (E). In the lattice sum, sum the last integer coordinate first. Its center depends only on earlier coordinates, so (E) bounds it uniformly. Repeat in reverse order to obtain the denominator of (D). Tonelli's theorem applies because every summand is nonnegative.

For the Gram signature, `E ||Z||^2=m` exactly. Jensen therefore makes (D) fully explicit for every finite `n>m` and `1<=t<n`:

\[
\boxed{L\ge
\left\lceil\binom nt\frac{e^{-\lambda m}}
{\prod_{j=1}^m(1+\sqrt{\pi V_{j,n}/\lambda})}\right\rceil.}
\tag{F}
\]

One may optimize over `lambda>0`; `lambda=1/2` is a simple choice. This is a real analytic lower bound; a claimed integer certificate from its numerical evaluation must control rounding. It is not necessarily better than existing exact signed-polynomial certificates.

For the asymptotic theorem, bounded-continuous convergence gives, for each **fixed** `lambda`,

\[
\mathbb E e^{-\lambda\lVert Z_n\rVert^2}\to (1+2\lambda)^{-m/2}.
\]

Multiplying (D) by `prod sqrt(V_j)` and taking `liminf` gives

\[
\liminf_n\frac{L_n\prod_j\sqrt{V_j}}{\binom nt}
\ge\left(\frac{\lambda}{\pi(1+2\lambda)}\right)^{m/2}.
\]

Now let `lambda -> infinity`, **after** the limit in `n`. This proves precisely (A), without a local CLT, shrinking-ball estimate, or prescribed-signature assertion. It does not by itself establish the central-choice refinement; the original fixed-ball diagonal argument does.

## 3. Finite-field interpretation

The real/rational Gram transformation is used only to count classes of integer signatures. Do not reduce its denominators modulo a prime. Equality of the first `m` integer binomial-moment sums implies equality of the first `m` ordinary power sums, since each `x^j` is an integer combination of `binom(x,i)`, `i<=j`. For any prime `p>n` and `m<t<=n`, Newton identities over `F_p` then make the first `m` elementary symmetric coefficients identical within a class.

Let `P_S(X)=prod_{a in S}(X-a)`, and choose `g` to be its common monic degree-`t` top part through degree `t-m`. Put `k=t-m`. The distinct polynomials `f_S=g-P_S` have degree `<k`, and each agrees with the received word `g|_{0,...,n-1}` at exactly the `t` coordinates in `S`. Hence the length-`n`, dimension-`k` Reed–Solomon code over every prime `p>n` has a list of size at least `L_n` at relative radius `(n-t)/n`.

No no-wraparound hypothesis on the integer moments is needed: equality over the integers implies equality after reduction. Only domain distinctness and the inverses in Newton's identities are used. No distributional claim over a finite field, specific transform domain, fixed-gap linear-list theorem, or protocol acceptance claim follows from this argument.

## 4. Qualifications and audit outcome

- Original constant, covariance normalization, triangular lattice argument, and sequential limits are correct.
- The sampling-density hypothesis can be weakened as in (A). Fixed `m` remains essential to this proof.
- If `min(t,n-t)` stays bounded, this CLT proof fails. We make no Gaussian constant claim in that regime.
- Gaussian weighting proves an explicit finite-size bound (F), but neither it nor the CLT gives a finite-size error estimate for the sharper constant `(2pi)^(-m/2)`.
- For `n=64,t=34,m=2`, the expression `binom(n,t)/(2pi sqrt(V_1 V_2))` is about `5.6518e12`. It is an asymptotic reference value, **not a proven finite-size certificate**. Equation (F) with `lambda=1/2` is about `2.0667e12`, and is weaker than the existing degree-20 signed-polynomial certificate.
