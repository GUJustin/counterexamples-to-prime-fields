# Independent audit of the partial-prefix reduction

The mathematical reduction in `PARTIAL_PREFIX_REDUCTION.md` passes. This audit does not repeat the already independent capacity/conservation replay of its large flow certificate.

## Challenge layers form a safe relaxation

A source monomial X^xY^iR^jZ^z has layer k=i+j+z. The zero-received-word substitution Y=tR+t²E preserves total R,E,Z degree, hence k. Within a layer, different jet degrees q have different Z exponents, so these target blocks remain independent. Dimension and local rank add over the layers.

Replacing Y by Z lowers i while increasing z and preserves k. Thus every actual translation-stable layer has exactly the stated within-layer Y-downward implication. Replacing Y by a constant instead links different layers. Omitting that implication only enlarges the feasible class. Omitting the extra layer constraint q≤k enlarges it further. Therefore the optimized single-layer graph is a SUPERSET of every layer of every actual allowed monomial source. A zero optimum is decisive in the negative direction; a positive relaxed solution would need closure restored before being a construction.

## Tail completion is closure-safe

If a jet pair has X-prefix height h≥m, its newly completed columns all have x≥h≥m, hence extraction grade ell=x+i≥m. They are in every one-point contact kernel. Its lower-Y neighbor already has height at least h≥m, and completing it adds only equally harmless columns. Its maximum allowed height is larger by w. Simultaneous completion therefore preserves all X/Y closure relations and the weighted-degree cap.

The last compressed indicator, at x=m-1, has benefit H-m+1 and means height H. Without that indicator the maximal allowed height is m-1. These are exactly the completed heights {0,...,m-1,H}. The indicator itself can be rank-bearing when i=0; the rank graph includes it explicitly. Only the extra columns x≥m represented by its bulk benefit are automatically free. This distinction is handled correctly in the stated graph.

## Rank formula

For fixed (q,ell), each present monomial is uniquely indexed by i with x=ell-i and j=q-i. Its truncated expansion has Pascal entries binomial(i,a), whose initial rows have Vandermonde rank min(m-ell,number of selected indices) in characteristic>Q. Blocks are disjoint because ell equals t-degree minus E-degree. Therefore the graph uses the exact zero-point rank. Translation stability identifies ranks at the other received coordinates.

These facts validate the zero-optimum conclusion at m115 for the stated partial-X/partial-Z monomial class, with no claim about arbitrary nonmonomial spaces.

## Analytic large-m extension without further graphs

There is a simple uniform tail bound even for arbitrary X-downward jet columns, without requiring Y-downward closure. Let k_q be the number of ambient jet pairs of degree q; for Q159,Rcap35 it is at most36. For ell≤m-k_q the contact depth m-ell is at least k_q, so the Pascal map has full column rank. For a selected X-prefix of height h at (i,j), at least

    min(h,M_ij),  M_ij=m-k_q-i+1,

columns lie in these full-rank blocks, provided M_ij≥0. Ignoring all remaining nonnegative rank contributions gives

    dimension-n*rank <=sum_(i,j) [h_ij-n*min(h_ij,M_ij)].

For 0≤h≤H_ij=mA-wi-(w-1)j, the bracket is a decreasing linear function until M_ij and increasing afterwards. Its maximum is at an endpoint, bounded by max(0,H_ij-nM_ij). Now

    H_ij-nM_ij
      =-(n-A)m+(n-w)i-(w-1)j+n(k_q-1)
      <=-80869m+131073*159+262144*35
      =-80869m+30015647.

For m≥372 this is strictly negative (at372 it is -67621), and every M_ij is positive. Hence no nonempty X-downward layer has positive dimension margin for any m≥372. Summing layers extends this to arbitrary finite challenge support. The bound uses D=mA; smaller D only reduces H in this direct inequality.

Thus the remaining multiplicities for a possible partial-prefix improvement are finite, m1 through371, with m115 already excluded by the exact graph. This is a reduction of scope, not authorization or a recommendation to run371 large graphs. No computations beyond integer arithmetic are needed for the large-m exclusion.
