# Independent audit of the complete C2 obstruction

**PASS**, for the precise sign-twisted doubled-Hadamard incidence model, in characteristic different from2. This is not an exclusion of arbitrary eight-section banks or arbitrary involution actions.

Audited sources: UNIVERSAL_C2_NORM_BRIDGE.md and THREE_SELECTOR_OBSTRUCTION.md. I independently reconstructed the selector matrix from the pairwise quartic elementary sums; verify_three_selector.py/json checks both kernel vectors, all eighteen2×2 minors, and all maximal minors. Runtime0.55 seconds. This reconstruction does not read the generator's saved matrix.

## Incidence and exceptional cases

Each pair has exactly six prescribed intersections, exhausting the sextic degree. Therefore all eight signed leading coefficients are distinct; in particular a0 is nonzero and normalization a0=1 is valid. Subtracting T*B0(T²) preserves the model and permits B0=0.

The all-plus quadratic has p≠0 because its roots are nonzero, and sigma≠0 because otherwise its root set equals its reversal, identifying distinct complementary new nodes. Its two square values are distinct: opposite roots would again imply sigma=0.

For E_i=Ai-A0, factor the all-plus difference as

 E_i(T²)+TBi(T²)=(T²-e0i)(T²-sigma*T+p)*[(ai-1)T²+beta_i*T+zi].

Comparing even and odd parts directly gives the stated universal identity. This proof does not divide by Ci(-p), p+edge, or a coordinate of an involution. At any old edge the factor R0 is a unit, so the beta edge identities hold even if p+edge=0.

Those identities make all beta_i simultaneously zero or simultaneously nonzero. In the zero case the residual quadratic for each pair(0,i) is even. Saturation identifies its two roots with that pair's other two prescribed new nodes; evenness identifies that block with its distinct complementary reversal. Thus zero beta is impossible. Nonzero beta_i are pairwise distinct by the same edge identities.

The complement-slope equations have the displayed signs: the residual slope equals (ui-uj)/(ai-aj)+sigma=(beta_i-beta_j)/(ai-aj). Complementary pairs have reversed residual root sets. The explicit3×3 system has determinant zero and minors ±beta_i(S-2beta_i); these cannot all vanish when beta_i are nonzero. Hence its full kernel is the asserted amplitude line, including all rank-exception cases. t≠0 follows from distinct leading coefficients.

## Polynomial common C and norm

The three H identities follow from eleven distinct Y roots of polynomials of degree≤8. Their leading terms imply that if any physical B_i leading coefficient vanishes then all do. The physical ratios ui/beta_i=1-sigma*t*(S-2beta_i) cannot all vanish, or be all equal, on three distinct beta_i. Thus every Bi has degree2.

The common-root argument is complete even when the root equals e0i or one of e12,e13,e23: at most one edge of the latter triangle is lost, and the other two connect all three labels. It forces the prohibited equality of the three physical ratios. Therefore gcd(B1,B2,B3)=1, and the common rational C has no denominator. Its degree is exactly4, not merely bounded above, by the signed-leading guard.

The degree8 norm has eight distinct nonzero new square roots. At each new node at least one Bi is nonzero because the three have no common root, so the incidence equations genuinely imply C=-2TV there. Thus the norm is squarefree and disjoint from all old edges. No rational-C or additional residual-factor branch remains.

## Selector and final contradiction

All Qi have the same nonzero leading coefficient; common normalization preserves signed-leading distinctness. Their common nonzero constant term forces even Hamming distances. Distances0/8 contradict distinct signed A-leading coefficients. Distances2/6 produce a degree2 factor in the pair decomposition. At an old edge the even/even alternative makes the B values different, whereas the odd/odd alternative requires that quadratic's odd coefficient to vanish. Its two roots would then be opposite, contradicting distinct norm-root squares. Therefore every distance is4. Independently, direct saturated incidence counting gives four shared new matches per pair after its two old matches, yielding the same distance4 conclusion.

For three selectors, the four column sign cells have size2. The independently reconstructed3×4 matrix has the two claimed kernel vectors. Its rank cannot drop below2: all eighteen minors force the three cubic S expressions to vanish; either their triple products are nonzero and all leading sums vanish, or at most two m coordinates survive and two signed leading sums agree up to sign. Both contradict guards. Hence the root-product vector lies in the stated2-plane and all three old edge squares equal the same scalar. This contradicts the six distinct old edges.

No gap was identified in the chain, including the affine involution chart, exceptional p+edge values, mixed even/even pair case, or common-factor possibility. Earlier finite-field searches and large symbolic eliminations are not used by this proof.
