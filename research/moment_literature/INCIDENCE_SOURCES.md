# Primary-source audit: the MDS incidence envelope

Checked 2026-09-15. Coordinated with `research/puncturing_improvement`; reused its Jo PDF/text. No manuscript or git changes.

## Source statements and dates

**Sunghyeon Jo, ePrint 2026/1432.** Theorem 4.2 applies to any linear `[n,k]` MDS code over `F_q`, with `1 <= k < n`, every integer error budget `0 <= E <= n`, and effective agreement threshold `t_eff=max(n-E,k+1)`. It proves

`B_C(E) <= min_{k+1 <= b <= t_eff} floor[binom(n,b)/binom(t_eff-1,b-1)]`.

Here `B_C` counts distinct bad affine-line parameters. Definition 2.1 requires an agreement support of size at least `n-E` on which the received pair has no simultaneous codeword explanation. Lemma 4.1 proves the sharp rejecting-test abundance `binom(m-1,b-1)` on an unexplained support of size `m`. No Johnson-range, prime-characteristic, prescribed-domain, or large-field assumption is needed for this upper bound. [Paper and version metadata](https://eprint.iacr.org/2026/1432).

Archive received date: **July 13, 2026**; revised **August 19, 2026**. The inspected PDF is dated August 19. Its SHA256 is `2ec8659e1720c9ca24f881591cf64d00291fb12c3602a796278772a98c1c58d6`.

**Przemek Chojecki, ePrint 2026/1463.** The inspected author source explicitly imports the all-test-size MDS envelope from Jo's Theorem 4.2 and reproduces his rejecting-test induction. Its displayed introductory theorem adds a challenge subset `Gamma` and the trivial bound by `|Gamma|`; the incidence argument is unchanged. It explicitly distinguishes slopes from witnesses/supports. Its exact-agreement incidence uses a *chosen support of size a*, which need not be the entire agreement set. [Archive metadata](https://eprint.iacr.org/2026/1463), [pinned author source](https://raw.githubusercontent.com/przchojecki/rs-mca/32a41660e3088eeeb15a16645330856794302ff0/RS_MCA_Paving_v9.2.tex).

Archive received date: **July 17, 2026**; approved **July 21, 2026**. Source declares July 17. The last file-changing commit is `32a41660e3088eeeb15a16645330856794302ff0`, dated July 21, 19:03:56 UTC. The ePrint PDF fetch failed; claims about detailed text above refer to that pinned author source, not an asserted PDF/source identity.

## Exact support is the same badness criterion

This is a direct definition check. Suppose `u_z` agrees with `c` on `A`, where the tuple of coefficient words has no simultaneous explanation. Let `S=Agr(u_z,c)` be the entire agreement set. Then `A subset S`. An explanation on `S` would restrict to one on `A`, so `S` is also unexplained. Conversely, the entire support itself can serve as the witnessing subset. Thus, for a fixed pair `(z,c)`, existence of an unexplained witnessing support of sufficient size is equivalent to the entire agreement support being unexplained.

The distinction is the **counting unit**: the existing theorem counts parameters `z`; the manuscript's stronger counting statement can count all distinct pairs `(z,c)`. Do not present whole-support badness itself as a newly stronger notion of MCA.

## Witness-pair and degree-e consequences

Neither inspected incidence theorem states these consequences verbatim. They follow by short modifications of Jo's proof and should be introduced as corollaries of his incidence argument, without a claim of priority.

Let `u_z=sum_{j=0}^e z^j u_j`. Count pairs `(z,c)` for which `S=Agr(u_z,c)` has size at least `t` and at least one coefficient word is outside `C|S`. Take `t_eff=max(t,k+1)` and fix `k+1 <= b <= t_eff`.

1. Choose, for each pair, one unexplained coefficient on `S`. Jo's abundance lemma gives at least `binom(|S|-1,b-1)` subsets `A` of size `b` on which some coefficient is unexplained.
2. For a fixed such `A`, pass to the quotient `F^A/(C|A)`. The coefficient vectors define a nonzero vector-valued polynomial of degree at most `e`. Apply a linear functional that is nonzero on one coefficient. Every accepted parameter is a root of a nonzero scalar polynomial, so there are at most `e` distinct accepted parameters.
3. For each fixed accepted `z`, at most one global codeword agrees on `A`, by the MDS property and `b>=k`. Hence `A` is charged by at most `e` pairs, even when many codewords are near one line point.

Double counting gives the witness-weighted statement

`sum_{bad (z,c), |S|>=t} binom(|S|-1,b-1) <= e binom(n,b)`

and therefore the total-pair bound

`#bad pairs <= min_{k+1<=b<=t_eff} floor[e binom(n,b)/binom(t_eff-1,b-1)]`.

For a restricted challenge set, the same proof holds. **Do not cap the pair count by `|Gamma|`**: a single parameter may have several witnesses. The parameter projection alone admits that cap. Keep `e` inside the floor; `e*floor(x)` is not interchangeable with `floor(e*x)`. Repeated parametrizations and inseparability do not invalidate the distinct-root bound. At `e=0` there are no bad pairs under this definition.

## Additional literature qualification

Jo's separate [ePrint 2026/891](https://eprint.iacr.org/2026/891) treats generator-MCA and curve-decodability **interleaving stability**, including polynomial generators. Its abstract was checked, not the full proof. It is a relevant citation for any subsequent claim about interleaving transfer; its existence also makes a broad claim to have introduced polynomial-generator MCA untenable. This audit does not establish novelty of the degree factor or weighted consequence across the entire literature.

## Recommended wording

> Jo's circuit-incidence theorem gives the following envelope for MDS codes. We record its witness-counted polynomial-curve consequence: MDS uniqueness permits counting codeword witnesses separately, while the polynomial root bound replaces one parameter per rejecting test by at most e.

Use Jo as the theorem attribution. Cite Chojecki as a related reproduction/application if relevant, not as the origin of the all-test-size envelope. The earlier elementary puncturing bound may remain for its proof perspective, but should not be advertised as the strongest known universal envelope.
