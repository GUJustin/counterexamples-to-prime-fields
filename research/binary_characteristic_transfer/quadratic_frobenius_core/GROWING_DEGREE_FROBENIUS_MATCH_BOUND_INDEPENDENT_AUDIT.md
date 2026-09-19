# Independent audit: growing-degree Frobenius match bound

**PASS for the quarter-density, unpadded construction.** This does not apply unchanged to the neutral-padded9p² construction. No manuscript was edited.

Sources inspected: `GROWING_DEGREE_FROBENIUS_MATCH_BOUND.md`, `scaled_fiber_padding.tex`, and the actual intended domain in `density_quarter_puncturing.tex`.

For P in B[X], B=F_(p²), of actual degree d>2, a matching t satisfies z=t^p, z²=P(t), and t²=P^sigma(z). Writing P^sigma(Z)=E(Z²)+Z O(Z²) gives the stated necessary eliminant

[X²-E(P(X))]²-P(X)O(P(X))².

For even d its first square has a unique nonzero leading term of degree d²; the second product has degree at most d(d-1). For odd d the second product has unique nonzero leading degree d², while the first composed square has degree at most d(d-1). The X² cross terms and X^4 term are lower because d>2. Thus the eliminant is not identically zero and has at most d² roots.

On each of the four physical B-lines, rescaling the coordinate and received leading coefficient gives precisely that equation, with the line parameter absorbed into the constant coefficient of P. Rescaling does not change actual degree d. If the normalized coefficients are not all in B, a B-linear projection annihilating B yields a nonzero polynomial of degree<=d at every match. If they are all in B, apply the eliminant. Each component therefore contributes at most d², and arbitrary deletion of second-block coordinates can only decrease the count. Hence any genuinely degree-d witness contributes at most4d² on the intended domain.

For p>=257 and 3<=D with4D²<=2p, all newly admitted degree3,...,D witnesses therefore have agreement<=A=2p on EVERY member of the normalized affine line. Old quadratic witnesses remain, so every list at every threshold strictly above2p is exactly unchanged, including its witness identities and multiplicities. Both source agreements remain exactly2p, and common agreement remains exactly2p by the simultaneous old quadratic witness on D0. The inequalities are valid with equality4D²=2p: the target threshold is strictly greater thanA.

The intended length and threshold are

n=(5p²-1)/2,  T=ceil(sqrt(5p²-1))-1.

The new dimension is D+1, and T<sqrt(2n). In this tiny-rate regime the first-order curve satisfies n*a1((D+1)/n)>sqrt((D+1)n/2). For D>=3 the latter is at leastsqrt(2n)>T. Thus first-order placement is LOST immediately upon admitting cubic witnesses. The construction remains below the enlarged Johnson threshold but is no longer an above-first-order example. With D=Theta(sqrt p), its dimension is Theta(sqrt p), rate Theta(p^(-3/2)), and label count Theta(p³)=Theta(n^(3/2)); this is a tradeoff, not the sought stronger lower-bound regime.

Important scope correction added to the candidate note: if the5p²+4 neutral points of `scaled_fiber_padding.tex` are retained, X³ itself is a newly admitted codeword and agrees with every finite pencil member on all those points. Then the claimed source agreement and list preservation fail. The no-neutral hypothesis is therefore essential, not cosmetic.

## Independent audit of the primitive-scale strengthening

**PASS with primitive s and no neutral padding.** The normalized leading-coefficient quotient is exactly s^(d-2)*v^((delta-epsilon)*d) modulo B*. Since E*/B* has orderp²+1, primitivity makes its exponent test valid. Its parity cases exclude simultaneous good components in different blocks for every3<=d<=p. Root counting on the single possible good block and coefficient projection on the other prove2p+2d. No quadratic elimination estimate is needed for this strengthening.

