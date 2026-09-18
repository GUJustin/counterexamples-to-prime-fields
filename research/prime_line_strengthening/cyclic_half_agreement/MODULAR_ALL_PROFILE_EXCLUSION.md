# Modular certificates for all q127 doubling-invariant cyclic profiles

The generator tests all38 first-support unit classes, all556 compatible representative target supports, and every twist h=64,...,126:35028 cases. Source S is the complement of C, target T has size63, and all definitions are recorded in doubling_profiles127.json. Multiplying exponent indices by a unit is a cyclotomic Galois automorphism, so first-support unit normalization loses no characteristic-zero solution.

For each split prime p, choose zeta of exact order127. Let B_S and A_T be the monic support locators, P=X^h mod B_S and v=X^h mod A_T. All these polynomials are cyclotomic integral before reduction. Select a pivot k with v_k nonzero modulo p. The remainder of P(alpha X) modulo A_T has coefficients u_j=P_j alpha^j−P_63 A_j alpha^63. Thus a common second-coset value requires every integral polynomial
E_j=v_k P_j alpha^j−v_j P_k alpha^k+P_63(v_j A_k−v_k A_j)alpha^63
(j!=k) to vanish. Every E_j has characteristic-zero degree at most63.

The exact factor H(alpha)=product_{t:T+t subset S}(alpha−zeta^t) divides every E_j by the first-support interpolation identity. Monic division preserves cyclotomic integrality. Hence E_j/H has degree at most63−degH, without assuming that the observed modular degree of P is its characteristic-zero degree.

At a prime above p, if some quotient attains this upper degree and their modular gcd is1, there is no characteristic-zero common root. Indeed the full-degree quotient has unit leading coefficient, so any monic common factor over the local fraction field is integral; its monic reduction remains nonconstant and divides all reductions, a contradiction. Consequently no allowed alpha (nonzero and alpha^127!=1) exists. H contains only forbidden same-coset roots.

Generator results: p509 certifies34848 cases; p2287 certifies all remaining180. All35028 output rows are accepted. The generator uses ordinary Euclidean gcd and records supports, twist, prime and root of unity so an independent implementation can reconstruct every equation. It does not merely test alpha values in the residue field.

Artifacts: modular_profiles.cpp, modular_profiles.in, modular_profiles.jsonl, modular_profiles.resources.json. Independent verification is performed by paley_exact/verify_modular.cpp, which reconstructs remainders and verifies extended-Euclidean identities rather than trusting generator polynomial data.

Scope: characteristic-zero exclusion for all cyclic two-coset constructions with both supports doubling-invariant at q127, degree63 and h>63. This does not exclude positive-characteristic exceptional constructions, non-doubling-invariant supports, different twist ranges, or noncyclic banks.
