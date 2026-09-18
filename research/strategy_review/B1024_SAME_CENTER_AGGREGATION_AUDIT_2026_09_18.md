# B1024 aggregation: pole injection works, head-fiber merging does not

September 18, 2026. Bounded independent audit of the pinned rational construction. No search, protocol execution, or manuscript changes.

## Outcome

The fourfold shortfall remains a valid **distinct line-label** target: a pole can be chosen so every counted support has a distinct challenge. It is not a fixed-word-list shortfall. Within the B1024 template, different head/product fibers cannot be added around one center, even after arbitrary admissible codeword translations and changing the affine origin on the line. The exact compatibility condition is already the signature used in the existing count. This closes that specific aggregation shortcut; it does not bound a genuinely exceptional signature fiber or unrelated constructions.

The pinned parameters are p=2130706433, q=p^6, n=262144, k=131072, B=1024. Put Y=X^B, take the fixed monic core R of degree1023 with R(0)!=0, and let V_U be the monic root polynomial of a136-subset of mu256 excluding1. The certified six-head-plus-product fiber has at least68,579,341,025,511,059 supports; the target is274,980,728,111,395,088. The exact construction and prior scope are in `research/better_codes_revisit_2026_09_17/SAME_DOMAIN_PADDING.md`.

## Pair count becomes distinct challenges without material loss

Choose a reference V0 in the fiber and define

    gamma_U=(V0(alpha)-V_U(alpha))/alpha,
    P_U=R[(V0-V_U)(Y)-gamma_U Y]/[Y(Y-alpha)].

The common product ensures divisibility at Y=0; the definition ensures divisibility at alpha. The shared six nonmonic leading coefficients imply deg(V_U-V_V)<=129 for every pair. For distinct supports the polynomials are distinct, so

    (V_U(Y)-V_V(Y))/Y

is nonzero of degree at most128. A pair therefore causes a label collision at at most128 poles. For a chosen bank of L supports, it suffices that

    q > p+128*binom(L,2)

to choose alpha outside Fp and avoid ALL pair collisions simultaneously. The exclusion of Fp supplies alpha!=0 and avoids all packet/core poles. At the target L the forbidden fraction is less than5.172e-20; the bound is overwhelmingly satisfied. This is an existence statement for alpha over the allowed sextic field, not an efficient exhaustive pole-search prescription.

If the actual fiber is larger, first retain exactly L supports; there is no need to union-bound over an unknown enormous full fiber. Once alpha is selected the received line is fixed, and every retained support supplies its distinct gamma. Thus the original count shortfall does not require another pigeonhole loss. The gamma-dependent term remains essential, so this argument does not make the bank a list about one fixed word.

## Exact same-line equivalence criterion

For a fixed R and admissible alpha, set T=Y(Y-alpha) and

    f_V=R V(Y)/T,  f1=-R/(Y-alpha).

The evaluation points are the pinned n roots of unity; the rational denominators do not vanish there. For degree136 reference polynomials V,W, the two affine lines have the same center modulo a codeword and their shared direction precisely when

    f_V-f_W = P+s f1,  deg P<k

for some scalar s. Clearing denominators gives, with a harmless sign choice,

    T P=R[V(Y)-W(Y)+sY].

Both sides have degree below n: the right side has degree at most140287, and the left at most133119. Equality at the whole domain is therefore a polynomial identity, even if P and s have coefficients in the sextic field.

Evaluation at X=0 forces V(0)=W(0). Degree comparison forces deg(V-W)<=129, because a degree130 term on the right would have degree134143, exceeding133119. Conversely, if these two conditions hold, choose s to make V(alpha)-W(alpha)+s alpha=0. Then the quotient is polynomial and has degree at most

    1023+1024*129-2048=131071.

Thus the criterion is **if and only if**: same product and same six nonmonic leading coefficients. These are exactly the original signature coordinates. Low-degree codeword translations, affine-origin changes, and extension-field coefficients in the translation do not merge different signature fibers.

In particular, five independently selected large head fibers generally give five different center cosets, not a fivefold larger bank around one fixed center/line. Partitioning one signature fiber into disjoint packet subfamilies and then reuniting them merely recovers its existing cardinality. A new gain must prove a larger fiber or a different compatible identity, not add separate maxima.

## Different support sizes and genuine fixed-word variants

Still fixing B,R,T, suppose the reference polynomials have different degrees h. At the needed agreement, h>=136. The highest error term has degree1024h+1023, above deg(TP)<=133119; adding a multiple of RY does not alter it. Consequently different h cannot satisfy the same-center identity above. Even allowing a nonzero scalar normalization does not cancel a unique highest degree. This rules out adding the nearby cardinality strata through the same received-line template.

For the genuine fixed-word variant with denominator Y, its centers are W_V=R V(Y)/Y. The analogous identity YP=R(V-W)(Y) requires V(0)=W(0) and deg(V-W)<=128, since deg(YP)<=132095. Thus it fixes a seventh nonmonic leading coefficient. Its generic certified list size is32,186,199, not the68-quadrillion line-label count. Different seventh-head fibers are again different codeword cosets of the center.

These assertions do not exclude aggregation from different denominators, packet orders, or entirely different error factorizations. Those would require proving a common received-word identity and disjoint candidate sets; no such identity follows from the existing separate counting guarantees. Coarser packet families that already sit inside one original signature fiber are included in that fiber's count and cannot be counted a second time.

## Practical next certificate

The target remains concrete: prove a single six-head-plus-product fiber has at least274,980,728,111,395,088 supports. The elementary pole-injection inequality then converts it to that many distinct labels on one admissible received line. Alternatively, exhibit genuinely different support families with an explicit common-center identity outside the fixed-template obstruction and prove their candidate sets disjoint. The archived average alone supplies neither improvement.
