# Comparison with Diamond–Gruen and Krachun–Kazanin–Haböck

Primary-source comparison, September 18, 2026. No novelty priority claim is
made beyond what these particular theorems establish. No protocol attack or
operational Stwo security conclusion follows from this comparison.

## Conclusion

The prior results are already stronger on several important axes. Neither
prime-field counterexamples, superlinear counts, growing absolute source
separation, nor the failure of the original capacity conjecture is new here.
The narrow distinction of the new quadratic-bank theorem is their conjunction
with an agreement threshold **above the first-order curve**, fixed message
dimension three, singleton threshold lists for a constant fraction of labels,
and exact control of both endpoint and common agreements. Its rate and all
fractional source gaps vanish. It does not improve the fixed-rate near-capacity
growth supplied by Krachun–Kazanin–Haböck.

## Diamond–Gruen

Benjamin E. Diamond and Angus Gruen, *On the Distribution of the Distances of
Random Words*, [ePrint 2025/2010](https://eprint.iacr.org/2025/2010), now listed
as the full version of the CRYPTO 2026 paper. Primary text checked: Definition
4.1, Remark 4.2, Theorems 2.5 and 4.14 (printed pp. 7–8, 18–19, 22).

For every prescribed integer c*≥2, their explicit family has

    q=n^(c*+1), f=n−z=floor(e n^(1/3)),
    k=(1−2/[3(c*+1)])f.

Along their prime-n/integrality subsequence, every corresponding MDS code has
proximity error greater than n^c*/q. Thus an affine line has more than n^c*
close labels. Theorem 2.5 obtains such a line through a deep hole. Therefore
the source-to-threshold agreement separation is already f−k=Theta(n^(1/3));
growing absolute separation alone is not an advance of our result.

Their argument is characteristic- and evaluation-domain agnostic. The displayed
sequence q=n^(c*+1), with n prime, is an extension-field sequence, so it should
not be relabeled as an explicit prime-alphabet theorem without a separate
specialization argument. This caveat does not diminish the prime-field prior
work below.

The agreement fraction a=f/n and rate rho=k/n are both Theta(n^(−2/3)).
The first-order curve has a1(rho)~sqrt(rho/2)=Theta(n^(−1/3)). Hence
a/a1(rho) tends to zero: this particular family is not a first-order-regime
counterexample. Their arbitrary polynomial exponent and universal-domain scope
are advantages that the new quadratic construction does not subsume.

## Krachun–Kazanin–Haböck

Dmitry Krachun, Stepan Kazanin and Ulrich Haböck, *Failure of proximity gaps
close to capacity*, [ePrint 2026/782](https://eprint.iacr.org/2026/782), Theorem 1
(printed p. 3), with the near-capacity interpretation on pp. 2–4.

For any fixed tau≥1, distance delta in (0,1), and
beta>max(tau+1,12/5), they obtain infinitely many n=2^b and primes
p=Theta(n^beta), with evaluation domain the order-n multiplicative subgroup.
The code distance is delta*=delta+o(1/log n). For
eta~c/(tau log n), their list center has at least n^(tau−o(1)) nearby codewords
at distance delta*−eta. Their affine line has at least n^(tau−o(1)) nearby
labels at distance delta*−2eta, while its direction word is at distance at
least delta*−eta from the code.

In agreement language, the line threshold is rho+2eta and the direction has
agreement at most rho+eta. This is a genuine growing separation of at least
eta n=Theta(n/log n), over prime fields at any chosen fixed rate, with an
arbitrarily large fixed polynomial exponent in the label count. These are
substantially stronger guarantees than ours if the first-order location and
singleton requirement are omitted.

However rho+2eta tends to rho. At fixed rho in (0,1), the first-order threshold
a1(rho) is strictly greater than rho. Thus their asymptotic family eventually
lies below the first-order agreement threshold. Their theorem does not state
singleton line lists or the exact equal endpoint/common-agreement property
used in our construction. We do not infer those properties are impossible;
they simply are not provided by the cited theorem.

## What the new theorem actually distinguishes

Our message dimension is k=3, rho=3/n, and

    T/n~sqrt(2/n),  a1(3/n)~sqrt(3/(2n)),

so (T/n)/a1(3/n) tends to 2/sqrt(3)>1. At the same time T²<2n, so the
threshold lies below the exact degree-two Johnson agreement threshold.
The two source agreements and their common agreement equal A=T−d exactly.
For every sufficiently large prime, at least (1/e−o(1))p labels have singleton
threshold lists. One choice has d~log n/(2loglog n) and p/n~e loglog n.

The relative first-order margin is a constant fraction of a1, but its absolute
agreement-fraction margin is Theta(n^(−1/2)); the rate is vanishing and d/n
tends to zero. This does not prove tightness of fixed-rate first-order bounds,
nor force an n² exponent there. It is also not a first counterexample to the
capacity conjecture, which the above papers already disprove.

There is also a direct check that DG's uniform-random-word mass mechanism does
not already give this dimension-three parameter pair. For any length-n domain
over Fp, a uniform random word U satisfies

    Pr(agreement(U, degree≤2)≥T)
      ≤ p³ binom(n,T)p^(−T)
      ≤ p³ (en/(Tp))^T
      ≤ n³(e/T)^T,

where p≥n and T>3. At T~sqrt(2n) this is superpolynomially small. Even after
multiplication by p, the bound is at most n⁴(e/T)^T for T>4. Thus the generic
averaging lower bound through a deep hole cannot supply the constant-density
line conclusion at this pair. This does not rule out other applications or
refinements of their techniques; it identifies why our structured core is a
material extra ingredient rather than an immediate specialization of their
random-word theorem.

## Stwo and the first-order regime are different comparisons

The primary [S-two whitepaper, ePrint 2026/532](https://eprint.iacr.org/2026/532),
Appendix A.5 (printed pp. 74–80 in the locally archived March 24 revision),
discusses list- and curve-decodability beyond Johnson and near Elias capacity.
It explicitly acknowledges the Diamond–Gruen and Krachun–Kazanin obstructions;
its prime-field discussion qualifies the near-capacity observation by the
fixed-positive-relative-distance regime. Its conjectures should not be called
the Dao–Kominers–Thaler first-order theorem or treated as identical statements.

The new result is a coding-theoretic separation in the DKT first-order
agreement regime. It does not realize Stwo's fixed characteristic, FFT/circle
domain, rate, complete transcript, or sampler. The older KKH construction's
multiplicative subgroup and fixed-rate properties are closer to two of those
structural features. None of these comparisons by itself establishes an
accepted false Stwo proof or a concrete security level.

## Source provenance

The ePrint abstract/metadata pages were checked live. Full primary texts were
read locally because PDF retrieval was restricted:

- DG: `/Users/jthaler/Dropbox/Documents-full-2026-09-16/Documents/binary_pg_flock/rounds/san/B334/lit/eprint2025-2010.txt`.
- KKH: `/Users/jthaler/Dropbox/Documents-full-2026-09-16/Documents/stwo_audit_2026-09-15/sources/actual_list_literature/kkh2026_782.txt` (matching PDF beside it).
- Stwo: repository `tmp/source-audit/stwo-2026-532.txt`; the precise version/hash audit is `research/paper_referee/stwo_source_provenance.json`.

The local DG text contains the formulas quoted above; no assertion is made
that it incorporates every editorial change in the currently listed revision.
