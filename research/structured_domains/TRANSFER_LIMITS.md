# Transferring interval certificates to multiplicative subgroups

Research note, September 15, 2026. These are elementary coding-theoretic
lemmas, with no novelty claim. They clarify which parts of the manuscript's
interval construction can survive a prescribed-domain restriction. They
do not establish an improved bound for a fixed cryptographic parameter set.

Throughout, RS(F,D,k) evaluates polynomials of degree less than k at D.
Its rate is k/|D|. The gap at agreement threshold t is (t-k)/|D|.

## 1. Affine changes of variable cannot identify the domains

**Lemma.** Let p be prime and let H be a proper multiplicative subgroup
of F_p^* of order n >= 3. No affine image of {0,...,n-1} equals a
multiplicative coset cH.

**Proof.** Suppose the image is {a+bi: 0 <= i < n}, with b != 0.
The first two power sums of cH vanish: sum x = sum x^2 = 0, because
n > 2. The first equation gives a = -b(n-1)/2. Substitution into the
second gives

    0 = b^2 n(n^2-1)/12.

Here p >= 7, and none of b, n, n-1, n+1 is zero modulo p. Indeed,
a proper subgroup has n <= (p-1)/2. This is a contradiction. QED.

The restrictions matter. A two-point set is an affine interval, and the
full group F_p^* is the interval {1,...,p-1}. The lemma only rules out
affine changes of variable; it makes no assertion about all generalized
Reed--Solomon equivalences or projective coordinate changes.

## 2. Moments of exponents are the wrong signatures

**Lemma (Prouhet obstruction).** Let m >= 1, let g have multiplicative
order n >= 2^(m+1), and let the field characteristic exceed n.
There are equally sized subsets A and B of {0,...,n-1} such that

    sum_{i in A} i^j = sum_{i in B} i^j  (over the integers, 0 <= j <= m),

but sum_{i in A} g^i != sum_{i in B} g^i in the field.

**Proof.** Expand

    Q(X) = product_{r=0}^m (1-X^(2^r)).

Every exponent from 0 through 2^(m+1)-1 has one binary expansion, so
every coefficient is +1 or -1. Take their supports as A and B.
The root at X=1 has multiplicity m+1. Applying (X d/dX)^j and
evaluating at 1 gives the integer moment equalities for j <= m.
On the other hand, Q(g) != 0: no order n >= 2^(m+1) divides any
2^r with r <= m. QED.

For m=2, A={0,3,5,6} and B={1,2,4,7}. Both have sum 14 and sum
of squares 70, but their field sums differ by (1-g)(1-g^2)(1-g^4).
Thus even an exact interval certificate for two index moments cannot
be reused as a certificate for the first coefficient on a subgroup.

**A related degree obstruction.** If n < p and g != 1, the unique
polynomial of degree less than n taking i to g^i on 0,...,n-1 has
degree exactly n-1. Its Newton expansion is

    sum_{j=0}^{n-1} (g-1)^j binom(X,j).

The highest coefficient is (g-1)^(n-1)/(n-1)! != 0. Consequently,
the natural ordering of a subgroup by powers does not provide a
low-degree polynomial substitution carrying an interval to it.
This is an obstruction for that ordering, not for every bijection.

## 3. What complete-fiber transfer actually preserves

