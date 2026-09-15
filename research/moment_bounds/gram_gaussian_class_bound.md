# Gaussian lower bound for a central interval-moment signature class

Date: 2026-09-15. Scope: fixed-dimensional asymptotics for subsets of an integer interval. This is an application of the classical finite-population CLT and the classical Gram norm, with no novelty assertion, no local CLT, and no finite-`n` error estimate. No canonical manuscript edits.

## Result

Fix an integer `m>=1`. Let `t=t_n` satisfy `t/n -> rho` for a fixed `rho in (0,1)`. For a `t`-element subset `S` of `{0,...,n-1}`, define its integer moment signature

\[
M(S)=\left(\sum_{x\in S}{x\choose1},\ldots,
             \sum_{x\in S}{x\choose m}\right)\in\mathbb Z^m.
\]

Let `L_n` be the largest size of a signature class. For the normalized Gram polynomials `B_j` from `gram_moment_norm_proof.md`, set

\[
\sigma_{j,n}^2
=\frac{\prod_{i=1}^j(n^2-i^2)}
{(2j+1){2j\choose j}^{2}(j!)^2},
\qquad
V_{j,n}=\frac{t(n-t)}{n-1}\sigma_{j,n}^2,
\quad 1\le j\le m<n.
\tag{1}
\]

Then

\[
\boxed{\quad
\liminf_{n\to\infty}
\frac{L_n\prod_{j=1}^m\sqrt{V_{j,n}}}{{n\choose t}}
\ \ge\ (2\pi)^{-m/2}.
\quad}
\tag{2}
\]

In fact one can choose classes satisfying this bound whose standardized Gram signatures tend to zero. An equivalent explicit asymptotic bound is

\[
L_n\ge (C_{m,\rho}-o(1))\,
\frac{{n\choose t}}{n^{m(m+2)/2}},
\quad
C_{m,\rho}=
\frac{\prod_{j=1}^m\bigl[\sqrt{2j+1}{2j\choose j}j!\bigr]}
{(2\pi\rho(1-\rho))^{m/2}}.
\tag{3}
\]

## 1. Exact covariance and a finite-population CLT

Choose `S` uniformly among all `t`-subsets and put

\[
Y_j(S)=\sum_{x\in S}B_j(x),\qquad
Z_{n,j}=Y_j(S)/\sqrt{V_{j,n}}.
\]

The population means of `B_j` vanish and their population covariances are zero for distinct degrees. The standard sampling-without-replacement covariance formula gives

\[
\mathbb E Y_j=0,\qquad
\operatorname{Cov}(Y_i,Y_j)=\mathbf1_{i=j}V_{j,n}.
\tag{4}
\]

Thus `Cov(Z_n)=I_m` exactly.

### Primary theorem and its hypotheses

