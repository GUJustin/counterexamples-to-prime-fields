# Dickson collision energy: remove the forced square shape exactly

September 18, 2026. Proved identities and scoped energy bounds; no construction scan. Builds on NONDIVISOR_DISCRIMINANT_GATE.md and its independent audit. The new replay is verify_dickson_excluded_shape.py/json, separate from the older verifier.

Let p be odd, H=mu_n in Fp*, 3≤e<n, k=e-1 coprime to n. For t in H minus {1},

    v_t=4-4 t^(k-1)(t-1)²/(t^k-1)².

Remove v=0 as in the earlier gate. Write M_v for the retained multiplicities, m'=sum M_v, E*=sum M_v², C*=sum M_v chi(-v), and J(beta)=chi(beta)sum M_v chi(beta-v). Admissible full-coefficient nonsquare quadratics have beta=b²/(ac) outside {0,4}.

## 1. A forced square relation and exact improved moments

For EVERY t in the domain, 4-v_t is a nonzero square. If n is even, k is odd, so t^(k-1) is a square. If n is odd, every element of H is already a square in Fp. The remaining factor is an explicit nonzero square. Therefore

    J(4)=m'.

This is not an additional hypothesis about Dickson polynomials or a character-sum estimate. Removing both forbidden shapes beta=0,4 from the earlier exact moments gives

    N=p-2,
    sum J(beta)=-2m',
    S2=sum J(beta)²=p E* - 2m'² - C*²,

where both sums now run over beta outside {0,4}. In particular one must not spend this deterministic beta=4 spike on possible admissible shapes.

If a positive necessary threshold is K=A(A-2)-(n-1)+B0, the one-sided variance bound becomes

    # qualifying shapes ≤ (N S2-4m'²)/(S2+N K²+4K m').

Proof: apply the nonnegative shift-square argument to a sample of size N with mean -2m'/N. If its variance is zero, no positive threshold is reached. All denominators in the displayed bound are positive for K>0.

Even one qualifying shape requires

    S2 ≥ K² + (K+2m')²/(p-3).

Indeed, once a value x≥K is chosen, the other p-3 values sum to -2m'-x; Cauchy gives the claimed minimum at x=K. This strengthens S2≥K² and is equivalent to asking that the one-sided count bound be at least one.

For n/p→1, A/sqrt(p)→c with c²>3/2, and m'/p→gamma, a necessary asymptotic condition is

    liminf E*/p ≥ 2 gamma² + (c²-1)²

(and retaining C*²/p² can only strengthen it). In the important small-zero-fiber case M0=o(p), gamma=1 and the floor is 2+(c²-1)², strictly above 9/4 at the target. The qualification M0=o(p) is necessary: n~p by itself does not imply m'~p. The original pair-root budget separately forces gamma≥c²-1 for any viable sequence.

Thus a proved energy upper bound E*≤(9/4+o(1))p, with negligible zero fiber, would close the strict c²>3/2 target. No such uniform energy theorem is asserted here.

## 2. Exact inverse-Dickson reduction

Let D_r(z) be defined by D_r(u+u^-1)=u^r+u^-r. Suppose r k=±1 modulo n, with r≥2 and gcd(r,n)=1. Substitute t=u^r, a permutation of H. Since the denominator is unchanged by inversion,

    v_(u^r)=4-4 S_r(z),
    z=u+u^-1,
    S_r(z)=(D_r(z)-2)/(z-2).

The quotient S_r is a monic polynomial of degree r-1. At the selected u≠1, z≠2, so the identity follows by literal cancellation. For every nonzero v, the polynomial equation S_r(z)=1-v/4 has at most r-1 roots, and each z has at most two u-preimages. Hence the PROVED bound is

    M_v≤2(r-1),       E*≤2(r-1)m'.

This holds even when the displayed exponent k has size comparable to n; the controlling degree is its inverse height, not k. It uses no Weil estimate or genericity assumption.

For odd r=2s+1 there is the further exact identity

    S_r(z)=[1+D_1(z)+...+D_s(z)]².

It follows by squaring u^(-s)(1+u+...+u^(2s)). For even r=2s,

    S_r(z)=(z+2)V_(s-1)(z)²,

where V_(s-1)(u+u^-1)=(u^s-u^-s)/(u-u^-1). In particular S_2=z+2 and S_3=(z+1)². For inverse height two all retained fibers have exactly two elements, giving E*=2m' exactly. Here n is odd, so u=-1 is absent and the inversion symmetry has no retained fixed point.

## 3. Why small inverse height is not a hidden construction

The SAME substitution bounds actual agreement. If x=u^r then x^e=u^(r+1) or u^(r-1) on H. Thus Q(x)=x^e becomes

    a u^(2r)+b u^r+c-u^(r±1)=0.

For r≥2 this is a nonzero polynomial of degree 2r (a≠0). Consequently A≤2r. Fixed inverse height therefore cannot support a growing sqrt(n) agreement bank, even though its collision energy is exceptionally small. Any surviving family needs inverse height at least A/2 as well as the previously known forward-degree requirement.

This is an exact restriction on a structural exponent family, not a blanket monomial obstruction. At inverse height comparable to sqrt(n), the proven energy bound is too large to settle the target. The remaining positive task is an exponent family with both heights large and unusually favorable ADMISSIBLE-shape bias; neither the unavoidable beta=4 spike nor a large removed zero fiber can supply it.

## Validation scope

The bounded stdlib replay covers the same p=11,17,31,47 and full/half-size domains as the earlier moment verifier. It checks every coprime exponent, every positive integer moment threshold through n, the forced-square identity, both excluded-shape moments, the one-point bound, and the inverse-Dickson fiber estimate. It is identity validation, not a search for a new bank. No larger finite-field job or claim of prime-field construction is made.
