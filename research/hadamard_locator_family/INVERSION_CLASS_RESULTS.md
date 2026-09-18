# Variable inversion-class reduction and two bounded seed gates

No eight-word realization was found. The exact positive algebraic progress is a rational parametrization solving ALL edge, all-plus, and internal-complement conditions; only the cross-pattern equations remain. Finite-field collision results below do not exclude characteristic-zero or extension-valued shape solutions.

## Rational internal-compatibility family

Set opposite edges to

    (e01,e02,e03,e12,e13,e23)=(1,b,c,q/c,q/b,q).

All six must be distinct and nonzero. The Ceva beta ratios simplify to

    beta=(0,q-bc,q-c,q-b).

The complementary slope equations admit

    a0=1, a_i=1+t*v_i,
    v_i=beta_i*(sum beta-2 beta_i).

All three H-complement equations have the SAME numerator. Put

    N=bc+bq+cq+q,
    M=b²c²-b²cq+b²c-b²q-bc²q+bc²+bq²-bq
      -c²q+cq²-cq+q².

On the nonzero-denominator chart they force

    t=-N/(qM).

All-plus compatibility then forces

    p=-q*(bc+b+c+q)/N,
    k=sigma*tau=(q-b²)(q-c²)(q-1)/(qM).

These identities are verified symbolically in inversion_gate.py/json and inversion_parameters.py/json. Eliminating k gives the common linear factor

    N*p + q*(bc+b+c+q),

multiplied respectively by cp+q and bp+q and proven nonzero edge-difference factors. Since b!=c and p,q!=0, the two extra factors cannot both vanish. Thus this p formula is necessary on the stated chart.

The chart N*M=0 is not removed by an existence argument. It remains a separate exceptional locus. The explicit all-plus pencil also uses C_i(-p)!=0; those charts are retained as unexamined exceptions, not silently saturated from a universal theorem.

## Four-variable exact residual system

After V=sigma*T and z=sigma², the eight sextics, up to a common nonzero scalar, have coefficients rational in b,c,q,z; adjoining sigma is not needed to define them in the V coordinate. For partition(0,i)|(j,l), the normalized node quadratic is

    V² + k*(beta0-beta_i)/(a0-a_i)*V + z*H0i/p.

The all-plus quadratic is V²-zV+pz. Edge quadratics are V²-z e_ij.

The six cross-remainder equations are reconstructed exactly over Q(b,c,q)[V,z] by inversion_cross.py. Each of the three remainders has nine monomials in V,z, with V degree at most1 and z degree at most4. The artifact retains their rational coefficient expressions. Computation took15.0sec and107MiB under the60sec/384MiB watchdog.

The degree28 domain locator is the product of six edge quadratics and each of the four transversal quadratics with its V-reversal. Its squarefreeness is essential; solving only the six residual equations is insufficient.

## Deterministic F29/F43 gates

inversion_search.cpp enumerates every nonzero ground-field triple(b,c,q), retains six distinct edges, the explicit nonzero denominators, and eight distinct leading coefficients ±a_i. It forms the six degree-at-most-four equations in z by direct small polynomial arithmetic, computes their gcd, and RETAINS every nonconstant gcd, including factors with no ground-field root. Zero gcds are also handled as identically vanishing systems.

Final runs do not require square edge values. Thus algebraic node candidates are retained, not merely fully split prime-field banks. All saved gcds happened to be linear:

| prime | triples | edge-guarded | leading-guarded | nonconstant z gcds | algebraically distinct locators |
|---|---:|---:|---:|---:|---:|
|29|21952|15600|8544|96|0|
|43|74088|59280|40944|240|0|

Every one of the336 candidates has deg gcd(K,K')=12. The failure is actual collision, not failure of rational splitting. Representative factorizations have six triple roots and ten other simple roots. No extension-valued z root was lost: all saved gcds have degree1. Extension-valued SHAPE parameters are not covered.

verify_modular_candidates.py independently reconstructs the eight sextics with FLINT, rechecks all-plus and cross-pattern divisibility, the leading guards, and the degree28 locator for all336 records. It confirms every collision degree12 in0.54sec. This independently replays candidates, not the completeness of the C++ negative-shape census.

## Scope and next meaningful step

The variable inversion class now has a precise six-equation/four-variable algebraic target. The two prime gates supply no valid point and no global characteristic-zero exclusion. Further prime sweeps are not justified by this evidence alone. A useful next step would be saturation of these exact residual equations by the locator discriminant, or a genuinely different general Ceva involution chart. Neither is completed here.
