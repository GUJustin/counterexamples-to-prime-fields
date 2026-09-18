# Independent audit: Lattès and completely split fiber gates

Verdict: **both conditional gates pass**. Their restrictions must remain visible; neither proves an arbitrary bounded-degree pencil theorem. No main manuscript changes were made.

## LATTES_SECTION_GATE.md

The Legendre duplication identity and its quadratic discriminant in lambda are correct. Writing a=1−2c±2sqrt(c(c−1)) gives a!=0, lambda=aP²+(1−a)P, and lambda−c=(sqrt(a)P+(1−a)/(2sqrt(a)))². These include c=0,1. For polynomial P, lambda must be polynomial. Two distinct labels would give polynomial squares differing by a nonzero constant, so both square roots would be constant. Thus a nonconstant lambda permits at most one finite label and at most four polynomial x-sections. The assertion for rational sections at three labels also checks: the product of the three square roots yields a nonconstant map from P¹ to a smooth genus-one curve, excluded by Lüroth even in positive characteristic.

For the general nonsingular Weierstrass equation, an actual rational elliptic point T whose double has x-coordinate c indeed gives the square value c³+Ac+B. The cubic is squarefree. Pasten–Wang Theorem 3 with genus zero, polynomial degree three, mu=2 requires M>30, hence31 labels. A squarefree polynomial with a nonconstant irreducible factor cannot satisfy the resulting multiplicity-two conclusion. Characteristic zero is automatic; in positive characteristic p>3 and coefficient height<p ensure separability and exclusion of nonconstant K^p factors.

The eight-section matrix has rank eight: cross-difference degree<=7, eight distinct input functions, then coprimality. The numerator of the duplication map reduces to (3u²+A)² at a denominator root; nonsingularity therefore proves coprimality. The column degree sum is16D. Cramer's-rule minors provide a polynomial coefficient vector of height<=16D, and its (u⁴,u²,u) numerator subvector is proportional to (1,−2A,−8B). Dropping coordinates does not increase projective function-field height; the relevant constants are nonzero for p>3. Thus p>max(3,16D) is a correct sufficient guard. The displayed bound is conservative but valid.

Consequently the stated nonconstant-curve bound is **120 distinct polynomial x-coordinate sections**. It is not a bound of120 on rational elliptic points themselves: a given x-coordinate can correspond to both signs of y. If counting actual points, the immediate corresponding bound is240. The note's use of “bank” for the polynomial x-coordinates is correct; summaries should preserve this distinction.

Equation (7), including its denominator square class c+2P, checks by direct expansion. It prevents applying the cubic square-value theorem to arbitrary rational x-preimages. The exclusion of c+2P=0 before division is appropriate: this case has constant P. The differing-quadratic-twist possibility and X-dependent coordinate changes remain genuine uncovered cases, not positive constructions proved here.

## BOUNDED_DEGREE_SPLIT_FIBER_GATE.md

The reconstruction rank2b+1 is correct. There are enough distinct section functions because distinct labels cannot share a root without contradicting gcd(N,T)=1. The maximal-minor degree bound for coefficient index j is [b(b+1)−j]D. Combining the discriminant's ordinary coefficient degree2b−2 and index-weight degree b(b−1) gives exactly

`A_b D=b(b−1)(2b+1)D`.

The chosen full-degree, nonzero-discriminant split fiber supplies a nonzero square F(c0): its leading coefficient occurs to the even power2b−2. With e=2b−2, the reciprocal transform Z^e F(c0+1/Z)/F(c0) is monic of degree e and height<=A_bD, including when deg F<e. Its extra root at Z=0 belongs to the constant polynomial factor and does not invalidate the theorem.

The characteristic guard p>max(e,A_bD) implies separability for all irreducible factors of degree<=e and excludes nonconstant K^p factors by height. In fact p>e already gives p>b for b>=2, so no separate D=0 exception is needed in that explanatory sentence; this is only a simplification, not a defect in the stated guard.

The multiplicity hypothesis must refer to **nonconstant-coefficient** irreducible factors, after monic normalization. Reciprocal substitution preserves their multiplicities; no such factor can map to the constant root Z=0. With all these multiplicities one, the square-value input mu=2 contradicts their presence. The exact strict threshold is

`M>11e−3=22b−25`.

Thus M>=22b−24 remaining labels, or **22b−23 original labels**, is correct. The conclusion F=s²q(C), q in k[C], follows by undoing the reciprocal transformation.

## Scope that must not be enlarged

For b>=3, a single polynomial section does not make the residual factor's discriminant square. The fully split hypothesis is essential to this particular proof. Repeated moving discriminant factors also evade the multiplicity-one contradiction. Finally a constant branch locus has not yet been converted here into a complete tame-cover descent/isotriviality classification. The note correctly labels that as an additional step rather than invoking it implicitly.

These audits therefore support archiving the two notes as verified conditional research results, without representing them as a solution for all higher-degree rational pencils or all Lattès x-preimages.
