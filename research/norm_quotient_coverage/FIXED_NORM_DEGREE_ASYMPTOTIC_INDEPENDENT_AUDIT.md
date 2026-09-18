# Fixed norm degree: polynomial prime alphabet and asymmetric endpoint audit

2026-09-18. **PASS**, with fixed norm degree and the source asymmetry stated below. This is an application of the existing completion and norm-compiler arguments. The general dimension-shift compiler already reproduces its asymptotic tradeoff, so no asymptotic gain is established.

## Audited theorem

Fix an integer e≥1, 0<ρ<1, β>12/5, and a constant C satisfying

    e/h(ρ) < C < (e+1)/h(ρ),

where h uses natural logarithms. There are unbounded lengths n and primes p, with p=Θ((n/log n)^β), a chosen domain D⊂Fp of size n, and the ordinary prime-alphabet RS code of dimension J=floor(ρn), together with words f,g, such that, writing

    A=J+m−1,       T=J+(e+1)m−1,

one has

    agr(f)=CA(f,g)=A,
    A≤agr(g)≤J+em−1=T−m,
    agr(f+λg)=T  for every λ∈Fp*.

Here m→∞, n=(s+1)m and s=C log p+O(1). In particular every normalized interior mixture (1−t)f+tg, t∈Fp\{0,1}, has exact agreement T. Both endpoints are outside that tested radius. The radius θ=1−T/n lies strictly below the prime-alphabet Elias radius for all sufficiently large members, and p>J.

This theorem asserts exact agreement for the polynomial source and ordinary common agreement; it does not assert an exact agreement for the rational source g.

## Prime family and bias

Choose m among powers of two and a prime p≡1 mod m with p∈[m^β,2m^β], for every sufficiently large such m. The powerful-modulus prime-existence application is already justified from the primary Thorner–Zaman result in PRIME_ALPHABET_PRIME_EXISTENCE_AUDIT.md; its strict β>12/5 hypothesis is retained here.

Let H=(Fp*)^m, reserve a0∈H, and use the population of factors b−a for a∈H\{a0}. Let E=Fp^e and choose b of degree e over Fp. For e=1, additionally choose b∈Fp*\H; this is possible for the growing m. For e≥2, b automatically lies outside Fp. Thus the pole polynomial has no roots on the eventual domain.

The uniform mixed-character bound over Fp*, followed by subgroup-character averaging, is at most e√p for every nontrivial character of E*. Removing the reserved tag costs one. Thus, with P=(p−1)/m−1,

    ε ≤ (e√p+1)/P = O_e(m/√p).

For e=1 this is the usual Jacobi-sum estimate. For e≥2 it is the mixed Katz estimate for the étale algebra E×Fp; all native characters, including norm-descended characters, are covered. Since β>2, both population size and reciprocal bias grow as positive powers of M=p^e−1:

    P=M^((1−1/β)/e+o(1)),
    ε≤M^(-(1/2−1/β)/e+o(1)).

All these statements are uniform in the choice of the full-degree b. The prime p is the code alphabet; E is auxiliary.

## Completion at the exact message dimension

Set s=ceil(C log p), n=(s+1)m and J=floor(ρn). Write uniquely

    J−1=(r−e−1)m+w,       0≤w<m.

Then r=ρs+O_e(1), so r/s→ρ and e+1≤r≤s eventually. The fixed-weight seed-and-pair theorem applies to Γ=E* because

    s/log M → C/e > 1/h(ρ).

It produces s distinct nonreserved tags such that their r-subset products ∏(b−a) cover **all** of E*. The number of completion pairs can depend on the fixed e,ρ,β,C but remains constant as p grows. The bounded rounding discrepancy in r does not affect that theorem.

This is stronger coverage than needed: in particular every λ∈Fp* occurs. There is no conditioning on a subfield event, and no replacement of a distinguished subfield by an arbitrary coset.

## Compiler and descent

Put Y=X^m and let R be the degree-w locator of w points in the reserved fiber. The monic degree-e polynomial

    T_b(Y)=Norm_(E/Fp)(Y−b)

is the minimal polynomial of b and is nonzero on all domain tags. Define

    f=R Y^(r−e),       g=R/T_b(Y).

For a represented native λ=VS(b)∈Fp*, divisibility T_b|(VS−λ) gives the native prime-field witness

    hS=R [T_b(Y)Y^(r−e)+λ−VS(Y)]/T_b(Y).

