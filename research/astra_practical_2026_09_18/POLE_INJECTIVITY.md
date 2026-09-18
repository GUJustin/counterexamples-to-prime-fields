# Injective pole labels preserve the factor-four counting target

Independently checked by audit_random_directions on September 18, 2026. This clarifies the existing rational-line construction; it is not a larger bank or an improved benchmark.

For the B1024 construction, let a family of L distinct 136-subsets share the six leading nonmonic coefficients and product of their monic support polynomials V_U(Y). Then V_U−V_V has degree at most129 and zero constant term. Therefore (V_U−V_V)/Y is a nonzero polynomial of degree at most128.

With reference V_0, define gamma_U=(V_0(alpha)−V_U(alpha))/alpha. For each pair U!=V, at most128 values of alpha cause gamma_U=gamma_V. Excluding the whole base field also ensures that the pole lies outside the packet domain and is nonzero. Consequently

    p + 128*C(L,2) < p^6

suffices to choose one alpha giving distinct labels for every member of the family. At L=274980728111395088 the excluded fraction is below5.172e−20; exact integer arithmetic is in POLE_INJECTIVITY_CHECK.json.

Thus a factor4.0097 improvement in the six-head-plus-product fiber size would survive conversion from witness pairs to distinct challenges. The existing68579341025511059 family is a line family, NOT a fixed-word list. A fixed-word compiler cannot be applied to it without addressing its nonzero direction; see ../better_codes_revisit_2026_09_17/SAME_DOMAIN_PADDING.md. This argument concerns the original algebraic line; benchmark premises and the required radius suffix must still be verified for any proposed improved construction.
