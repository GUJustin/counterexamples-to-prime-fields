# Independent F_(p³) finite-certificate and scope audit

Follow-up: `fp3_far_endpoints.tex` now obtains p individually far inputs by puncturing one core fiber of at most p coordinates. The exact spectrum is p empty lists, p³−2p singleton lists, and p lists of size p over the same field. The source-separation limitations below concern the unpunctured construction and invertible source changes; the later puncturing argument changes the evaluation domain and avoids them.

September 18, 2026. **PASS for the full fragment `fp3_common_agreement.tex`, including the interpolation certificate, all-quadratic classification, exact list sizes, and ordinary-common-agreement scope.** No manuscript edit or downstream exceptional-count constant is supplied here.

## Exact finite certificate

Use p>=4099, N=2p²−p−1, K=3, message degree D=2, A=2p−ceil(4sqrt(p))−2, m=6, derivative cap3, total jet cap B=3A, and challenge height H=40B. The derivative-weighted source has

    x+2i+j<6A=2B,  j<=3,  i+j<=B.

The four derivative-column coefficient counts are B(B+1), B², B(B−1), and B(B−2), respectively. Their sum is exactly

    G=4B²−2B.

This explicitly retains the joint cap in the final column; summing an unrestricted weighted triangle instead would introduce one erroneous column. The primary local-rank formula, Eq.62 of the cached ePrint, has six block sums

    4,8,12,15,14,9,

so R=62. Its specialization cutoff is inactive on these small local blocks. These are the prescribed rank upper bounds; a separate generic-rank assertion is unnecessary.

The row-weighted source side is at least (H−B+1)G and target side at most (H+1)NR. Therefore it suffices to show

    (39B+1)G−(40B+1)NR>0.

Here is a proof for ALL p>=4099, rather than only sampled integers. Since p>=4096, sqrt(p)<=p/64, and

    B>=6p−12sqrt(p)−9 >=(93/16)p−9 >=29p/5.

Also B<=6p. Consequently

    39G−40NR
      >= (7196/25)p²+2012p+2480 >0.

This implies both G>NR and the strict graded margin, because the latter equals B(39G−40NR)+(G−NR). Proposition5.10 therefore supplies a sound first-order interpolant, nonzero at every challenge specialization, uniformly in the domain and received line. Lemma5.9's independent reconstruction guard is p>max(D,derivative cap)=3. There is no requirement p>B or p>H.

`verify_fp3_finite_independent.py/json` independently rebuilds coefficient prefixes by derivative columns and local ranks by blocks. All four original JSON rows agree exactly, including the initial conservative margin122950627672764 at p4099. The large-prime row is an arithmetic control, not a fixed-domain benchmark statement.

A is below exact Johnson: A<2p−2 and (2p−2)²<2N for p>1. The first-order curve comparison is also explicit using the existing low-rate estimate

    N*a1(3/N) <=sqrt(3N/2)+(3N/8)^(1/4)
              <(7/4)p+sqrt(p)<(29/15)p<=A.

The last inequalities hold at the stated onset. This curve check and the finite interpolation certificate are distinct from the characteristic guard.

## Root and label geometry checks

Each plane W has p+1 F_p-directions, each contributing p−1 nonzero physical square roots, so |D0|=p²−1. The shared one-dimensional plane intersection contributes p−1 physical coordinates. Thus after assigning overlap to the core, the exact length is 2p²−p−1.

The image-line identity I_u=(delta/u)F_p and dimension-two plane intersection give at least one representation of every nonzero label. The sole completely deleted fresh fiber is a zero fiber on the exceptional all-directions label line; those labels have other both-nonzero representations. Lambda0 has a different undeleted zero-fiber pair giving exactly2p−2 matches. Hence every finite label has at least A matches. The ceiling in A is conservative and correct. Affine nonzero fibers use a separable cubic norm polynomial and Hasse's bound, not an unjustified two-roots-per-every-y count.

