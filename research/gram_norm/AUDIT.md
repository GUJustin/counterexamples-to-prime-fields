# Independent audit: exact Gram norms and growing moment order

The formulas and proof in `gram_moment_norm_proof.md` are correct. The
following compact proof suffices for the manuscript. This is a classical
orthogonal-polynomial identity, not a new norm formula.

## Statement and short self-contained proof

Let `n >= 2` and `0 <= j < n`. With falling factorials and forward
differences, put

\[
F_j(x)=(x)_{\underline j}(x-n)_{\underline j},\qquad
G_j(x)=\frac{\Delta^j F_j(x)}{(2j)!}.
\]

The polynomial `G_j` has degree `j` and leading coefficient `1/j!`.
For every polynomial `p`, the boundary zeros of `F_j` at
`0,...,j-1,n,...,n+j-1` give the exact identity

\[
\sum_{x=0}^{n-1}p(x)\Delta^jF_j(x)
=(-1)^j\sum_{y=j}^{n-1}F_j(y)\nabla^jp(y).
\]

This follows simply by expanding the forward difference, shifting
`y=x+h`, and collecting terms. Thus `G_j` is orthogonal to every smaller
degree polynomial. As `nabla^j G_j=1`, taking `p=G_j` gives

\[
\begin{aligned}
\sum_{x=0}^{n-1}G_j(x)^2
&=\frac{(j!)^2}{(2j)!}
  \sum_{y=j}^{n-1}\binom yj\binom{n+j-1-y}j\\
&=\frac{(j!)^2}{(2j)!}\binom{n+j}{2j+1}.
\end{aligned}
\]

The last identity counts `(2j+1)`-subsets of an `(n+j)`-element ordered
set by their middle element. Consequently, for `X` uniform on the grid,

\[
N_j:=\mathbb E G_j(X)^2
=\frac{\prod_{i=1}^j(n^2-i^2)}
 {(2j+1)\binom{2j}j^2(j!)^2}.
\]

For `j>=1` the mean is zero, so this is also the variance.

## Exact use in the manuscript's triangular moment bound

The manuscript excludes a constant term from its `b_j`. Set
`b_j(x)=G_j(x)-G_j(0)`, which has precisely the required form
`binom(x,j)+sum_{1<=i<j}c_ji binom(x,i)` with rational coefficients.
Subtracting this constant has no effect on variances or covariances.
For uniformly random `t`-subsets, the exact covariance matrix of the
subset sums is diagonal and

\[
V_j=\frac{t(n-t)}{n-1}N_j.
\]

Therefore these values can be substituted directly in the existing
concentration proposition for **every** `1<=m<t<n`; no fixed-`m`
assumption is needed for the exact finite bound. Orthogonality gives
uncorrelated subset sums, not independence.

Each `G_j` minimizes variance among polynomials with leading coefficient
`1/j!`: write any competitor as `G_j+q`, with `deg q<j`, and use
`Var(G_j+q)=N_j+Var(q)`. Equality allows a constant. Thus this choice
simultaneously minimizes the variances, and hence the denominator of the
existing bound, among its triangular changes of coordinates. This is
not a claim that its Chebyshev/union-bound argument is optimal.

For fixed `m` and `t/n -> rho in (0,1)`, the resulting leading constant
in front of `binom(n,t)/n^(m(m+2)/2)` is

\[
2^{1-m}(m+2)^{-1-m/2}[\rho(1-\rho)]^{-m/2}
\prod_{j=1}^m\sqrt{2j+1}\binom{2j}j j!.
\]

For `m=2` this reduces to the manuscript's
`3 sqrt(60)/(8 rho(1-rho))`.

## Endpoint checks

- `j=0`: `G_0=1`, squared norm `1`, variance `0`.
- `j=1`: variance `(n^2-1)/12`.
- `j=2`: variance `(n^2-1)(n^2-4)/720` when `n>=3`.
- `j=n-1`: squared norm `1/[n binom(2n-2,n-1)]`, which is strictly
  positive even though small. The formula remains exact here.
- At `j>=n`, positive definiteness fails and the stated theorem does not
  apply. Likewise `t=0,n` gives deterministic subset sums; the manuscript
  already excludes these endpoints.
- These are real/rational identities used for counting. There is no
  need to reduce the Gram coefficients modulo the code's prime.

## What changes when m grows

Writing

\[
N_j=\frac{n^{2j}}{(2j+1)\binom{2j}j^2(j!)^2}\,R_j,
\qquad R_j=\prod_{i=1}^j\left(1-\frac{i^2}{n^2}\right),
\]

and `S_j=j(j+1)(2j+1)/6`, the elementary logarithm bounds give, for
every `j<n`,

\[
-\frac{S_j}{n^2(1-j^2/n^2)}\le\log R_j\le-\frac{S_j}{n^2}.
\]

Thus the continuum approximation to each norm is uniform over
`j<=m` when `m=o(n^(2/3))`. When multiplying all standard deviations,
however, the correction accumulates. Exactly,

\[
\log\prod_{j=1}^m\sqrt{R_j}
=\frac12\sum_{i=1}^m(m-i+1)\log(1-i^2/n^2).
\]

Let `A_m=m(m+1)^2(m+2)/12`. For all `m<n`,

\[
-\frac{A_m}{2n^2(1-m^2/n^2)}
\le\log\prod_{j=1}^m\sqrt{R_j}
\le-\frac{A_m}{2n^2}.
\]

For `m=o(n)`, the sharper expansion is

\[
\log\prod_{j=1}^m\sqrt{R_j}
=-\frac{m(m+1)^2(m+2)}{24n^2}
 +O\!\left(\frac{m^6}{n^4}\right).
\]

Hence the product of norms is continuum-equivalent only when
`m=o(sqrt(n))`; if `m/sqrt(n)->c`, its square-root product has the
nontrivial factor `exp(-c^4/24)`. Any growing-`m` conclusion must also
retain the factorial constants, the `(m+2)` factors, and ceiling errors
from the finite concentration bound. The exact formula is safer than
extending the manuscript's fixed-`m` big-O statement by substitution.

## Independent evidence and attribution

`verify_gram_norm.py` uses exact `Fraction` arithmetic and independently
orthogonalizes sampled binomial polynomials, then compares with the
Rodrigues expression and both norm formulas. It covers every degree
through `n-1` for `2<=n<=24`, checks summation by parts also against
higher-degree polynomials, and exhaustively verifies the finite-subset
covariance formula for `n<=10`. `verified.json` records counts.

The primary source [Lin and Wong, *Global Asymptotics of the Discrete
Chebyshev Polynomials*, equations (1.1)--(1.2)](https://arxiv.org/pdf/1207.2536)
uses `t_j=Delta^j F_j/j!`; multiplying their norm by
`(j!/(2j)!)^2` gives the formula above. Their grid size is their `N`,
and their degree is their `n`. The manuscript's symbols reverse those
roles. [DLMF 18.19](https://dlmf.nist.gov/18.19) gives the corresponding
Hahn family. The simpler self-contained proof avoids any normalization
ambiguity in citing these classical identities.
