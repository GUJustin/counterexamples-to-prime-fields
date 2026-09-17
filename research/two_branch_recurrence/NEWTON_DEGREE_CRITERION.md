# A leading-degree criterion for linear first-order MCA counts

September17,2026. Generalization of the shared-denominator argument,
submitted for independent audit. No novelty claim. This is a theorem
about candidates satisfying a specified identity, not a construction of
such an identity for every received word.

## Statement

Let F be ANY field and D>=1, ell>=2. Consider actual degree-<=D
polynomial solutions of

    T(X,z) P' + sum_(j=0)^ell A_j(X,z) P^j=0.       (1)

Assume A_ell!=0, deg_X T=t, with leading coefficient tau(z)!=0,
and the following degree restrictions:

    deg_X A_1<=t-1,
    deg_X A_0<=t+D-1,
    deg_X A_j+jD<t for 2<=j<=ell when A_j!=0.       (2)

No separate characteristic restriction is needed: the explicit pivot
hypothesis below supplies exactly the required invertibility. All
coefficient polynomials T,A_j have z-degree at most a, a fixed
nonnegative integer. Assume each polynomial pivot

    d_i=i tau+(A_1)_(t-1), 1<=i<=D

is nonzero. In particular t>ell D, since A_ell!=0. Put

    delta=aD, M=a(ell D+1), L=aD+1.

On any n distinct evaluation points and any received line f+zg, at any
integer agreement A>D, actual solutions of(1) have full common witnesses
outside at most

    a(D+1)+2ell M+n(M+ell L)/(A-D)+ell n            (3)

labels. This is O_{a,ell,eta}(n) when A-D>=eta*n and D<=n. It includes
solutions singular at every agreement coordinate; no lower bound on the
number of nonsingular agreements is assumed.

## 1. Top-degree elimination

By(2), every nonlinear term has X-degree<t after substituting any
candidate of degree<=D. Hence the equations at X^(t+i-1), i=D,...,1,
are linear triangular equations for the nonconstant coefficients of P.
The coefficient of its i-th coefficient is d_i. The constant coefficient
c=P(0) does not occur at those degrees. Each off-diagonal coefficient has
z-degree<=a, and the inhomogeneous coefficient from A_0 also has degree<=a.

As in SHARED_DENOMINATORS.md, set Delta_i=product_(h=i)^D d_h and
Delta=Delta_1. Then the i-th message coefficient is N_i/Delta_i with

    deg N_i<=a(D-i+1).

Passing to the common denominator Delta shows that

    P=c+W(X,z)/Delta(z), W(0,z)=0,
    deg_z Delta<=aD, deg_z W<=aD.                  (4)

No denominator of degree quadratic in D is needed. Exclude the at most
aD roots of Delta. On the complement, the parametrization exactly
preserves the actual solution locus, not merely a superset of formal
solutions.

## 2. A bounded-degree plane system

Substitute(4) into(1) and multiply by Delta^ell. Every residual coefficient
in X is a polynomial F_i(z,c) of c-degree<=ell and z-degree<=M:

    Delta^(ell-1) T W'
        +sum_j A_j(c Delta+W)^j Delta^(ell-j).

Each term has z-degree at most a+ell aD=M. Choose a nonzero coefficient
h(z) of A_ell as a polynomial in X. The corresponding residual has
c-leading coefficient h(z)Delta^ell. Exclude also the at most a roots of
h. On the resulting open set the plane system has a nonzero equation
of c-degree ell, with nonvanishing leading coefficient.

Let U be the greatest common divisor of all nonzero residual polynomials,
over an algebraic closure. Its irreducible factors describe all curve
components of the common zero set. U divides the chosen residual, so
its summed bidegrees are at most(M,ell). Any vertical factor must be
supported on a root of h Delta, already excluded. Thus there are at
most ell reduced horizontal components.

Divide every residual by U. The resulting system has gcd1. If one
residual quotient is a nonzero constant, there are no common zeros off
U. Otherwise choose a nonzero quotient G and a generic constant linear
combination H of the other quotients that shares no irreducible factor
with G. Such a combination exists: each of the finitely many factors of
G is avoided by some quotient, because the total gcd is1. Coefficients
may be chosen over the algebraic closure, which is infinite.

Both G and H have bidegrees at most(M,ell). Their proper intersection in
P1_z x P1_c has total multiplicity at most2M ell. Every isolated point
of the original common zero locus lies off its curve locus U=0 and is
one of these intersection points. Therefore isolated labels outside the
excluded set number at most2M ell. The bound also covers all finite
residual loci. When M=0 it correctly gives no isolated challenge labels:
the equations do not vary with z.

## 3. Incidences with the actual received line

Agreement at coordinate x is the equation

    Delta c+W(x,z)-Delta(f(x)+zg(x))=0,

of bidegree at most(L,1). On a component C of bidegrees(s,r), unless
agreement is identically true, its resultant has z-degree at mosts+rL.
Away from Delta=0 every root gives at most one agreeing point, since
the agreement equation is linear in c with nonzero leading coefficient.
Summing over components gives at most M+ell L nonpersistent agreeing
points per coordinate.

If a component has at most D persistent coordinates, each A-near point
uses at least A-D nonpersistent incidences. This contributes at most
n(M+ell L)/(A-D) labels. If it has more than D persistent coordinates,
interpolation forces the whole candidate polynomial to equal a base-field
affine codeword graph F0+zG0. Outside at most n extra-agreement labels,
its full agreement set is the coefficientwise common agreement set of
those witnesses. There are at most ell components. Adding the excluded
labels and isolated-label bound proves(3).

## Interpretation and boundary

This is a Newton-degree separation criterion: the top D coefficient
equations are linear because the nonlinear value terms lie strictly below
them. It permits moving nonmonic T, bounded-degree parameter dependence,
and nonlinear value degree ell. It does not require T to be a locator
or nonzero at any evaluation point. Thus it addresses cases excluded by
the repository's earlier nonsingular-agreement argument, which required
agreement larger than the separant degree.

The restrictions still exclude generic implicit equations nonlinear in P',
identically resonant pivots, and nonlinear terms entering the top-degree
range. The known quadratic isolated Wronskian family lies at this last
boundary, as detailed in SHARED_DENOMINATORS.md. To search for genuinely
superlinear nearby families, build agreement into equations with that
nonlinear interference; bounded challenge degree or nonmonic pivots alone
do not evade this theorem.

The use of a generic residual combination and intersection theory only
counts actual isolated points. It does not assume linear independence
implies coprimality: the common curve gcd is removed explicitly first.
