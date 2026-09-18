# What is and is not optimized in the primary better.codes source

## Conclusion

The archived DKT staircase/full-prefix theorems do not prove optimality of the primary benchmark sources. They share the same local first-jet rank algebra, but their proved quarter-rate asymptotic threshold/cost conclusions are not the present finite primary-source/retained-factor ledger. The direct benchmark work had tested a few nonrectangular auxiliary wedges, not exhaustively optimized arbitrary primary supports.

This audit supplied a concrete exact min-cut formulation for the previously unoptimized primary-A subset problem. The first frozen-shape computation is now complete and negative: its global maximum sufficient surplus is exactly zero. This closes all Y-downward full-prefix subsets of that one primary shape, rather than only the rectangular support. It does not close other multiplicities, challenge caps, source roles, partial-prefix supports, or global dependencies between evaluation points.

## Primary provenance and terminology

The cached official `tmp/current-lower-primary-cache/LowerFoundation.lean` defines `globalExponents`/`globalCoefficientBox` near lines16120 onward by

    i+j+z<=L, j<=s, x+w*i+(w-1)*j<D.

Its local coefficient boxes and `contactRankBound` are near lines15780 and15999. `blockEntry` near line16185 explicitly replaces Y^i by terms (u0+u1 Z)^(i-f) a^f, f<=i, and preserves slope exponent j.

`MovingFiberSelection6811.lean` selects two interpolants from the TCap and B kernels. Source A separates factors dividing its ENTIRE kernel from complementary factors; it is not simply the selected QA polynomial. `full_A_divisor_mem_box` and `common_A_ys_le` near lines214--231 transfer the whole-kernel divisor into the existing caps. Positive nullity suffices for A; TCap requires a stronger nullity-versus-quotient-count statement to retain its total cap.

The number6802316684345 is the dimension of the binding factor's OWN system (weight55w, joint total3261, YR degree55, R degree12), not the coefficient count of primary A. Likewise (r,v,z)=(12,43,3206) are the routing coordinates of a possible factor, not a complete description of the primary interpolation support. One cannot optimize the unknown actual monomials of that factor as if they were a fixed interpolation source.

## Audit of earlier work

* `PRIMARY_A_REPAIR.md` exhausts stated rectangular cap grids, including the general local rank sum, and separately proves exactness of the unchanged one-point rank. It explicitly does not exclude arbitrary supports.
* `better_codes_new_mechanism/README.md` and `ROOT_WEDGE_AUDIT.md` genuinely test a nonrectangular benchmark support, i+kappa*j<=H. This is an auxiliary m1000,L60000,s310 source: seven wedges and one factor-degree partition are tested. Its negative result is not an exhaustive primary-A or Newton-polygon optimization.
* Exact-slab files sharpen quotient-image counts while retaining the existing source; they do not optimize its input monomial support.
* `optimize_prefixes.py` optimizes stored phase-ledger prefixes with sources fixed. These are not polynomial coefficient prefixes.
* `first_order_support_audit` and `current_graded_method_costs` prove broad full-prefix/downward-support results, including grouped sorting and nonmonomial extensions. Their integrated necessary fourth-power regular-family cost is at rate1/4 near the DKT threshold, under its stated declared-degree ledger. Here w/n is almost1/2 and A/n is about0.6915, and the objective is the finite primary/retained-factor certificate. It would be wrong to substitute those asymptotic statements for a finite optimality theorem here. Their exact local rank formula is nevertheless directly useful below.

## Exact finite primary-A target

Try restoring the old A caps at target agreement181275, without enlarging the factor context:

    n=262144, w=131071, m=115,
    D=m*A=20846625, L=274277, s=35, qmax=159.

Let S be ANY subset of the5130 pairs (i,j) with j<=35 and i+j<=159, closed under (i,j)->(i-1,j). Retain all monomials

    X^x Y^i R^j Z^z,
    0<=x<D-w*i-(w-1)*j, 0<=z<=L-i-j.

