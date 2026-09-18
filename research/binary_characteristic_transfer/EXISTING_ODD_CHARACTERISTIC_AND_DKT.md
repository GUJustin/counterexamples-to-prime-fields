# Existing characteristic extensions and the DKT comparison

Read-only audit, September 18, 2026. No files in the binary-field repository were changed.

## Conclusion

An extension from characteristic two to fixed odd characteristic is already proved in the binary-field project, including near-Johnson ordinary lists, two individually far sources, exact native-field endpoints, and all-rate/all-challenge conclusions on linear domains. Reproving an odd-characteristic analogue would not be a new direction. The remaining distinction is **prime ambient field / characteristic large compared with message degree**, not simply odd characteristic.

“Native field” means no additional challenge-field extension. It does not mean prime field. Likewise, a proper affine linear domain need not be a subfield, although its growing dimension uses a proper scalar subfield of the ambient field.

## Strongest existing contracts

Sources below are relative to `/Users/jthaler/Documents/binary_field_counterexamples/`. The labels are stable LaTeX labels; theorem numbers follow the current status document.

### Near-Johnson lists and two far sources: all prime powers

`sections/constructions/fullfield-elliptic.tex`, `thm:fullfield-elliptic` (Theorem 4.10), already allows every prime power b. Let B=F_(b^(2n)), let D be B or an F_b-hyperplane, let d=dim(D), h=2n-d in {0,1}, and N=b^d. For 2≤t≤n-h, put

    M=b^(2t)(b^t-1) [n-h choose t]_(b²),
    delta=(b-1)N/b^(2t).

The low-rate contract is K=N/b², T=N/b-(b-1)N/b^(t+1), L=M/(b-1). The complementary high-rate contract is K=(b-1)²N/b², T=(b-1)N/b-N/b^(t+1), L=M. There are at least L distinct degree-<K explanations with exactly T matches. For any containing field F of size q>N, the associated pair has CA=agr(g)=K and at least

    ceil(L(q-N)/(q-N+delta(L-1)))-1

nonzero bad challenges. The stated bounds on agr(f) are strictly below T. Thus this is already a two-far-source result, not merely a common-agreement statement.

For fixed b and t=d/4+O(1), log_b L=d²/8+O_b(d), while T/N=√(K/N)-Theta_b(N^(-1/4)). In particular b=3 already gives rates 1/9 and 4/9 with agreements tending to 1/3 and 2/3. This is a strong fixed-odd-characteristic extension.

The fixed-codimension corollary `cor:elliptic-fixed-codimension` gives T=√(NK)-O(√N), a constant fraction of the challenge field bad, and both sources far. With positive domain codimension the challenge field can be B itself; for the full domain the displayed pole compiler requires an outer extension. In either case the growing F_b-vector-space dimension is essential to this construction.

### Exact native endpoints: all prime powers, with explicit two-far guarantees

`sections/constructions/near-unit-probability.tex`, `thm:hyperplane-near-unit` (Theorem 4.14): for any prime power b and proper affine F_b-domain D of size N=b^d, d≥3, the low endpoint is K=N/b², T=N/b, with CA=agr(g)=K, agr(f)≤(b+1)K/2-1, and exactly b(N-1)/(b-1) nonzero bad challenges. A complementary high-rate statement holds for b>2 with the same exact count and both sources far.

The full-native-field endpoint (Theorem 4.15), B=D=F_N, N=b^m, m≥4, has exactly (N-b)/(b-1) bad challenges. Its bad probability tends to 1/(b-1); its common agreement and second-source agreement are between K and K+b-1, with the displayed first-source bound below threshold. Thus the binary near-unit probability should not be silently transferred to odd b. The odd-characteristic native conclusion is already present, but its limiting probability is different.

### Every fixed characteristic, arbitrary linear domains, all rates

`sections/constructions/quadratic-near-johnson.tex`, `cor:arbitrary-domain-all-rates` and `rem:fixed-characteristic-all-rates`, explicitly extend **all conclusions** to every fixed characteristic p on F_p-linear domains, with p-dependent constants and onset.

At each fixed rate rho and exponent s, a threshold alpha in (rho,√rho), exact common agreement J=floor(rho N), and bad probability

    ≥ 1/(1+C_(rho,s,p) q/N^s)-1/q

are available. Polynomially bounded challenge fields can have every challenge bad by taking s sufficiently large. This is not a uniform near-Johnson claim: alpha and constants depend on the chosen exponent.

