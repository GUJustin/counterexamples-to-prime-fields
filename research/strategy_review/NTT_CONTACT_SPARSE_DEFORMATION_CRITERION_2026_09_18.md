# Sparse deformation of the frozen monomial contact test

Exact bounded derivation; no rank computation, source-cap change, or claimed improvement. Read `NTT_CONTACT_48_PROFILE_COMPRESSION_2026_09_18.md` with its local-rank correction and `NTT_CONTACT_LOCAL_RANK_AUDIT_2026_09_18.md`. The monomial word has a guaranteed kernel; actual block ranks and cokernels remain unknown.

Keep p=2130706433,n=262144,w=131071,a=181275,m=115,Q=159,s=35 and all other frozen caps. Let V be the Z-free full-Q source, of dimension 47859086760. For g=0, injectivity on V implies injectivity on the entire Z-capped source, since each Z-coefficient lies in a subspace of V.

## 1. A genuinely closed class of perturbations

If P(X) has degree at most w, the automorphism

 (X,Y,R) -> (X,Y+P(X),R+P'(X))

and its inverse preserve the source: P has weight at most w, P' has weight at most w−1, expansions lower Y/R exponents, and hence preserve both i+j<=Q and j<=s. They also preserve the strict weighted X bound. Locally they identify the contact ideals for received words f and f+P. To see this directly, substitute X=alpha+T,Y=f(alpha)+T R+T²E; the residual Taylor terms after the translation are divisible by T² and are absorbed by an invertible polynomial change of R,E over the local T-ring. Thus divisibility by T^m is unchanged.

For the full source, replacing P by ZP and P' by ZP' also preserves i+j+z<=L: every added Z replaces one Y or R exponent. This proves the same equivalence for changing g by a polynomial of degree at most w.

Consequently f=X^a+cX^b with b<=w, or adding such a monomial as g, cannot remove the existing kernel. These perturbations are exactly codeword translations of the received pair within the frozen capped interface. Exponents of word values may first be reduced modulo n; the statement concerns their low-degree representative.

## 2. Fixed-target local map and character shift

For a potentially useful b>w, write f_c=X^a+cX^b and g=0. At alpha in mu_n normalize

 X=alpha(1+u), R=alpha^(a−1)r, E=alpha^(a−2)e.

The column X^dY^iR^j maps, modulo u^m, to

 alpha^(d+a(i+j)−j) (1+u)^d
 [1+ur+u²e+c alpha^(b−a)]^i r^j.

This gives an exact polynomial matrix M(c)=M0+cM1+... of degree at most Q in c. Its target is fixed: use the local image I spanned by u^d(ur+u²e)^i r^j with the original i,j caps and 0<=d<m. Translation by the received value preserves this space. All original X-prefixes contain these local u powers (the smallest prefix length exceeds m), so dim I is the independently audited 182580. The full target is the direct sum of I over the n nodes.

The cyclic action diagonalizes M0. Its c-linear term changes source character chi to target character chi+(b−a) modulo n. Explicitly M1 is multiplication by alpha^b followed by differentiation in Y in unnormalized local coordinates. For a perturbation g=cX^b, the analogous term also multiplies by Z; the same cyclic shift holds, with the challenge exponent raised by one.

This is an exact matrix formula; no rank is inferred from profile dimension alone.

## 3. First-order obstruction map and a two-layer reduction

Let K=ker M0 and C=coker M0, using the fixed local target just specified. The canonical first-order obstruction is

 B_b:K -> C,  F -> [M1 F].

If B_b is injective, then M(c) is injective over F_p(c). Proof: an allegedly nonzero formal kernel vector can be divided by its minimal c-valuation. Its constant term F0 is nonzero and lies in K. The next coefficient equation forces M1F0 into im M0, contradicting injectivity of B_b. Equivalently a maximal minor has a nonzero leading coefficient after separating the rank-r0 block of M0. The converse is not asserted: higher-order obstructions can still kill a vector in ker B_b.

The obstruction respects the shift:

 B_b,chi:K_chi -> C_(chi+b−a).

Thus a first-order certificate must in particular satisfy dim K_chi<=dim C_(chi+b−a) for every chi. These dimensions use ACTUAL ranks, not just 182580 or the source counts. The endpoint support-domination compression for M0 cannot be blindly reused for these shifted obstruction maps.

There is a useful exact row reduction. For F in K, its full local substitution is divisible by u^m. Differentiation in e equals u² times differentiation in normalized Y. Hence M1F is divisible by u^(m−2). Modulo u^m, it lives only in the last TWO contact layers u^113,u^114. Therefore it suffices to project those layers into the cokernel. An actionable exact certificate is: construct bases of K_chi and enough dual vectors annihilating im M0 in the destination character, pair them with M1, and show each resulting obstruction block has full column rank. This focuses the new algebra on top contact layers rather than recomputing a dense perturbed matrix. Neither these bases nor their ranks have been computed here.

With multiple sparse perturbations one gets the sum of the corresponding shifted maps, with independent scalar parameters; the same formal obstruction criterion applies over their rational function field. There is no proof that all high-degree sparse words retain kernels.

## 4. Generic parameters are not automatically prescribed-field parameters

A successful obstruction certificate proves generic injectivity over F_p(c). It does NOT by itself supply c in F_p. A nonzero maximal minor has degree at most Q*dim(V)=159*47859086760 in c, much larger than p; it could vanish at every element of the prime field. Over an extension with more elements than that degree, some specialization is nonzero. The existing proposed F_{p^6} alphabet easily meets this size bound, but its admissibility must be checked against the precise frozen-source theorem before claiming a counterexample to that theorem. No such source-convention assertion is made here.

For an actual prime-field falsification one needs an explicit c with a verified nonzero minor, a determinant-degree/root exclusion sharpened below p, or another argument preventing all prime-field specializations from vanishing. A special-word injectivity result can refute a uniform kernel assertion only over an alphabet actually covered by that assertion. Conversely the present guaranteed monomial kernel does not prove a universal source repair or change the final charge ledger.

## Bounded next mathematical target

Exclude all degree<=w perturbations by the translation lemma. For one named b>w, seek a formula for the two-layer maps B_b,chi and a symbolic left inverse or nonzero pairing certificate. Stop short of numerical rank claims until actual kernel/cokernel information is supplied. This is a new exact deformation criterion, not a proposed large matrix job or a recycled random-word scan.

## Root review

Independently checked the source-cap invariance, the first-order formal-kernel proof, and the two-layer support claim. The latter follows from the exact polynomial identity partial_E(F after substitution)=T^2*(partial_Y F after substitution); divisibility by T^115 therefore gives T^113 after differentiating in Y. The determinant-degree warning is necessary. No actual obstruction-map ranks were established.
