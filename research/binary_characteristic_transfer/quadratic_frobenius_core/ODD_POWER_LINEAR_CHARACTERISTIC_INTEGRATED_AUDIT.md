# Linear-characteristic odd-power integration audit

2026-09-18. **PASS** for the actual manuscript fragments and verifier hashed below. No manuscript edits.

I read the integrated lemma and the changed finite-proposition, asymptotic and numerical passages. The lemma now states the exponent-gcd bound and proves both ingredients: at most δ good branches globally and at most H0=h/δ matches per bad branch after the bijective substitution z↦z^δ. The good-branch Kummer argument applies at exponent H0 with the necessary characteristic coprimality automatic from H0|p²+1. Its final two-case arithmetic correctly gives strict agreement<hp at p≥3h−1. The earlier coarse bound remains valid and is not confused with the sharper one.

The finite proposition consistently changes the exact-source guard to p≥3h−1 while retaining U=hp+h² otherwise. All threshold exclusions still follow from U<T, and the full core attains hp at every parameter. Thus every empty-list word, including both endpoints, has exact hp agreement under the new guard. The asymptotic family's stronger growth hypotheses imply the new guard. Its retained-domain and label-count arguments are unchanged.

I literally replayed the updated deterministic verifier with the research-toolchain Python: all THREE cases passed. The code enumerates the divisors H0>1 of h and maximizes the proved bound; it does not enumerate domains or witnesses. Its integer square/fourth-root rounding bounds the first-order expression conservatively, and its squared threshold guard verifies strict placement below Johnson.

| p,h | n,k | T | exact source/common | noncanonical upper | first-order upper | minimum canonical |
|---|---|---:|---:|---:|---:|---:|
| 97,5 | 70560,6 | 593 | 485 | 142 | 483 | 672 |
| 307,65 | 11333322,66 | 27141 | 19955 | 12610 | 19802 | 36720 |
| 2013265921,12241 | 98329309808423281932846,12242 | 34693646123820 | 24644388138961 | 2312937842 | 24533338196068 | 48839817953280 |

The new p=307 paragraph matches the certificate: 29028384 singleton labels, one further list of size 308, and exact loss/capacity ratio 7186/27075>0.2654. In particular p<h² here, so it actually exercises the new refinement. The existing p97 and BabyBear ratios remain 108/587 and 10049257984859/34693646111578. No coordinate-level p307 fixture is claimed or required by this algebraic parameter certificate.

Historical integrated audits remain unchanged. The valid alternative endpoint choice in the older raw p97 fixture, documented in ODD_H_EXACT_SOURCE_INTEGRATED_AUDIT.md, is unaffected.

## Source hashes

- `odd_h_exact_source_lemma.tex`: `cb8d04f7de0e1ec06f1884eaa5e6eddd65596e6696c4383c99bd090defcdd95a`
- `higher_power_frobenius.tex`: `839cb3f62eae1db4cb2971ffa457bc6a8733125897d8b415dcb608a1010bdd76`
- `verify_higher_power_deterministic.py`: `0a26a025f0e6ba87ea67a774c9e756fbc14ed6f6e86271fa3b0740c4a0a06708`
- `verify_higher_power_deterministic.json`: `65b621ec170403d98c2e0a6626b91d8b5c92d8c5f5b0a1086b18d394260a3315`
