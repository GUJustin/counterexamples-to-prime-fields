# Quadratic Frobenius core: complete quadratic classification

**Update:** the structured-padding question posed below is now resolved by `scaled_fiber_padding.tex`, with independent audit in `TWO_BLOCK_INDEPENDENT_AUDIT.md`. The original seed/target analysis is retained below as provenance.

Let p be odd, B=F_(p²), and E any finite field containing F_(p⁴). Choose v with v² a nonsquare of B. Then v is outside B and

    D0={x in E*: x² in B*}=B* disjoint-union vB*,
    |D0|=2(p²−1).

Indeed B* consists of squares in F_(p⁴); the two B-lines above exhaust the two square classes of B*. Set f(x)=x^(2p). The zero direction on this core is only a proposed construction component, not a finished proximity line.

## The exact high-agreement bank

For a,b in B satisfying

    a^(p+1)=1,  b^p=−a^p b,

put Q_(a,b)(X)=aX²+b. The equation f(x)=Q_(a,b)(x) descends under y=x² to y^p−ay=b. The F_p-linear map y→y^p−ay has one-dimensional kernel and image characterized by the displayed condition on b. Every nonzero y has exactly two preimages in D0.

Thus b≠0 gives exactly 2p matches; there are (p+1)(p−1)=p²−1 such distinct quadratics. The p+1 members with b=0 have exactly 2p−2 matches. Other B-coefficient even quadratics have at most two matches: if a does not have norm one, the linearized map is invertible, and if b fails the image condition there are no solutions.

## Every other quadratic has at most max(p,4) matches

Write Q=aX²+cX+b with coefficients anywhere in E. On either component x=u t, t∈B*, u∈{1,v}, the equation becomes

    t^(2p)=A t²+C t+B0,
    (A,C,B0)=(a u^(2−2p), c u^(1−2p), b u^(−2p)).

If these three coefficients are not all in B, apply a B-linear functional E→B which vanishes on B but not on one coefficient. A nonzero polynomial of degree at most two then vanishes at every matching t. This component contributes at most two matches.

Suppose instead all three coefficients are in B. Because u² and u^(2p) lie in B*, this implies a,b∈B and c u∈B. If c=0, this is the already classified even case on both components. If c≠0, the other component has exactly zero matches: its quadratic and constant terms and the received value are in B, while its nonzero linear term lies in a different one-dimensional B-space. Therefore it suffices to count on this one component with C≠0.

Frobenius and substitution give

    C^p t^p=H(t),
    H(t)=(1−A^(p+1))t²−A^p C t−A^p B0−B0^p.

Every solution is a root of

    H(t)²−C^(2p)(A t²+C t+B0).

If this polynomial is nonzero, there are at most four roots. If it is identically zero, H has degree at most one (its quadratic leading coefficient would otherwise have nonzero square), and the nonzero polynomial C^p t^p−H(t) has at most p roots. This also explains the square-of-a-linear-polynomial exceptional case, without needing to assume or classify its parameters.

If neither component was coefficientwise B-valued, the total is at most four. Combining cases proves the claimed bound over the entire coefficient field E, not merely over B.

For p≥5, outside the full canonical even family all quadratics have at most p matches. In particular the complete nearest list has exactly p²−1 words, each with agreement 2p. The p+1 b=0 words must not be omitted from future nonbank bounds: relative to only the maximal bank, the second agreement level is 2p−2, not p.

## Small exact gate

`check.py` independently enumerates all p^6 quadratics over B for p=3 and p=5, using tuple arithmetic with a nonsquare generator. It counts even matches through y=x² and non-even matches directly on B* (the opposite component contributes zero). It verifies the bank counts and all bounds. The receipts in `check.json` show maximal lists of 8/24 words at 6/10 matches, with 4/6 secondary even words at 4/8 matches. The maximal non-even agreements are 3/5. The extension-coefficient cases are proved above; they were not exhaustively enumerated by this gate.

## Scope and next constraint

This is a genuine rich core with p²−1 maximal quadratic witnesses on 2(p²−1) points, in characteristic p greater than the code dimension three. Its ambient field contains F_(p⁴), not the prime field. Its rate tends to zero. No fresh-padding construction, source-separation claim, or large affine-label population is proved here. Any padding argument must control the secondary b=0 bank as well as the ≤p noncanonical words. The desired many fresh matches per witness/label remains a separate task.
