# Bounded Taylor-order trade at the binding singleton

We tested whether increasing k can lower the graph charge through the divisor k+1, rather than just changing B/U/s/m/L. The target remains agreement181275, group11, contact(r,v,z)=(12,43,3206), total3261.

For the paired change (k,n0)→(k+1,n0+1), the budget flag changes by (0,1,0): its all coordinate B−2(n0−k−1) is preserved, while the yz coordinate increases by1. The graph contribution is divided by the larger k+2. However, the source coefficient budget loses weighted degree. At h=n0 the reserve changes from k to n0, and for h>n0 it increases by1. The local rectangular rank bound is independent of k,n0. Thus the exact surplus slope and required L must be recomputed.

First, with all other geometry frozen, we examined dk,dn0∈[-2,2], subject to source conditions. No candidate that activates at the contact improves its actual max-of-four root bound. The paired +1,+1 changes behave as follows:

| Source | Result |
|---|---|
| 21 | The sufficient closed-rank cutoff cap becomes150, below U151 |
| 5 | The sufficient closed-rank cutoff cap becomes214, below U215 |
| 22 | Positive kernel requiresL4814 and activationz4760, after the contact |

The first two failures are limitations of the retained sufficient formula, not impossibility results for arbitrary interpolation arguments.

Second, we attempted to repair these gates in a bounded neighborhood: dk∈{1,2}, dn0∈{0,1,2}, dm∈{0,1,2}, dU∈{−2,−1,0}; B,s remain fixed. Among126 shapes surviving the initial source conditions, none activates at the contact. The smallest feasible L found for sources21,5,22 is respectively20660,4842,4814. The first even exceeds the retained root domain total7501. For every positive-surplus case the minimumL is solved from the exact affine count-minus-rank expression and its positivity is checked directly.

These candidates are rejected before identity absorption/characteristic checks, so they are not presented as full replacement profiles. The earlier-active candidates from the frozen scan are ranked by their complete rounded root envelope; none improves the existing contact. This establishes only the stated finite-neighborhood result, not global optimality over Taylor order or support shapes.

Reproduction: `auxiliary_taylor_order_probe.py` and `auxiliary_taylor_gate_repair.py`, with corresponding JSON outputs and standard384MiB/60second resource reports. No catalog mutation, receipt change, or Lean theorem claim was made.
