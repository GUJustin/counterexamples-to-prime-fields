# Independent audit: majority lower construction and sharp Dickson-bank upper bound

**Verdict: PASS**, for the stable versions of `DICKSON_MAJORITY_LOWER.md` and `DICKSON_SHARP_LIST_THRESHOLD.md` reviewed September 17, 2026. No mathematical repair remains. The only previously identified transcription error in the upper note (the denominator after dividing the square-root term) has already been corrected to L²n. No manuscript was modified during this audit.

## Lower construction: checked hypotheses and every conversion

1. The prime condition p≥4096 L³4^L implies p>2L. Thus the 2L shifts ±1,...,±L are distinct and nonzero, and the L squared parameters give distinct bank polynomials. The congruence p≡1 modulo 8 gives both chi(−1)=1 and chi(2)=1. Dirichlet applies to the fixed progression 1 modulo 8, so sufficiently large primes exist for every fixed L; no uniform least-prime estimate is claimed or needed.

2. The majority word is well-defined on square coordinates: s→−s swaps the signs in each pair, preserves their sum, and preserves the fixed positive tie rule. At regular s, candidate i matches precisely when its two signs both equal the selected sign. The square-root representative is therefore irrelevant.

3. The independent-sign probability holds individually for every i, not only on average. Expanding the indicator gives

       E F_i=1/4+[E(sigma xi_i)+E(sigma eta_i)]/4,

   since E(xi_i eta_i)=0. Coordinate permutation symmetry and sigma S=|S| imply each of the 2L expectations equals E|S|/(2L). The telescoping random-walk identity yields exactly

       mu_L=1/4+binom(2L,L)/(2*4^L).

   Fixed tie breaking causes no error because the product sigma S vanishes on a tie. The central-binomial lower bound b_L≥1/(2sqrt L) follows from the displayed induction, including L=1.

4. The Fourier transfer is valid with real normalized Boolean Fourier coefficients. Parseval bounds their squared sum by one, and Cauchy bounds the nonconstant absolute sum by 2^L. Every nonempty character product has distinct linear factors. I independently read the cited primary source: Bourgain–Garaev–Konyagin–Shparlinski, *On the hidden shifted power problem*, [Lemma 17, page 10](https://arxiv.org/pdf/1110.0812). It bounds the mixed product sum by (r+d)sqrt p. Taking a nonzero constant additive phase (d=0, an irrelevant unit-modulus scalar) and r≤2L gives the precise 2L sqrt p bound used here. All multiplicative characters in this application are the nonprincipal quadratic character. Thus the cited theorem supports the explicit constant, not merely an unspecified big-O estimate.

5. At a zero-character point the multilinear extension averages the original Boolean function over the missing signs. Its value lies in [0,1], so deleting the 2L endpoints and s=0 costs at most 2L+1. This step avoids an incorrect exponential endpoint charge. The estimate applies separately to every F_i using the same deterministic shifts and the same word; neither a union bound over random parameters nor candidate-specific words are used.

6. Removing endpoints leaves a set stable under s→−s. The matching-square count is at least (p mu_L−E_L)/2, where E_L=2L2^L sqrt p+2L+1. Each candidate also has exactly n/4 nonsquare matches. Therefore its total normalized agreement is at least

       3/8+b_L/4−E_L/(2n), n=p−1.

   The discarded positive correction mu_L/(2n) is harmless. The factor one half for square coordinates is present.

7. Since n≥p/2, the error is at most 2L2^L/sqrt p+(2L+1)/p. Under p≥4096 L³4^L, the first term is ≤1/(32sqrt L). The second has that same upper bound because 4096 L³4^L≥32(2L+1)sqrt L for L≥1 (for example, 2L+1≤3L makes the latter immediate). The net gain is consequently at least 1/(8sqrt L)−1/(16sqrt L)=1/(16sqrt L). The stated finite constant 4096 passes.

8. For 0<epsilon≤1/32, x=1/(256epsilon²)≥4. Thus L=floor x≥x/2=1/(512epsilon²), while L≤x implies 1/(16sqrt L)≥epsilon. This proves the claimed existential Omega(epsilon^(-2)) list lower bound for sufficiently large primes. It does not claim the lower bound for every fixed prime.

9. The full ordinary core persists: on square coordinates shifted received values ±1 annihilate both coefficients of the primitive ODE, and on nonsquares shifted value zero does so. The same actual bank solutions are retained; no coordinatewise surrogate equation replaces the global one.

## Upper theorem: checked exact bucket and moment constants

The nonsquare zero bucket totals Ln/4; every nonzero bucket there is a singleton. On squares, only ±1 can be shared. Each shared sign has total Ln/8. The endpoint adjustment is essential and correct: deleting s=0 subtracts one for the sign chi(a), while the two endpoints each add one half for that same sign.

For S(s)=sum_{a in A}(chi(s+a)+chi(s−a)), the exact identity is

    sum_s S(s)²=2Lp−4L².

The endpoint-corrected shared-bucket difference is S(s)/2+E(x)/2 with sum_x|E(x)|=L. After the two-to-one square map and the maximum-of-two-buckets formula, this gives

    sum_{x square} max(N+,N−)
      ≤Ln/8+(1/8)sqrt(n(2Lp−4L²))+L/4.

Allowing singleton buckets costs at most one at each of the n coordinates. Hence the universal total-agreement bound in the upper note is correct. Upon division by Ln, the square-root term is

    (1/8)sqrt((2Lp−4L²)/(L²n)).

Using L≤n/2 and p≤2n gives epsilon≤9/(8L)+1/(4sqrt L). If L≥epsilon^(-2) and 0<epsilon≤5/8, the right side is at most (61/64)epsilon, a contradiction. The nonzero list is strictly smaller than epsilon^(-2); adding the zero polynomial gives at most ceil(epsilon^(-2)). Received values outside F_p match none of the classified polynomials, so the extension-alphabet statement is valid.

## Dependencies, tests, and scope

The classification dependency was independently checked previously: all degree≤k−1 shifted solutions are the 2k nonzero Dickson bank members and zero, over every extension field of this characteristic. The upper theorem therefore bounds the complete solution set of this ODE, not an arbitrarily selected subset presented as complete.

I inspected `check_dickson_majority_lower.py` and its actual output `dickson_majority_lower_checks.json`. It computes 15 deterministic received words using one representative from each square-root pair and checks the target gain with an exact integer-square inequality. Only p=65537,L=1 meets the conservative displayed prime condition; the artifact correctly labels the others as uncertified by that condition. These controls are not used as a substitute for the uniform proof. I did not rerun the numerical job in this audit.

The conclusions establish an exact 3/8 transition and matching Theta(epsilon^(-2)) dependence for this particular globally constrained solution bank. They do not upper-bound all Reed–Solomon lists, produce superlinear prime-field scalar labels, improve better.codes, or show tightness at the general first-order proximity threshold. The lower agreement statement at epsilon=0 is the previously established Dickson construction, not a new lower bound attributed to this audit.
