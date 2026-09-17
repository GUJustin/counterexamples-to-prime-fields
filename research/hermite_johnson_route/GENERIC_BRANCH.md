# Generic polynomial-root branches: coefficient fields, poles, and incidence

This is an independent mathematical proof audit. It is not a claim that the proposed interpolation polynomial exists with useful parameters, nor does it cover roots arising only after a special z specialization.

## Setup and conclusion

Letk be an algebraically closed field, K=k(z), and

 Q(X,z,Y)=Σ_{i=0}^B a_i(X,z)Y^i ∈ k[X,z,Y],

witha_B≠0, B≥1, anddeg_z(a_i)≤H. SupposeP(X)=Σ_{j=0}^D c_j X^j∈Kbar[X] satisfiesQ(X,z,P(X))=0. SetL=K(c_0,...,c_D), andd=[L:K]. Then:

1. d≤B, including inseparable branches;
2. on the smooth projective curveC with function fieldL, the common pole divisor of allc_j has degree≤dH;
3. the projective image of(1,z,c_0,...,c_D) has degree≤d(H+1), and the map fromC to that image is birational;
4. every nonpersistent coordinate-agreement hyperplane cuts this branch in at mostd(H+1) points, counted with multiplicity onC;
5. if more thanD distinct evaluation coordinates agree persistently with an affine received line, the branch is an affine polynomial pencil.

No characteristic lower bound is needed for these conclusions over perfect constants. Working overalgebraicclosurek conveniently removes residue-degree notation. The pole argument also works over a perfect nonclosed constant field using divisor degrees with residue degrees.

## 1. Why the coefficient field has degree at mostB

LetT=P(X), considered as an element ofL(X). The minimal polynomial ofT overK(X) has degree exactlyd. In the separable case this is immediate: distinctK-embeddings ofL sendT to distinct polynomials, because equality of polynomials forces equality on every coefficient and the coefficients generateL.

For completeness, inseparability does not create a hidden larger coefficient field here. In positive characteristicp, letLs be the maximal separable subextension ofL/K. It is a one-variable function field over perfect constants and hasp-rank one. Every finite purely inseparable extension ofLs lies in its unique chainLs^(1/p^e); consequently[L:Ls]=p^e equals the purely inseparable exponent.

The number of distinct conjugates ofT is[Ls:K], again because its coefficients generateL. Its inseparability exponent is exactlye. IndeedT^(p^e) has separable coefficients. Conversely, ifT^(p^f) were separable overK(X) forf<e, extend to a finite separable normal closure ofLs. Over that field's rational function field, T^(p^f) is both separable and purely inseparable, hence belongs to the rational function field. A polynomial inX with algebraic constant coefficients that belongs to that rational function field has all its coefficients in the constant field. Therefore everyc_j^(p^f) is separable overK, forcingL/Ls to have exponent≤f, a contradiction.

Thus the minimal-polynomial degree is[Ls:K]p^e=d. It dividesQ viewed inK(X)[Y], so d≤B. Distinct conjugacy classes of polynomial roots correspond to distinct irreducible factors; the sum of their coefficient-field degrees is at mostB, even when inseparable factors occur.

The perfect-constant hypothesis matters. For example overK=Fp(u,z), P=u^(1/p)+z^(1/p)X satisfiesY^p−u−zX^p=0 ofY-degreep, but its coefficient field has degreep². This counterexample cannot occur forK=k(z) withk perfect.

## 2. Common coefficient poles by Gauss valuation

For a placev ofL, use its Gauss extension toL(X). Then

 v(P)=min_j v(c_j),

andv(a_i)=min_Xcoeff v(a_i's coefficient). Suppose firstv lies over a finite place ofk(z). Allv(a_i)≥0. Ifm=v(P)<0, the equationΣa_iP^i=0 forces somei<B with

 v(a_i)+im≤v(a_B)+Bm.

Hence(B−i)(−m)≤v(a_B)−v(a_i)≤v(a_B), so−m≤v(a_B). This bounds the maximum pole order among all coefficients simultaneously, not merely each coefficient separately.

Writeg(z) for the gcd of the nonzeroX-coefficients ofa_B, andh for their maximumz-degree. At finite places the Gauss valuation ofa_B equals the pullback valuation ofg. The finite part of the common pole divisor therefore has degree≤d·deg g.

At places above infinity multiply the entire equation byz^(−H). All transformed coefficients are integral there. The leading coefficient's Gauss valuation is e_v(H−h), wheree_v is the ramification index above infinity. Repeating the root bound gives common coefficient pole order≤e_v(H−h). Its total degree is at mostd(H−h).

Combining both parts gives

 deg Pole(c_0,...,c_D) ≤ d(deg g+H−h) ≤ dH.

The identities summing ramification/residue degrees are valid also for inseparable maps of function fields. Over algebraically closed constants they reduce toΣe_v=d. No separability assumption was used in the Gauss argument.

## 3. Projective degree and individual agreement cuts

The pole divisor ofz has degreed. A common pole divisor for1,z,c_0,...,c_D therefore has degree≤d(H+1). These rational functions define a basepoint-free linear system after their common pole divisor is included. The associated projective morphism has pullback hyperplane degree at mostd(H+1).

Its image function field is preciselyk(z,c_0,...,c_D)=L. Thus the morphism is birational onto its image, including in positive characteristic; no unaccounted inseparable map degree remains. The projective image consequently has degree≤d(H+1).

At coordinatex_i with affine received valueu_i+zv_i, agreement is the hyperplane equation

 g_i=Σ_j c_j x_i^j−u_i−zv_i=0.

Ifg_i is not identically zero, its poles lie in the same common divisor and its zero divisor has degree at mostd(H+1). Counting distinct good specialization points, or their z labels, can only decrease this bound. Points where a coefficient has a pole do not directly specialize to finite polynomial roots; any extra specialized roots must be handled by the separate special-fiber argument.

## 4. Persistent coordinates and affine pencils

Ifg_i=0 identically atD+1 distinctx_i, Vandermonde interpolation overk gives

 P(X)=A(X)+zB(X), degA,degB≤D.

In particularL=k(z), d=1, and the image branch is an affine line (or a projectively equivalent line). This conclusion does not by itself give correlated agreement at a larger thresholdT: the numberq of persistent coordinates may satisfyD<q<T.

For a non-affine branch,q≤D. At any near-codeword label with at leastT>D agreements, there are at leastT−D nonpersistent incidences. Hence that branch contributes at most

 n·d(H+1)/(T−D)

such labels, provided only finite, defined branch specializations are counted.

For an affine branch, ordinary correlated agreement is excluded at thresholdT only ifq<T. Every other coordinate has at most one exceptionalz because its residual is affine in z. Thus the branch contributes at most(n−q)/(T−q)≤n labels. This separate treatment is essential; it is invalid to discard every branch with more thanD persistent coordinates as a threshold-T correlated-agreement witness.

Summing over polynomial-root conjugacy classes usesΣd≤B. Generic non-affine branches therefore contribute at mostnB(H+1)/(T−D), and at mostB affine branches contribute at mostBn. This is only the generic-branch contribution; interpolation existence and special-only roots remain separate tasks.
