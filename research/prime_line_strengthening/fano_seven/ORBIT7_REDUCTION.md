# Orbit7: complete amplitude reduction (work in progress)

This note records an exact reduction and one fixed-node exclusion. It is not yet a global obstruction.

The ordered design is

    T=123,145,167,246,257,347,356,
    C=124,136,157,237,256,345,467.

Normalize the seven quadruple coordinates to infinity,0,1,u,v,w,z in the displayed C order, using degree-three binary-form coordinate transformation. Subtract P1, so P1=0. The prescribed two quadruple roots of each remaining Pi give

    Q2=(X-w)(X-z), Q3=(X-v)(X-z), Q4=(X-u)(X-v),
    Q5=(X-u)(X-z), Q6=(X-u)(X-w), Q7=(X-v)(X-w).

Write Pi=Qi Li. Every possible family satisfying the quadruple incidences is obtained from three amplitudes j,k,l as follows:

    L_i=(k/Qi(1)-j/Qi(0))*X+j/Qi(0),          i=2,4;
    L_i=l*(X-1)+k/Qi(1),                      i=3,6;
    L_i=l*X+j/Qi(0),                          i=5,7.

Here j is the common value at0 for candidates2457, k the common value at1 for2346, and l the common leading coefficient at infinity for3567. All three are nonzero because candidate1 is outside those quadruples. Completeness follows directly from the two values, or value and leading coefficient, determining each linear Li. All denominators are node-distinctness guards.

For each pair i,j, divide Pi-Pj by the binary quadratic locator of its two prescribed quadruple nodes. This leaves a binary linear form. The three lines associated with a T-triple must have their remaining root in common, so the determinant of two coefficient vectors vanishes. At fixed quadruple nodes these are seven quadratic equations in(j,k,l).

The bounded test `orbit7_fixed.py` instead uses the equivalent all-finite remainder parametrization at quadruple nodes0,...,6. Its seven quadrics span all six quadratic monomials in three amplitudes: the7-by6 coefficient matrix has rank6 over Q. Thus that particular node configuration admits no nonzero amplitude solution. This does not justify a generic-to-global inference.

The separate factor check `orbit7_factor_audit.py` identifies exactly one linear factor of each quadratic as a forbidden extra quadruple-node equality. Removing those factors leaves seven genuine linear amplitude constraints. The factors are compared exactly with evaluated pair differences; this is not a numerical nonzero test. The generic script `orbit7_generic.py` constructs the normalized family above and attempts the same division symbolically, retaining any removed node factors for later admissibility checks. A future global argument must audit all such factors and treat every exceptional locus rather than assuming a generic rank calculation covers it.

## Completed generic linearization

The generic symbolic check completed in2.22seconds under the watchdog. All seven quotients are exactly homogeneous linear forms in(j,k,l). No nonconstant row gcd was removed: every recorded row gcd is1. Every denominator is a product of u,v,w,z, their differences from1, and pairwise differences, so every denominator is nonzero on the distinct-node locus.

The forbidden factors divided out, in T order, are

    -k, -j, -l, -P2(u), lead(P2)-l, j-P3(0), -P3(u).

Each is an extra equality of an outsider with the quadruple at the indicated node (infinity for the leading-coefficient expression), hence is nonzero in a saturated realization. The resulting complete7-by3 coefficient matrix is exported in `orbit7_generic.json`; `orbit7_generic.py` verifies the divisions exactly. Any admissible realization must lie in the rank-at-most-two locus of this matrix with j,k,l all nonzero. This conclusion covers all distinct normalized quadruple-node configurations, not only a generic open subset beyond the already-required node guards.

## Exhaustive two-branch reduction; second branch excluded

Rows are numbered from zero. Minor(0,1,3), after removing only nonzero node factors, is the product

    ((w-1)(z-v)u+vw(w-v))
    * ((v(w+z-1)-wz)u+wz(1-v)).

Thus every realization belongs to one of the two branches

    I:  u=vw(v-w)/((w-1)(z-v)),
    II: u=wz(v-1)/(v(w+z-1)-wz).

The first denominator is a node guard. The second cannot vanish on its branch: otherwise its defining equation would give wz(1-v)=0, also a node collision. No third exceptional branch is omitted.

On branchII, minor(0,1,2) has, up to nonzero node factors and denominator factors, the square

    [v(w+z-1)-2wz+z]^2,

whereas minor(0,3,4) has the square

    [v(w+z-1)-z]^2.

Both must vanish. Subtracting their unsquared expressions gives 2z(1-w)=0. This is impossible in characteristic different from2. Thus branchII is globally excluded in odd characteristic and characteristic zero. These substitutions and the exact lists of removed guards are recorded in `orbit7_branches.py/json`; the watchdog run completed in14.2seconds, approximately69MiB RSS.

BranchI remains unresolved at this stage. No global orbit7 obstruction or positive realization is claimed.

## Symmetry consequences and scope of algebraic diagnostics

`orbit7_symmetry.py` checks the21 permutations preserving both displayed Fano systems. For each it permutes the quadruple coordinates and renormalizes the first three to infinity,0,1 by an exact projective transformation. Since branchII is impossible in every such normalization, the branchI equation must hold in each transformed set of coordinates. Substituting the original branchI expression for u gives the additional necessary polynomial equations in `orbit7_symmetry.json`. Only transformed node guards are cancelled. This is a necessary-condition argument, not an assertion that every rank-two amplitude solution realizes distinct triple nodes.

The nonsaturated Groebner diagnostics `orbit7_branch1_basis.*` and `orbit7_symmetry_basis.*` operate over Q. Their nonunit outputs do not imply a realization: they still include forbidden node-collision components. Conversely no all-characteristic conclusion may be inferred merely from rational Groebner arithmetic. Any subsequent exclusion must explicitly invert mandatory guards and record its characteristic scope.
