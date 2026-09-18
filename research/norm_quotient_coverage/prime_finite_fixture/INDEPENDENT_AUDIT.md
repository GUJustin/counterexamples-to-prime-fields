# Independent finite prime fixture audit

2026-09-18. **PASS.** `independent_ntt.py` imports none of the producer's code and uses no FLINT or floating-point arithmetic. It independently verifies the field, generator, tag geometry, all 65536 convolution coefficients, and the exact positivity inequalities. Runtime 2.153 seconds. Receipt: `independent_ntt.verified.json`.

## Exact character certificate

65537 is prime by trial division. Since its multiplicative order is a power of two and 3^32768=−1, 3 is primitive and is a nonsquare. The 1420 distinct tags are nonzero squares, omit the reserved tag1, and their supplied logs satisfy 3^e=3−a. Thus the factor indicator has 1420 distinct positions on the cyclic group of order65536.

The independent radix-two NTT modulo998244353 cubes its Fourier transform and inverts, producing the cyclic ordered-triple counts. Every true integer coefficient is at most1420²=2016400<998244353: fixing the first two positions permits at most one third. Therefore the modular residues uniquely equal the actual integer coefficients. All65536 agree exactly with the independently produced FLINT binary. Their sum is1420³ and maximum45723.

Their square sum is125113995212860. Finite Fourier orthogonality gives

    Σ_(χ≠1)|Σ_a χ(3−a)|^6
       =65536*125113995212860−1420^6
       =1052619325992960
       <710^6=128100283921000000.

Every summand is nonnegative, so each individual nontrivial character sum has modulus strictly below710. This is an exact integer proof, not a numerical Fourier screen.

For r712 and θ=r/1420, the fixed-cardinality Cauchy exponent with conservative bias710 is u=63012/355. The character prefactor is(65537−2)(1420+1)=93125235. Exact rational arithmetic verifies u^5/120>93125235; exp(u)>u^5/120 therefore proves the required Fourier error below1. Every nonzero field element is consequently represented by a product of exactly712 distinct factors3−a. No subset enumeration is required for this existential conclusion.

## Compiler and endpoint checks

The domain consists of the square roots of the1420 sampled tags and reserved tag1, giving2842 distinct nonzero coordinates. The pole3 is nonsquare, so X²−3 never vanishes there. For J1421, r712, m2, padding degreew0:

    f=(X^1424−3^712)/(X²−3),   g=−1/(X²−3).

The first source is monic degree1422. Root counting for f−h and 1+(X²−3)h bounds each source's agreement by1422 for deg h<1421. Interpolation in Y=X² on711 tags gives strict-degree witnesses attaining1422 common coordinates, so both individual and ordinary common agreements are exactly1422.

For each λ≠0, choose a712-subset with V_S(3)=−λ. The standard quotient witness has degree≤1420 and residual V_S(X²)/(X²−3), with exactly1424 zeros on the domain. Hence all65536 nonzero pencil labels qualify, while λ0 and the projective direction do not. For normalized mixtures(1−t)f+tg, precisely the65535 parameters t∉{0,1} qualify. This is near-threshold existence; it does not enumerate witnesses, classify lists, or prove a larger fixed-word list.

The moment proof and exact root counts supply a concrete finite certificate at rate1/2, source agreement1422, threshold1424, and prime alphabet65537. Its source gap is two coordinates; no larger-gap benchmark implication is claimed.
