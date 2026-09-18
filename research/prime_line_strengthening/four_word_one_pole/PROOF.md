# A proper one-pole extension of the four-word cyclotomic seed

## Positive result and scope

The exact 300-case search in `check.py` finds twelve distinct proper one-pole functions with six agreements on the archived four-word length-12 seed. Consequently there is a characteristic-zero five-word bank of length 28, degree cap 6, and at least 14 agreements per word. It reduces to prime-field examples at arbitrarily large completely splitting primes. This is a bounded bank, not an unbounded-list theorem or a new superlinear line construction. No novelty priority is asserted.

The seed is from restored `Documents/mca_exponent_one/rounds/R15_H_RAW.md`, four-element list on mu_n. Targeted searches in the seed and constructor notes, and the archived E/H round files, found no previous test of this particular one-pole problem. This is a bounded search-scope statement, not a global archive absence claim.

## Seed and exact witness

Let zeta=(sqrt(3)+i)/2, a primitive twelfth root, and eta=zeta². On Omega=mu_12 take the four polynomials

    H_u(X)=u X²+u^(-1),  u in {1,eta,eta²,eta⁴}.

At each x=zeta^j there is exactly one unordered pair of candidates with equal values: its parameters satisfy uv=x^(-2). Define w(x) to be that common value. Each candidate matches exactly six nodes. Translate by H_(eta⁴), and call the resulting word w0. Its zero indices are

    {0,1,2,6,7,8}.

Put

    a=15/26−3sqrt(3)/13 + i(5/13+9sqrt(3)/26),
    c=27/26−3sqrt(3)/26 + i(−21/26+11sqrt(3)/26),
    V(X)=(X−1)(X−zeta)(X−zeta²).

Then c V(X)/(X−a) agrees with w0 precisely at indices 0,1,2,3,4,5. The script verifies these identities in the exact algebraic number field Q(zeta), not floating-point arithmetic. It also verifies that a is outside all twelve nodes and V(a)!=0. Therefore

    R(X)=H_(eta⁴)(X)+c V(X)/(X−a)=N(X)/(X−a),
    N(X)=(X−a)H_(eta⁴)(X)+c V(X),

is proper, has deg N<=3, and matches the original word at six coordinates.

## Explicit length-28 consequence

Use phi(T)=T²; its critical value zero avoids Omega and a. Over the number field containing zeta_24 and sqrt(a), take the domain

    Omega'={x:x² in mu_12} union {sqrt(a),−sqrt(a)} union {0,2}.

These are 28 distinct points: a is nonzero and outside mu_12, while 4 is neither in mu_12 nor equal to a. The five candidates are

    G_u(T)=(T²−a)H_u(T²),  u in {1,eta,eta²,eta⁴},
    G_5(T)=N(T²).

All have degree at most 6 and are distinct; equality of G_5 with an old candidate would make R polynomial, contradicting properness. On the first 24 coordinates set the received word to (T²−a)w(T²), on the two pole coordinates set it to zero, and at 0 and 2 set it to G_5.

Each old candidate has twelve matches over its six old matches and two matches on the pole fiber. The new candidate has twelve matches over its rational agreements and two on the added coordinates. Thus each has at least fourteen matches, with code dimension 7 exactly one quarter of the length 28.

All constants and coordinates are algebraic. Excluding the finitely many primes dividing denominators, collisions, and the finitely many displayed nonzero guards, reduction at a completely splitting prime preserves this construction in the prime field itself. There are arbitrarily large such primes. This claim concerns this fixed finite construction, not a characteristic-changing transfer from an arbitrary finite-field extension.

## Why the 300 tests are complete

For any proper rational candidate N/(X−a) of numerator degree at most 3 agreeing six times, its difference from any old degree-2 polynomial has numerator degree at most 3 and is nonzero. Hence it can meet each old candidate at at most three nodes. At every coordinate exactly two old candidates match the received word. Six new agreements therefore give twelve intersections with the four old candidates, forcing exactly three with each. More than six new agreements are impossible by the same count.

After subtracting H_(eta⁴), the numerator is a nonzero scalar multiple of the monic cubic V_Z vanishing at exactly three of the six zero coordinates. Choose these in C(6,3)=20 ways. At two of the other three matching coordinates the affine function

    (X−a)/c

must have values V_Z(x)/w0(x). Choosing these in C(6,2)=15 ways uniquely determines that affine function. A constant affine function is not a proper one-pole candidate and is rejected. Otherwise the test checks pole avoidance, properness, and all twelve agreements. Any extension-valued solution is recovered with coefficients in Q(zeta), because the two affine interpolation equations and V_Z are defined there.

The 300 tests yield 152 proper off-domain candidates counted with repetition: 116 with five matches and 36 with six. The latter consist of twelve distinct candidates, each recovered from the three choices of two of its three nonzero matching coordinates. All twelve are recorded in `check.json`.

The run used the repository's `run_bounded.py` with 384 MiB and 60-second limits; `resources.json` records successful completion. An initial type error from using an integer divided by an algebraic-domain element was corrected before the successful run; the saved source and resource report refer to the corrected run.

## Remaining induction problem

The five-word bank is real. It does not automatically supply a proper degree-7 numerator with a single off-domain pole and fourteen agreements, which would produce a sixth word at length 60. Old unused rational witnesses acquire two poles under T² and cannot simply serve as the next inputs. A repeatable algebraic source of fresh one-pole witnesses remains missing.
