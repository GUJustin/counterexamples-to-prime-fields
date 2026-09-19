# Deterministic higher-power integration: independent audit

2026-09-18. **PASS.** Read the revised higher_power_frobenius.tex in full and the new verify_higher_power_deterministic.py; replayed the latter literally using the research-toolchain Python/FLINT environment. This receipt supersedes the current-status applicability of the earlier probabilistic integration receipt, which is preserved unchanged as historical evidence.

## Revised proof checks

- Odd h dividing p²+1 implies gcd(h,p²-1)=1. Each individual branch maps bijectively onto B* under x^h (and onto eta*B* on the fresh block). This is the exact reason deterministic retention works.
- The displayed R complete branches and tau successive powers of z0=xi^M on the next branch are disjoint, avoid the core, and contain exactly m coordinates. Since0<m<N, the next branch index R is valid even when tau=0. Every canonical support retains at least R(p-1) fresh points. The finite inequality hp+h²<T<=(h+R)(p-1) therefore replaces the probabilistic step completely.
- Primitive xi makes z0 have order p²-1, so z0 is outside F_p. The explicit labels1+eta*z0 and2+eta*z0 have independent B-components over F_p and lie outside every canonical plane. They are distinct, differ by1, and give an invertible received-pair change. No search for endpoints remains.
- The intermediate-coefficient branch obstruction, noncanonical bound hp+h², canonical classification, exact singleton/zero-label profile, and exact common agreement hp remain valid after the specified partial branch. Individual source agreements remain bounded in[hp,hp+h²]; no equality at the upper endpoint is asserted.
- The asymptotic proof keeps h=5^a, the Dirichlet prime schedule, m=floor((1-2/sqrt(h))*N), and R/h tending to1. The deterministic minimum is asymptotic to2hp, exceeding T asymptotic to sqrt(2)*hp. The previous first-order deficit and all claimed limits are unchanged.

The actual general-k first-order correction remains(k³n/72)^(1/4), consistent with cached primary equations(29)--(31). The finite low-rate premise is explicit. No new priority, constant-rate, prime-alphabet, or practical-domain claim appears.

## Literal verifier replay

Both cases pass exact integer/rational arithmetic, including primality, divisibility, branch guards, deterministic canonical minimum, source/noncanonical separation, first-order placement, and strict Johnson rounding.

| p,h | n,k | First-order upper | CA | Source upper | T | Canonical minimum |
|---|---|---:|---:|---:|---:|---:|
| 97,5 | 70560,6 | 483 | 485 | 510 | 593 | 672 |
| 2013265921,12241 | 98329309808423281932846,12242 | 24533338196068 | 24644388138961 | 24644537981042 | 34693646123820 | 48839817953280 |

The small case has921984 singleton labels, one98-list, and guaranteed loss ratio83/587>0.14. The BabyBear case retains the previous singleton count8160249298611705595853537280 and guaranteed ratio5024554071389/17346823055789>0.28965. Its full-branch count12018 and partial-branch size1768686400869808686 reproduce the stated m exactly.

The domains and endpoints are now algebraically specified, rather than merely obtained by a probabilistic existence argument. This checker still does not enumerate their coordinates or lists. In particular the BabyBear domain length is about9.8e22 and its rate about1.25e-19. No correction was required. No additional parameter or field scan was performed.

## Frozen hashes

higher_power_frobenius.tex:

    f198efecbc5c929cd655e3219bb7d2c4e47e688f954dd9166ff5b95a6820cb00

verify_higher_power_deterministic.py:

    745af5b8fbace5b6636807570b281efc2498621aaf80b174b6c2cb062c050cf7

verify_higher_power_deterministic.json:

    b8ee54b2106b070e560765d61385e9e92c241118c42c4b55cf7bb09d5580cd6c


Post-review text update: the new small-p97 paragraph and plural finite-certificate heading were read and checked against the already replayed deterministic receipt. All eleven displayed small-instance parameters agree exactly; no new mathematical assertion or test was added. The theorem hash above is refreshed for this version.
