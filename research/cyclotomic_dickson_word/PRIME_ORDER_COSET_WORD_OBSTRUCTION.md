# Prime-order coset words cannot have a fixed linear surplus in characteristic zero

September 17, 2026. Proof proposed by the root research agent and
independently audited. No computation is needed.

## Stronger theorem: arbitrary polynomial degree

Let r be prime, let s>=1 be coprime to r, and let w on mu_(sr) be
constant on each mu_r coset. If P has degree at most D and is NOT
invariant under multiplication by mu_r, then its A agreements occupying
q cosets satisfy

    A <= D+q-1 <= D+s-1.

This holds for arbitrary characteristic-zero coefficient and word fields.
To prove it, choose one nonzero coefficient whose exponent is not
multiple of r and preserve its nonvanishing in the cyclotomic linear-
system reduction below. Subtract the entire invariant part Q(X^r) from
P and the corresponding constant on each coset from its word value.
Normalize the remaining coefficients at a prime above r. All retained
exponents are nonzero modulo r, and at least one coefficient is a unit.
Thus the reduced derivative is nonzero even if D>=r. The monic-locator
and distinct-coset argument below then gives A-q<=D-1 exactly as before.

Consequently, for RS dimension K=D+1, every noninvariant candidate has
surplus A-K<=s-2, independent of D. Any candidate exceeding this bound
must be invariant, and has a multiplicative orbit of size one. Thus
changing the rate by permitting K>r does not restore a growing-orbit
fixed-margin source with fixed s. Invariant polynomials descend to the
s-point coset domain; when agreement exceeds D+1 they are determined by
a bounded number of coset values, giving only boundedly many candidates
for fixed s, rather than merely bounded orbit size.

## Special case: degree less than the prime order

Let r be prime and s>=1 an integer coprime to r. On the domain mu_(sr)
in characteristic zero, let w be any word constant on each coset of
mu_r. If a nonconstant polynomial P of degree <r agrees with w on A
points, and those points occupy q cosets, then

    A <= r+q-2 <= r+s-2.

The word values and polynomial coefficients may be arbitrary complex
numbers; they need not initially belong to a number field. The same
statement holds over every characteristic-zero field containing the
domain and the specified data, by the linear-system reduction below.

For fixed s, a nonconstant candidate therefore has surplus at most s-2
above the dimension r. This rules out a fixed positive normalized margin
for the proposed prime-order cyclic orbit source, for EVERY coset word,
not merely the Dickson word. Constants can have more matches if several
cosets have the same value, but there are at most s relevant constants;
they cannot generate growing nearest orbits.

## Proof

Write K=Q(zeta_(sr)). Let S_j be the set of selected agreement nodes in
occupied coset j, of size A_j>=1. Introduce unknown coefficients c_0,...,
c_(r-1) and one unknown value v_j per occupied coset. The equations

    sum_(i=0)^(r-1) c_i*x^i = v_j,  x in S_j,

are linear over K. They have the given complex solution with at least
one nonzero coefficient c_h, h>=1. Scale this solution to set c_h=1.
The resulting inhomogeneous linear system is consistent over C, hence
also over K by Gaussian elimination. It supplies a nonconstant
polynomial and coset values in K realizing all selected agreements.
No claim that it preserves other agreements or the original word values
is needed for the upper bound.

Subtract the polynomial's constant term from it and all v_j, so c_0=0.
Choose a prime ideal over r in K and its discrete valuation ring O.
Multiply the polynomial and values by a scalar of valuation minus the
minimum valuation of its nonzero nonconstant coefficients. All polynomial
coefficients are then in O, and at least one nonconstant coefficient is
a unit. Its reduction Pbar is therefore nonconstant of degree <r.
For every occupied coset choose x in S_j. Roots of unity are units of O,
so v_j=P(x) lies in O as well.

Since P-v_j vanishes on S_j, it is divisible over K[X] by the monic
locator L_j=product_(x in S_j)(X-x). Both P-v_j and L_j are integral;
monic polynomial division shows that the quotient belongs to O[X].

In the residue field of characteristic r, all r-th roots of unity
reduce to 1. Because r does not divide s, the s-th roots of unity remain
distinct after reduction. Each coset therefore collapses to one residue
alpha_j, with distinct alpha_j for distinct occupied cosets. Reducing
the divisibility gives

    (X-alpha_j)^(A_j) divides Pbar-vbar_j.

Differentiation gives

    (X-alpha_j)^(A_j-1) divides Pbar'.

The derivative is nonzero: Pbar is nonconstant and has degree strictly
less than the residue characteristic r. The alpha_j are distinct, so
all these factors divide it simultaneously. Consequently

    A-q=sum_j(A_j-1) <= deg(Pbar') <= r-2.

This proves the result. The linear-system argument works from any
characteristic-zero extension field just as from C, because consistency
and a prescribed nonzero coefficient are detected by ranks over K.

## Audit details and boundaries

* Normalizing all coefficients without first subtracting c_0 would be
  insufficient: only the constant coefficient might remain a unit.
  Subtracting it ensures nonconstant reduction.
* The original word need not specialize; the auxiliary K-valued solution
  preserves precisely the selected incidence equations required.
* Integrality of the quotient follows from division by a MONIC locator.
* Distinct residue cosets require r coprime to s. This hypothesis is
  essential to the displayed proof and is not omitted.
* For the special-case proof, degree <r makes the reduced derivative
  nonzero. In the general theorem one must first strip ALL invariant
  exponents divisible by r; subtracting only the constant would fail.
* The theorem is in characteristic zero. It does not automatically bound
  all finite-field specializations uniformly in r or in the original
  characteristic-dependent word. For each fixed support pattern, a
  nonexistence statement can be preserved outside finitely many primes,
  but this does not remove the exceptional-prime research route.

For s=4 and odd prime r, every nonconstant candidate has at most r+2
agreements. The geometric-kernel construction at r=3 mod4 reaches r+1,
so it sits within one point of this general upper bound. The hoped-for
fixed-linear-margin upgrade within arbitrary four-value coset words is
therefore impossible in characteristic zero.
