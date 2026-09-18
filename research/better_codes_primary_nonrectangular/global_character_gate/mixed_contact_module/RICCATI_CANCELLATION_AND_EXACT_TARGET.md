# Received-word-dependent mixed contact modules

## What is new, and what is not

A three-graph Riccati determinant gives a concrete cancellation helper with derivative degree one and graph degree two. It is not a product of candidate graphs. The exact nonsymmetric example below has a one-dimensional contact kernel where the displayed full source and sum of local ranks are both 30. However, deleting the unused YR support makes the ordinary full-prefix dimension test positive already. Thus this example is **not an escape from the optimized monomial-support barriers**, and it supplies no better.codes improvement. Its useful outcome is an explicit module whose cross-triple cancellations can be tested without confusing the number of determinant presentations with the number of independent source polynomials.

## The exact multiplicity-two global ideal

Let S(X) be the squarefree node locator, f(X) its received-word interpolant, U=Y−f(X), and V=R−f′(X). For the contact substitution X=x+t, Y=f(x)+tR+t²E, the multiplicity-two kernel ideal in k[X,Y,R] is exactly

`J₂=(S², SU, U², S′U−SV)`.

At each selected point, S is a local parameter times a unit. To first order U=tV, while S=tS′(x), so the displayed generators have contact at least two. Conversely the local kernel is `(t²,U−tV)`; localizing the displayed global ideal gives that ideal. Both ideals are supported over the squarefree divisor S=0, so their equality follows by the Chinese remainder decomposition. This description is received-word-dependent and mixes X,Y,R. It is outside a jet-only translation degeneration, but a raw generator weight is not a minimal weighted source degree: syzygies can cancel its largest X terms.

There is also an exact finite-dimensional rank formulation. Write a capped source as `F=Σ_{j=0}^s R^j F_j(X,Y)`, with coefficient spaces V_j. Let I be the ideal of the received plane points and let

`T_j = {( (∂X F_j)(x,f(x)), (∂Y F_j)(x,f(x)) )_x : F_j∈V_j∩I}`.

Write these two n-vectors as a_j,b_j. Multiplicity two is precisely

`a_0=0, a_j+b_{j−1}=0 (1≤j≤s), b_s=0`.

Consequently the kernel dimension is the sum of `dim(V_j∩I²)` plus the dimension of this chain space inside the product of the T_j. This is an exact global cancellation optimization, not a sum of independently declared local ranks. Source caps enter through V_j; the two gradient coordinates must not be optimized separately.

## Three-graph determinant and an exact example

For three degree-at-most-w candidates define

`D₁₂₃ = det[(1,Y,Y²,R); (1,P₁,P₁²,P₁′); (1,P₂,P₂²,P₂′); (1,P₃,P₃²,P₃′)]`.

Its weighted degree for weights `(1,w,w−1)` is at most `4w−1`; its Y-degree is at most two and R-degree at most one. It has contact at least two at every coordinate where two of the three candidates match the received word. To see this, subtract one matching graph row from the variable row and the other matching row. The Y-difference in each is t times its R-difference modulo t², while their Y²-differences are 2f times their Y-differences modulo t². The determinant therefore has no terms of contact order zero or one.

Take

`P₀=0, P₁=(X−1)(X−2), P₂=(3/10)(X−3)(X−4)`.

Their six distinct pair-intersection coordinates are `1,2,3,4,−1,16/7`, with received values `0,0,0,0,6,18/49`. Each candidate agrees at four coordinates. Set w=2,m=2,A=4, strict weighted cap8, joint Y/R degree at most2 and R-degree at most1. The exact 30-by-30 contact matrix has rank29. Its nonzero kernel element is

`S(X)R + b(X)Y² + a(X)Y`,

where

* `S=(X−1)(X−2)(X−3)(X−4)(X+1)(X−16/7)`;
* `b=20(2X²−10X+11)/7`;
* `a=−(14X⁵−97X⁴+116X³+515X²−1456X+1016)/7`.

The standalone exact rational generator and replay are `three_graph_gate.py/json`. No R-free helper in this source can exist: restriction to each matching candidate has eight zeros counted with multiplicity but weighted degree at most seven, so it vanishes identically; all three distinct graph factors would divide it, contradicting Y-degree at most two.

The limitation is important. In the smaller support `{1,Y,Y²,R}`, at general cap4w there are `12w+1` source coefficients and only `4n` local rows. For n=3w the ordinary dimension count is already positive. The example does not contradict any optimized full-prefix barrier.

## Concrete remaining optimization and benchmark cost

For L given nearby candidates, form the polynomial-coefficient matrix C whose columns are the triple determinants D_ijk, in the ambient weighted box of degree at most4w−1. Let T select coefficients forbidden by a desired smaller weighted cap, and let M be the actual global contact map on this polynomial ambient space. The dimension of genuine allowable contact helpers in this determinant span is exactly

`rank(C) − rank([TC; MC])`.

This subtracts determinant identities automatically; counting the C(L,3) presentations without subtracting ker(C) would be spurious. The matrix can be assembled from candidate coefficients and actual agreement incidences. It is a precise, untested cancellation target; no large scan is justified without a list-size hypothesis that forces this rank difference positive.

At the benchmark w=131071 and A=181275, one raw triple determinant has weight at most524283 while multiplicity-two strict allowance is362550. Thus its worst-case weighted degree needs a reduction of161733, about30.85 percent. This is much more than merely the old primary-A row deficit of1,455,824,819,236. At m115 and derivative cap35, even the optimistic mixed construction of35 raw Riccati factors plus45 hypothetical contact-one graph factors costs24,248,100, exceeding20,846,625 by3,401,475. This is a cost of that construction, not a lower bound on all cancellation helpers. It makes clear what new cross-triple syzygy or higher-contact module theorem would have to accomplish.

The exact gradient-chain formulation is the strongest usable remaining optimization from this check. A benchmark claim still requires either a quantified large-list theorem controlling those global gradient images, or a genuinely cap-reducing identity among triple determinants. Neither is currently proved.
