# Extension-native labels on a chosen prime-field short domain

2026-09-18. **PASS**, including an independent exact sufficient certificate for the proposed Goldilocks parameters. This is a chosen-domain existence result, not the prescribed NTT-domain benchmark and not an explicit enumeration of native labels.

## Primary mixed-character bound, including norm-descended characters

Let E=F_(p^d), let b generate E/F_p, let H=(F_p*)^m, and let χ be ANY nontrivial character of E*. Extend base-field characters ψ by zero at zero. Apply Katz's Theorem2 to the finite étale F_p-algebra E×F_p, its regular element(b,0), and character χ×ψ. Regularity holds because the d conjugates of b are distinct and none is0. The algebra has dimension d+1, so

    |Σ_(a∈F_p*) χ(b−a)ψ(a)|≤d sqrt(p).

The sign adjustment between a−b and b−a is constant of modulus1. χ×ψ is nontrivial for every χ≠1, regardless of whether χ descends through a norm. Katz's proof explicitly preserves nontriviality after splitting by composition with a surjective norm; distinct regular punctures then preclude cancellation of all local ramification. Thus no omitted-character exception exists.

Averaging over the m base-field characters trivial on H gives |Σ_(a∈H)χ(b−a)|≤d sqrt(p). Delete the reserved tag a0∈H. For the population A={b−a:a∈H\{a0}}, size P=(p−1)/m−1, every nontrivial character of the NATIVE target group E* has normalized mean at most

    ε=(d sqrt(p)+1)/P.

This is an immediate specialization of the primary Katz construction already audited, not a replacement of E*-characters by base-field characters. Primary: Katz, *An Estimate for Character Sums*, Theorem2 and pp.198–199, https://web.math.princeton.edu/~nmk/old/estcharsums.pdf .

## Finite theorem and code scope

Apply the finite fixed-cardinality seed/pair lemma with group order M=p^d−1 and the preceding P,ε. Whenever its finite recurrence reaches Mh_t<1, it yields s distinct tags and exact r-subset product coverage of E*. Choose D={x∈F_p*:x^m∈G∪{a0}}, n=(s+1)m, and J−1=(r−2)m+w. Select w reserved-fiber points and their locator R.

The words f=R(Y^r−b^r)/(Y−b), g=−R/(Y−b), Y=X^m, take values in E on a domain contained in F_p. Their denominator is root-free because b∉F_p. The code consists of E-coefficient polynomials of degree<J. All root-count arguments remain valid over E and count the same distinct base-field evaluation points. Interpolation in Y on base-field tags is allowed over E. Consequently

    agr_J(f)=agr_J(g)=CA_J(f,g)=J+m−1,
    agr_J(f+λg)=J+2m−1 for EVERY λ∈E*.

The upper interior bound uses the monic degree-T residual and hence covers arbitrary E-coefficient competitors, not only base-field codewords. Normalized affine mixtures have exactly q−2 interior parameters at that distance and two far endpoints, where q=p^d.

## Independent Goldilocks sufficient certificate

Take p=2^64−2^32+1, d3,m1024,s255,n262144,J131072,r129,w1023,t4. Then s0247,r0125 and

    P=18014398505287679,
    ε≤(3*2^32+1)/P<2^−20,
    L0=binom(247,125)>2^242,
    M=p^3−1<2^192.

All the following are exact integer/rational checks:

- binom(247,2)/P<1/2, so the distinctness probability lower bound exceeds1/2;
- 247ε<1/2, so (1+ε)^247≤1/(1−247ε)<2;
- consequently the seed upper bound h0<4*2^192/2^242=2^−48;
- for every j0,1,2,3, P_j=P−247−2j>2 and (Pε+247+2j)/P_j<2^−20;
- if h_j≤2^−48, the recurrence gives h_(j+1)<2(h_j²+2^−40h_j)<2^−38h_j.

Thus h4<2^−200 and Mh4<2^−8<1. This is a strict sufficient proof without floating-point square roots or exponentially large product enumeration. The estimate sqrt(p)<2^32 is immediate. If a primality certificate is desired, p is Proth form(2^32−1)2^32+1 with odd coefficient<2^32, and exact modular exponentiation gives7^((p−1)/2)=−1 mod p, certifying primality by Proth's theorem.

The code parameters therefore have exact source/common agreement132095 and exact interior agreement133119. Capacity margin is2047/262144; source-to-interior gap is1024/262144. Characteristic p is much larger than J. The challenge alphabet is E=F_(p^3), and all q−2 interior affine mixtures are covered.

The domain is a CHOSEN union of256 cosets of the order1024 subgroup of F_p*, not the prescribed μ262144 domain. No prescribed-domain benchmark improvement follows. No below-Elias assertion is made here: Elias must use q=p^3, and its comparison is a separate exact entropy calculation.
