# Cubic-cover norm gate: full rank

The eight matrices in `gate.json` have full column rank over F29: rank 26 for the no-full-fiber pattern and rank 20 for each of the seven one-full-fiber patterns. Consequently none of these patterns admits a primitive cubic norm relation with the pole bounds below. This rules out cubic-cover proper one-pole augmentation wherever the existing two-pattern theorem applies. It does not silently extend that theorem to covers with hypotheses it did not establish (notably a nonsquarefree denominator).

## Pole flags

Let psi:P1_U -> P1_X have degree d, and let a rational residual function v satisfy

    (v)_infinity <= (3-f) psi^*(infinity) + [b].

Assume (psi,v) is birational onto its image. The monic minimal polynomial over k(X) is

    v^d + a_1(X)v^(d-1) + ... + a_d(X).

At finite places other than psi(b), all conjugate values are integral. At psi(b), the extra simple pole on the normalization contributes total pole degree at most one to each elementary symmetric function: in an extension splitting all branches, the negative valuations of all conjugates sum to at most one in base valuation units. Each symmetric coefficient therefore has valuation at least -1. At infinity the corresponding sum for any j conjugates is at most j(3-f), with an additional at most one if psi(b)=infinity. These statements also follow from integrality of elementary symmetric functions after extending the discrete valuation and summing over the ramification conjugates.

If psi(b) is finite, multiply by X-psi(b); otherwise leave the monic equation unchanged. This gives a nonzero polynomial relation whose coefficient of v^(d-j) has degree at most j(3-f)+1, including j=0. Passing to a primitive relation by removing polynomial content preserves these bounds.

In the proper one-pole construction v initially equals N/(ell*S^3), with psi=R/S. Subtract the base interpolant through the f full fibers and divide by their locator in X. The full-fiber equalities remove the apparent new finite poles. The stated residual pole bound follows. The pole at b remains proper. For prime degree d=3, failure of birationality would imply v belongs to k(psi). A lone extra simple pole off S is impossible for such a pullback (its pole divisor contains the entire degree-three fiber, with multiplicity). If b lies at a simple root of S, the unequal orders at the three S roots likewise exclude a pullback. These are the hypotheses used in the archived squarefree-S pattern proof.

## Singular-point constraints

Two distinct points of the normalization above the same finite pair (x,v) imply that the image point is singular. For a primitive plane equation F(X,v), this implies

    F(x,v) = F_X(x,v) = F_v(x,v) = 0.

This argument requires distinct preimages and birationality, both supplied by the selected separable fibers and the preceding proper-pole argument. No assumption of ordinary nodes or transverse branches is required.

For f=0 there are seven double triple-bucket fibers and seven single quadruple-bucket fibers. The degree flags are (1,4,7,10), giving 26 coefficients. The seven singular points and seven other points impose 28 homogeneous linear equations.

For f=1 remove the full triple fiber and its paired empty quadruple fiber. The transformed values at every remaining base node are

    v_i = (word_i - word_full)/(x_i - x_full).

There are six double fibers and six singles. Flags (1,3,5,7) give 20 coefficients and 24 equations.

## Exact finite certificate and characteristic-zero consequence

The input is the independently archived Paley reduction from `../quadratic_one_pole_route/fiber_patterns.json`: p=29, zeta=16, alpha=3, first seven nodes quadruple buckets and last seven triple buckets. Matrix columns are X^k v^l. Rows are value, X derivative, or v derivative as explicitly recorded. `gate.json` includes every matrix, pivot row/column set, and empty kernel.

These eight full-rank matrices certify the characteristic-zero Paley construction as well. Its node and word values are algebraic and integral at the chosen prime above 29; all node differences used as denominators are units. The recorded nonzero maximal minors are reductions of the same characteristic-zero minors. Thus the characteristic-zero linear systems have full column rank. This is ordinary minor specialization, not an inference from a modular ideal computation. It also gives exclusion in characteristic 29 for this exact bank, and in every characteristic where the same finitely many minors and input guards remain nonzero.

The conclusion is an obstruction to the entire eligible cubic-cover family, not merely to a sampled cover or a selected pole. Extending beyond the established two-pattern hypotheses requires a separate proof of that combinatorial/geometric classification.
