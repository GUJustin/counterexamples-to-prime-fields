# Exact split criterion for the d=4, s=2 native locator labels

September 18, 2026. This audits the named growing-characteristic construction in the prime workspace. No binary-workspace edits, label scans, or rank jobs were made. For every odd prime p and every nonzero head parameter theta in E=F_(p^4), the image of its canonical two-space label map has size

    p^4/2 + O(p^(7/2)),

with an absolute implied constant, uniform in theta. Thus no sequence of nonzero parameters makes this particular label image cover almost all native labels as p tends to infinity. This does not upper-bound additional witnesses that may appear after padding. It preserves the previously proved existence of a parameter whose image is strictly larger than p^4/2.

## 1. Signs, coordinates, and exact recovery of subspaces

For an Fp-basis x,y of a two-space W, put

    Pij=x^(p^i)y^(p^j)-x^(p^j)y^(p^i),
    A=P01, B=P02.

The monic locator is X^(p^2)+a1 X^p+a2 X, where a1=-B/A and a2=A^p/A. Here A!=0. Frobenius gives

    B^(p^2)=-B,
    P12=A^p, P23=A^(p^2), P03=-A^(p^3), P13=B^p.

Consequently the Plucker equation and the label are exactly

    Q(A,B):=A A^(p^2)-A^p A^(p^3)-B B^p=0,
    z=theta*a1+a2^p-a1^(p+1)=(A^(p^3)-theta B)/A.

Basis changes multiply (A,B) by a common nonzero Fp scalar. Conversely every nonzero pair with B^(p^2)=-B and Q(A,B)=0 comes from a unique W up to that scaling. First A cannot vanish, since Q(0,B)=-B^(p+1). Set a=-B/A and b=A^p/A. A direct composition gives

    (X^(p^2)-a^(p^2)X^p-b^(-1)X)
        composed with (X^(p^2)+aX^p+bX)
      =X^(p^4)-X.

The X^p coefficient vanishes because a^(p^2)b^(p+1)+a=0; the X^(p^2) coefficient vanishes by Q=0. Since b!=0, the inner polynomial has exactly p^2 distinct roots in E, forming a two-space. Equality of its a,b for two coordinate pairs forces A'/A in Fp* and then B'/B the same scalar (with the evident interpretation if B=0). This proves recovery without a descent assumption.

## 2. The explicit binary quadratic when Norm(z)!=1

Write indices modulo four and define

    z_i=z^(p^i), t_i=theta^(p^i),
    Z=z_0 z_1 z_2 z_3=Norm(z),
    T=t_0 t_1 t_2 t_3=Norm(theta), delta=1-Z,
    D_i=t_(i+1)-t_(i+3) z_(i+1) z_(i+2).

Suppose delta!=0. The label equation A^(p^3)-zA=theta B has exactly one solution A for every B in the two-dimensional Fp space B^(p^2)=-B. Fourfold substitution yields

    A=(-z_1 D_1 B+D_0 B^p)/delta.

Its conjugates give the exact restricted Klein form

    Q(A,B)=(U B^2+P B^(p+1)+V B^(2p))/delta^2,

where

    U=(1-z_1 z_3)D_1D_3,
    V=(z_0 z_2-1)D_0D_2,
    P=sum_(i=0)^3 z_i D_i D_(i+1)-delta^2.

For a compact discriminant put

    l_i=t_(i+1)t_(i+2)z_i, L=sum_i l_i,
    E2=sum_(i<j)l_i l_j,
    C=sum_(i=0)^3 t_(i+1)t_(i+2) product_(j!=i+2) z_j,

and define the Fp-valued polynomial

    F_theta(z)=(Z-L+1)^2+4*((T-1)Z+T+C-E2).

All its expressions are cyclically invariant, so their values and the polynomial in any Fp coordinate system for E are defined over Fp. Direct expansion gives the exact integer-coefficient identity

    P^2-4UV=delta^2 F_theta(z).

The identity was also checked symbolically with eight independent variables z_0,...,z_3,t_0,...,t_3, before imposing any finite-field relations.

The quadratic-character twist matters. Choose epsilon in F_(p^2) with epsilon^p=-epsilon and d=epsilon^2 a nonsquare in Fp. Choose beta!=0 with beta^(p^2)=-beta, and write

    B=beta(r+epsilon s), r,s in Fp.

Since Q^p=-Q and (beta^(p+1))^p=-beta^(p+1), the form q=Q/(beta^(p+1)) is Fp-valued. The determinant of the change (r,s)->(B,B^p) is -2epsilon beta^(p+1). Therefore its ordinary binary discriminant is exactly

    disc(q)=4d F_theta(z)/delta^2.

In particular, for delta!=0 the number of two-spaces with label z is exactly:

* two if F_theta(z) is a nonsquare in Fp;
* zero if F_theta(z) is a nonzero square;
* one if F_theta(z)=0 but (U,P,V)!=(0,0,0);
* p+1 if U=P=V=0.

These are projective Fp zeros of the binary form, so there is no omitted scaling multiplicity. Nonzero zeros automatically have A!=0. This is the desired exact split and degeneracy criterion on the complement of Norm(z)=1.

As a separate check, on theta,z in Fp the formula specializes to

    F_theta(z)=(z^2-1)^2*((1-z^2)^2+4*(z-theta^2)^2),

