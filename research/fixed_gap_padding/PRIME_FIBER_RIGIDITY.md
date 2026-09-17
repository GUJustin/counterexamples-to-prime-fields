# Exact lists under specially chosen prime-degree fiber lifts

September 17. Proof-reviewed research note, not a global list-size bound.

Let q_1,...,q_m be distinct rational primes, and let B be prime. There
are arbitrarily large primes p such that every X^B-q_i splits into B
distinct roots in F_p, and the union D of these fibers has the property:

    a subset A of D has sum zero iff A is a union of whole fibers.

More generally, two subsets with the same sum can differ only by
replacing whole fibers with empty fibers, with every partial fiber
unchanged. In particular no extra partial-fiber cancellation occurs.

## Number-field proof

Work first over E=Q(zeta_B) and let alpha_i^B=q_i. The classes q_i are
independent in E^*/E^{*B}: taking valuations above q_i isolates its
exponent, and the ramification index is either 1 or B-1, both coprime
to B. Kummer theory therefore gives degree B^m for
K=E(alpha_1,...,alpha_m), with the usual radical monomial basis.
In particular the alpha_i are linearly independent over E.

If sum_i alpha_i sum_j c_ij zeta_B^j=0, with c_ij in {0,1}, each inner
sum vanishes. The minimal polynomial 1+X+...+X^(B-1) shows that all
coefficients c_ij in a fixed fiber are equal. This is precisely the
whole-fiber assertion. Applying the same argument to coefficients in
{-1,0,1} proves the difference assertion. Distinct roots from different
fibers cannot coincide, since their B-th powers differ.

There are only finitely many subset differences. For each difference
that is nonzero in K, exclude the rational primes dividing its nonzero
algebraic integer norm. Also exclude primes ramified in K, primes at
most mB, and primes dividing the relevant q_i or q_i-q_j. Infinitely
many remaining primes split completely in K, by Chebotarev. Reduction
at any prime above such a p preserves every nonzero subset difference
and splits all the required fibers. This proves the finite-field claim.
No bound on the least acceptable p is asserted.

## Exact decoding-list consequence

Let W(Y) be monic of degree t, with 1<=k<t<=m. On the seed domain
{q_1,...,q_m}, consider degree-<k polynomials agreeing with W on at
least t points. On the lifted domain D, use degree-<kB polynomials and
the received word W(X^B), at agreement threshold tB.

Every lifted nearby polynomial is exactly P(X^B), where P is a seed
nearby polynomial. Thus the entire decoding list at this particular
received word is preserved, not just a selected sublist.

To prove this, W(X^B)-Q(X) is monic of degree tB. If it has at least
tB domain roots, it is the locator of a tB-subset A. Its coefficient
in degree tB-1 is zero: W(X^B) has only B-divisible exponents, and
deg Q<kB<=tB-B. Hence A has sum zero, so it is a union of exactly t
whole fibers. Its locator is product_{i in I}(X^B-q_i). Subtraction
shows that Q=P(X^B), with deg P<k, and that P is a seed nearby
polynomial. The converse follows by composition. The root-counting
argument also gives exact agreement tB whenever a candidate exists.

The same claim holds for W and Q over an extension alphabet: a monic
degree-tB polynomial with tB base-field roots is their base-field
locator, so Q automatically has base-field coefficients when W does.

## Scope and significance

For fixed seed data and growing prime B, this gives fixed rate and
fixed gap, with an exactly fixed decoding list at the displayed word.
Choosing p arbitrarily large ensures n=o(p) if desired. It strengthens
the control available in a fiber lift, but DOES NOT bound the global
maximum decoding list over all received words. Arbitrary received
words need not have a representative of degree tB, so the locator and
zero-sum argument cannot be applied to them.

