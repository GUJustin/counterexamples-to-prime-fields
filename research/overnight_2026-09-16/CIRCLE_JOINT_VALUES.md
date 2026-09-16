# Refining circle collisions at the original support points

This is a further exact refinement of `CIRCLE_COLLISION_REFINEMENT.md`.
Its numerical effect for M31 is small. The small-field fixture gives a
visible improvement from 294 guaranteed labels to 302, with 373 observed.
The verifier selects the first maximizing product exponent in numeric order;
the earlier fixture selected a different maximizing class and observed 370.

## The joint count at each point

Retain the notation there: R_A=v-F_A/Y^(r+1), residual degree d, N supports,
each of size h in G=mu_M, all containing a fixed anchor. At any y in the
full norm-one circle U, both R_A(y) and F_A(y)/y^(r+1) satisfy

    z^p = c^(-1) y^(-d) z.

Their sum v(y) belongs to the same p-element linear subspace. For y in G,
let s_y be the number of supports containing y. Exactly s_y evaluations
R_A(y) equal v(y), since F_A(y)=0 if and only if y belongs to A. All other
evaluations therefore occupy at most p-1 bins. Consequently their total
colliding pairs at y are at least

    f_N(s_y) = binom(s_y,2) + P(N-s_y,p-1).

The earlier theorem retained only the first term. This additional term
counts pairs of supports that both omit y but have the same value there.
It does not double-count the shared-support collisions.

The function f_N is discretely convex: its forward difference is

    f_N(s+1)-f_N(s) = s - floor((N-s-1)/(p-1)),

which is increasing. Thus with one fixed anchor and total remaining
incidence N(h-1), write a,e=divmod(N(h-1),M-1). The total collision lower
bound on G is

    G_min = binom(N,2) + (M-1-e) f_N(a) + e f_N(a+1).

More generally, with b common anchors, balance the N(h-b) incidences over
M-b points and add b*binom(N,2). Exact incidence counts can replace this
balanced lower bound when known.

The remaining calculation is unchanged:

    C = d*binom(N,2) - G_min - (p+1-M)*P(N,p),
    J = min {j>=1 : P(N,j) <= floor(C/Q)}.

Here Q=p^2-p-1 for quadratic-field poles and Q=p^4-p^2 for quartic-field
poles. The point-value phase and the root-degree bound are the same ones
already proved for the original theorem.

## Exact product classes when r=0

For M a power of two, identify roots of G with exponents 0,...,M-1 and
anchor exponent 0. Let C_k(c) count k-subsets of {1,...,M-1} whose exponent
sum is c modulo M. An exact finite Fourier calculation gives

    C_k(c) = (1/M) sum_{d|M} R_d(c)
              * (-1)^(k+floor(k/d)) * binom(M/d-1,floor(k/d)),

where R_d is the Ramanujan sum. For d>1 a power of two it is d/2 when
d divides c, -d/2 when d/2 divides c but d does not, and zero otherwise;
R_1(c)=1. Indeed a character of order d gives generating polynomial
(1-(-z)^d)^(M/d)/(1+z); its degree-k coefficient is the displayed signed
binomial coefficient.

For h-subsets containing the anchor, select a c maximizing C_(h-1)(c).
The incidence of a nonzero exponent a in that class is exactly

    sum_{j=0}^{h-2} (-1)^j C_(h-2-j)(c-(j+1)a).

This follows by removing the factor (1+z*u^a) from the generating function.
It determines both the exact class size and every support incidence.

The producer uses a take-or-omit dynamic program. The independent verifier
uses the character formula above, checks exhaustive small classes, and
independently enumerates all 405 residual polynomials at all 961 points of
F31^2. The evidence is in `circle_product_verification.json`.

## M31 values

| M,h | Earlier refined bank | New joint-count and exact-product bank |
|---|---:|---:|
| 64,19 | 40446904889937 | 40446905204913 |
| 64,35 | 11674175862720502 | 11674175866824006 |
| 128,19 | 365153906390146587 | 365153907657996934 |
| 512,11 | 334185303254161863 | 334185312123996677 |

For the low-rate n=4096, K=64, T=86 example, the exact product class has
N=597986899829131351. This slightly strengthens the already certified
24.5949-bit threshold comparison. The new CIRCLE_PRODUCT_DYADIC.md certificate now optimizes this stronger
formula, including every product class, throughout the stated native
one-anchor dyadic family. Both parameter winners remain unchanged.
It does not optimize actual leading-coefficient class sizes or arbitrary
subclasses.

The extra-anchor discovery scan found no improvement among its screened
native dyadic candidates. It is recorded as a discovery result, not as an
independent exhaustive optimality theorem for extra anchors.
