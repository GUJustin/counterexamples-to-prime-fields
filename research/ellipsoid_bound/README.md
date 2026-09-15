# Finite ellipsoid concentration on triangular moment lattices

This note audits and strengthens the finite lattice bound in
`ellipsoid_moment_bound_audit.md`. It concerns coding theory and finite
probability distributions. It makes no claim about a concrete proof system.

## 1. An exact finite bound

Let a population of size N have statistic B in the affine lattice
Λ = b + T Z^m, where T is lower triangular with diagonal entries one.
Let L be the largest statistic-class size, μ = E B, and Σ = Cov(B).
Write κ_m = π^(m/2)/Γ(m/2+1). Then

    L ≥ N / [κ_m (m+2)^(m/2) sqrt(det(Σ + I/12))].             (1)

In particular, writing V_j = Var(B_j),

    L ≥ N / [κ_m (m+2)^(m/2) ∏_j sqrt(V_j + 1/12)].         (2)

Formula (1) is at least as strong as (2), by Hadamard's determinant
inequality. If the coordinates are pairwise uncorrelated, the formulas
coincide. Variances may be zero: the added I/12 makes the smoothed
covariance positive definite. The original note's V_j > 0 assumption is
needed for its unsmoothed standardization, but not for (1) or (2).

**Proof.** The sets λ + [-1/2,1/2)^m partition R^m. To locate x's cell,
choose z_j recursively as the unique integer for which

    x_j - b_j - Σ_(i<j) T_ji z_i - z_j ∈ [-1/2,1/2).

This also proves uniqueness; neither rational entries nor bounded
off-diagonal entries are needed. Covolume one alone would not suffice.

For U independent and uniform on [-1/2,1/2)^m, Y = B+U has density
bounded by L/N and covariance W = Σ+I/12. Whiten Y by W^(-1/2) and
center it at μ. The resulting Z has E||Z||²=m and density bounded by
M = (L/N)sqrt(det W). For R²>m,

    R²-m = E(R²-||Z||²)
         ≤ M ∫_(R^m) (R²-||z||²)_+ dz
         = M · [2κ_m/(m+2)] R^(m+2).

The right ratio is optimized at R²=m+2. Rearranging proves (1).
Hadamard's inequality proves (2). All statements use the actual mean.

This proof avoids any point-counting approximation or enlargement of
the ellipsoid. The additive 1/12 is the exact variance of a unit cell.
The continuous second-moment/density inequality is elementary; no claim
of novelty is made for it. The contribution here is its explicit use
with the triangular moment lattice and the resulting finite constants.
For m=1 the result is sharp on a uniform distribution on consecutive
integers: L ≥ N/sqrt(12V+1), with equality before integer rounding.

## 2. Consequences for moment fibers

Let B_j be sums over uniformly chosen t-subsets of {0,...,n-1} of

    binom(a,j) + Σ_(i<j) c_ji binom(a,i).

The integer binomial-moment signatures lie in Z^m. Thus these transformed
signatures lie in a unit-diagonal triangular lattice. Each fiber agrees
on the original first m moments, so the paper's equal-moment construction
turns a fiber into a list at t agreements and dimension k=t-m.

For two moments, choose

    b_1(a) = a,
    b_2(a) = binom(a,2) - (n-2)a/2.

Their subset sums are uncorrelated and have variances

    V_1 = t(n-t)(n+1)/12,
    V_2 = t(n-t)(n+1)(n²-4)/720.

Hence the entirely explicit finite conclusion is

    L ≥ binom(n,t) / [4π sqrt((V_1+1/12)(V_2+1/12))].        (3)

For fixed t/n → ρ in (0,1), this gives

    L ≥ [3sqrt(60)/(πρ(1-ρ)) + o(1)] · binom(n,t)/n^4.

The paper's rectangular Chebyshev argument has constant
3sqrt(60)/(8ρ(1-ρ)). The ellipsoid argument improves that leading
constant by 8/π. In dimension m the corresponding ratio is

    (m+2) 2^(m-1) / κ_m.

The exact multiplicative finite correction to the uninflated ellipsoid
expression is ∏_j(1+1/(12V_j))^(-1/2). It tends to one whenever
Σ_j 1/V_j = o(1), including when m grows. This is stronger than the
condition needed by a proof using worst-case cell-radius inflation.

## 3. Exact optimization of quadratic lattice weights

For a lattice statistic with positive variances, put
Q(λ)=Σ_j(λ_j-μ_j)²/V_j, so E Q(B)=m. Direct summation gives, for u>m,

    L ≥ N(u-m) / Σ_(λ∈Λ) (u-Q(λ))_+.                       (4)

The denominator includes unattainable signatures, which is permissible
because their weights are nonnegative. For fixed u, let c count the
lattice points with Q<u and let s sum their Q values. Away from a lattice
shell, the derivative of (u-m)/(cu-s) has the sign of mc-s.

Starting just above m this sign is positive. Each new shell q>m changes
mc-s by its multiplicity times (m-q), hence decreases it. Consequently
the global maximum occurs at the first shell where this sign changes
from nonnegative to nonpositive. Beyond that shell the objective cannot
increase. This gives an exact global optimizer using only an ordered
list of lattice quadratic values up to the crossing, without numerical
optimization or floating-point arithmetic.

For n=64,t=34, the means and shear are integers; the centered lattice is
Z². With (V_1,V_2)=(5525,376805), let d=V_1 V_2=2081847625 and
e(x,y)=V_2 x²+V_1 y². The certified optimum is

    u = 8327308730 / 2081847625.

There are 573367 points with e<8327308730 and four points on the boundary.
The exact sum of positive scaled weights is 2387288605450190. Thus

    L ≥ ceil(6746253002126536483649675520 / 2387288605450190)
      = 2825905919681.

The scaled derivative sign is 10035263030 before the boundary shell and
-6619190890 after it. These signs certify global optimality within (4).
The simpler choice u=4 gives 2825905919527, only 154 less. This small
gain should not be presented as a significant improvement in the paper.

Using π<355/113, the closed-form bound (3) certifies
L≥2825885263137 by integer arithmetic alone. These quadratic bounds
improve the unconditional rectangular concentration example, but they
remain below the existing conditional degree-20 certificate
L≥5074503250115. They do not replace that stronger finite result.

## 4. Verification

Run `python3 research/ellipsoid_bound/verify_lattice_bound.py` from the
repository root. The standard-library checker verifies:

- 4096 rational triangular-cell fixtures, including nonintegral and
  negative shears, and exclusion of all adjacent alternative centers;
- 44 exhaustive small subset distributions, comprising 2024 subsets,
  checking the signed second-moment identity and the exact lattice bound;
- the length-64 optimized certificate by exact shell enumeration;
- an independent row-sum calculation of the u=4 denominator;
- an integer-square-root certificate for the π<355/113 version of (3).

The JSON file records the resulting certificates. Finite tests accompany
the proofs; they are not substitutes for the general tiling or smoothing
arguments. No shared manuscript was changed by this audit.
