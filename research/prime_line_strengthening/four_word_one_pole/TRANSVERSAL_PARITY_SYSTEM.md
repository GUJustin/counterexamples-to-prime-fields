# Exact parity system for a second one-pole extension

This note gives a square-root-free system for a genuinely different next-step support: one match over every one of the twelve original base coordinates. It does not assert existence of a solution. No parameter search was run.

## Variables and seed

Let a1,...,a4 be the reciprocal-quadratic seed parameters, with all the nonzero/distinct-square/signed-product guards from `generalization/GENERIC_ONE_POLE.md`. Let a0=e1 e4/e3 be its first rational witness's pole, off the base domain. Choose the first quadratic map phi(T)=T²+c, where c avoids the base domain and a0.

At a base coordinate y=±a_i a_j, write v=a_i²+a_j². The lifted received value is

    W(y)=(y−a0)v.

A prospective second witness has normalized denominator T−b and numerator degree at most seven. Its unique parity form is

    N(T)=E(y)+T O(y),
    E(y)=u0+u1 y+u2 y²+u3 y³,
    O(y)=v0+v1 y+v2 y²+v3 y³.

Here the four coefficients named v_j are unrelated to the edge value v.

A selected match satisfies

    E(y)+b W(y)+T[O(y)−W(y)]=0.

Consequently, if O(y)−W(y)!=0, the selected square root is reconstructed by

    T=−[E(y)+b W(y)]/[O(y)−W(y)],

and the exact matching condition is

    [E(y)+b W(y)]²=(y−c)[O(y)−W(y)]².       (1)

This eliminates all 2^12 choices of square roots. Conversely any solution of (1) with the displayed nonzero denominators reconstructs twelve distinct selected T values: their squares plus c are the twelve distinct y values. It gives exactly one matching point per base fiber, provided c avoids that fiber's value.

## Twelve explicit cubic equations

For an edge ij set q=a_i² a_j² and v=a_i²+a_j², and define

    r0=u0+u2 q−b a0 v,    r1=u1+u3 q+b v,
    s0=v0+v2 q+a0 v,      s1=v1+v3 q−v.

These are the reductions of E+bW and O−W modulo y²−q. Equation (1) holds at both y=±sqrt(q) if and only if

    r0²+q r1²−2q s0 s1+c(s0²+q s1²)=0,
    2r0 r1−s0²−q s1²+2c s0 s1=0.          (2)

Apply (2) to all six edges. For a fixed seed these are twelve equations of total degree at most three in ten variables u0,...,u3,v0,...,v3,b,c. With the four seed parameters free, there are fourteen variables. Rather than substituting the rational function a0, one can introduce it as a fifteenth variable and add

    e3 a0−e1 e4=0.

This gives thirteen polynomial equations with denominators avoided. This system is suitable for a bounded future finite-field solve and exact lifting test. Merely counting variables and equations does not prove it has any admissible point.

## Essential guards and constructive sufficiency

All seed and first-witness guards must hold. In addition require:

1. c is outside the twelve base coordinates and c!=a0.
2. For each edge, s0²−q s1²!=0. This is exactly O−W nonzero at both base coordinates and prevents spurious 0/0 square-root reconstruction.
3. b²+c lies outside the twelve base coordinates and differs from a0. This keeps the new pole off the entire 26-point core, including the unselected halves of the fibers.
4. E(b²+c)+b O(b²+c)!=0. This makes N/(T−b) proper.
5. N(T)−(T−b)G5(T) has two distinct roots outside the full core and outside b. This is the residual-root guard from `SECOND_STEP_DEFORMATION_ASSESSMENT.md`.

Over an algebraically closed characteristic-zero field, these conditions suffice to make a six-word bank after the next one-pole extension: (2) gives twelve core matches, guard5 permits choosing the two fresh nodes so the witness has fourteen matches on the length-28 word, and the standard extension gives length60, degree cap14, agreement at least30, with six distinct candidates.

For an actual finite-prime-field point, the first pole fiber additionally has to split: a0−c must be a nonzero square. The selected transversal roots already lie in the field by the rational reconstruction formula, and their opposite roots do too. The two roots in guard5 also need to lie in that field if one wants the whole finite construction immediately over that prime, rather than in an extension.

A finite-field point with all open guards and full Jacobian rank thirteen for the thirteen-equation/fifteen-variable system is a concrete sufficient deformation certificate: after localizing at the guards, the Jacobian criterion gives a smooth point over the localized integer base. It lifts to characteristic zero, so the generic fiber is nonempty and has an algebraic-number point. The exact rank and guards would need independent verification; they are not consequences of the dimension heuristic. One may then choose sufficiently large completely splitting primes for the finite characteristic-zero construction.

## The tempting odd specialization is an existing candidate

In the squared-value bridge, let e_j denote the elementary symmetric functions of parameters t_i, and let E_j denote those of t_i². The identities

    E1=e1²−2e2,
    E2=e2²−2e1 e3+2e4,
    E4=e4²

show that e1=e2=0 gives E1=0, E2=2e4. The generic first witness for the squared seed is then

    R_squared(y)=−y−2e4+e4²/y,

with pole a0=0. Its pole-cleared lifted candidate is exactly

    G5(T)=T² R_squared(T²)=−T^4−2e4 T²+e4².

This is precisely the polynomial produced by the odd squared-value bridge. It is not a sixth candidate. Moreover the critical value c=0 coincides with a0 and collapses the required pole fiber. Any deformation based on this point has to escape both the old-candidate identity and the bad pole/critical-value guard; it cannot be counted as a positive starting solution.

## Next justified test

A meaningful next computational task would solve a low-dimensional specialization of (2) while retaining all five guards, then verify the full thirteen-row Jacobian for any hit. There is presently no such hit or proved preservation class. The system supplies a precise target without repeating previously excluded three-double-fiber corrections or enumerating all square-root branches.

## Subsequent scope correction: the all-twelve-base transversal cannot finish

The root agent identified a decisive residual-degree obstruction after this note was written. Such a transversal shares six selected core matches with G5. The nonzero polynomial N−(T−b)G5 has degree at most seven, leaving at most one fresh root, whereas the proposed completion needs two. Therefore its guard5 is impossible. The displayed parity equations remain correct interpolation equations, but are not a viable complete-extension target. The revised search in `transversal_search/` instead selects one first-pole fiber point and eleven old base fibers, omitting one of G5's positive-edge fibers; its G5 overlap is five and it leaves a quadratic residual for the two fresh points.
