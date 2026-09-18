# Asymmetric two-component collision bank: independent audit

2026-09-18. **PASS, asymptotically.** Proof fragment: `asymmetric_collision_bank.tex`, label `thm:asymmetric-collision-bank`. No main-file edits. The proof depends on the same elementary translated-grid estimates as the regular collision bank, with collision counting restricted to its rich component.

## Exact core and filler exclusion

For two disjoint K_(t,t), K_(s,s), coherent square factors give bank parameters θ²=a/b, all distinct. Disjoint small-prime vertex sets and p>K^4 limit each pair product to two owners. The two owners are rectangle diagonals within one component; their products agree exactly and their pair sums differ. Assigning the two roots separately yields

    L=t²+s²,
    A=2(L−1)−(t−1)²=t²+2s²+2t−3,
    A'=2(L−1)−(s−1)²=2t²+s²+2s−3,
    Ncore=(t²A+s²A')/2,
    A−A'=(s−t)(s+t−2).

Thus every rich word has exactly A core matches. The filler component need not be equalized to this degree. At grid side M=floor(L/8), a filler label fiber has size at most 1+2M/K, because a,b are distinct primes in [K/2,K] and the integer interval of a u+b v has length <p. With t=o(s), this is o(s²), while A−A'~s². Fillers are therefore below A at **every** label, not just with high probability. This is the key reason only the rich component enters the raw-label collision budget and endpoint exclusions.

Every quadratic outside the full bank has at most L core matches, regardless of the unequal core degrees. On the grid, all such nonconstant quadratics have at most 2M matches; constants have the usual one-row bound except zero at λ=−c0. Neutral cubic padding adds at most three. Hence all nonbank outsiders other than this one exceptional label are below A.

## Noncircular parameter and prime choice

Let K grow and H=floor(16 K^(2/3)(log K)^(4/3)). Define v_x as the number of primes in [x/2,x], t=floor(v_H/16), s=floor(v_K/16), R=t², M=floor((t²+s²)/8), Q0=RHM. These do not depend on p. The interval prime number theorem gives

    t~H/(32 log H), s~K/(32 log K),
    M~K²/(8192(log K)²),
    Q0/K^4→9/8192.

The factor 9/8192 follows from H³~4096K²(log K)^4 and (log H)/(log K)→2/3. Selecting p≡1 mod4 in (4096Q0,8192Q0) gives p/K^4 bounded below asymptotically by 9/2, so p>K^4. Such primes exist in the fixed progression for all sufficiently large K. Also H<K/2, so the two sets of vertex primes are disjoint. A largest quartic class in either interval has enough primes for its two vertex parts, with the conservative division by 16 leaving surplus. Different components may use different quartic classes and different reference primes; coherence is required only inside each rectangle.

## Simultaneous grid and collision events

The retained-grid expectation remains (1/2−o(1))M² because L²/p=O((log K)^−4). It yields probability at least 1/3−o(1) for X≥M²/4. Each of the R rich banks then has at least HM/16 fibers of size d=floor(M/(64H)). Cross-bank raw-label collisions among these rich banks have

    E C≤binom(R,2)(3HM)²/p.

Markov bounds Pr(C>RHM/64) by 288/4096<1/3. The two events therefore coexist, without an independence assumption. Removing both endpoints of all collisions leaves RHM/32 rich labels; discarding the zero-polynomial exception loses at most one. Filler coincidences do not spoil singleton lists because their total agreement is uniformly below A.

## Sources, CA, and domain padding

The union of rich raw labels has size at most 3RHM<p−2. Choose c0 and two finite far parameters outside this union and the zero exception. Every such word has exact maximum A. Neutral points avoid the cubic intersections with all L bank words, so neither rich nor filler core degrees increase. Since Ncore~s^4/2 and grid size≤M²~s^4/64, both fit comfortably inside n=floor((A+d)²/2)+1~2s^4; p≫n leaves enough neutral points.

For explaining direction zero, ordinary common agreement is bounded by the core-plus-neutral maximum A. For nonzero explaining direction it is at most 2+2M<A. The rich bank attains A, and the invertible endpoint change preserves this exact common agreement. The threshold list is a singleton at every retained good label, while the relaxed A-list contains only the R rich words and possibly zero. Successful witnesses are not claimed to have exactly T matches.

## Audited result and limits

There are at least RHM/32−1>p/2^18−1≥p/2^19 singleton interior labels eventually, with

    n=Θ(K^4/(log K)^4),
    p=Θ(n(log n)^4),
    d=Θ(n^(1/3)/(log n)^2),
    R=Θ(n^(1/3)(log n)^2),
    normalized source gap=Θ(n^(−2/3)/(log n)^2).

The threshold is strictly below degree-two Johnson by definition, and both source A and target T are above first order eventually. Rate is 3/n. The normalized source gap is still o(n^−1/2), so this is not a constant fraction of the capacity or first-order margin. It is a different count/gap/alphabet tradeoff, not a uniform improvement on the preceding bank. No finite onset, prescribed domain, practical protocol, or n² count-tightness assertion is made.
