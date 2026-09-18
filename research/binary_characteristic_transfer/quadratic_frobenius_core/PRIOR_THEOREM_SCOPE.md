# Scope comparison for the two scaled Frobenius blocks

Checked September 18, 2026 against the named local primary texts below. This establishes non-subsumption by these particular statements, not a literature-wide novelty or priority claim.

## Matched result

The audited new construction has N=9p², K=3, q=p⁴, T=4p, individual source agreements and common agreement exactly 2p, and M+1=(p+1)(p−1)²+1 exceptional labels. M lists are singleton; the direction label has two constants. For safely p≥41, T is above first order and below Johnson. The agreement gap is Θ(√N), rate vanishes, characteristic is Θ(√N), and bad-label probability is Θ(1/p)=Θ(N^(−1/2)). It is not a prime-alphabet or fixed-rate result.

## Existing projective theorem: closest direct comparison

`../projective_quadratic_line.tex`, Theorem `thm:projective-quadratic-line`, already proves K=3, Θ(N^(3/2)) labels, Θ(√N) source gap and above-first-order/below-Johnson threshold, with exhaustive singleton lists. Its N=2(p⁴+p³+p²+p+1), q=p¹⁵, source agreement 2(p+1), and exceptional agreement 2(p²+p+1).

It does NOT specialize to N=Θ(p²): its five-dimensional source domain and three-space locator population fix these exponents. The new parameter improvement is characteristic N^(1/4)→N^(1/2), field size Θ(N^(15/4))→Θ(N²), and hence a better exceptional-label probability. The enlarged neutral blacklist makes both source agreements and common agreement exactly 2p. It loses the all-singleton property at one direction label. Neither the label exponent nor the square-root agreement-gap scale is new relative to that theorem.

## Binary repository ingredients

Read-only files checked:

* `sections/constructions/quadratic-near-johnson.tex`, Theorem `thm:near`: binary additive domain, N=16K, rate 1/16, codimension-two locator compiler, Θ(N²) labels. This is a stronger count at its own fixed characteristic/rate, but its displayed Frobenius-square identities and N/K relation do not specialize to odd p, K=3, N~p².
* `sections/preliminaries.tex`, pole-reduction lemma and its proof: evaluating correction polynomials at a pole converts a pre-existing family of M locators into at most M labels, with possible collisions. Applied directly to the p²-scale Frobenius-core bank, this does not create the additional factor p needed for p³ labels. It also changes the degree bound by division. The new label identity b−eta*v uses TWO independently chosen intercepts from the same image line, rather than one evaluation of each original correction.
* `sections/balanced-padding.tex`, Lemma `lem:balanced-padding`: multiplication by a locator raises code degree and creates common zero coordinates. It does not yield the degree-preserving neutral cubic padding here.
* `research/frontier/characteristic-and-domains.md`, “Incomplete Artin–Schreier packets”: products of h fibers of X^p−X on a domain of m fibers give K=(h−1)p, T=hp and binomial(m,h) locators, then pole reduction. K grows at least as p for h≥2, so this statement cannot give K=3 for growing p. Our use of y^p−ay=b is the same elementary Artin–Schreier geometry, but pairing two intercept fibers across scaled blocks is not that packet theorem.
* `sections/constructions/subfield-gold.tex`, Theorem `thm:subfield-gold`: b a power of two, K=(b−1)²N/b², tensor/derivative compiler followed by pole reduction. Again this does not have the required odd-characteristic fixed message dimension.

No theorem among these inspected statements is a two-scaled-block specialization with the matched parameters. The ingredients—linearized polynomials, norm-one directions, independent field coordinates and a step direction—are elementary and familiar. The defensible claim is a new explicit matched-parameter construction within this project, not a new general compiler principle or an assertion that no equivalent construction exists elsewhere.

## Diamond–Gruen

Primary local text: `.../binary_pg_flock/rounds/san/B334/lit/eprint2025-2010.txt`, Theorems 2.5 and 4.14, Definition 4.1. Public identifier: https://eprint.iacr.org/2025/2010.

Theorem 2.5 converts uniform close-word mass into a proximity-error lower bound through a deep hole. It is universal but does not itself certify the present structured line. At K=3, T=4p, N=9p², q=p⁴, its random-word input satisfies

    Pr(agreement≥T) <= q³ * binom(N,T) * q^(−T).

Even q times this upper bound tends to zero superpolynomially, so that input cannot imply Θ(p³) exceptional labels here. This is a statement about the bound supplied by their averaging mechanism, not a prohibition on other refinements of their methods.

Their explicit Theorem 4.14 family has q=n^(c*+1), agreement f~e*n^(1/3), and K a positive constant multiple of f. Thus K is not three and its agreement fraction is Θ(n^(−2/3)), below the first-order scale Θ(n^(−1/3)). Their arbitrary polynomial count exponent, domain universality and pre-existing growing source separation are not superseded by this new example.

## Krachun–Kazanin–Haböck

Primary local text: `.../stwo_audit_2026-09-15/sources/actual_list_literature/kkh2026_782.txt`, Theorem 1. Public identifier: https://eprint.iacr.org/2026/782.

Theorem 1 fixes delta∈(0,1), hence fixed rate, with n=2^b and prime alphabet p=Theta(n^beta), beta>max(tau+1,12/5). Its line has n^(tau−o(1)) near labels at agreement rho+2eta, eta=Theta(1/log n), with direction agreement at most rho+eta. The theorem cannot be specialized by silently making delta tend to one so that K=3: delta is fixed and its constants depend on it. At its stated fixed rate the agreement tends to capacity rho, below a1(rho). It is substantially stronger on prime alphabet, fixed rate and arbitrary count exponent, but it does not subsume the above-first-order fixed-K parameter tuple here.

## Recommended claim

“The two-block construction gives an explicit quadratic-witness line over F_(p⁴), with length Θ(p²), Θ(p³) exceptional labels, and an above-first-order threshold separated by Θ(p) from both source agreements and common agreement.” Then identify the improvements over the existing projective construction and retain the extension-field/vanishing-rate limitations. Do not call superlinear counts, growing source gaps, or near-capacity failure new in isolation.
