# Independent audit of the general monic-cubic pencil list bound

**Later strengthening:** the final list theorem uses `p>max(3,2D)`; see `TWO_D_RADICAL_BUDGET.md`, its independent audit, and `general_cubic_list.tex`. The stronger characteristic assumptions in this earlier argument remain valid sufficient conditions.

**PASS.** The zero-dimensional and positive-dimensional critical-locus arguments combine into a uniform ordinary-list bound for the stated monic-cubic first-integral family.

Let k have characteristic zero or p>max(3,6D), D>=1, and

`F(X,u)=u³+a2(X)u²+a1(X)u+a0(X)`,

where deg a2<=D, deg a1<=2D, deg a0<=3D. Let H in k[X] be nonzero. On any n>D distinct coordinates, let L distinct polynomial sections P of degree at most D satisfy F(X,P)=c_P H for constants c_P and agree with an arbitrary received word in at least A>=D+eta*n coordinates, eta>0. Then

`L <= 9+(3+108D/n)/eta`.

The constant is conservative. This concerns one specified first-integral pencil, not every cubic differential equation, all Reed–Solomon lists, or received-line bad-label counts.

## Positive-dimensional critical locus

The argument in `CRITICAL_COMPONENT_CONSTANT_VALUE.md` passes independently. One may extend the constant field to its algebraic closure. The nonzero leading coefficient3 of F_u excludes a vertical common component. A critical root r generates a separable extension L0/k(X) of degree d<=2. For v=F(X,r)/H the common-component equation gives v'=0.

If a nonzero-label section exists, N=deg H<=3D. The critical root is integral at finite places and has pole order at most De above infinity. Hence F(X,r) has poles only at infinity, of order at most3De. Dividing by H gives the valid total pole bound

`h_(L0)(v) <= dN+d(3D−N)=3dD<=6D`.

In characteristic p, the nonzero extended derivation has kernel L0^p. Any nonconstant p-th power has height at least p. Thus p>6D makes v constant; in characteristic zero the derivative-zero conclusion already gives a constant. No unproved p>D substitute is used.

The repeated root of the monic cubic F−c0H lies in k(X): its gcd with its derivative is linear in the double-root case; the triple root is recovered from the quadratic coefficient. Integrality and the weighted coefficient bounds then give

`F−c0H=(u−R)²(u−S)`, with R,S polynomial of degree<=D.

If R=S, a nonzero shifted-label section provides a polynomial h with H proportional to h³, and all sections lie in R+t h. If R!=S, put h=R−S and q=H/h³. For constant q all sections again lie in R+t h. For nonconstant q, the independently audited three-cover lemma allows at most two nonzero shifted labels, each with at most three sections, plus at most R,S at the repeated label: at most eight total.

An affine family has ordinary list bound L(A−D)<=n by its common-zero counting argument. Thus the positive-dimensional case has L<=max(8,1/eta), which is below the proposed general bound. If no nonzero original-label section exists, there are at most three sections from F(X,P)=0, so no height argument is needed.

## Zero-dimensional critical locus and arbitrary domains

Let r be the number of evaluation coordinates at which H vanishes. At any other coordinate x, a candidate matching the received value w_x must have the uniquely determined label c=F(x,w_x)/H(x). A fixed label has at most three polynomial sections because F(X,u)−cH is monic cubic over k(X). Consequently

`L A <= L r+3(n−r) <= L r+3n`,

and therefore `r>=A−3n/L`.

If L>max(9,3/eta), this implies r>D. In particular the total number n0 of distinct roots of H satisfies n0>=r>D. The repeated-H theorem, already audited with the original critical ideal, bounds the entire polynomial-section bank and hence the selected list by

`L <= 9+108D/(n0−D) <= 9+108D/(r−D)`.

Combining this with r−D>=eta*n−3n/L gives

`(L−9)(eta−3/L)<=108D/n`.

Expansion yields

`eta*L <= 9eta+3+108D/n−27/L`,

which is even slightly stronger than the claimed bound. If L<=max(9,3/eta), the claimed bound holds immediately. This accounts for every list size without dividing by a nonpositive expression.

No restriction that the evaluation domain lie among the roots of H is needed. Those roots are forced to cover most agreement coordinates when L is large; this is the bridge from the previous root-domain count to the new arbitrary-word statement.

## Audit conclusion

The proof uses all three verified inputs with their correct scopes: critical-scheme excess counting when the critical ideal is zero-dimensional; a degree-and-characteristic controlled constant-critical-value reduction otherwise; and the genus-three obstruction for the remaining normalized repeated cubic. Splitting F into polynomial seeds and squarefreeness of H are both unnecessary. The weighted monic coefficient bounds and the short-characteristic condition remain substantive hypotheses.
