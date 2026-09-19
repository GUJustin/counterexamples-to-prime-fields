# Routing theorems: exact interface to a numerical ledger improvement

2026-09-19. Updated after the audited linear-17 own-system exclusion.
The exact-cap exclusions certify no positive numerical ledger delta by
themselves. They remove specified factorization patterns, but do not
supply a smaller unconditional normal cost.

## The exact inequality supplied by a routing theorem

The pinned definition in LowerFoundation.lean is

    NoLargeSelectedPencil(selected,Gamma,w,e)
    := for all degree<=w P0,P1,
       #{gamma in Gamma: selected(gamma)=P0+gamma P1} <= e+1.

Consequently, if existence of a universal factor F with property C(F)
forces every agreeing candidate onto one affine pencil, then

    C(F) and the routing hypotheses imply |Gamma|<=e+1.       (A)

In a proof branch assuming |Gamma|>e+1, no such F can occur at all.
This is stronger than merely lowering F's individual mixed-intersection
charge, but only under C(F). The pinned 6811 code uses e=80860, so (A)
is 80861 there. An agreement-181275 target port must supply its own
consistent pencil threshold; substituting e=n−181275 gives 80870, but
that substitution is not itself a completed protocol port.

For the new theorem C(F) includes exact own caps
wt(F)=55w, deg_(Y,R)F=55, deg_R F=12, deg_(Y,R,Z)F=3261;
leading-R Y-degree 43; and a quadratic leading factor repeated 13 times
with nonzero discriminant. Existing repeated-linear routing can replace
that last condition by its proved multiplicity range. A theorem about
these patterns says nothing about a factor with the same numerical flags
and a different leading factorization.

## Stronger exclusions now available

`LINEAR17_OWN_SYSTEM_EXCLUSION.md`, independently audited in
`LINEAR17_OWN_SYSTEM_INDEPENDENT_AUDIT.md`, strengthens the conclusion
for the same exact caps. A graph-power helper belongs to the universal
factor's own interpolation system but has R-degree zero. This contradicts
the own-system identity W_F=kF, since F has R-degree12. It excludes every
linear leading factor of multiplicity17 through43 outright. The same
helper excludes the separable quadratic-13 case after its centered
coefficient argument; the zero-discriminant case is linear26.

These exclusions need no NoLargeSelectedPencil hypothesis or selected
candidate agreement threshold. Consequently their valid use at the
universal-factor consumer is a direct contradiction branch, rather than
an e+1 pencil charge. Equation(A) above remains the appropriate interface
for results that establish only routing.

In the high-multiplicity classification at these exact caps, a single
linear factor of multiplicity13--16 remains unresolved; two distinct
linear factors of multiplicity at least13 cannot coexist. The compatible
necessary-resource profiles in `LINEAR13_16_RESOURCE_LIMIT.md` do not
realize global factors. Lower-multiplicity and squarefree patterns,
other caps and weights, and the unconditional complement charge also
remain outside these exclusions.

## Where a valid improvement would enter

The pinned proof consumer with the right hypothesis is
`tmp/current-lower-primary-cache/MovingFiberInitialBound6811.lean`,
`initialA_universal_singleBound`. It explicitly assumes F belongs to
`initialAUniversalFactors`, meaning F divides every reconstructed primary
kernel source. It currently transfers source caps and calls
`MovingFiberSingletonGeometry6811.factor_count_of_cover` to prove

    #(regularSeeds(F)) <= sheetSlope(j)*z + sheetOwn(j,r,v).   (B)

An adapter could split on C(F), apply (A) to a merely routable branch
or the own-system contradiction to an excluded branch, and use an
improved, proved bound on the complement. To lower the unconditional
right side of (B), the complement must have its own smaller bound or be
excluded. A classification that proves every factor in a numerical cell
is routable would also suffice. The quadratic-13 theorem alone provides
neither assertion for the complement.