The two-far refinements have different field/count contracts. Converting a construction over B into a proper extension F makes both individual agreements exactly J while retaining the B-based count. Retaining the original q-dependent count with both sources far uses the stronger extension-degree hypothesis [F:B]≥s+1. These should not be merged into a single native all-challenge/two-far assertion.

## Growing characteristic: the retained weakening already in the archive

`research/frontier/characteristic-and-domains.md`, “Incomplete Artin--Schreier packets,” uses E=F_(p²), phi(X)=X^p-X, and D=phi^(-1)(Y) with |Y|=m. For 2≤h<m≤p,

    N=mp, K=(h-1)p, T=hp, L=binom(m,h).

With m=(8+o(1)) ln p divisible by 4, h=m/4+1, and challenge field F_(p^4), the existing result is

    p=Theta(N/log N), K=N/4,
    T/N-K/N=Theta(1/log N),
    #bad=Omega(N³/log⁴ N), Pr[bad]≥1/(4N).

This is the strongest retained near-linear-characteristic fixed-rate tradeoff identified in the audit. It still uses complete F_p-fibers and a proper extension field. Its capacity gap shrinks, and eventually p<K-1. It therefore does not contradict a fixed-gap or large-characteristic DKT upper bound.

The archive already explains the obstruction to upgrading this one-direction construction: compositions on complete phi-fibers descend to the m-point quotient, preserving rate and agreement. A proper packet union cannot simultaneously be invariant under a second independent F_p-translation direction. A new fixed-gap construction would need a genuinely different mechanism, rather than another choice of packets.

## Matched DKT comparison

The current primary-source extraction is `../prime_field_tightness/EPRINT_2056_COMPARISON.md`, based on the September 2026 145-page public ePrint 2026/2056, SHA256 b67c188ec477b6063caf9c1c06b214c71e358ff09b9517adcdb1db212ea2700a. This audit checks the comparison of stated hypotheses, not the entire upper-bound proof.

* At agreement a_1(rho)+eta_1, the first-order bounds are O_rho(N/eta_1²) for lists and O_rho(N²/eta_1⁴) for full-agreement-set MCA exceptions. The counting characteristic guard is char 0 or p>max(K-1,B_partial). The decoder has the weaker p>K-1 guard.
* The current capacity theorem has characteristic guard p>K-1, with gap-dependent polynomial exponents and minimum length. A shrinking gap cannot be substituted into a fixed-gap comparison while holding those constants/exponents fixed.
* These results are not restricted to prime ambient fields. Extension fields meeting the characteristic guard are also covered.
* At rate 1/4, a_1=(3+√133)/31≈0.46879234. The binary project's concrete cited bound at agreement at least 0.49 is 1.325775e6 N² under the stated large-characteristic hypotheses. The fixed-small-characteristic counterexamples are outside those hypotheses.

For fixed b (hence fixed characteristic) and growing N, the positive-rate constructions above have K growing and fail p>K-1. Their near-Johnson thresholds can exceed the first-order threshold, but that does not fix the failed characteristic hypothesis. Conversely, native-field constant bad probability is only O(N) bad labels when q=N; it is not by itself a contradiction to an O(N²) count.

Do not overstate this as “all extension-field examples fail the characteristic guard.” For example the proper-domain endpoint d=3,b=p has K=p, so p>K-1 holds. Its rate is 1/p², its bad count is only linear in N, and it does not give the forbidden fixed-rate superquadratic comparison. Field structure, rate, threshold, and count must all be matched.

## What is genuinely open or useful to weaken

1. **Fixed odd characteristic:** already solved in substantial generality; not a new transfer target.
2. **Growing characteristic at quarter rate:** the packet result above already gives a precise weakening, with shrinking capacity gap and p=Theta(N/log N). It is compatible with the existing upper-bound landscape.
3. **Prime ambient fields with growing N at fixed positive rate:** none of the linear-domain mechanisms above transfers directly. F_p has F_p-dimension one. Passing to F_(p^m) changes the alphabet class; calling it native does not repair that distinction.
4. **Large characteristic above the message degree:** a superquadratic exceptional count at a fixed first-order margin would contradict the stated DKT theorem. A plausible matching target is instead an Omega(N²) lower bound in that regime, or a capacity-regime lower bound below the first-order curve. Our existing quadratic-extension ordinary-CA constructions already provide quadratic counts at fixed capacity gaps, but do not give a prime-ambient or first-order matching result.

The useful next question is therefore a new prime-field/large-characteristic mechanism at a carefully matched threshold, rather than another odd-characteristic version of the binary constructions.
