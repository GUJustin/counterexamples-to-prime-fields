# Independent audit of the binding primary/simple-tail model

**PASS.** Checked BINDING_CONTACT_SIMPLE_TAIL_MODEL.md independently, including
the exact pinned primary caps and the actual cleared-tail normalization in
the cached primary source. This validates a countermodel to eliminating the
binding carrier using primary contact resources alone. It does not construct
a target retained second-jet source or a bad-label bank.

Write W=Y-Z and K=k(X). After dividing by Lambda^10, the carrier is
Z^3261+f(R,W), where f_R(0,0)=1 and f(0,0)=0. In a factorization of f,
exactly one factor vanishing at the origin can occur, to multiplicity one;
otherwise every first partial derivative would vanish there. Eisenstein at
that irreducible factor proves irreducibility in K[R,W,Z]. The Y^55
coefficient is one, so the original carrier is primitive over k[X]; the
coordinate change W=Y-Z is invertible. Thus the claimed global irreducibility
has no constant-field or inseparability gap.

The exact degrees (R, joint Y/R, joint Y/R/Z) are (12,55,3261).
The exact weight is 55w=7208905. In the local first-jet substitution,
the two linear order-ten terms cancel, while the remaining order-ten
coefficient is Lambda'(x)^10(R^12+Z^3261), which is nonzero formally.
Hence every actual contact is exactly ten, and the charge is 45w=5898195.

Multiplication by W^108 gives actual contact118, exact weight163w=21364573,
R-degree12, joint jet degree163, and joint jet/challenge degree3369.
These fit the stated repaired primary caps (36,163,176421), and the
strict weight budget118*181275=21390450 leaves25877. This is a genuine
explicit source polynomial, so a source-dimension existence argument is
unnecessary; no claim that every primary source contains the factor follows.

At the selected point (W,R,Z)=(0,0,0), F_R=Lambda^10 is a nonzero element
of K. The linearized surface equation is R=(Lambda'/Lambda)W. The ODE
preserves the zero section and differentiates its linearized flow exactly,
giving linear part Lambda^(j)/Lambda times W for D^jY. In characteristic
zero or p>n the leading coefficient of Lambda^(w+1) is nonzero. Thus the
first omitted derivative has a nonzero W differential on the smooth carrier;
its intersection curve is reduced and smooth at the point, with multiplicity
one. Nonlinear R^12,W^55,Z^3261 terms contribute no hidden linear term.

The precise cached identities also agree with this argument:

* LowerFoundation.lean, iterate_Y_eq_numerator (line4564), expresses D^jY
  as the numerator multiplied by the inverse separant to power2j.
* globalTailCut_eq (line32249) adds the scalar (-X)^j to the numerator.
* The actual first-tail cut uses j=w+1.

At the generic-X point both F_R and X are units. Consequently the actual
cleared first-tail polynomial differs from D^(w+1)Y by a unit there.
Hasse normalization also differs by the invertible factorial (w+1)!.
These normalizations preserve the nonzero differential and multiplicity one.

The example concerns a single chosen primary source and a single regular
selected seed. Its received line consists of codewords. It supplies neither
universal primary-kernel divisibility nor the missing target second-jet
retained-source conditions. Those additional hypotheses remain available
to a stronger geometric theorem, and no benchmark result is disproved.
