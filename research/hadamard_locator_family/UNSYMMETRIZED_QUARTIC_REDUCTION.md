# What symmetry does not prove, and a symmetry-free quartic reduction

## 1. The closed C2 family and the disjoint-copy target differ

`UNIVERSAL_C2_NORM_BRIDGE.md` assumes two aligned copies of the affine-
hyperplane design. Its six old fourfold masks occur at opposite pairs of
nodes and its eight transversal masks each occur at two quadratic roots.
It therefore has fourteen distinct incidence masks, each repeated twice.
The design explicitly selected in `EXACT_TARGET.md` has twenty-eight
DISTINCT masks, from two disjoint Hadamard copies. Incidence-mask
multiplicities are invariant under candidate relabeling, node relabeling,
and changes of the parameter coordinate. The disjoint target cannot be
put into that C2 ansatz, even before testing whether a projective
involution exists.

The earlier symmetry gate in `C2_CEVA_REDUCTION.md` already separates
these cases. It does not prove that a realization of the disjoint design
has any nontrivial geometric automorphism.

## 2. An explicit counterexample to automatic lifting

Combinatorial incidence automorphisms need not act on the parameter line,
even for an existing saturated quarter-rate bank. Over Q take

    (a1,a2,a3,a4)=(1,2,5,13),
    H_i(X)=X^2/a_i^2+a_i^2,
    domain={ +/- a_i a_j : 1<=i<j<=4 }.

All twelve nodes are distinct. At either node of pair ij, the received
value a_i^2+a_j^2 agrees with H_i and H_j. No third candidate agrees,
because equality with H_k is equivalent to

    (a_k^2-a_i^2)(a_k^2-a_j^2)=0.

Thus this is the exact saturated L4 example: twelve nodes, four
quadratics, six agreements each, every pair sharing exactly two nodes.

Swap labels 1 and 2 and preserve the sign of each pair occurrence. This
is an automorphism of its block multidesign. On the domain it fixes the
four distinct nodes +/-a1a2 and +/-a3a4, but interchanges other nodes,
for example a1a3 and a2a3. A projective automorphism fixing three distinct
points is the identity. Therefore this combinatorial automorphism has
no PGL2 lift.

This disproves the general assertion that saturation makes design
automorphisms geometric. It does NOT by itself prove that every possible
eight-sextic realization is asymmetric: that stronger conclusion, or
its negation, remains to be proved. In particular, the existence of some
abstract involution gives no right to impose T->-T.

A precise missing lemma would be: the guarded realization moduli space,
quotiented by parameter PGL2 and the common-polynomial/value gauges,
contains a fixed point for an appropriate design involution whenever it
is nonempty. Neither a combinatorial automorphism nor zero expected
dimension implies that fixed-point assertion. A finite set of several
realization classes can be freely permuted. Uniqueness of the realization
class would suffice, but has not been established for this target.

For the disjoint design, the archived automorphism audit gives full
union group order336. If its exclusions of lifted order2/order3 elements
are used, any geometric stabilizer has order1 or7. Hence any finite set
of labeled realization classes is a union of group orbits of sizes336
or48. A proven total degree below48 would be a genuine obstruction;
no such degree bound is presently available. This is a precise possible
rigidity gate, not an argument from expected dimension.

## 3. Choose half of the nodes; the other half are quartic gcd roots

The disjoint two-Hadamard design is a 3-(8,4,2) design. Indeed each
Hadamard copy is the fourteen affine planes of F2^3, and each triple of
vertices lies in exactly one plane. Fix candidate0 and let Z be the
fourteen blocks containing0. Give their nodes arbitrary distinct values
z_C. The triples C minus {0}, for C in Z, form two disjoint Fano planes
on labels1,...,7.

For each nonzero label i define the monic sextic

    H_i(X)=product_{C in Z, i in C}(X-z_C).

It factors canonically as A_i B_i, where A_i and B_i are the monic cubic
locators from the two Fano copies. For i!=j there are exactly TWO blocks
containing0,i,j, one in each copy. Therefore

    G_ij=gcd(H_i,H_j)
        =(X-z_{C_ij})(X-z_{D_ij}),   deg G_ij=2.

Take nonzero pairwise distinct constants lambda1,...,lambda7, with
lambda0=0, and form the quartics

    Q_ij(X)=(lambda_i H_i(X)-lambda_j H_j(X))/G_ij(X).

They have degree exactly four. No involution, parity restriction, common
cover, or relation between the two copies' node values is assumed.

For every block B not containing0, let

    R_B(X)=gcd { Q_ij(X) : i,j in B, i<j }.

There are fourteen such gcds, each using six quartics. The complete
unsymmetrized realization problem has the following equivalent form:

1. Every R_B has degree exactly one.
2. Its root y_B is outside all fourteen chosen nodes z_C.
3. The fourteen y_B are pairwise distinct.
4. The z_C and lambda_i satisfy the distinctness guards above.

These are exact algebraic conditions on fourteen node values and seven
leading coefficients. They eliminate the other fourteen node variables.
On each subresultant chart the missing nodes are rational functions of
these parameters, because their monic gcd is linear. A root of a
quartic need not be adjoined.

### Necessity

Subtract the zeroth candidate from every candidate and from the word.
Saturation and the six prescribed roots give P_i=lambda_i H_i. In a true
realization, Q_ij has exactly the four roots y_B for blocks B avoiding0
and containing i,j. These roots are distinct. Intersecting those four-
root sets over all six pairs within a given B leaves exactly the one
node belonging to B: all masks have size four and the design has no
repeated mask. Thus R_B is precisely X-y_B.

### Sufficiency

Set P0=0 and P_i=lambda_i H_i. At z_C the candidates in C agree at zero,
and exactly those candidates vanish. At y_B the six quartics vanish,
so the four candidates in B agree; the excluded known-node guard means
that no G_ij vanishes there. Every pair i,j has its two prescribed known
roots and its four prescribed distinct missing roots. Their difference
has degree six with nonzero leading coefficient, so this exhausts all
its roots. Any additional agreement outside a prescribed mask would
supply a seventh root to some pair difference. Thus the constructed bank
has EXACTLY the required incidence masks and is a valid eight-sextic
half-agreement realization. The nearest-list completeness argument of
`EXACT_TARGET.md` then applies unchanged.

## 4. What this buys, and what remains open

The initial42-by7 locator-kernel description uses all28 node variables.
The quartic formulation uses only14 chosen node variables plus7 leading
coefficients. Scaling the lambdas and affine parameter normalization
leave18 parameters; full PGL2 normalization gives17 on appropriate
charts, with its finite-domain guards retained. The missing nodes are
reconstructed rationally from explicit low-degree gcds.

A concrete next construction must produce a pair of labeled cubic-
locator families (A_i),(B_i) and distinct lambdas for which those fourteen
six-quartic gcds are linear and disjoint. This is genuinely outside the
closed C2/common-cover families: the two Fano node sets are independent,
and the factors vary with i. It is not multiplication of a known bank
by a common cubic. One can formulate the conditions using degree-four
subresultant rank drops without guessing any geometric symmetry.

This reduction is a bounded, falsifiable algebraic target. It is not a
positive construction, a global nonexistence theorem, or evidence that
random fixed-node probes will succeed. A payoff would be an identity
ensuring the fourteen linear gcds simultaneously, preferably one that
extends along a Hadamard recursion. Without such an identity or a genuine
rigidity theorem, imposing a parameter involution would discard the
very unsymmetrized solutions this target is intended to seek.