Distinct-prime seed domains can have genuine list collisions, e.g.
{3,5,7,11,13}, k=1, t=2, W(Y)=Y^2-16Y. Its exact seed list consists
of the constants -39 and -55, from pairs {3,13} and {5,11}.
Exact fixtures for B=2 and B=3 check all 1,024 and 32,768 subset sums,
respectively. They verify the stronger subset-difference assertion via
partial-fiber signatures, and enumerate the full decoding list, which
has exactly the two claimed constants in each case.

## Large fixed seed lists are compatible with the hypothesis

The distinct-prime seed restriction does not destroy the moment lower
bound's leading exponent. Let the seed nodes be the first m rational
primes, all at most Q=O(m log m). Fix rational rho, k=rho*m, and
s=floor(c sqrt(m/log_2 m)), t=k+s. The j-th binomial moment of a
t-subset lies in an integer interval containing at most

    t binom(Q,j)+1

values. Therefore the logarithm of the number of moment vectors is at
most

    (s^2/2) log_2(Q/s) + O(s^2+s log m)
      = (c^2/4+o(1)) m.

The subset count has logarithm H_2(rho)m+o(m). For c^2<4H_2(rho),
one moment class hence has size at least
2^((H_2(rho)-c^2/4-o(1))m). The binomial moments determine the same
leading locator coefficients, exactly as for interval nodes. Choosing
one class defines a monic received polynomial W of degree t and an
exact finite seed list of some size L with this lower bound.

Now fix that seed. Exclude finitely many reducing primes so that no new
seed t-subset has the prescribed leading locator coefficients modulo p
unless it already has them over the integers. This is possible because
there are finitely many such coefficient differences. The fiber theorem
then gives, for every growing prime fiber degree B, a prime-field code
of length mB, dimension kB, agreement threshold tB, and EXACTLY L nearby
codewords at the displayed received word. Rate k/m and gap s/m are
fixed throughout this length-growing family. The chosen p may be taken
arbitrarily large, so n=o(p) and strict characteristic Elias can both
be imposed.

This retains the previous moment construction's asymptotic lower-bound
exponent. Its additional conclusion is exact preservation of the entire
list at the selected word. It is not a new lower bound on the global
worst-case list size, and does not settle actual-list-size line bounds.

## Entire low-degree received-line profiles are preserved

The correspondence holds simultaneously for every member of any seed
line W_z(Y)=U(Y)+z V(Y), with deg U,deg V<=t. On the lifted line
W_z(X^B), at threshold tB and message dimension kB, all nearby
polynomials are exactly the compositions of seed nearby polynomials at
threshold t. The statement is valid for parameters in any extension
alphabet. When W_z has degree t, divide its difference from the candidate
by its leading coefficient and use the same zero-root-sum proof. When
deg W_z<t, tB roots force the difference to be identically zero, which
is possible exactly when W_z itself has degree<k. This is also precisely
the seed conclusion. Thus no leading-coefficient exceptional parameter
is omitted.

For selected witness pairs the maximum concurrency on a parametrized
affine codeword line is preserved too. Any such line containing two
lifted candidates has composed intercept and direction, by interpolating
those two candidates at their two distinct labels. It therefore comes
from a seed codeword line, and conversely composition preserves every
seed concurrency. Single-pair concurrency causes no exception.

Ordinary correlated agreement at these thresholds is preserved as well.
If there are explaining F,G of degree<kB on at least tB common
coordinates, choose two parameters whose received members have degree
t, when the seed line has a nonzero degree-t coefficient. Each combined
candidate is composed by the preceding argument, so F and G are composed.
The common agreement set is then a union of fibers and has at least t
seed coordinates. If both received coefficients have degree<t, any one
of their differences from a candidate has degree<tB, so tB common roots
force polynomial equality; a correlated explanation exists exactly when
both coefficients are codewords, again matching the seed statement.

Consequently this controlled composition lift cannot increase the
number of nearby parameter labels or produce a superlinear line count.
It preserves normalized distance but increases length. Padding leaves
this low-degree received-line setting; its direction vanishes on too
many core points to have degree<=tB. The pointwise list control must not
be carried over to that different line without a new proof.
