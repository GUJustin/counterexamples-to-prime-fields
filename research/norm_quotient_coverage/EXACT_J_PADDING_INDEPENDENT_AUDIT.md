# Independent exact-dimension norm-quotient audit

Date: 2026-09-18. Verdict: **PASS for the theorem in NORM_COMPILER.tex**, with one unnecessary assertion in COMPILER_AUDIT.md requiring removal. No manuscript was edited.

Let E=F_(p^5), q=p^5, m=(q−1)/(p−1), Y=X^m, and b∈E\F_p. Write J−1=(r−2)m+w, 0≤w<m, with 2≤r<p−2. Reserve a tag a0∈F_p*, choose w points B in its norm fiber, and let R be their monic locator. Set A=J+m−1 and T=J+2m−1.

## Algebra, exact agreements, and zero

The proposed f=R(Y^r−b^r)/(Y−b) is monic of degree A. The denominator of g=−R/(Y−b) never vanishes on E. For any strict-degree-J witness h, f−h is a nonzero polynomial of degree A. The equation g=h has numerator R+(Y−b)h, of degree at most A, and this is nonzero: if h≠0, its second summand has degree at least m>deg R; if h=0, R≠0. Thus both individual agreements are at most A.

Interpolate each quotient-variable source on any r−1 tags outside {0,a0}, using polynomials of degree at most r−2; substitute Y and multiply by R. The resulting strict-degree-J witnesses agree simultaneously on those fibers and on B, exactly A coordinates. Therefore agr_J(f)=agr_J(g)=CA_J(f,g)=A.

For an r-subset S of F_p*\{a0}, put V_S=∏(Y−a), P_S=Y^r−V_S, λ_S=−V_S(b), and h_S=R(P_S(Y)−P_S(b))/(Y−b). Then deg h_S≤J−1 and

    f+λ_S g−h_S = R V_S(Y)/(Y−b).

The zero set consists exactly of B and the r selected full norm fibers, which are disjoint by the tag exclusion. Its size is T. Zero supplies no additional match, since R(0)V_S(0)≠0. The labels are nonzero.

## Product coverage and quantifiers

Katz's degree-five affine-line bound gives |Σ_(a∈F_p) χ(b−a)|≤4√p for every nontrivial character of E*. Deleting 0 and a0 leaves s=p−2 terms and bound 4√p+2. Applying the fixed-cardinality character lemma with θ=r/(p−2) proves every nonzero product occurs whenever

    log((p^5−2)(p−1)) < θ(1−θ)(p−4−4√p).

The independent character audit is `../astra_practical_2026_09_18/FIXED_CARDINALITY_CHARACTER_AUDIT.md`. No restriction on character order is missing. For fixed 0<ρ<1 and J=floor(ρq), the Euclidean-division choice has θ→ρ, so the displayed condition and r-range hold for every sufficiently large prime. This is an eventual theorem with an explicit sufficient inequality, not a uniform small-prime onset assertion.

Consequently the affine bad-label set at threshold T is exactly E*: all nonzero labels qualify and λ=0 does not. The projective direction g is also far. This does not classify threshold lists or prove uniqueness of witnesses.

**Correction:** COMPILER_AUDIT.md says different labels have different witnesses because agr(g)=A<T. That inference is invalid: the same polynomial can approximate different words on different coordinate sets, so subtraction does not produce T matches for g. The theorem and its bad-label count do not need witness injectivity. Remove this sentence unless separately proved.

## Prior containment and strongest honest comparison

The cached primary Krachun–Kazanin–Haboeck text, ePrint 2026/782, Appendix A (printed pp.13–16), explicitly uses the quotient-variable witnesses (P_S(X^m)−P_S(z^m))/(X^m−z^m), degree (r−2)m, and rm agreements. Thus the quotient compiler itself is already present. The present specialization chooses b outside the norm image directly, shifts the first source to a polynomial, uses Katz plus fixed-cardinality character sums for complete nonzero-label coverage, and reserves one norm fiber to hit an exact prescribed dimension. These are the relevant refinements; this is not a new quotient mechanism.

At the same full native domain and alphabet q=p^5 and fixed dimension floor(ρq), the earlier internally padded d5 locator theorem has exact common/direction agreement J and gap Θ(p^3), with at least q−3 labels (all on a special prime subsequence). Here both individual and common agreement are J+m−1, the nearby threshold is J+2m−1, and the exact source-to-near gap is m=Θ(p^4). There are exactly q−1 nearby affine labels for all sufficiently large primes. The larger gap and two far sources are genuine improvements in those coordinates, but the relaxed common-agreement baseline prevents componentwise domination of the exact-CA-J theorem.

The prior native norm compiler in LOCATORS_TREES_NORMS_TRANSFER.md already gives all native labels in a different rate regime (rate tending to one as its norm parameter grows); its exterior-field version has a different alphabet and label count. It does not already state this arbitrary fixed-rate, exact-dimension, both-far native theorem.

KKH's published theorem has an inverse-logarithmic normalized gap, larger asymptotically than the present Θ(q^(−1/5)) gap. Its stated prime-alphabet domain and label-fraction guarantees differ. Almost-complete native coverage here is a precise feature to emphasize, not a blanket improvement over KKH. None of these statements addresses the large-characteristic guard p>J at fixed rate: here p=q^(1/5)≪J.
