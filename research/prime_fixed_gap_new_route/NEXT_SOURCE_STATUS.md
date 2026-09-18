# Source search after the sharp Dickson theorem

September 17, 2026, evening. Theorem R.5 and its quadratic-alphabet
majority lower construction are already in the published working paper.
The remaining prime-field target requires a different step: a growing
fixed-gap bank on a domain of length small compared with the prime, or
a direct line construction not requiring such a bank.

## Evidence that changes the search

1. **Common-factor shortening is ruled out for a growing Dickson bank.**
   The common gcd of pairwise differences has degree at most `2p/L`,
   including multiplicities and all algebraic roots. Subtracting a common
   polynomial, dividing by a common factor, and puncturing therefore
   still gives `p <= 8n'+2` once `L>=16`. See
   [the exact proof](SHORTENING_AND_REYNOLDS_GATES.md).

2. **The proposed full Reynolds bank has no tested surplus beyond its
   small bounded cases.** All 377 tested parameters fail for the original
   word. Even the optimal word for the entire bank fails to exceed the
   code dimension in all tested cases with `r>=5`. The characteristic-zero
   lift has no candidate collisions at any coordinate. This is evidence
   against the current complete-bank proposal, not a finite-field
   impossibility theorem. See [scope and checks](REYNOLDS_FINITE_SURVEY.md).

3. **A new split cubic polynomial first-integral proposal has a uniform
   section bound.** With squarefree H and a zero-dimensional original
   critical ideal, there are at most 69 sections whenever `deg H>D`,
   including cancellations at infinity. That covers every viable
   root-domain instance of this proposed mechanism. The full-degree case
   has the sharper bound 33. See the
   [construction and proof](../short_domain_cubic_source/SPLIT_CUBIC_PENCIL.md).

4. **Simply adding a second derivative does not improve the benchmark.**
   The dense source's sufficient dimension certificate fails in all 353
   tested shapes, with an exact affine test covering all challenge caps
   within each shape. A restricted support would also need a new
   downstream counting theorem. See the
   [exact comparison](../better_codes_second_jet/COMPARISON.md).

5. **All degree-two rational pencils are controlled in the short-prime
   regime, including quadratic moving denominators.** Five polynomial
   sections bound the discriminant height by `10D`; reciprocal
   normalization at one known square value allows the verified
   Pasten--Wang theorem to apply without a splitting cover. At least
   twenty-one labels force a Möbius family when `p>max(2,10D)`.
   The local collision pattern then bounds a surplus-`eta*n` list by
   `max(40,ceil(2+2/eta)-1)`. See the
   [height proof](../short_domain_cubic_source/QUADRATIC_QUADRATIC_HEIGHT_GATE.md)
   and [agreement proof](../short_domain_cubic_source/RATIONAL_PENCIL_MOBIUS_BRIDGE.md).
   The linear-denominator subclass has a sharper affine-family conclusion.

## Unexcluded directions worth distinguishing

* Rational first-integral pencils of degree at least three in the value
  variable. Their fibers can meet at common base points,
  escaping the disjoint-critical-support argument above. Dickson itself
  has a quartic numerator and quadratic denominator, but an alternative
  must avoid its degree being proportional to p.
* Genuinely nonintegrable cubic equations, or repeated-root denominators,
  with an explicit growing polynomial solution family and an agreement
  surplus. Existence of many solutions alone is insufficient.
* A direct prime-field line construction or a proper subbank of a modular
  projection. Neither the full-bank modal calculation nor the polynomial
  first-integral theorem excludes these.

No new better.codes score, fixed-gap superlinear prime-field label count,
or intrinsic first-order proximity tightness result is claimed. The
purpose of these records is to avoid recycling mechanisms for which an
actual obstruction has now been proved, while keeping the remaining
targets explicit.
