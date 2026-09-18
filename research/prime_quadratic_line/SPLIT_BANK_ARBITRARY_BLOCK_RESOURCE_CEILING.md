# Split-bank resource ceiling with unequal sides and arbitrary block sizes

2026-09-18. Independent algebra audit of `square_linear_block_bank.tex`. No manuscript edits.

## Standard architecture and exact assumptions

Partition the evaluation domain into Z and disjoint nonempty fresh blocks E_j. All coordinates are nonzero. On Z, set g=0 and allow arbitrary f. On E_j set

    f=0, g=X²/b_j,

where the b_j are distinct nonzero scalars. Let n0=|Z|, n1=Σ_j D_j with D_j=|E_j|, and n=n0+n1. Assume the ordinary common agreement of (f,g), for degree≤2 explanations, is at most A. Test agreement A+d with d>0.

We first count only nonzero parameters with a qualifying pure quadratic aX². To obtain a bound on ALL exceptional parameters, additionally require that every threshold witness at a nonzero parameter is pure. This latter classification holds in the proved square-linear lemma, but is not automatic for arbitrary r,s or tiny blocks. The λ=0 parameter and the projective point at infinity contribute at most two further labels regardless of their lists.

## Strong resource inequality, independent of the named bank

For every nonzero scalar a define

    c_a = |{x∈Z : f(x)=a x²}|.

Each x∈Z contributes to at most one c_a, hence Σ_a c_a≤n0. The explaining pair (aX²,0) shows c_a≤A. The pair (0,X²/b_j) shows D_j≤A. These are consequences of ordinary CA; no individual-source assumption is needed.

At λ≠0 the pure word aX² agrees on E_j exactly when λ=a b_j. Distinct b_j imply that it agrees on at most one fresh block. Its total agreement is therefore either c_a or exactly c_a+D_j. A qualifying pair (a,j) must satisfy

    c_a+D_j≥A+d,  0≤c_a,D_j≤A.

If d>A there are no such pairs. Otherwise both resources are at least d, and

    c_a D_j≥Ad.

For example, write c_a=A−u with 0≤u≤A−d. Then D_j≥d+u and
(A−u)(d+u)=Ad+u(A−d−u)≥Ad.

Let P be the number of qualifying pairs. Summing their products and then enlarging to all pairs gives

    Ad·P ≤ Σ_qualifying c_a D_j
           ≤ (Σ_a c_a)(Σ_j D_j)
           ≤ n0 n1.

Every pure-mediated label has at least one qualifying pair; multiple witnesses or repeated products only reduce the number of labels. Consequently

    B_pure ≤ floor(n0 n1/(Ad)) ≤ floor(n²/(4Ad)).

This applies even to partial cores, deleted pair intersections, unequal bank sizes, arbitrary neutral values on Z, and pure witnesses outside the original bank. It does not require product injectivity or a two-owner core. Under the stated non-pure exclusion, the full projective exceptional population is at most this bound plus2.

If A≥a√n and d≥b√n for fixed a,b>0, then

    B_pure≤n/(4ab).

Thus arbitrary block sizes cannot produce superlinear counts in the existing classified split-bank architecture. The product resource estimate is sharp as a scalar ledger: all positive c_a=A and all D_j=d attain c_aD_j=Ad and the qualifying inequality with equality. This does not assert that every ledger equality admits the required polynomial incidence realization.

## Literal complete r-by-s core

With r monomials a_iX² and s nonzero constants b_j, if all pair ratios have two distinct nonzero square roots and all 2rs core coordinates are distinct, then n0≥2rs. Every named monomial has 2s core matches and every named constant has2r. The canonical product population is at most rs≤n/2, regardless of fresh-block sizes. Product collisions only lower it. This immediate bound is already enough for the literal full-core extension, but does not by itself cover core thinning; the resource inequality above does.

A direct sufficient non-pure exclusion for the complete core plus cubic neutral padding is also explicit. A polynomial outside the r+s bank has at most r+s core matches by counting its at most two intersections with each owner, with each core point counted twice. A bank constant has2r core matches. A non-pure polynomial has at most2s matches on the fresh blocks for λ≠0 and at most3 neutral matches (bank constants have zero neutral matches if excluded when padding). Therefore it is enough that

    A+d > max(r+3s+3, 2r+2s).

The original symmetric lemma uses the stronger D>4t+3, so this condition is satisfied there. Unequal sides must recheck this classification rather than inherit it from the symmetric case.

## What would actually escape this ceiling

The proof uses two separate mechanisms: common agreement caps each zero-direction resource and each whole fresh block by A; and a nonzero label/pure witness can receive only ONE fresh block. Superlinear labels require abandoning at least one relevant premise, for example introducing genuinely non-pure threshold witnesses or changing fresh words so a witness can accumulate support across many blocks at the same label. Simply adding more monomials/constants, thinning the core, or varying the D_j does not evade it.

This is not an O(n) theorem for arbitrary quadratic received lines. If non-pure witnesses are no longer excluded, their labels are not counted here. Nor does the fixed-bank budget alone establish the one-block property or common-core richness. Those are separate structural hypotheses.
