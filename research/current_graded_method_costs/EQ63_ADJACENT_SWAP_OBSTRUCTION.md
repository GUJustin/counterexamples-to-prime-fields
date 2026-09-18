**Subsequent result:** `EQ63_GROUPED_POSITIVE_SORTING.md` resolves positive feasibility by allowing excess deletion and prefix trimming before grouped shifts. The counterexamples and elementary normalizations below remain valid; their formerly open question is answered by that broader operation.

# Exact Eq63 adjacent-swap formula and a whole-margin obstruction

This checks the entire weighted dimension-minus-rank expression, not merely one of its moments. It does not disprove a sorting principle restricted to positive feasible supports.

Let w_q=(H-q+1)_+, d=D-1, and take saturated full coefficient prefixes. Swap adjacent inverted column heights a<b at derivative indices s,s+1. The common support has height a in both columns. Excess monomials u=a,...,b-1 move from (u,s+1) to (u,s), hence from degree q=u+s+1 to q-1. Put C_u=mA-Du-d(s+1).

For each local rank grade ell, write c_{q,ell} for the number of common-support monomials on diagonal q with Y0 exponent at most ell, and

    e_{q,ell}=1{c_{q,ell}<m-ell}.

The exact change in the UNNORMALIZED Eq63 margin is

    sum_{u=a}^{b-1} [w_{q-1}(C_u+d)-w_q C_u]
    - n sum_{u=a}^{b-1} sum_{ell=u}^{m-1}
             [w_{q-1} e_{q-1,ell}-w_q e_{q,ell}].       (1)

This follows directly from the saturated rank formula sum_ell min(c,m-ell). Each excess contributes at most one monomial to a fixed diagonal, so its increment is exactly the displayed indicator. The formula includes arbitrary surrounding columns and truncated challenge weights.

## Counterexample to unconditional monotonicity

Take heights (0,1), so the sole jet monomial Y1 is sorted to 1. Both saturated ranks equal m. Formula (1) becomes

    M_sorted-M_original=mA+dH-nm.

At H=m it is negative whenever A+D-1<n. This holds near the quarter-rate critical agreement for all sufficiently large admissible lengths. Saturation is automatic once mA-d>=m. Thus even the WHOLE Eq63 margin can decrease under sorting, under the intended near-critical and saturated hypotheses.

This need not rely on a missing zeroth column. Take heights (1,2) sorted to (2,1), and m>=3,H>=2. The common support is {1,Y1}. The moving monomial Y0Y1 has old local rank m-1; its new marginal rank beside Y1 is m-2. Therefore

    M_sorted-M_original
      =mA-2D+1-n(m-1)+H(n+D-1).

For H approximately m/4, A/n approximately a0, and large n,m, its leading coefficient divided by nm is a0-1+5/16<0. Both supports contain 1 and all coefficients are saturated. This again concerns the actual complete margin.

A concrete direct-rank check uses n=65536,D=16383,A=30723,m=256,H=64.
The corrected margin epsilon* is approximately0.0000606658, inside the
specified interval. The original margin is -1710112451, the sorted margin
is -1713749056, and the difference is -3636605, exactly as above.

## What remains open

Both examples have negative Eq63 margins; they do not produce a support beating the fourth-power bound or refute preservation of POSITIVE feasibility under a carefully chosen grouped sorting operation. The first example reverses sign at H=m(n-A)/(D-1), so it cannot obstruct a large-height theorem. A useful remaining target is either a positive-support sorting theorem, or a direct negative-prefix-area bound for merely Y0-downward supports. The Eq64 sorting proof cannot be imported: its row weight is constant, precisely the property absent in (1).
