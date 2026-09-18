# Independent Newton/discriminant audit

## Exact local support lemma: PASS

Let t=X−x and translate Y by the received symbol. Write N=Y−tR and use the normal monomials

    t^i Y^k N^j R^l,  i l=0, j+l≤r.

These are a basis of the R-degree≤r polynomials: reducing tR=Y−N gives spanning, while substitution Y=tR+t²E,N=t²E gives distinct initial monomials

    t^(i+k+2j) R^(k+l) E^j.

For fixed j, the pair (i+k,k+l) uniquely determines i,k,l under i l=0. Hence no initial-contact cancellation is possible. In particular every nonzero normal monomial occurring in a contact-a polynomial has i+k+2j≥a.

To contribute to the leading physical R^r coefficient A_r(t,Y), a monomial must have j+l=r; its leading contribution is (−1)^j t^(i+j)Y^k. Put u=i+j. If i>0 then l=0,j=r; if i=0 then j=u≤r. Thus j=min(u,r), uniquely. These contributions cannot cancel either. Therefore every monomial t^uY^k of A_r satisfies

    u+k+min(u,r)≥a.

This is exact in every characteristic and uses the actual first-jet substitution.

## Discriminant valuation: PASS, with a stronger nonmonic formulation

Let q=deg_Y A_r≥1 and assume its discriminant Δ_Y(A_r) is nonzero. No local-unit assumption on the leading coefficient is required. Define

    Φ_(q,r)(a)=Σ_(j=1)^(q−1) max(0,a−j,2(a−j−r)).

Then at the coordinate x,

    ord_x Δ_Y(A_r) ≥ Φ_(q,r)(a_x).

Proof: extend the t-adic valuation to an algebraic closure of the fraction field. The coefficient support bound puts every Newton-polygon point above the convex piecewise-linear function

    g(j)=max(0,(a−j)/2,a−j−r).

Therefore the lower Newton polygon ν(j) is also above g. This statement is about polygon ordinates, not a pointwise count of roots above each of the displayed slopes.

Write the finite root valuations increasingly as v1≤...≤vq and let b be the leading-coefficient valuation. For nonzero discriminant the roots are distinct, and

    val(Δ)=(2q−2)b+2Σ_(i<j)val(ρ_i−ρ_j)
           ≥(2q−2)b+2Σ_(i=1)^q(q−i)v_i
           =2Σ_(j=1)^(q−1)ν(j).

The last identity follows because ν(q−k)=b+Σ_(i=1)^k v_i. Thus the leading valuation cancels exactly; negative root valuations cause no problem. If there is a single zero root, omit its infinite valuation from the zero-weight final term or apply the same formula with that convention. Two zero roots would make the discriminant zero and are outside this branch. No Puiseux expansion, factorial division, or tame-ramification assumption is used.

When q≥a, summing g gives the proposed formula

    D_r(a)=a(a−1)/2                         if a≤2r,
           a(a−1)−r(2a−2r−1)             if a≥2r.

For q<a the correct unconditional expression is the truncated Φ, not D. Importantly Φ is convex as a function of a. Hence a global mean contact bound gives a Jensen bound even when some individual contacts exceed q or the leading coefficient vanishes. At q=43,r=12,a=40, Φ=900.

A false shortcut to avoid: the support bound does not guarantee a−2r roots of valuation at least1. For example Y⁴+t³ satisfies the r=1,a=4 support bounds but all roots have valuation3/4. Its integrated polygon/discriminant bound still holds.

## Global polynomial degree budget

If F has weighted degree V with wt(X)=1,wt(Y)=w,wt(R)=w−1, then A_r has weighted degree at most W0=V−r(w−1). Let q=deg_Y A_r and d=W0−qw≥0. Weighted homogeneity of the discriminant gives

    deg_X Δ_Y(A_r)≤(q−1)(2W0−qw)
                 =q(q−1)w+2(q−1)d.

Consequently, on the nonzero-discriminant branch,

    Σ_x Φ_(q,r)(a_x)≤q(q−1)w+2(q−1)d.

This applies to arbitrary received symbols and nonuniform contacts. It is a resource bound; it does not by itself identify a remaining normal-component pole/genus cost or a complete benchmark certificate.

## The zero-discriminant branch is real

Irreducibility and regularity of F do NOT imply squarefreeness of A_r. For example

    F=Y²(R−1)+Y−X

is primitive and irreducible as a linear polynomial in R, has actual polynomial solution P=X, and F_R(X,P,P')=X² is nonzero generically. But A_1=Y² has identically zero discriminant. This example does not claim the binding high-contact source caps; it disproves deriving the missing hypothesis from irreducibility/regularity alone.

At the benchmark p>q, every nonconstant irreducible Y-factor over K(X) is separable. Thus one can factor the primitive part of A_r as ∏G_i^e_i, and the product of distinct factors has nonzero discriminant and smaller Y-degree whenever repetition occurs. This supplies a potential lower-degree helper, but its contact must be rederived: replacing a power by its radical can lose all but a 1/max(e_i) fraction of the root multiplicity. The original Φ bound cannot simply be transferred to that radical. Nor does the smaller degree alone establish the required normal ledger bound.

Without p>q there is a further inseparable obstruction: Y^p−X is irreducible in K(X)[Y] with zero discriminant and has no lower-degree factor over that coefficient field. For example F=(Y^p−X)(R−1)+Y−X is again a primitive irreducible regular equation with solution P=X. The benchmark degree guard excludes this particular inseparability issue, not ordinary repeated factors.

## Supporting-line numerical certificate: independently PASS

Read `better_codes_kernel_base_factors/newton_discriminant_gate.json` and independently recomputed all68 local ranks using explicit sums over each monomial rectangle and its shifted kernel rectangle, rather than the generator's closed box formula. Every rank, Φ value and rational slack identity agrees. Under the separately established own-system dimension inequality and sum ord(lc_Y A)≤12, the supporting line yields the exact ceiling229763340. The upper236715234 and residual6951894 are correct. This check does not strengthen the nonzero-discriminant hypothesis or supply a normal-term charging theorem.
