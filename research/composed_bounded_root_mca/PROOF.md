# A common polynomial composition does not evade the bounded-root barrier

September 16 evening continuation. New proof candidate, self-reviewed;
not yet integrated into the manuscript. This is a restricted upper bound,
not the sought fixed-gap quadratic lower construction.

## Statement

Fix r>=1 and 0<rho_min<=rho_max<a<=1. Let D/n be in
[rho_min,rho_max], A>=a*n, and let phi in F[X] be any nonconstant
polynomial of degree B. Candidates are P=Q(phi(X)) of degree at most
D, where Q has at most r distinct algebraic roots; nonzero scalar
factors and all root multiplicities may vary. The zero candidate is
also allowed. The received words f,g on n distinct x-coordinates are
arbitrary; they need not be constant on phi-fibers.

In characteristic zero, or with p/n sufficiently large in terms of the
fixed parameters, the number of labels z with a candidate whose full
agreement support has size >=A and admits no degree-<=D interpolant
for g is O(n). The implied constant is uniform in B and phi. In
particular B may grow with n, and P may have an unbounded number of
distinct roots.

The proof extends the existing bounded-root argument by keeping the
fiber multiplicity explicitly. Its only additional ingredient is the
elementary bounded-linear-space lemma below.

## 1. A fixed low-dimensional linear space

Let U be an ell-dimensional subspace of degree-<=D polynomials, with
ell fixed. On a full agreement support of size >=A, there are at least
(A-D)^ell ordered ell-tuples whose evaluation functionals on U are
independent. At each step choose a nonzero polynomial in the kernel
of the previous evaluations: at least A-D remaining support points
do not vanish on it. Earlier chosen points do vanish and are not
counted again.

For a fixed independent tuple, interpolation in U against f+zg gives
an affine graph P_z=U0+zU1. Such a graph has at most n bad labels:
a bad full support must include a coordinate where agreement is not
identical in z, and that coordinate determines at most one label.
There are at most (n)_ell ordered tuples. Choosing one candidate per
bad label and double counting gives

    # bad labels <= n (n)_ell/(A-D)^ell <= n (n/(A-D))^ell.

No characteristic condition is needed. This is the H=0 specialization
of ../linear_differential_mca/PROOF.md, proved here for self-containment.

## 2. Effective length and the small-effective-length case

Put K=floor(D/B) and N=n/B, where N need not be an integer.
Every candidate has deg Q<=K. The space {Q(phi):deg Q<=K} has
dimension K+1 because composition with a nonconstant polynomial is
injective. Fix a sufficiently large constant N0, depending only on
r,rho_min,rho_max,a, as specified by the thresholds below.

If N<N0, then K+1<=rho_max*N0+1 is bounded. Section 1 and
A-D>=(a-rho_max)n give the asserted O(n) bound. This includes B>D,
when only constant candidates occur.

If N>=N0, choose N0>=2/rho_min, so

    (rho_min/2)N <= K <= rho_max*N.

Apply the bounded-root construction in the Y variable to Q, with
degree cap K and effective length N. The following details justify
that its incidence proof survives repeated Y-coordinates.

## 3. Common factors and clusters

Each equation phi(x)=y has at most B domain solutions. Therefore a
nonzero Y-polynomial of degree h vanishes at at most B*h of the
original x-coordinates. If three residual Q-candidates in a common
factor class are graph-noncollinear, their common agreement support
has size at most B*(h+s), where h is the residual degree and s the
number of distinct roots of the common factor. Graph collinearity is
preserved and reflected by composition, by its linear injectivity.

The original small-residual argument thus applies whenever
h+s<=a^3*N/16. Its collinear triples still contribute at most n bad
labels per graph, NOT N. Consequently each class has at most
16*n/a^3 bad labels, exactly the required scale.

Set delta=a^3/(128r). For a fixed set S of at most 3r Y-roots, place
their multiplicities in boxes of side floor(delta*K)+1. If the
outside multiplicity is at most r*delta*K, factoring the lower-corner
common factor leaves degree <=4r*delta*K<=a^3*N/32. Its root count
is <=3r. Taking N0>=96r/a^3 makes the preceding condition hold.
There are at most B0=(1+ceil(1/delta))^(3r) boxes. Thus such a
cluster contains at most C*n selected bad labels, C=16*B0/a^3,
uniformly in B, phi, and the positions of S.

## 4. Private heavy roots and quadruple incidence

Choose the same constant auxiliary monomial degree m as in the
bounded-root proof. That proof's Wronskian and gcd estimate takes
place entirely in Y, for four Q-candidates with private roots of
multiplicity at least delta*K. It bounds the degree of their common
incidence gcd away from the root union by

    24*K/(m+5) + beta,
    beta=(4r-1)*(M-1)/2,
    M=binom(m+3,3)-(m+1).

Adding the <=4r Y-roots and pulling back through phi gives at most

    B * (24*K/(m+5) + beta + 4r)

common x-agreements. Choose m and N0 so this is at most a^4*n/32,
and so delta*K>binom(binom(m+3,3)-1,2)*(4r-1). These are the
original thresholds with n,D replaced by N,K; K is a positive
fraction of N and all choices are uniform in B. The Wronskian only
needs p>m*K. The assumed sufficiently large p/n ensures this.

A quadruple without a private heavy root is charged to a cluster of
Section 3, giving at most 4*C*n*L^3 degenerate ordered quadruples
among L selected labels. Their common supports have size at most n.
The same fourth-incidence inequality as in the original proof gives

    a^4*n*L^4/16 <= a^4*n*L^4/32 + 4*C*n^2*L^3,

provided L>=6/a. Thus L<=128*C*n/a^4. Smaller L are also O(n).
The zero polynomial adds at most n bad labels. This completes both
effective-length cases.

## Scope checks

- There is one common phi for the entire candidate family. Label-dependent
  or candidate-dependent changes of variables are not covered.
- The argument does not assume fiber-invariant received words. It uses
  only the maximum fiber size B for common-agreement root counts.
- Every badness test remains in the original degree-D code on the
  original x-coordinates. Badness is not transferred to a quotient code.
- The graph bound is n, not n/B. Replacing it by n/B would be unjustified.
- Small n/B is covered by a bounded-dimensional linear space, not by
  claiming the large-effective-length Wronskian thresholds hold there.
- This does not settle general first-order or higher-order MCA.
