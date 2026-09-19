# Quadratic multiplicity 13: strengthened local resources still permit the target

September 19, 2026. This decides a specific attempted improvement to the
frozen benchmark. It is not a globally realizable polynomial, source line,
or coding counterexample, and supplies no better.codes improvement.

Use the binding-shape definitions and exact rank function from
OWN_SYSTEM_RIGIDITY.md and CENTROID_DISCRIMINANT_ROUTING.md:
n=262144, w=131071, required agreements T=181275, characteristic
p=2130706433. Write the leading coefficient as A=G^13 H, with
Y-degrees 2 and 17. The required rank sum is 6802316684344.

At a good matching coordinate, put u=ord G(P), v=ord H(P), and let
a be the contact. Besides 13u+v>=max(ceil(a/2),a-12), selecting the
seventeen roots of H in the Newton polygon gives

    v >= max(0, ceil((a-26)/2), a-38).

Indeed the sum of the smallest seventeen root valuations of A is at
most the sum over these selected roots, namely v. The Newton support
lower bound at Y-degree 26 is the displayed expression. The leading
coefficient is a unit at the good nodes. Budgets for finite u,v presume
the corresponding along-candidate polynomials are not identically zero;
identically zero branches require separate routing arguments.

Even stronger coefficientwise local Newton constraints admit the
following integer profile. Unmatched rows do not spend the two
along-candidate value budgets.

| Matches? | a | ord Disc G | u | v | Count |
|---|---:|---:|---:|---:|---:|
| Yes | 30 | 0 | 1 | 9 | 53342 |
| No | 42 | 1 | — | — | 80869 |
| Yes | 42 | 1 | 1 | 17 | 74593 |
| Yes | 43 | 2 | 2 | 9 | 25813 |
| Yes | 43 | 2 | 3 | 9 | 27527 |

The node and agreement totals are exactly n and T. The discriminant
budget and matching G-value budget both equal 262142=2w. The matching
H-value budget is 2228219=17w+12. The rank sum is 7009938620360,
exceeding the required value by 207621936016, with no exceptional nodes.

These are not merely feasible abstract orders. At the candidate value
Y=0, explicit local germs for the four matching states are

    a30: G=(Y-t)(Y-1),       H=Y^17-t^9;
    a42: G=Y^2-t,           H=(Y-t)^17;
    a43,u2: G=(Y-t)(Y-2t),  H=Y^17-t^9;
    a43,u3: G=(Y-t)(Y-t^2), H=Y^17-t^9.

The unmatched state may use the same a42 germ; its value orders are not
charged to the selected agreement set. The checker expands G^13 H
over the integers and checks nonzero coefficients modulo the actual
prime. For every germ, the minimum of i+j+min(i,12) over nonzero
t^i Y^j terms is exactly a. Thus the full leading-coefficient Newton
support holds, including every partial-root consequence; this is
stronger than checking only the displayed total H-order inequality.

Root reviewed the valuation argument, explicit germs, and budget scope,
then replayed quadratic13_joint_resource_check.py. It uses exact integer
arithmetic and writes quadratic13_joint_resource_check.json. No floating
point optimizer is needed to verify the exhibited profile.

This does not exhibit compatible global G,H or a universal contact
polynomial. The missing ingredient is a further global compatibility
condition or another independent resource. Existing rank, discriminant,
local Newton support, and the two value-degree budgets alone cannot
exclude this profile. It would be incorrect to treat the profile as
evidence of a large actual list or a soundness counterexample.
