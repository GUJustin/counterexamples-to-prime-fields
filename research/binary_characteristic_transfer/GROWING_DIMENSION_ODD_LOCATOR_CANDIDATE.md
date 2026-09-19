# Growing-dimension odd-characteristic locator candidate

Research candidate rejected by an elementary support-intersection check, not a counterexample theorem. 2026-09-18.

**Decisive check.** Two different displayed locators differ by a polynomial of degree at most 2K. Their two 4K-element root sets in an n-element domain intersect in at least 8K−n points. Therefore n<6K permits at most one such locator. In particular the apparently attractive first-order window below cannot supply even two members, let alone superlinear challenge count. This shows why checking the compiler and threshold placement is insufficient. A subsequent construction must change the high locator coefficients or use a different identity.

The binary near-Johnson example suggests relaxing the code degree rather than requiring its short-tail compiler to survive unchanged. The following identity is valid in every odd characteristic (independently checked by symbolic expansion).

Put u=X^K and L=u^4+a u^2+b u+V, where V(0)=0 and deg V<K. Then

    L [u^4−a u^2−b u−V+a^2+θ]
      = u^8+θu^4−2ab u^3+R,

where

    R=(a^3+θa−b^2)u^2−2a u^2 V
       +(a^2+θ)b u−2b u V+(a^2+θ)V−V^2.

R is divisible by X and has degree at most 3K−1. Consequently, for code dimension k=3K−1 and sources

    f=X^(8K−1)+θX^(4K−1),  g=X^(3K−1),

the challenge λ=−2ab has witness −R/X of degree at most 3K−2. Every nonzero root of L is an agreement point. A squarefree fully split L supplies at least 4K−1 agreements. Also g has agreement at most 3K−1 with every degree-<k polynomial. Interpolation on any k domain points attains this bound for g and simultaneously for f, so common agreement is exactly 3K−1. The strict dimension choice is essential: at dimension 3K, g itself would be a codeword.

This does not bound the first source's individual agreement. Additional roots from the other factor are possible. Distinct locators need not yield distinct products ab, and no singleton-list claim follows.

## Why the parameter window is worth testing

If n=cK+O(1) with 16/3<c<6 and K tends to infinity, the tested agreement 4K−1 is below the finite Johnson threshold sqrt(n(3K−2)). First-order placement at this positive rate requires checking the full rate-dependent formula; the low-rate leading approximation alone does not certify it.

That check succeeds for the **tested threshold** when c=11/2. The limiting rate is ρ=6/11, and DKT Equation (31), upper branch, gives

    a1(ρ)=[3ρ+2sqrt(ρ(5−ρ)(2−ρ))]/(8−ρ)
          =0.723887084988...
          <8/11=0.727272727272...<sqrt(6/11).

An exact certificate for the first strict inequality is

    [(8/11)(8−6/11)−3(6/11)]²
       −4(6/11)(5−6/11)(2−6/11)=2788/14641>0,

with the unsquared left expression positive. Continuity gives the same strict placement for all sufficiently large even K at n=11K/2, k=3K−1, T=4K−1. The common agreement is at capacity, below the first-order curve; only the tested threshold is above it. Source placement must not be described otherwise.

The loss is K/n, and the tested agreement exceeds k/n by K/n. These are equal positive constants in this window. Thus increasing code dimension does not automatically eliminate the desired relative loss.

## The construction problem and why this version fails

The initial target was a prime field F_p and a domain D of n≈cK distinct points supporting a family of squarefree, fully split locators of the above shape, all roots in D, with more than n times a growing factor distinct products ab. The support-intersection argument above rules this out in the proposed window, regardless of the prime size.

Taking quartics in X^K over a fixed number of multiplicative fibers also gives only a bounded number of support choices. The substantive next target must allow differences of locators to have larger degree while still compiling their high coefficients into one challenge parameter and low-degree witnesses. This note records an exact failed transfer so it is not mistaken for progress toward the requested counterexample.
