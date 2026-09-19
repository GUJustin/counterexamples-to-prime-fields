# Odd h: Kummer branch classification and exact source agreement

2026-09-18. Independent algebraic verdict: **PASS** under the explicit hypotheses below. This strengthens the previous h=5 audit to all odd h and removes the individual-source uncertainty when p>=h². No scan or manuscript edit.

## One good branch: descent before applying Kummer

Let B=F_(p²), let h>1 be odd with h dividing p²+1, and let P in B[Z] have degree at most h. In particular gcd(h,p²-1)=1 and the characteristic does not divide h. A good branch requires solving

    z^(hp)=P(z), z in B.

For nonconstant P choose the largest divisor d of h for which P is a dth power polynomial over the algebraic closure, and put H=h/d. One may write P=R^d with R in B[Z]. Indeed, normalize P by its leading coefficient; its unique monic dth root is fixed by coefficientwise p²-Frobenius and therefore belongs to B[Z]. The leading coefficient of P has a unique dth root in B*, since gcd(d,p²-1)=1. Scaling the monic root gives the required R. Its degree is at most H.

The dth-power map is bijective on B, including zero. Hence the original equation is equivalent, on B-points, to

    z^(Hp)=R(z).

This reduction avoids having to compare roots-of-unity factors of the original degree-h curves.

If H>1, maximality of d says R is not a qth power polynomial over the algebraic closure for any prime q dividing H. A polynomial is a qth power in the rational function field precisely when all its root multiplicities are divisible by q (scalar factors have roots over the algebraic closure). The Kummer irreducibility criterion therefore makes U^H-R(Z) irreducible over the algebraic-closure rational function field, and hence in the two-variable polynomial ring. Since H is odd, there is no additional fourth-power binomial exception. For H=1 the polynomial is linear in U and is irreducible directly.

Every B-solution lies on the two curves

    F(Z,U)=U^H-R(Z),
    G(Z,U)=Z^H-R^sigma(U),

where sigma is coefficientwise p-th power and U=z^p. Both curves have total degree H. A common component would force G=cF, since F is irreducible and the degrees agree. Comparing coefficients then forces

    R(Z)=a Z^H+b.

This is a necessary shape condition, not an assertion that every such R actually gives a common component.

If R has this shape, a,b belong to B and the Hth-power map also permutes B. Writing y=z^H reduces the equation to y^p=a y+b, with at most p solutions. If R does not have this shape, the curves have no common component and Bezout gives at most H² solutions. A constant P has at most one solution separately. Consequently every normalized polynomial with a nonzero intermediate coefficient has the uniform bound

    good-branch matches <= max(p,h²).

When d=1 the common-component shape would be P=aZ^h+b, excluded by the nonzero intermediate coefficient. When d>1, that shape for R may give a genuinely noncanonical P=R^d; the semilinear p-bound is exactly what handles it.

## Number of good branches

Use the primitive-scale two-block construction over E=F_(p⁴), with M=p²+1, alpha_t=xi^((M/h)t), and the guard h-1<M/h. A degree-at-most-h polynomial Q outside the family aX^h+b has a nonzero coefficient q_j for some1<=j<h.

Within either block, the necessary coefficientwise-B condition on branch index t is a cyclic congruence whose number of solutions is either zero or gcd(j,h). Across the two blocks the earlier congruence obstruction rules out good branches in both blocks simultaneously. Therefore the total number of good branches across the full2h-branch domain is at most

    gcd(j,h) <= h/ell,

where ell is the smallest prime divisor of h. This bound uses a single fixed nonzero intermediate coefficient of Q, so different coefficients or branches do not need to be selected adaptively.

Every bad branch contributes at most h matches by projection. On every good branch the intermediate coefficient remains nonzero under normalization, and the classification above applies. Since max(p,h²)>=h, replacing the actual good-branch count by its upper bound is valid. Thus all noncanonical Q, uniformly in the challenge, satisfy

    agr <= (h/ell)*max(p,h²) + (2h-h/ell)*h.

Arbitrary puncturing of the original two blocks, including deterministic branch prefixes, preserves this estimate. It does not authorize additional neutral coordinates.

## Exact sources when p>=h²

Under p>=h², the last bound becomes

    U_nc=(h/ell)*p + (2-1/ell)*h².

For every odd h>=3 and ell>=3 this is strictly less than hp. Indeed, the difference is at least its value at p=h²:

    hp-U_nc >= h² * [(1-1/ell)h-(2-1/ell)] > 0.

Thus all noncanonical witnesses have fewer than hp matches. Canonical witnesses outside the doubly canonical label planes have at most hp matches. Either explicit endpoint outside those planes has a core canonical fiber attaining hp. Consequently

    A(r0)=A(r1)=CA(r0,r1)=hp.

The original canonical threshold-list profile is unchanged for every threshold above hp for which all retained canonical supports qualify. In this p>=h² regime the old sufficient inequality hp+h²<T may be weakened to hp<T; retaining the old stronger guard is also valid.

The asymptotic sequence h=5^a, p>h^(a+4) satisfies p>=h², so its source agreements are exactly hp, not merely hp+O(h²). Its already proved asymptotic agreement locations and limiting loss ratio are unchanged.

For h=5,p=97 this recovers exact sources485. For the BabyBear h=12241,p=2013265921 parameters, p>h² also holds, so both sources are exactly24644388138961. No primality assumption on h is needed for this conclusion; the smallest-prime-factor bound suffices. A sharper numerical noncanonical cap can use that factor if independently verified.

This audit does not claim irreducibility when h is even, a classification of arbitrary received sources, or any statement about a prescribed practical domain. The descent, odd Kummer condition, primitive scale, finite branch guard, and retained-domain hypothesis are all part of the result.
