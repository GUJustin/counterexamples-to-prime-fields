# Quadratic/linear pencils in short prime-field regimes

The algebraic reduction in `RATIONAL_PENCIL_BUCHI_BRIDGE.md` passes independent audit. A newer primary theorem yields a positive-characteristic extension with an explicit height bound: **twenty distinct section labels and p>6D force the same affine-family conclusion for sections of degree at most D**. This is an exclusion for this rational-pencil class, not a new lower-bound construction.

## Verified primary theorem and its exact scope

Hector Pasten and Julie Tzu-Yueh Wang, *Extensions of Büchi's Higher Powers Problem to Positive Characteristic*, IMRN 2015(11), 3263–3297, DOI [10.1093/imrn/rnu033](https://doi.org/10.1093/imrn/rnu033). The [author manuscript](https://people.math.harvard.edu/~hpasten/preprints/PWposIMRN.pdf), Theorem 3, printed pages 4–5, applies over a genus-g function field with algebraically closed constants. For a monic degree-n polynomial, remove its constant polynomial factors. Its remaining distinct irreducible factors must be separable and not belong to K^p[C]. If mu is at least every factor multiplicity and every zero of each of M distinct constant specializations has multiplicity divisible by mu, then all remaining factor multiplicities equal mu, provided

`M > 4n max(g−1,0)+11n−3`.

Identically zero specializations are allowed. For n=2, g=0, mu=2 this requires **M>=20**. Squares meet the zero-multiplicity condition. Section 2 defines projective coefficient height and records its additivity under polynomial multiplication.

The earlier [Shlapentokh–Vidaux manuscript](https://arxiv.org/pdf/1004.0731), Theorem 1.4, concerns consecutive prime-field arguments and permits Frobenius-shaped exceptions. It cannot simply be applied to arbitrary pencil labels. The newer arbitrary-label theorem above supplies the needed precise input. Pasten's characteristic-zero eight-label theorem is not being extended by analogy.

## Corollary with an explicit short-characteristic condition

Let k be algebraically closed of characteristic p>2 and K=k(X). Suppose

`N=n2 u²+n1 u+n0`, `T=d1 u+d0`,

have coefficients in K, n2*d1!=0, and gcd(N,T)=1 in K[u]. Let D>=0, p>6D. If at least twenty distinct constants c_i admit polynomial sections P_i of degree at most D with N(P_i)=c_i T(P_i), then all polynomial sections of this pencil lie on a single affine family A+sB, s in k. The generators A,B can be chosen polynomial of degree at most D, with B!=0.

### Four sections control coefficient height

Different labels yield different sections: T(P)=0 would force N(P)=0, contradicting coprimality. Choose four sections and form the four rows

`(P_i², P_i, 1, −c_i P_i, −c_i)`.

This 4-by-5 matrix has rank four over K. Indeed, any vector in its kernel gives another pair (Ntilde,Ttilde) of degrees at most (2,1). The cross-difference Ntilde*T−N*Ttilde has u-degree at most three and vanishes at the four distinct P_i, so it is zero. Coprimality and the exact numerator degree two imply that the new pair is proportional to (N,T). Thus the kernel is one-dimensional.

Signed maximal minors provide a polynomial representative of the original pair. Column degrees in X are bounded by (2D,D,0,D,0), so its coefficient degrees obey

`deg(n2,n1,n0,d1,d0) <= (2D,3D,4D,3D,4D)`.

There is no assumption here that the originally supplied rational coefficients have small height; the sections themselves produce the bounded representative.

### Excluding the Frobenius factors

Form the monic discriminant quadratic in the label C:

`G(C)=C²+((-2n1 d1+4n2 d0)/d1²) C+(n1²−4n2 n0)/d1²`.

Its projective coefficient vector can be represented by three polynomials of degree at most 6D. Hence its height is at most 6D<p. For every section label, G(c_i) is the square of `(2n2 P_i+n1−c_i d1)/d1`.

Heights of monic factors add: at each place, the minimum coefficient valuation of a product is the sum of the two minima (Gauss's lemma), and summing gives the claim. Therefore each monic irreducible factor of G has height less than p. A monic polynomial in K^p[C] with at least one nonconstant coefficient has such a coefficient f^p; its height is at least h(f^p)=p h(f)>=p. No such factor occurs. Factors in k[C] are removed before applying the primary theorem. All irreducible factors of degree at most two are separable because p>2.

If G has nonconstant coefficients, apply the quoted theorem with mu=2. Every nonconstant irreducible factor must have multiplicity two. Since the total degree is two, this forces G to be a square. But its discriminant as a polynomial in C is

`16 n2 (n2 d0²−n1 d1 d0+n0 d1²)/d1^4`,

which is nonzero by n2*d1!=0 and gcd(N,T)=1. Thus G must instead have constant coefficients.

### Affine family and agreement bound

The quadratic formula now gives every section in the form

`P=−n1/(2n2)+(d1/(2n2))*(c±sqrt(G(c)))`.

Both scalar choices are constants because k is algebraically closed. Choose two distinct polynomial sections to turn these rational affine generators into polynomial generators A,B of degree at most D. This covers all polynomial sections, not only the twenty initially chosen.

For a bank of L distinct degree-at-most-D sections and an arbitrary received word on n distinct coordinates, each candidate agreeing at least a times, the common positions B(x)=0 number at most D; elsewhere at most one candidate matches. Therefore `L(a−D)<=n`.

Without twenty distinct labels there are at most nineteen fibers, each containing at most two sections. Thus any bank from this pencil with a−D>=eta*n satisfies

`L <= max(38, floor(1/eta))`.

This applies over prime fields by extending constants to their algebraic closure. The two polynomial generators can be chosen from base-field sections; a base-field section then has a base-field scalar coefficient. In particular D=o(p) eventually meets p>6D. No automatic extension to quadratic denominators, higher numerator degree, or general first-order differential equations is asserted.

## Audit outcome

The original characteristic-zero discriminant reduction, coprimality exclusion of the square case, and agreement counting are correct. The positive-characteristic extension above uses a verified arbitrary-label theorem plus an explicit four-section height calculation. No numerical scan or unproved suppression of Frobenius exceptions is involved.