Its degree is ≤J−1 by cancellation of the degree-r terms. Its residual has exactly w+rm=T zeros. The monic cleared numerator proves the upper bound T against every message. Interpolation on r−e full tag fibers, together with the R zeros, gives the common lower bound A. The monic degree-A source f proves equality for f and CA. Finally, clearing the denominator for g gives a nonzero polynomial of degree ≤J+em−1. These are precisely the independently audited conclusions in NORM_POLE_NATIVE_FIELD_DESCENT_INDEPENDENT_AUDIT.md.

All p−1 nonzero pencil labels are represented, so the Möbius conversion λ=t/(1−t) gives all p−2 normalized interior mixtures, with no uncertainty from losing the omitted pencil label −1.

## Exact normalized gaps and Elias inequality

Write ρ_n=J/n and η=T/n−ρ_n. Then

    η=((e+1)m−1)/n,
    (T−CA)/n = em/n,
    dist(f,code)−θ = em/n,
    dist(g,code)−θ ≥ m/n.

Consequently the exact common-loss fraction is em/((e+1)m−1)→e/(e+1), and the certified smaller endpoint fraction is at least m/((e+1)m−1)→1/(e+1). Also

    η log p → (e+1)/C,
    n=Θ(m log p),   log n=(1/β+o(1))log p,

so η=Θ(1/log n), p=Θ((n/log n)^β), and n=o(p).

For fixed ρ, θ→1−ρ and

    H_p(θ)=θ+h(ρ)/log p+o(1/log p).

Thus

    (1−ρ_n−H_p(θ))log p → (e+1)/C−h(ρ)>0.

This proves strict below-Elias radius with the stated native prime alphabet. It does not rely on the auxiliary alphabet p^e in the entropy comparison. At fixed rate the agreement still approaches ρ, hence this is not first-order DKT tightness.

## Corrected matched comparison: the general dimension shift already matches

The norm theorem above remains valid, but restricting the prior comparison to either t=0 or t=m−2 misses the relevant dimension shifts. The full ledger in DIMENSION_SHIFT_COMMON_GAP.md permits every 0≤t≤m−2. With old fiber size m_o and dimension raised from J0 to J=J0+t, it gives

    agr(f)=CA=J+m_o−1−t,
    agr(g)≤J+m_o−1,
    T=J+2m_o−1−t.

Choose t=floor((1−1/e)m_o), with e fixed and m_o growing. This is admissible eventually, including t=0 for e=1. Then

    common-loss fraction → e/(e+1),
    smaller endpoint guarantee → 1/(e+1),
    η log p → (1+1/e)/C_o,

where s_o=C_o log p+O(1). The original PRIME-group completion only needs C_o>1/h(ρ), and strict prime Elias needs

    C_o < (1+1/e)/h(ρ).

This is a nonempty fixed-width interval. The older note's closing interval concerns the extreme shift t=m_o−2, not these proportional shifts. The same growing-fiber prime family yields polynomial alphabet here. Exact dimension rounding is harmless: divide J−t−1 by m_o to obtain r_o−2 and w_o; then r_o/s_o→ρ.

There is a direct matched ledger. Set m_o=e m_n and t=(e−1)m_n, where m_n is the norm compiler's fiber size, and take C_o=C_n/e. At the same J one obtains exactly

    A_old=J+m_n−1=A_norm,
    upper agr(g_old)=J+e m_n−1=upper agr(g_norm),
    T_old=J+(e+1)m_n−1=T_norm.

The leading domain lengths match because s_o~s_n/e. Exact equality of lengths also holds when s_n+1 is divisible by e; rounding s_n to that residue costs only O(1) tags and leaves every asymptotic statement unchanged. Subset weights and reserved-core sizes may differ, which does not affect these agreement identities.

For a common prime family one can take the modulus e times a growing power of two: its radical is bounded for fixed e, so the same powerful-modulus prime-existence argument applies. Alternatively separate power-of-two families already establish the identical asymptotic exponents and gap fractions without demanding identical primes. Multiplying fiber size by fixed e only changes fixed constants in p=Θ((n/log n)^β).

**Corrected verdict:** the fixed-e norm construction has no established asymptotic improvement over the general dimension-shift compiler. It may give a useful finite-parameter option when available fiber divisibility or prescribed parameters differ, and its auxiliary-field-to-native-field descent is a separate algebraic observation. Those points do not justify presenting its asymptotic gap tradeoff as new.

The paired-domain results also already supply near-total common-loss profiles and balanced two-far profiles in their stated, non-polynomial-alphabet regime. That comparison remains valid but is no longer decisive: the existing general dimension-shift construction is the directly matching polynomial-alphabet benchmark. No literature-priority claim or growing-e theorem is made.