For D=floor(p/20), p>=257, the exact positive quadratic (59/100)p²-(21/5)p-3 proves2p+2D<T. Therefore every threshold list, including the exceptional multiplicities, is unchanged. The correct source/common assertion is the interval[2p,2p+2D]; claiming exact2p here would be unsupported. The capacity-relative gap lower limit is (sqrt5-2.1)/(sqrt5-0.05), while dimension isTheta(p) and rateTheta(1/p). First-order placement is lost, as explicitly stated in the consolidated candidate.

The earlier exact-source variant is retained rather than overwritten. This audit does not supply a concrete selected domain at a large practical prime; its domain selection remains the existence argument of the quarter-density theorem.

## Bounded prior-work comparison: basic KKH canonical bank

The primitive-scale variant has, over the SAME ambient alphabet E=F_(p^4),

n~(5/2)p², k~p/20, A<=2.1p, T~sqrt5*p,
B=(p+1)(p²-1)~p³, and characteristic p>k.

It has a positive source/common-loss-to-capacity-margin ratio but lies below first order. No first-order requirement is imposed in the following comparison.

Primary source reread: Krachun--Kazanin--Haböck, *Failure of proximity gaps close to capacity*, ePrint2026/782, Section2.1 and AppendixA equations(5)--(6), Propositions3--4. The archived primary text is

`/Users/jthaler/Dropbox/Documents-full-2026-09-16/Documents/stwo_audit_2026-09-15/sources/actual_list_literature/kkh2026_782.txt`.

Section2.1 and AppendixA both explicitly use polynomial degree at most(r-2)m. Hence their strict message dimension is k0=(r-2)m+1, domain length n=sm, canonical agreement rm, and at most binom(s,r) distinct canonical labels (there is one label assigned to each subset). Grant arbitrary positive integer fiber sizes and any field supporting them; this is more permissive than the literal prime-field, power-of-two subgroup hypotheses of the primary theorem. It also grants whatever pole choice separates the canonical labels. The following ceiling therefore does not rely on an unfavorable alphabet or subgroup-existence assumption.

Allow code enlargement to k>=k0 and tested-threshold weakening to T<=rm. If r>=3, then

T/k <= rm/((r-2)m+1) < r/(r-2) <=3.

But the new variant has T/k tending to20sqrt5>44. Thus no r>=3 basic canonical bank matches these dimensions and agreements. Only r=2 remains. Then m>=T/2, s=n/m<=2n/T, so

B_canonical<=binom(s,2)<2n²/T²=O(n)=O(p²).

This is strictly below the new Theta(p³)=Theta(n^(3/2)) canonical population. Enlarging the alphabet to E, even allowing every canonical support to have a distinct native E-label, does not increase the number of subsets. Conversely the literal primary prime alphabet has characteristic at least its domain length and cannot directly have the new characteristic p~sqrt n; the field-independent ceiling above already rules out matching even after generously relaxing that issue.

The same basic count conclusion survives standard common-zero padding: with padding degree w, k0=w+(r-2)m+1 and canonical agreement w+rm. For r>=3 this is at most3(k0-1). For r=2, w<=k-1 implies m>=(T-k+1)/2 and the canonical count is at most2n²/(T-k+1)²=O(n) in the matched regime. This paragraph concerns that explicit padding ledger only.

**Scoped conclusion.** The new growing-dimension tradeoff is not already supplied by the basic KKH canonical subset bank with code enlargement and threshold weakening, even without asking for first-order placement, exact lists or the same source bounds. The decisive difference is the simultaneous ratio T/k and superlinear canonical count, not merely the lack of an endpoint or singleton assertion in the prior theorem. The earlier local r=2 quadratic-enlargement result also has only a linear canonical count and does not remove this mismatch.

This is NOT a novelty certificate against all constructions in KKH or the literature. It gives no upper bound on additional noncanonical witnesses/labels that might appear upon code enlargement, and does not cover arbitrary transformations, new denominator compilers, or a strategically punctured larger construction. It therefore supports only the concrete non-subsumption claim above; no priority or general optimality claim follows.
