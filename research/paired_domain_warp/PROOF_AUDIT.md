# Paired-block proof audit

September 17, 2026. Internal mathematical audit; not external peer review
or proof-assistant certification. The integrated statement is paired.tex.

1. Code dimension: H_I is monic even of degree2D. H_0-H_I has degree
   <=2D-2, so dimension2D-1 suffices. The input w has maximum agreement
   exactly2D: degree gives the upper bound; zero attains its roots.
   Thus the input is one coordinate short of the RS covering radius.
2. Threshold: one block ofr ±pairs gives2r extra agreements. The gap
   numerator is2r+1, while the far separation numerator is2r. These
   are agreement/distance counts in the FULL length2(m+rq) code.
3. Fourier group is (Fp*)^r, NOT dimension2r: the two coordinates in
   a sign-pair have equal even-polynomial values. A block image has
   V=(p-1)^r possible vectors. All its components are nonzero.
4. Character input: BGKS, arXiv1110.0812v2, Lemma17, printedpage10,
   product of2r characters at DISTINCT shifts±x_j, constant additive
   phase. At leastone character is nonprincipal. Its bound2r sqrtp,
   plus2r+1 deleted arguments, gives lambda<=(4r+2)/sqrtp when
   p>(4r+2)^2. The factor chi_j(-1) is constant of unit modulus.
5. Orthogonality: after common factors cancel, independent seeds on
   each side give two independent u-step products of the same measure.
   Collision probability is (1/V) sum_chi |hatmu(chi)|^(2u).
   Exact finite group convolutions and cyclotomic reductions replay
   this identity; they do not prove the cited Weil bound.
6. Conditioning: independent seeds avoid0 andall±x_j. Distinct-square
   failure <=m(m-1)/(p-2r-1)<=2m²/p. Divide event probabilities by
   a0=1-2m²/p. No independence after conditioning is claimed.
7. Short differences: if1<=u<=r, two distinct monic degree-u locators
   in Y differ in degree<=u-1, so cannot agree at r distinct x_j².
   Thus these pairs have ZERO collisions after conditioning. This is
   essential; diagonal pairs alone contributeL to the energy.
8. Remaining pairs: u>=r+1, lambda<1 gives bound
   (1/V+lambda^(2r+2))/a0. Therefore average excess energy
   E[Delta]<=p^r/L+((4r+2)^(2r+2)+2m²)/(p-2m²).
   No unproved independence between support pairs is used.
9. Sampling order: uniform good core then uniform outside block has
   the same joint law as uniform block then uniform compatible core.
   Every core has equal outside-block count, and every block has equal
   compatible-core count. Sampling disjoint blocks preserves this
   marginal for each block. Union+Markov costs q, not independence.
10. Conditioning on all block energies being good leaves directions
    independent, since they are sampled afterwards. For a fixed nonzero
    z, z times a uniform direction vector is uniform. Failure to hit
    any block therefore has probability<=(gamma/(1+gamma))^q.
    Sum over p-1 labels, then union with the bad-block event.
11. Parity: odd K uses the even construction, optionally adding0 with
    no selected agreement there. Even K at an odd denominator multiple
    has odd n; multiply byX and add0 as a common agreement. Both K
    and the threshold/far agreements increase by1. Every rational rate
    is handled exactly. Adjusting m byO(r) supplies block divisibility.
12. Fixedr asymptotics: L>=p^(r+epsilon), delta=p^-Omega(1),
    q=Theta(logp). Small fixedgamma gives high-probability full coverage.
    The numerical-constant range is c2<1+1/(2r); NOT arbitraryc2.
13. Growingr: anyr→infinity withr logb=o(b), n=(2r+1/2)b/H+O(1),
    m=(n-tb)/2+O(r), t=1/[4(-log2(1-rho))]. Binomial entropy:
    log2L=rb+b/8+O_rho(b/r+r+logb), henceL>=p^(r+1/9).
    The entire Fourier/conditioning error is p^-1+o(1); delta is
    O(p^-1/9). Withgamma=p^-1/20, qdelta/gamma=p^-Omega(1),
    and p*gamma^q<=p^(1-q/20), whereq→infinity. No fixedr constant
    is silently used here: the explicit (4r+2)^(2r+2) is retained.
14. Elias: eta*b-H=Theta_rho(1/r), while H2(rho+eta)-H=O_rho(1/b).
    Since r=o(b), the strict inequality holds. The numerical fraction
    has logarithm log2n-b/(4r+2)+O(1/r)→minusinfinity.
15. Scope: gap shrinks; domains are random paired subsets, not a fixed
    FFT subgroup. The sampler outputs a code and line but does not
    recover a nearby witness for a supplied label. Probability is over
    its randomness; a stored sample is not thereby deterministically
    certified to cover every nonzero label. No actual-list upper bound
    or fixed-positive-gap superlinear conclusion is established.

Finite results: geometry, parity, exact Fourier identities, and all six
primary probability rows PASS. Independent coarser integer replay proves
failure bounds2^-134,2^-128,2^-97,2^-298,2^-284,2^-60 for the stated rows.
The length2518 sample is separately replayed by direct root products.
The earlier simple one-pair curve proof is retained in single_pair.tex;
it gives a smaller M127 existence certificate but is not needed for the
integrated multiblock theorem. WORKING_PROOF.md and MULTIBLOCK_WORKING.md
retain development history; their initial provisional bounds are superseded
by paired.tex and this audit.
