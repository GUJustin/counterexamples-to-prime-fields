# Structured puncturing: what survives and what remains open

September 18, 2026. No computation or manuscript addition. The goal here is to retain a gap of order sqrt(new length), not merely to re-create the constant-gap incidence construction.

## Exact incidence reduction

Identify B=F_(p²) with the affine plane F_p². Keep square lifts of sets S,T in the core and eta-scaled fresh block, respectively. Each affine line in B is a fiber of y^p−ay for one norm-one a. Write r_S(a,b),r_T(a,v) for its retained point counts. The canonical quadratic at label lambda=b−eta*v has

    2 r_S(a,b)+2 r_T(a,v)

active matches. The representation is unique for every nonzero label; thus these are genuine label counts, not a witness-pair overcount. If n=Theta(m), |S|,|T|=O(m), target agreement Theta(sqrt(m)), and the source agreement gap is at least c sqrt(m), then every qualifying canonical pair must have both counts at least c sqrt(m)/2: an off-plane endpoint already attains the core contribution, and the corresponding fresh-only canonical witness attains the fresh contribution. A gap bound cannot be obtained by putting nearly all matches on one side.

For k-rich lines put R_S(a)=#{b:r_S(a,b)>=k}, and similarly for T. Necessarily

    M <= sum_a R_S(a) R_T(a),
    R_S(a)<=|S|/k,   R_T(a)<=|T|/k.

For a point set of size m, elementary affine-plane counting gives the exact identity

    sum_all_lines (r(line)-m/p)^2 = pm-m²/p.

Consequently the number of k-rich lines is at most

    (pm-m²/p)/(k-m/p)^2,       k>m/p.

When m=o(p²), k>=c sqrt(m), this is O_c(p), giving M=O_c(p sqrt(m)). It permits, but does not construct, superlinear populations for m=p^alpha, 1<alpha<2. Equivalently p=n^gamma with 1/2<gamma<1 permits only the upper exponent gamma+1/2 under this particular bound. This is not an impossibility theorem.

The original Theta(p) threshold/gap cannot be preserved at n=o(p²) below Johnson: T<sqrt(2n) alone forbids it. A successful new construction must shrink the agreement and gap to Theta(sqrt(n)).

## Cartesian grids do not provide the desired square-root gap

For S=A×B of size m=o(p²), the number of c sqrt(m)-rich lines is O_c(sqrt(m)). Here is the precise tool and reduction. Stevens--de Zeeuw, Theorem 4, gives I(A×B,L)=O(a^(3/4)b^(1/2)|L|^(3/4)+|L|) when a<=b, ab²<=|L|³, and a|L|<<p². [Primary source](https://arxiv.org/pdf/1609.06284).

If a<c sqrt(m), only vertical lines can be rich, giving at most a such lines. Otherwise a,b=Theta_c(sqrt(m)). Were there more than C_c sqrt(m) rich lines, choose exactly that many; the characteristic condition holds since m=o(p²), and the incidence inequality contradicts their richness for sufficiently large fixed C_c. Thus two such grids give M=O_c(m), using the per-direction bound above. The same conclusion holds for projective images (discard chart poles) and fixed-size unions, with constants depending on the number of pieces. This closes the proposed Cartesian/subgrid mechanism, not arbitrary punctured point sets.

## Constant-gap fallback, retained only for comparison

There is an explicit puncturing with p=Theta(n), M=Theta(n^(3/2)), but gap only TWO. It is the earlier incidence mechanism in Frobenius coordinates, not a dominating improvement.

Choose L>=8, t0=L(L+1)/2 and a prime 2t0<p<4t0. In coordinates y=u+omega*v, retain the pair intersections of the L lines

    v=j*u+j²,  j=1,...,L.

No three concur; their intersections are (u,v)=(-i-j,-ij), all nonzero. Core square lifts have L(L−1) nodes, each selected quadratic has 2L−2 matches, and every other quadratic has at most L matches by counting intersections with the L selected quadratics.

On the eta-scaled block keep y=t+omega*t² for t=1,...,t0. Every quadratic has at most four matches with any f+lambda*g on this block. For an even quadratic this is a nonzero quadratic in t. For a non-even one, isolating its linear X term and squaring gives a quartic; it cannot be an identity because the right side is a nonzero scalar times t+omega*t², with a simple zero at t=0. Each chosen bank has fresh image proportional to t²-jt, whose only repeated values pair t with j−t. Since p>2t0, its exact image size is t0-floor((j−1)/2).

Add one neutral node, with g=0 and f avoiding the L bank values. Then

    n=2L²+1, T=2L, A=CA=2L−2,
    M=L*t0-floor((L−1)²/4).

Far endpoints are chosen outside these finite label sets. Nonbank total agreement is at most L+5<=A. M canonical singleton exceptions survive; the direction parameter adds the familiar two-constant list. For sufficiently large L the threshold is above first-order and below exact Johnson. The characteristic is Theta(n), but the ambient field is Theta(n^4), and the gap is constant. This does not solve the requested square-root-gap puncturing target.

## Decision

No structured puncturing preserving the square-root gap was found. The genuinely remaining problem is an explicit small prime-plane point set with enough parallel families of sqrt(m)-rich lines to make sum_a R_S(a)R_T(a) superlinear, together with the needed noncanonical-witness control. Balanced/unbalanced Cartesian grids, fixed unions, and the constant-gap line-arrangement fallback do not supply it. Do not interpret the O(p sqrt(m)) capacity as an existence argument or launch an unstructured point-set scan.
