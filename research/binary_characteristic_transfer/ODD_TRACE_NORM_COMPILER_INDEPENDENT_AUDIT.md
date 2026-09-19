# Odd-characteristic norm–trace compiler: independent algebra audit

2026-09-19. **PASS** for the construction specified below. No manuscript edits or finite scan. This verifies the refinement's identities/count; it does not claim the fixed-characteristic phenomenon is new relative to the archived norm compiler.

Fix an odd prime p, integer s≥2, Q=p^s, B=F_(Q²), E=F_(Q⁴), and beta∈E\B. Let n=Q² and

    d=(n+Q)/p, T0=n−d, D=n−n/p,
    k=(p−1)T0/p, Λ=X^n−X.

Here k is an integer because s≥2. For a∈F_Q*, b∈B, c∈Fp* define

    G=Tr_(F_Q/Fp)(a(X+b)^(Q+1))+c,
    F=a^(Q/p)(X+b)^(Q/p).

The trace expression means the sum of p-power polynomials, not a trace defined only after evaluation.

## Roots, normalization and the exact head gap

On B the inner (X+b)^(Q+1) is a norm to F_Q. A nonzero trace level has Q/p norm values, all nonzero, each with Q+1 preimages. Hence G has exactly d distinct native roots and degree d. Its leading coefficient is a^(Q/p), the same as F. Telescoping gives

    G^p−G=a(X+b)^Q Λ=F^p Λ.

Set J=Λ/G and P=FJ. Then P is monic of degree D and

    P^p=Λ^(p−1)−J^(p−1).

The root −b of F is not a root of G because c≠0, and already belongs to J. Thus P has exactly T0 distinct native roots, all in B. Multiplicity at the center adds no extra coordinates.

The leading term on the right is X^(pD). The next term of Λ^(p−1) has degree (p−2)n+1, while deg J^(p−1)=(p−1)T0=pk. For odd p and Q≥p², pk>((p−2)n+1), since their difference is [Q²−(p−1)Q]/p−1>0. Therefore deg(P−X^D)≤k. No characteristic-two cancellation is assumed here.

## All differences split natively, giving exact injectivity

Consider the Fp-space of polynomials

    Tr_(F_Q/Fp)(A X^(Q+1)) + Tr_(B/Fp)(lX) + c,
    A∈F_Q, l∈B, c∈Fp.

If A≠0, completing the norm reduces to the same form centered at some b. For nonzero trace level there are d simple native roots. At zero level there are d−Q distinct native roots; the center has multiplicity Q+1 and the others are simple, so the full degree d still splits over B. If A=0,l≠0, the polynomial is a nonzero affine full trace polynomial of degree n/p and has n/p distinct native roots. The nonzero constant case has no roots. Thus EVERY nonzero polynomial in this space has all its algebraic roots in B. Evaluation at beta is injective.

This space has dimension 3s+1 over Fp: the mixed exponents (Q+1)p^i do not collide with the linearized p-power exponents, and the two trace coefficient maps are injective. Its dimension is compatible with dim_Fp(E)=4s.

Equal values P1(beta)=P2(beta) imply J1(beta)^(p−1)=J2(beta)^(p−1), hence G1(beta)=rG2(beta) with r∈Fp*. The difference belongs to the preceding space, so injectivity forces polynomial equality. The original parameter family is free modulo simultaneous Fp* scaling of a,c; scaling F and G together leaves P unchanged. Its number of classes is n(Q−1). Equivalently normalize c=1: all n(Q−1) pairs (a,b) then give distinct P(beta). None is zero because every root of P is native. Normalizing G alone without the same scaling of F would destroy the monic P convention.

## Sources and fixed-rate placement

Put f=(X^D−beta^D)/(X−beta), g=1/(X−beta). For each label lambda=P(beta), the codeword

    q=(X^D−P+P(beta)−beta^D)/(X−beta)

has degree<k and matches f+lambda*g on exactly T0 native coordinates. Over F_(Q⁸)=E⊕omega E, endpoints f+omega*g and f+(omega+1)*g each have exact agreement k by coefficient projection onto g. Their ordinary common agreement is k. All n(Q−1) labels remain distinct interior affine parameters. This certifies that many witnesses; it does not by itself classify all lists or prove singleton behavior.

Finite Johnson slack at threshold T0 is

    n(k−1)−T0²=(Q/p)T0−n>0

for every odd p and s≥2. At fixed p with s→infinity,

    rho=k/n→(1−1/p)²,
    T0/n→1−1/p=sqrt(lim rho),
    (T0−k)/n=T0/(pn)→(p−1)/p²,
    number of certified labels=n^(3/2)−n.

Thus the normalized margin is positive at fixed p, and projection makes both endpoint losses equal that entire margin. The threshold approaches Johnson from below.

There is also a direct finite first-order check. Let c=(p−1)/p and a=T0/n=c−1/(pQ), so rho=c*a. The high-rate boundary polynomial equals

    (8−rho)a²−6rho*a+rho(4rho−5)
      =a*[3(p−1)Q²−(4p²+2p+2)Q−(p−1)]/(p³Q²)>0.

