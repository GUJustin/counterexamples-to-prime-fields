# Random-tag norm compiler: prior-work and Pareto audit

2026-09-18. Read-only comparison; no main-paper edits. **Do not claim novelty for almost-all challenge coverage at inverse-logarithmic capacity margin.** Crites–Stewart already state all-affine-label coverage in this asymptotic regime. The remaining distinction of the audited norm construction is its two individually far sources and exact source/common-agreement ledger, obtained by a structured quotient construction on a union of norm fibers.

## Direct primary result that must be compared

Crites and Stewart, *On Reed–Solomon proximity gaps conjectures*, ePrint 2025/2046, Corollary 1, states: for q≥10 and q≥n, if

    n(1−H_q(f/n))+2+sqrt(nH_q(f/n)−f) ≤ k ≤ n−f−2,

there exist u0,u1 with distance(u1,RS(F_q,D,k))>f and distance(u0+λu1,RS(F_q,D,k))≤f for **every** λ∈F_q. In fact their statement allows any prescribed direction u1 farther than f. The domain is arbitrary; there is no characteristic-two restriction.

Primary PDF: https://eprint.iacr.org/2025/2046 ; local downloaded source `tmp/cs_novelty_audit/cs.pdf`, extracted `cs.txt`, Corollary 1 at lines 671–685. The extracted radical is rendered across lines; the following paragraph explicitly compares nH_q(f/n)−f to its square root.

This really applies at inverse-log margin. Fix 0<ρ<1, k=floor(ρn), and q polynomial in n with q≥n. Write h(ρ)=−ρ log ρ−(1−ρ)log(1−ρ), using natural logs. Choose any fixed 0<c<h(ρ) and set n−f=k+c n/log q+O(1). Then

    n(1−H_q(f/n)) = k−(h(ρ)−c+o(1)) n/log q.

The extra square-root term is O(sqrt(n/log q)), so the lower condition holds eventually; the upper condition holds because c n/log q→∞. Thus their theorem already supplies all-label coverage at a positive inverse-logarithmic margin for arbitrary growing odd characteristic as well as other characteristics. It is not merely a margin of order (log n)/n.

However λ=0 makes u0 itself near. An invertible reparametrization of a projective line with only its direction point far cannot create a second far point. Therefore this corollary does **not directly** subsume the two-far-source norm theorem. It also does not state the latter's exact individual/common agreement A=J+m−1. This audit does not prove that a further elementary modification of CS could not recover that feature.

## KKH and the earlier conversion theorem

Krachun–Kazanin–Haboeck, ePrint 2026/782, Theorem 1 and Appendix A Proposition 3, give fixed-rate inverse-logarithmic margins and arbitrarily large polynomial exceptional counts over prime alphabets on multiplicative subgroups. Proposition 4 explicitly guarantees at least q/(2n) labels. Appendix A already contains the precise quotient-variable mechanism used here, with degree (r−2)m and rm agreements. The source-shift and tag selection do not justify attributing a new quotient compiler.

Ben-Sasson–Carmon–Haböck–Kopparty–Saraf, ePrint 2025/2055, Theorem 1.9, turns a q-sized list obstruction into at least q/(2n) near challenges with common distance at least δ−1/n. Its characteristic-two Theorem 1.6 supplies stronger constant-gap phenomena in a different field regime. These statements do not supply the requested growing-characteristic two-far exact profile directly.

Sources inspected: the cached primary texts `.../sources/actual_list_literature/kkh2026_782.txt`, Appendix A pp.13–16, and `bchks2025_2055.txt`, Theorems 1.6 and 1.9; primary links https://eprint.iacr.org/2026/782 and https://eprint.iacr.org/2025/2055 .

## Existing binary-repository comparison

The binary manuscript's related-work section already explicitly credits CS with every-challenge examples over arbitrary fields/domains and the inverse-log alphabet-size limitation. This prevents framing almost-complete logarithmic-gap coverage as a newly identified regime.

Its current frontier `research/frontier/characteristic-and-domains.md`, “Exact quarter rate and near-linear characteristic,” gives incomplete Artin–Schreier packets with p=Θ(n/log n), q=p^4, K=n/4, gap p and guaranteed bad fraction at least 1/(4n). The random norm tags improve that stated coverage bound and, at d=2, use q=p^2 while retaining the same characteristic scale. But that comparison is within these particular constructive families, not a new unrestricted coverage theorem. Earlier d5 internally padded locators have exact common agreement J, which the norm construction relaxes to J+m−1.

## Safe positioning

The audited new statement is a structured two-far refinement: for fixed d≥2 and rate ρ, every sufficiently large prime admits a union-of-norm-fibers domain of length Θ(p^(d−1)log p), native alphabet p^d, exact individual/common agreement J+m−1, and all q−1 nonzero affine challenges at agreement J+2m−1. Both gaps have logarithmic normalized order. This is obtained from standard ingredients and is not claimed to have priority.

The proof could be useful for its exact profile and transparent witness identities. Its significance cannot be based solely on almost-all coverage or logarithmic margin, already covered more generally by CS. Its domain is generally not a multiplicative subgroup and its alphabet is not prime. A genuine novelty claim would require checking whether the two-far feature and exact source ledger are already implicit in another prior construction; this bounded audit has not established their novelty.
