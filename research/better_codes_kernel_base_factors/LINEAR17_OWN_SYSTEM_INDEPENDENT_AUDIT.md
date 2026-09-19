# Independent audit: linear-17 own-system exclusion

2026-09-19. PASS for the exact binding caps stated in
LINEAR17_OWN_SYSTEM_EXCLUSION.md. No complete ledger improvement follows.

Read the finalized exclusion proof, remaining-resource profile note, and
pure-Python certificate; independently replayed the certificate successfully.
Also recomputed the critical rational bounds independently before reading
the finalized checker. No floating-point optimization enters the proof.

The normalization and descent are valid: multiplicity greater than 12
forces the monic graph factor to have weight w. At least 182253 good
nodes with contact above 30 force the same graph identity; interpolation
on w+1 nodes gives P=P0+ZP1 over the original coefficient field. This is
needed to put the eventual helper in the original own system, not merely
a scalar-extended space with uncontrolled Z degree.

For Q=(Y-P)^43 times the stated locator, each graph node obtains at least
43 units of contact; every remaining contact deficit is supplied by the
locator. At nongraph nodes the locator supplies the full actual contact.
The helper is nonzero, has R-degree zero, joint (Y,R) degree 43 and
joint (Y,R,Z) degree 43. Its weight is at most 43w plus locator degree.
Thus the proved locator bound puts Q in W_F. The own-system identity
W_F=kF contradicts R-degree zero versus deg_R F=12. This is an outright
exclusion of a universal irreducible factor, not just candidate routing.

Bad-node accounting is sound: there are at most 12 bad nodes, their total
leading-coefficient order is at most 12, and a<=43+2b. Therefore all their
locator contributions together cost at most 12*43+24=540, while their
rank contribution is at most 12R(67). Zero-contact padding does not create
actual graph nodes and only relaxes the good-node rank bound.

For e>=18 all good nongraph contacts are at most 25. Independently checked
the pointwise rank inequality and the exact locator bound
5652585643980/3602417, whose integer part is 1569109. This leaves 3743
units below 12w. The same bound covers all multiplicities 18 through 43,
not only the exploratory range ending at 26.

For e=17 the centered H has degree 26. If H25=0, a nonzero received offset
cannot be a root of multiplicity 26, because its W25 coefficient would
be -26 B s. Both B and s are nonzero at a good nongraph node, and the
benchmark characteristic exceeds 26. Thus the preceding bound applies.
If H25 is nonzero, every good contact-43 node is a graph node and its
specialized W42 coefficient vanishes. That coefficient is exactly H25,
so there are at most deg_X H25<=w+12 such nodes. The corrected R42
baseline then gives locator bound 1152463886007/738980, integer part
1559533 and slack 13319. Independently checked all 44 contact states.

Two distinct graph factors of multiplicity at least 13 are also excluded:
each must equal the received symbol at the same 182253 high-contact good
nodes. Their difference has X-degree at most w, so the graphs coincide.
No assignment of disjoint graph-coordinate subsets evades this argument.

The separable quadratic-13 corollary is valid. The earlier coefficient
proof gives its affine centroid and H=(Y-Pc)^12 J5. At a good noncentroid
node, G can contribute multiplicity at most 13 and J at most 5, giving
contact at most 18. This is covered by the same h25 helper inequality.
Thus both nonzero-discriminant quadratic13 and its zero-discriminant
linear26 alternative are excluded at the stated exact caps, without a
selected-list hypothesis.

The remaining e13..16 resource profiles were checked too. They meet the
rank requirement and each stated centered-coefficient degree budget;
local Newton models meet the reported contacts. Their best graph-power
locator weights, over every permitted exponent 0 through 55, exceed the
own cap by the recorded positive amounts. These are compatible necessary
resources and local germs, not globally realized polynomials. In
particular they do not prove that no different helper or further global
compatibility argument can exclude these cases.

## Final artifacts audited

SHA256 values after independent replay:

- `LINEAR17_OWN_SYSTEM_EXCLUSION.md`: `9664445a894afc40d43f4a3455cc22a70af7a27d3a8fca4d658901967c81a70c`
- `LINEAR13_16_RESOURCE_LIMIT.md`: `b63ff1781292f477f446f098157059a53aa3eba3df6c6e8e350e419d79ab7251`
- `linear17_own_system_certificate.py`: `a5c6218a5deb5c18559c9084a10f9159c9049cbdb7b79c44214e845d388878b3`
- `linear17_own_system_certificate.json`: `c708282b95f132eabf52c740d570f30404eb0f72381bfa247ccaec5221ad5c77`
- `QUADRATIC13_CENTERED_COEFFICIENT_ROUTING.md`: `d0f77f3d474ab5bfc0602c0e3a541e4a0e60c5e7fdf0167d28bead290750c09f`
