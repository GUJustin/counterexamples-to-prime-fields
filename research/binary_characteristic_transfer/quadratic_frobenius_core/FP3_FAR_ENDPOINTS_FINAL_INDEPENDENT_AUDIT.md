# Final independent audit: one-core-fiber puncturing

September 18, 2026, superseding the earlier two-endpoint-support version of this receipt. **PASS** for the current `fp3_far_endpoints.tex`, titled “One-fiber puncturing: an exact spectrum with far inputs.” No main manuscript edits.

## Exact puncture and spectrum

The choice u1=eta*u0 is in W and differs projectively from u0. Its image line Iu1=eta^-1 Lambda0 is distinct from Lambda0, while eta*Iu1=Lambda0. Thus every b*!=0 in Iu1 defines a coset Lambda*=b*+Lambda0 disjoint from Lambda0.

The p−1 nonzero core fibers have total physical size p²−p, giving one C* of size at most p. Deleting ONLY C* yields n>=2p²−2p−1. At every parameter in Lambda*, the unique doubly canonical quadratic is Q*=a_u1 X²+b*. Its entire core support is removed, leaving at most p+2sqrt(p) fresh matches. Every other quadratic was already bounded by max(p+2sqrt(p),16)=p+2sqrt(p). Thus all p coset parameters are genuinely far, not merely missing a selected witness.

For a generic parameter outside Lambda*, its unique high witness has either different leading coefficient, so intersects C* in at most two roots of Qlambda−Q*, or the same leading coefficient and different constant term, so its core fiber is disjoint from C*. It retains at least A−2=T matches. Its competitors remain below T.

At each lambda in Lambda0, the old p qualifying witnesses all survive. The u1 witness has constant zero and hence core support disjoint from C*. Every other qualifying direction has different leading coefficient and loses at most two matches. No previously excluded competitor can enter, since T remains above its all-quadratic bound.

This proves the exact spectrum:

    p empty lists,
    p³−2p singleton lists,
    p lists of size p.

All three parameter strata are disjoint and total p³. The empty parameters are exactly Lambda*. This strictly strengthens the previous lower-count two-fresh-fiber puncture; no leftover-plane classification is now missing.

## Source and weighting scope

No fresh coordinates were deleted, so g remains nonzero and the p far words are distinct. They are collinear, not affinely independent. Any two distinct far endpoints induce an affine bijection of E, giving exact nearby probability1−p^(-2) and singleton probability1−2p^(-2).

For t>=2 distinct selected far inputs, uniform E-valued affine weights give a uniform parameter because the map from the sum-one weight hyperplane has rank one and fibers of size |E|^(t−2). This claim does not require affine independence of the inputs. In contrast, F_p-valued affine weights remain in the empty coset Lambda*, so every such mixture stays far. The manuscript correctly makes the challenge-field distinction explicit.

Individual source agreements are at most p+2sqrt(p). Ordinary common agreement is bounded by either individual agreement; no identification of their nearest witnesses is needed.

## Uniform finite certificate and thresholds

Now T=2p−ceil(4sqrt(p))−4. With p>=4099, B=3T satisfies

    B>=6p−12sqrt(p)−15
      >=(93/16)p−15
      >=29p/5,

using sqrt(p)<=p/64 and p/80−15>0. Also B<=6p and n<=2p². For m6, derivative cap3, H40B, the previously independently rebuilt primary counts remain G=4B²−2B and R62. Hence

    39G−40*62n >=(7196/25)p²−468p>0,

and the graded surplus is

    B(39G−40*62n)+(G−62n)>0.

This is the strict finite row test; the reconstruction guard is only p>3.

For exact Johnson,

    2n−T² >=16p sqrt(p)−20p−2>0.

For first-order curve membership, T>=2p−5sqrt(p), and sqrt(p)>24 implies

    n*a1(3/n)<(7/4)p+sqrt(p)<T.

The source gap is at least p−6sqrt(p)−5, positive at the onset. The theorem retains vanishing rate and vanishing normalized separation, despite an absolute Theta(sqrt(n)) gap.

## Updated finite-census scope

The CURRENT `check_fp3_exact_lists.json` matches the one-core-fiber theorem:

* p47:44 deletions,n4326,T62;47 empty,103729 singleton=47³−2*47,47 lists of size47.
* p53:44 deletions,n5520,T72;53 empty,148771 singleton=53³−2*53,53 lists of size53.

Both rows now have `all_quadratic_exclusion_applies=true`: T>p+2sqrt(p) and T>16. The earlier p47 canonical-only warning applied to the obsolete two-fresh-fiber threshold and is superseded. These small rows check exact list geometry; they do not establish the uniform finite interpolation certificate at those small primes. The theorem's certified onset remains4099. I read these receipts but did not independently rerun the field census; the present audit is algebraic.

## Comparison

The new theorem retains characteristic Theta(sqrt(n)), singleton population Theta(n^(3/2)), and both-source gap Theta(sqrt(n)) over F_(p³), with nearby probability1−p^(-2). It improves the earlier F_(p⁴) field size and the previous one-minus-1/p lower probability without enlarging the alphabet. It remains an extension-field result, not prime-alphabet or fixed-rate tightness, and the finite support certificate is not a matching universal exceptional-count budget or a better.codes certificate.
