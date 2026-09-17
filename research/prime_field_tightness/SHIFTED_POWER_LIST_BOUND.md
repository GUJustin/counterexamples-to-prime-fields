# Characteristic-zero list bound for a common scaled-power family

September 17, 2026. Locally audited proof; no novelty claim. This rules
out one variable-degree candidate family for a characteristic-zero
source construction. It is not an arbitrary prime-field list bound.

Let x_1,...,x_n be distinct complex nodes, w an arbitrary received word,
and m>=1 an integer. Among the distinct polynomials

    P(X)=(uX+v)^m,  u,v in C,

at most

    2*binom(n,3)/binom(A,3)                             (1)

can have at least A>=3 agreements with w. This includes arbitrary scalar
multiples of shifted mth powers, since scalars have mth roots in C.
The bound is independent of m. At a fixed positive agreement fraction,
it is constant even if m grows with block length.

## At most two candidates on any three distinct nodes

Suppose prescribed values y_i are matched at three distinct x_i. If all
three values are zero, the only possible polynomial is zero. Otherwise
form the Hermitian positive semidefinite rank-one matrix determined by
(u,v), so that

    |u x+v|^2 = a |x|^2 + b x + conjugate(b) conjugate(x) + c,
    a=|u|^2, b=u conjugate(v), c=|v|^2.

Agreement imposes three REAL LINEAR equations on the four-dimensional
real space of Hermitian2-by2 matrices, with right sides |y_i|^(2/m).
These equations are independent. To see this, their coefficient matrices
are three positive semidefinite rank-one matrices for three distinct
projective vectors (x_i,1). A nontrivial real relation among them would,
after separating signs, equate one rank-one positive semidefinite matrix
to a positive sum of two nonproportional rank-one matrices. The latter
has rank two, a contradiction. Relations supported on fewer terms are
also impossible because the vectors are pairwise nonproportional.

The solution space is therefore an affine real line M_0+sH. Its nonzero
Hermitian direction H vanishes on three distinct vectors (x_i,1). H
cannot be definite, or nonzero semidefinite: a semidefinite rank-one
form vanishes on only one projective vector. Thus H is indefinite and
has nonzero determinant. The equation

    det(M_0+sH)=0

is a genuine quadratic in s, with at most two real solutions. Hence
there are at most two positive semidefinite rank-one matrices.

For a given nonzero matrix, (u,v) is determined up to a common complex
phase. Consequently P=(uX+v)^m is determined up to a scalar of modulus
one. Matching any prescribed nonzero y_i fixes this scalar. There are
therefore at most two distinct polynomials P matching all three values.
Double-counting pairs (candidate, agreeing triple) proves (1).
The argument applies to every characteristic-zero field by embedding
the finitely generated field of the relevant finite configuration into C.

## Common polynomial offsets and multipliers

For fixed S,R with R nonzero, consider candidates

    P=S+R(uX+v)^m.

Delete the h domain nodes at which R vanishes, and divide w-S by R on
the remaining nodes. If A-h>=3, the same proof bounds the candidate
list by

    2*binom(n-h,3)/binom(A-h,3).                        (2)

Counting all R-zero nodes as agreements only weakens this upper bound.
If deg S<k and deg R+m<k, these candidates belong to the dimension-k
RS code. At threshold A>=k+eta*n one has

    A-h >= A-deg R >= eta*n+m+1.

Thus for fixed eta>0 and sufficiently large n, (2) is O(eta^-3),
uniformly in the growing exponent m and the common polynomials S,R.
This covers a degree-growing residual family beyond the bounded-degree
rational envelopes already studied. It does not cover candidate-dependent
multipliers, arbitrary low-degree inner polynomials, or varying exponents.
Partitioning by exponent alone gives at most an extra factor k, so that
observation does not rule out growing mixed-exponent banks.

## Characteristic restriction is essential

Over F_p with p odd, the p distinct polynomials

    (X-a)^((p-1)/2), a in F_p,

each agree with the constant-one word on exactly (p-1)/2 of the p
nodes. For example p101 gives101 candidates with50 agreements, whereas
(1) would give 2*binom(101,3)/binom(50,3)<18. These agreements are BELOW
the code dimension51, so this is not a fixed-gap counterexample; it
simply demonstrates that the characteristic-zero lemma cannot be
asserted over finite fields, even with polynomial degree below p.
No uniform superpolynomial-field transfer threshold is proved here.
