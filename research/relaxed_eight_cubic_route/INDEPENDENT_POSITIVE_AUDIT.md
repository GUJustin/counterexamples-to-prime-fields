# Independent positive-construction audit

## Seed and smooth characteristic-zero lifting: PASS

`independent_verify.py` rebuilds all 56 incidence equations from the eight
coefficient rows and sixteen received values in `local_search.json`.
Every polynomial has exactly seven agreements. The sixteen nodes are
nonzero and distinct; the eight leading coefficients are nonzero and
distinct. The selected 56 Jacobian columns are all32 coefficient
variables, node variables1..14, and word variables1..10. Their determinant
is14 modulo17. This is an independent modular elimination, not a rank
value copied from the search.

The same verifier exhausts all1820 four-point supports with independent
Vandermonde solves. There are1022 distinct interpolants, maximum agreement7,
and exactly the eight listed maximizers. Any cubic with at least four
agreements, even over the algebraic closure, is uniquely determined over
F17 by four matching points, so this is a complete census.

Fix the eight nonpivot variables to their displayed integer residues.
Multivariate Hensel gives an integral17-adic solution to the square
56-equation system. The Jacobian remains invertible. The solution is
algebraic over Q: the corresponding characteristic-zero component has
local dimension zero by the Jacobian criterion (equivalently,
differentiating the equations makes the module of differentials of the
finitely generated coordinate field over Q vanish). Hence the solution
generates a number field embedded in Q17, not an unspecified transcendental
17-adic point. All open guards survive because their reductions are units.

Source completeness also lifts. Any cubic with seven agreements has
integral coefficients by interpolation on four unit-separated source
nodes. Its reduction is one of the eight finite-field cubics. Its seven
matching indices must be exactly that cubic's known support, and four-
point uniqueness then identifies it with the lifted listed cubic.
More than seven agreements would contradict the finite-field census.

## Square pullback completeness: PASS

At characteristic17, all32 points above the sixteen nonzero Y nodes are
distinct over F289. For a non-even degree-six competitor write

    Q(T)=E(Y)+T O(Y), Y=T^2, degE<=3, degO<=2, O!=0.

Both signs can agree only where O(Y)=0, so at most two full fibers occur.
Fourteen agreements therefore require at least twelve norm-hit fibers.
At each such fiber,

    w^2+B(Y)w+C(Y)=0, B=-2E, C=E^2-YO^2.

The independent replay `verify_quadratic_pullback.py` reverses the unknown
order to C0..C6,B0..B3, enumerates omitted four-subsets, and uses forward
elimination/back substitution rather than the generator's RREF. It
reproduces all1820 ranks:1686 inconsistent rank11,132 consistent rank11,
and2 inconsistent rank10. No positive-dimensional consistent stratum
is omitted. The132 consistent systems give84 distinct norm polynomials.
Since every consistent system has full column rank, these polynomials
are defined overF17 even if Q has arbitrary algebraic-closure coefficients.

Every one of the84 candidates fails at least one of the NECESSARY
coefficient conditions

    C0=E0^2, C6=E3^2.

Thus all are excluded before any square-root test. This independently
proves that no non-even degree-six polynomial has14 agreements over
Fbar17. Even candidates reduce to the complete cubic source census,
so the square pullback has maximum agreement14 and exactly8 maximizers.

For characteristic-zero transfer, every lifted source coordinate is a
17-adic unit. Adjoin their square roots in the unramified quadratic
extension; the residues are32 distinct points ofF289, since17 is odd.
Any degree-six competitor with14 agreements is integral by interpolation
on seven of these unit-separated points. Its reduction must be one of
the eight even listed polynomials and has exactly its fourteen-point
support. The lifted competitor and that listed polynomial agree at
those points, so seven-point uniqueness makes them identical. This
covers an apparently non-even competitor whose odd part vanishes after
reduction; such a polynomial cannot be dismissed solely by reducing its
odd part.

## Prime-field specialization and scope

Adjoin all32 square-root coordinates to the number field and take a
finite Galois closure. Outside finitely many primes, coefficients,
node separation, supports, and nonzero leading coefficients persist.
Completeness persists as well: there are only finitely many four-point
source and seven-point pullback interpolants, and all their nonzero
evaluation differences can be protected by excluding finitely many
prime ideals. Arbitrarily large rational primes split completely in
the finite Galois extension; their residue fields are prime fields and
contain every coordinate. This yields COMPLETE nearest lists of size8
at n16,k4,A7 and n32,k7,A14 over arbitrarily large prime fields.

The latter rho=7/32 and a=14/32 satisfy the high-rate branch condition
rho>11-3sqrt13 and the exact positive margin

    (8-rho)a^2-6rho*a+rho(4rho-5)=105/8192.

The capacity gap is7/32. List size8 and length32 are fixed. No growing-list,
length-exponent, or better.codes ledger improvement is claimed.

The seed has incidence histogram{2:4,3:2,4:8,5:2} and pair usage78<84.
In particular its two fivefold points escape the preserved-four-seed
transversal model; this is not a counterexample to that model's exclusion.
