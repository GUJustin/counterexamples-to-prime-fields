# Four-cycle reduction for arbitrary two-fiber error banks

2026-09-18. Independent algebraic audit: **PASS**. **Superseded count bound:** TWO_FIBER_LINEAR_RESOURCE_BOUND.md now proves O(n) in the same at-most-two-fiber model via three-edge paths and 2-degeneracy. The cycle arguments below remain historical valid proofs, not the current surviving exponent. This gives a restriction on a surviving partial-bank target, not a construction or a linear-count upper bound for arbitrary witnesses.

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


## Five-cycle extension: independently checked

Under exactly the same assumptions, a cycle on FIVE distinct tags also forces L contained in V_H. This does not assert the analogous conclusion for longer cycles. In particular every subgroup except possibly one has neither a four-cycle nor a five-cycle. The numerical O(n^(5/4)) bound above is unchanged; no stronger extremal estimate is claimed here.

Index the five vertices cyclically by i, their fiber locators by F_i=N_H-a_i B_H, and their chosen edge errors by e_i on fibers i and i+1. Each error has nonzero restriction on each endpoint fiber. Let W=span(e_1,...,e_5). Any four edges form a path, so leaf elimination shows they are independent. Thus dim W is four or five. Adjacent edge syndromes are distinct by parity-check injectivity on three fibers, as before, and hence the syndrome image of W has dimension exactly two.

Let U be the union of the five fibers and put R_5=Φ/prod_(i=1)^5 F_i. The codewords supported on U are precisely evaluations of R_5 P for polynomials P of degree at most ell: indeed deg R_5=n-5ell and k-1=n-4ell. Restriction of R_5 to U is everywhere nonzero. The kernel of evaluation of degree-at-most-ell polynomials on fiber i is exactly the one-dimensional span of its monic locator F_i.

### Excluding dim W=5

Suppose the five errors are independent. Their codeword subspace then has dimension three. Identify it with a three-dimensional residual polynomial space A consisting of the P for which eval(R_5 P) lies in W. At each fiber, the local restrictions of W span at most two dimensions, since only its two incident edges contribute. Therefore evaluation of A on that fiber has rank at most two. Its kernel has dimension at most one by the preceding locator fact; hence it has dimension exactly one and F_i belongs to A. The local evaluation rank is exactly two, so the two incident edge restrictions are independent at every vertex.

Because the five errors are a basis of W, each edge has a well-defined coefficient functional c_i on A. The codeword R_5 F_i vanishes on fiber i. Local independence forces both incident coefficients, c_(i-1)(F_i) and c_i(F_i), to vanish. The same argument on fiber i+1 gives c_i(F_(i+1))=0. Since distinct tag locators F_i and F_(i+1) span the two-dimensional space span(N_H,B_H), EVERY coefficient functional c_i vanishes on this space. But this space is contained in A, and the map from A to its five edge coefficients is injective: multiplication by R_5 and evaluation on U are injective for degree at most ell. This contradiction excludes dim W=5.

### The rank-four case is canonical

Thus dim W=4. Its single dependence on the five edge generators has all coefficients nonzero, since any four are independent. On each vertex this dependence makes the two incident restrictions proportional, so the local span is one-dimensional.

The codeword subspace of W now has dimension two; let A be its residual degree-at-most-ell polynomial space. At each fiber, evaluation of A has rank at most one. The locator-kernel fact again forces F_i to belong to A. Therefore

    A=span(N_H,B_H).

In particular eval(R_5 B_H) lies in W and is nonzero at every point of each selected fiber. It fixes their local shapes. Moreover

    R_5 B_H = C_H prod_(tag a outside the five)(Y_H-a).

The last product is a nonzero scalar on each selected fiber. Thus every local shape is proportional to C_H, and every cycle edge syndrome belongs to V_H. Two adjacent syndrome points span L, proving L contained in V_H.

The proof permits vanishing individual coordinates initially; it derives full support of all cycle restrictions. It continues to exclude extra-error coordinates outside the two selected fibers. Its use of actual edge errors, residual polynomial spaces, and injective coefficient maps is essential; a graph count without these incidence identities would not establish the conclusion.


## Six-cycle extension: independently checked

A cycle on SIX distinct tags likewise forces L contained in V_H. This assertion requires t>=6; for smaller t there is no such cycle. The following proof concerns only this cycle and does not assume a classification of longer cycles.

Let its edge errors e_1,...,e_6 have nonzero restrictions on their endpoint fibers, and let W be their span. Any five form a path and are independent; adjacent syndromes are distinct, so the syndrome image of W has dimension two. Thus dim W is five or six. Write F_i=N_H-a_i B_H and R_6=Φ/prod_(i=1)^6 F_i. Codewords supported on these six fibers are precisely eval(R_6 P), deg P<=2ell.

