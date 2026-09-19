# Fixed-extra quotient and CRT: independent audit

2026-09-18. Actual proof source FIXED_EXTRA_QUOTIENT_INTERSECTION_SYSTEM.md read and independently checked: **PASS**. The actual CRT script was also reviewed and replayed: **PASS**, agreeing with the independently implemented direct syndrome calculation for the one specified pair. This note concerns one fixed extra set, not variable witness-dependent extra coordinates or a general cross-subgroup intersection theorem.

## Exact quotient dimension

After removing the shared far residue space and multiplying by J, the code is RS_(k+d) on D minus Z. For a clean subgroup its generalized weighted space is spanned modulo this code by X^j e_i, 0<=j<=d, 0<=i<=2, where

    e_i=N^(t-3+i)/K^(2i+1), zero on the kernel.

Lower tag powers give polynomial codewords: deg(X^j C Y^a)<=k+d-1 for a<=t-4. Thus these 3(d+1) generators span.

They are independent. A relation with coefficient polynomials P_i of degree at most d, modulo a polynomial of degree less than k+d, can be cleared by K^5. Its numerator degree is at most ell(t-1)+d. It vanishes on n-d-t nonkernel evaluation nodes, and

    n-d-t - [ell(t-1)+d] = ell-2d > 0.

Hence the relation is a rational identity. At the t kernel roots the highest pole term forces P_2 to vanish, because N is nonzero there and d<t. Successive pole orders then force P_1 and P_0 to vanish. This proves exact dimension 3d+3 under the stated ell>=23, d<=5 assumptions.

## Independent CRT derivation

For two clean distinct subgroups write K,K' for kernel locators and

    A_H = sum_(i=0)^2 P_i N_H^(t-3+i) K_H^(4-2i).

Their rational words are A_H/K^5 and A_H'/K'^5, with zero extensions on their respective kernels. A relation modulo a polynomial P of degree less than k+d holds on the punctured domain if and only if the following conditions hold.

Let

    F=Φ/(J K K'),
    M=A_H K'^5-A_H' K^5-P K^5 K'^5.

Off the two kernels, M vanishes at every remaining evaluation point, so M=FQ. The exact degree bounds are

    deg M <= n+ell+d-2,
    deg F = n-d-ell+1,
    deg Q <= 2ell+2d-3.

At a root of K, the zero extension requires P=-A_H'/K'^5. Consequently

    FQ ≡ A_H K'^5       (mod K^6),
    FQ ≡ -A_H' K^5      (mod K'^6).

The sixth powers, not merely the fifth powers, are required: the extra factor enforces the value of the polynomial quotient at the kernel nodes, beyond cancellation of rational poles. F is invertible modulo both powers, since the two kernel sets, Z, and the remaining domain roots are disjoint. Thus CRT supplies a unique representative Q modulo K^6 K'^6. Require its degree to be at most 2ell+2d-3. Then the numerator A_H K'^5-A_H' K^5-FQ is divisible by K^5 K'^5; its quotient P has degree at most k+d+2. Requiring its top three coefficients to vanish imposes precisely deg P<k+d.

Conversely, these CRT and degree conditions give equality at every nonkernel node via the factor F, and at each kernel node via the sixth-power congruence. Hence this is an exact linear test, including the specified zero extensions.

For ell=23,d=5, the modulus degree is 12t=132 and the Q cap is 53. There are 78 forbidden high-Q coefficients and three final degree constraints, yielding an 81-by-36 matrix. No rank assertion follows from these dimensions alone.

## Independent direct one-pair replay

The standard-library script ell23_fixture/independent_pair_1_2_syndrome.py reconstructs the punctured parity-check matrix directly from domain derivative weights and recomputes the 18 zero-extended generators for subgroup indices 1 and 2. It does not import the producer's direct or CRT code and uses its own modular elimination.

For Z=[7,231,340,411,470], the code has length259, dimension178 and redundancy81. All parity-check/code moments vanish exactly. The two individual syndrome ranks are18 and18, and the joined81-by-36 matrix has rank36. This agrees with the corresponding record in the parent's saved all-clean-pairs census. The receipt is ell23_fixture/independent_pair_1_2_syndrome.json; runtime was approximately0.49seconds.

This verifies only that specified pair and fixed Z independently. It does not claim an independent replay of all253 pairs, another extra set, or a general theorem of cross-subgroup disjointness after residue removal.

## Actual proof-source review

The saved FIXED_EXTRA_QUOTIENT_INTERSECTION_SYSTEM.md was read in full. Its exact basis, degree cutoffs, necessary-and-sufficient kernel conditions, and equation count agree with the independent derivation above. The local simplification (5) also checks: with u=K²/N, A=N^(t-1)(p2+p1u+p0u²), whereas Φ/K=N^t(1-sigma1*u+sigma2*u²) modulo K^6. Inverting the latter gives precisely its stated coefficients and prefactor J*Kprime^6/N; the opposite subgroup carries the required minus sign.

Proof-source SHA-256: e0960170c0323e53915deb62a8065e45ce062467bc927b944ed725d882620713

## Final actual-code replay and comparison: PASS

Read verify_fixed_extra_crt.py in full and replayed its one specified pair. Its exact polynomial arithmetic, extended-Euclidean inverses, CRT construction, signs, coefficient ordering, sixth-power constraints, and modular rank elimination match the proof. Its use of the truncated Q in the three infinity equations is valid because the other78 equations force the discarded high coefficients to vanish; this is a linear-system equivalence, not a per-column divisibility claim.

The replay produced an81-by-36 matrix of rank36, with zero intersection. Both domain factorizations and all36 local tag-sum shortcuts passed. The independently implemented direct parity-check matrix also has rank36 for precisely the same pair1,2, fixedZ, and fixture hash. Thus the two independently formed linear systems agree on their zero nullspaces in this fixture. No claim of entrywise equality or independent checking of all253 pairs is made.

CRT script SHA-256: f49d67f85bcc560dc0bd35df27ee0fa4405263efaefd92d0c5f6268cab81374d

CRT matrix SHA-256 (compact JSON): 5b97a7665a096914629ae696b51908017ca56109a32e859f4493f705add35ce1

Replay runtime was approximately0.50seconds. The proof hash above was refreshed after the producer added its finite outcome. This completes the bounded proof/source/one-pair audit; no further fixture work was performed.
