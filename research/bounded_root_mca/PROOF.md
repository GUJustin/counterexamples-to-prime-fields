# Arbitrary bounded-root candidates have linear MCA

September 16, 2026. Self-reviewed proof with passing exact checks.
This strengthens the fixed-power result to arbitrary root multiplicities. It is an upper bound excluding a family, not the desired
quadratic proximity-gap lower bound.

## Theorem

Fix r>=1 and 0<rho_min<=rho_max<a<=1. Let D/n lie in
[rho_min,rho_max], A>=a*n, and work in characteristic zero or with p/n
sufficiently large in terms of r,a. For sufficiently large n, the number
of bad full-support MCA labels on any received line, witnessed by a
degree-at-most-D polynomial with at most r distinct algebraic roots, is
O_{r,a}(n). Root positions, multiplicities, and nonzero scalars all vary.
The zero polynomial adds at most n labels.

Bad means that the full support {x:f(x)+z*g(x)=P(x)} has at least A
positions and admits no degree-D polynomial explanations for both f,g.
This is the same definition as Appendix G. Work over an algebraic closure
when discussing roots; an interpolant of degree <=D on >D base-field
points descends to the base field.

## 1. An affine polynomial pencil contains at most n bad labels

For fixed U,V of degree <=D, put P_z=U+zV. A bad full support for P_z
contains a coordinate where (f,g)!=(U,V). At that coordinate agreement
forces g!=V and determines the unique label z=(U-f)/(g-V). Therefore
at most n selected bad pairs can lie on this affine pencil. The same
statement applies to graph-collinear pairs (z,P), since two distinct
labels determine U,V uniquely.

## 2. A common factor with a small residual degree gives O(n) labels

Suppose all selected candidates have the form H*Q, for one fixed H
with at most s distinct roots, and deg Q<=K, with deg(H)+K<=D.
Assume K+s<=a^3*n/16. If three graph points (z,Q) are not collinear,
their line-incidence determinant is a nonzero polynomial of degree <=K.
Their common agreement support therefore has at most K+s positions:
outside the roots of H divide by H, and use the determinant.

For L selected distinct bad labels with L>=4/a, triple incidence is at
least a^3*n*L^3/8. Noncollinear triples contribute at most
(a^3*n/16)*L^3. Each ordered pair lies on a unique graph line, which
contains at most n selected bad labels by Section 1; hence collinear
triples contribute at most n^2*L^2. Thus

    L <= 16*n/a^3.                                    (2)

The bound also covers L<4/a since n>=1 and a<=1. No characteristic
assumption is used in this step. If K is just a uniform upper bound on
residual degrees, replace it within a class by min(K,D-deg H).

## 3. Almost all root multiplicity on a fixed small set

Set delta=a^3/(128r). Let S be any fixed set of at most 3r algebraic
roots. Consider candidates having total root multiplicity outside S at
most r*delta*D. Partition their exponents at the roots of S into boxes
of side w=floor(delta*D)+1. Within a box, factor the product H with the
lower-corner exponents. The residual degree is at most

    |S|*(w-1)+r*delta*D <= 4r*delta*D <= a^3*n/32.

If 3r<=a^3*n/32, Section 2 applies to each box. The number of boxes
is at most

    B0=(1+ceil(1/delta))^(3r).

Thus the total selected bad labels in this cluster are at most C*n,
where C=16*B0/a^3. The constants are uniform in S and in its locations.
The common factors can be considered over the algebraic closure. The
original candidates are over the base field, so the pencils through two
of them have base-field coefficients; alternatively use interpolation
descent on each full support.

## 4. Gcd bound when each candidate has a private heavy root

Take four nonzero polynomials P_i of degree <=D, each with at most r
roots. Suppose each P_i has a root a_i of multiplicity at least delta*D
which is not a root of any other P_j. Put

    N=binom(m+3,3), J=m+1, M=N-J.

If

    delta*D > binom(N-1,2)*(4r-1),
    characteristic zero or p>m*D,                     (3)

