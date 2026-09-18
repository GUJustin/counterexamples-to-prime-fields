# Independent audit: secondary labels and exact three-level spectrum

September 18, 2026. **PASS** for `SECONDARY_LEVEL_AND_TRACE_OBSTRUCTION.md`, for every prime p≥5. In particular this covers the manuscript's p≥53 range. No finite-field census is needed.

## Exhaustive classification already at p² agreements

First project the unmultiplied agreement polynomial f+zg-h onto the theta² coefficient. Its degree is at most p²-1, and it vanishes on at least p² distinct coordinates, including zero if matched. Thus z+theta² lies in B+Btheta and h=h0+theta h1.

Set T=X^(p⁴)+bX^(p²)-Xh0 and L=X^(p³)+aX^(p²)-Xh1. Each of T/X and L/X vanishes at every matched coordinate. Consequently

    (T-L^p+a^pL)/X = T/X-X^(p-1)(L/X)^p+a^p L/X

vanishes at every match, including zero. Its degree is at most p²-1, so it is zero. Coefficients at exponents p(j+1)-1 for 1≤j≤p-2 force the middle coefficients of h1 to vanish; the rest force those of h0 to vanish. This proves the asserted linearized form and label formula without treating zero as an extra or lost root.

For v≠0, the constant term of h is (a^p-theta)v≠0, so agreement count is |ker_B L|-1. A count at least p² forces the three-plane locator and p³-1 agreements. For v=0, zero matches, L=J^p with monic linearized degree-p² J, and the count is |ker_B J|. At least p² matches force J to be the squarefree locator of a two-plane. These exhaust all cases.

Each two-plane determines one secondary label. Its theta component determines a and its B component determines c under injective Frobenius; hence the two-plane locator and candidate are uniquely determined. The secondary population is exactly the Gaussian number M, before checking disjointness from the primary population.

## Operator trace and disjointness

If a label belongs to both populations, its fixed a,c give L_W=J_U^p+vX with v≠0. Then U intersect W is zero. Since their dimensions are two and three, they sum to the whole five-dimensional space B. The map Q(x)=-J_U(x)^p/v is zero on U and identity on W. It is therefore a projection with operator trace 3 in F_p.

Independently, for an F_p-linear map Q(x)=sum_(i=0)^4 a_i x^(p^i), extend scalars to an algebraic closure. The five coordinates are the embeddings sigma_j(x)=x^(p^j). In those coordinates,

    sigma_j(Q(x))=sum_i sigma_j(a_i) sigma_(j+i mod 5)(x).

Thus the diagonal entries are precisely sigma_j(a0). Its matrix trace is Tr_(B/Fp)(a0). This argument also applies in characteristic five: the field extension is separable, and the cyclic shift still has no fixed coordinate. For the purported projection, a0=0, so its trace is zero. Since 3≠0 for p≥5, this is impossible.

This proves primary/secondary disjointness without genericity assumptions, nonvanishing denominators beyond v≠0, or a numerical test. The trace argument alone leaves characteristic three open, which is outside the stated range.

## Complete quantifiers

On the entire affine challenge field F_(p^15), after the theta² source shift:

* M labels have maximum agreement p³-1, with exactly one witness at any threshold at least p²;
* M disjoint labels have maximum agreement p², with exactly one witness at that threshold;
* all other labels have maximum agreement C=p²-1.

For the last assertion, the upper bound follows from exhaustive classification; the lower bound follows from the simultaneous degree-<p source explanations on U minus zero, for any two-plane U, for every challenge.

All 2M high labels have theta² coefficient -1 and are nonzero. Since CA=C, the exact bad-label count is 2M at threshold p² and M at every integer p²<T≤p³-1. At thresholds above p³-1 there are no qualifying labels. No assertion about list cardinality at C is warranted. This is an affine challenge-line result, not a projective-infinity challenge or a uniform list bound over all received words.

The manuscript may therefore replace its conservative outside-primary bound ≤p² by this exact spectrum. The field, vanishing rate, and vanishing absolute first-order margin remain unchanged.
