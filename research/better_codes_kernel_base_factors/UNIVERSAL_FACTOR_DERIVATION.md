# A usable restriction on universal primary-kernel factors

## What the pinned proof actually assumes

Primary repository proximity-prize/proximity-prize, pin cdb451f13fdc6c84f5fe363e77ee13a89bd30974:

* `MovingFiberInitialCore6811.lean:initialAUniversalFactors` and its membership theorem require F to divide EVERY reconstructed primary-A kernel element.
* `initialAUniversalProduct_dvd` asserts joint divisibility of that universal-factor product into every such source.
* `MovingFiberSelection6811.lean:full_divisor_mem_box` obtains a nonzero source from the dimension gate and transfers its caps to the common divisor. The current common_A slope/jet bounds use this support transfer; they do not establish generic irreducibility.
* `MovingFiberInitialBound6811.lean:initialA_universal_singleBound` routes these common factors into the geometric receipt. Factors escaping a source are handled separately by helpers.

Thus a single interpolant containing a binding-shaped factor is not a model for the universal branch. Generic irreducibility of a selected source would not automatically resolve the common-factor branch either. A Bertini claim needs a base-component analysis, a non-composition/separability hypothesis, and a field-of-definition argument; none follows merely from a positive kernel dimension.

## Full source space and a contact-preserving operator

Let V_D be the full linear space of source polynomials Q(X,Y,R,Z) with strict contact weight less than D, uniform contact at least m at the domain nodes for the affine symbols f_i+Z g_i, R-degree at most s, and joint (Y,R,Z)-degree at most L. Extra downward-closed joint jet caps may also be imposed.

Suppose g_i=h(x_i) for a polynomial h. Define

    delta_h=partial_Z+h(X) partial_Y+h'(X) partial_R,
    Delta=max(0,deg h-w).

This operator preserves the contact conditions. Indeed the invertible jet translation

    Y=W+Z h(X), R=U+Z h'(X)

makes the received word independent of Z, and conjugates delta_h to partial_Z. Locally the difference h(x+t)-h(x)-t h'(x+t) is divisible by t^2, so the translation changes the auxiliary contact variable E by a polynomial and preserves contact in every characteristic.

The operator raises contact weight by at most Delta: the two multiplication/derivative terms have weight changes at most deg h-w and deg h'- (w-1), respectively. It never increases the R-degree or the joint caps; in fact each nonzero term lowers joint (Y,R,Z)-degree by one. Therefore

    delta_h^j(V_(D-M Delta)) is contained in V_D, 0<=j<=M.       (1)

These are full-source statements, not assumptions about a particular reconstructed source array.

## Interior-source universal-factor lemma

Assume a nonzero Q lies in V_(D-M Delta). Let an irreducible F divide every member of V_D. Suppose its multiplicity e in Q satisfies e<=M and e! is nonzero in the field. Then

    F divides delta_h F.                                      (2)

For otherwise v_F(delta_h Q)=e-1: in differentiating F^e H the term e F^(e-1)(delta_h F)H has exactly that valuation, while all remaining terms have valuation at least e. Repeating gives v_F(delta_h^e Q)=0, contrary to (1) and universal divisibility. It suffices to assume characteristic zero or characteristic greater than M.

After the jet translation, (2) says an irreducible polynomial divides its Z-derivative. Since a nonzero derivative has strictly smaller Z-degree, the derivative must vanish. If moreover characteristic zero or p>L, no positive Z-exponent in the translated factor can be divisible by p, so the factor is completely independent of Z in the translated coordinates.

A weight-only sufficient condition for e<=M is

    (M+1) wt(F) >= D,

because wt(Q)<D and weighted degrees add. For codeword directions deg h<=w, Delta=0 and the full kernel itself supplies the interior Q. The argument then excludes every non-invariant common factor, with no reserve loss. For near-codeword directions deg h=w+1, an M-unit strict-weight reserve is sufficient.

## Binding cell and the exact reserve test

At the target primary shape m118,s36,L176421,D118*181275=21390450, every factor in the binding cell r12,y55 has

    wt(F)>=55w-12=7208893, 3 wt(F)>D.

Thus M=2 would suffice for any direction of degree at most w+1, IF an interior source of strict weight less than D-2 were certified.

The approved bounded exact test evaluated only D,D-1,D-2, with all other parameters fixed. The coefficient count was independently recomputed by a direct bounded Y/R sum. With local rank bound34814470939, the source-dimension lower bounds are

    cutoff D:    782513,
    cutoff D-1: -951762359,
    cutoff D-2: -1904307231.

Hence the current minimal-L count does not certify even a one-unit reserve. Negative values are failures of this lower bound, NOT proofs that the interior kernel is zero. The test ran under the384MiB/60s watchdog in0.56seconds; exact data and code are `interior_gate.json` and `interior_gate.py`. No parameter grid was run.

## Scope and next missing facts

This is a genuine operator restriction beyond scalar contact budget. In particular the old word-Z binding model is not invariant under delta_1 and so cannot be universal; indeed it is already excluded more directly by the valid source (Y-Z)^118. The shifted degree-w+1 model is likewise visibly not universal because its corresponding graph power is a source. Removing these illustrative models is not benchmark progress.

For a general received direction, its degree-less-than-n interpolant can have degree n-1, making Delta roughly w at the pinned dimensions. The interior requirement can then be substantial. The lemma does not show that an arbitrary line has a low-degree direction, or that the required interior kernel exists.

The concrete remaining task is to prove nonvanishing of a suitable interior kernel, or identify another contact-preserving low-cost operator, for the actual worst-case line class. Alternatively one needs an explicit Hilbert-function bound on the full common-divisor module. Neither a generic-member irreducibility assumption nor a finite-field Bertini heuristic supplies that missing statement. No full-ledger cost or score improvement is claimed.
