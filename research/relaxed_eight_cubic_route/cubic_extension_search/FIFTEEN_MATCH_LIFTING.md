# Fifteen-match cubic-cover candidates: fixed-source lifting gates

The parent search `full15.json` reports three canonical non-descended candidates of degree9 with15 matches on the48-node F289 cubic pullback. `lift15.py` independently verifies their exact supports and closes under deck C3 and Frobenius. Each orbit has size3, for9 distinct candidates in total; each orbit contains an F17-coefficient representative.

The exact rational source is the independently certified eight-cubic seed in affine coordinate U=1/(X-3). Its residue identification with the original F17 seed is

    q_i(U)=10(P_i(11-3U)-P_3(11-3U)).

Consequently the correct fixed rational cover is U=(11-T³)/3, and a raw candidate C(T) is normalized to10(C(T)-P_3(T³)). Testing a different source coordinate without this transformation would not test the desired lift.

## Fixed cover

In the unramified quadratic ring (Z/17²)[theta]/(theta²-7), lift each marked T uniquely by T³=11-3U_i, and lift word values from the exact rational table. Interpolate the candidate through the first10 of its15 matched nodes. These nodes are unit-separated, so the degree9 interpolant is unique. Every one of the9 candidates fails at one or more remaining nodes modulo17². Exact residuals divided by17 are in `lift15.json`.

## Varying covers

Write a general degree-three rational map as U=A(T)/B(T), with A degree<=3 and B=1+B1*T+B2*T²+B3*T³. The pulled-back received value is B(T)³*w_i, because the source sections have degree3. Candidate H has degree<=9. At each matched node impose

    A(T_i)-U_i B(T_i)=0,
    H(T_i)-w_i B(T_i)³=0.

The two-modulus cyclic family is represented by varying A0 and B3 after fixing domain scale; the general family has7 coefficient parameters minus3 domain-PGL gauges, hence4 moduli. In the eliminated-node linearization, ten candidate coefficients plus general-cover coefficients have rank14; cyclic two-modulus systems have rank12.

All cyclic-family candidates fail modulo17². In the general family, the first two deck/Frobenius orbits fail modulo17², but the third passes. `lift15_vary_cover.json` saves exact matrices and verified left-null obstructions.

For the F17-rational representative of the third orbit (case8 in `lift15.json`), retain the15 matched node variables explicitly. There are30 equations in32 variables: H0..H9,A0..A3,B1..B3,T1..T15. Fix A2=0,A3=11,B1=0; the remaining29-variable Jacobian has rank29. All30 equations lift and replay exactly modulo17². At the next digit the unique left-null compatibility equation has nonzero RHS7, so no correction exists modulo17³. `lift15_general_hensel.json` records the17² point, exact defect vector divided by17², and the left-null vector.

Thus no unramified characteristic-zero lift exists for any of these9 candidates with its exact support, even allowing a general degree-three rational map and keeping the rational source fixed. This is a local statement at these residue points. It does not exclude other15-match characteristic-zero branches or bad-reduction covers.

The remaining three tangent directions are expected to be precisely the domain-PGL action. A formal gauge-normalization argument may strengthen this to arbitrary ramification at these same points; that strengthening is not asserted here pending an independent proof/audit.
