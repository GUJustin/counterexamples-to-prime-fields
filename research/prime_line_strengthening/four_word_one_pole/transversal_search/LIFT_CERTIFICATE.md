# Independent exact deformation certificate

The five stored finite-field hits all pass the independent verifier `independent_lift.py`: thirteen norm equations, Jacobian rank thirteen, and every required open guard. The first hit alone suffices for a number-field construction. This note records the lifting argument and guard scope; the separate construction note gives the resulting six-word bank.

## Variables and equations

Order the fifteen variables as

    (a1,a2,a3,a4,a0,c,b,E0,E1,E2,E3,O0,O1,O2,O3).

Let e_i denote the elementary symmetric functions of the four a_i. The first equation is e3*a0-e1*e4=0. The original twelve base coordinates are y=±a_i*a_j, with edge value v=a_i^2+a_j^2. Their lifted word is W(y)=(y-a0)*v. Add the pole fiber y=a0, W=0.

Choose twelve of these thirteen fibers: retain the pole fiber and omit exactly one positive original pair coordinate. For each retained fiber impose

    (E(y)+b*W(y))^2-(y-c)*(O(y)-W(y))^2=0,

where E,O have degree at most three. All thirteen equations are polynomial with integer coefficients in the fifteen variables. The prospective numerator is N(T)=E(T^2+c)+T*O(T^2+c).

If O(y)-W(y) is nonzero, the selected point is the rational expression

    T_y=-(E(y)+b*W(y))/(O(y)-W(y)).

It satisfies T_y^2+c=y and N(T_y)=(T_y-b)W(y). In particular the pole fiber requires O(a0)!=0, not just its norm equation. Distinct fibers give distinct selected points.

## First complete certificate

At p=97 the variable vector is

    (48,1,31,32,53,0,81,34,93,84,56,54,0,3,70).

The exact reconstructed numerator, in ascending powers of T, is

    (34,54,93,0,84,3,56,70).

The thirteen Jacobian pivot columns are0,...,12; the free columns13,14 are O2,O3. Thus fixing O2=3 and O3=70 gives a square invertible thirteen-variable Jacobian modulo97.

The verifier constructs its Jacobian by exact first-order dual-number arithmetic, separately from the search code's interpolation. All thirteen equations evaluate to zero. It also independently reconstructs N using eight-point Lagrange interpolation and checks all twelve matching identities and square-root identities. The updated verifier explicitly checks the support is pole-plus-eleven, the omitted coordinate is positive, and all stored word values equal the seed formulas.

## Open guards checked

* All a_i and e3 are nonzero; the four squares are distinct; the twelve signed products are distinct.
* The first pole a0 is outside the twelve base coordinates and satisfies the first-pole equation. The generic formula then supplies a proper first witness.
* The critical value c avoids all thirteen base values, so every quadratic fiber has two distinct points.
* Every retained O(y)-W(y) is nonzero, including O(a0).
* b^2+c avoids all thirteen base values, keeping the second pole off the ENTIRE26-point core, not merely the twelve selected points.
* N(b)!=0, so the second rational witness is proper.
* Let G5 be the first pole-cleared candidate. The polynomial N-(T-b)G5 has five known selected roots, precisely the positive original pair fibers retained in the support. Division by their product gives a polynomial of degree exactly two, of nonzero discriminant, coprime to every full-core fiber polynomial T^2+c-y and nonzero at b.

For the first hit this quotient is74T^2+2T+8, with discriminant61 modulo97. The independent first-hit audit additionally finds its roots24,52 in F97, both fresh. Splitting of this quadratic over F97 is convenient but is NOT required for the number-field lift: nonzero discriminant and the coprimality guards suffice after a finite extension.

All guards are polynomial nonvanishing conditions after clearing the already-checked denominators. The residual quotient's coefficients are regular near the certified point: its five forced roots are distinct rational functions supplied by the reconstruction formula, and the exact agreement equations force the division remainder to vanish.

## Why full rank gives an algebraic characteristic-zero solution

Fix the two free coordinates O2,O3 to the integers3,70. Multivariate Hensel lifting applies to the remaining thirteen integral polynomial equations and their invertible Jacobian, yielding a solution in Z_97 reducing to the displayed point. Every guard remains a unit, so none can vanish at the lift.

The lifted coordinates are algebraic over Q, not merely unspecified transcendental97-adic numbers. Indeed let L be the field generated over Q by these finitely many coordinates. Differentiating their thirteen polynomial equations in Omega_(L/Q) gives the invertible Jacobian times the vector of coordinate differentials equal to zero. The determinant is nonzero in Q_97, so all differentials vanish. For a finitely generated field extension in characteristic zero, this forces transcendence degree zero. Hence L/Q is a number field.

Adjoin the finitely many square roots giving all core fibers and the two roots of the residual quadratic. The guard inequalities persist under extension. This supplies a genuine finite characteristic-zero bank with the required fresh coordinates. Excluding finitely many bad primes and reducing at completely splitting primes then realizes it in arbitrarily large prime fields. This argument does not rely on a heuristic variable-minus-equation count.

## Verification record

The final independent replay checked all five stored hits under the384MiB/60s watchdog in0.55seconds using under8MiB. Each had all guards true and Jacobian rank13. Files `independent_lift.json` and `independent_lift.resources.json` record the exact arrays and resource result. The first hit's interpolation/residual guards were also independently checked by a separate agent in `independent_first_hit.py/json`.

This is a finite six-word construction after the second one-pole extension, not a proof that the extension can be repeated indefinitely or that bad labels grow superlinearly.
