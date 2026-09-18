# Nonrectangular TCap and B: exact fixed-cap barriers

No primary-source gain results from these gates. At fixed TCap multiplicity226 and jet caps312/70, arbitrary Y-downward full-prefix supports cannot prove the old total common-divisor cap9275 for **any** challenge cap L. At fixed B multiplicity134 and jet caps185/40, allowing those supports does not lower its minimum challenge cap below22192.

These are exclusions of the stated dimension/rank sufficient tests, not of actual source kernels or common divisors. Cross-coordinate dependencies beyond the sum of one-point ranks remain outside the tests.

## Exact graph gates

All cases use n=262144, w=131071, A=181275 and D=mA. The graph and rank proofs are in `INDEPENDENT_FORMULA_AUDIT.md`. The extraction is saturated in each case: D-(w-1)Q is74310 for TCap and42900 for B, exceeding m-1.

| Gate | m | Q | R cap | L | Maximum surplus |
|---|---:|---:|---:|---:|---:|
| TCap old-total rectangular optimum |226|312|70|9281|0|
| TCap asymptotic slope |226|312|70|weights1|909424303|
| B old challenge cap |134|185|40|18992|0|
| B one below repaired threshold |134|185|40|22191|0|

The slope gate uses coefficient benefits D-wi-(w-1)j and challenge weights one in each rank block. It therefore maximizes the exact coefficient of L in the surplus. Its maximizing support is the entire19738-monomial ambient box. The other gates return the empty support.

`mincut_gate.cpp` supplies the exact64-bit optimization. The sparse primal flows and residual cuts are in the correspondingly named `.flow` and `.json` files. `verify_receipt.py` separately streams the flow, reconstructs every original capacity, verifies conservation and flow=cut, then recomputes the selected support's coefficient count and Pascal rank. All four receipts passed; this replay took3.21seconds and32MiB. The largest optimization used about156MiB and2.67seconds.

## Positive-feasibility monotonicity under L

For a fixed support S of maximum jet degree qmax≤L, write its margin

    G_S(L)=sum_q (L+1-q)*a_q,

where a_q is the coefficient benefit minus n times the unweighted local rank on diagonal q. Let A_h=sum_(q≤h)a_q. If G_S(L)>0, the maximum prefix A_h is positive. Truncate S after a maximizing prefix h. This remains Y-downward. For the removed tail, every relative partial sum A_t-A_h is nonpositive, so summation by parts with decreasing positive weights proves that truncation cannot decrease G_S(L). The truncated support has positive unweighted surplus A_h, and consequently remains positive for every larger L.

Thus an exact zero optimum at L0 excludes positive feasibility at every L≤L0, including smaller L where the available total-degree cap is truncated. This argument does not assume the margin of an arbitrary untrimmed support is monotone.

For B, the L22191 cut therefore rules out all smaller L. The already verified rectangular source has positive surplus28698360 at L22192. Hence22192 is the exact least L in the entire stated downward-support class at these fixed m and jet caps.

## TCap quotient penalty for every L

A total common-divisor cap T requires restricted-kernel nullity larger than the full coefficient count of the quotient box with challenge cap

    u=L-T-1.

Retaining the FULL primary kernel is valid: the restricted kernel embeds in it. If every full-kernel element were divisible by a factor of total degree at least T+1, division would inject the restricted kernel into that full quotient box. Thus the sufficient test is

    G_S(L)>C(D,L-T-1,70),

with quotient count zero if L≤T. No support-specific quotient erosion is assumed.

Take T=9275. For L≤9281 the preceding monotonicity argument and the zero cut exclude even positive nullity. For L>9281, the two graph bounds give, for every support,

    G_S(L) <=909424303*(L-9281).

Here u=L-9276≥6. Exact coefficient counts are

    C(D,5,70)=2275866530,
    C(D,6,70)-C(D,5,70)=1132428304.

The quotient first differences are nondecreasing because successive challenge diagonals add nonnegative coefficient widths. Therefore

    C(D,u,70) >=2275866530+(u-5)*1132428304
              >909424303*(u-5)
              =909424303*(L-9281).

The strong TCap test fails for every L. This extends the earlier rectangular all-L failure to every Y-downward full-prefix monomial subset at this fixed m and these jet caps.

## Downstream scope

The frozen TCap total9275 would have preserved the old aggregate total box, while B's old L18992 would have reduced pair and derivative-chain costs. Neither is recovered. These proofs do not cover changing m or the jet caps, support-sensitive quotient bounds, nonmonomial restrictions, or genuinely global constraint dependencies. They do not improve the binding MCA cost or constitute a full ledger recomputation.
