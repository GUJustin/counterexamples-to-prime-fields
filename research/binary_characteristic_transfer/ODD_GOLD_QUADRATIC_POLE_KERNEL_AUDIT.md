# Odd Gold at quadratic exterior poles: kernel and exact fiber reduction

Independent algebra audit, 2026-09-19. The kernel and population bound PASS. No uniform fiber-size or exact nonzero-label count is asserted.

Use the parameters of ODD_GOLD_CUBIC_POLE_EXACT_CLASSIFICATION.md, with m=2s+1, r=p^s, n=p^m, s≥2. Here choose any β∈B₂\B, write β=x+η with x=(β+β^n)/2∈B and η^n=−η, and set aβ=η^(−r−1)∈B*. Let H be the Fp space of Gold traces plus linear traces plus constants.

## 1. Exact evaluation kernel

    ker(evβ:H→B₂)=Fp Kβ,
    Kβ(X)=Ψ_(aβ)(X−x)−1.

For a nonzero quadratic coefficient a, a root β outside B must also be a derivative root by G^p−G=ΛG′. The affine derivative has a unique native root x₀ and all other roots x₀+η₀Fp with η₀^n=−η₀. Thus its native center is x₀=x. Completing the quadratic shows that G=Ψ_a(X−x)+c.

The derivative condition at η is equivalent to c_a=aη^(r+1) satisfying c_a^(p^(s+1))=c_a. Here c_a∈B because r+1 is even, and gcd(s+1,m)=1, so c_a∈Fp*. Conversely this condition is sufficient. Evaluation of the reduced Gold polynomial at η gives Ψ_a(η)=c_a: s+1 unwrapped trace terms contribute +c_a and s wrapped terms contribute −c_a. Thus vanishing forces c=−c_a, giving exactly c_a Kβ. With quadratic coefficient zero, a nonzero affine trace polynomial has no exterior root, so there are no further kernel elements.

The word “center” here is the native root of the derivative, equivalently the unique completion-of-square center; it is not the translation parameter b, which equals −x in bank notation.

## 2. Residual labels and their multiplicities

Every bank locator G is fully split in B, so G(β)≠0. For two bank residuals, the identity

    P(β)^p=Λ(β)^(p−1)−(Λ(β)/G(β))^(p−1)

shows that their labels agree if and only if G₁(β)=uG₂(β) for some u∈Fp*. Equivalently, their projective classes lie on the same projective line through [Kβ]. Each such line has p+1 Fp points, one of which is the kernel point; it therefore contains at most p bank members. Normalized bank locators represent distinct projective points, because their completed level is one.

The zero-label members are exactly

    a=t aβ, b=−x, t∈Fp*, with a in the good square class.

There are exactly (p−1)/2 of them: χ_B restricted to Fp* is χ_p since m is odd. Their G(β) values cannot vanish because every bank G is split natively. All other bank labels are nonzero. Consequently the number of distinct nonzero labels is at least

    ceil((M−(p−1)/2)/p),  M=n(n−1)/2.

For fixed p this is Θ(n²), at every quadratic exterior pole. The bound is not uniform in growing p. Each nonzero threshold list has between one and p witnesses, with exact maximum agreement T. The complete residual classification from the cubic note is field-independent and therefore proves that these fibers exhaust the threshold lists; no extra witnesses occur.

The Ω source argument remains valid over B₂. Its complementary c* is nonzero and outside the threshold bank by the source bound U<T. The affine chart using endpoints f+c*g,c*g retains every nonzero bank label and excludes the zero label (the projective direction point is replaced by reciprocal agreement k). The resulting number of interior exceptions has the stated lower bound, with list sizes bounded by p rather than singleton lists.

## 3. Exact algebraic fiber formula

For any nonzero-label bank locator G, take its p representatives

    G_t=G+tKβ, t∈Fp.

They parametrize all nonkernel projective points on its evaluation line exactly once. Expand G_t=Ψ_(a_t)+Tr(ℓ_t X)+c_t. If a_t=0 it is not a bank point. Otherwise the polar operator

    J_a(b)=a b^r+a^(p^(s+1)) b^(p^(s+1))

is a permutation of B. Put b_t=J_(a_t)^(-1)(ℓ_t), and v_t=c_t−Ψ_(a_t)(b_t). Then G_t is a projective bank point if and only if

    v_t≠0 and χ_B(a_t) χ_p((-1)^(s+1) v_t)=1.

