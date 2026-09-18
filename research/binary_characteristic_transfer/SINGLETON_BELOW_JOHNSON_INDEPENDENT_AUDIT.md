# Stronger exact singleton classification: independent audit

September 18, 2026. **PASS** for the root agent's coefficient-elimination strengthening, now incorporated in `large_characteristic_singleton_line.tex`.

The exact Gaussian classification holds for **every threshold strictly greater than p²**, including the advertised below-Johnson threshold A0=p³-p². This supersedes the threshold limitation in the original finite-difference audit.

For any candidate with more than p² agreements, put R=X(f+zg-h). Projection onto the theta² coordinate yields a polynomial of degree at most p² vanishing on more than p² points, hence z+theta²=b+theta a and h=h0+theta h1. Its B and theta components are

    T=Xp4+bXp2-Xh0,
    L=Xp3+aXp2-Xh1.

Here Xpj denotes X^(p^j). Both vanish on the matching nonzero coordinates and R's root set; coefficient projection is valid at all roots of R because those coordinates belong to B. The polynomial

    T-L^p+a^p L=(b+a^(p+1))Xp2+(Xh1)^p-a^p Xh1-Xh0

has degree at most p² and the same more-than-p² roots, so is identically zero. Its coefficients at X^(jp), 2≤j<p, force all middle coefficients of Xh1 to vanish. The identity similarly makes Xh0 a combination of X^p and X. Thus R and L are linearized. Their common roots in B form a subspace with more than p² points, hence at least p³. Monicity and degree p³ of L force a three-dimensional locator with nonzero linear coefficient. The previously audited coefficient recovery and label injectivity then apply unchanged.

Therefore exactly M=[5 choose 2]_p nonzero shifted labels have any candidate with more than p² matches. Each has exactly one such candidate, with precisely p³-1 matches. Every other label has agreement at most p². At every integer p²<T≤p³-1, all qualifying lists are singleton, and the full-agreement-set exceptional count is exactly M because CA=p²-1<T.

## Why the strict inequality matters

One cannot infer a three-dimensional squarefree locator from at least p² roots. For any two-plane U with locator J=Xp2+uXp+vX, the polynomial L=J^p is monic of degree p³ with zero X coefficient and has p² distinct roots. Taking a=u^p,c=v^p, the same construction gives a candidate with zero constant term agreeing on all U, including zero. Its shifted label is c^p-a^(p+1)+theta a-theta².

Thus the quotient-by-X argument can force linearization already at p² matches, but cannot exclude this inseparable two-plane branch. We do not assert that all other labels have agreement at most CA, or that singleton classification extends to T=p². Whether some of these secondary labels coincide with the three-plane labels is unnecessary for the stated theorem.

## Admission update

The new proof is shorter than the finite-difference proof and strengthens the below-Johnson conclusion materially: a superlinear exact bad-label population has singleton lists at the same advertised threshold where the explicit DKT comparison applies. This remains a single received-line result at vanishing rate and shrinking absolute margin. It does not bound the maximum list size over all received words or resolve prime-ambient/fixed-rate tightness.
