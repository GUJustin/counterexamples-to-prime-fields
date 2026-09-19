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