[Li–Ding, *General forms of finite population central limit theorems with applications to causal inference*, arXiv:1610.04821v1, Theorem 1, equations (2)--(4)](https://arxiv.org/pdf/1610.04821) state the following Hájek-type sufficient condition. For a population of size `N`, sample size `q`, population variance

\[
v_N=\frac1{N-1}\sum_i(y_i-\bar y)^2,
\quad
d_N=\max_i(y_i-\bar y)^2,
\]

if

\[
\frac{d_N}{\min(q,N-q)v_N}\longrightarrow0,
\tag{5}
\]

the sample mean, centered and divided by its exact standard deviation, converges to `N(0,1)`. The paper explicitly attributes the classical theorem to Hájek; Appendix A1 discusses its relation to the original Lindeberg condition. This condition permits triangular arrays and is invariant under rescaling the population values.

### Verification for every Cramér--Wold projection

Fix `u in R^m`, `u != 0`, and define population values

\[
a_{n,x}=\sum_{j=1}^m u_j B_j(x)/\sqrt{V_{j,n}}.
\]

Their mean is zero. Orthogonality and (1) give the **exact** finite-population variance

\[
v_n=\frac1{n-1}\sum_{x=0}^{n-1}a_{n,x}^2
=\frac{n\|u\|^2}{t(n-t)}=\Theta_u(n^{-1}).
\tag{6}
\]

For each fixed degree `j`,

\[
\max_{0\le x<n}|B_j(x)|=O_j(n^j),
\qquad V_{j,n}=\Theta_{j,\rho}(n^{2j+1}).
\tag{7}
\]

Here is a direct bound for the first assertion, avoiding an unstated uniform asymptotic. The identity

\[
\Delta^j F_j(x)=\int_{[0,1]^j}F_j^{(j)}(x+u_1+\cdots+u_j)\,du
\]

and the product rule for the `2j` linear factors of `F_j` imply

\[
|B_j(x)|\le\frac{(n+j)^j}{j!}
\quad(0\le x<n).
\]

The second assertion in (7) follows directly from (1) and `t/n -> rho`. Thus

\[
\max_x|a_{n,x}|=O_{u,m,\rho}(n^{-1/2}),
\qquad
\frac{\max_xa_{n,x}^2}{\min(t,n-t)v_n}=O_{u,m,\rho}(n^{-1})\to0.
\]

The cited theorem applies. Since the sample **sum** of these population values is `u dot Z_n` and has variance `||u||^2`, Cramér--Wold yields

\[
Z_n\ \Longrightarrow\ G\sim N(0,I_m).
\tag{8}
\]

Only fixed `m` and fixed projections `u` are used.

## 2. Counting the triangular lattice: the proposed epsilon is correct

The leading coefficient of `B_j` is `1/j!`, the same as `binom(x,j)`. Therefore

\[
B_j(x)={x\choose j}+\sum_{i=0}^{j-1}a_{ji}{x\choose i}.
\]

As subset size `t` is fixed,

\[
Y(S)=A_nM(S)+b_n,
\tag{9}
\]

where `A_n` is unit lower triangular and `b_n` is constant. Signature classes for `M` and `Y` coincide. Every Gram signature lies in the affine lattice

\[
\Lambda_n=A_n\mathbb Z^m+b_n.
\]

**Tiling fact.** For any real unit lower triangular `A` and any `b`, the half-open axis-aligned cubes

\[
\lambda+[-1/2,1/2)^m,\qquad\lambda\in A\mathbb Z^m+b,
\tag{10}
\]

tile `R^m`, up to boundary conventions. To locate the cube containing a point, choose its first integer lattice coordinate by rounding the first coordinate after subtracting `b_1`. Then choose the second after subtracting its already-determined first-coordinate shear, and proceed inductively. Every choice is unique with the half-open convention. In particular, **these cubes need not be the linear images of a standard fundamental parallelepiped**; replacing them by those images would introduce an unnecessary shear loss.

Let `D_n=diag(sqrt(V_{1,n}),...,sqrt(V_{m,n}))` and

\[
\epsilon_n=\frac12\sqrt{\sum_{j=1}^m V_{j,n}^{-1}}=O_{m,\rho}(n^{-3/2}).
\]

Under `D_n^{-1}`, the cubes in (10) become disjoint axis-aligned boxes of volume `1/prod_j sqrt(V_{j,n})`; every point of a box is within `epsilon_n` of its center. Thus for every `R>0`, if `N_n(R)` counts ambient lattice points satisfying `||D_n^{-1}lambda||<=R`, then

\[
N_n(R)\le
\left(\prod_{j=1}^m\sqrt{V_{j,n}}\right)
\omega_m(R+\epsilon_n)^m,
\quad
\omega_m=\frac{\pi^{m/2}}{\Gamma(m/2+1)}.
\tag{11}
\]

Only an ambient lattice containing the possible signatures is needed. No assertion that every ambient lattice point is attainable is made.

## 3. Fixed-radius pigeonhole, then a separate small-radius limit

For fixed `R>0`, (8) and the Gaussian's zero mass on the sphere imply

\[
p_n(R):=\Pr(\|Z_n\|\le R)\longrightarrow
p(R):=\Pr(\|G\|\le R).
\]

There are exactly `binom(n,t) p_n(R)` subsets in this ball, distributed among at most `N_n(R)` signatures. Therefore some class in the ball has size at least

\[
\frac{{n\choose t}\,p_n(R)}
{\bigl(\prod_j\sqrt{V_{j,n}}\bigr)\omega_m(R+\epsilon_n)^m}.
\tag{12}
\]

Taking `liminf` for this fixed radius gives

\[
\liminf_n\frac{L_n\prod_j\sqrt{V_{j,n}}}{{n\choose t}}
\ge\frac{p(R)}{\omega_mR^m}.
\tag{13}
\]

Now, **after the limit in `n`**, let `R` decrease to zero. Continuity of the Gaussian density at zero gives

\[
\lim_{R\downarrow0}\frac{p(R)}{\omega_mR^m}=(2\pi)^{-m/2},
\]

which proves (2). Formula (3) follows by inserting the asymptotics from (1).

### Optional genuinely central choice

A diagonal argument supplies an unspecified sequence `R_n -> 0` for which the bound in (12) still has normalized liminf at least `(2pi)^(-m/2)`: take fixed radii `R_h=1/h`; choose increasing cutoffs `N_h` such that for all `n>=N_h`, `p_n(R_h)>=(1-1/h)p(R_h)` and `epsilon_n<=R_h/h`; then use `R_n=R_h` between successive cutoffs. The selected class has standardized signature tending to zero. This supplies existence, **not an explicit shrinking rate**.

## What this argument does not establish

- It gives a lower bound on a maximum class, not an asymptotic equality or an upper bound.
- It does not give a local limit theorem or the mass of a prescribed single signature.
- It is not uniform in a growing number of moments `m`.
- It supplies no explicit finite-`n` convergence rate or finite certificate. Those require separate estimates or exact computation.
- The sequential limit in (13), or the nonquantitative diagonal choice, is essential; weak convergence alone cannot justify an arbitrarily specified shrinking radius.
