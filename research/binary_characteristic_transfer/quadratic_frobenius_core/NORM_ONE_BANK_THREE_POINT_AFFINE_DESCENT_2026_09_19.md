# Three-point affine-plane bound for the norm-one quadratic bank

September 19, 2026. Independent proof of the root agent's proposed
coefficient-descent obstruction. This strengthens the initial six-point
bound to a sharp three-point bound. It is a necessary-condition result,
not a new proximity-gap construction. No manuscript changes or novelty
claim are made.

The bank is the one in
[the prime-power norm-one note](NORM_ONE_PRIME_POWER_SUBPLANE_AND_FIELD_GATE.md):
for a prime power Q, let E=F_(Q^3) and

    B = {(a, -a^(Q^2+1)) : a in E, Norm_(E/F_Q)(a)=-1}.

The coefficient geometry proved here works in every characteristic,
including two and three. The associated two-square-root evaluation-domain
construction in the source note separately assumes odd characteristic.

## 1. Exact affine-plane intersection theorem

**Theorem.** Every affine F_Q-subspace of E^2 of dimension at most two
contains at most three points of B. The bound three is attained.

Use the following parameterization, with d in E* taken modulo F_Q*:

    p(d) = (-d^(Q^2)/d, -d^Q/d),
    z(d) = (p(d),1) = (-d^(Q^2),-d^Q,d)/d.              (1)

The first coordinate a has norm -1, and

    a^(Q^2+1) = d^(Q-1),

so (1) lies in B. The kernel of d -> d^(Q^2-1) in E* is F_Q*, because
gcd(Q^2-1,Q^3-1)=Q-1. Thus (1) gives all Q^2+Q+1 bank points exactly
once as d ranges over the F_Q-projective points of E.

We use the elementary Moore determinant criterion: for three elements
d_1,d_2,d_3 of E, their vectors

    M(d_i)=(-d_i^(Q^2),-d_i^Q,d_i)

are E-linearly independent exactly when the d_i are F_Q-linearly
independent. One direction follows from F_Q-linearity of M. For the
other, a dependence among the rows of the Moore matrix would give a
nonzero polynomial c_0 X+c_1 X^Q+c_2 X^(Q^2) vanishing on an F_Q-basis
of E. Its F_Q-linearity would make it vanish on all Q^3 elements of E,
contradicting its degree at most Q^2.

Let Pi be an affine F_Q-plane and put S=Pi intersect B.

### Case A: S contains three points that are not E-collinear

Write them as p(d_1),p(d_2),p(d_3). By the criterion, d_1,d_2,d_3
form an F_Q-basis of E. Their affine F_Q-span is exactly Pi.

For another p(d) in S, write

    d = c_1 d_1+c_2 d_2+c_3 d_3,       c_i in F_Q.

F_Q-linearity of M gives the unique E-barycentric coordinates

    z(d) = sum_i (c_i d_i/d) z(d_i).                    (2)

Because p(d) belongs to Pi, those coordinates also belong to F_Q.
If c_i and c_j were both nonzero, the ratio of the corresponding
nonzero coordinates in (2) would force d_i/d_j to belong to F_Q,
contrary to independence of the d_i. Hence precisely one c_i is
nonzero, and p(d) is one of the original three points.

### Case B: all points of S are E-collinear

There is nothing to prove if |S|<=1. Otherwise choose distinct p(d_0),
p(d_1) in S. Their parameters d_0,d_1 are F_Q-independent. The Moore
criterion implies that every parameter of a point in S lies in

    U = span_(F_Q){d_0,d_1}.

Consequently all their first coordinates belong to the parameterized
projective line

    A(T,U) = -(d_0^(Q^2) T+d_1^(Q^2) U)/(d_0 T+d_1 U),
                                      [T:U] in P^1(F_Q).             (3)

The denominator never vanishes at an F_Q-projective point. As a
rational function over E, (3) is nonconstant: cancellation would imply
(d_1/d_0)^(Q^2)=d_1/d_0 and hence d_1/d_0 in F_Q. Its unique pole
v=-d_1/d_0 has exact degree three over F_Q, so v,v^Q,v^(Q^2) are
distinct finite points.

The first-coordinate projection of Pi is an affine F_Q-subspace of E
of dimension at most two. Thus there are kappa in E*, c in F_Q with

    Tr_(E/F_Q)(kappa a)=c

for every first coordinate of Pi. This uses the nondegenerate finite-
field trace pairing; it remains valid in characteristic three even
though Tr(1)=0.

Consider the formal rational function

    R(T/U) = sum_(i=0..2) kappa^(Q^i) A^[Q^i](T/U)-c,                (4)

where A^[Q^i] means twisting the coefficients, not the variable. On
F_Q-projective parameters, (4) is exactly the required trace equation.
Its three summands have simple poles respectively at v,v^Q,v^(Q^2).
Each residue is nonzero and no other summand has that pole. Hence R
is not the zero rational function, in every characteristic.

Multiplying (4) by the homogeneous cubic

    N(T,U) = prod_(i=0..2)(d_0^(Q^i) T+d_1^(Q^i) U)

