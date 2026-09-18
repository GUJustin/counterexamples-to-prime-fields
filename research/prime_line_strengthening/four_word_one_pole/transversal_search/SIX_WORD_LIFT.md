# Certified second one-pole extension

The self-contained theorem and proof are in `six_word_lift.tex`. They establish a number-field bank, and hence banks over arbitrarily large prime fields, with sixty distinct evaluation points, six distinct polynomials of degree at most fourteen, and at least thirty agreements per polynomial.

This is a fixed six-word construction at exact quarter rate and half agreement. It does not prove growing lists, a superlinear proximity-gap counterexample, DKT tightness, or a better.codes improvement. No priority claim over older fixed six-word constructions is made; the point here is a certified second application of the one-pole extension mechanism.

## Certificate chain

1. The generic reciprocal-quadratic identity in `../generalization/GENERIC_ONE_POLE.md` constructs the first rational witness and its five-polynomial lift.
2. The first record of `hits.jsonl` gives the second proper rational witness over F97.
3. `independent_first_hit.py/json` verifies its twelve core agreements, proper pole, degree, and the two fresh roots24,52.
4. `independent_lift.py/json` verifies the thirteen-equation norm system, all open guards, and a full-rank13 Jacobian minor (first thirteen columns, with free coefficients O2,O3 fixed to3,70).
5. The independent pointed Jacobian calculation uses25equations in27variables and gives determinant21 modulo97 for its first25columns. This avoids relying only on the norm-system implementation.
6. Hensel lifting plus the nonsingular algebraic system gives a number-field realization. The residual quadratic remains squarefree and off the core/pole. The elementary second quadratic pullback then gives the stated60-point bank.

The manuscript fragment contains all construction formulas, finite-field coefficients, interpolation coordinates, both equation systems, the lifting argument, and the final prime-field reduction. It is an independent input; neither the main paper nor its build was edited here.
