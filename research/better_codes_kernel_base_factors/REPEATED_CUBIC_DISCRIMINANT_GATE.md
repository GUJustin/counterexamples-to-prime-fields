# Cubic repeated factors: exact small-discriminant costs and a surviving profile

Status: bounded branch completed. The Newton/discriminant and own-rank resources alone do NOT exclude a cubic factor repeated13 or14 times. An explicit locally compatible profile also meets the along-candidate helper degree budgets. This is not a global polynomial counterexample.

Use the binding constants from REPEATED_QUADRATIC_DISCRIMINANT_GATE.md, and characteristic>43 (the target satisfies this). Let A=G^e H with deg_Y G=3, e in{13,14}, h=43-3e. Weighted additivity forces wtG=3w; normalize G monic in Y over k(Z). Then deg_X DiscG<=6w. Outside at most12 zeros of lc_Y H, A is monic up to a unit, contact a<=43, and all local root valuations are nonnegative. Write delta=ord_x DiscG when the discriminant is nonzero.

## Exact local cost table

The following lower bounds are sharp as local Newton-support bounds:

|e|delta>=0 range|delta>=1 begins|delta>=2 begins|delta>=3 begins|delta>=6 begins|
|---:|---:|---:|---:|---:|---:|
|13|a<=17|18|30|31|43|
|14|a<=15|16|28|30|42|

Equivalently the largest contact compatible with costs0,1,2,3,6 is respectively

    43-2e, 55-2e, 43-e, 55-e, 43.

Here is a direct proof without a general root-slope assumption. If G has at most one root at the received symbol, the multiplicity in A is at most e+h=43-2e. Thus larger a forces delta>=1. If delta=1, exactly two roots specialize there, with valuations1/2,1/2; the third is a unit. Their3e copies in A have total valuation e, so NP_A(h)<=e. The required ordinate a-12-h then gives a<=55-2e. If a>43-e, all three roots must specialize to the symbol.

For this last case translate the symbol to0 and write G=Y³+bY²+cY+d, with all three coefficients divisible by t. The discriminant formula gives an exhaustive classification below valuation6:

* ord d=1: the term -27d² uniquely has smallest valuation, so delta=2 and all three roots have valuation1/3.
* ord d>=2 and ord c=1: -4c³ uniquely dominates, so delta=3; the roots have valuations1/2,1/2,k for an integer k>=1.
* ord d=2 and ord c>=2: -27d² uniquely dominates, so delta=4 and all three roots have valuation2/3.
* Otherwise ord(b,c,d)>=(1,2,3), and every discriminant term has valuation at least6.

The delta2 case has NP_A(h)<=e, contradicting the required half-bound (a-h)/2>e once a>43-e. In the delta3 case, selecting the2e half-valued roots gives NP_A(h+e)<=e, requiring a<=55-e. In the delta4 case all G roots together give NP_A(h)<=2e, again requiring a<=55-e. Therefore beyond that threshold delta>=6. There is no unaccounted delta5 cancellation branch: in each of the first three cases the lowest discriminant term is unique.

For local sharpness one may take H=(Y-t^N)^h for large N, and use respectively G=(Y-t^N)(Y-1)(Y-2), (Y²-t)(Y-1), (Y-t)(Y-2t)(Y-1), or (Y²-t)(Y-t^N). For the final cost6 use three distinct roots proportional to t and likewise put H's roots proportional to t. These examples refer only to the local leading coefficient, not to a global universal source.

## Finite rank optimization

The exact LP maximizing sum R(a) over n good nodes with the above costs and sum delta<=6w has values

* e13:7749236943045, attained by contacts29 at3 nodes and42 at262141 nodes;
* e14:7351998045040, attained by contacts15 at2 nodes and41 at262142 nodes.

Both exceed the necessary own-system lower bound6802316684344, even without spending the12 exceptional-node allowance. The script enumerates all pairs of contact states using rational arithmetic; a one-budget finite LP has an optimum on such a pair.

## Stronger feasible profile, including helper intersections

At262142=n-2 nodes take contact40 and discriminant valuation3. At the remaining2 nodes take contact0 and valuation0. Then

    sum delta=3(n-2)=786426=6w,
    sum R(a)=(n-2)R(40)=6965732643688
                       >6802316684344.

The contact40 local data is realized explicitly:

    G=(Y²-t)(Y-t),
    H=Y-1                     (e14),
    H=(Y-t)²(Y-1)²            (e13).

The script expands A=G^e H over the integers and checks that the minimum of u+k+min(u,12) over its nonzero t^uY^k coefficients is exactly40. DiscG=4t(t²-t)² has order3. Along a generic agreeing candidate Y=ct+O(t²), c!=1, G has order2, while H has order0 for e14 or2 for e13. On181275 agreement coordinates these totals are362550<=3w and respectively0 or362550<=h w+12. Thus the previously proposed helper-degree inequalities also remain feasible.

These local germs and numerical budgets do not assert that a single bounded-weight global G,H, let alone a universal source F, realizes the profile. A further global compatibility, ramification, or own-system constraint is required to close this branch. The present certificate precisely identifies the surviving case: a widespread local quadratic ramified pair plus one integral root, with discriminant valuation3.

Artifacts: repeated_cubic_discriminant_gate.py/json. No parameter scan or asymptotic inference was used.
