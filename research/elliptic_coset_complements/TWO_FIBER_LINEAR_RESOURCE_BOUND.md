# Linear label bound for arbitrary two-fiber elliptic errors

2026-09-18. Independent audit: **PASS**. This supersedes the four-, five-, and six-cycle count bounds. It closes the displayed at-most-two-nonkernel-fiber support model with a far endpoint, including arbitrary error values within each fiber. It does not cover five additional error coordinates.

## Hypotheses and exact bound

Let ell>=11 be an odd prime, different from the field characteristic, and use the elliptic domain and quotient maps in FIXED_SUBGROUP_QUOTIENT_PLANES.md. In particular the characteristic is greater than three, all ell-torsion is rational, and

    n=(ell²-1)/2, t=(ell-1)/2, k=n-4ell+1, r=n-k=4ell-1.

The code consists of polynomial evaluations of degree less than k. Each order-ell subgroup H supplies t disjoint nonkernel fibers D_a, each of size ell. Their locators are F_a=N_H-a B_H, where B_H=K_H² and

    Φ=K_H prod_a F_a,   C_H=K_H B_H^(t-4).

Consider a genuine two-dimensional syndrome plane L of a received pencil. Assume at least one endpoint has maximum codeword agreement strictly less than n-2ell. In particular, an endpoint far at the tested threshold n-2ell-5 satisfies this condition.

Count projective syndrome points on L admitting an error vector supported in at most two nonkernel fibers for some H. Individual error entries may vanish; neither constant nor canonical values within a fiber are assumed. The number of distinct such points is at most

    binom(t,2) + ell*(2t-3) + (ell+1)
    = (9ell²-28ell+11)/8
    = O(n).

The same upper bound applies to any affine chart of this pencil. This is a support-restricted statement, not an upper bound for all near codewords at the slack-five threshold.

## Two elementary syndrome facts

Parity-check columns are MDS: any at most r are independent. For two adjacent fiber pairs {a,b} and {b,c}, chosen errors with nonzero restrictions on both endpoint fibers cannot have proportional syndromes. Otherwise their nonzero difference would be a codeword supported on at most 3ell<r coordinates. The difference is nonzero because of the two exclusive leaf fibers.

An error support contained in one fixed pair contributes at most one projective point on L. If L were contained in that support syndrome space, every pencil word, including the assumed far endpoint, would admit at most 2ell errors. This is excluded. Representation on a given pair is unique after fixing the syndrome, because 2ell<r.

For each H, make a simple graph G_H on its tags: an edge is present if a point of L has an error supported on its two fibers with nonzero restriction on EACH. Fix one such error per edge. Errors confined to one fiber are counted separately below.

## Three-edge-path rigidity

Take any simple path a-b-c-d and its three errors e_ab,e_bc,e_cd. The three syndromes lie in L, so there is a nontrivial relation

    alpha*s(e_ab) + beta*s(e_bc) + gamma*s(e_cd)=0.

Both alpha and gamma are nonzero: if either vanished, the two remaining adjacent syndromes would be proportional, contrary to the preceding fact. The middle coefficient beta is allowed to vanish.

The error combination

    w=alpha*e_ab + beta*e_bc + gamma*e_cd

is nonzero, because its restriction on the leaf fiber D_a is alpha times a nonzero vector. It is a codeword supported on the union U of the four fibers. Since |U|=4ell=r+1, the shortened code on U is one-dimensional. Explicitly, w is a nonzero scalar multiple of the evaluation of

    Φ/(F_a F_b F_c F_d).

This polynomial has degree n-4ell=k-1 and has no zero on U. The identity

    Φ/(F_a F_b F_c F_d)
      = C_H prod_(tag z outside {a,b,c,d})(Y_H-z)

shows that its restriction on each selected fiber is a nonzero scalar multiple of C_H. On the two leaves there is no other error term. Therefore e_ab restricted to D_a and e_cd restricted to D_d are canonical C_H-weighted vectors. Full coordinate support at these leaves follows automatically; it was not assumed.

## A nonempty 3-core forces the canonical syndrome plane

Suppose G_H has a nonempty subgraph of minimum degree at least three. Every oriented edge a->b in that subgraph extends to a simple three-edge path a-b-c-d. Choose a neighbor c of b different from a, then a neighbor d of c outside {a,b}; the degree-three condition guarantees this choice. The path lemma makes the restriction of e_ab on D_a canonical. Apply it also to the reverse oriented edge b->a to obtain the canonical restriction on D_b.

Hence every edge of this subgraph has both restrictions C_H-weighted. Its syndrome lies in the canonical three-space V_H spanned by the zero-extended functions

    C_H Y_H^(t-3), C_H Y_H^(t-2), C_H Y_H^(t-1).

To see this directly, interpolate the tag weights by a polynomial of degree at most t-1; multiplying its terms of degree at most t-4 by C_H gives codewords, leaving exactly these three syndrome generators. Two adjacent edges exist and their syndrome points are distinct, so they span L. Thus L is contained in V_H.

The independent pole/degree audit in FIXED_SUBGROUP_QUOTIENT_PLANES_INDEPENDENT_AUDIT.md proves

    dim(V_H intersect V_H') <= 1  for H != H'.

Therefore at most one subgroup graph has a nonempty 3-core.

## Counting edges and one-fiber points

A graph with no nonempty minimum-degree-three subgraph is 2-degenerate: repeatedly remove a vertex of degree at most two. On t>=2 vertices it has at most 2t-3 edges, since the last two vertices contribute at most one edge and each preceding vertex at most two. The possible exceptional subgroup contributes at most binom(t,2) edges. There are ell+1 subgroups, so two-fiber points are bounded by

    binom(t,2)+ell*(2t-3).

For each H, there is at most one additional projective point admitting a one-fiber-supported error. Two distinct such points would span L inside the sum of their fiber support spaces (or in one fiber space), contradicting the far-endpoint hypothesis. Thus adding ell+1 bounds all at-most-two-fiber points. Different supports or subgroups may share points; counting them separately only enlarges the bound.

## Scope

The result permits arbitrary, partially vanishing error values inside the selected nonkernel fibers. Its exact premises are a genuine syndrome pencil, a far endpoint, and support contained in at most two of these fibers. It excludes a superlinear challenge population within that entire model.

It does not exclude witnesses supported on two fibers plus up to five other coordinates, kernel-fiber additions, different omission families, or received pencils with no far endpoint. In particular, the numerical slack-five Johnson/first-order window alone does not put every qualifying witness inside this two-fiber model. No finite-field scan or generic dimension heuristic enters the proof.
