# Exact decomposition for the modular collision target

Let D=mu_256 minus {1}, m=255, r=136. The signature of a subset is its first six power sums and its product, in F_p. Since p>6, the power sums encode the same leading coefficients as the original signature. For t>=0 let E_t count ordered pairs (A,B) of disjoint t-subsets of D with equal signatures. Then the full ordered collision count is exactly

    sum_signature L_signature^2 = sum_(t=0)^119 E_t * C(255−2t,136−t).

Proof: uniquely decompose any ordered equal-signature pair (U,V) as U=C union A, V=C union B, where C=U intersection V. Additive moments and the nonzero common product cancel. Conversely every ordered disjoint exchange (A,B) has exactly C(255−2t,136−t) admissible common parts. E_0=1.

Moreover E_t=0 for 1<=t<=7. Newton identities determine the first min(t,6) elementary coefficients; for t=7 the common product also determines the remaining constant coefficient. Thus two such t-subsets have identical monic root polynomials and cannot be disjoint and nonempty. At t=8, the first possible exchange, the two degree-eight monic root polynomials must differ by cX with c nonzero.

This reduces a possible collision certificate to genuinely modular disjoint-exchange counts. It does not establish excess collisions: the weighted sum still has to exceed N*(274980728111395088−1), with N=C(255,136). Small exchanges alone are not asserted to dominate. The exact identity and zero layers were independently enumerated on three small finite-field examples by verify_exchange_decomposition.py/json. Those examples validate bookkeeping, not the large-field target.
