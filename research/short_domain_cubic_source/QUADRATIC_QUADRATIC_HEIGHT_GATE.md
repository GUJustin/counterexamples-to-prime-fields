# Quadratic/quadratic pencil: independent height and square-value gate

The reciprocal-parameter reduction extends the preceding positive-characteristic argument without adjoining a denominator root. The sharper sufficient characteristic condition is **p>10D**, rather than p>12D.

Let k be algebraically closed of characteristic p>2, K=k(X), and let N,T in K[u] be coprime with max(deg_u N,deg_u T)=2. Suppose at least 21 distinct constants c_i admit polynomial sections P_i in k[X], deg P_i<=D, satisfying N(P_i)=c_i T(P_i). If p>10D, the discriminant of N−CT, as a quadratic in u, is a rational-function square times a constant-coefficient polynomial in C.

This is the height/discriminant conclusion. The classification and agreement bound for the resulting Möbius family are a separate step; the sections need not form an affine family.

## Five-section reconstruction

Choose five labels. The sections are distinct, since T(P_i)=0 would force N(P_i)=0. Write the coefficient vector in the order (n2,n1,n0,t2,t1,t0). The five interpolation rows are

`(P_i²,P_i,1,−c_i P_i²,−c_i P_i,−c_i)`.

The matrix has rank five. Indeed, two kernel vectors define pairs whose cross-difference has u-degree at most four and vanishes at five distinct elements P_i of K. It is therefore zero. Coprimality makes every pair proportional to the given pair: since at least one original polynomial has degree two, a common nonconstant multiplier would exceed an allowed degree. Thus the kernel is one-dimensional.

The column X-degree bounds are (2D,D,0,2D,D,0). Signed maximal minors give a polynomial representative with coefficient degrees at most

`(4D,5D,6D,4D,5D,6D)`.

Consequently all coefficients of

`F(C)=(n1−Ct1)²−4(n2−Ct2)(n0−Ct0)`

have X-degree at most 10D. The polynomial F is nonzero and not a square in K(C): the generic polynomial N−CT is irreducible of degree two in u, because N/T is a coprime rational map of degree two; characteristic is not two. A square discriminant would contradict this irreducibility.

## Reciprocal parameter and the primary theorem

There are at most two labels with F(c_i)=0. Choose one of the given sections with F(c0)=s²!=0; explicitly

`s=2(n2−c0 t2)P0+n1−c0 t1`.

This identity also holds when the fiber's quadratic leading coefficient vanishes. Set

`G(V)=V² F(c0+1/V)/F(c0)`.

This is monic of degree two. Its coefficient vector is represented by

`(F(c0), F'(c0), [C²]F)`.

All three entries have X-degree at most 10D, so its projective coefficient height is at most 10D<p. Each of the twenty other section labels gives a distinct nonzero constant V_i=1/(c_i−c0), and G(V_i) is a square in K.

Apply [Pasten–Wang, Theorem 3](https://people.math.harvard.edu/~hpasten/preprints/PWposIMRN.pdf) exactly as audited in `RATIONAL_PENCIL_POSITIVE_CHARACTERISTIC.md`: genus zero, quadratic degree, square multiplicity, twenty distinct constants. Height below p excludes all nonconstant K^p factors by factor-height additivity; degree at most two and p>2 ensure separability. It follows that G has constant coefficients or is a square. The latter is impossible because the reciprocal substitution is a K-automorphism of the parameter function field and the multiplier V²/F(c0) is itself a nonzero square.

Thus G belongs to k[V], and

`F(C)=s² (C−c0)² G(1/(C−c0)) = s² f(C)`

for a constant-coefficient polynomial f in k[C] of degree at most two. The argument includes linear F; its second branch value is then at infinity. No denominator splitting cover or increase of the function-field genus was used.

## Audit boundary

All bounds above are consequences of five low-degree polynomial sections; no independent low-height hypothesis on the initially presented rational coefficients is required. The result applies to D=o(p) eventually. It does not claim an affine form for the polynomial section bank, nor a list-size or bad-line bound before the separate Möbius-family argument is supplied.
