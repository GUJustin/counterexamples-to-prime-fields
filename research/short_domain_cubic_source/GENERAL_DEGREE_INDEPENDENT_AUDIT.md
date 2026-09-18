# Independent audit: arbitrary fixed value degree, zero-dimensional critical ideal

Verdict: **PASS**, including the stated constants and the repeated-constant-fiber corollary. This audit concerns GENERAL_DEGREE_ZERO_DIMENSIONAL_LIST.md only; it does not remove the zero-dimensional hypothesis from the list theorem or classify the exceptional pencils. The vague perturbative Bezout paragraph was replaced with the direct actual-bidegree argument below.

## Valuation lemma

Write F_u(P+Z)=b product_i(Z−delta_i), with b−1 roots counted with multiplicity. Nonzero A=F_u(P) makes every delta_i nonzero. In one fixed extension of the base valuation choose delta of maximum valuation. For the coefficient c_j of Z^j, every term of c_j delta^j is, up to a nonzero constant, A times j ratios delta/delta_i. Hence its valuation is at least v(A), regardless of cancellation. Multiplication by delta and division by j+1 give

    v(F(P+delta)−F(P)) >= v(A)+v(delta)
                           >= b*v(A)/(b−1).

Only integers1,...,b are inverted; characteristic zero or p>b is sufficient. Repeated roots and ramification cause no problem. At infinity the same argument chooses minimum degree and reverses the valuation inequality. No degree-D characteristic restriction is used here.

For fixed x, the b−1 critical roots of F_u are fixed algebraic functions in one chosen valued algebraic closure. Each quotient F(r)/H has at most one finite residue. Thus at most b−1 distinct labels have excess at that x, even though different sections may select different roots. The same argument gives at most b−1 exceptional labels at infinity. The strict thresholds d>(b−1)m/b and deg(A)<(b−1)N/b are correctly translated into the floor and ceiling formulas.

## Critical length and local charging

If A vanished identically, differentiation of F(P)=cH would put the entire graph of P in the original critical ideal. Its zero-dimensionality therefore ensures A!=0. On that graph the second critical generator is −H A P', so the local graph quotient of the critical algebra is precisely the local ring modulo A. Its length is ord_x A; this is bounded above by the local critical intersection length.

Homogenize each generator to its own actual bidegree. Neither contains a boundary divisor. Any common projective curve must meet the affine chart, contradicting the hypothesis. The proper intersection bound is therefore

    ell <= ((b−1)D)*b + (b−1)*(N+bD−1)
         = (b−1)(N+2bD−1).

This avoids any generic-perturbation assertion. It also covers degree drops by using actual bidegrees first.

One section is selected per nonzero nonexceptional label. Away from H, different labels cannot use the same critical point. At a root of H, at most b−1 selected labels have positive excess. Charging each excess by its local critical length gives total cost at most(b−1)ell. Counting every section in the same fiber would invalidate this step; the note correctly postpones the factor b until after counting labels.

The per-section lower cost is

    ceil((b−1)N/b)−sum_x floor((b−1)m_x/b)
      >= r_H−floor(N/b) >= r_H−D,

where N<=bD follows from one nonzero-label section. The b−1 exceptional labels plus the zero label contribute at most b² sections. The remaining factor is

    b(b−1)ell <=3b²(b−1)²D.

This verifies the bank bound exactly, including the cubic specialization108D.

## Arbitrary-word conversion

At coordinates outside H, a matched word value fixes the constant label, and each label has at most b sections. Thus La<=Lr_H+bn. If L>max(b²,b/eta), the resulting signed inequality r_H>D licenses the bank bound. Expanding

    (L−b²)(eta−b/L)<=3b²(b−1)²D/n

and discarding its positive b³/L term yields the claimed upper bound

    L<=floor[b²+(b+3b²(b−1)²D/n)/eta].

The small-L cases are dominated by this same expression. Applying the finite-subset argument also excludes an infinite family.

## Structural corollary

A positive-dimensional critical component is nonvertical because F_u has nonzero constant leading coefficient b. A generic critical root r has degree d<=b−1 over k(X); under p>b(b−1)D its extension is separable. The weighted monic derivative equation makes r integral at finite places and bounds its infinity poles by D times ramification.

For v=F(r)/H, the critical relation gives v'=0, and the pole-divisor estimate is

    h(v)<=dN+d*max(bD−N,0)=dbD<=b(b−1)D.

In characteristic p, the derivation kernel is L^p because the constant field is perfect and X'=1. A nonconstant pth power has height at least p, contradicting the strict bound. Thus v is constant; in characteristic zero the conclusion follows directly. The minimal polynomial of r divides both F_u and F−cH, proving a repeated u-dependent factor over the algebraically closed constant extension.

The corollary is a necessary structural condition for violating the list bound, not an isotriviality or rational-root classification. The characteristic inequality is strict and the constant c need not descend to the original constant field.
