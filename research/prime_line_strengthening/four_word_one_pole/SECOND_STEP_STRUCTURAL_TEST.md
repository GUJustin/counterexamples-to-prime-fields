# Structural second-step test: a restricted correction family fails

The five-word construction remains valid. This note tests a limited algebraically motivated way to supply its next one-pole witness. It does not exclude general degree-(7,1) rational witnesses or arbitrary modifications of the first extension.

## General parity decomposition

Allow the first quadratic map to be phi(T)=T²+c, where c avoids the old domain and first pole a. Put y=phi(T). Every rational function N(T)/(T−b), deg N<=7, has a unique decomposition

    R(T)=A(y)+B(y)/(T−b),   deg A,deg B<=3.

For an even received value W(y), write C(y)=W(y)−A(y). A match at a nonpole point requires

    (T−b) C(y)=B(y).

On a two-point fiber this implies

    (y−c) C(y)²=(B(y)+b C(y))².              (1)

Both points match exactly when B(y)=C(y)=0. A proper nonpolynomial witness has B nonzero and therefore has at most three double-matched fibers. This is a degree restriction, not a proof that fourteen total matches are impossible.

An unused original rational witness pulled back through phi retains two poles. Making its old pole the critical value gives a double pole, not a simple pole: its numerator is nonzero there by properness. Thus ramification alone cannot fix the next-step input. Multiplication by a linear factor cancels one order but changes all matched received values and raises the degree budget of the old polynomial bank; it is not an operation preserving the current length-28, degree-6 instance.

## A 60-case algebraic reduction

Choose the polynomial part to be one of the four old lifted candidates,

    A(y)=(y−a) H_i(y).

It matches the first lifted word W(y)=(y−a)w(y) at the six old base coordinates matching H_i, and on the pole fiber y=a. Choose two distinct matching base coordinates r,s and take

    B(y)=lambda (y−a)(y−r)(y−s), lambda!=0.

This creates three double-matched fibers and hence six matches. At the four other matching base coordinates C=0 but B!=0, so there are no matches. To attain twelve matches in the paired 26-point core, one must therefore get a single match at each of the six remaining base coordinates; only the two fresh coordinates can supply the other two matches needed for fourteen total.

For a nonmatching old base coordinate y set

    z_y=(y−r)(y−s)/(w(y)−H_i(y)).

Equation (1) reduces to

    y=alpha+beta z_y+gamma z_y²,
    alpha=c+b², beta=2b lambda, gamma=lambda².

Thus the six rows (1,z_y,z_y²,y) must have the same rank as their first three columns. This condition is necessary even if c,b,lambda are allowed in arbitrary algebraic extensions. If it passed and gamma!=0, the remaining field and pole guards would have to be checked separately.

There are only four choices of H_i and fifteen choices of {r,s}, giving sixty exact tests over Q(zeta_12). `second_step_rank.py` found:

- 48 cases with coefficient rank 3 and augmented rank 4;
- 12 cases with coefficient rank 2 and augmented rank 3;
- no consistent cases.

Therefore this subfamily cannot supply the next witness, for any choice of the first quadratic critical value, prospective pole, correction scale, or two fresh coordinates. The result is independent of which of the twelve first-step one-pole witnesses supplied a: the factor y−a cancels from (1).

The calculation ran under the repository's 384-MiB/60-second bounds and completed in under one second; exact per-case ranks and resource data are retained in `second_step_rank.json` and `second_step_resources.json`.

## Remaining concrete freedom

The next rational witness may have a polynomial part A(y) not equal to an old lifted candidate, or may decline to match both points of the first pole fiber. Those possibilities are not tested here. A fresh structural identity is needed before a larger search; the positive five-word bank alone is not evidence that the extension repeats.