The all-quadratic core bound C0<=max(p+2sqrt(p),8) passes the independent check below. Then the same bound holds on the scaled/deleted fresh block. For a simultaneous witness pair, subtracting its explainers gives a quadratic matching g. If that difference is0, simultaneous matches lie on D0; if1, they lie on D1; otherwise at most four coordinates can match the zero--one direction. Thus

    CA <=p+2sqrt(p),
    A−CA >=p−6sqrt(p)−3 >0.

This proves an ordinary-common-agreement gap. It DOES NOT imply individually far sources. Every finite point on the received line has agreement at least A; its projective direction g also has at least |D0| matches. Consequently an invertible source change within E cannot give two individually far endpoints at threshold A.

## Matched comparison

| Family | Length | Field | Exceptional labels | Source/common distinction |
|---|---|---|---|---|
| Projective locator quadratic line | 2(p⁴+p³+p²+p+1) | F_(p^15) | Gaussian[5,2]_p~p⁶ | Both sources and CA exactly2(p+1); threshold~2p² |
| Scaled two-block construction | 9p² | F_(p⁴) | (p+1)(p−1)² singleton labels, plus one two-word label | Both sources and CA exactly2p; threshold4p |
| Present overlapping-plane construction | 2p²−p−1 | F_(p³) | ALL p³ finite labels | CA<=p+2sqrt(p), threshold~2p; every source on the line is already close |

The new result improves the challenge field to Theta(N^(3/2)) and achieves failure probability one for the ordinary-CA statement at characteristic Theta(sqrt(N)). Its count exponent remains3/2. It does not dominate the individually-far F_(p⁴) theorem; losing source separation is material, not a cosmetic presentation choice.

Universal source conversion over F_(p⁶) would restore both individual agreements equal to the old CA and preserve the p³ labels (plus the projective direction label). That enlarges the field to Theta(N³) and loses unit failure probability; it is not a field reduction relative to the F_(p⁴) theorem.

The certificate above proves the finite first-order support exists. It does not evaluate the downstream numerical list/MCA budgets. In particular no earlier31000N² constant is silently transferred. With q~N^(3/2), a generic constant-times-N² count would again exceed the field and supply no nontrivial probability upper bound.


## Final adversarial review of the complete theorem fragment

The non-even square case is valid and actually gives at most three matches per block. Writing Q=(uX+w)² forces u,w nonzero. Of the two Frobenius equations x^p=±(ux+w), at most one can have an F_p-line fiber, because Norm(-u)=-Norm(u). The other contributes at most one point. A line fiber excludes zero. Three distinct points whose squares lie in W would force the quadratic projection of (z+tv)² to E/W to vanish identically, putting z²,zv,v² in a two-dimensional space. This contradicts degree three of z/v over F_p. Hence its contribution is at most two.

For a nonsquare Q=aX²+bX+c, b!=0, the printed elimination is correct: b2*z=R-d*y, then F+G*y=0 with y²=Q. If F²-G²Q were zero, nonsquareness in E(X) forces F=G=0. For a=0, G=-b2²*b1 is nonzero. For a!=0, G=0 forces R constant, contradicting its linear coefficient -a2*a1*b. Thus the degree-eight root bound is genuine, including leading-degree degeneracies. This handles all non-even competitors on both blocks, giving at most16 total.

For even quadratics, canonical status on either block fixes the same slope a_u and kernel direction in W. Failing the image condition on the other block gives zero solutions, not an extra uncontrolled small list. Therefore only doubly canonical quadratics can reach A.

Outside Lambda0 there is exactly one representing direction, and it cannot have the wholly deleted fresh fiber. For each nonzero element of Lambda0, all p+1 directions represent it; exactly u0 has v=0 and is deleted. At lambda0, all directions have b=v=0 and again exactly u0 is deleted. Distinct directions give distinct a_u. Consequently the exact list counts are p³-p singleton lists and p lists of size p, as stated.

The common-agreement proof correctly uses the DIFFERENCE of the two polynomial explainers; it does not infer common agreement from their separate nearest words. Conversely all finite source points are already nearby, so this is not a two-individually-far theorem. The fragment states that distinction clearly. Its bound 39G-40*62N >=(7196/25)p²-468p is a slightly weaker valid version of the bound above. All threshold and characteristic assertions pass at the printed onset.
