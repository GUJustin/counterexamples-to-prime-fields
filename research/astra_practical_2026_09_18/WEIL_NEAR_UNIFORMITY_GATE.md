# Can standard subgroup character bounds certify near-uniform packet fibers?

September18,2026. **Decision: no.** At the actual prime, standard complete-field Weil/Gauss bounds are already larger than the entire256-element subgroup. The resulting subset-coefficient bounds do not exclude the target and do not justify calling the fiber route futile. No heuristic is promoted to an upper bound.

## Actual character-sum scale

Let p=2130706433, H=mu256, D=H minus1, and P_b(X)=Σ_(j=1)^6 b_j X^j for b!=0. Let chi be any character of H, including the twists used to retain root products. Extend chi to a multiplicative character of Fp*. With index

    I=(p-1)/256=8323072,

character orthogonality expresses the H-sum as the average of I complete mixed sums over Fp*. The standard mixed Weil bound for a nonconstant polynomial of degree d<=6 is d sqrt(p); the untwisted complete additive case can be slightly sharper, but does not change this conclusion. Averaging I bounds does NOT divide the final bound by I, since there are I summands. Removing1 gives

    |Σ_(x in D) chi(x)e_p(P_b(x))|
       <= min(255, d sqrt(p)+1)=255.

Numerically,

    sqrt(p)=46159.57574545...,
    6 sqrt(p)+1=276958.45447270... .

Even the favorable linear/Gauss estimate sqrt(p)+1=46160.57574545... is vacuous compared with255. The polynomial has degree less than p and is nonconstant, so there is no Artin–Schreier degeneracy issue; the problem is purely the short subgroup scale. The benchmark's index8128 refers to the much larger NTT domain, not to this256-element tag subgroup.

Primary reference checked: *Moment subset sums over finite fields*, Theorem5 (mixed character-sum form) and its surrounding discussion:
https://pmc.ncbi.nlm.nih.gov/articles/PMC10941333/
Theorem5 with one multiplicative factor X and polynomial additive argument of degree d yields the d sqrt(p) scale. The paper's near-uniform/positivity regimes require a character-sum bound small relative to the underlying set; those hypotheses are not met here. Their results for large polynomial-image sets cannot be imported by ignoring the index of H.

## Explicit subset-coefficient consequence

For a moment frequency b and product character chi, set v_x=chi(x)e_p(P_b(x)). The136-subset Fourier coefficient is the elementary symmetric coefficient e136(v). Its logarithmic generating function is

    ∏_(x in D)(1+z v_x)
      =exp(Σ_(j>=1)(-1)^(j-1) S_j z^j/j),
    S_j=Σ_(x in D)chi(x)^j e_p(j P_b(x)).

For1<=j<=136, j is nonzero modulo p, so the same degree-six bound applies. Using only |S_j|<=B gives the standard cycle-index majorant

    |e136(v)| <= [z136](1-z)^(-B)=binom(B+135,136).

Here B=255, hence the majorant is binom(390,136), larger than the trivial number of subsets binom(255,136). Thus the standard distinct-coordinate/subset-coefficient pipeline gains nothing after inserting the actual finite constants. Keeping the exact product classes and applying |H_h(b)|<=N_h gives only

    F_h(a)<=N_h.

The largest exact product-class mass in the archived integer DP is

    6417043898306465355817890560136032291335107637534903232761973368781765385,

about2.334e55 times the required274980728111395088. This is the valid universal bound delivered by that Fourier-triangle pipeline, not evidence of near-uniformity.

Even a hypothetical uniform coefficient bound |H_h(b)|<=sqrt(N_h) would give a Fourier-inversion error of roughly sqrt(N_h), about9.21e18 TIMES the target. This hypothetical calculation is not an asserted bound; it explains why square-root cancellation in each individual subset coefficient, followed by a triangle inequality over all frequencies, would still be insufficient. Near-uniformity needs additional control across frequencies or direct combinatorics.

## A stronger elementary universal cap, still far too large

The six moments and product uniquely determine a residual seven-element subset: Newton identities recover its first six elementary coefficients and the product recovers the seventh. Therefore in a fixed signature fiber, no129-subset can be contained in two distinct136-subsets. Counting inclusions gives the rigorous cap

    F_h(a) <= floor(C(255,129)/C(136,129))
             =19456813239826912104785503475612323471014784594878905504701958237.

This is about7.076e46 times the target. It is stronger than the preceding trivial product-class cap but remains wholly incapable of deciding the fourfold excess question. It is not claimed to be the optimal constant-weight-code bound; no association-scheme optimization was run.

## Relation to the certified Fejer test and scope

The independently certified six-coordinate/eight-harmonic Fejer gate found very small coefficients at those selected frequencies and ruled out that finite collection of sufficient concentration certificates. It does not give bounds at the other p^6-1 frequencies, nor turn a sufficient lower-bound test into a universal upper bound. No inference of global uniformity follows from it.

The actual numerical arithmetic is saved in `WEIL_NEAR_UNIFORMITY_GATE.json`. The rigorous conclusion is limited: **standard complete subgroup Weil/Gauss estimates plus the usual absolute-value subset sieve cannot prove the target impossible at this prime.** A near-uniformity theorem here would need genuinely stronger short-subgroup information or coordinated cancellation. The present audit supplies no such theorem, and the modular fiber target remains open.
