# Return to the increasing-characteristic ladder

September 18, 2026. Read-only comparison of the binary repository's `AGENTS.md`, `docs/research-strategy.md`, and `research/frontier/characteristic-and-domains.md`. No other binary-repository source was read or edited for this task. Statements below distinguish the guarantees recorded in those sources from a proposed next construction.

## Existing ladder: contracts must not be merged

| Regime | Domain and code | Agreement/common agreement | Challenge count and alphabet | What grows |
|---|---|---|---|---|
| Fixed characteristic, generalized locator compiler | Every sufficiently large prescribed additive domain, fixed rate rho | A constant gap above rho, depending on the compiler parameters and characteristic; not a uniform near-Johnson guarantee | Recorded probability at least `1/(1+C_(rho,s) q/N^s)-1/q`; all challenges for polynomial-size fields after choosing s sufficiently large | Length grows; the stated constants depend on p |
| Punctured trace, low endpoint | `N=b^m`, m>=2; domain `F_N^*`, n=N-1; K=N/b^2 | T=N/b-1; CA=K; agr(f)=T, agr(g)=K | All N native challenges at this threshold | p<=b<=sqrt(N); for b growing, rate tends to zero |
| Punctured trace, high endpoint | Same domain; K=(b-1)^2 N/b^2 | T=(b-1)N/b-1; CA=K | At least `(N-1)/(b-1)` nonzero labels plus zero | At maximal characteristic the rate tends to one |
| Incomplete Artin–Schreier packets | E=F_(p^2), phi=X^p-X; m selected image values; n=mp, K=(h-1)p | T=hp, CA=K, exact capacity gap 1/m | In F of size q>n: at least `ceil(binomial(m,h)(q-n)/(q-n+K(binomial(m,h)-1)))` labels | Characteristic may be nearly linear in length |
| Quarter-rate packet specialization | m divisible by four, h=m/4+1, m=(8+o(1))ln p; n=mp, K=n/4 | T=K+p; CA=K; relative capacity gap p/n=Theta(1/log n) | q=p^4; at least q/(4n)=Omega(n^3/log^4 n), probability at least1/(4n) | p=Theta(n/log n), but gap shrinks |

The low trace row's all-challenge threshold is BELOW Johnson agreement, since `K(N-1)-(N/b-1)^2=N(2b-1)/b^2-1>0`. The sharper nonzero-label threshold `N/b` is above Johnson on the punctured domain; it must not be substituted while retaining the beyond-Johnson description. These trace rows do not give both-source separation at the printed all-challenge thresholds. The strategy records separate root-free-denominator endpoint sources that are both far, with different count contracts.

The packet row is already an all-prime construction; characteristic three is not a new extension. Its displayed quarter-rate source has a superlinear count, but approaches capacity, not a fixed positive first-order margin. It should not be compared to a fixed-gap binary near-Johnson result by holding only the rate fixed.

## Exactly where prime-alphabet specialization breaks

There are two distinct failures, neither cured by merely letting p grow.

1. **Trace/subspace rank collapses.** On the prime field, the only F_p-vector subspaces are zero and the whole one-dimensional field. The trace endpoints require `m>=2`; setting the ambient field to F_p removes the hyperplane population and violates their parameter hypotheses. A prime field also has no proper subfield from which the existing source-conversion coordinates can be chosen.
2. **Artin–Schreier fibers collapse to one fiber.** On F_p, `X^p-X` is identically zero. Its nontrivial p-point image and p-element fibers occur in F_(p^2). The packet construction needs `2<=h<m<=p` distinct image values, so it cannot even be instantiated in the prime alphabet. Moreover its domain already has `n=mp>p`; n distinct prime-field evaluation points are impossible. The degree-four challenge choice is a further extension, not a cosmetic parameter.

Thus the recorded p~n/log n theorem is an increasing-characteristic EXTENSION-field result. It is compatible with large-characteristic prime-field upper bounds and supplies no specialization with n<=p. A Frobenius descent or coefficient restriction cannot preserve these domain/fiber cardinalities.

## One useful next extension: truncated transversal packets with no common fibers

The most concrete escape to test is to retain the sparse p-by-m domain but build support locators from TRANSVERSAL m-point lines, rather than complete p-point fibers of one additive map. This keeps the increasing-characteristic scale and removes the common quotient at the support level.

Choose omega in F_(p^2) outside F_p and a set Y subset F_p of size m. Use

    D={x+omega y : x in F_p, y in Y},   |D|=mp.

The current construction uses the horizontal p-point rows. Instead, for a,b in F_p, use the truncated transversal

    S_(a,b)={b+(a+omega)y : y in Y},
    J_(a,b)(X)=product_(y in Y)(X-b-(a+omega)y).

Each locator has degree and exact D-root count m. Distinct transversals intersect in at most one point. Allowing differing slopes a prevents all supports from being unions of complete fibers of one fixed map. Crucially, using the complete p-point line locator would cost degree p for only m useful roots and lose the intended parameters; the truncated locator above avoids that immediate loss.

