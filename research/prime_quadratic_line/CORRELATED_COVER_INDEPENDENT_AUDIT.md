# Independent audit: correlated covers

**PASS (2026-09-18).** Independently checked `correlated_cover_line.tex` against the external proposed construction in `../astra_strategy_2026_09_18/strategy_breakthrough_finish_finish.answer.md`. No manuscript edits were needed.

## Prime selection and subgroup

The stated Bombieri–Vinogradov consequence is valid for every fixed `0<b<=1`. Summing the progression counts for moduli `2s`, with `s` in a fixed dyadic interval of scale `X^(b/3)`, gives a main term bounded below by a positive constant times `X/log X`. The summed errors at the two endpoints are `O(X/log^2 X)`. All moduli lie below the classical level `X^(1/2)/log^B X`. Consequently there are infinitely many prime/divisor pairs, with `s=Theta(L^b)` and, by choosing the interval constant small, `s<=L/100`. This does not assert existence for every prime or for a prescribed divisor.

The subgroup has even order and more than `32L^2` elements. The existing integer Sidon exponents have `4 max b_i < |H|`; therefore both ordinary pair-sum collisions and collisions caused by a sign are excluded. There is room for the core and the specified fresh nodes. Every selected base point has exactly `s` distinct nonzero preimages.

## Random word and all codewords

The core double-counting bound applies to every nonbank polynomial of degree at most `2s`, including polynomials that do not descend through the cover. Exceeding `A` requires at least `L-1` fresh fibers. A single fiber has match probability at most `s/(p-2L)`. The union bound includes all `p^(2s+1)` polynomials and all `p` parameters. Its logarithm is at most `[6s+(b-2+o(1))L] log L`, which tends to minus infinity under the stated constants.

For each fixed parameter other than 0 and 1, each bank loses at most `6L` possible fresh nodes to the blacklist. Desired values are distinct at any fresh node. Thus the bank–fiber hit count is a sum of independent Bernoulli variables with mean tending uniformly to 1 and maximal success probability tending to zero. Exactly one hit has probability tending to `1/e`. Subtracting the global nonbank failure event before averaging over labels establishes existence of a realization with the claimed singleton count; it does not require independence between labels.

## Exact source and common agreements

The blacklist gives no fresh bank hits at old labels 0 or 1. The nonbank-good event gives no nonbank agreement above `A` at either label. Hence `f` and `f+g` each have exact agreement `A`.

For the original source pair `(f,g)`, a nonzero polynomial explanation of `g` has at most `2s+3s` matches; this is smaller than `A` for all sufficiently large `L`. The zero explanation restricts common matches to the core, whose maximum is exactly `A`. Common agreement is invariant under the invertible source change `(f,g)->(f,f+g)`: the explaining pair `(U,V)` changes to `(U,U+V)`, and conversely. This explicitly justifies the theorem's common-agreement statement for the final named sources `F,G`.

The fractional-linear parameter change sends every counted old label (which excludes 0 and 1) to a finite nonzero new parameter, and polynomial scaling preserves list size. At the additional parameter -1, zero matches the entire core, while every nonzero polynomial has at most `5s<T` matches, so the optional infinity singleton assertion is also correct.

## Scaling and scope

The identities `n=s(2L^2-2L+1)`, `T=s(2L-1)`, and `(k-1)n-T^2=s^2` are exact. With `alpha=b/(b+2)`, the exponents in the theorem follow. The first-order comparison follows from the stated low-rate expansion and `T/sqrt(kn/2)->sqrt(2)`.

For `b<1`, the absolute distance below the Johnson threshold is of order `s/L` and tends to zero; the fragment correctly does not claim this distance stays constant. The rate and normalized source separation vanish. The result is a polynomial absolute-gap construction, not fixed-rate sharpness. Prime existence uses an average distribution theorem, not a constructive small-prime search.

The manuscript's primary BV citation is appropriate subject to the parent agent's already completed verification of Harper Theorem 7.1. An independently checked primary research formulation is Maynard, *Primes in arithmetic progressions to large moduli I: Fixed residue classes*, equation (1.1), https://arxiv.org/html/2006.07088.
