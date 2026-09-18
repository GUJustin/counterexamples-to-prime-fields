# Orbit 2 realization rigidity (characteristic zero)

**Result.** Every admissible realization of the ordered orbit-2 incidence pattern is, after a projective change of the evaluation coordinate, addition of a common cubic, and a common nonzero value scaling, one of the three Galois conjugates of the bank in `ORBIT2_POSITIVE_BANK.md`. Its normalized tangent space is zero. This does not assert that the three conjugates are inequivalent, or mutually equivalent.

The archive contained the complete elimination ingredients, but its positive-construction statement did not state this classification. The following short resultant argument removes the need to interpret a large unsaturated Groebner computation.

## Complete chart

Use the ordered complement blocks C=137,145,167,236,247,256,345 and triple blocks T=123,124,156,257,346,357,467. Normalize the first three quadruple nodes to infinity,0,1, and write the others u,v,z,d. All seven nodes are distinct. Subtract a common cubic to make the infinity word zero, interpolate the six remaining quadruple words by a degree-at-most-five polynomial, and subtract its degree-at-most-two part. The resulting interpolant is

    W=a X^3+b X^4+c X^5.

For each candidate, take the remainder of W modulo the locator of its finite quadruple nodes. Candidates matching infinity have a degree-three locator and hence a quadratic remainder; the others have a degree-four locator and a cubic remainder. Thus this construction parametrizes every realization in the chart. The amplitude vector (a,b,c) is nonzero, since otherwise candidates coincide.

The seven necessary linear amplitude equations are saved in `nonfano2_projective.json`; their integer row contents are all one. The T156 row has a-coefficient -1. Eliminating a leaves a six-by-two matrix, whose fifteen minors are in `nonfano2_minors.json`. Its rows-(4,6) minor factors as

    -(d-1)(d-uv+uz-z)(-dvz+dv+uvz-uv+uz-vz).

Consequently exactly two branches need consideration; no division by a potentially zero amplitude was used.

## Branch I is impossible

Here d=uv-uz+z. A necessary equation gives

    u=vz/D,  D=v+z^2-vz.

D cannot vanish because v,z are nonzero. The rows-(0,4) remaining minor is

    v z (v-z)^2 (v+z^2-2vz)/D.

Every factor is nonzero: in particular (v+z^2-2vz)/D=1-u. This contradicts the minor equation. The exact substituted numerator and denominator are recorded in `nonfano2_branchI_reduce.json`.

## Branch II forces the known cubic

Here

    d=[uv(z-1)+z(u-v)]/[v(z-1)].

The denominator is nonzero by the node guards. A remaining equation forces

    u=vz^2(v-z)/D,
    D=v^2z-v^2-vz^3+2vz^2-vz+v-z^2.

Again D cannot vanish, because v,z,v-z are nonzero. Two necessary equations after this substitution are

    E=v^2z-2v^2+vz+v-z^2,
    F=v^3z^3-v^3z^2+v^3z-v^3-2v^2z^3
      +2v^2z^2+v^2z-2vz^3+z^5.

These are the rows-(0,1) and rows-(1,3) entries of `nonfano2_branchII_reduce.json` after removing only nonzero node/denominator factors. Direct exact resultant calculation gives

    Res_v(E,F)=z^6(z-1)^4 f(z),
    f(z)=z^3-10z^2+3z+1.

Thus f(z)=0. Exact elimination of E,F,f gives 25v=-4z^2+27z+7; substitution recovers

    u=(-z^2+13z+3)/20,
    v=(-4z^2+27z+7)/25,
    d=(-3z^2+29z+4)/20.

The cubic is irreducible over Q (neither possible rational root ±1 works) and separable. The amplitude matrix has rank at least two: at z=4 modulo83, its rows0,1/columns0,1 minor equals1. The already verified characteristic-zero bank supplies a nonzero kernel vector, so the rank is exactly two over Q[z]/(f), and hence at every conjugate. Its known kernel has a nonzero first coordinate, permitting a=1. This uniquely determines b,c as in the positive-bank note. Triple nodes are then unique: in this pattern each triple contains a pair appearing in only that triple block. That pair already shares two quadruple nodes, leaving at most one other root of its nonzero cubic difference. The saved bank verifies existence and all distinctness guards at all conjugates.

## Tangent certificate

With a=1, the normalized variables are (u,v,z,d,b,c). Differentiate the seven amplitude equations. At the good prime83, z=4, the point is (31,12,4,70,69,25). The first six rows of this seven-by-six Jacobian have determinant14 modulo83. Thus the characteristic-zero Jacobian has full column rank six, at every Galois conjugate, and the normalized realization tangent space is zero.

`orbit2_rigidity_audit.py/json` independently recompute the short resultants, exact cubic elimination, node formulas, amplitude minor and Jacobian. The bounded initial run completed in1.11 seconds using73 MiB; the final augmented exact run completed in under one second.

## Consequence and scope

There is no unused local deformation or separate admissible component of orbit2 that could change the fixed-bank norm curve into genus zero. The quadratic-cover exclusion for the known bank applies to its conjugates by Galois invariance. This closes that particular proposed construction direction; it is not an exclusion of larger-degree banks or unrelated eight-word constructions. Characteristic-zero classification is the claim here; small-characteristic exceptional fibers are not classified by this note.
