# Independent audit: biased-population seed plus fixed-cardinality pair completion

2026-09-18. **PASS.** Pure finite-group proof; no computation required. All Fourier estimates below apply to the actual nonuniform population, not to a uniform surrogate.

Let G be a cyclic group of order M, and A⊂G have P distinct elements. Suppose

    |P^(-1) Σ_(a∈A)χ(a)|≤ε

for every nontrivial character χ. Assume asymptotically P≥M^γ and ε≤M^(−κ) for fixed γ,κ>0. Fix0<ρ<1 and C>1/h(ρ), with natural-log binary entropy h. Then, for all sufficiently large M, A contains a set of s=C log M+O(log log M) distinct generators whose products of exactly r=ρs+O(1) elements cover G. More precisely the proof permits any prescribed seed cardinality r0=ρs0+O(1), followed by a fixed number t of pairs, giving s=s0+2t and r=r0+t.

## 1. Seed energy, with exact overlap counting

Sample X1,...,Xs0 iid uniformly from A; let r0∈(0,s0), L=binom(s0,r0), and n_y count index subsets I of size r0 with product X_I=y. Put

    Δ=M Σ_y n_y²/L²−1.

Always Δ≥0. Two index subsets I,J with |I\J|=|J\I|=u have equal-product probability

    M^(-1) Σ_χ |E χ(X)|^(2u).

Cancellation of common indices is exact. There are L binom(r0,u)binom(s0−r0,u) ordered pairs with this u. Consequently

 EΔ ≤ (M−1)/L Σ_u binom(r0,u)binom(s0−r0,u)ε^(2u)
     ≤ (M−1)(1+ε)^s0/L.                         (1)

The last inequality embeds the diagonal u=u terms in the full product (1+ε)^r0(1+ε)^(s0−r0). It includes u=0 correctly.

The iid sample is distinct with probability at least 1−binom(s0,2)/P. Because Δ is nonnegative, conditioning on distinctness increases the bound on its expectation by at most the reciprocal of this probability. Hence a distinct seed realizes

    Δ≤(M−1)(1+ε)^s0/[L(1−binom(s0,2)/P)].       (2)

If its represented support occupies fraction1−h0, Cauchy–Schwarz gives Δ≥h0/(1−h0), so h0≤Δ/(1+Δ)≤Δ. With s0~C log M and r0=ρs0+O(1), (2) is M^(1−Ch(ρ)+o(1)). The assumed strict entropy inequality therefore gives h0≤M^(−δ) for some fixed δ>0.

## 2. Completion step on the remaining population

Suppose B is the represented product set, H=G\B has fraction h, and j fresh pairs have already been used. Delete all seed elements and those2j elements from A, leaving A_j of size P_j=P−s0−2j. The new normalized character bias is bounded by

    η_j=(Pε+s0+2j)/P_j.                         (3)

Choose two distinct elements a,b uniformly from A_j. Extending each existing representation by exactly one of them replaces B by aB∪bB; its holes are aH∩bH. For independent draws with replacement, Parseval gives

    E[|aH∩bH|/M]≤h²+η_j² h(1−h).

Indeed this is the squared L2 norm of the convolution of the normalized population measure with the hole indicator. The trivial Fourier coefficient contributes h²; the nontrivial squared Fourier mass of the indicator is h−h². This is valid without any uniformity assumption on A_j.

Conditioning the pair to be distinct and using nonnegativity yields

    E_distinct[h_new]
       ≤[h²+η_j²h(1−h)]/(1−1/P_j)
       ≤[h²+η_j²h]/(1−1/P_j).                  (4)

Thus some distinct fresh pair satisfies (4). Each completion step uses two new generators, but increases the size of every represented subset by exactly one. All chosen generators remain distinct.

## 3. Why only a constant number of pairs is needed

For any fixed number of steps, (3) is at most M^(−κ0) eventually, where κ0=min(κ,γ)/2>0. Also1−1/P_j≥1/2. If h≤M^(−a), (4) gives

    h_new≤4 M^(−min(2a,a+2κ0)).

For sufficiently large M this implies h_new≤M^(−a−min(a,2κ0)/2). Starting at fixed a=δ, these exponents eventually exceed1 after a number t depending only on δ,κ0. Choose t in advance and require the finitely many inequalities simultaneously. Once h<M^(-1), the integral number of holes is zero. If coverage is achieved early, further fresh pairs preserve coverage, so exactly t steps may always be performed.

No hidden logarithmically growing completion count occurs. No explicit polynomial-time method to locate a good seed or pair is asserted by this existence argument.

## 4. Exact prescribed dimension is compatible

For the fiber compiler with one reserved tag, first choose a completion count t from the fixed positive exponent margins. Set final s=s0+2t, n=(s+1)m, and J=floor(ρn). Define

    r=floor((J−1)/m)+2,    r0=r−t,
    w=J−1−(r−2)m.

Then0≤w<m and r0=ρs0+O(t+1), uniformly in m≥1. Thus the same seed entropy estimate applies, while the completion ends at exactly the compiler's required r. The reserved tag is excluded from the original population; this costs one element/bias term and must be included in the input values P,ε. It does not affect positive fixed power exponents.

The compiler's exact source/common agreement A=J+m−1 and certified near threshold T=J+2m−1 follow from its already audited algebra. The completion changes neither formula.

## 5. Below-Elias window and limits

The entropy condition is C>1/h(ρ). Since the certified agreement is T/n=ρ+2/s+O(1/n), its capacity slack has leading constant2/C when expressed in units1/log M. The q-ary Elias agreement boundary has leading constant h(ρ). Thus choosing

    1/h(ρ)<C<2/h(ρ)

puts the compiler's certified agreement strictly ABOVE the Elias agreement boundary (equivalently its decoding radius strictly BELOW Elias), provided q=M+1 and the compiler's remaining hypotheses hold. This is the intended below-Elias radius window. The two inequalities have a nonempty interval, unlike the earlier first-moment Cauchy certificate.

This receipt certifies the nonuniform group argument and dimension matching. Its application to a particular prime family still requires the independently proved population-size and character-bias estimates, prime-existence input, and quotient compiler. It is not a first-order tightness theorem: at fixed rate the slack still vanishes and remains below DKT's rate-only first-order agreement curve.
