# Cubic derivative equations: unique rational singular jet

2026-09-17. Extension of the audited rational-jet argument. No main-paper edit.

## Statement and accounting

Let Q(X,z,u,v) have derivative degree at most three, total (u,v)-degree at most B0, and z-degree at most H0. Put h=B0+H0. Assume characteristic zero or p>3, as well as the regular-incidence and interpolation-root characteristic hypotheses used in the existing theorem. At coordinate x substitute u=f_x+zg_x and write

    F_x(z,v)=a(z)v^3+b(z)v^2+c(z)v+d(z).

Every coefficient has degree at most h. There is a fixed ordinary core S0, a fixed rational-Hermite core S1, and at most 4hn exceptional coordinate-label incidences outside S0 such that every remaining singular agreement outside S0 belongs to S1 and forces one prescribed rational derivative

    P'(x)=r_x(z),

whose numerator and denominator have degree at most 2h. Here S0 consists exactly of coordinates where F_x is identically zero as a polynomial in (z,v).

Consequently the rational Hermite theorem applies with rational-height parameter 2h and exceptional-incidence budget 4hn. Writing u0=|S0| and s=|S1|, its sufficient signed margin is unchanged:

    A-D >= eta*n,
    A-u0 >= sqrt(D*s/2)+epsilon*n.

At fixed positive rate and fixed positive margins, all full-support bad labels among actual polynomial solutions are O(n). Constants depend on B0,H0 and the margins. The original equation's X-degree remains unrestricted.

This is conditional on all candidates being solutions of the common equation. It does not say every arbitrary first-order interpolant has derivative degree at most three.

## Exact local classification

All identities in this section are initially over K(z). For each coordinate determine the generic v-degree m of F_x, after discarding identically zero leading coefficients.

### Generic cubic

Suppose a is nonzero. Define

    Delta=b^2*c^2-4*a*c^3-4*b^3*d-27*a^2*d^2+18*a*b*c*d,
    U=b^2-3*a*c,
    V=9*a*d-b*c.

These have z-degrees at most 4h,2h,2h respectively.

If Delta is nonzero, do not put x in S1. Every singular specialization lies among its roots, at most 4h labels. This assertion also covers degree drops: when a(z)=0 the cubic discriminant becomes b(z)^2(c(z)^2-4b(z)d(z)). A repeated quadratic root therefore still forces Delta(z)=0; if b(z)=0, any singular linear or identically zero specialization also lies among its zeros.

If Delta is identically zero and U is nonzero, put x in S1 and prescribe

    r_x=V/(2U).

Exclude the roots of aU, at most 3h labels. At every remaining label the cubic has exactly one repeated root, given by this formula. To verify it, factor the specialized cubic over an algebraic closure as a(v-r)^2(v-s), with r!=s. Direct expansion yields

    U=a^2(r-s)^2,    V=2a^2*r*(r-s)^2.

The discriminant-zero condition guarantees such a repeated-root factorization; U!=0 excludes a triple root. In particular the repeated root is rational over the specialized base field, without choosing a square root.

If Delta and U both vanish identically, put x in S1 and prescribe

    r_x=-b/(3a).

Exclude roots of a, at most h labels. Since characteristic is not two or three, U=0 and Delta=0 imply c=b^2/(3a) and d=b^3/(27a^2); hence the polynomial is a(v+b/(3a))^3. This also proves rationality of the unique repeated root. No perfectness hypothesis is needed.

### Generic quadratic

If a is identically zero but b is nonzero, use discriminant c^2-4bd. If nonzero, all singular specializations are among its at most 2h roots, including degree drops. If it is zero identically, put x in S1, prescribe r_x=-c/(2b), and exclude roots of b. This is the already audited quadratic case.

### Generic linear, constant, or zero

If a=b=0 and c is nonzero, singular agreement requires c(z)=0, giving at most h exceptional labels. If only d is nonzero, any actual root requires d(z)=0, also at most h labels. Neither type belongs to S1. If all four coefficient polynomials vanish identically, x belongs to S0 and is charged to the ordinary-core loss instead.

The maximum exceptional count in every nonordinary case is 4h. On S1 the rational derivative height is at most 2h, with all its possible poles included in the designated exceptions. The count is coordinate-based and uniform across every candidate, so at most 4hn/(e+1) labels have more than e exceptional coordinates.

## Transfer through rational Hermite interpolation

Use the existing finite Hermite parameters M,T,B,V,c_M. At a coordinate of S1 write r_x=N_x/E_x with numerator and denominator degree at most 2h. In

    R(x+t,z,f_x+zg_x+r_x(z)t+U)

multiply by E_x(z)^B. Every constrained coefficient then has z-degree at most

    H+B(2h+1).

The same dimension argument therefore works with

    H=floor(s*c_M*B*(2h+1)/(V-s*c_M)).

Outside the explicitly counted coordinate-label exceptions, clearing denominators is reversible and matching the first jet gives multiplicity at least M. The specialization-safe root lemma and persistent-agreement incidence argument are unchanged. Regular agreements are still counted using the ORIGINAL equation and its original B0,H0, with no inflation of X-degree or any replacement of full agreement supports.

## Scope of the structural message

A nonzero cubic in the derivative has only one distinct repeated root. This extends the one-jet method beyond quadratic derivative equations. Degree four is the first degree that permits two different repeated derivative roots, for example (v-r_1)^2(v-r_2)^2. Thus an escape from this particular rational single-jet theorem needs either the quantified ordinary-core loss, failure of its numerical agreement margin, lack of bounded equation complexity/containment, or derivative degree at least four. This is not an intrinsic impossibility theorem for all proximity gaps.