**Lemma (general pullback).** Let phi in F[X] have degree d >= 1.
Let D' and D be nonempty finite evaluation sets such that phi maps D' onto D
and every fiber has exactly d points. Put |D|=N and assume 1 <= k <= N
and 0 <= t <= N. Any L distinct
polynomials of degree less than k agreeing with a received word w
on at least t points of D give L distinct polynomials in
RS(F,D',dk) agreeing with w composed with phi on at least dt points.
Thus relative rate k/N, relative agreement t/N, and gap (t-k)/N
are preserved. If the original agreement counts are exact, so are
the new counts.

**Proof.** Compose each polynomial with phi; the degree is at most
d(k-1) < dk. Each original equality is repeated on exactly d points,
and each inequality remains an inequality throughout its fiber.
Because k <= N, distinct original polynomials give distinct evaluation
words on D. Surjectivity preserves this distinction on D'. QED.

The polynomials actually fit dimension d(k-1)+1. Using this smaller
ambient code preserves the same list and agreements, lowers the rate
by (d-1)/(dN), and increases the gap by the same amount. This exact
rounding improvement follows from the degree bound; it does not
change the required quotient domain or produce additional witnesses.

For a subgroup H_n and d dividing n, phi(X)=X^d maps H_n onto
H_(n/d), with d points per fiber. The lemma therefore lifts a
certificate on a **smaller subgroup of the same field**. It does
not turn an interval certificate into a subgroup certificate.

There is also a necessary condition: the image of any multiplicative
coset cH_n under X^d is the multiplicative coset c^d H_(n/gcd(n,d)).
The manuscript's Lemma `fg:lift` constructs complete power fibers over
an interval by varying the prime. Its resulting domain need not be
a subgroup, and for a proper image subgroup of size at least three
the first lemma forbids the required affine identification. The
original fixed-gap theorem remains valid on its stated domain.

## 4. Bare field pigeonholing cannot replace concentration below Elias

Let D be any n-element subset of F_p, p > n, and let t=k+m<n with
k,m >= 1. Sorting t-subsets by their first m elementary symmetric
coefficients gives at most p^m classes. Hence the usual vanishing-
polynomial construction gives

    L >= ceil(binom(n,t)/p^m).

This is universally valid, but the numeric guarantee is at most 3
whenever theta=1-t/n lies strictly below the characteristic-p Elias
radius at rate rho=k/n.

**Proof of the limitation.** Write eta=m/n, so theta+rho+eta=1.
The strict entropy condition H_p(theta)<1-rho is equivalent to

    H_2(theta) < eta log_2 p + theta log_2(p/(p-1)).

Using binom(n,t) <= 2^(n H_2(theta)), we obtain

    binom(n,t)/p^m < (p/(p-1))^(n theta) < e,

since p-1 >= n and theta<1. Taking a ceiling gives at most 3.
This bounds the strength of this particular certificate, not the true
list size. More precise binomial estimates may improve the constant.

Thus a meaningful prescribed-subgroup result needs nonuniformity of
the actual coefficient signatures, rather than just their field-sized
range. Shrinking the number of canceled coefficients alone does not
evade this below-Elias obstruction to the elementary counting bound.

## 5. An exact formulation of the missing subgroup statistic

Let M=binom(n,t), let char(F_p)>m, and let N_v count t-subsets with
power-sum signature v=(sum x,...,sum x^m) in F_p^m. Newton identities
identify these fibers with the first-m-coefficient fibers. If chi is
a nontrivial additive character of F_p and

    E_xi = [Z^t] product_{x in D}
                  (1 + Z chi(sum_{j=1}^m xi_j x^j)),

then finite Fourier orthogonality gives the exact identity

    sum_v N_v^2 = p^(-m) sum_xi |E_xi|^2.

Consequently

    max_v N_v >= ceil( (p^(-m)/M) sum_xi |E_xi|^2 ).

The xi=0 term recovers M/p^m. Any stronger conclusion requires a
lower bound for the nonzero Fourier energy, or another verified
description of heavy coefficient fibers on the prescribed domain.
This identity is a diagnostic reformulation, not a claim that the
needed character-sum estimate or an efficient computation is known.

## Validation and relation to the manuscript

`verify_transfer_limits.py` checks the affine obstruction, the Prouhet
moment and field-sum statements, the Newton interpolation degree,
complete subgroup fibers, and exact list transfer on small fields.
The proofs above are independent of the finite checks.

The manuscript already contains the complete-fiber construction and
explicit multiplicative/circle constructions. This note adds precise
limitations on transporting its *interval concentration certificates*;
it does not replace those constructions or assert a new contest result.
