# Independent audit: d=4,s=2 Plücker native-label profile

Verdict: PASS. Reviewed the complete `PLUCKER_D4_S2_NATIVE_LABEL_PROFILE_2026_09_18.md`, not only its asymptotic statement. No binary-repository or manuscript edits. Exact independent algebra replay: `verify_plucker_discriminant_independent.py` and `.json` in this directory; it uses sparse integer polynomials in eight independent variables, not the author's implementation or a finite-field label scan.

## Original labels and converse recovery

The Moore minors give a1=−B/A and a2=A^p/A with A!=0. Their Frobenius identities give the stated Klein equation Q=AA^(p²)−A^pA^(p³)−BB^p=0, and reduce theta*a1+a2^p−a1^(p+1) exactly to (A^(p³)−theta B)/A. Thus the sign agrees with the original locator elimination; it is not a label set for a sign-reversed head.

The converse composition checks coefficientwise. For a=−B/A,b=A^p/A, the outer linearized polynomial X^(p²)−a^(p²)X^p−b^−1X composed with X^(p²)+aX^p+bX has leading term X^(p⁴), X coefficient −1, vanishing X^(p³) coefficient, and the two remaining coefficients vanish by B^(p²)=−B and Q=0. Since b!=0, the inner polynomial is separable and all its p² roots lie in E. This proves an actual two-space, not merely a formal Plücker point. Equality of a,b recovers the coordinate pair up to F_p* scaling, including B=0. No geometric descent hypothesis is missing.

## Generic fiber algebra and nonsquare twist

The fourfold recurrence for A yields exactly delta A=−z1 D1 B+D0 B^p. Conjugating this expression with B^(p²)=−B gives coefficient pairs for (B,B^p):

 (-z1D1,D0), (-D1,−z2D2), (z3D3,−D2), (D3,z0D0).

Independent multiplication recovers U,P,V in the note. The eight-variable integer replay then verifies P²−4UV=delta²F_theta identically, before any field relations. It also verifies the scalar theta,z slice and all homogeneous pieces used later; the resulting F polynomial has 27 terms.

The twist is necessary and correctly signed. Q^p=−Q, and beta^(p+1) has the same anti-Frobenius property, so q=Q/beta^(p+1) is F_p-valued. The determinant of (r,s)→(B,B^p) is −2epsilon beta^(p+1). Binary discriminant scales by the determinant squared and by the square of any scalar multiplier. After the delta^−2 form factor and beta normalization, this gives precisely

 disc(q)=4d F_theta/delta²,

where d=epsilon² is nonsquare. Therefore NONSQUARE F_theta gives two projective F_p zeros; nonzero square F_theta gives none. Discriminant zero gives one unless the whole form is zero, when all p+1 projective points qualify. A nonzero Q-zero automatically has A!=0, so no projective point must be subtracted. This proves the stated exact generic label criterion.

## Exceptional loci

When Norm(z)=1, solving A^(p³)−zA=theta B reduces to C^(p³)−C=kappa B. The image is the absolute trace-zero hyperplane and kernel F_p. The trace annihilator of the anti-p² two-space is precisely F_{p²}; hence the fiber dimension is two or three exactly as stated. In dimension three, any ternary quadratic over a finite field of odd order is isotropic (including degenerate forms), and nonzero Q-zero still forces A!=0.

The dimension-three parameter set is z=theta^(1−p)kappa^(p−1), kappa in F_{p²}*, exactly theta^(1−p)mu_(p+1), with p+1 elements. The entire norm-one locus has p³+p²+p+1 elements. These exceptional fibers are treated directly rather than assigned the generic discriminant test.

## Geometric nonsquareness and counting

Over the algebraic closure, the four Frobenius-conjugate coordinate linear forms are independent by the invertible Moore matrix of an F_p-basis of E. The polynomial coefficients descend to F_p because the formulas are invariant under cyclic conjugation.

For theta!=0, every conjugate t_i is nonzero. The homogeneous pieces in z have degrees 8: Z²; 7 and 6: zero; 5: −2ZL; 3: 4C. The four cubic monomials in C are distinct and have nonzero coefficients. If F_theta were a geometric square, a degree-four square root would have leading part ±Z; comparison forces its degree-three and degree-two parts to vanish and its degree-one part to be ∓L. Such a square has zero cubic part, contradicting 4C!=0. This works in every odd characteristic, including three. Rational-function squareness reduces to polynomial squareness by unique factorization.

Thus Y²−F_theta is irreducible over the algebraic closure's rational function field and, being monic primitive in Y, defines a geometrically integral affine hypersurface in A⁵ of degree eight and dimension four. Smoothness is not required. The cited primary estimate was checked directly in [Slavov, introduction Eq. (1)](https://arxiv.org/html/2105.14868): its constants depend only on degree and ambient dimension. It therefore gives uniformly in theta and the coordinate basis

 #hypersurface(F_p)=p⁴+O(p^(7/2)),
 sum_z chi(F_theta(z))=O(p^(7/2)).

The zero set of F_theta has at most 8p³ points, and the norm-one locus has O(p³) points. Removing or restoring these loci changes the attained-label count by O(p³), smaller than the stated error. Hence every nonzero theta has image size p⁴/2+O(p^(7/2)) with an absolute implied constant. For theta=0, the direct norm-one restriction gives only O(p³) labels. Letting theta vary with p cannot evade this uniform conclusion.

## Link to the construction and scope

At the unpadded seed, p²−1 nonzero agreements with a constant give at least p² roots after adjoining zero of the stated linearized polynomial. Its F_p-kernel contains a two-space; linearized division or the locator elimination then recovers the original label. This remains true if the constant is zero and the residual is inseparable: the finite-field kernel is still a vector space, and the two-space locator is separable. Thus the canonical image is the exact label set at that unpadded threshold.

After internal padding, other strict-degree witnesses need not be divisible by the padding locator. The result bounds the canonical labels, not all possible labels of the padded line. It does not contradict the pooling guarantee of more than half, and it does not prove an upper bound on padded-source failure. No positive prime-alphabet or benchmark conclusion is justified by this classification alone.
