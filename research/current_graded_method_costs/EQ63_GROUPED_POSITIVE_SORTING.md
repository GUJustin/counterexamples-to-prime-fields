# Positive Eq63 feasibility survives deletion and grouped height sorting

This is not monotonicity of the decreasing rearrangement of a fixed multiset of heights. The counterexamples in EQ63_ADJACENT_SWAP_OBSTRUCTION.md remain valid. The allowed operation here can delete an entire excess block or truncate that block before moving it.

## Theorem

Let S be a finite Y0-downward jet support, with all derivative-weighted coefficient prefixes x+Du+(D-1)v<mA, D>=2. Assume the exact saturated local rank formula is valid (in particular, the characteristic guard of the support audit suffices). If the Eq63 affine-line margin is positive at H, there is a coordinatewise monomial order ideal passing Eq63 at the SAME H, with no larger total-degree or derivative cap. Consequently the fourth-power declared regular-family ledger lower bound extends to every such Y0-downward support.

Before the saturated argument, discard jet degrees q>H, which have zero contribution. Also discard the final diagonals Lq=mA-(D-1)q<m: their unweighted surplus is nonpositive by the finite half-rank lemma, so their Eq63 contributions are nonpositive. These deletions preserve Y0-downward closure. Every remaining degree satisfies q<=H and is saturated. Every later move either deletes monomials or lowers their total degree, preserving these conditions.

Write S as columns of heights h_v, including empty intermediate columns, over v=0,...,V. For a subset B serving as an unchanged baseline define

    C(q,ell)=#{(u,v) in B:u+v=q, u<=ell},
    f_ell(z)=min(z,m-ell), 0<=ell<m.

The saturated rank on degree q is sum_ell f_ell(C(q,ell)).

## One step with a previously fixed sorted suffix

Suppose columns j+1,...,V form a decreasing suffix, all of whose heights are at most every height in 0,...,j. This holds initially for the empty suffix. Choose i<=j with minimum height c in 0,...,j. If i=j, fix that column and continue.

Otherwise let E be the excess above height c in columns i+1,...,j. The baseline B=S minus E retains all earlier columns 0,...,i-1, height c in columns i,...,j, and the fixed suffix. Define

    X(q,ell)=#{(u,v) in E:u+v=q, u<=ell},
    d_q=sum_ell [f_ell(C(q,ell)+X(q,ell))-f_ell(C(q,ell))],
    g_q=(1/n)sum_{(u,v) in E,u+v=q}[mA-Du-(D-1)v].

Then the normalized whole margin decomposes EXACTLY as

    M(S)=M(B)+sum_q (H-q+1)(g_q-d_q).        (1)

All excess degrees are active. The d_q are marginal ranks relative to B, not ranks of E alone.

### Case 1: nonpositive weighted excess

If the excess sum in (1) is nonpositive, delete E. This does not decrease the margin, and all columns i,...,j now have height c. In particular column j can be fixed as the new rightmost minimum. Every remaining prefix height is still at least c, and the previously fixed suffix heights are at most c.

### Case 2: positive weighted excess

Put P_k=sum_{q<=k}(g_q-d_q), and choose k in 0,...,H maximizing P_k. The weighted excess margin is sum_{k=0}^H P_k>0, so its maximum is positive. Delete from E all monomials above total degree k. The new excess prefix sums agree through k and equal P_k thereafter, so its weighted margin does not decrease. Its total unweighted marginal surplus is now P_k>0.

This trimming preserves each excess column as an initial interval above c: its new height is c or min(h_v,k-v+1), whichever is larger. Thus every prefix column remains of height at least c. Baseline B is unchanged, and rank increments at retained degrees are unchanged because the exact local rank decomposes by total degree.

Move the trimmed excess one column left, (u,v)->(u,v-1). The baseline stays fixed. The new column j has height c; the earlier prefix heights remain at least c, so this again fixes one more column of the decreasing suffix.

## The rank transport inequality

For every ell, the baseline consists of an order ideal of height at most c (all columns 0,...,j of height c plus the already decreasing suffix), together with excess intervals in earlier columns v<i. Its active diagonal count is nonincreasing at every q>=i+c.

Indeed the height-c order ideal, after intersection with u<=ell, has nonincreasing diagonal lengths beyond its first incomplete diagonal, which occurs no later than degree c. Each earlier excess column starts at degree v+c<=i+c-1, and hence its interval indicator cannot increase between q and q+1 for q>=i+c. Summing proves

    C(q,ell)>=C(q+1,ell) whenever shifted excess occurs at q.   (2)

The trimmed excess begins at u>=c, v>=i+1; after shifting it has q>=i+c. Its new active count at q is exactly its old active count at q+1. Since f_ell is concave, (2) gives

    f_ell(C(q,ell)+X(q+1,ell))-f_ell(C(q,ell))
       <=f_ell(C(q+1,ell)+X(q+1,ell))-f_ell(C(q+1,ell)).

Consequently its new marginal rank d'_q satisfies

    d'_q<=d_{q+1}.                             (3)

No claim comparing ordinary first moments by themselves is required.

## The complete margin increases

A moved coefficient prefix grows by D-1, and its challenge weight grows from w_q=H-q+1 to w_q+1. By (3), the marginal weighted rank after moving is at most sum_q(w_q+1)d_q. Therefore

    M(after shift)-M(before shift)
      >=sum_q(g_q-d_q)
        +(D-1)/n * sum_{(u,v) in trimmed E}(H-u-v+2)
      >0.

The first term is the positive P_k arranged by the trimming step. This accounts for the ENTIRE source-minus-rank expression.

## Termination and scope

Each step fixes column j and reduces j by one. Trimming/deletion never lowers a prefix column below the current minimum c, so the suffix invariant survives; after at most V+1 steps all heights are decreasing. The support is then a coordinatewise order ideal with positive margin. Total degree, derivative cap and coefficient positivity have not increased; saturation and the characteristic guard persist. Apply ORDER_IDEAL_FOURTH_POWER.md to conclude the lower bounds at the original H and original declared caps.

This proves a positive-feasibility reduction, not preservation of the original support, its dimension, or its sorted multiset. It uses the derivative-weighted full-prefix source and the exact rank formula. It does not address arbitrary nonmonomial sources, equal-weight cutoffs, global matrix dependencies, or actual list-size lower bounds.