Its coefficient count is

    C(S)=sum_(i,j)inS (L-i-j+1)*(D-w*i-(w-1)*j).

Received-word translations preserve the source: lowering Y can increase Z but preserves the joint cap, while the downward-Y condition and full X prefixes preserve the remaining caps. At the zero point the extraction is onto each local block simultaneously: the monomial X^(ell-i)Y^iR^jZ^z supplies exactly block ell. Its required X coefficient is present because

    D-(w-1)*159=6495>115.

Thus no enclosing-box loss is needed. At fixed binary degree q and block ell the contact matrix is the first m-ell Taylor coefficients of a^i b^(q-i) along a=b. In characteristic greater than159, its Pascal/Vandermonde rank is

    min(m-ell, c_(q,ell)),
    c_(q,ell)=#{(i,j)inS:i+j=q, i<=ell}.

The exact one-point rank is therefore

    R(S)=sum_q (L-q+1) sum_(ell=0)^(114) min(115-ell,c_(q,ell)).

The sufficient uniform kernel surplus is C(S)-nR(S). It does not assume independence between different nodes; it uses their rank sum as an upper bound.

## One min-cut optimizes all these supports

For each monomial pair use a binary selected variable x_i. For every(q,ell), introduce z_(q,ell). With h=m-ell and K=n(L-q+1),

    K min(h,sum x_i)=min_(z in{0,1}) K[h*z+sum x_i*(1-z)].

A directed graph realizes this exactly: source-to-monomial capacity equals its coefficient benefit; monomial-to-auxiliary capacity K; auxiliary-to-sink capacity Kh. Add an implication edge (i,j)->(i-1,j) of capacity greater than the sum of all benefits. Source-side monomials are selected. Cut capacity equals total benefits minus surplus after minimizing the auxiliary variables. Consequently a maximum-flow/minimum-cut equality certifies the global optimum over every downward support, not a scan or heuristic.

The graph has15827 vertices and261039 original edges. `mincut.cpp` found an empty-support optimum with

    flow=cut=total benefits=13123663101701085,
    max_S [C(S)-nR(S)]=0.

`verify_flow.py` is an independent plain-Python checker, not an optimizer. It reconstructs every edge, verifies every sparse flow amount against capacity, checks conservation at every internal vertex, computes the claimed cut, and independently recomputes the support count/rank objective. It PASSed all checks in0.54seconds using4.5MiB. Thus no support in this specified class supplies strict positive nullity at the frozen primary-A shape.

## Preferred interface if another shape succeeds

Keep the original FULL primary kernel. A positive-dimensional optimized-support subkernel embeds into it, proving the full kernel nonzero (or supplying a lower bound on its nullity). Equivalently, adding the omitted columns increases rank by at most their number. This preserves all full-kernel universality and own-system replacement lemmas; there is no need to redefine the primary kernel as the smaller source.

If instead one literally changes the primary kernel to an arbitrary support subspace, the newer own-system rigidity argument cannot automatically be reused: its replacement G^e H relies on multiplicatively additive degree caps, which an arbitrary staircase need not possess. The subkernel-witness interface avoids that problem.

Any successful future source witness would still require the appropriate generic Lean adapter and complete ledger regeneration; positivity alone is not a7.65% score improvement. TCap's stronger quotient-nullity condition and B's selection role must be preserved separately.

## Remaining concrete scope

No arbitrary-support global optimum has been proved across all primary multiplicities/caps. At the same m,D,j/q caps, a parametric-L extension can be checked by two further min-cuts: one at L=159 and one for the slope in L. If both maxima are zero, every support's affine-in-L margin is nonpositive for all L>=159. This is a precise next finite certificate, not a claim already established by the present frozen-L flow.

Other meaningful extensions include different m/D caps, the TCap nullity objective, and translation-stable partial X/Z prefix shapes with a newly proved exact extraction/rank formula. The current result neither licenses an optimistic quotient erosion nor improves the source-independent normal retained charge at the binding factor by itself.
