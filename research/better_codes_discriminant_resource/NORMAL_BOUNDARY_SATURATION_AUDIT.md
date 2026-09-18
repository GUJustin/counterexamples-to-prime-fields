# Normal-ledger boundary audit: what C2 already removes

## Existing exact reduction

Pinned cached `tmp/current-lower-primary-cache/LowerFoundation.lean`, lines 22353–22410, defines `excessFactor`, `reductionMultiplier`, and

    reducedStep(F,P,s,b) = numeratorStep(F,P,b) - reductionMultiplier(F,P,s,b)*F.

The multiplier is formed explicitly from the top R coefficients of F and P and their Y derivatives. `numerator_sub_reduced_dvd` proves congruence modulo F. Lines 22802–22870 prove the improved R-degree bounds. The global reduced cut is defined at 36256; the carrier-congruence transport and its budget family appear at 46532 onward.

`LowerGeometry.lean`, lines 4036–4069, explicitly records the numerical change: at derivative order d the first-tail R cap drops from `(2r-1)d` to `2(r-1)d`. The other cumulative caps are unchanged. This is the C2 improvement already present in the repaired normal cost. It is not an available new d-fold subtraction.

The actual budget consumer constructs an `activeNestedUnitFamily` from support caps of the reduced cut (`LowerFoundation` 46575 onward). Its final scalar cap remains `flagMixed(carrier,reducedTail,rationalFlag)`. The proof uses affine regular components and grouped resultant factors; the displayed cap does not explicitly subtract the boundary component described next. Excluding separant-zero affine components from the indexed family is not itself a quantitative subtraction from that cap.

## A precise residual generic boundary lemma

Write

    F=A(X,Y,Z) R^r+B(X,Y,Z) R^(r-1)+...,
    q=1/R.

At the generic point of a component of A=0 assume A_Y and B are units and the characteristic is zero or exceeds 2d. The compactified carrier equation is A+Bq+O(q^2)=0. Thus q is a local parameter on the carrier and

    F_R = -B q^(-(r-2)) + lower pole terms.

For the implicit derivation D with DX=1, DY=R and DZ=0, differentiating the carrier gives

    Dq = -(A_Y/B) q^(-1) + regular terms.

Consequently D^jY has exact pole order 2j-1 for j>=1: starting from DY=q^-1, each step multiplies the leading coefficient by a nonzero odd integer and by A_Y/B. No cancellation occurs under the characteristic hypothesis.

The reduced numerator represents `F_R^(2d) D^dY` on the carrier. Its exact pole order is therefore

    2d(r-2)+(2d-1)=2d(r-1)-1.

The reduced flag allows R pole order 2d(r-1). Thus its compactified restriction still vanishes to order **exactly one** along this generic boundary component. The global-tail scalar factor involving X and d! is a unit at the generic point and changes nothing.

This identifies one residual generic boundary copy after the large C2 cancellation. It does not furnish a complete new flag-budget theorem: incorporating it requires revising the grouped projection/resultant degree bounds, including their compactification and boundary degrees. No numerical normal-cost subtraction is asserted here.

## Consequence for the new leading-coefficient geometry

At a generically simple component of A with B nonzero, the residual coefficient is one irrespective of the large derivative order d=131072. Singularities at finitely many X nodes, measured by the recent Newton/discriminant resource, do not increase this generic divisorial multiplicity. They might affect additional localized intersection corrections, but that requires a separate intersection calculation; a discriminant/conductor total cannot be inserted as a boundary multiplicity.

If A is repeated, or B vanishes along one of its components, the hypotheses fail. Those strata require their own normalization and pole calculation. The generic lemma is neither an exclusion nor a bound on all such strata.

Accordingly, the substantial universally predictable leading-R cancellation is already accounted for in C2. The one remaining generic boundary component is a precise potential refinement, but there is no present theorem converting the new contact/discriminant resource into the large normal-ledger subtraction needed at the binding cell. No benchmark improvement follows from this audit.

## Binding arithmetic: one copy is negligible

The exact archived `flag_mixed` implementation reproduces normal cost 352613725068219795 at

    p=(3206,43,12), q=(840433664,11272193,2883584),
    R=(420223244,5505110,1310743).

The formal one-unit improvement of the R cap, preserving the other cumulative caps, is q -> q+(0,1,-1). Its exact mixed-cost difference is **35955701882**. Even granting the larger change q -> q-(0,0,1), which also improves the other cumulative caps, saves only **45338775053**. These are sensitivity calculations, not a proved all-component replacement of the tail flag.

For a deliberately much more generous geometric bound, the one-copy boundary curve is A(Y,Z)=0, of ordinary degree at most t-r=3249. Bound the restricted coordinate section by its full total-degree cap sum(R)=427039097, ignoring the finer flag geometry. Ordinary plane Bezout bounds this one-copy contribution by **1387450026153**. This comparison assumes the generic-simple boundary setting above and a proper restricted section; it does not replace the routing proof. It is already much larger than the flag sensitivities and still supplies only 0.006594 percent of the required reduction **21042194961366305** (short by a factor exceeding 15000).

Exact arithmetic is saved in `normal_boundary_one_copy.json`. Thus pursuing the single generic residual boundary copy cannot close the benchmark gap. This avenue is stopped; a qualitatively larger repeated-boundary or global compatibility theorem would be needed before further ledger work is justified.
