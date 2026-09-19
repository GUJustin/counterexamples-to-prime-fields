# Odd-h exact-source integration: independent audit

Date: 2026-09-18. Verdict: **PASS** for the actual sources hashed below.

## Proof audit

The standalone lemma supplies its full two-block setup, including primitive scaling, odd h dividing p²+1, and h−1<(p²+1)/h. These hypotheses imply p does not divide h and gcd(h,p²−1)=1. Thus its Kummer extension is separable; the unrelated research-note correction concerning this hypothesis does not affect the manuscript lemma.

For a noncanonical coefficientwise-B branch, P is nonconstant. Taking d to be the gcd of h and its geometric root multiplicities gives P=R^d with R in B: the leading dth root is unique in B, and Frobenius fixes the resulting polynomial. The residual binomial U^(h/d)−R(Z) is geometrically irreducible by maximality of d. Its intersection with its conjugate transpose has at most (h/d)² points unless the equations are proportional. Proportionality forces R=a Z^(h/d)+b, reducing the actual B-valued matches, through a bijective power map, to y^p=ay+b and at most p points. This establishes the claimed local max(p,h²) bound, including the h/d=1 case.

An intermediate coefficient gives at most h/ell good branches, all in one block: the cross-block congruence is incompatible with 0<h−j<(p²+1)/h. Each remaining branch has at most h matches by projection. Consequently the displayed global bound is valid, and p≥h² makes it strictly smaller than hp. Puncturing only reduces these counts.

The integrated finite proposition correctly keeps U=hp+h² outside the new p≥h² regime, and uses U=hp inside it. No threshold lists change: canonical double-fiber witnesses meet the deterministic lower bound, all noncanonical witnesses are below threshold, and single-fiber canonical witnesses have at most hp matches. Every empty-list word has a nonzero core fiber of hp matches, hence has exact agreement hp when p≥h². The indicator argument still gives exact ordinary common agreement hp. The asymptotic family satisfies p≥h², so both endpoint agreements and common agreement are now exact, without changing the first-order or Johnson placement.

## Numerical and fixture checks

I literally replayed `verify_higher_power_deterministic.py` with the research-toolchain Python; it passed. BabyBear has n=98329309808423281932846, k=12242, T=34693646123820, and exact source/common agreement 24644388138961. Its noncanonical upper bound is 2312937842, and its exact loss/capacity ratio is 10049257984859/34693646111578. The small case has p=97, h=5, n=70560, k=6, T=593, exact source/common agreement 485, noncanonical upper bound 142, and ratio 108/587. These agree with the integrated numerical paragraphs.

I inspected the updated p97 verifier and receipt; I did not repeat its domain enumeration. The receipt's exact source conclusion uses the audited algebraic exclusion, rather than exhaustive enumeration of all degree-five codewords. Its raw rows retain SHA256 `7257c227fe55be89a8e320d123452c8ae708095165068ed93c81c15c3c2cefd0`.

The raw p97 fixture uses the alternative endpoint pair 1+eta*z and 1+eta*(z+1); the manuscript and parameter checker display 1+eta*z and 2+eta*z. Both pairs are distinct and outside all canonical planes, since their two B-components are Fp-linearly independent. Thus both have the same proved agreement/list profile. The raw array is a fixture for the alternative valid pair, not a literal coordinate replay of the manuscript's displayed second endpoint.

## Scope

This audits the degree-four extension construction on its specified branch-prefix domain. It does not claim a prime alphabet, fixed rate, prescribed practical domain, or optimal exceptional-label count. No new scan was run. Historical audits remain unchanged.

## Frozen source hashes

- `odd_h_exact_source_lemma.tex`: `ddb2852e91cbbd6b45d7bb5045bb77d1f6b57925d696a195417df0ae69c11cd4`
- `higher_power_frobenius.tex`: `51aa652623cf30238e5e319b33bec3c9fcfcaa2af8117c243d9ee223fa47c35a`
- `verify_higher_power_deterministic.py`: `4757b582b2471cd305f844fc2b8c4c7a73a6b8f9018b5f4eb9810743a87c9b60`
- `verify_higher_power_deterministic.json`: `3707a9fce935227365f0543ae2d7e214f6007349a5257d2dd76830518117ec66`
- `higher_power_p97_fixture/verify.py`: `3fceb39c667512947122753c96da761c141777ed394e51df050a33f38eed083b`
- `higher_power_p97_fixture/receipt.json`: `12fce300e808a55492bcd1550aa38b4d807fe43b99d799ed17c8dc45e8cb176f`
