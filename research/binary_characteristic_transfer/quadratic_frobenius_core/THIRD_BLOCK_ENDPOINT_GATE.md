# A third scaled Frobenius block: exact population/endpoint dichotomy

Independent bounded constructive gate, September 18, 2026. This treats the natural third-block condition specified below, not arbitrary endpoint-dependent edits or received words. No computation was run.

## Model

Retain E=F_(p³), odd p, a two-dimensional F_p-plane W, eta outside F_p, and the two-block canonical parameterization

    a_u=u^(p-1), I_u=(delta/u)F_p,
    b,v in I_u, lambda=b-eta v.

Add a third scaled block with fresh received word `theta*(x²/theta)^p` and constant direction h, on the square lift of theta W after deleting points already assigned to the first two blocks. A quadratic a_u X²+b is canonical there exactly when

    b-h lambda in theta I_u.

The proposed gain is to retain Theta(p³) labels with three large canonical fibers, while finding two endpoints with only about two such fibers.

## Rank dichotomy

Write b=(delta/u)B and v=(delta/u)V, with B,V in F_p. The third condition becomes

    (1-h)B+h eta V in theta F_p.

Its linear map from F_p² to E/(theta F_p) is independent of u. If its rank is at least one, at most p pairs (B,V) survive per direction, and at most p(p+1)=O(p²) jointly canonical witness-label pairs exist. If the rank is two only the zero pair survives.

Therefore Theta(p³) labels canonical on all three blocks require rank zero. For h neither zero nor one, this is equivalent to

    h=t/(eta+t), theta in F_p* · eta/(eta+t), t in F_p*.

Indeed 1-h and h eta must be nonzero scalar multiples of theta; their ratio lies in F_p*. In this case the third condition is IDENTICALLY satisfied for every first-two canonical pair. Multiplying theta by an F_p* scalar changes neither its plane nor the condition. The endpoint cases h=0 or h=1 give respectively theta in F_p* or eta F_p*, so the third underlying plane duplicates an existing block and contributes no new coordinates under this model.

## Overlap cannot make far endpoints in the redundant case

Normalize theta=eta/(eta+t). Write `W=u0 span(1,eta)`, where F_p u0=W intersect eta^(-1)W. The three distinct planes W, eta W, theta W share the SAME intersection line

    F_p eta u0.

For example theta*(eta+t)u0=eta u0. Because every pair of distinct planes intersects in a line, this exhibited line is their entire pairwise intersection.

In the third block's normalized variable, the deleted line is therefore F_p*(eta+t)u0. A canonical third fiber can be entirely deleted only when

    [u]=[(eta+t)u0],   b+t v=0.

Then lambda=b-eta v=-(eta+t)v lies in `(delta/u0)F_p`, exactly the all-directions exceptional line of the first-two parameter geometry. The analogous completely deleted second fiber has [u]=[u0], v=0, and lies on that same parameter line.

Outside this exceptional line there is one canonical direction and neither deletion occurs. On the exceptional line all p+1 directions are available; omit the two distinct bad directions and choose any of the remaining p-1. At lambda=0 the same choice avoids both deleted zero fibers. Hence every finite parameter retains a canonical witness across all three blocks.

By the already proved norm-cubic/Hasse fiber bounds, a canonical fiber has between p-2sqrt(p) and p+2sqrt(p) square-root points (zero fibers have p-1). Each of the second and third nondeleted fibers loses at most two points to the shared overlap. Thus EVERY finite parameter has individual nearest agreement at least

    3p-6sqrt(p)-4.

Every three-block canonical witness has at most `3p+6sqrt(p)` matches. The possible gap above any finite endpoint's individual agreement is therefore at most `12sqrt(p)+4`, not Theta(p). This conclusion does not require excluding noncanonical competitors: those can only make an endpoint closer.

## Why this decides the proposed amplification

In the positive-rank case, an even witness canonical on only two blocks has at most `2p+4sqrt(p)+2` matches; the third noncanonical even block has at most two. Hence a target exceeding `2p+epsilon p` for fixed epsilon>0 and large p requires joint canonicity on three blocks, and then only O(p²) labels survive. In the zero-rank case, Theta(p³) joint labels are retained but EVERY endpoint already has about3p matches, so the intended linear-in-p individual gap disappears.

This rules out the named third-scaled-block strategy for upgrading the native F_(p³) ordinary-CA theorem into a two-individually-far theorem with the same Theta(p³) population and Theta(p) gap. It does not obstruct the existing ordinary-CA-only result, and it does not exclude nonlinear fresh directions, deliberate edits that destroy this shared canonical structure, or a new witness bank. Those would require a different identity rather than additional copies of this third-block constraint.