Indeed completion gives Ψ_(a_t)(X+b_t)+v_t; divide by v_t to obtain the unique normalized bank locator. Hence the exact threshold-list size at the corresponding label is the sum of these p explicit indicators. This is a necessary-and-sufficient fiber formula, not an assertion that its value is independent of the pencil. It includes all degeneracies without division by a zero level.

## 4. Prior and scope

The binary primary source already discusses quadratic-extension pole conversion for Gold and elliptic families in fullfield-elliptic.tex, paragraph “Explicit pairs in quadratic extensions,” following its odd-ambient proof. Thus quadratic-alphabet polynomial population is not by itself a new mechanism. The exact one-dimensional evaluation kernel, at-most-p list bound, and exact fiber formula should be compared against that paragraph before assigning novelty. No prime-alphabet consequence follows: the alphabet is F_(n²), not Fp.

## 5. Explicit growing-characteristic comparison

Keeping p visible changes the comparison. The established harmonic collision conversion with population L=M and collision cap δ=p(p−1), at quadratic alphabet size q=n², gives

    ceil(M(n²−n)/(n²−n+p(p−1)(M−1)))−1.

Since M=(n²−n)/2, its unrounded term is

    2M²/[2M+p(p−1)(M−1)],

of order n²/p² as p grows. The exact projective-fiber result above gives at least ceil((M−(p−1)/2)/p), of order n²/p. Their leading ratio is (p−1)/2. At s=2, n=p⁵, these scales are p⁸ versus p⁹=n^(9/5).

The primary source’s odd-ambient proof explicitly states the generic cap δ=(b−1)b^(2j+2h+1−h), which is p(p−1) in the full-rank, unshortened specialization. Its displayed harmonic formula occurs in `thm:fullfield-elliptic`. However the fixed-codimension corollary itself assumes j≥2 on a full domain; j=0 is outside that corollary’s stated quantifiers. Accordingly this is a matched comparison with the existing population/compiler and harmonic conversion method, not a quotation of a theorem claiming all j=0 growing-p parameters. The exact kernel bound is a concrete factor-p improvement over that harmonic bound. It does not alone establish literature-wide novelty.

The collision cap itself is consistent with the current algebra: a collision between two residuals gives G₁−uG₂=0 for some u∈Fp*, and a nonnative root of each difference must be an affine derivative root. There are at most p such roots for each u, hence at most p(p−1) nonnative collision poles. This method loses information about their grouping into projective evaluation fibers, precisely what the kernel argument recovers.

The comparison must also keep dimensions distinct: the inherited degree allowance is k_old=(p−1)²n/p², whereas the exact theorem uses k=k_old−(p−1)p^(s−1). Neither dimension is smaller than the characteristic in this regime. The growing-p count gain does not imply a prime-alphabet result or uniform constant relative source loss.

## 6. Exact quadratic-pole histogram invariance

For any two quadratic exterior poles β,β₀, uniquely choose u∈B*, c∈B with β₀=uβ+c. For each normalized bank polynomial put

    a′=a u^(r+1), b′=(b+c)/u,
    G_new(X)=G(uX+c),
    F_new(X)=u^(1/p) F(uX+c),
    P_new(X)=u^(−D)P(uX+c).

The trace identity for G_new is an exact polynomial identity: the expressions agree at all native points and both have degree d<n. The good square class is unchanged because r+1 is even, and (a,b)↦(a′,b′) is a bijection of the bank. Differentiation gives the displayed F_new. Since Λ(uX+c)=uΛ(X), its residual is u^(1/p−1)P(uX+c). This scalar is u^(−D), because u^(1/p)=u^(n/p) and u^(n−1)=1.

Consequently P_new(β)=u^(−D)P(β₀). The nonzero scalar preserves zero and all evaluation-fiber sizes. Thus the COMPLETE bank multiplicity histogram, not merely a lower bound, is independent of the quadratic exterior pole. By exhaustive residual classification, the complete nonzero affine threshold-list histogram is also independent of the pole after the complementary-source chart.

For (p,s)=(3,2), the separate bounded fixture reports nonzero fiber histogram {1:14210, 2:6246, 3:900}, with one zero-label bank member. The arithmetic check is 14210+2·6246+3·900=29402=M−1 and total nonzero labels 21356. Given that independently produced finite bank certificate, transport proves this histogram at every quadratic exterior pole. This audit establishes the transport algebra; it does not claim to have independently replayed the finite bank enumeration.