agreeing with the independent one-dimensional slice calculation.

## 3. The exceptional norm-one labels

For Norm(z)=1 choose a0!=0 with a0^(p^3)=z a0, and put kappa=theta/a0^(p^3). Such a0 exists by the norm-one criterion for the cyclic multiplicative group. Writing A=a0 C0, the label equation is

    C0^(p^3)-C0=kappa B.

For B^(p^2)=-B it is soluble exactly when

    Trace_(E/Fp)(kappa B)=0.

The image of C0->C0^(p^3)-C0 is the trace-zero hyperplane, and its kernel is Fp. Thus the full linear fiber has Fp dimension two unless kappa lies in F_(p^2), in which case it has dimension three. The trace functional vanishes on every anti-p^2 B precisely in this latter case, by the nondegenerate trace pairing and the decomposition E=F_(p^2) plus its anti-p^2 space.

This gives an exact residual criterion for each exceptional label. In the dimension-two case choose a nonzero allowed B=b0 and any c0 solving c0^(p^3)-c0=kappa b0; then substitute

    A=a0(r+s c0), B=s b0

into Q and divide by beta^(p+1). The usual binary discriminant and zero-form cases give the exact count, just as above. In the dimension-three case the restricted form is ternary and always has a nonzero Fp zero; every such label is attained. This uses the elementary isotropy of a ternary quadratic over a finite field of odd order, including degenerate forms.

The dimension-three locus has the explicit description

    z in theta^(1-p) * mu_(p+1),

and hence consists of p+1 labels. Indeed kappa in F_(p^2)* gives a0^(p^3)=theta/kappa and z=theta^(1-p)kappa^(p-1), and conversely. The whole Norm(z)=1 exceptional locus has exactly p^3+p^2+p+1 elements. Its precise binary split pattern is immaterial to the asymptotic estimate; no generic-fiber assertion is being applied to it.

## 4. Why no nonzero parameter has almost-all image

Choose any Fp basis for E. Its four conjugate coordinates z_i become independent linear coordinates after extending scalars to the algebraic closure: the relevant Moore matrix is invertible because the basis is Fp-linearly independent. Thus geometric squareness can be checked in the independent variables z_0,...,z_3.

For theta!=0, all t_i are nonzero. The degree-eight homogeneous part of F_theta is Z^2; its degree-seven and degree-six parts are zero; its degree-five part is -2ZL; and its degree-three part is 4C. Here C is nonzero: its four distinct cubic monomials have nonzero coefficients t_(i+1)t_(i+2).

If F_theta were a square over the algebraic closure, its polynomial square root would have degree four. Up to sign its degree-four part would be Z. Comparing degrees seven and six forces its degree-three and degree-two parts to vanish. Comparing degree five forces its degree-one part to be -L. The square of such a polynomial has no degree-three part, contradicting 4C!=0. Odd characteristic is used here. A rational-function square would be a polynomial square up to a constant, by unique factorization; over the algebraic closure the constant is also a square. Therefore F_theta is not a square even in the geometric rational function field.

It follows that the affine degree-eight hypersurface

    Y^2=F_theta(z_1,...,z_4) in A^5 over Fp

is geometrically integral, of dimension four. This checks the essential Lang-Weil hypothesis, rather than assuming it from generic fiber behavior. The uniform bounded-degree estimate gives

    #points=p^4+O(p^(7/2)),
    sum_(z in E) chi(F_theta(z))=O(p^(7/2)).

The constants depend only on degree eight and ambient dimension five, not on theta, the field basis, or p. One primary reference stating the needed affine bound with constants depending only on degree and dimension is Kaloyan Slavov, [Improved Lang-Weil bounds for a geometrically irreducible hypersurface over a finite field](https://arxiv.org/pdf/2105.14868), introduction equation (1). Its hypotheses match the geometrically integral hypersurface just established. No smoothness assumption is needed.

Since F_theta is a nonzero degree-eight polynomial, at most 8p^3 labels have F_theta(z)=0. Outside this locus and the p^3+p^2+p+1 norm-one labels, the split criterion says that a label is attained exactly when chi(F_theta(z))=-1. Consequently

    |{z_W(theta): dim_Fp W=2}|=p^4/2+O(p^(7/2)),

uniformly for every theta!=0. For theta=0, every label has Norm(z)=1 directly from z=A^(p^3)/A, so the image has size at most p^3+p^2+p+1. Allowing theta to vary with p therefore does not restore almost-all coverage.

## 5. Construction scope

At the unpadded seed K0=1, this image is also the exact label set for agreement at least p^2-1 with a constant on E*. Indeed such agreement makes the p-linear polynomial X^(p^3)+theta X^(p^2)+zX^p-hX have at least p^2 roots after adjoining zero; its kernel then contains a two-space, recovering the displayed locator label. Thus the result closes the proposed all-native-label strengthening by choosing a special theta in this seed.

For the internally padded fixed-rate pair, it bounds the labels guaranteed by these canonical supports. It does not exclude additional degree-<J witnesses that fail to arise by multiplying a seed constant by the padding locator. The existing characteristic N^(1/4), square-root-order common-agreement gap, and more-than-half lower bound remain valid. No improvement to a prime-alphabet first-order counterexample or to better.codes follows.
