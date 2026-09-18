# Non-even square witnesses: fixed translated blocks and linear modulation

Independent exact-identity gate, September 18, 2026. This closes the proposed p-match-core / 2p-match-fresh route with a fixed translated Frobenius block and a fixed nonzero linear fresh direction. It does not classify arbitrary new received words or directions.

## Core square family

On the B=F_(p²) component of the core, a non-even quadratic with p matches to X^(2p), for p>=5, must be a square

    Q(X)=(uX+w)²,
    u^(p+1)=1, w!=0, w in I_u=image(t^p-u t),

after replacing (u,w) by its simultaneous negative if necessary. The two factors of the agreement equation are `X^p-uX-w` and `X^p+uX+w`. Their p-root cases use the distinct image lines I_u and I_-u; a nonzero w belongs to at most one. If u is not norm one, each linearized factor has at most one root. Conversely the displayed conditions give exactly p matches, none at zero.

Necessity of being a square follows directly from the quartic elimination in PROOF.md: a p-match non-even witness with p>=5 makes that quartic identically zero, expressing Q as a square of a linear polynomial over B. The other B-line of the full doubled core gives the same classification after its fixed scaling. Thus there are at most `2(p+1)(p-1)=O(p²)` such core p-match witnesses, even allowing all E coefficients. The bound suffices here; no double-counting correction is needed for the conclusion.

## A fixed translated fresh block without linear modulation

A canonical quadratic on a fresh block centered at h has shape `a(X-h)²+b`. Equating its linear coefficient to Q gives `w=-uh` and a=u². In the B chart, w in B and u in B* already force h in B. If h!=0, the image condition `w^p=-u^p w` gives

    -u^p h^p = h,  hence u=-h^(p-1).

Thus u is fixed by the center, and then w is fixed as well. If h=0, w=0, which is the even canonical family rather than the targeted non-even p-match family. The same calculation applies in the other chart after its fixed coordinate scaling. Choosing a different fixed center does not preserve a growing non-even bank.

## A linear fresh direction allows movement but loses label multiplicity

Let Z=X-h and take a fresh source of scaled Frobenius form, with direction

    g=gamma Z+delta,  gamma!=0.

The condition that Q is canonical for the fresh word f+lambda g is exactly that `Q-lambda g` is even in Z, with the appropriate constant-image condition. Its odd coefficient gives

    lambda gamma = 2u(uh+w).

Therefore EACH fixed core square witness has AT MOST ONE possible label, regardless of whether its remaining constant coefficient satisfies the fresh image condition. The coefficient identity remains valid over E and after either fixed core chart scaling; characteristic is odd.

Hence this route has only O(p²) joint core-p / fresh-2p witness-label pairs. It cannot produce the proposed p⁴ population, nor the already achieved p³ population, at n=Theta(p²). Thinking of the center as varying with lambda does not evade the identity: that variation is precisely what the unique linear-coefficient equation controls.

If gamma=0, the fixed-center obstruction returns. In the exceptional even-center case the mechanism is again the previously analyzed even bank. A fixed additional linear term in f merely changes the numerator of the unique-label equation; it does not change the conclusion.

## Scope and next decision

The threshold arithmetic `sqrt(3N/2)<3p<sqrt(2N)` for N~5p² is compatible asymptotically, but does not create a population. The shared polynomial identity above explains why this particular modification cannot attain it. No numerical scan is warranted for this subclass.

To use non-even witnesses productively, one needs a source/direction identity giving MANY labels per core witness without forcing a unique label through a linear coefficient, or a substantially larger core p-match family. A nonpolynomial fresh direction, a different core with a genuinely three-parameter witness population, or a different agreement mechanism is outside this gate. None is presently supplied by the calculation. The result is not a universal obstruction to quadratic first-order counterexamples.
