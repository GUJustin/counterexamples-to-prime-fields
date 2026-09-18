# Square-quadratic banks: an explicit grid obstruction and a nonplanar core

2026-09-18. Bounded route calculation for Q_(a,b)(X)=(aX+b)² in odd characteristic. The bank is not generally equivalent to the old planar bank. The simplest dense integer selection nevertheless fails as a growing-agreement core, for an exact incidence reason. A sparse explicit selection supplies a nonplanar rational core, but no improved fresh-label theorem is proved.

## 1. Why pairwise splitting alone is insufficient

For distinct parameters, the difference factors as

    Q_(a,b)−Q_(c,d)=[(a−c)X+(b−d)][(a+c)X+(b+d)].

This guarantees rational pair intersections when both factors are nonconstant, but does not guarantee two roots for every pair (equal slopes lose a root), distinct roots, distinct coordinates across pairs, or compatible received values at shared coordinates. Those are separate requirements.

Consider the explicit full grid

    1≤a,b≤H,     L=H²,

over a prime p>8H². Its bank polynomials are all distinct. Every finite pair-intersection coordinate has a reduced rational representative x=u/v with v>0 and

    max(|u|,v)≤2H.

The reduction of these fractions modulo p is injective: a nonzero cross determinant has absolute value at most 8H²<p. Thus there are only O(H²) collision coordinates, even though there are Θ(H^4) pairs.

The decisive issue is not just the coordinate count. Let q=max(|u|,v). For any chosen received value w at x, bank matches obey

    (a u+b v)²=v²w mod p.

If any bank word matches, fix one integer value c=a0u+b0v. Every other match must satisfy a u+b v≡±c mod p. Since all such integers have magnitude at most 4H², the guard p>8H² turns these into literal integer equalities. For each sign, the integer points in the H×H parameter box lie along the primitive direction (v,−u), so there are at most

    1+floor((H−1)/q)

of them. Therefore the largest received-value bucket at this coordinate is at most 2(1+(H−1)/q).

There are at most 4q reduced representatives of height q. Summing over all possible pair-intersection coordinates gives the uniform bound

    total chosen core incidences
      ≤ Σ_(q=1)^(2H) 4q·2(1+(H−1)/q)
      ≤32H² =32L.

This holds for EVERY received word and EVERY subset of those coordinates. The average bank agreement on a collision-only core is therefore at most 32. If a selected collection of bank words all has at least A core matches, its size is at most 32L/A. In particular the full L~H² bank cannot have growing regular agreement A~H on an O(H²)-point core.

Coordinates outside the pair-intersection set have buckets of size at most one. On any n-point domain the full-bank incidence sum is consequently at most n+32L. Adding arbitrary coordinates does not silently restore the lost Θ(L²) pair incidences. This is a scoped obstruction for the full integer parameter grid, not all square-quadratic selections or small-characteristic modular realizations.

## 2. The square bank is genuinely nonplanar

The coefficient points of the grid bank are

    (a²,2ab,b²) in affine coefficient space.

For H≥3 and p>8H² they have affine span three. Indeed an affine relation A a²+2B ab+C b²=D, holding on the grid, is a quadratic identity in a for each of at least three b values. It forces A=B=0, then C=D=0.

The old bank θ+X²/θ lies in the affine plane whose X coefficient is zero. Adding the same polynomial to every bank word translates coefficient space. A Möbius coordinate substitution with its standard degree-two GRS multiplier acts by the invertible symmetric-square representation on binary-quadratic coefficients. Common scaling is also invertible linear. These operations preserve affine-span dimension. Hence the full square grid cannot be transformed to the old bank by any combination of these operations.

This is a genuine distinction even though both descriptions involve conics: the square bank lies on a quadratic cone in three-dimensional affine coefficient space, not in one affine plane. Candidate-dependent rescaling is not an allowed escape from this argument, because it does not preserve agreement with one common received word.

The subfamily a=1 is a different degenerate case: all leading coefficients coincide, and subtracting X² leaves affine polynomials. Each distinct pair then has only one finite intersection. It does not exploit the intended three-coefficient freedom.

## 3. An explicit sparse nonplanar bank with a perfect rational core

There is no universal obstruction to regular cores for square banks. Let t_i=3^i, 1≤i≤L, and take

    Q_i(X)=(t_i X+t_i²)².

For i<j, the two distinct rational intersection coordinates are

    x_ij^+=−(t_i+t_j),
    x_ij^−=−(t_i²+t_j²)/(t_i+t_j).

All these coordinates are distinct. To see this, set T=t_j and u=t_i≤T/3. The positive magnitudes of the two roots lie respectively in (T,4T/3] and (2T/3,T). Different maximal indices j give disjoint combined intervals. For fixed j, T+u is strictly increasing, while (T²+u²)/(T+u) is strictly decreasing for 0<u≤T/3, since its derivative has numerator u²+2Tu−T²<0.

Thus this bank has a rational core of L(L−1) points, each owned by exactly two bank polynomials, with A=2(L−1) matches per bank word and at most L matches for any outsider quadratic. It has affine coefficient span three for L≥5: an affine relation on (t_i²,2t_i³,t_i^4) would be a degree-four polynomial with at least five distinct roots, hence zero.

For an explicit sufficient good-reduction bound, put T_max=3^L. Numerators of the second root type have magnitude ≤2T_max² and denominators ≤2T_max. A difference of two distinct roots has nonzero cross numerator of magnitude ≤8T_max³. Every prime p>8T_max³ therefore preserves all root distinctness and the core incidences. No splitting-prime theorem is needed. This bound is exponential in L; it is a sufficient bound, not a proof that smaller good primes do not exist.

This sparse bank demonstrates a valid nonplanar core, but its parameter heights do not currently support the compact arithmetic grid bundling that produced the earlier polynomial gaps. Merely having rational split differences is not a fresh-label multiplicity theorem.

## 4. Fresh-block interface and remaining constructive requirement

For a general square bank, after setting U=1/g, V=x²/g, Z=x/g and W=f/g, its label becomes

    λ=b²U+2ab Z+a²V−W,      Z²=UV.

The additional linear coefficient therefore introduces the coordinate Z, but it is constrained by the rank-one relation Z²=UV; it is not an independent third rectangular-grid coordinate. Any proposed fresh set must also assign a unique f and g to each actual evaluation coordinate x. A product box that repeats x with different values is invalid.

The full integer-grid bank is closed by the incidence bound in section 1. The sparse exponential selection in section 3 escapes that obstruction and is not equivalent to the old planar bank, but a useful larger-loss construction would still require a compact-height selection and a fresh-block structure with both large label fibers and a uniform exclusion of every nonbank quadratic. No such fresh structure follows from the two linear factors of pair differences. No improved gap, count, or alphabet theorem is claimed here.