A precise positive target is now an actual head-coefficient fiber, rather than an unsupported claim that multiple directions amplify lists. Fix rho=1/4 and a constant epsilon>0, put K=floor(n/4), T=ceil((1/4+epsilon)n), and construct many distinct monic degree-T divisors L_S of the domain locator, whose roots are unions of these truncated transversals (with overlap handled exactly), such that ALL coefficients in degrees K+1 through T-1 agree across the family. Then a common degree-T head H gives corrections C_S=L_S-H of degree at most K, each with T matches to the word -H. The existing exterior-pole compiler makes strict degree-<K witnesses and yields at least

    ceil(B(q-n)/(q-n+K(B-1)))

labels from B distinct corrections, with exact CA=K. For q=p^4 and B>q, this would retain the existing Omega(q/n) count while replacing its vanishing capacity gap by a fixed epsilon. The root supports must vary in more than one direction; a family secretly equivalent to parallel fibers does not meet the intended target.

**Decisive missing lemma:** produce this large common-head fiber at fixed epsilon, not merely many choices of slopes and intercepts. Products of h truncated line locators have degree hm and may have overlapping roots; counting parameter choices is not a lower bound on a coefficient fiber or on distinct roots. Approximately Theta(n) top-coefficient constraints are required for fixed epsilon. The present sources do not solve them, and ordinary pigeonholing over the extension field does not automatically help. The first bounded mathematical test should derive these head equations for two or three slope classes and identify an identity that makes a linear number of them redundant. Without such an identity, do not escalate to a large search.

This is a candidate mechanism for a FIXED-GAP increasing-characteristic extension-field theorem, not yet a prime-field construction. A later prime-alphabet result would additionally require a replacement domain with n<=p and no reliance on a two-dimensional F_p affine grid. That additional step is explicitly unsolved.

## Priority conclusion

Do not spend effort re-proving odd-characteristic trace endpoints or the already proved p~n/log n packet theorem. The productive gap is fixed agreement excess at fixed rate while characteristic grows, with supports that have no common complete-fiber quotient. The transversal-locator head-fiber problem states one concrete extension and the exact identity it needs. It is not currently a positive theorem or a claim of dominance over the existing binary results.

## Additional decisive guard: p>K and full-line packing

The relevant message-degree guard is `p>K−1`, equivalently `p>=K` for integer code dimension K; a separate derivative-degree guard must also be checked. In particular K=p is admissible, unlike K>p. Merely p tending to infinity is insufficient. At fixed rate `K~rho n`, this requires `n=O_rho(p)`. In particular the existing quarter-rate packet row with `n~8p ln p` has `K~2p ln p>p` and does NOT enter that large-characteristic regime. The increasing-characteristic and large-characteristic relative-to-message-degree questions must be separated.

There is an elementary obstruction to fixing this by adding complete fibers in several directions. Let a domain D of size n in ANY F_(p^m) contain R distinct affine F_p-lines. Every line has p points and two distinct lines meet in at most one. If d_x counts the chosen lines through x, then

    sum d_x=Rp,
    sum d_x^2 <= Rp+R(R-1).

Cauchy–Schwarz gives `(Rp)^2/n <= Rp+R(R-1)`, and, for R>0 and n<p^2,

    R <= n(p-1)/(p^2-n).

Therefore n<=C p implies R=O_C(1) as p grows; with fixed positive rate and p>K this is O_rho(1). This holds for arbitrary ambient extension degree, without parallelism or a common quotient. It excludes a growing bank of DISTINCT COMPLETE affine p-lines in the relevant regime, not arbitrary polynomial supports or unions of partial lines.

Accordingly the concrete transversal proposal should first be tested with a FIXED small m satisfying `rho m<1`, rather than only with m~log p. At quarter rate, m=3 gives n=3p and K=floor(3p/4)<p; each truncated transversal has three points, so the full-line obstruction does not apply. A bank formed from many such small pieces would still need the common high-coefficient cancellation lemma already identified above. No such lemma is currently proved. This fixed-m version is the appropriate target if the aim is to enter the DKT characteristic range; the logarithmic-m version only improves the older increasing-characteristic extension-field contract.


## Follow-up comparison after the scaled-Frobenius theorem

The completed `quadratic_frobenius_core/scaled_fiber_padding.tex` now gives N=9p², K=3, threshold 4p, both-source/common agreement at most 2p+3, and (p+1)(p−1)² singleton exceptions plus one two-word exception over F_(p⁴). Its multiplicity-six finite DKT certificate has derivative cap three, so p>3 suffices for reconstruction. This supplies an actual large-characteristic extension-field line, not just the partial-support proposal above.

A fresh read of the binary repository's endpoint and source-conversion updates does not dominate it. The proper-domain boundary b=p,d=3 has K=p, N=p³ and p³+p²+p exceptional labels: its characteristic guard passes, but its count is only linear in length. The punctured trace boundary b=p,N=p²,K=1 can gain both-source/common agreement exactly one after source conversion into F_(p⁴), while retaining p² labels and threshold p−1. This has a large source gap but only linear count. The new source conversion does not increase the exceptional population or lower the code dimension of the other endpoint families.

The substantive open upgrade remains a prime-alphabet analogue, a fixed-rate example in the applicable error range, or an exceptional-count improvement that preserves the existing gap. The current completed construction does not settle those targets.
