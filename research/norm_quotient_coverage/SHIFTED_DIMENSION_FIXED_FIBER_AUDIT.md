# Fixed fibers with shifted message dimension: audit and matched comparison

2026-09-18. **PASS with asymmetric endpoint scope.** This is not a new almost-entire-common-gap phenomenon: the active paired-domain one-far theorem already has that ratio.

Fix m≥2 and write

    J−m+1=(r−2)m+w, 0≤w<m.

Equivalently J is m−2 above the minimal compiler dimension J0=w+(r−2)m+1. Choose a covering tag set of size s and domain n=(s+1)m as before, with R the degree-w reserved-fiber locator. The same f,g have

    A=deg f=w+(r−1)m=J+1,
    T=w+rm=J+m+1.

The old common witnesses still have degree at most J−m+1<J. They give A common matches. Since f is monic of degree A, no degree<J polynomial exceeds A matches to f. Thus agr_J(f)=CA_J(f,g)=J+1 exactly.

For g the numerator R+(Y−b)h is nonzero and has degree at most J+m−1. Therefore

    J+1 ≤ agr_J(g) ≤ J+m−1 <T.

Do not state agr(g)=J+1 without a new proof. Both endpoints are far, but only f has the full m-coordinate source gap; g is guaranteed only a two-coordinate gap.

For every h of degree<J, the cleared residual for f+λg is monic degree T: the competing term(Y−b)h has degree at most J+m−1=T−2. Coverage supplies a canonical witness of degree≤J−m+1 attaining T for λ≠0. Hence every interior projective point has exact agreement T.

At prescribed J=floor(ρn), Euclidean division above fixes r and w, and r/s→ρ. The seed/pair theorem still supplies coverage for C>1/h(ρ), s=ceil(C log p). For fixed m, primes p≡1 mod m have population sizeΘ(p) and character biasO(p^(-1/2)), so there are infinitely many such primes by Dirichlet (all sufficiently large primes in that progression work). The alphabet is exponential in n. The capacity margin isη=(m+1)/n, and ordinary common loss is m/n=[m/(m+1)]η. The guaranteed smaller individual endpoint gap is2/n=[2/(m+1)]η.

The Elias calculation is

    η log p→(m+1)/(mC).

Thus1/h(ρ)<C<(1+1/m)/h(ρ) is the correct nonempty below-Elias window. Letting fixed m be large makes the COMMON loss fraction approach one but makes the certified smaller endpoint loss fraction approach zero.

## Existing paired result and an exact leading-constant match

The active `research/paired_domain_warp/completion.tex`, Corollary `pd:full-gap`, already gives common agreement K+1 and nearby agreement K+2k+1 on a one-far line, with leading length

    n_old~(2k+4/5) log p/h(ρ).

Thus its common-loss fraction2k/(2k+1) already tends to one. It additionally supplies a multidimensional exact profile, disjoint lists, and an efficient high-probability sampler.

For even m=2k, choose the new constant

    C=(m+4/5)/(m h(ρ)).

This lies strictly within the new below-Elias interval. Then n_new~n_old, and at the same prime alphabet and limiting rate the two constructions have the same leading length, identical capacity numerator m+1, identical common-agreement offset1, and identical common-loss numerator m. The additional certified feature of the shifted norm compiler is that its SECOND endpoint is also far, albeit by only2/n. It does not improve the matched common-loss ratio or leading length.

The older paired TWO-far corollary balances the endpoint gaps at roughly half the capacity margin. The shifted norm construction instead gives a strongly asymmetric guarantee: one endpoint gapm/n, the other only2/n. For large m the guaranteed minimum endpoint separation is worse. Therefore neither a new near-total common-loss claim nor a blanket two-far dominance claim is justified. The concise defensible distinction is an asymmetric two-far refinement of the one-far profile at matched leading parameters; its expository value should be weighed against the already stronger symmetric m2 corollary for minimum endpoint gap.
