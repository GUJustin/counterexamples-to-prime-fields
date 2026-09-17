# Specialization-safe polynomial-root lemma

2026-09-17. Proof prepared independently of the interpolation step. All geometry is over an algebraic closure of the coefficient field. No assumption that special roots automatically extend to generic polynomial roots is made.

## Statement

Let 0!=Q(X,z,Y) be a polynomial with

    deg_X Q <= T, deg_z Q <= H, 1<=deg_Y Q<=B,

and assume characteristic zero or characteristic p>B. Let D>=0 and C=B+H. There is a set E of at most (2B+1)H challenge values and a collection of polynomial-root curves such that, for z outside E, every degree-at-most-D polynomial P with Q(X,z,P(X)) identically zero is either on one of these curves or belongs to a set of at most

    max(0,2(T+BD)-1) C^2                              (S1)

exceptional solution pairs (z,P). The curves consist entirely of degree-at-most-D polynomial solutions; their total degree in coefficient space with the challenge coordinate included is at most

    C [1+max(0,2D-1)C].                               (S2)

Both bounds are linear in T+D when B,H are fixed. In particular the number of exceptional challenge values is O_{B,H}(T+D), as required. We may discard finitely many points on each curve when describing its rational parametrization; outside E the retained curves contain every specialization of its generic polynomial branch.

The characteristic restriction is only for the elementary squarefree reduction. The Hasse/Taylor recursion below divides by Q_Y, never by an integer or a factorial. In particular it needs no condition p>T or p>D.

## 1. Safe content removal and squarefree reduction

Work over an algebraically closed constant field K from the outset. Factor Q in K[X,z,Y]. Remove all irreducible factors independent of Y and retain each remaining irreducible factor only once, obtaining R. The degree in each variable does not increase. Each retained factor is separable in Y: its positive Y-degree is less than p, so its Y-derivative is nonzero; irreducibility and characteristic zero or p>B give coprimality over K(X,z). Consequently R is squarefree in Y over K(X,z).

If Q has no positive-Y factors, all possible polynomial roots occur when its Y-independent content specializes to zero identically in X. This yields at most H challenge values, and there are no curves to consider.

In the remaining case, write Q=c(X,z) prod_i R_i(X,z,Y)^{m_i}. Choose any nonzero coefficient of c as a polynomial in X. Its roots in z, at most H, contain every value at which c(X,z) vanishes identically. Outside this set, the specialized identities Q(X,z,P)=0 and R(X,z,P)=0 are equivalent, because K[X] is an integral domain. No additional specialization principle about factorization is needed.

## 2. A regular center with a constant-size exceptional set

Choose alpha in K so that both the Y-leading coefficient of R(alpha,z,Y) and

    Res_Y(R,R_Y)(alpha,z)

are nonzero polynomials in z. Such alpha exists: the corresponding polynomials in X,z are nonzero, so only finitely many constants make all their z-coefficients vanish. There is no need to adjoin a transcendental constant or to work over an imperfect constant field.

Set F(z,u)=R(alpha,z,u) and A(z,u)=R_Y(alpha,z,u). Exclude zeros of the leading coefficient and resultant. Their total number is at most

    H+(2B-1)H=2BH.

Together with the content exception this proves |E|<=(2B+1)H. Outside E, every initial value u with F(z,u)=0 is a simple root, so A(z,u)!=0, and F has its generic Y-degree. This also excludes intersections of distinct positive-Y components at such points.

The initial plane curve F=0 has total degree at most C. Ignore vertical components; they occur only over the excluded leading-coefficient/content values. Its remaining irreducible components have total degree at most C.

## 3. Uniform Taylor denominators and degree bounds

Expand around alpha using Hasse coefficients:

    R(alpha+t,z,u+v)=sum_{a,b} c_ab(z,u)t^a v^b.

Every c_ab has total degree in (z,u) at most C, independently of T. On the curve F=0 the constant coefficient vanishes and c_01=A. There is a unique formal solution

    v(t)=sum_{j>=1} a_j t^j

where A is invertible. For every j>=1,

    a_j=N_j(z,u)/A(z,u)^(2j-1),
    deg N_j <= (2j-1) C.                              (S3)

Here the numerator is a polynomial representative, with equality interpreted in the function field of each initial-curve component; the same universal recursion supplies representatives for all components.

Proof by induction: solve the coefficient of t^j for A a_j. A remaining term with t-degree a and v-degree b has a product of earlier coefficients with indices summing to j-a. After division by A its denominator exponent is

    e=2(j-a)-b+1 <= 2j-1,

since the removed linear term is the only contributing term with 2a+b<2. Its numerator has degree at most eC, by the inductive bounds and the coefficient c_ab. Multiplying by A^(2j-1-e) gives the stated common denominator and degree. For b=0 the contributing coefficient has a=j and e=1, with the same bound. No factorials are inverted.

## 4. Why a nongeneric special polynomial root costs only O(T+D) points

Fix an irreducible nonvertical component Gamma of F=0. The preceding formal solution is defined over its function field. If it is a polynomial of degree at most D, retain Gamma as a polynomial-root component.

Otherwise some coefficient a_j with

    D<j<=N:=T+BD                                     (S4)

is nonzero in that function field. To prove this, let P_D=u+sum_{i=1}^D a_i t^i. If every coefficient after D through N vanished, the true formal solution and P_D would agree through order N. Substituting P_D into R therefore gives a polynomial vanishing through order N. Its t-degree is at most T+BD=N, so it vanishes identically. Since its constant value is u and A!=0, uniqueness of the formal implicit root forces it to equal the original series, contradicting our assumption. If N<=D there are consequently no nongeneric components.

Choose just one index j satisfying (S4) for each nongeneric component. By (S3), N_j is not identically zero on that component. Every specialized degree-at-most-D polynomial root on this component, outside E, has a_j=0 and hence N_j=0. Plane Bezout bounds these points by

    deg(Gamma) (2j-1)C.

Summing over components gives (S1), because their degrees sum to at most C. There is only one polynomial root at each regular initial point (z,u), by formal uniqueness. Thus this bounds solution pairs, not merely an auxiliary projection with uncontrolled fibers. This is the missing specialization safeguard.

## 5. Degree of the retained coefficient curves

For D>=1 put delta=A^(2D-1). The map from a retained initial component to the challenge and coefficient vector is

    (z,u) -> (z,u,a_1,...,a_D).

Using (S3), its homogeneous coordinate functions can be represented by

    delta, z delta, u delta,
    N_j A^(2D-2j) for 1<=j<=D.

Every entry has degree at most 1+(2D-1)C. A rational map given by forms of degree at most L sends a plane curve of degree d to a curve of degree at most dL (homogenize to common degree and intersect with a generic hyperplane). Base points only lower this upper bound. Summing yields (S2). For D=0 the map is the identity on (z,u), giving degree at most C.

The map remembers z and u, so it is generically injective. Converting Taylor coefficients at alpha to monomial coefficients in X is an invertible linear map, preserving the degree bound. Every regular point on a retained component specializes to a polynomial solution: all coefficients beyond D vanish identically in its function field, and the degree-D polynomial substitution identity therefore vanishes on the component. The recursion has no pole outside A=0, already excluded in E.

## Application scope

This lemma supplies a bounded-degree collection of actual solution curves, O(T+D) isolated solution pairs, and a constant number of exceptional labels. It does not on its own show that every nearby RS candidate satisfies the interpolated equation; that containment is the separate Hermite interpolation step. Nor does it by itself count ordinary-common-agreement exceptions; the persistent-agreement incidence argument must be applied to these actual solution curves.
