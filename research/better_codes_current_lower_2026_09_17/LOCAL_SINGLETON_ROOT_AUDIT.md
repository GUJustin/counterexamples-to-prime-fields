# Root-side review of context-local phase sources

September 17, 2026. This is an applicability review, not a passing target
certificate or a completed Lean port.

The pinned MovingFiberRouting6811.lean theorem
`exists_strict_helper_split_of_batch_source_thin` quantifies its helper
characteristic gates and stage charges only over factors in the supplied
nonempty finite set A. It does not require those gates for every possible
factor in the global component box. For A={F}, its proper-subset conclusion
forces U to be empty, so it directly bounds the regular seed count of F.
There is no requirement to use the same auxiliary interpolation source
for different singleton factors.

This permits a source chosen for one numerical context (r,y,t), provided
ALL the following are retained:

- positive kernel-dimension lower bound at the target agreement;
- weighted shape bound and the original source multiplicity hypotheses;
- the contact-thinned power-band inequality, not merely positive nullity;
- feasible and terminal fuel, with fuel below the characteristic;
- positive remaining weighted cutoffs and the per-stage capacity bounds;
- HelperPairGates for every stage through that fuel at the actual factor;
- an upper charge for every stage cost, and the selected-line/no-large-pencil
  hypotheses required by the generic theorem.

With D=m*A_target and delta=A_target-w+1, the stage capacity inequality
is an equality before any harmless weakening:

  D-j*delta = (m-j)*A_target+j*(w-1).

For a fixed context, later helper caps L-j*t,Y-j*y,S-j*r only decrease.
The nonnegative mixed characteristic products and helper-count numerator
are therefore largest at stage zero. This justifies checking the actual
context's stage-zero products as a sufficient uniform-in-stage bound,
while separately preserving all routing/fuel conditions above.

The stage-zero charge can use actual r,y,t instead of the global maxima.
At fixed r,y, its regular-count numerator is affine in t: the only
variable agreement cap is 1+2*w*t, and it multiplies the fixed mixed
quantity y*S+r*Y. Thus an exact affine majorant in the singleton's z=t-y
coordinate is available. A source can be used only on the integer z-range
where its routing and characteristic gates hold; endpoints must enter
singleton-envelope reconstruction.

The current PhaseSourceSound wrapper uses global component caps and cannot
be reused unchanged for this purpose. A separate local singleton adapter
must invoke the generic theorem. Moreover the pinned theorem contains
incumbent agreement/error literals; the target-A generalization must still
be ported and proved. None of this review says that a candidate meets the
numeric gates or that its resulting ledger passes.
