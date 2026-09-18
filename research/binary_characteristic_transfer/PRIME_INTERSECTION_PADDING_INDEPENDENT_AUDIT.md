# Independent audit: prime-field quadratic intersections plus padding

**Final construction update:** the manuscript route now uses the stronger rational core P_i=X²/a_i²+a_i² and fresh f=X⁴,g=X³ described below. It removes both the splitting-prime requirement and the extra two-element threshold list of the original draft audited afterward. The older cubic/step-direction audit is retained only to explain that resolved issue.

## Final rational-core / quartic-cubic padding audit

Take distinct positive primes a_i. Pair differences of P_i=X²/a_i²+a_i² have roots exactly ±a_i a_j. Unique factorization makes all pair roots distinct. All nodes and values are rational; every sufficiently large prime preserves the complete incidence pattern. No Chebotarev or Dirichlet input is required.

At t=N0+1 fresh nonzero nodes use f(x)=x⁴,g(x)=x³. The labels are z_ij=P_i(x_j)/x_j³-x_j. Choose distinct integer x_j greater than Q=max a_i². Each label lies strictly in (-x_j,-x_j+1), so different columns are disjoint; within a column equality would mean x_j=±a_i a_k, impossible. Thus all labels are distinct, negative, and nonzero. Their reductions remain distinct and avoid1 at every sufficiently large prime.

A direct finite-field greedy version only forbids at most N0+j+1+4L+4jL² choices at stage j. Once p>2Q preserves the core, this gives an explicit sufficient characteristic bound without bounding rational collision numerators.

Non-incumbent quadratics have at most L core matches and four fresh matches, hence at most A for L>=6. Incumbents have A core matches and at most one fresh match. Thus the original affine line has exactly tL high labels, with singleton threshold-T lists; outside them its agreement is exactly A.

For the common-agreement bound, a nonzero quadratic direction witness has at most two core zeros and three fresh matches with x³. A zero direction confines the simultaneous set to the core, whose maximum agreement is A. This proves CA=A, attained by every incumbent together with the zero direction. At projective infinity the step direction has now been replaced by g: only the zero polynomial reaches threshold T, with N0 matches, while every nonzero quadratic has at most five.

Take the new source pair f and f+g (or f and f+v g in the finite-field greedy version, with v nonzero outside the high label set). Both sources have nearest agreement A. Invertible source mixing preserves CA. Its affine line has exactly tL+1 nonzero high labels, and **all** their threshold lists are singletons, including the label -1, whose unique witness is zero. This verifies the corrected manuscript claim.

The finite certificate in the final section below is unchanged. Its concise input form is `prime_quadratic_finite_certificate.tex`, independently audited by the auditor agent as well.

## Original variant audit (superseded)

The construction is valid. The both-far reparametrization adds one extra exceptional challenge with a two-element threshold list, but it still has a unique nearest polynomial. All statements below use L>=25, avoiding small-parameter curve issues.

## Explicit rational core and split primes

Take P_i(X)=iX²+i²X+i³ for 1<=i<=L. The pair difference is

    (i-j)(X²+(i+j)X+i²+ij+j²),

with discriminant Delta_ij=-3i²-2ij-3j²<0. Each monic pair quadratic is irreducible over Q. Two such quadratics coincide only for the same unordered pair: their linear coefficient determines the sum and their constant coefficient then determines the product. Thus all their roots are simple and disjoint over Qbar.

Let M0 be 8 times L!, the product of all |Delta_ij|, and the absolute nonzero pairwise resultants of the monic quadratics. Every sufficiently large prime p congruent to1 modulo M0 preserves simplicity and pairwise disjointness and splits every discriminant. Indeed -1 and2 are squares modulo p, and every odd prime dividing a discriminant is a square by quadratic reciprocity and p congruent to1 modulo that prime. Dirichlet gives arbitrarily large such p. No unspecified genericity or Chebotarev theorem is needed.

The N0=L(L-1) core nodes are these pair-intersection abscissas, with received word equal to the common ordinate. Each P_i has exactly A=2(L-1) core matches. Any other degree-at-most-two polynomial Q has at most L core matches: each matching node gives two incidences with the P_i, while each nonzero difference Q-P_i has at most two roots.

## Fresh nodes and exact original-line classification

Put t=N0+1. At fresh nodes x_j use f(x_j)=x_j³ and g(x_j)=1; on the core use f equal to its received word and g=0. Choose all fresh nodes distinct and outside the core, with all tL values

    z_ij=P_i(x_j)-x_j³

distinct and nonzero. At stage j (zero indexed), at most

    N0+j+3L+3jL²

choices are forbidden. Distinctness within one new column is automatic outside the core. Thus p>N0+t+3L+3(t-1)L² suffices, and can be imposed on the split primes above.

At z=z_ij, exactly P_i has T=A+1=2L-1 matches: its A core matches and that one fresh match. A different non-incumbent Q has at most L core matches and at most three fresh matches, since Q(X)-X³-z is a nonzero cubic. Hence it cannot reach T for L>=5. Every incumbent has at most one fresh match by label distinctness. Therefore the original line has exactly tL exceptional labels at threshold T, each with a singleton threshold list and unique nearest polynomial. Every other label has nearest agreement exactly A.

## Common agreement and both-far correction

If a nonconstant quadratic G agrees with the step word g, it matches at most two core and two fresh points. If G=0, simultaneous agreement is confined to the core and is at most A. If G=1, it is confined to fresh points and is at most three. Other constants match nowhere. Taking F=P_i,G=0 attains A. Thus CA(f,g)=A exactly.

Since all z_ij are nonzero, f itself has nearest agreement A. Choose v nonzero and outside the exceptional label set, and replace the source pair by

    f_new=f,  g_new=f+v g.

Both individual source agreements and common agreement are now exactly A. For z!=-1, the new word is (1+z) times the old word at parameter vz/(1+z). It inherits exactly tL high labels, with singleton threshold lists. At z=-1 the word is -v g. Its threshold-T list consists of exactly the two constants 0 and -v, with agreements N0 and t=N0+1. Any nonconstant quadratic has at most four matches. Consequently its nearest polynomial is uniquely -v.

The both-far version therefore has exactly tL+1 nonzero bad labels, all with unique nearest polynomials. All but the single label -1 have singleton lists at T. Outside this set the nearest agreement is A. Claiming tL bad labels, or singleton threshold lists at every label after this reparametrization, would be incorrect.

## First-order and finite support comparison

The total length is n=2L(L-1)+1 and the dimension is3. Exactly

    T²=2n-1,

so T is below the exact Johnson threshold sqrt(2n). The low-rate bound gives

    n a1(3/n) <=sqrt(3n/2)+(3n/8)^(1/4)
              <(7/4)L+sqrt(L)<2L-1=T

for L>=25. The derivative-weighted support m4,S2,B=2T has G=3B²=24n-12>(47/2)n and local rank23; H=48B passes the graded challenge test. The characteristic guard is p>2.

The same explicit D=2 counting calculation as the projective certificate yields list budget18n and full-MCA budget31000n². In detail, lambda<=3n/B, both incidence ratios are at most4n/B and5n/B, Freg<=5B,S<=3B,Hs144B,J<=778B². The regular terms are at most9336n²+25n², and the ordinary tail is at most6924n+13827nB<=20751n². Total30112n²<31000n².

Finally tL+1 is asymptotic to n^(3/2)/(2sqrt(2)). The field is genuinely prime, while the code dimension stays3 and the rate and absolute first-order margin vanish. The common-agreement gap T-A is exactly one coordinate; this distinction should remain explicit.
