# Independent review: fixed-involution packing

September 19, 2026. Root reviewed the general proof and replayed the
separate finite checker. The proof passes under its stated odd-field,
distinct-coordinate, selected-support hypotheses.

The coefficient functional annihilates each orbit's root quadratic. Its
representation by the two evaluation functionals has both coefficients
nonzero because a single evaluation functional would have zero
discriminant. Thus each pair belongs to a unique affine coefficient
plane, establishing the shared budget. Distinct pairs have distinct
agreement-line directions: dependence of restricted evaluations would
put the coefficient functional in their span, forcing exactly the same
involution pair. Three owned lines determine at most one triangle.

Within one plane every two-root difference is an involution orbit, and
its selected incidence multiplicity is at most R. Combining this with
the existing double-edge lower bound proves (4); solving the quadratic
and summing its positive parts proves (5) and (6). The parameter b is
positive since (T-1)^2>n-1 and T>=3 imply T^2>n. Also R>=1 for
3<=T<=n, so the displayed pair-count upper bound has the correct sign.

The finite replay passes 3,630 word/involution cases, with sampled words
and exhaustive quadratic and involution enumeration as specified in the
receipt. It is supporting evidence, not proof of the general lemma.
There is no improved counterexample, list exponent, or prime-specific
consequence established by this note.

Reviewed note SHA256: `55639027ebcc3e146efce4927d13b559785e0816393c2b114b9c294c860427b7`.
