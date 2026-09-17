# Exact list preservation with composite fibers and padding

September 17, 2026. Extension of PRIME_FIBER_RIGIDITY.md.

The prime-degree hypothesis can be replaced by a coprimality condition
if one uses all the automatically vanishing moments of orders 1,...,B-1,
rather than only the first moment. This also permits added rational nodes
and code dimensions not divisible by B.

## Moment rigidity over a number field

Let positive integer nodes a_1,...,a_m have private rational primes r_i:
v_{r_i}(a_i)=1 and v_{r_i}(a_j)=0 for j!=i. Let B>=2 be any integer
coprime to every r_i. Put E=Q(zeta_B) and alpha_i^B=a_i.

The primes r_i are unramified in E, so valuations show that the classes
of a_i generate a subgroup (Z/BZ)^m in E*/E*B. Kummer theory gives
[E(alpha_1,...,alpha_m):E]=B^m. Consequently the monomials
product_i alpha_i^{e_i}, 0<=e_i<B, form an E-basis. In particular,
for each 1<=j<B, the elements 1,alpha_1^j,...,alpha_m^j are independent.

Add any finite set U of distinct positive rational integers, disjoint
from the fibers over characteristic zero. For a subset A of the union
of U and the roots of all X^B-a_i, suppose

    sum_{x in A} x^j = 0,  1<=j<B.

For j=1, independence of 1 and the alpha_i forces sum(A intersect U)=0.
Positivity therefore forces A intersect U empty. For every fiber i and
every j=1,...,B-1, independence forces

    sum_{r=0}^{B-1} c_{ir} zeta_B^{rj}=0,

where c_{ir} is its 0/1 incidence vector. Inverting the B-point Fourier
transform over E shows that all c_{ir} are equal. Thus A is a union of
whole fibers. The converse follows from the geometric series identity.

For fixed B and U, exclude primes dividing norms of nonzero moment sums
and nonzero differences between domain nodes, and exclude ramification
and primes <=n. Infinitely many remaining primes split completely in
the number field. At each such prime, the same moment-vector zero test
characterizes unions of whole fibers. No estimate on the least prime
is claimed. Positivity is used over characteristic zero before these
finite exclusions, not as an ordering on the finite field.

## Exact decoding lists

Let W be monic of degree t over the integers and choose

    1 <= K <= (t-1)B+1.

At agreement threshold tB, every degree-<K candidate Q for W(X^B)
has difference equal to the locator of a tB-subset: it is monic of
degree tB and has at least tB roots. Its first B-1 leading coefficients
vanish. Newton identities, in characteristic p>n>=tB, imply that its
first B-1 root moments vanish. Moment rigidity makes the root subset a
union of t complete fibers, containing no node of U. Hence

    Q(X)=P(X^B),  deg P < ceil(K/B),

where P agrees with W on t seed nodes. Conversely every such seed
candidate supplies a lifted candidate. This describes the ENTIRE list,
including over extension alphabets, since a monic polynomial with tB
base-field roots is its base-field locator.

Exclude finitely many additional primes dividing nonzero leading
coefficient differences between W and seed locators. Then the seed list
itself is the characteristic-zero list and is exactly constant as the
selected prime field varies.

## Exact lists at every prescribed small rational gap

Use m,t,k,a,rho from PRESCRIBED_GAP.md. Choose an integer D such that
D*t/a and D*rho*t/a are integers. In the CRT translation of the seed
choose private primes r_i not dividing D. Let B grow through multiples
of D coprime to all r_i (for example D times primes outside this finite
set). Translate W along with the seed. Let

    n=Bt/a,  K=rho*n,  |U|=n-mB.

These are integers with exact rate rho and exact gap eta. For small
eta, t-rho*t/a=eta*t/a tends to infinity, so K<=(t-1)B+1. The seed
dimension ceil(K/B)=ceil(rho*t/a) is fixed as B grows and contains
the original degree-<k candidates. Choose U={1,...,n-mB}; none is a
fiber root over characteristic zero, since each a_i has a private
valuation one and hence is not a Bth power of a rational integer.

The ENTIRE displayed list is therefore exactly a fixed finite list of
size L_star with

    log_2 L_star >= (H_2(rho)^2/2-o_rho(1)) /
                    (eta^2 log_2(1/eta)).

Prime sizes can ensure n=o(p) and strict Elias. This proves exact
pointwise list preservation at every sufficiently small rational gap.
It does not bound the global maximum list over arbitrary received
words, amplify the list with length, or prove a superlinear line count.
