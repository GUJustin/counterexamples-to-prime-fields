# The KKH r=2 quotient after enlargement to quadratic RS

2026-09-18. A proved comparison result, with an exact finite parameter-existence certificate. No manuscript changes. This note does not enumerate the selected tags, pole, coordinates, or labels.

The r=2 quotient from Krachun--Kazanin--Haböck, [Failure of proximity gaps close to capacity](https://eprint.iacr.org/2026/782), Appendix A, is the starting point. The prior local comparison is [SPLIT_MONOMIAL_CONSTANT_BANK_PRIOR_COMPARISON.md](SPLIT_MONOMIAL_CONSTANT_BANK_PRIOR_COMPARISON.md). The added argument below controls **all nonconstant quadratics** on a suitably chosen union of odd-size power fibers. It supplies exact equal-distance endpoints and a linear number of singleton labels at a tested threshold below Johnson and above first order. Thus the missing arguments in that earlier comparison are partly resolved positively.

The distinction between the **canonical agreement 2m** and the **tested threshold T<2m** is essential. The proof guarantees many singleton labels; it does not assert that every nearby label is singleton.

## 1. A geometric exclusion lemma for odd fibers

Let p be an odd prime, let m>1 be odd with m dividing p−1, and write

    H=(F_p^*)^m,  L=|H|=(p−1)/m.

For a tag set A⊂H of size s<m, use the domain

    D={x∈F_p^*: x^m∈A},   n=sm.

Each selected fiber contains exactly m coordinates. Put

    C_m={(1+ζ)^(−m): ζ∈μ_m\{1}} ⊂ H.

Because m is odd, −1 is not in μ_m, so every displayed inverse exists. The involution ζ↦ζ^(−1) has no fixed point on μ_m\{1}, and

    (1+ζ^(−1))^(−m)=ζ^m(1+ζ)^(−m)=(1+ζ)^(−m).

Consequently |C_m|≤d_0:=(m−1)/2.

**Lemma.** If

    |A∩h C_m| ≤ m−s−1   for every h∈H,                 (1)

then every nonconstant polynomial Q∈F_p[X] of degree at most two agrees on at most m−1 coordinates with every received word that is constant on each selected fiber.

**Proof.** A nonconstant linear polynomial has at most one agreement in each fiber. A quadratic has at most two. Write Q=aX²+b_1X+c, with a≠0. If b_1=0, distinct points with the same Q-value are negatives of one another. Their mth powers differ because m is odd and the points are nonzero; hence there is again at most one agreement per fiber.

If b_1≠0, two agreeing points u,v in one fiber have fixed nonzero sum h_0=−b_1/a. Their ratio ζ=v/u lies in μ_m\{1}, and

    u=h_0/(1+ζ),   u^m=h_0^m(1+ζ)^(−m).

Thus every doubled fiber has its tag in A∩h_0^m C_m. There are at most s agreements before counting second hits, so (1) gives at most s+(m−s−1)=m−1. This proof uses no values of the fiber-constant word. ∎

Oddness is necessary for this particular uniform exclusion argument. For even m, x and −x lie in the same fiber, and a quadratic aX²+c can give two hits per selected fiber. No even-m assertion is made here.

## 2. An exact existence criterion for the tag set

Let k=m−s. Select A uniformly from the s-subsets of H. For any specified k-subset R⊂H,

    Pr[R⊂A]=(s)_k/(L)_k ≤ (s/L)^k.

For each h, union over the k-subsets of hC_m, then union over its L possible dilates. A sufficient condition for some A satisfying (1) is

    L binom(d_0,k) (s/L)^k < 1.                        (2)

The criterion is used below with 1≤k≤min(s,d_0). If k exceeds s or d_0, a bad intersection is impossible and no union bound is needed. This is sampling without replacement; no independence of selected tags is assumed.

## 3. Exact quadratic-list classification of the quotient pencil

Fix A satisfying (1), and choose a pole b∈F_p\A. The pole may belong to H; it only needs to avoid the selected tags. Write Y=X^m and define received words on D by

    f=Y+b,   g=−1/(Y−b),   W_λ=f+λg,   λ∈F_p.

The code is ordinary RS of **message dimension 3**, with witnesses of degree at most two. The received word f has a degree-m polynomial representative and g is rational on D; the sources themselves are not asserted to have degree three.

For a constant witness c and a selected tag y,

    W_λ(y)=c  iff  y²−cy+cb−b²−λ=0.                 (3)

This polynomial is monic of degree two. It vanishes at two distinct selected tags α,β exactly when

    c=α+β,   λ=λ_{α,β}:=−(α−b)(β−b).                (4)

Hence every unordered pair of tags supplies a constant with exactly 2m agreements. A constant with only one matching tag has exactly m agreements. Nonconstant quadratics have at most m−1 agreements by the lemma.

Let Λ be the image of the unordered tag pairs under (4). The complete maximum-agreement profile is therefore

    agr_3(W_λ)=2m  for λ∈Λ,
    agr_3(W_λ)=m   for λ∉Λ.                          (5)

The lower bound m in the second line follows by matching the value on any one fiber. For every integer threshold m<T≤2m, the list at W_λ consists exactly of the constants from pairs representing λ. Two different such pairs give different constants: equal sums and equal products would determine the same unordered pair. Also, pairs with a common tag cannot collide when b avoids A.

Thus a label has a singleton list at any such T if and only if it has precisely one unordered-pair representation. Equations (3)--(5) exclude all additional quadratic witnesses, not just additional canonical witnesses. Zero is not in Λ, since b avoids the selected tags.

## 4. Choosing the pole and counting singleton labels

Set N=binom(s,2). For two different unordered pairs {α,β} and {γ,δ}, equality of their labels means

    αβ−b(α+β)=γδ−b(γ+δ).                            (6)

If their sums differ, (6) has exactly one possible pole in F_p. If their sums agree, it has no solution: equality of their products would force equality of the two pairs. Therefore each unordered pair of distinct supports collides at at most one pole, and restricting poles to F_p\A can only remove collisions.

Let C_b count unordered pairs of supports colliding at b. Summing (6) over allowed poles gives

    sum_{b∉A} C_b ≤ binom(N,2).

There is consequently an allowed pole with

    C_b ≤ C_*:=floor(binom(N,2)/(p−s)).               (7)

A label represented j≥2 times accounts for j nonsingleton supports and binom(j,2) collisions. Since j≤2 binom(j,2), the total number of spoiled supports is at most 2C_b. The number of singleton labels is therefore at least

    B_single ≥ N−2C_*.                              (8)

This count is obtained after fixing the good tag set. The tag-set existence argument and pole averaging have compatible quantifiers. No assertion that C_b=0 is needed or implied.

## 5. Both endpoints and common agreement are exactly m

Individually, f and g are injective functions of the selected tag. Their exact agreements with dimension-three RS are m, by the geometric lemma and a constant matching one fiber.

For a standard affine line with no loss of finite labels, take

    F=W_0=f,   G=W_η,

where η∈F_p^*\Λ. Such η exists whenever N<p−1. Equation (5) gives

    agr_3(F)=agr_3(G)=m.

Define common agreement CA_3(F,G) as the largest number of coordinates on which F and G simultaneously agree with their respective degree-at-most-two witnesses. If either witness is nonconstant, the common set has size at most m−1. If both witnesses are constant, the injectivity of F on tags restricts it to at most one fiber. Conversely, the two constant values of F and G on a chosen fiber attain m common agreements. Thus

    CA_3(F,G)=m.                                    (9)

The standard affine parameterization is

    (1−u)F+uG=W_{ηu}.

Multiplication by nonzero η bijects all finite labels. Every singleton label counted in (8) is retained, and none is an endpoint, since 0,η∉Λ. This choice avoids the omitted-label issue that can arise from projectively reparameterizing the intercept/direction pair f,g themselves.

## 6. A fully checked finite parameter-existence certificate

The accompanying [integer verifier](verify_kkh_r2_enlargement.py) uses no floating-point inequalities and performs no tag, pole, domain, or label enumeration. Its [receipt](verify_kkh_r2_enlargement.json) certifies the following parameters.

| Quantity | Value |
|---|---:|
| Prime p | 2,147,483,647 |
| Odd fiber size m | 7,161 |
| Available tags L=(p−1)/m | 299,886 |
| Selected tags s | 4,680 |
| Length n=sm | 33,513,480 |
| Message dimension | 3 |
| Source and common agreement A | 7,161 |
| Tested threshold T=8m/7 | 8,184 |
| Canonical nearby agreement | 14,322 |
| Canonical pair count N | 10,948,860 |
| Averaged collision bound C_* | 27,911 |
| Guaranteed singleton labels | 10,893,038 |

Primality is proved by trial division through floor(sqrt(p))=46,340. The exact factorization

    p−1=2·3²·7·11·31·151·331

also certifies m|p−1. The verifier optionally identifies 7 as a primitive generator, using this complete factorization. With d_0=3,580 and k=2,481, it checks (2) by the exact integer comparison

    L binom(3580,2481) 4680^2481 < 299886^2481.

In fact the left side times 2^11692 is still smaller than the right side. Existence of the required A thus has ample exact slack. Equations (7)--(8) then give the displayed label count, for any A furnished by the first argument. Since N<p−1, the endpoint parameter η exists as well.

For placement, the established first-order bound used in this repository is

    n a_1(3/n) ≤ sqrt(3n/2)+(3n/8)^(1/4).

The integer inequalities

    3n < 2·7091²,   3n < 8·60⁴

give n a_1(3/n)<7151<7161=A. Also

    2n−T²=49,104>0.

Therefore the certified tested threshold satisfies

    n a_1(3/n) < A=CA < T < sqrt(2n).

The source-to-tested-threshold gap is T−A=1,023=T/8. Its ratio to the capacity margin is

    (T−A)/(T−3)=1023/8181=341/2727.

The guaranteed singleton count exceeds n/4. At this finite instance p lies between 64n and 65n. These are exact finite comparisons, not an assertion of an infinite prime family with the same balanced divisor shape. The good tag set, pole b, and endpoint η are established by finite counting and are not individually enumerated in this certificate.

## 7. What this resolves, and what remains distinct

The KKH r=2 quotient, together with the odd-fiber exclusion and pole averaging above, can match the conjunction of dimension three, equally far endpoints, exact common agreement, sources above first order, a tested threshold below Johnson, constant relative source separation, and a linear number of singleton nearby labels. The finite parameter certificate rules out treating that conjunction alone as a distinguishing feature of the newer two-ray construction.

Two limitations remain explicit. First, the canonical nearby words here have agreement 2m, substantially above the tested threshold; the newer two-ray construction has its nonzero successful words at its stated threshold. Second, the averaging proof guarantees a large collection of singleton labels while allowing some additional nonsingleton nearby labels. It does not establish the newer construction's all-near-label singleton profile or its exact prescribed count.

The proof is conditional on elementary fiber arithmetic and the displayed finite inequalities. It does not establish an unbounded family of primes p=Θ(n) having a divisor m with s/m in the required balanced interval. For sequences with m→∞, s/m→c in (32/49,2/3), the same geometric and collision argument is available whenever (2), N<p−1, and the desired singleton lower bound hold; it gives the threshold T≈8m/7 and asymptotic loss-to-capacity ratio 1/8. Establishing any additional prime-family statement requires its own justification. No claim of historical priority or complete subsumption is made here.
