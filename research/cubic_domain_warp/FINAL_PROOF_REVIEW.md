# Final mathematical review before integration

Theorem `cw:punctured-line` and Lemmas `cw:irreducibility`, `cw:finite`, September 17, 2026.
Labels are used because the strongest construction now precedes the interval refinements.

- Absolute, not merely rational, irreducibility: the entire component
  argument is over the algebraic closure. Vandermonde independence
  holds there too. Triple base points are smooth because exactly one
  term of the derivative of one product survives. All base lines lie
  on one component; restricting it to a plane forces degree at least
  the entire degree. This excludes extra factors and multiplicities.
- Dehomogenization: the irreducible homogeneous polynomial is not W.
  For u>=2 its degree is u; for u1 the U coefficient is nonzero.
  Its affine chart W1 is nonempty and remains irreducible.
- Moment order: 3s original moments preserve s moments after a cubic
  map. Equality through s gives locator difference degree<=t-s-1=K;
  division by the common anchor gives degree<K. No off-by-one remains.
- Good parameter count: each collision of seed nodes is one affine
  line in the two-parameter plane, since the U coefficient is nonzero.
  No independence of these bad events is assumed. p>2m² suffices.
- Outside pair roots: common support factors are removed first, and
  then the common anchor is divided out. Remaining common factors have
  roots only on the core. The equivalence with the residual surface
  therefore also holds at the removed anchor, if it becomes padding.
- Uniform point-count input: primary Cor5.6 requires p>2d², satisfied
  since d<=t<=m and p>2m². Its constants are polynomial in degree.
  Summing over L choose2 pairs before averaging introduces no field-size
  condition depending on L; the multiplier is still B=1+o(1).
- Image estimate: after selecting one good map, the total second moment
  is <=LR+L(L-1)B. Cauchy–Schwarz yields M=LR/[R+(L-1)B]. This is
  <=R<=p-1, so the missing-label factor is nonnegative. Top-q images
  have mean at least M; arithmetic–geometric mean bounds their product.
- Complete coverage: independent NONZERO directions act transitively
  on the p-1 label universe. Expected missing labels<1 forces a choice
  with none, because the missing count is a nonnegative integer.
- Exact far point: w has monic degree t-1, every codeword degree<K<=t-1,
  and selected candidates already have t-1 core roots. Thus its maximum
  agreement on the entire final domain is exactlyt-1, excluding CA.
- Quantifiers: u>c2 permits beta near rho and a constant C in the stated
  open interval. All choices then stay fixed as p grows. Moment-range
  loss is O(loglogp), support exponent exceeds logp by a fixed proportion.
  Length is logarithmic, gap shrinks, relative separation1/u is fixed.
- Scope: actual global lists remain >p asymptotically; use3(s+1)
  original moments on unanchored threshold-t core subsets. No FFT-domain
  transfer, fixed-positive-gap superlinear result, or efficient witness
  enumeration follows from this argument.

Finite evidence is recorded separately. The primary arithmetic checker
and independent moment-box replay both pass for M127, M1279 and M9689. Geometry
checks cover small instances and identities; the proof above establishes
the all-field geometric statement. This is an internal mathematical review,
not a claim of external peer review or formal proof-assistant verification.

The new M127 certificate has n214,K107,m202,A109,q13, original3
moments, far separationeta/2 and prescriptionfraction<2^-12.
PrimaryGramlist151bits; independentanchored-boxlist137bits. Both
check the exact rational missing-label expectation (integer powers in
the independent implementation). The larger rows retain the simpler
quarter-missing proof. No floating-point comparison certifies coverage.