gives a nonzero homogeneous cubic in F_Q[T,U]. It has at most three
distinct projective roots. Since N is nonzero at every point of
P^1(F_Q), at most three parameters in (3) satisfy the trace equation.
This proves |S|<=3 also in Case B.

Finally, choose an F_Q-basis d_1,d_2,d_3 of E. The three corresponding
bank points are E-affinely independent, and their affine F_Q-plane
contains exactly those three by Case A. Thus the constant is sharp.

## 2. Descent under an arbitrary common injective E-linear map

The next step needs linear disjointness. A direct argument using
barycentric coordinate minors in the target field is insufficient:
vectors with coefficients in K can be E-independent but K-dependent.

**Field lemma.** Let Omega contain E and a finite field K, and put
k=E intersect K. Then E and K are linearly disjoint over k. In particular, for any
E-linear subspace W of Omega^N of dimension d,

    dim_k(W intersect K^N) <= d.                       (5)

For completeness, if E=F_(ell^s) and K=F_(ell^m), their intersection
has degree gcd(s,m) over F_ell and their compositum has degree
lcm(s,m). These degree formulas give linear disjointness over k.
To obtain (5), expand any E-linear relation among vectors in K^N in
a k-basis of E. Linear disjointness allows comparison of those basis
coefficients in every coordinate. Therefore vectors that are
k-independent remain E-independent.

**Descent corollary.** Suppose K is finite and k=E intersect K is contained in F_Q.
Let T:E^2 -> Omega^N be injective and E-linear, and let H in Omega^N
be arbitrary. Then

    |{b in B : H+T(b) in K^N}| <= 3.                  (6)

If the set is nonempty, choose b_0 in it. Differences of selected
outputs lie in

    T(E^2) intersect K^N,

which has k-dimension at most two by (5). Their preimages under T lie
in a k-subspace of E^2 of dimension at most two. Enlarging its scalar
span to F_Q puts all selected b in an affine F_Q-plane. Section 1
then proves (6).

No bound on output degree or target extension degree is used. The
condition is the actual field intersection E intersect K subset F_Q.
For E=F_(ell^(3r)), K=F_(ell^m), Q=ell^r, this is equivalent to

    v_3(m) <= v_3(r).

In particular, for Q=ell and 3 not dividing m, at most three transformed
bank witnesses can have all their coefficients in F_(ell^m).

## 3. Common rational pullbacks and multipliers

Let Omega contain E and a finite field K, take a nonconstant phi(X) in Omega(X), a
nonzero common multiplier M(X) in Omega(X), and a common translation
H(X) in Omega(X). Transform each native quadratic by

    P_a(X)=a X^2-a^(Q^2+1)
       -> H(X)+M(X)[a phi(X)^2-a^(Q^2+1)].              (7)

The coefficient map (a,b) -> M(X)[a phi(X)^2+b] is injective and
E-linear because phi is nonconstant. Also

    E intersect K(X) = E intersect K = k.

The same k-basis of E stays independent over K(X): clear any proposed
rational-function denominators and compare coefficients of X, then
use its independence over K. Thus the linear-disjointness argument of
Section 2 applies with ambient field Omega(X), target field K(X),
and N=1. If k subset F_Q, at most three expressions in (7) belong to
K(X), and therefore at most three can be target-field polynomials of
any degree. Clearing denominators with a common factor, when desired,
is already included in M.

This is a coefficient-bank obstruction. It does not require the
transformed evaluation coordinates to descend, and it does not
assert that a proposed rational pullback preserves agreement or
Reed--Solomon distance. It rules out transferring a growing part of
this particular bank by a common injective E-linear transformation,
including nonlinear rational changes of the evaluation variable with
a common multiplier. It does not cover parameter-dependent maps,
nonlinear operations on the coefficient pair, traces, or changes of
characteristic.

## 4. Audit of the initial six-point route

The initial cubic/quadratic Bezout proof also works. When the
a-projection of Pi has F_Q-rank two, its norm equation has an
anisotropic binary cubic leading form and is irreducible over F_Q.
One nonzero F_Q-linear component of b+a^(Q^2+1) is a genuine quadratic.
The cubic need not be geometrically irreducible, but it cannot share a
geometric component with the F_Q-defined quadratic: their normalized
gcd over the algebraic closure would be Frobenius-fixed, hence defined
over F_Q, contradicting irreducibility and the degree inequality.
Bezout therefore gives six. The Moore/trace argument above provides
the stronger sharp bound three and avoids that geometric distinction.

## 5. Exact small-field checks

The root agent's standard-library
[verification script](verify_norm_bank_affine_planes.py) and
[saved receipt](verify_norm_bank_affine_planes.json) check every affine
span of a bank triple for Q=3,5,7. The bank sizes are respectively
13,31,57, and the numbers of triple spans checked are 286,4495,29260.
Each maximum intersection is exactly three. All tested triples have
F_Q-affine dimension two; this does not assert E-noncollinearity.
The script also checks irreducibility of each cubic field modulus and
the multiplicative-order identity for every nonzero represented element.
These are finite-field consistency checks; the proof above supplies the
uniform result for all prime powers and the descent conclusion.
