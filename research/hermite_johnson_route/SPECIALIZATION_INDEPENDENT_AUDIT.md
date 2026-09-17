# Independent audit and consolidated polynomial-root constants

The proof in `SPECIALIZATION.md` passes the checks below. Its ordinary constant centeralpha is preferable to the earlier transcendental-center sketch: no auxiliary imperfect constant field is introduced.

## Checked points

1. Factoring in the polynomial UFD, removingY-independent content, and retaining each positive-Y factor once does not increase any separate variable degree. Outside at mostH roots of a chosen nonzeroX-coefficient of the removed content, the original and reduced polynomial-root identities are equivalent in the integral domaink[X]. This remains true under specialization; it does not require factorization to specialize faithfully.

2. After squarefree reduction, characteristiczero orp>B makes the reduced polynomial separable inY overk(X,z). One ordinaryalpha in the algebraically closed constant field can avoid the finitely many roots of a nonzeroX-coefficient from both the leading coefficient and resultant. Their evaluations remain nonzero polynomials inz. The conservative exceptional-label count is

 E0=(2B+1)H,

includingH for content,H for the leading coefficient, and(2B−1)H for the resultant. Some of these sets overlap; the stated sum is safe.

3. WithC=B+H, the formal implicit coefficients satisfya_j=N_j/A^(2j−1), degN_j≤(2j−1)C. In a remaining recurrence term witht-degreea andv-degreeb, indices sum toj−a. Multiplying numerator bounds and the polynomial coefficient produces degree at mosteC, wheree=2(j−a)−b+1 is its denominator exponent after division byA. Except for the isolated linear termAa_j, every contributing term hase≤2j−1. Clearing to the common denominator preserves the claimed degree bound. Hasse expansion uses binomial coefficients in the field but divides by no factorial or integer. This argument remains valid forj≥p.

4. On any nonpolynomial initial component, somea_j withD<j≤N=T+BD is nonzero. Otherwise theD-truncation yields a polynomial substitution of degree≤N vanishing to orderN+1, so the substitution is zero and formal uniqueness forces a polynomial branch. IfN≤D, all components are polynomial and this exceptional contribution is zero.

5. Choose one suchj on each nonpolynomial component. Its numerator does not vanish identically there. Bézout bounds all its regular special polynomial-root points. At a regular initial point(z,u), implicit uniqueness gives at most one specialized polynomial root; consequently the count is for solution pairs, not an uncontrolled auxiliary fiber. A safe bound is

 S0=max(0,2(T+BD)−1)(B+H)^2,

orS0=0 whenT+BD≤D.

6. Every regular point of a retained polynomial component specializes to a genuine degree≤D root. Recursion denominators are powers ofA, andA=0 is already exceptional. Taylor-to-monomial coefficients are related by an invertible triangular linear transformation in every characteristic; no factorial inverse is required.

## Stronger retained-curve bound from the generic audit

The degree bound(S2) inSPECIALIZATION.md is valid but not needed in its weakerO(D) form. On a retained component, the Taylor coefficients are rational inz,u, whileu=P(alpha) is a linear combination of the monomial coefficients. Hence its function field is exactly the polynomial root's coefficient fieldk(z,c_0,...,c_D).

Underp>B, a short separability proof suffices. ChooseD+1 ordinary constantsx_i where the reduced resultantRes_Y(R,R_Y)(x_i,z) remains nonzero. EachP(x_i) is separable algebraic overk(z); Vandermonde interpolation shows every coefficient lies in the separable closure. Distinct embeddings of the coefficient field give distinct polynomial roots ofR, so its degreed≤B and the sum of these degrees over distinct generic polynomial branches is≤B. This avoids the optionalp-rank argument inGENERIC_BRANCH.md.

The Gauss-valuation proof there gives common coefficient poles of degree≤dH and projective curve degree≤d(H+1), with coordinates(1,z,c_0,...,c_D). Summing yields the sharper total retained-curve degree

 Delta_total≤B(H+1).

The root family coordinates generate its function field, so the projective parametrization is birational; no hidden covering degree is omitted.

## Consolidated full-support root-incidence lemma

Fix distinctx_1,...,x_n, affine received valuesf_i+zg_i, a degree boundD, and an agreement thresholdA>D. Call(z,P) bad ifP has at leastA full value agreements but no degree≤D polynomialG matchesg on all those agreement coordinates. Among rootsQ(X,z,P(X))=0 withdegP≤D, the number of labels possessing a bad pair is at most

 E0+S0+B(H+1)·(n−D)/(A−D)+Bn.                 (R)

Explanation: nonaffine branches have at mostD persistent agreement hyperplanes. If a branch hasq≤D persistent coordinates, each bad point needs at leastA−q nonpersistent incidences and there aren−q available hyperplanes. Its contribution is≤degree(branch)·(n−q)/(A−q), at mostdegree(branch)·(n−D)/(A−D). Every affine branchP=F+zG contributes at mostn bad labels: a bad full support must contain an agreement outside the persistent set, and each such coordinate contributes at most one label. There are at mostB affine branches. Exceptional labels contributeE0 and isolated pairs at mostS0.

The same upper bound applies to ordinary-CA exception labels when no threshold-A affine pencil witness exists, but(R) is stated directly for bad full supports and does not assume that every affine branch already witnesses threshold-A correlated agreement.

For the root lemma alone, characteristiczero orp>B suffices. Any stronger condition such asp>max(D,B) comes from the separate differential-equation/regular-incidence application, not the implicit recursion. Interpolation existence and that application remain separate audited hypotheses. No Lean compilation or automated proof certification is claimed.
