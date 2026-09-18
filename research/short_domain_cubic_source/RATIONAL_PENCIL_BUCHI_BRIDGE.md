# Rational first-integral pencils: an exact quadratic bridge

This note gives a characteristic-zero restriction for a moving denominator, not a classification of all rational fibrations. No new positive construction is obtained.

## Primary input

Hector Pasten, *Representation of squares by monic second degree polynomials in the field of p-adic meromorphic functions*, Theorem 3.9, PDF page 5:
https://people.math.harvard.edu/~hpasten/preprints/pAdicTAMS.pdf

The theorem applies to a function field of a nonsingular projective curve over a characteristic-zero field. A monic quadratic taking square values at at least max(8,4(g+1)) distinct constant arguments must be a square polynomial or have constant coefficients. For the rational function field, g=0 and the threshold is eight. We may extend the constant field to its algebraic closure, so every constant quadratic value has a constant square root. This is a classical theorem, not a new ingredient claimed here.

## Proposition: a linear moving denominator forces an affine family

Let k be algebraically closed of characteristic zero, K=k(X), and

    N=n2 u²+n1 u+n0,   D=d1 u+d0,

with coefficients in K, n2*d1 nonzero, and gcd(N,D)=1 in K[u]. Suppose there are polynomial sections P_i in k[X] and at least eight distinct constants c_i with N(X,P_i)=c_i D(X,P_i). Then all polynomial sections of the rational pencil belong to one affine family

    P=A(X)+s B(X),  s in k,

where A,B are polynomials and B is nonzero. If the selected sections have degree at most m, A and B can be chosen of degree at most m.

Proof. Define the monic quadratic in the constant parameter C

    F(C)=[(n1−C d1)²−4n2(n0−C d0)]/d1².

For every section label c_i,

    F(c_i)=[(2n2 P_i+n1−c_i d1)/d1]²

is a square in K. Pasten's theorem implies F is square in K[C] or has constant coefficients. The first alternative is impossible: N−CD is irreducible over K(C) as a polynomial in u because it defines the degree-two rational function N(u)/D(u). More elementarily, any factorization of the polynomial linear in C would force a C-independent factor dividing both N and D, after Gauss's lemma. A square discriminant would factor this quadratic, contradicting coprimality.

Thus F belongs to k[C]. Every section has the form

    P=−n1/(2n2)+(d1/(2n2))*(c±sqrt(F(c))).

It lies in a fixed affine K-function family with scalar coefficient. Distinct section labels yield distinct functions and hence distinct scalar coefficients. Choosing two distinct polynomial sections as affine generators makes both generators polynomial; if their degrees are at most m, so are the generators. The same affine line contains all other polynomial sections. This proves the claim.

### Agreement consequence

For distinct members A+s_i B of degree at most m and any word on n distinct coordinates, let each candidate have at least a agreements. The common coordinates B(x)=0 number at most m. At every other coordinate at most one candidate can match. Hence

    L(a−m) ≤ n.

In particular a fixed positive surplus a−m≥eta*n bounds L≤1/eta. The eight-label theorem concerns labels; each quadratic fiber has at most two sections. Thus even when fewer than eight labels occur there are at most fourteen polynomial sections, and no growing bank is hidden in repeated labels.

This excludes a large-list construction from the stated characteristic-zero quadratic/linear rational pencil. It does not assert a characteristic-uniform finite-field theorem. In particular it cannot be applied to Dickson's quartic/quadratic first integral by changing its degrees silently.

## Follow-up and a geometric diagnostic

A general quadratic denominator need not have a rational root over k(X), but a splitting cover is unnecessary: reciprocal normalization at one existing square discriminant value handles this case. The subsequent `RATIONAL_PENCIL_MOBIUS_BRIDGE.md` proves the Möbius-family conclusion and its agreement bound. `QUADRATIC_QUADRATIC_HEIGHT_GATE.md` extends it to characteristic p>max(2,10D). The earlier apparent quadratic-denominator escape is therefore closed. Higher u-degree pencils remain outside these results.

For general coprime N,D define

    J=N_u D−N D_u,  K0=N_X D−N D_X.

On a section N(X,P)=cD(X,P), differentiation gives K0(X,P)=−J(X,P)P′. Off the base locus N=D=0, a point determines c uniquely. Consequently sections with different labels have disjoint critical support there; shared basepoints are precisely where the earlier common-denominator critical-length counting argument fails. A successful growing bank must make the available critical mass concentrate at common basepoints, or make the sectionwise critical polynomial unusually small. This is a diagnostic, not a proved general upper bound.

At a simple basepoint (x,u0), the first-order section identity is

    (N_u−cD_u)(x,u0) P′(x) + (N_X−cD_X)(x,u0)=0.

When the first coefficient is nonzero this prescribes a derivative rationally in c. This could support a refined incidence argument, but by itself does not construct many sections or imply that c agrees with a received-line challenge. No automatic Hermite transfer is claimed.
