# Split monomial/constant bank: independent proof audit

2026-09-18. **PASS**, including the strengthened block-size-14 variant. This is an elementary finite construction with linear-in-length exceptional count, a constant native fraction when p=Θ(n), and source loss comparable to its vanishing capacity margin. No novelty assertion is made.

## 1. Exact core and distinct labels

Let t≥2 and p be an odd prime large enough for the choices below. Let z generate the squares in Fp*, of order h=(p−1)/2, and require t²<h. For 0≤i,j<t put

    a_i=z^i,       b_j=z^(tj),
    Q_i(X)=a_i X²,       P_j(X)=b_j.

The ratios b_j/a_i have exponents tj−i, which are distinct integers in a single interval of length t². They are therefore distinct modulo h. The products a_i b_j have distinct exponents i+tj in [0,t²−1]. All these field elements are nonzero squares.

Use both roots of x²=b_j/a_i as core coordinates, and set f=b_j,g=0 there. There are exactly 2t² distinct coordinates. Each is owned by exactly Q_i and P_j; every one of the 2t bank words has 2t core matches. A quadratic outside that bank has at most 2t core matches, by counting at most two intersections with each of the 2t owners and two owners per matched coordinate. A pure cX² not among the Q_i has zero core matches.

## 2. Fresh blocks and neutral coordinates

Choose t disjoint sets S_j, each of size D=14t, outside zero and the core. On S_j set

    f=0,       g=x²/b_j.

Set T=16t, n=128t²+1. Choose two distinct nonsquares α,β∈Fp*. Both lie outside the square good-label set {a_i b_j}. Add n−16t²=112t²+1 neutral points with g=0,f=x³, excluding all previous coordinates, zero, every root of x³−Q_i and x³−P_j, and every point

    x=α/b_j or β/b_j.

There are at most 6t+1 additional excluded points. Thus p>n+6t+1 is a sufficient field-size guard, along with t²<h. One may take a prime 256t²<p<512t² by Bertrand's theorem, for all t≥2. These choices give p=Θ(n), without a progression or splitting condition.

## 3. Complete finite-pencil profile

Consider f+λg and all polynomials of degree at most two.

* If λ=a_i b_j, Q_i matches its 2t core points and all D points of S_j. It has no other fresh matches and no neutral matches, so its agreement is exactly T=16t.
* For any nonzero λ, a pure quadratic cX² has a full fresh block precisely when c=λ/b_j, for a unique j. Otherwise it has no fresh matches. If λ is not good, none of these t slopes is a bank slope, so each has zero core matches. A nonbank pure quadratic has at most one neutral match, at x=c.
* Every nonpure quadratic has at most 2t core matches, two matches per fresh block, and three neutral matches: at most 4t+3<T. This includes the bank constants as a valid upper bound. The zero polynomial is treated separately.

Consequently every nonzero good label has a singleton T-list, containing Q_i, and every nonzero nongood label has maximum agreement either 14t or 14t+1. At the selected nonsquare endpoints α,β, the extra neutral exclusions remove that possible one-coordinate gain, so both maxima are exactly 14t. Each endpoint has precisely the t pure nearest witnesses λX²/b_j.

At λ=0, the zero polynomial has exactly 14t² agreements, all on the fresh block union. Core values are nonzero and neutral coordinates avoid zero. Every other quadratic has fewer than T agreements. Thus its T-list is also the singleton {0}. This gives the exact finite-pencil near set

    {0} ∪ {a_i b_j : 0≤i,j<t},

of size t²+1, and all of its lists are singleton. The good nonzero labels have exact agreement T, while the zero label has larger agreement 14t².

At the projective direction g, zero has exactly n−14t²=114t²+1 matches. A nonzero pure quadratic matches at most one fresh block and no zero-direction point; a nonpure quadratic has at most 2t+2 matches. Hence the direction also has singleton T-list {0}. The full projective line has exactly t²+2 near points.

## 4. Ordinary common agreement is exactly 14t

The explaining pair (F0,G0)=(0,X²/b_j) matches f,g simultaneously on all D points of S_j, proving CA≥D.

For an upper bound, if the explaining direction is a nonzero pure quadratic cX², it has no zero-direction matches because every coordinate is nonzero, and at most D fresh matches. If it is nonpure, it has at most two zeros on the combined core/neutral block and at most two matches per fresh block, totaling at most 2t+2<D. If it is zero, joint matches are restricted to core and neutral points; the explaining intercept has at most 2t+3<D matches there. These cases exhaust all directions and establish

    CA(f,g)=14t.

Choose the two received endpoints F=f+αg and G=f+βg. The source change is invertible, so CA(F,G)=14t, and section 3 proves agr(F)=agr(G)=14t exactly.

For normalized affine mixtures the old label is λ=α+u(β−α), an affine bijection of Fp. Thus exactly t²+1 interior parameters are near, all with singleton lists; the endpoints are far. For the unnormalized pencil F+uG, the projective parameterization omits the far point G and includes the near direction at u=−1, so there are exactly t²+2 near parameters. These two counts should not be conflated.

## 5. First order, Johnson, and the actual scale

The degree-two Johnson agreement is sqrt(2n)=sqrt(256t²+2)>16t=T. The first-order curve obeys

    n a1(3/n) ≤ sqrt(3n/2)+(3n/8)^(1/4).

For t≥400 the right side is below 14t (for example, bound the two terms by 13.857t and 2.633sqrt(t)). Thus both exact source/common agreement A=14t and the target T are above first order, while T is strictly below Johnson. The characteristic guard p>2 is automatic.

The source-to-target gap is 2t. Its ratio to the capacity surplus T−3 tends to 1/8; its normalized size is Θ(n^−1/2), the same order as the capacity and first-order margins. But the exceptional count t²+1 is only Θ(n), even though it is a constant fraction of p for p=Θ(n). This is not a superlinear or quadratic-in-n count lower bound. The construction has dimension three and vanishing rate; no fixed-rate claim follows.

## 6. Original D=3t version

The initially proposed variant also works with blocks of size 3t, target 5t, and n=floor(25t²/2)+1. Its finite near set is again exactly {0}∪{a_i b_j} for t≥4, all singleton; CA=3t. Without the endpoint-specific exclusions, nongood endpoint agreements are between 3t and 3t+1 for pure witnesses, while the generic nonpure upper bound is 4t+3. The larger block constant 14 makes this generic outsider bound smaller than the block agreement and places that exact source agreement above first order. This is the substantive convenience of the strengthened ledger.

## Prior-comparison scope

This core is the elementary two-family intersection construction, and its fresh mechanism is direct block replication. The nearest witnesses at far labels are label-dependent pure quadratics, not a single fixed bank with A core matches, so the older fixed-bank fresh-incidence budget must not be applied without its hypotheses. Nevertheless the output here is only linear in n. No claim that this elementary pattern is historically new or that it subsumes the superlinear constructions is justified without a separate matched literature audit.