### Rank six is impossible

Suppose dim W=6. Let A be its residual polynomial kernel space, of dimension four, inside the polynomials of degree at most 2ell. For each vertex set

    A_i={P in A: F_i divides P}.

Evaluation on its fiber has rank at most two, so dim A_i>=2. For distinct i,j, the intersection A_i intersect A_j consists of polynomials divisible by F_i F_j, of degree at most 2ell. It therefore has dimension at most one. Consequently at most one A_i can have dimension at least three: two such subspaces of the four-space A would intersect in dimension at least two. No A_i has dimension four, because its intersection with any other A_j would then have dimension at least two.

Call a vertex good when dim A_i=2. At a good vertex, evaluation of A has rank exactly two, so the two incident edge restrictions are independent. Let c_i:A -> field be the coefficient of edge e_i in the unique W-basis expansion of eval(R_6 P). This functional is nonzero: if it vanished on A, the four-dimensional codeword kernel would lie in the span of the five other errors, whose dimension is five and whose syndrome image has dimension two, giving kernel dimension only three.

For an edge with both endpoints good, c_i vanishes on A_i and A_(i+1). As c_i is nonzero, their sum has dimension at most three; hence their intersection is nonzero. Its polynomials are multiples of F_i F_(i+1), so this product belongs to A.

There are at least five good vertices. Deleting the possible bad vertex leaves a path of five good vertices and four good-good edges. Three consecutive edge products span

    S=span(N_H², N_H B_H, B_H²).

Indeed, the first two products share their middle locator and span that locator times span(N_H,B_H), while the third does not vanish at that middle tag. Thus S has dimension three and is contained in A. At every good vertex A_i=F_i span(N_H,B_H), since the right side is a two-space already contained in A_i. Each of the four good-good edge functionals therefore vanishes on all of S: the sum of the two distinct spaces F_i span(N_H,B_H) and F_(i+1) span(N_H,B_H) is S.

The injective map from A to its six edge coefficients consequently sends the three-space S into at most the two remaining coordinate positions. This is impossible. If all vertices are good, one may still select any five-vertex path, giving the same contradiction. Thus dim W cannot be six.

### Rank five forces canonical weights

Now dim W=5. Its unique edge dependence has every coefficient nonzero, so incident restrictions are proportional at every fiber. The residual codeword space A has dimension three and degree at most 2ell, and evaluation on each fiber has rank at most one. Hence dim A_i>=2. For every distinct pair i,j, dimension counting in A gives A_i intersect A_j nonzero. Divisibility and degree imply F_i F_j belongs to A. Three suitable pair products span S, so A=S.

In particular eval(R_6 B_H²) is a codeword in W, nonzero everywhere on its six fibers. The identity

    R_6 B_H² = C_H prod_(tag a outside the six)(Y_H-a)

forces each local error shape to be proportional to C_H. All six edge syndromes are in V_H, and adjacent ones span L. This proves the six-cycle assertion.

Accordingly, outside at most one subgroup, the represented-pair graph has no cycles of lengths four, five, or six. The previous numerical bound is retained here; any improved extremal estimate requires its own justification. Extra error coordinates outside the selected fibers remain excluded.


### Elementary improved count after the six-cycle lemma

A graph on t vertices with neither a four-cycle nor a six-cycle has at most 2t(1+t^(1/3)) edges. Here is a self-contained bound sufficient for the exponent. A bipartite subgraph retains at least half its e edges. If it has E edges, iteratively delete vertices of current degree less than E/t, keeping this threshold fixed. Not all vertices can be deleted, since otherwise their removed edge counts would sum to less than E. The remaining nonempty bipartite graph has minimum degree delta>=E/t>=e/(2t). Its girth is at least eight. If delta>=2, a breadth-first tree through depth three gives at least 1+delta+delta(delta-1)+delta(delta-1)^2 distinct vertices: a repetition would create a cycle of length at most six (odd cycles are absent). Thus t>=(delta-1)^3 and delta<=1+t^(1/3). If delta<2 the claimed bound follows immediately as well. Combining yields the stated edge estimate.

Apply this to all but the possible exceptional subgroup. Including its complete graph and all single-fiber points, the number of projective challenge classes certified by arbitrary at-most-two-fiber errors is at most

    binom(t,2) + 2ell*t*(1+t^(1/3)) + (ell+1)
    = O(ell^(7/3)) = O(n^(7/6)).

The constants are deliberately elementary. One may take the minimum of this bound and the earlier four-cycle bound at any finite ell. This improves the surviving upper exponent but still permits a superlinear bank; it proves neither existence nor a linear ceiling.
