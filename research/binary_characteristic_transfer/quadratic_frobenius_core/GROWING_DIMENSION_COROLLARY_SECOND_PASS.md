# Growing-dimension corollary: second pass on the integrated text

September 18, 2026. **PASS as written.** Audited the corollary “Growing dimension, with weaker placement” in density_quarter_puncturing.tex, then checked consistency with GROWING_DEGREE_FROBENIUS_MATCH_BOUND.md and its earlier independent audit. No manuscript edits.

For a polynomial of actual degree \(3\le d\le p\), the normalized leading coefficient on \(v^\epsilon B_0\) is
\[
h_dv^{\epsilon(d-2p)},
\]
and on \(s_1v^\delta B_0\) it is
\[
h_ds_1^{d-2}v^{\delta(d-2p)}.
\]
Their ratio is exactly the exponent expression in the corollary. Modulo \(B_0^*\), the class of \(s_1\) generates a group of order \(Q=p^2+1\), and \(v\) has order two. The possible exponents are \(d-2\) or, only for odd \(d\), \(d-2+Q/2\). Since \(1\le d-2\le p-2<Q/2\), no exponent vanishes. The line parameter affects only the constant coefficient and cannot invalidate this leading-coefficient test.

Thus at most one block has any component whose normalized polynomial is coefficientwise \(B_0\)-valued. On that entire block the original matching equation is a nonzero degree-\(2p\) polynomial, including its constant received-word offset. It gives at most \(2p\) matches across both components. Each component of the other block contributes at most \(d\) matches by a nonzero coefficient projection. If neither block is valued, \(4d\le2p+2d\). Arbitrary puncturing of the second block preserves the result.

Consequently \(D=\lfloor p/20\rfloor\), \(k=D+1\) gives the claimed upper bound \(2p+2D<T\) for every new witness. The displayed quadratic inequality in \(p\) correctly proves the strict comparison, with the integer square-root threshold. Hence the full threshold-list profile is unchanged.

The original two endpoints are outside all canonical parameter planes. Their old quadratic agreements are at most \(2p\), while the simultaneous old witness still attains \(2p\) on the core. Combining old and new witnesses proves exactly the stated interval
\[
2p\le \operatorname{agr}(r),\operatorname{agr}(s),
       \operatorname{CA}(r,s)\le2p+2D.
\]
Equality at the lower endpoint is not proved for this larger degree range and is correctly not claimed.

At \(p=257\), the exact values are
\[
k=13,\quad n=165122,\quad T=574,\quad
A_{\max}=538,\quad
\frac{T-A_{\max}}{T-k}=\frac{36}{561}=\frac{12}{187}.
\]
The limiting lower bound exceeds \(0.0622=311/5000\): after rearranging and squaring positive quantities, this is equivalent to
\[
5\cdot93780^2-209689^2=3965279>0.
\]

Finally \(k\ge4\) gives
\[
n a_1(k/n)>\sqrt{kn/2}\ge\sqrt{2n}>T.
\]
So this promotion loses the original first-order placement, exactly as the corollary states. It raises message dimension to \(\Theta(p)\), while rate and fractional loss still vanish as \(\Theta(p^{-1})\). The absence of neutral padding is essential: this audit applies to the quarter-density domain, not the older construction with neutral values \(f=X^3\).
