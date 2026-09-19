# Four-cycle reduction for arbitrary two-fiber error banks

2026-09-18. Independent algebraic audit: **PASS**. This gives a restriction on a surviving partial-bank target, not a construction or a linear-count upper bound for arbitrary witnesses.

## Setup and statement

Use the domain, code, and quotient maps of FIXED_SUBGROUP_QUOTIENT_PLANES.md. In particular ell>=11 is odd, n=(ell²-1)/2, t=(ell-1)/2, strict message dimension k=n-4ell+1, redundancy r=4ell-1. All ell-torsion is rational and the characteristic is different from ell and two. Write Φ for the domain locator. For a subgroup H, its t nonkernel tag fibers D_a have size ell and locators L_a=N_H-a B_H. Also

    Φ=K_H prod_a L_a,   C_H=K_H B_H^(t-4).

Let L be a two-dimensional syndrome space of a received pencil. Assume at least one endpoint has maximum codeword agreement strictly below n-2ell. This assumption follows, for example, from being far at the intended threshold n-2ell-5.

For each H form a simple graph G_H on its t tags. An edge {a,b} is present if some nonzero syndrome point on the projective line P(L) admits an error vector supported in D_a union D_b whose restriction to EACH of the two fibers is nonzero. Individual coordinates within either fiber may vanish. Error values may be arbitrary and nonconstant within a fiber; they are not assumed in advance to be C_H-weighted.

**Four-cycle lemma.** If G_H contains a cycle on four distinct tags, then L is contained in the canonical three-dimensional syndrome space V_H spanned by the zero-extended functions

    C_H Y_H^(t-3), C_H Y_H^(t-2), C_H Y_H^(t-1).

Together with dim(V_H intersect V_H')<=1 for H distinct from H', this implies that at most one G_H contains a four-cycle. Consequently the total number of distinct projective challenge points certified by errors genuinely using two fibers is at most

    binom(t,2) + ell * t/4 * (1 + sqrt(4t-3))

(and an integer floor may be applied to each graph bound). Errors using only one fiber add at most ell+1 points in total. Thus ALL errors supported on at most two nonkernel fibers give at most this displayed bound plus ell+1, still O(ell^(5/2))=O(n^(5/4)). The bound leaves a superlinear partial bank possible.

## Four-cycle proof

Let its four edges be ab,bc,cd,da. Choose corresponding actual error vectors e_ab,e_bc,e_cd,e_da, each with nonzero restriction on both of its two blocks. No coordinatewise nonvanishing is assumed. Let W be their linear span and U the union of the four fibers.

Any three of these errors form a path and are linearly independent: a leaf block occurs in only one remaining edge, so its nonzero restriction forces that coefficient to vanish, and iteration eliminates the other coefficients. Thus dim W>=3.

The parity-check map restricted to vectors supported on U has one-dimensional kernel. Indeed |U|=4ell=r+1, and any r parity-check columns are independent. All four images lie in L, which has dimension two. Rank-nullity therefore gives dim W<=3. Equality holds, and there is a unique linear dependence among the four errors, with every coefficient nonzero (otherwise three would be dependent).

On each vertex block the dependence contains just its two incident edge restrictions. Hence those two restrictions are proportional. Choose a nonzero local vector v_a supported in D_a, and similarly v_b,v_c,v_d, so every edge error lies in the span of its two corresponding local vectors. These four local vectors are independent, having disjoint supports. Their span contains W and therefore contains the nonzero parity-check kernel vector supplied by W.

The unique codeword supported on U is a scalar multiple of the evaluation of

    P_U(X)=Φ(X) / prod_{a in {a,b,c,d}} L_a(X).

Its degree is n-4ell=k-1, it vanishes precisely outside U on the evaluation domain, and it is nonzero at every coordinate of U. Thus each v_a is proportional to P_U restricted to D_a. In particular every local vector is now FORCED to have full coordinate support, and so are both restrictions of each cycle error. This is a consequence of the cycle, not a hypothesis. This identity can also be written P_U(x)=Φ'(x)/(prod_four L_a)'(x) on U, but derivatives are unnecessary for the argument.

Crucially,

    P_U(X)=C_H(X) prod_{tag z outside {a,b,c,d}} (Y_H(X)-z).

On a selected fiber D_a, the last product is a nonzero scalar. All four local vectors are therefore proportional to the restriction of C_H to their respective fibers. Each cycle edge error is a canonical weighted-tag error and its syndrome belongs to V_H.

The syndrome points of adjacent edges are distinct. Otherwise a nontrivial linear combination of their errors would be a codeword supported on three fibers, contradicting parity-check injectivity on 3ell<4ell-1 coordinates; the combination is nonzero by the exclusive leaf blocks. Two distinct projective syndrome points span L. Hence L is contained in V_H, as claimed.

## From cycles to the count bound

The independently audited three-space intersection result is proved in FIXED_SUBGROUP_QUOTIENT_PLANES_INDEPENDENT_AUDIT.md. It uses rational degree and kernel-pole arguments and does not assume the errors in the present graph are canonical. Since distinct V_H intersect in dimension at most one, a two-space L can lie in at most one of them. Every other graph G_H is four-cycle-free.

For a four-cycle-free simple graph on t vertices, any two vertices have at most one common neighbor. Thus

    sum_v binom(deg(v),2) <= binom(t,2).

Cauchy-Schwarz, with edge count e, gives

    2e²/t-e <= t(t-1)/2,

and therefore e<=t(1+sqrt(4t-3))/4. Apply the complete-graph bound to the possible exceptional subgroup and this extremal bound to the remaining ell subgroups.

To pass from edges to labels, each support must contribute at most one projective syndrome point. If L intersect S_(D_a union D_b) had dimension two, then the whole pencil would admit explanations with at most 2ell errors, contrary to the far-endpoint premise. Thus each edge specifies one projective point. Different edges may still give the same point, which only reduces the total count. An affine chart cannot increase it.

Single-fiber errors contribute at most one projective syndrome point per subgroup. If two distinct such points exist, their span is L and is contained in the sum of the two corresponding fiber spaces (or in one fiber space if they use the same fiber). This would put L inside a two-fiber support space and contradict the far-endpoint premise. Summing over ell+1 subgroups gives the additional ell+1 term; collisions across subgroups only decrease the count.

## Scope and surviving target

This result applies to arbitrary error vectors supported on at most two nonkernel fibers, including partial coordinate support. A graph edge requires nonzero restriction on both fibers; the separate single-fiber argument covers the remaining nonzero errors. Leaf independence requires only these nonzero restrictions. The unique MDS kernel word forces full coordinate support when a four-cycle occurs. Witnesses using up to five additional errors, kernel-fiber additions, or other support families are not covered.

The result does not prove the surviving O(n^(5/4)) scale attainable. A proposed superlinear bank in this model must, apart from at most one subgroup, have a four-cycle-free graph of represented pairs. The combinatorial supply of such graphs is not enough: the common syndrome line and its distinct-label/source-distance conditions still require proof. No finite-field scan or elliptic computation was used.

Revision audit: the original full-coordinate-support premise was unnecessarily strong. The strengthened proof above uses only nonzero restrictions on the two endpoint fibers and derives full support on every cycle. The O(n^(5/4)) conclusion now includes all at-most-two-fiber error supports, with an explicit additional ell+1 allowance for single-fiber points.
