# Two filtrations: exact obstruction and a bounded-degree transfer

Status: independently audited scoped theorem; integrated as a filtered-row-test corollary. It extends neither arbitrary filtered spaces nor nonmonomial Eq64 without additional work.

## Exact obstruction to preserving both jet filtrations

Take D=2 and the translation-stable space W=span{1,Y0,Y0^2+Y1^3} in characteristic zero. Its total-degree multiplicities occur at 0,1,3, and derivative-weight multiplicities at 0,2,4. No downward-Y0 monomial space can preserve both. Degree0 forces1; the single degree1 monomial must have weight2, hence beY0. A degree3 monomial of weight4 must beY0Y1^2, but downward closure then requires Y1^2, a prohibited degree2 monomial. Thus an unrestricted two-filtration monomial-preservation theorem is false. This does not by itself disprove positive-feasibility transfer with changing dimensions.

## A scoped finite transfer when maximum jet degree d<=D

Let W subset k[Y0,Y1] be translation-stable in Y0, with degree at most d<=D, and characteristic zero or greater than d. Let U=k[X]W intersect {wt<mA}, with derivative weights(1,D,D-1). Use total-jet-degree filtrations on U and the finite local target. Define

    G_q=dim U_{<=q}-dim U_{<=q-1},
    L=image of U in the local contact quotient,
    R_q=dim(L intersect target_{<=q})-dim(L intersect target_{<=q-1}).

These are TARGET-image filtration ranks, not increments obtained by restricting the INPUT to degree q. In the homogeneous case they coincide with the original degreewise ranks.

Claim: if sum_q(H-q+1)_+(G_q-nR_q)>0, a full-prefix downward-Y0 monomial source passes the same test, with no larger jet caps. The proved fourth-power declared-ledger lower bound therefore transfers to this restricted filtered class.

### Why these row counts define a sound graded test

Choose a total-degree-adapted basis of U and a coordinate projection injective on L, obtained by echelon pivots in decreasing target jet degree. There are R_q selected coordinate rows of degree q. Translation in Y0 preserves U, including the derivative-weight cutoff, so each translated local image equals L after scalar extension; the same rows detect every local condition. An entry from a degree-q source column to a degree-r target row after an affine received-word shift has challenge degree at most q-r. The graded kernel lemma therefore uses exactly the displayed G_q and R_q.

### Exact finite first degeneration

Choose a filtration-adapted basis f_i of W. In each associated total degree q, echelonize its highest parts in increasing Y1 exponent; let v_i be the pivot. All lower total-degree terms have derivative weight at most D(q-1), whereas the pivot has weight Dq-v_i>=q(D-1). Since q<=D,

    D(q-1)<=q(D-1)<=Dq-v_i.

Thus wt(f_i)=Dq-v_i: replacing f_i by its highest total-degree part does not change its weight. The highest parts have distinct echelon pivots. Their weighted initial forms, including any equal-weight lower-degree tails, are independent over k[X]: in a relation, take the largest jet degree among terms of maximum weight and its first pivot. Hence X^x f_i, 0<=x<mA-wt(f_i), form a basis of U.

The family t^q f_i(t^-1Y0,t^-1Y1) has the same pivot weights and the same X-prefix lengths at every parameter, including0. Its limit is exactly the full-prefix global source associated to gr(W), not a source with missing coefficient slots. Each G_q is preserved.

For t nonzero the local image is obtained from L by the diagonal target action scaling jet degree r by t^-r. The Grassmannian limit is gr(L), with degree-q dimension R_q. Every limiting source vector maps into this limiting image, so the local image of U(gr W) is a graded subspace of gr(L). Consequently its degree-q rank is at most R_q, separately for every q. This is stronger than a mere inequality of total ranks.

Apply HOMOGENEOUS_NONMONOMIAL_TRANSFER.md to gr(W) to obtain the desired monomial source, preserving G_q and decreasing ranks further. Translation stability and caps survive both limits. This proves the claim under the stated filtration-based row-test convention.

## Scope distinction

The d<=D restriction is a sufficient compatibility condition for the two filtrations, not a claim of optimality. The counterexample above has d=3>D=2. Without such compatibility, the first limiting full-prefix source may acquire extra coefficient slots and the rank argument does not control them. No transfer of a different, input-filtered definition of local R_q is asserted; confusing input and target filtrations would be a gap. Nonmonomial Eq64 and arbitrary global source spaces remain outside this note.
