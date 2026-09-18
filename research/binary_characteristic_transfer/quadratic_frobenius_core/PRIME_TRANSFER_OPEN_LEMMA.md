# What a prime-field transfer of the rich core still needs

Read against `research/prime_quadratic_line/REGULAR_JOHNSON_DESIGN_GATE.md`, `modular_cyclic_bank/RESULTS.md`, and the exact F49 gate. This is a construction target and transfer lemma, not a new obstruction or a claim that every dense core is a finite plane.

## Precise sufficient arithmetic core lemma

A useful characteristic-zero route would supply, for arbitrarily large integers s, a number field K_s, n_s=Theta(s²) distinct evaluation coordinates x_j, received values w_j, and L_s=Theta(s²) distinct quadratics P_i in K_s[X], each matching at least c*s coordinates, with c and the length constant large enough for the subsequent first-order ledger. Equivalently, coefficient points (a_i,b_i,c_i) must lie on many selected planes

    a*x_j²+b*x_j+c=w_j.

The selected planes have pairwise distinct x_j. Total selected incidences are Theta(s³), so the average plane contains Theta(s) coefficient points. This is the actual missing rich-core lemma. A growing finite list alone, or full coefficient rank alone, does not imply it.

If such a configuration exists, its finite equations and strict inequalities DO transfer to infinitely many prime alphabets: clear denominators, take a finite normal extension containing all entries, choose primes splitting completely and avoiding the finitely many bad norms, then reduce into F_P. Distinct nodes, distinct quadratics, selected incidences, and any explicitly imposed nonincidences survive. One may choose arbitrarily large such P, so n_s<P poses no obstruction. This gives no useful upper bound on P and no automatic label population or probability bound.

For exact nearest-list control one must additionally certify a nonbank cap in characteristic zero and preserve it: every quadratic with at least three matches is determined by one of finitely many three-point supports. Thus the full support-interpolation census, or a symbolic bound replacing it, provides finitely many algebraic tests whose nonzero values can also be protected at reduction. Merely reducing the displayed bank does not supply completeness.

This transfer step is routine once the arithmetic core exists. The currently missing step is constructing the arithmetic core itself, not selecting splitting primes.

## Why the current families do not prove that lemma

* The Frobenius core uses complete affine F_p lines, paired square lifts, and the identity y^p−ay=b. Its large population depends on the characteristic. Copying its full repeated incidence design and asking for a characteristic-zero realization retains precisely the finite-geometry issue; it is not a formal lift of polynomial coefficients. The existing regular-design note excludes one duplicated projective-plane model, but does not classify all dense or partial designs.
* Generic smooth lifting is not a growing-size mechanism here. There are 3L_s+2n_s=Theta(s²) coefficient/node/word variables, versus Theta(s³) selected incidence equations. Thus a full-row-rank Jacobian certificate is impossible for large s. A genuine lift would have to retain extensive algebraic dependencies; this dimension count does not rule out a structured singular family.
* The rational conic and elliptic constructions already reduce to prime fields, but their coordinate buckets have bounded richness two or three. They do not yield Theta(s) richness with L_s,n_s both Theta(s²). Whole-domain covers replicate incidences and increase polynomial degree; they do not preserve degree two.
* A coefficient bank sampled on a fixed algebraic curve of bounded degree also cannot provide the target via transverse plane sections: each selected plane not containing a curve component has at most that fixed degree of intersection. Such an approach needs growing curve degree, plane-contained components with controlled cross incidences, or a genuinely modular geometry. No such realization has been established here.
* The modular cyclic action is an actual growing population mechanism if one can prove a suitable root count: on mu_n, a single full-coefficient quadratic agreeing with X^m at A points gives an orbit of n quadratics with the same agreement. The missing uniform assertion is A>=c*sqrt(n), at the required constant and with a usable nonbank cap, for infinitely many prime fields with spare evaluation coordinates. The existing 698-profile gate and the F49 gate give isolated rank-three orbits, not that assertion. The fixed-character-order exponents already have the recorded asymptotic limitation; enlarging the census is not a proof strategy.

## What this would and would not improve

Even the arithmetic core lemma only transfers the high-multiplicity core. To obtain Theta(n^(3/2)) affine labels with Theta(sqrt(n)) extra agreement, one still needs the independent-intercept pairing identity supplied by the two Frobenius blocks, or another correlated padding mechanism. In the extension construction it is

    z=b−eta*v,  b,v in the same F_p-line Ia.

A core realization with unrelated coefficients does not automatically retain this additive label factorization. Therefore the precise constructive goal has two stages: (i) a growing arithmetic or genuinely prime-field quadratic rich core, (ii) a compatible repeated-label identity. Existing conic covers establish a weaker gap/count tradeoff but do not establish either stage at the stronger parameters.

Assessment: no verified growing-size prime-field transfer of this rich core is currently supplied by the available methods. The arithmetic-core lemma above is a concrete sufficient route, and the cyclic root-count assertion is a separate modular route. Neither follows from finite seeds or from reducing the characteristic-p affine-plane formulas. No new isolated-seed search is recommended without an identity addressing one of these two missing assertions.
