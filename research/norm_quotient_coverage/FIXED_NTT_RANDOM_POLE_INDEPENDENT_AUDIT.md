# Fixed NTT-domain random-pole image audit

2026-09-18. **PASS.** The prescribed subgroup domain supports the exact source/threshold profile with a positive fraction of all sextic-field labels by elementary pole averaging. It does not need a selected domain. It does not prove all-label coverage or the larger benchmark threshold 139782.

## Ordered collision count

Take p=2130706433, E=Fp^6, q=p^6, n=262144, m=1024, D=μ_n⊂Fp*, G=μ_256\{1}, s=255, r=129 and L=binom(s,r). The population of full-degree-six poles is

    B=E\(Fp^3∪Fp^2),       Q=|B|=q−p^3−p^2+p.

This is exact: all proper subfields are contained in Fp^3 or Fp^2, and their intersection is Fp. In particular every pole is outside the domain and tag field.

For different r-subsets S,T, put u=r−|S∩T|. Factoring the common locator gives

    VS−VT = V_(S∩T) [V_(S\T)−V_(T\S)].

The bracket is nonzero of degree at most u−1, since its two terms are distinct monic degree-u polynomials. The common factor has only Fp roots, so cannot vanish at a sampled pole. For each fixed S there are binom(r,u)binom(s−r,u) choices of T. Thus, for the ordered label-collision energy Eb,

    E_b Eb ≤ L + (L/Q) A,
    A=Σ_(u≥1) binom(r,u)binom(s−r,u)(u−1).

There is a full-degree pole with energy at most this average. Cauchy–Schwarz on its label multiplicities yields

    image ≥ ceil[L Q/(Q+A)].

No extra factor two appears: the energy counts ordered pairs, including L diagonal pairs.

Because the bracket has Fp coefficients, its degree-six roots occur in six-element Frobenius orbits. The stronger safe root bound is

    d_u=6 floor((u−1)/6).

Replacing u−1 by d_u throughout is valid; notably u≤6 contributes nothing. It requires no unproved equidistribution. Further equal-product or factorization information might improve this root ceiling, but is not needed here.

## Independent integer result

The saved FIXED_NTT_RANDOM_POLE_INDEPENDENT_ARITHMETIC.json independently evaluates both sums and ceilings. The original bound gives at least

    1491382506403155392854641762120006575825783192321836242

labels, with reciprocal fraction approximately 62.74117647. The six-orbit improvement gives at least

    1553276470857367347050498710657094691569048149670139791

labels, with reciprocal fraction approximately 60.24110632. The decisions use exact integers; the displayed reciprocal fractions are explanatory only. This is existence of a good pole, not its explicit computation.

## Exact ordinary RS compiler on the prescribed domain

Reserve the tag 1 and take R=(X^1024−1)/(X−1), whose 1023 domain roots are precisely μ_1024\{1}. Write Y=X^1024 and, for the good pole b, define

    f=R(Y^129−b^129)/(Y−b),       g=−R/(Y−b).

For PS=Y^129−VS, at native sextic label λ=−VS(b)≠0 the witness

    hS=R[PS(Y)−PS(b)]/(Y−b)

has degree ≤1023+127·1024=131071. Its residual is R VS(Y)/(Y−b), so it agrees on exactly 133119 domain points. For every degree-<131072 witness, the cleared residual has monic degree 133119; hence the maximum agreement at every represented label is exactly that number.

The source f has degree 132095. Clearing the denominator for g gives a nonzero polynomial of degree at most 132095. Interpolation on any 128 tag fibers, plus the R zeros, supplies separate witnesses with the same 132095 matching coordinates. Therefore

    agr(f)=agr(g)=CA(f,g)=132095.

Both endpoints have exactly 1024 fewer matches than the represented-label threshold. The alphabet and challenge field are E, while the evaluation domain is exactly the prescribed prime-field subgroup D. Normalized affine-mixture counting can lose the one pencil parameter λ=−1, so the guaranteed interior count is at least image−1.

## Prior result and scope correction

This is the classical quotient-variable/pole-averaging method, not a new mechanism. The cached Krachun–Kazanin–Haboeck primary paper, ePrint 2026/782 Appendix A, explicitly supplies Lemma 3 (evaluation diversity by a second moment), the quotient-variable construction, and Proposition 4 as a resulting large-image corollary. Its concrete stated lower bound is different; the present overlap and full-degree refinements are the elementary finite calculation above.

More directly, the repository already has the overlap-refined image estimate in `research/binary_characteristic_transfer/QUOTIENT_VARIABLE_COMPILER_INDEPENDENT_AUDIT_2026_09_18.md`, under “Generic averaged pole bound,” including shared-root and equal-product corrections. `COMPILER_AUDIT.md` also records a weaker r−1 root-count bound. Thus the present positive fraction was already available from existing machinery after applying it to the benchmark tag set; it should not be presented as a newly discovered construction principle.

Earlier selected-domain caveats remain correct for the nearly-all-label completion certificates, whose tags were chosen. They must not be read as saying no useful fixed-subgroup result exists. This audit proves a fixed-NTT-domain existential result with roughly q/60.24 represented labels at agreement 133119. It proves neither nearly-all coverage nor agreement 139782, and does not specify a practical protocol, a chosen concrete good pole, or singleton lists.
