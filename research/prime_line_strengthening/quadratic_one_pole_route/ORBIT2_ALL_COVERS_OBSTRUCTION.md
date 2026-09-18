# The orbit2 seven-bank: the remaining quadratic norm curve has genus three

Status: complete characteristic-zero exclusion for proper one-pole augmentation through a rational quadratic cover of the archived orbit2 bank. This uses the same necessary pole/stratum theorem as ALL_COVERS_NORM_OBSTRUCTION.md, but a different obstruction in the no-full-fiber case.

Use the exact number-field bank in `fano_seven/orbit2_independent_field_audit.json`, over K=Q(q), q³-10q²+3q+1=0. Its14 distinct affine nodes, cubic coefficients, word values, and incidence masks were independently verified previously. Reduce at q=4 modulo83. Every displayed denominator is a unit, all nodes remain distinct, and direct evaluation of the seven reduced cubics recovers exactly the archived masks.

The full/empty incidence census has1,1,54,276 patterns for f=0,1,2,3. The norm relation has coefficients of degrees at most(1,4-f,7-2f), evaluated at14-2f fixed transformed values. All f>=1 matrices have full column rank modulo83: respectively12,9,6. Their selected nonzero minors therefore exclude those strata over K and every characteristic-zero extension.

For f0, the14-by15 matrix has rank14. Its normalized kernel, in column order A_0,A_1,B_0,...,B_4,C_0,...,C_7, reduces to

    (25,29, 70,79,46,41,78, 42,55,73,73,50,23,69,1).

In contrast to the Paley bank, A is nonzero. The discriminant B²-4AC is

    -8X^8+35X^7+36X^6+28X^5-13X^4-21X^3-3X²+24X+36

modulo83. It has degree8 and is squarefree. The saved certificate explicitly supplies polynomials S,T over F83 such that

    S*Disc + T*Disc' = 1.

This is enough for a rigorous characteristic-zero conclusion without printing the large exact kernel. The chosen14-by14 minor is a unit at the prime q=4 above83. Set the remaining coordinate to1 and solve by Cramer's rule. The resulting exact K-kernel generator is integral at that prime and reduces to the displayed vector. Its discriminant has degree8, since the leading coefficient remains nonzero, and is squarefree, since the resultant with its derivative is a unit by the modular Bezout certificate. Hence its quadratic function field has geometric genus3.

A proper quadratic-cover witness would make v generate K(U)/K(X), by the pole argument in the general theorem. Its primitive norm relation must span this one-dimensional kernel, so K(U)=K(X,v) would be the genus3 function field. But K(U) is rational, of genus0. This contradiction excludes the last stratum. Multiplying the relation by a scalar changes the discriminant by a square scalar and does not change the conclusion.

## Independent verification and artifacts

`orbit2_prepare.py` evaluates the exact archived number-field bank and recomputes its masks. `orbit2_norm_gate.py/json` records all332 matrices and rank minors. `orbit2_verify_norm_gate.py` independently reconstructs the bank reduction and complete incidence-pattern set, rebuilds every matrix with polynomial Lagrange interpolation, and replays all332 selected minors by exact integer Bareiss elimination. It separately computes and verifies the discriminant Bezout identity. Both checks PASS.

Certificates are `orbit2_norm_independent_verification.json` and `orbit2_discriminant_certificate.json`. The entire calculation is a small linear-algebra/Bezout certificate, not a cover scan or an inference from modular nonlinear ideal inconsistency. No conclusion about other seven-banks, unrelated eighth-word constructions, or asymptotic lists is made.
