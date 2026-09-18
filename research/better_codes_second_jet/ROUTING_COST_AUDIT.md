# Routing-cost provenance and restored retained-branch result

## 1. Conditional two-source helper formula

The exact primary statement used is `AsymmetricHelper.regularSeeds_count_le_left_intersection` in cached LowerGeometry.lean, near line14076. Its required hypotheses are:

- a regular irreducible left factor F of the current carrier;
- coprimality of F with the proposed helper;
- left and right Y,R,Z degree caps;
- positive left R cap and left/mixed characteristic bounds;
- distinct evaluation coordinates, candidate degree≤w and agreement≥A;
- the existing `NoLargeSelectedPencil` condition;
- the helper specializes identically to zero for every candidate counted in the left regular-seed set.

It does NOT require the helper to be produced by a first-order interpolation source or to satisfy its source contact/root budget. Therefore a nonzero coprime resultant already known to vanish on the candidates can be used directly. The missing factorwise avoidance premise remains substantive.

For right caps (353,80,11029), the exact critical-context cost is47,911,200,271,295. Reproducible evaluation of all5238 cached (r,v) contexts at both ends of their total-degree interval verifies every mixed characteristic gate; costs are monotone in that total degree. The maximum is427,895,671,772,928 at cumulative left caps (Y,R,Z)=(163,36,9678). Details are in conditional_resultant_contexts.json.

This is also a conditional aggregate bound for the regular factors if their cumulative degree sums obey those caps and every factor has a suitable coprime helper with the same right caps. The helper numerator expands into a homogeneous quadratic with nonnegative coefficients plus a linear form in the left caps. The quadratic part is

    4w(n−w)(Y*R*rightZ + Y*Z*rightR + R*Z*rightY).

Consequently it is superadditive on nonnegative caps; the linear terms add exactly. Summing floors cannot exceed the floor of the aggregate numerator. This does not count nonregular factors or prove that all needed helper witnesses exist.

Terminology correction:288,191,873,412,750,740 is the current critical singleton COST. The full target MCA allowance is274,980,720,453,263,170. Neither number is the conditional regular-helper count. Comparing the tiny helper value to the full allowance alone would not establish a score improvement.

## 2. Restored second-jet routing is present

The restored `SecondJetAsymmetric.numericBound` in SecondJetRefinements.lean takes the MAXIMUM of:

    proper asymmetric helper count;
    normal +131076*ceil(moving/(k+1))+coefficient helper count.

The second term is the retained divisibility branch, and must not be omitted. The old theorem uses agreement181353. Our arithmetic port sets A=181275 in every asymmetric helper numerator and gap; the normal and moving constants depend on fixed n,w and remain unchanged.

The script restored_route_cost.py independently reproduces the primary old fixture

    numericBound(10,37,2276,47,155,2255,21,5,7)=268923679246212987

before evaluating the repaired source profiles at the new target. This checks the full flagMixed expression, budgetFlag, rounding, and max of branches against the saved primary theorem.

## 3. Exact critical-contact outcome

At (r,v,z)=(12,43,3206), all four repaired source profiles activate and pass the arithmetic pair characteristic gates. Their costs are:

| Profile | Proper helper | Full retained/maximum cost |
|---|---:|---:|
| m108, L2557 | 179900392369286 | 518435692262946165 |
| m114, L2777 | 198873257629702 | 509590929180880563 |
| m116, L2721 | 198928618826265 | 510076044303133106 |
| m96, L2698 | 161616239624234 | 514348991244948394 |

The minimum is still above the current critical singleton cost288191873412750740. More decisively, the shared normal term alone is

    352613725068219795.

It already exceeds that current cost. Thus no optimization of B,U,L,s,k,n0 can improve this exact contact through the same restored retained bound: its source-independent normal summand is too large. This is a proof-level lower limit on this particular upper-bound expression, not a lower bound on the actual bad-label count.

A full envelope propagation of these four unchanged routing profiles cannot remove the binding singleton peak, because none lowers the value at that peak. Profiles might improve other contacts, but that would not by itself repair the localized final deficit. A useful next advance must reduce the retained normal geometry, avoid its branch through a proved alternative, or change the binding-factor route.

No new benchmark score or fully checked target Lean receipt is claimed.
