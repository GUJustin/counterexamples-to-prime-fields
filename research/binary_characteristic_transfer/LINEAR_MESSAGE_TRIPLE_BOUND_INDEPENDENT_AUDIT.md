# Independent audit: sharp triple bound for linear messages

September 18, 2026. **PASS**, over any field, without a characteristic restriction.

## Universal bound

Let x_1,...,x_N be distinct evaluation points. Let f+zg be an affine received line and let C be the maximum ordinary common agreement of f,g with degree-at-most-one witnesses. Suppose A>C. Necessarily C≥2 when N≥2, so the nonvacuous range has A≥3.

A candidate is a pair (z,h), h(X)=alpha X+beta, with at least A matches. Fix an ordered pair of distinct matching coordinates x,y. Their two equations in (alpha,beta,z) have independent alpha,beta columns. Hence they define the whole affine pencil

    h=F_(x,y)+z G_(x,y),

where F_(x,y),G_(x,y) are the linear interpolants of the corresponding two source values.

A further coordinate contains this entire pencil exactly when both f and g agree there with F_(x,y),G_(x,y). There are at most C such coordinates, including x,y. Therefore at least A-C matching third coordinates impose a genuinely new equation and determine a unique z and h. Each candidate contributes at least A(A-1)(A-C) independent ordered triples.

An independent ordered coordinate triple determines at most one (alpha,beta,z). There are at most N(N-1)(N-2) ordered triples in total. Thus the **total number of qualifying candidate pairs**, and in particular the number M of qualifying labels, obeys

    M≤N(N-1)(N-2)/[A(A-1)(A-C)].

This counts only triples whose three coefficient constraints are independent; dependent triples need not determine a candidate. The argument supplies enough independent triples for every candidate because A>C. It handles arbitrary source words and all field characteristics.

## Exact lower construction and asymptotic sharpness

For the projectivized p^5 source before the quadratic pullback, put

    n=S5=1+p+p²+p³+p⁴,
    A=S3=1+p+p²,
    C=S2=1+p,
    M=[5 choose2]_p=n(p²+1).

The existing exact source classification gives exactly M qualifying labels and one qualifying linear witness at each. The identities

    A-1=pC, A-C=p², n-C=p² A,
    n-1=pC(p²+1)

give

    M=n(n-1)(n-C)/[A(A-1)(A-C)].

Hence the ratio of the achieved count to the universal upper bound is exactly

    (n-C)/(n-2),

which tends to one as p grows. Both counts are asymptotic to n^(3/2). This is a matched-parameter asymptotic sharpness result, not merely a comparison of exponents at different thresholds.

## Exact incidence interpretation

The quotient domain is the point set of PG(4,p). A canonical three-dimensional vector-space support becomes a projective plane with A points. For any pair of domain points, their spanning projective line has C points. The simultaneous source interpolants agree on that line. Since g has degree C on the quotient domain, they cannot have more common points. Thus each pair's entire-pencil coordinate set has exactly C points.

Consequently the exact number of independent ordered triples for this source is n(n-1)(n-C). Every noncollinear ordered triple spans a unique projective plane and is explained by its canonical label/witness. The construction therefore saturates the refined independent-triple incidence count exactly. Its asymptotic loss in the universal bound comes only from counting the collinear triples among all distinct-coordinate triples.

## Scope for integration

This gives an elementary geometric companion to the new projective construction and explains its n^(3/2) scale for **linear messages (K=2)**. It does not assert a universal N^(3/2) upper bound for arbitrary quadratic messages (K=3). The quadratic pullback's above-first-order/below-Johnson result remains a separate statement; its exact lists were audited by pullback to the original source.

No claim of literature priority is made for the elementary independent-constraint counting lemma. No main manuscript edits or numerical computation were needed.
