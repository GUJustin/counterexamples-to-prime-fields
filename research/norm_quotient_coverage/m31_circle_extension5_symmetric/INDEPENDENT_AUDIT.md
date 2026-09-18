# Independent degree-five trace-circle audit

2026-09-18. **PASS**, for the explicitly defined E-valued Laurent code and selected domain. No manuscript edits or protocol equivalence claim.

## Character estimate

The degree-two trace map from the circle to the affine line is defined over Fp and ramifies only over ±2. The five conjugates of a degree-five b avoid these branch values. Thus the pullback has ten distinct simple zero punctures. At each, the local character is a Frobenius conjugate of the nontrivial native character χ, hence remains nontrivial. This also covers characters descending through any norm: trivial restriction to a smaller multiplicative group does not trivialize these local characters. The circle twist is unramified at these ten points and cannot cancel them.

The only additional possible ramification is at the two geometric poles of the trace map. Both sheaves are tame. On the projective line with at most twelve actual punctures, geometric nontriviality gives Hc0=Hc2=0 and tame Euler characteristic gives dim Hc1≤10. Weight ≤1 yields 10√p. The parameter point at infinity corresponds to a=1; it is regular and included, with value χ(b−2), so no omitted endpoint term is needed. This uses the rank-one Lang character construction and weight argument described in the cited Katz primary proof, not a character-order restriction.

## Trace population

H has order 2^22 and contains both ±1. Its trace image has 2^21+1 elements. Removing the two branch traces leaves 2^21−1 tags, each counted twice in H. Subtracting the two branch contributions before dividing by two gives 5√p+1. Removing the reserved regular tag adds one, yielding population P=2^21−2 and numerator 5√p+2<231707. This factor of one half and both removal costs are correct.

Independently recomputed the exact overlap sum, distinct-sampling correction, and every one of the twenty-two upward-rounded rational recurrences. All numerators match receipt.json and (p^5−1)h22<1. The saved independent_arithmetic.json records the final exact numerator and hashes of the reviewed sources. This is a finite existence certificate, not an explicit tag list.

## Code and exact agreements

Since p≡3 mod4, adjoining i to E gives Fp10. The displayed cosine and sine functions are Fp-valued on the circle, so their E-span is well defined. Their Laurent monomials are independent in characteristic different from two; a nonzero Laurent polynomial supported on [−L,L] has at most 2L distinct nonzero roots. This proves both dimension 131071 and applicability of the root bounds to arbitrary witnesses, including sine modes.

Every regular tag fiber has 1024 distinct points. Neither z=±1 occurs in such a fiber, so its 512 trace values are distinct simple roots of C512(X)−a0. Dividing by X−x0 removes exactly the pair z0,z0^−1. Hence R has exactly 1022 domain roots, disjoint from the chosen tag fibers.

The canonical witnesses have Laurent degree ≤65535. Their residuals have exactly 133118 roots. Against any witness in the full code, the cleared residual has extreme Laurent degree 66559: the competing term (Y−b)h has degree ≤66047, so the extreme coefficients cannot cancel. This gives the matching upper bound.

The source f has Laurent degree 66047, giving agreement ≤132094. For g, clearing the denominator gives Laurent degree at most 66047 and a nonzero numerator: divisibility of R by Y−b is impossible because their Laurent widths are respectively 1022 and 1024. The 128-tag locator construction gives common witnesses of degree ≤65535 matching on exactly 132094 points. Thus both source agreements and ordinary common agreement equal 132094, and every nonzero pencil label has exact agreement 133118.

## Scope and closure

The capacity margin remains 2047/262144. This changes the native challenge extension degree and the code dimension (131071, not 131072); it does not increase the margin or produce a prescribed FFT domain. At the next complete-fiber size, 2048, there are at most 128 fibers, and even all 2^128 supports are fewer than p^5−1 labels. Therefore larger fibers cannot improve the all-label margin within this fixed-core compiler. This is not an upper bound for arbitrary code witnesses or partial-fiber constructions. No further variants of this route are proposed.
