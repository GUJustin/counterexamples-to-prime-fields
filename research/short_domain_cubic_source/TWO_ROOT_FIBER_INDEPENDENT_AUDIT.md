# Independent audit: arbitrary two-root constant fibers

**PASS.** Independently checked ROOT_TWO_ROOT_FIBER_DERIVATION.md and the
expanded arbitrary-(r,s) portion of HIGH_MULTIPLICITY_REPEATED_FIBER.md.
No corrections are needed. This audit is separate from the earlier
(b-1,1) audit and covers the added decomposition and gcd arguments.

For coprime r,s and b=r+s, h(Y)=Y^r(Y+1)^s has exactly the stated tame
branch cycles: (r)(s), (b), and one transposition. The nonzero critical
value is (-1)^r*r^r*s^s/b^b. Characteristic zero or p>b ensures this
value is nonzero and every listed inertia order is prime to p.

The polynomial decomposition proof is sound. Distinct roots of an outer
polynomial have disjoint nonempty inner fibers. With only two available
roots, an outer polynomial with at least two roots forces both inner
fibers to be singleton fibers. Their polynomials have the same leading
coefficient, and subtracting produces a nonzero term of degree m-1;
p>b>=m rules out its disappearance. A one-root outer polynomial would
force its degree to divide both r and s. Both cases contradict a
nontrivial decomposition.

The conversion from rational intermediate fields to polynomial
intermediate maps is valid: the unique point over the original infinity
implies a unique intermediate point over infinity. After choosing this
point as the pole of a rational coordinate on the intermediate curve,
both maps have only their infinity pole and are therefore polynomial.
Luroth supplies that coordinate. Thus indecomposability implies primitive
monodromy. Conjugate transposition edges form an invariant block
partition; primitivity makes the graph connected, giving S_b.

The joint monodromy is S_b^3 by the distinct finite-branch inertia
argument. At zero, the number of simultaneous inertia orbits is

    r^2+s^2+3r+3s.

Specifically, a mixed (r,r,s) tuple space has r^2*s points and orbit
length r*s, hence r orbits for each of three placements; the opposite
mixed type contributes s for each placement. The unmixed contributions
are r^2 and s^2. Primitive powers of the individual inertia cycles do
not change these lengths. Infinity contributes b^2 orbits, and each
separate simple branch has index b^2. Hence

    g=1+(b^2+2rs-3b)/2 >= 1.

This includes r=s=1, with genus one and no ramification at zero.
Inseparable q again causes no exception to the Luroth obstruction.

For d=gcd(r,s), fixing one nonzero-label section gives a nonconstant
q0=h0(Y*) and q=q0^d/lambda*. Every other section has h0(Y)/q0
constant; over algebraically closed constants it is a scalar mu.
The coprime lemma bounds these mu values by two. Each admits at most
b/d rational-function roots. The zero label adds only two sections.
Therefore 2b/d+2 bounds the whole bank, not merely the number of labels.
Collisions under mu -> lambda*mu^d cannot enlarge this section count.

The affine alternatives and list bound max(2b/d+2,floor(1/eta)) follow
under the explicit degree bounds on R,S. The theorem remains conditional
on a fiber supported on at most two polynomial linear roots; neither
arbitrary repeated fibers nor irreducible higher-degree root factors
are silently included.
