# Frozen primary A: arbitrary downward-support deletion does not repair it

For the frozen caps

    n=262144, w=131071, A=181275,
    m=115, D=20846625, L=274277, Q=159, Smax=35,

the maximum interpolation surplus over **all** Y-downward full-prefix subsets of the5130 available jet monomials is exactly zero. The empty support attains this value. Consequently none of these nonrectangular deletions gives a positive-nullity interpolation certificate.

This is a finite exact optimization, not a wedge/rectangle sample. The local rank formula and graph proof are in `INDEPENDENT_FORMULA_AUDIT.md`. `mincut.cpp` builds15827 vertices and261039 original directed edges. The total coefficient benefit and certified flow are both

    13123663101701085.

The residual source-side cut is just the source vertex, with the same capacity, so its selected support is empty. `mincut.flow` records every nonzero original-edge flow as an edge index and integer amount; `mincut.json` records the cut and totals. Independent capacity/conservation replay passed in `verify_flow.py/json`: all261039 capacities, flow conservation, cut equality, support closure, and exact zero surplus were checked.

The bounded run completed in0.54seconds. The wrapper's instantaneous peak-RSS sample is not an accurate memory measurement; the job was capped at384MiB and60seconds.

Scope: these fixed m, L and jet caps, full weighted X and challenge prefixes, Y-downward monomial supports, and the exact sum-of-one-point-ranks dimension test. This does not exclude different multiplicities/caps, smaller coefficient subspaces with global cross-coordinate dependencies, or nonrectangular TCap/auxiliary-helper improvements. No full-ledger or benchmark improvement results from this negative gate.