The bracket is increasing for Q≥p² and positive there for p≥3; at Q=p² it is 3p⁵−7p⁴−2p³−2p²−p+1>0. Since rho≥34/81 lies on the high-rate branch, this puts the tested agreement above the full first-order curve. This does NOT permit a large-characteristic DKT application: p is fixed while k grows.

For p=3,s=2 the exact parameters are n=81,d=30,T0=51,D=54,k=34, with648 distinct normalized labels. No enumeration is claimed in this audit.


## Matched comparison with the inherited full-rank high row

I read Section 1 of GOLD_AND_NEAR_JOHNSON_LEDGER.md. Its specialization to characteristic p, full domain dimension 2s and full quadratic rank parameter s already has the same agreement T0, list population M=n(Q−1), and dimension

    k_old=(p−1)² n/p².

Thus constant rate, constant normalized common gap, and the n^(3/2) population scale at fixed p are INHERITED, not new construction claims. The improvements audited here are the explicit coefficient formulas, exact injectivity for every exterior pole, and the smaller valid dimension

    k_old−k=(p−1)Q/p².

The archived conversion supplies a harmonic lower bound on distinct labels. At the natural pole field |E|=n² and fixed p this already retains M(1−O(n^(−1/2))) labels, so the injectivity refinement removes a finite collision loss rather than changing the asymptotic exponent. It also replaces an averaging/existence argument by every-pole injectivity for this exact family.

Lowering k reduces the Johnson bound, bringing the same agreement closer to it, but the positive slack computed above survives. It also reduces the first-order curve, which can change finite placement. At the smallest odd instance p=3,Q=9, the inherited k_old=36 has first-order sign −760/6561 and Johnson slack234, whereas the sharpened k=34 has first-order sign1496/59049>0 and Johnson slack72. Thus the lowering makes this finite instance cross above the full first-order curve while staying below Johnson. At p=3,Q=27 the old and new first-order signs are both positive; the asymptotic relevant-window phenomenon is not new.

This comparison does not revise any prior claim about prime alphabets or large-characteristic applicability. The fixed-characteristic extension-field construction was already present in the archived source.

## Native-field Omega source bound and lossless endpoint chart

Independent algebraic audit: PASS. Keep the notation above and put
`c_*^p = Lambda(beta)^(p-1)`, with the unique pth root in E. For any
strict-degree-k witness to `r0=f+c_*g`, its residual is
`P=X^D+C`, `deg C<=k`, and `P(beta)=c_*`. Define
`Qpoly=P^p-Lambda^(p-1)` and
`Omega=P' Qpoly-P Lambda^(p-2)=(P Qpoly)'`.
The cancellation of the leading term gives `deg Qpoly<=pk`; here the
next term of `Lambda^(p-1)` has degree `(p-2)n+1<=pk`.
Since p divides D, `deg P'<=k-1` (and <=k-2 when p divides k).
Consequently

`deg Omega <= max((p+1)k-1, D+(p-2)n)`.

At each native root x of P, Lambda has a simple root, and Qpoly has
order exactly p-1. Thus P Qpoly has order at least p. If that order
is exactly p its leading derivative vanishes in characteristic p;
otherwise differentiation loses at most one order. In either case
Omega vanishes to order at least p. This argument does not assume
that the native roots of P are simple.
On the other hand, Qpoly(beta)=0 and
`Omega(beta)=-c_* Lambda(beta)^(p-2)!=0`. Thus Omega is not the zero
polynomial, so native agreement is at most the degree bound divided
by p.

The exact difference between the two displayed degree bounds is
`((Q-p^2)(Q+1))/p^2 >= 0` for s>=2. Therefore

`agr(r0) <= U=floor(((p+1)k-1)/p)`.

Using `k=(p-1)T0/p` gives
`T0-U=ceil(T0/p^2+1/p)>0`. The reciprocal source
`r1=c_*g` has exact agreement k, and the ordinary common agreement
of r0,r1 is exactly k: its upper bound follows from r1, and its lower
bound follows from simultaneous interpolation on any k coordinates.
For every bank label lambda, lambda is nonzero and cannot equal c_*,
because its witness has T0>U matches. Under
`t=1-c_*/lambda`, the affine combination of the endpoints is
`(1-t)r0+t r1=(1-t)(f+lambda g)`.
Thus all M distinct bank labels survive as distinct interior affine
parameters; there is no chart loss. This proves certified witnesses,
not an unproved classification of every threshold list.

For s=2 both degree bounds coincide, U=D-p^2 and
`T0-U=p^2-p`. In the p=3,Q=9 example the source bounds are U=45
and k=34, the threshold is 51, and all 648 bank parameters survive.
The method and fixed-rate phenomenon are inherited; the sharper
finite dimension and resulting finite numerical bounds are the
refinements audited here.

## Actual primary-note second pass

Read the complete saved `ODD_TRACE_NORM_EXACT_COMPILER.md`, including its alternative Omega double-root proof, exact finite signs, and matched-prior comparison: PASS. SHA256 at this review: `8eada0284719216b0932742ca6e79034cb9e76751e5c57494a598f3be410c40c`. This hash records the research note, not a later manuscript fragment.
