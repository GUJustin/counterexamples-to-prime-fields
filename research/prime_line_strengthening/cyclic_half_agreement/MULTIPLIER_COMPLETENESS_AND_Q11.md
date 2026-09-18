# Complete multiplier census and exact q=11 test

## Difference-set completeness for q=31 and 127

Let q=2^m−1 be prime (here m=5 or7), r=(q−1)/2 and lambda=(q−3)/4. For a cyclic (q,r,lambda) difference set D, set a=sum_{d in D} zeta^d in Q(zeta_q). The difference-set identity gives a conjugate(a)=r−lambda=2^(m−2). Consequently every prime ideal dividing (a) lies above2. The automorphism sigma_2:zeta->zeta^2 fixes each prime above2, since it is the Frobenius element in the decomposition group. Hence (sigma_2(a))=(a), and sigma_2(a)/a is an algebraic-integer unit. Every complex conjugate has absolute value1; Kronecker's theorem gives this quotient ±zeta^t.

The minus sign is impossible: reducing exponents moduloq, D(X^2)+X^t D(X) would be divisible by Phi_q, hence have all coefficients equal, whereas its coefficient sum is2r=q−1, not divisible byq. For the plus sign the same argument applied to the difference (coefficient sum0) gives 2D=D+t as actual subsets. Thus E=D−t satisfies2E=E. This invariant translate is unique: if E+s is invariant too, E+2s=E+s, so E has additive period s, forcing s=0 because q is prime and E is proper/nonempty.

The nonzero doubling orbits have size m. Since r is divisible bym, an invariant set of size r cannot contain0. Therefore every rotation class occurs exactly once among unions of r/m nonzero doubling orbits. The exhaustive census checks all20 unions forq31 and all48620 unions forq127, testing every nonzero difference (symmetry permits half).

Results: q31 has8 rotation classes, partitioned under unit multiplication into classes of sizes6 and2 (Singer and Paley). q127 has80 rotation classes, in SIX unit-equivalence classes of sizes18,18,6,18,18,2. Thus Singer and Paley alone do not exhaust q127. Full representatives and all normalized sets are in multiplier_census.json. This proof and enumeration do not rely on an unverified literature classification.

## Exact complete two-coset test at q=11

Use the construction and coverage hypotheses of CYCLIC_CONSTRUCTION_AND_SEARCH_AUDIT.md. Autocorrelation saturation requires lambda_C(d)+lambda_T(d)=r−1, with C the complement of the first matching support. The independently checked profile enumeration gives24 ordered canonical(C,T) pairs. For each and h=6,...,10, compute P=X^h modulo the first-support locator over Q(zeta_11).

For a fixed t0 in T define, for each other t in T,
G_t(A)=sum_j P_j A^j [zeta^((j−h)t)−zeta^((j−h)t0)].
A second coset exists over any characteristic-zero extension only if these polynomials share a root alpha with alpha!=0 and alpha^q!=1. Canonicalizing T by rotation is harmless because alpha ranges over all algebraic roots, not a second separately normalized set of representatives.

All120 exact gcds have no such root. The script records explicit Bezout combinations equal to each raw gcd, verifies those combinations exactly, and verifies the raw gcd divides [A(A^q−1)]^r. Thus every common root is forbidden. Artifacts: exact_profiles_q11.json and exact_profiles_q11_bezout.json.gz. Runtime3.88sec, peak65MiB. The q7 regression has12 cases and recovers exactly the two conjugate h5 positive families.

Scope: this excludes the specified degree5 cyclic two-coset construction over characteristic zero, including all compatible supports and all twists above degree. It does not exclude arbitrary eleven-word banks, positive-characteristic exceptional solutions, or different cyclic received-word mechanisms.