This distinction matters for reuse. `factor_count_of_cover` and its
`raw_count` carrier option concern arbitrary regular factors with caps,
not necessarily universal primary-kernel factors. It is invalid to lower
their shared carrier option using a theorem whose proof needs universality.
Either keep a separate universal-factor receipt and consumer, or establish
the new inequality for every factor to which the shared receipt applies.

## The actual numerical term and its consumers

For r>=3,v>=2, `base_packing_audit.py:cost` uses f=(z,v,r),
(a,b,s)=(z,v−1,r−2), and the normal/carrier charge

    mix(f,reduced,normal) + 65539*mix(f,moving,cut),
    reduced=(2a*131072, 1+(2b+2)*131072, (2s+2)*131072),
    rational=(131074a,131074b+2,131074s+3),
    normal=rational+(0,0,131071),
    moving=(a,b+1,s+3), cut=rational+(0,131072,262144).

Here mix is the explicit mixed-flag polynomial in that file. A genuine
normal-cost improvement would need a theorem bounding the same active
seed/component incidence by a smaller expression, with all required
characteristic, support, pole and exceptional-component hypotheses.
Neither the centered-coefficient argument nor the stronger own-system
exclusion supplies a smaller normal vector or an inequality replacing a
summand of this expression for all remaining factors. Their valid outputs
are a pencil case or an exact-pattern contradiction, respectively.

`regenerate_singletons.py` imports this cost and takes the minimum over
eligible carrier, 16 root-group, and phase bounds. For each packing-sheet
slope it maximizes bound−slope*z over all critical points. Then
`replay_regenerated.py` rebuilds Bellman packing and inherited prefixes;
`finish_target_ledger.py` adds the repaired B/derivative/tail overhead and
checks every context against the protocol allowance. This is the concrete
chain an accepted replacement of (B) must traverse.

## Why the new subcase does not change that chain yet

The regenerated target has 5238 (r,v) rows: 1<=r<=36,
r+v<=163, and 0<=z<=9678−r−v. Its binding singleton is
(r,v,z)=(12,43,3206), so total degree is 3261 and Y/R degree is 55.
But these flags do not record the actual contact weight (the new theorem
fixes 55w), leading-R degree, discriminant, repeated-factor pattern, or
universal-kernel membership. The existing numerical consumer cannot test
C(F) from those flags. A row must cover all admissible factors in its cell,
including those outside C(F).

Inspection found no quadratic-13/centroid-certificate input in the current
ledger Python consumers or the pinned initial/singleton Lean consumers.
No carrier function, root envelope, phase potential, packing recurrence,
or protocol allowance changed when the new theorems were added. Their
exact certificates return coefficient contradictions, centroid counts,
and locator-cost bounds for specified leading patterns, not an
unconditional bound of form (B). Therefore rerunning the unchanged
ledger with this new note cannot certify a positive numerical delta.
This is an interface fact, not a claim that the old geometric bound is
mathematically tight on the unclassified complement.

## Concrete mathematical deliverable needed next

For the target primary source (m,q,s,L,D)=(118,163,36,176421,21390450),
with common-divisor total cap 9678, establish a complete alternative:
for every universal regular factor in the applicable source box,

    either all selected candidates lie on at most specified pencils,
    or #(regularSeeds(F)) <= B_new(r,v,z),

where the first branch has an explicit e+1 charge per pencil and the
second is genuinely smaller where the ledger binds. The theorem must
quantify the actual own-system caps and leading degree, not infer them
from one illustrative cell. A restricted theorem can still be useful if
its applicability is expressed by tracked data and all remaining cases
retain a proved charge in a refined packing receipt.

Only after this adapter is proved should numerical regeneration assign
new unconditional singleton values and propagate them through all 5238
rows, eight packing sheets, and 32 phases. The present frozen target
still needs 21042194961366305 total saving and has 2841 failing contexts.
Closing every high-multiplicity linear routing subcase would strengthen
the first alternative, but would not automatically prove the needed
complement bound or erase the full retained normal term.