the N degree-m homogeneous monomials in the P_i are linearly independent.
Indeed a ratio of two distinct monomials has order of absolute value
at least delta*D at some private heavy root. A minimal q-term linear
relation, via its (q-1)-Wronskian, would imply

    max_i deg f_i - deg gcd(f_1,...,f_q)
        <= binom(q-1,2)*(|S|-1),

where S is the union of the roots of the P_i. To see the degree bound
when the monomial degrees differ, omit a term of largest degree for the
global Wronskian degree bound, and omit one of smallest order separately
at each root for the local bounds. All these Wronskians are constant
multiples. The left side is at least the rational degree of any ratio,
giving a contradiction to (3).

For two independent linear forms F,G in four variables, the evaluated
degree-m ideal (F,G)_m has dimension M and codimension J in the monomial
space. Let d_alpha be the monomial degrees and a_alpha(s) their root
orders. A basis of this subspace has sum of degrees at most the sum of
the largest M of the d_alpha: order the formal monomials by degree and
row-reduce from highest degree. Thus its Wronskian has degree at most

    sum_alpha d_alpha - binom(M,2).

The valuation-filtration argument from Appendix G gives

    sum_(s in S) ord_s W
      >= sum_alpha d_alpha - J*m*sum_i deg(P_i) - |S|*binom(M,2).

Here sum_s max_alpha a_alpha(s)<=m*sum_i deg(P_i). Removing the
root-supported factors from the gcd T of F(P_i),G(P_i), every ideal
element is divisible by T. The common-factor Wronskian identity gives

    deg T <= 4*J*m*D/M + (4r-1)*(M-1)/2
           = 24*D/(m+5) + (4r-1)*(M-1)/2.             (4)

No equality of the candidate degrees or root exponents is needed.

## 5. Count the tuples without private heavy roots by the cluster bound

Select one bad candidate at each bad label. Call a root heavy if its
multiplicity is at least delta*D. A quadruple lacking private heavy
roots has some member i all of whose heavy roots lie in the union of
the other three root sets. Fix those other three candidates; their union
has at most 3r roots. Every root of P_i outside this union has multiplicity
less than delta*D, so P_i belongs to the cluster of Section 3. There are
at most C*n choices for its selected bad label. Summing over the four
possible entries gives at most

    4*C*n*L^3

degenerate ordered quadruples. Candidates with no heavy roots are
included automatically.

For every remaining quadruple, four distinct challenge labels give the
same two independent linear forms as in Appendix G. Equation (4), plus
the at most 4r roots in S, bounds their common support. Choose

    m>=1536/a^4-5,
    (4r-1)*(M-1)/2+4r <= a^4*n/64,

as well as (3). Then common support is at most a^4*n/32. If L>=6/a,
fourth incidence gives

    a^4*n*L^4/16 <= (a^4*n/32)*L^4 + 4*C*n^2*L^3,

and therefore

    L <= 128*C*n/a^4 = 2048*B0*n/a^7.                (5)

The small-L case satisfies this bound too. At fixed positive rate all
length and exponent conditions eventually hold. A sufficiently large
constant lower bound on p/n gives p>mD. The resulting constants are
very poor, but depend only on r,a.

## Verification and scope

The unequal-degree Wronskian checker passes three fixtures with candidate
degrees up to 425, including differing degrees and differing root
multiplicities. It checks monomial rank, formal ideal dimension, both
filtrations, Wronskian degree and root-order accounting, and the gcd away
from the root union. A rank-three negative control with four shared-heavy-
root candidates shows why the private-root hypothesis is needed there.

The cluster checker verifies all 1,025 bad labels and all their full
supports in a length-4,096 example with degree cap 1,024 and at most two
roots per candidate. It also verifies a noncollinear three-label example
by exact interpolation, all 70 quadruples in a mixed heavy-root fixture,
and twelve exact parameter choices. These finite checks supplement the
written proof; they do not instantiate its very large asymptotic constants
on an enumerated received line.

The proof has been self-reviewed twice. No independent mathematical
review or novelty claim is made. The general nonlinear first-order
conjecture and the fixed-gap quadratic lower-bound target remain open.
Candidates with a growing number of distinct roots are not excluded by
the fixed-r theorem. There is no better.codes score improvement.
