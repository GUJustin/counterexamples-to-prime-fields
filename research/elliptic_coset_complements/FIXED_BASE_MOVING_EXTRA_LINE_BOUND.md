# A fixed base support permits at most d+1 labels with d moving extras

September 19, 2026. Exact linear-code lemma; no scan.

**Result.** In the elliptic window, each fixed pair of full fibers permits at most six qualifying projective labels, even when its five extra positions vary arbitrarily and overlap. Therefore changing the petals alone cannot rescue a construction using only order-n distinct base pairs. This does not exclude the order-\(\ell^3\) collection of all fiber pairs.

## 1. Small-radius line lemma

Let \(\mathcal C\subseteq\mathbb F^N\) be a linear code of minimum distance strictly greater than \(3d\), where \(d\ge1\). Let \(w_0,w_1\) be two received vectors, and consider their projective pencil
\[
w_{[a:b]}=a w_0+b w_1.
\]
Agreement and distance to a linear code are unchanged by nonzero scalar multiplication. Assume one projective point on this pencil has distance strictly greater than d from the code. Then
\[
\boxed{\#\{[a:b]:\operatorname{dist}(w_{[a:b]},\mathcal C)\le d\}\le d+1.}
\tag{1}
\]

If there are at most two qualifying points, (1) is immediate. Otherwise choose distinct qualifying points represented by independent parameter vectors \(\theta_0,\theta_1\), and witnesses \(c_0,c_1\in\mathcal C\), with residuals \(e_0,e_1\) of weight at most d. Extend \(\theta_i\mapsto c_i\) linearly to a map from the two-dimensional parameter space into \(\mathcal C\).

For any other qualifying parameter \(\theta=a\theta_0+b\theta_1\), choose its codeword witness \(c_\theta\) and residual \(e_\theta\). The codeword
\[
c_\theta-a c_0-b c_1=a e_0+b e_1-e_\theta
\]
has weight at most \(3d\), so is zero. Thus every qualifying residual equals the same linear map
\[
E(\theta)=a e_0+b e_1.
\]
Let Z be the union of the supports of \(e_0,e_1\), and put \(v=|Z|\le2d\). For every parameter, including the assumed far point, E is a residual from a codeword. Therefore \(v>d\); otherwise the entire pencil would have distance at most d.

At each coordinate in Z, E is a nonzero linear form in the two parameter coordinates. It vanishes at at most one projective point. Each qualifying point requires at least \(v-d\) zeros among these v coordinates. If b denotes the number of qualifying points, incidence counting gives
\[
b(v-d)\le v,\qquad
b\le\frac{v}{v-d}\le d+1.
\]
This proves (1). It also covers dependent received vectors or a punctured syndrome image of dimension at most one; no rank-two image is assumed. Alternatively, in the latter case a far image leaves at most its single zero-image projective point qualifying.

The proof counts labels rather than support descriptions. It permits zero residual coefficients, nonunique support padding, and arbitrary values at the nonzero error positions. No distinctness or disjointness assumption on the extra sets is used.

## 2. Puncturing a fixed base support

Let an original linear code be evaluated on a domain D of size n. Fix a base set \(B\subseteq D\) of size b, and puncture its coordinates. Suppose the punctured code has minimum distance greater than \(3d\).

A witness whose errors are contained in B and at most d additional coordinates is exactly a witness within distance d on the punctured domain. If an original pencil point has maximum agreement strictly less than \(n-b-d\), then its punctured distance is strictly greater than d: a punctured agreement of \(n-b-d\) would already give that many original agreements.

Consequently this one fixed base support can account for at most \(d+1\) distinct qualifying projective labels. If a family uses F possible base supports, its total number of distinct labels is at most
\[
\boxed{(d+1)F.}
\tag{2}
\]
Overcounting a label with several support representations only makes this bound weaker.

## 3. Exact elliptic specialization

For
\[
n=(\ell^2-1)/2,\qquad k=n-4\ell+1,
\]
take B to be the union of any two full fibers, so \(|B|=2\ell\). Puncturing these coordinates leaves an ordinary Reed–Solomon code of length \(n-2\ell\), dimension k, and minimum distance
\[
(n-2\ell)-k+1=2\ell.
\]
At \(d=5\) and \(\ell\ge23\), this exceeds 15. A far endpoint at the tested threshold
\[
T=n-2\ell-5
\]
therefore implies at most six labels for any fixed base pair, irrespective of the moving quintic locators and their overlaps.

The 3/7 specialization uses only
\[
F=(\ell+1)(\ell-1)/2=n
\]
indexed base banks, so (2) gives \(6n\) without using its special petal geometry. Its disjoint petals sharpen the constant to \(2n\) in [TORSION_QUINTIC_SUNFLOWER_BOUND.md](TORSION_QUINTIC_SUNFLOWER_BOUND.md).

The full elliptic collection instead has
\[
F=(\ell+1)\binom{(\ell-1)/2}{2}=\Theta(\ell^3).
\]
Bound (2) permits that many labels. Thus the necessary change within this support model is to use more than order-n base pairs; adding only overlapping petals to a one-quotient-parameter family does not suffice. Two independent quotient tags, coupled to a genuinely shared source identity, remain a possible target. The lemma does not construct such an identity or rule it out.

## Scope

The strict condition is the punctured minimum distance \(>3d\), and the far-point premise is essential. A pencil entirely within a radius-d ball pattern can have all projective points qualifying. The bound does not apply after increasing d past this regime, changing the base sizes or code parameters without rechecking the distance, or replacing the stated support model by a different one.
