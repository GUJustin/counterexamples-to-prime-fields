# Certified rejection of the six-coordinate, eight-harmonic Fejer test

September18,2026. Bounded audit of sections1–2 of `packet_modular_finish.answer.md`. All work local; no rental or center search.

## Exact sufficient test: PASS

For product class h, let F_h(a) be the six-moment signature count and H_h(b) its unnormalized Fourier transform. For nonzero b and m=8<p, the Fejer kernel

    K(x)=1/(m+1)*|Σ_(r=0)^m exp(2πir(x-c)/p)|²

is nonnegative. Every element of Fp has p^5 preimages under a↦b·a and the sum of K over Fp is p. Hence its total over Fp^6 is p^6. Expanding and averaging proves

    max_a F_h(a) >= [N_h+2 Re Σ_(t=1)^8(1-t/9)e_p(-tc)H_h(tb)]/p^6.

A numerator strictly exceeding (target-1)p^6 certifies the integer target. The triangle expression with |H_h(tb)| upper-bounds this particular certificate at EVERY center. Failure of the triangle test does not upper-bound max F_h.

## Computation

`gate.cpp` computes all48 coefficients for b=e1,...,e6 and t=1,...,8, retaining256 product classes and subset sizes through136. It also computes zero frequency as a replay check. The descending-cardinality update is

    DP[k,h+j] += phase_j * DP[k-1,h],

with product indices modulo256 and j=1,...,255. The selected finite-field primitive root is used in the phases; this is genuinely modular, not a cyclotomic equality test.

The first run took0.64seconds and3168KiB sampled RSS under a512MiB/120second watchdog (`resources.json`). The source was then instrumented to emit the actual phases used in the same DP run. Compilation used `clang++ -O2 -std=c++17`, without fast-math, and the available MacOSX15.4 SDK. The instrumented rerun took under three seconds.

`coefficients.json` contains all coefficients. `screen.py` reads the exact N_h from the archived integer product distribution, checks their total C(255,136), and forms the all-center screen. The exact mean/target ratio is0.249396899544645429..., while all floating triangle screens are0.24939689954464547. Zero-frequency replay agrees with the exact integers within1.23e-16 relatively. Independent index-permutation checks use H_h(te3)=H_(3h)(te1), H_h(te5)=H_(5h)(te1), and H_h(te6)=H_(3h)(te2); discrepancies normalized by N_h are below2.67e-60. These checks alone are not the error certificate.

## Rigorous phase enclosure

`certify.py` uses only exact integers and rational arithmetic for its enclosures and final inequalities. It constructs a rational interval for pi from

    pi=16 atan(1/5)-4 atan(1/239),

using40 alternating terms and the next-term remainder. It propagates intervals at scale2^160 with outward integer rounding. For each phase argument x=2πr/p, it evaluates sine through degree61 and cosine through degree60, allowing the common Lagrange remainder7^62/62!, since0<=x<2π<7.

All12240 phases emitted by the actual DP are checked (2048 distinct arguments). Both real and imaginary errors are at most5e-11; their sum therefore bounds the complex absolute error by1e-10. This validates the library cos/sin outputs actually used, without assuming a library-specific transcendental accuracy guarantee. The17-significant-digit outputs round-trip to the recorded binary64 values.

## DP roundoff bound

The run records that binary64 is IEC559/IEEE and the active mode is round-to-nearest. A complex multiplication and addition use a bounded number of ordinary real operations; standard error bounds give, very conservatively, at most1e-12 times the sum of input magnitudes for their roundoff, apart from subnormal absolute errors. Combining that with phase error1e-10 is less than the deliberately enlarged per-stage allowance delta=1e-9. Fused multiply-add, if used by ordinary compiler contraction, only reduces the relevant operation count/error.

Apply induction to the positive subset-count recurrence that majorizes the absolute values of the Fourier DP. There are255 input stages. Consequently, for every final coefficient,

    |Hhat-H| <= ((1+delta)^255-1)*C(255,136)+1 =: E.

The extra1 covers all possible subnormal absolute errors: even the crude amplification bound10^9*2^255*2^(-1022) is far below1. No overflow is possible: all intermediates are bounded by a small multiplicative inflation of2^255, far below binary64's largest finite value. This is a standard floating-point error certificate under the explicitly recorded IEEE arithmetic/compiler assumptions, not a claim about arbitrary unsafe compiler transformations.

## Exact final rejection

For every direction and product class, the verifier replaces |H_h(te_j)| by

    |Re Hhat|+|Im Hhat|+E,

using exact rational values of the emitted binary64 numbers, and checks

    N_h+2 Σ_(t=1)^8(1-t/9)(|Re Hhat|+|Im Hhat|+E)
       < (target-1)p^6.

All1536 inequalities pass in exact rational arithmetic. The largest certified upper bound divided by target is approximately

    0.24952714459800474.

`certified.json` records the result; certification took8.47seconds. Thus none of these six coordinate directions with harmonics1 through8 can give the required Fejer certificate at ANY center. No center search or higher precision rerun is justified for this test.

## Scope

This is a rejection of one finite set of sufficient concentration tests, not a bound on the actual largest modular signature fiber. Mixed directions, larger harmonic sets, or concentration invisible to these projections remain untested. The fourfold line-label target remains open, and no new benchmark score follows.
