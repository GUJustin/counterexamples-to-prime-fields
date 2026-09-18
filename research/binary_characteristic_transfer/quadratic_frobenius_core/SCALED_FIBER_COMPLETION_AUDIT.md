# Independent completion audit: scaled Frobenius blocks

September 18, 2026. **PASS for the coding theorem in `scaled_fiber_padding.tex`, with the DKT-certificate qualification below.** I independently checked its proof using the elementary identities in `PROOF.md`; no exhaustive large-field computation was needed.

## Field, domain, and complete candidate classification

There exists a square eta=s² outside B=F_(p²) in E=F_(p⁴), since E has more than |B| squares. Every element of B* is a square in E. Consequently D0 is the disjoint union of two B-lines minus zero, has 2(p²-1) points, and the squaring map has fibers of size two onto B*. D1=sD0 has the same size and is disjoint from D0 because eta is outside B.

For norm-one a, the linear map y->y^p-ay has kernel and image of size p. Its image is exactly `I_a={b:b^p=-a^p b}`. Every nonzero b belongs to a unique such image line, so these are the p+1 lines in the two-dimensional F_p-space B. This verifies both the canonical-bank count p(p+1), including b=0, and the plane uniqueness used later.

The noncanonical bound <=p for p>=5 is valid over the FULL coefficient field E. On each B-line in D0, projection outside B bounds matches by two unless all transformed coefficients lie in B. If a linear coefficient is nonzero in the B-valued case, the other B-line has no matches. Frobenius elimination on the first line gives a quartic, or, when that quartic vanishes identically, a nonzero degree-p equation. If the linear coefficient is zero, either both lines are handled by projection or the even linearized equation gives the stated canonical classification (all remaining even cases have at most two matches). Thus no outside-B coefficient or odd-linear-term witness is omitted.

Scaling D1 and dividing by eta changes the constant to `(b-lambda)/eta` and preserves the quadratic leading coefficient. A witness canonical on either block is even with norm-one leading coefficient. If it fails the image condition on the other block, it has ZERO matches there, not merely <=p. This is essential to the threshold exclusion.

Since 1 and eta are B-linearly independent, `lambda=b-eta v`, b,v in I_a, uniquely specifies a,b,v whenever lambda!=0. The planes for different a meet only at zero. Both coordinates nonzero give exactly M=(p+1)(p-1)² labels, each with exactly 4p active matches and a unique canonical witness. Axis labels have 4p-2 and zero has 4p-4. These secondary levels must be retained.

## Neutral padding and source control

Padding excludes the 4(p²-1) active nodes and at most 3p(p+1) roots of the monic cubics X³-Q for all D0-canonical Q. The sufficient count is exactly

    p⁴-4(p²-1)-3p(p+1) >= 5p²+4,

or p⁴>=12p²+3p, valid for p>=5. Padding to N=9p² is therefore possible in E itself. No extension beyond E or prime specialization is hidden here.

D0-canonical witnesses gain no neutral matches. A witness canonical ONLY on D1 is not necessarily excluded by this blacklist, but gains at most three, hence has at most 2p+3 matches. A witness canonical on neither block also has at most 2p+3 total. This distinction does not alter the theorem. At threshold 4p, the raw line has precisely the M listed singleton exceptions.

The union of the parameter planes has 1+(p+1)(p²-1)=p³+p²-p elements, fewer than p⁴-1. There are therefore two distinct exterior parameters alpha,beta. Their words have agreement at most 2p+3. Common agreement of (f,g) is at most 2p+3: a direction polynomial other than constants 0,1 matches the zero/one step word at at most four coordinates; direction 0 reduces to D0 plus padding; direction 1 reduces to D1. Both remaining cases have the printed bounds. In fact the common agreement is at least 2p, but exact equality is not asserted.

The source transformation to f+alpha g and f+beta g is invertible and preserves common agreement. The parameter map omits only beta, which is not bad, and transports all M exceptions to nonzero finite labels. Its projective-infinity value is (alpha-beta)g. Precisely the two constants 0 and alpha-beta have threshold agreement there; every other quadratic has at most four matches. Thus the printed M singleton exceptions plus ONE two-element exception, with empty lists elsewhere, is exact. An all-line singleton statement would be false.

## Thresholds and meaningful comparison

Johnson agreement is sqrt(2N)=sqrt(18)p>4p. The displayed elementary first-order bound is valid: sqrt(3N/2)<(15/4)p, `(3N/8)^(1/4)<(3/2)sqrt(p)`, and the sum is below 4p once p>36. Thus p>=41 is safe. Dimension is three, characteristic p=sqrt(N)/3, source/target separation is at least 2p-3, and M~N^(3/2)/27. This is an extension-field construction over q=p⁴=N²/81 at vanishing rate, with absolute gap Theta(sqrt(N)).

Compared with the prior projective quadratic line, this improves characteristic versus length from order N^(1/4) to order N^(1/2), and substantially lowers extension degree, while retaining an N^(3/2) label count and square-root coordinate gap. The earlier family already had the latter gap scale. The new theorem does not preserve its exact singleton property at the extra projective parameter, and it does not reach prime-alphabet or fixed-rate scope.

**Do not reuse the old finite DKT certificate without recomputation.** For the previous m=4, derivative-cap-2, B=2T support, the claimed source leading coefficient is G=3B² and the rank is 23. Here B=8p gives G=192p², whereas 23N=207p². The old row-test margin is NEGATIVE. Thus its advertised 31000N² bound is not established for this parameter row by that certificate. A different support or a direct application with fully tracked parameters is needed for an explicit uniform finite bound. Merely p>2 does not itself check every reconstruction jet-degree guard.

More generally, q=N²/81. An O(N²) exceptional-count upper certificate with constant exceeding 1/81 is already larger than the entire challenge field. Such a comparison supplies no nontrivial failure-probability bound here. The above-first-order threshold is meaningful, but this theorem is not a matching universal quadratic DKT lower bound. Its actual bad probability is Theta(1/p)=Theta(N^(-1/2)), and the rate and normalized source gap vanish.

No new generic tightness claim, prime-field theorem, or fixed-rate separation follows from this audit.
