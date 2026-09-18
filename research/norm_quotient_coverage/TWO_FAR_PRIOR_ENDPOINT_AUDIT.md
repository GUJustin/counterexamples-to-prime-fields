# Two individually far endpoints: bounded primary-source audit

2026-09-18. Verdict: the inspected CS, Diamond–Gruen, KKH, and BCH statements do **not explicitly give two individually far endpoints with almost-all interior affine mixtures near at inverse-logarithmic gap in growing characteristic**. This is a bounded negative finding about the actual statements and arguments, not a priority claim for the norm construction.

## Exact endpoint premises

* **Crites–Stewart, ePrint 2025/2046, Corollary 1:** arbitrary field/domain; the entropy-window condition gives ALL affine words u0+λu1 near, with any prescribed far direction u1. Hence u0 is near. Their Theorem 1 fixes that direction and averages over an unrestricted uniform center. Theorem 3's extension-field variant likewise explicitly assumes only the direction is far. Neither theorem states both individual inputs far.
* **Diamond–Gruen, ePrint 2025/2010, Theorem 2.5:** for any linear code and radius z below covering radius, error is at least (q−1)/q times the close-word probability. Their proof fixes a deep hole u* and partitions the ambient space into punctured affine lines through u*. It obtains a direction u† with many near points u*+r u†. The center is far; the direction is not shown far. Nor is another finite point on that line shown far. The interleaved-distance conclusion follows solely from u* being a deep hole.
* **Krachun–Kazanin–Haboeck, ePrint 2026/782, Theorem 1 / Appendix A Propositions 3–4:** fixed-rate inverse-logarithmic gap on multiplicative subgroups of prime alphabets; only u1 is stated far. Proposition 4 gives at least q/(2n) near labels, not almost all. Its quotient structure is the relevant precursor, but the actual stated endpoint premise is one far direction.
* **Ben-Sasson–Carmon–Haböck–Kopparty–Saraf, ePrint 2025/2055, Theorem 1.6:** near-(1−o(1))q exceptional labels and an interleaved/common-distance lower bound, in characteristic two with constant fractional gap. Common distance does not imply either individual distance is large. Theorem 1.9 gives q/(2n) labels and common-distance control from a list obstruction, rather than the requested two-far profile. These are also different characteristic/gap regimes.

The binary manuscript's existing related-work text correctly distinguishes these mechanisms; its description of CS every-challenge coverage does not assert two far inputs.

## Why the existing CS averaging does not enforce a far center

Write Z(u)=#{λ: u+λg is near}, where g is fixed and far. The CS proof lower-bounds E[Z(U)] for an unrestricted uniform U, by translation invariance. Conditioning U to be far destroys that uniformity; no bound on E[Z(U) | U far] follows from their calculation. In the all-label conclusion, every maximizing center is necessarily near because λ=0 is counted. It would be contradictory to keep that conclusion unchanged and also require the center far.

A new estimate restricted to far centers could conceivably prove q−1 near labels, but it is not supplied by the existing argument. Likewise, an invertible projective reparametrization cannot turn a projective line with exactly one far point into one with two far points. The CS all-affine-near line has precisely one far projective point, namely its direction, so reparametrization alone definitively does not work.

The Diamond–Gruen construction starts at a far center but leaves its direction uncontrolled. Homogeneous distance invariance does not repair this: multiplying a direction by a scalar preserves its near/far status. Choosing two scalar multiples of the same deep hole merely makes dependent endpoints and supplies no near-mixture guarantee.

## Honest remaining distinction

The norm compiler rigorously gives two individually far source vectors, their exact common agreement A=J+m−1, and all nonzero affine combinations f+λg near. On its projective line exactly two points are far (f and the direction g). Equivalently, normalized interior mixtures of f and g are near for every parameter except the two endpoints. The distinction is stronger than the immediate endpoint information in the inspected results. Its novelty remains unestablished: this audit does not exclude an unadvertised algebraic consequence of another prior construction or a separate conditioning argument.

Primary PDFs and exact local sources:
- https://eprint.iacr.org/2025/2046 ; `tmp/cs_novelty_audit/cs.pdf`, Section 2, Theorems 1 and 3, Corollary 1.
- https://eprint.iacr.org/2025/2010 ; `tmp/cs_novelty_audit/dg.pdf`, Theorem 2.5 and proof (local extracted lines 551–628).
- https://eprint.iacr.org/2026/782 ; cached `sources/actual_list_literature/kkh2026_782.txt`, Theorem 1 and Appendix A.
- https://eprint.iacr.org/2025/2055 ; cached `sources/actual_list_literature/bchks2025_2055.txt`, Theorems 1.6 and 1.9.

## Follow-up: actual DG direction construction, not just its statement

Re-reading the complete proof of DG Theorem 2.5 confirms that u† is an arbitrary ambient vector chosen solely by pigeonhole over projective directions. There is no quotient formula, degree cap, prescribed denominator, or residual polynomial for u†. Even for RS, its unique evaluation interpolant can have degree n−1, so the proof supplies no root-counting lower bound on its distance. The explicit deep-hole choice concerns u* only.

There is a precise accounting reason the same pigeonhole calculation does not retain almost-all coverage after restricting to far directions. Let V=F_q^n, Q=|V|, and let B be the number of near vectors. The near set is scalar-invariant and contains zero. Consequently exactly (B−1)/(q−1) projective directions are near and (Q−B)/(q−1) are far. The punctured lines through the fixed far center partition V\{u*}, with exactly B near incidences in total. Each near direction could contribute up to q−1 incidences. Subtracting this entire allowed contribution leaves only

    B − [(B−1)/(q−1)](q−1) = 1

near incidence guaranteed over ALL far directions. The resulting restricted average is at least (q−1)/(Q−B), not close to q−1 in the general regime. This is a bound on what the available counting argument certifies, not an assertion that its chosen direction must be near or that stronger geometric information is impossible.

CS's actual proof uniformly randomizes the center with fixed far direction; swapping their roles turns the old center into an uncontrolled direction. In the all-affine-near corollary that old center is definitely near. Since nonzero scalar rescaling preserves distance to a linear code, reorienting or rescaling does not repair this. A genuinely additional argument would be needed to force both individual endpoints far while preserving the near count.
