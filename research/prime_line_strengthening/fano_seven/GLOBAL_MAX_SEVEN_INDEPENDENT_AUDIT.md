# Independent audit of the universal max-seven chain

Verdict: PASS in characteristic zero. The same finite proof gives the result
in all sufficiently large characteristics, after excluding finitely many
integer divisors. This audit does NOT claim every odd characteristic.

**Statement.** On any fourteen distinct field elements in characteristic
zero, a received word has at most seven distinct degree-at-most-three
polynomials with at least seven agreements. The explicit orbit7 example
attains seven. The assertion remains true over algebraic closures.

## Pair counting and possible repeated columns

For seven candidates, at least49 incidences and at most63 pair incidences
force exactly49 incidences, seven columns of size3 and seven of size4, and
exactly three shared coordinates for every pair. Indeed the convex minimum
at49 is63; at50 it is66. If t_i,q_i count triple and quadruple incidences,
t_i+q_i=7 and2t_i+3q_i=18, giving t_i=3,q_i=4.
The seven triple blocks T and the complements C of the seven quadruples
are therefore three-regular triple MULTISETS with pair counts adding to2.
Nothing at this step assumes distinct incidence blocks. Combined block
multiplicities are at most2 because each block contains a pair.

The independent vertex-by-minimum enumeration in independent_design_set.py
allows repetitions, enumerates12780 labelled regular halves, and joins the
complementary pair-count vectors into exactly6150 ordered labelled pairs.
Literal equality with the disjoint S7 expansions of the eight representatives
was checked; no swapping of T and C is assumed. Thus the list of eight cases
is exhaustive even for repeated support columns. This is an independently
implemented check, not merely agreement of two orbit counts.

The proven exclusions of orbits0,1,3,4,5,6 apply to all distinct coordinates,
including charts with triple nodes at infinity. The involution normalization
in0,1,3 loses no chart; their rational branch denominators are explicitly
handled. Orbits4,5,6 have independent proof audits. No assumption about the
actual values of the received word is imported into these exclusions.

## Why every eight-bank has an orbit7 subbank

For eight candidates, at least56 incidences and at most84 pair incidences
force exactly four candidates at every column, seven matches per candidate,
and exactly three matches per pair. Deleting any candidate produces one of
the seven-bank designs above. Conversely the extension of a given(T,C) is
unique: adjoin candidate8 to the T blocks and leave the quadruple blocks
unchanged.

If a seven-subbank is orbit7, nothing remains to prove at this stage. If it
is orbit2, delete candidate3 from its unique eight-extension. The resulting
seven-bank is orbit7 under the explicit label mapping

    1->1, 2->3, 4->5, 5->6, 6->7, 7->4, 8->2.

`global_seven_independent_checks.py/json` verifies this direct mapping on
both sets of blocks, without reusing the6150-entry classification lookup.
The full64-deletion table is supplementary; this single explicit map suffices.

## Orbit7 classification, without trusting a Groebner verdict

The normalized quadruple nodes are infinity,0,1,u,v,w,z. Subtraction of P1
and normalization of the nonzero quadruple value j give the complete
three-amplitude family recorded in ORBIT7_REDUCTION.md. Every discarded
amplitude factor is a forbidden additional quadruple equality. Node
factors and every projective normalization denominator are nonzero.

The two exhaustive branches from minor013 cover its denominator-zero loci.
BranchII is impossible in characteristic zero. On branchI,

    u=vw(v-w)/((w-1)(z-v)).

Every listed ordered-design automorphism produces another valid normalized
branchI identity: the inverse node permutation and determinant cross-ratio
normalization in orbit7_symmetry.py have been checked. Every canceled factor
is a factor of a mandatory nonzero node guard after substitution.

The independently implemented sparse Fraction checker validates the entire
380-node arithmetic identity DAG and checks its input set against these
necessary equations. It uses no SymPy arithmetic. Saturation introduces
only t(v-z)(w-1)=1, legal on every admissible realization. The certificate
proves the following exact ideal-membership consequences:

    (z-1)(w^2+w-z)=0,
    (z-1)(wz-2w+z-1)=0,
    (z-1)(v-z+1)=0.

Since z!=1, these imply z=w^2+w,v=z-1 and
w^3+2w^2-w-1=0. Substitution in branchI gives u=w^2. Thus every admissible
normalized realization is one of the three conjugates of the displayed
cubic-field point; no other component remains.

The amplitude matrix has rank exactly2 there. Independently, its rows0,1,
columns0,1 minor equals6w^2-2w-2, nonzero modulo the irreducible cubic.
Its normalized kernel is uniquely

    (j,k,l)=(1,3w^2+4w-5,3w^2+4w-6).

Therefore all admissible orbit7 banks are the displayed bank up to the
invertible coordinate, common-polynomial, and scalar transformations used
in the proof. Those transformations preserve agreement and cubic degree
as binary sections.

## The eighth candidate is impossible

For the classified bank, a putative eighth cubic must match every triple
node and no quadruple node. The independent five-point test fixes its scalar
from the first four targets and gives error486-390w-270w^2 at the fifth.
This is nonzero modulo the irreducible cubic, and remains nonzero at every
conjugate. Thus no orbit7 bank can have an eighth candidate. The deletion
argument proves the universal statement.

## Characteristic scope

All enumeration steps are combinatorial. The algebraic proof uses finitely
many rational polynomial identities, nonzero integer constants, and
nonvanishing resultants with the cubic for the amplitude minor and fifth
error. Clear all denominators and exclude their prime divisors, along with
these resultants and the existing guarded scalar constants. Outside this
finite set the same proof applies over the algebraic closure in that
characteristic. In particular it establishes an eventual prime-characteristic
upper bound; it does not justify silently replacing this by all odd primes.

The positive example reduces over arbitrarily large split primes, so seven
is sharp in characteristic zero and is attained in arbitrarily large prime
fields. This is a finite-parameter exact-list theorem, not an unbounded-list
construction, first-order proximity-gap tightness, or a better.codes gain.
