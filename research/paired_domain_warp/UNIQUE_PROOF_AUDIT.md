# Internal audit: exact local lists and deterministic unique witnesses

September 17, 2026. This is an internal proof audit with independent arithmetic
and exhaustive small instances, not external peer review or formal verification.

## Exact classification by signed relations

With direction supported on the two padding coordinates, any codeword at
agreement threshold K+3 must match both padding coordinates and K+1 nonpadding
coordinates. The far word's root bound is K+1, so this conclusion includes
all codewords, not only the displayed family. F-Q is monic of degree K+1,
its degree-K coefficient is zero, and it is the locator of those K+1 distinct
roots. Their sum is zero. The parity of the two padding values gives
H(1)/H(-1)=(-1)^(K+1). After canceling full sign-orbits, the remaining roots
therefore give a ternary relation in Fp(additive) x Fp*:
 sum eps_i a_i=0, product ((1-a_i)/(1+a_i))^eps_i=1.
The denominators and padding values are nonzero on a nearby nonzero parameter.

When the only relation is empty, every locator is paired. In the odd-degree
case zero is forced as a root; in the even-degree case it is excluded. This
handles all three exact-rate parity cases. The resulting lists are exactly
the fibers of the displayed subset-product map. Injectivity of that map is
needed only for uniqueness, not for the exact fiber classification.

verify_unique_geometry.py exhausts every potentially nearby codeword via
interpolation at all parameters, for generic and powers-of-two domains in all
three parity cases. All six fixtures pass. The optional zero coordinate is
explicitly included in the nonpadding roots; it is not a free extra agreement.

## Random short-domain theorem

Take m=(1/4)log2(p)+O_rho(1), giving n=(1/2)log2(p)+O_rho(1).
Invalid domains cost at most (m^2+2m)/p. Distinct support products differ by
a nonzero polynomial of degree <=2m, so any collision costs at most
2m*binom(m,D)^2/p <=2m4^m/p by union bound. For a fixed ternary support u>=3,
eliminate one variable using the sum equation. The second equation remains
a nonzero polynomial of degree <=u: its specialization to X,Y,-X-Y and
zeros is ±2XY(X+Y). Thus the joint event costs at most u/p^2. Supports u=1,2
are impossible on a valid domain. All nontrivial relations cost at most
m3^m/p^2. Rejection conditioning for a valid domain changes only a 1+o(1)
factor. Total failure is at most p^(-1/2+o(1)).

Entropy gives log2 J=nHrho/2+O(log n). The proposed exponent is
c2*nHrho/3, so every fixed c2<3/2 is defeated exponentially. Eta log2(p)
tends to6, so strict Elias holds with a constant margin in this comparison.
The gap shrinks; this does not settle the fixed-positive-gap frontier.

## Deterministic powers-of-two theorem

Set a_i=2^i. The largest D-subset positive product is bounded by
2^[D(2m-D+1)]. The field hypothesis puts every product below p and also
puts the entire sum of core magnitudes below p. Largest-power domination
then excludes every nonzero ternary sum, even before the ratio equation.

For T=product(4^i-1), write T=4^s U. The strict inequality 2/3<U<=1
identifies s from T's bit length (except the separately handled empty set).
At the first undecided index i, membership is equivalent to U<=1-4^-i:
the product of all later factors exceeds 1-(1/3)4^-i. This proves both
injectivity and an integer/rational greedy decoder. No integer-factorization
or primitive-divisor theorem is used. For arbitrary inputs, exact division,
final product, and support-size checks prevent false positives.

The field sign is z=(-1)^(D+1)T mod p. Lifting this signed label gives the
original integer T without wraparound. The exact local-list criterion
therefore upgrades the product decoder to a decision procedure for proximity
along the whole line and recovery of its unique witness. This is not merely
a procedure for recognizing a subset of nearby parameters.

Exact-rate choices n=Theta_rho(sqrt(log p)) satisfy the field bound. The
entropy comparison remains nHrho/2 versus c2*nHrho/3, and eta log2(p) tends
to infinity. Construction and decoding use polynomially many bit operations
in log p. No global maximum list-size bound is asserted.

check.py tests 32,738 supports exhaustively and rejects small nonbank inputs.
verify.py independently uses rational comparisons, replays 256 larger support
recoveries, verifies four finite parameter rows, and saves a deterministic
M1279/n82 instance with explicit polynomial witnesses. Its full classification
is mathematical and deterministic, unlike the earlier random completion sample.

## Two distance levels: scope and valuation argument

The additional statement is restricted to n=2m+2,K=2D-1, with no extra zero
coordinate. At K+2 agreements, zero padding matches is impossible. One padding
match forces a paired locator by integer root-sum dissociation, hence the
second padding match. With two padding matches and K known core roots, the
last locator root is minus their sum. Removing paired roots leaves an odd
number u of signed powers. If u=1 it completes a pair. For u>=3 the padding
equation is F=(1+S)prod(1-y)-(1-S)prod(1+y)=0 mod p.

In F/2=(S e2-e3)+(S e4-e5)+..., the unique lowest 2-adic term is u0^2 v0,
where u0=±2^a and v0=±2^b are the two smallest magnitudes. Its valuation
is2a+b; all other terms have strictly larger valuation. Thus F is a nonzero
integer. Its absolute value is less than2^[m(m+1)/2+2m+2], so the additional
field bound excludes modular cancellation. Every nonbank point therefore
has exactly the original far distance; zero supplies that distance everywhere.

check_two_adic.py verifies the precise valuation on all59,028 signed supports
of size>=2 among the first ten powers. check_two_levels.py exhausts all
interpolation pencils for five fixtures, determining every parameter even
in a61-bit field. A deliberate negative control (odd K with an extra zero)
has an intermediate distance level, confirming why the proposition's scope
must not be silently broadened.

## Concrete M31 local lists

The n62/K31 random-coordinate instance has no nonzero signed relation, proved
by two independent meet-in-the-middle enumerations of3^15 keys on each side.
Two independent bounded-memory fiber counts then agree on the exact histogram:
list sizes0..5 have respectively
2006567569,136494714,4337028,83442,891,3 parameters.
The total is p; the positive count is140916078; the weighted sum is145422675.
The136494714 uniquely nearby parameters alone beat the numerical prescription.
These are exact list sizes on this line, not a global list-size bound.
