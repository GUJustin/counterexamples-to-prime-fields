# Higher-power Frobenius integration audit

2026-09-18. Final verdict: **PASS** after literal finite-verifier replay and an independent second pass over the actual higher_power_frobenius.tex source. The mathematical minimal-dimension construction is independently audited in HIGHER_POWER_MINIMAL_DIMENSION_POSITIVE_AUDIT.md.

## Finite BabyBear certificate

Read verify_higher_power_babybear.py and replayed it literally with the research-toolchain Python/FLINT environment. Its exact conditions agree with the independent theorem audit:

- p is prime, h is a proper divisor of p²+1, h-1<(p²+1)/h, and D=h<hp.
- n=h(p²-1)+floor((54/55)h(p²-1)), k=h+1, and T=isqrt(hn-1) is the largest integer strictly below Johnson.
- The first-order upper bound uses the actual general-k expression sqrt(kn/2)+(k³n/72)^(1/4). Its two integer ceiling bounds are computed exactly; no floating-point approximation enters a decisive comparison.
- Required fresh retention is T-h(p-1). The rational gamma is the correct worst-support Hoeffding margin. The checked exponential exponent exceeds 2*bit_length(p)+1, which strictly exceeds log(p(p+1)); this establishes the union bound without evaluating exponentials numerically.
- The noncanonical cap hp+h² is below T; first order is below hp; there are at least two endpoint labels outside all canonical planes.
- The guaranteed source-loss ratio uses the upper source agreement hp+h² and compares exactly to28965/100000. The displayed decimal is explanatory only.

Replay values:

    p = 2013265921, h = 12241, k = 12242
    n = 98329309808423281932846
    T = 34693646123820
    exact common agreement = 24644388138961
    source agreement upper = 24644537981042
    first-order agreement upper = 24533338196068
    singleton labels = 8160249298611705595853537280
    guaranteed loss/capacity ratio = 5024554071389/17346823055789
                                 = 0.2896526963599943...

This is an exact finite hypothesis certificate combined with a probabilistic domain-existence proof. It does not enumerate the retained domain, sources, or lists. The length is about9.8e22, the rate is tiny, the alphabet is F_(p⁴), and the domain is selected rather than prescribed. No practical-code improvement or priority claim follows.

## Final actual-TeX second pass

Read higher_power_frobenius.tex in full. The finite proposition includes the necessary primitive scale, h-1<M/h branch guard, exact fixed-size retention criterion, and strict noncanonical cap below T. Canonical fibers, label-plane disjointness, exceptional zero label, and affine endpoint reparametrization match the audited construction. The common-agreement proof genuinely gives exact hp and does not silently replace the individual upper bound hp+h² by equality.

The general first-order formula was independently rechecked against the cached primary text tmp/eprint-2056/paper.txt, equations(29)--(31): with t=sqrt(rho/2), u²(u+3)=t and a1=t(1+u), giving the stated correction (k³n/72)^(1/4). The low-rate condition is explicit in the finite proposition and holds eventually in the asymptotic sequence.

The asymptotic proof uses h=5^a, a lifted square root of minus one, and Dirichlet primes larger than h^(a+4); it makes no effective least-prime claim. Its c=1-2/sqrt(h) retention choice, gamma limit2-sqrt(2), first-order deficit, vanishing rate, and count/alphabet exponents all agree with the independent audit. The limiting agreement ratios locate the source and tested agreements near the two curves; the text explicitly avoids a uniform-count optimality assertion.

The BabyBear paragraph reproduces the exact verifier values and explicitly says the domain is not enumerated. Its rate approximately1.25e-19, selected quartic-extension domain, and absence of a constant-rate/prime-alphabet/prescribed-short-domain claim are accurately stated. No priority claim is made. No correction was required.

## Frozen source hashes

higher_power_frobenius.tex:

    05259c7fedc04597d940315b0aca857b1018b470618fcab4cd459ccb777ac97e

verify_higher_power_babybear.py:

    060c16c2bbd49694a2a1612c2cd4a07e32a10ffc4fb696fd954f898b5b42ee9b

verify_higher_power_babybear.json:

    da2f22022f7ce49c530d5bb2c23b1aa1a7924d059a08d68cb59e7691b000870e

