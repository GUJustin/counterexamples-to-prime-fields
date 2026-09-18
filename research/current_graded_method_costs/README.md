# What the quarter-rate converse proves for the current graded ledger

**Current result:** Both Eq63 and Eq64 have necessary fourth-power regular-MCA
ledger cost for all Y0-downward monomial supports with full derivative-weighted
coefficient prefixes. `ORDER_IDEAL_FOURTH_POWER.md` proves the mandatory-triangle
case. `EQ63_GROUPED_POSITIVE_SORTING.md` reduces positive row-test certificates
to that case by excess deletion, prefix trimming, and grouped shifts; the
column test uses weighted height sorting. Arbitrary rearrangement need not
improve a graded margin. Independent proof audits are saved alongside both
arguments. The body below records the earlier missing step and its motivation;
that monomial-support gap is now closed. HOMOGENEOUS_NONMONOMIAL_TRANSFER.md
also proves the Eq63 result for total-degree-graded translation-stable jet
spaces, preserving exact finite prefixes. Arbitrary filtered nonmonomial
spaces, nonmonomial Eq64, equal-weight cutoffs, global kernel dependencies
and actual list lower bounds remain outside the integrated result.

September17,2026. A method-level consequence and a precise remaining lemma.
This concerns the numerical upper bounds produced by a specified proof
method. It is **not** an intrinsic lower bound on list sizes or exceptions,
and gives no better.codes improvement.

## A proved current-method list-cost lower bound

Use the exact full-coefficient monomial model of
`../first_order_support_audit/FINITE_LENGTH_GAP_COSTS.md`. In particular,
n>=12 is divisible by4, D=n/4-1, the monomial jet support is downward in
Y0, and characteristic is zero or exceeds its retained total jet degree.
Set

    a*=(An-8)/(n(n-8)), epsilon*=a*-(3+sqrt(133))/31,
    c0=(1-2(3+sqrt(133))/31)/8.

Assume 0<epsilon*<=1/2000 and positive source-minus-local-rank surplus.
The audited exact reduction gives

    m>c0/epsilon*, U>m/4, V>m/4-1, m>=16.

For declared total jet bound B and derivative bound b, we have
B>=U and b>=V>=m/8, so Bb>m²/32.

The CURRENT ePrint's Eq54 defines

    tau=2D-3,
    u=1+tau(B-1), v=min(u,tau(b-1)+D),
    F=Bv+b(u-v).

Here D>=2, B>=2, 1<=b<=B, and v>=0. Consequently

    F=bu+(B-b)v >=bu >=DbB/4 >Dm²/128.

Indeed tau>=D/2 and B-1>=B/2. Therefore even its sharper Eq56 list
budget lambda*F+S, with lambda>=1 and S>=0, costs

    Omega(D/(epsilon*)²).

This establishes the second inverse-gap power as necessary for THIS
squarefree numerical list ledger under the audited interpolation model.
It does not assume the obsolete cubic reconstruction formula. Eq57 is a
coarser version and inherits the same lower bound. It does not say every
first-order list proof, or actual list, has that cost.

## What graded challenge counting alone currently yields

Write G_q and R_q for the exact source dimension and local rank on total
jet degree q. For integer H>=0, current Eq63, for an affine received line,
requires

    sum_q (H-q+1)_+ (G_q-n R_q)>0.

Define prefix surplus P_j=sum_(q<=j)(G_q-n R_q). The left side is exactly
sum_(j=0)^H P_j. Thus some prefix P_j is positive with j<=H. Total-degree
truncation preserves downward Y0 closure and full coefficient prefixes.
Apply the audited finite-length parameter converse to that prefix: its
maximum derivative exponent exceeds m/4-1, but is at most j. Hence

    H>=j>m/4-1>=m/8.

Together with the preceding Bb bound, the current Eq54 joint degree

    J=H(2uv-v²)+2(1+tau H)F

satisfies

    J>=2 tau H F >=D² H Bb/4 >D²m³/1024.

The term 2uv-v² is nonnegative since 0<=v<=u. Every multiplier of J
in Eq55 is at least1, for all its allowed incidence thresholds L. Thus
optimizing L cannot remove this necessary cost. The currently proved
conclusion for the graded regular-family ledger is only

    Omega(D²/(epsilon*)³).

This falls one inverse-gap power short of the paper's fourth-power upper
bound. The old uniform-height converse would give H=Omega((epsilon*)^-2),
but Eq63 is different and that conclusion has NOT been transferred.
For epsilon>=1/n, epsilon* is of order epsilon; the corrected scale is
necessary near integer rounding.

## The former missing step (now resolved by grouped positive sorting)

In the leading normalized model, let d_q=B_q-R_q and P_j=sum_(q<=j)d_q.
For every positive-benefit prefix the audited ratio estimate gives

    P_j<=8 epsilon R_j<=8 epsilon R_H.

(The assertion is automatic for nonpositive P_j.) To force H=Omega(m/epsilon)
through the graded inequality, one sufficient new lemma would be a uniform
negative-prefix-area bound for graded-feasible supports:

    sum_(j=0)^H max(-P_j,0) >= c m R_H

with an absolute c>0 near quarter-rate critical agreement. Positivity of
sum P_j would then imply

    8 epsilon (H+1) R_H > c m R_H.

This is a useful target formulation, NOT a proved claim. Equivalent
first-moment bounds could suffice. In the untruncated case H>=Jmax,
the condition is

    (H+1) Delta > sum_q q d_q.

A suitable lower bound on that signed first moment, relative to mR, would
supply the missing factor. The present scalar estimate R/Delta>=1/(8epsilon)
does not control the moment. In truncated cases even the unweighted
truncated surplus need not be positive; Eq63 need not be monotone in H.

For logical clarity, aggregate parameter inequalities by themselves
cannot prove the desired result. Abstract degree arrays concentrated at
q=m with R_q=m² and B_q=(1+epsilon)m² satisfy R/Delta=1/epsilon and can
be assigned U=V=m/2, B=m, yet pass the graded inequality already at H=m.
These arrays are NOT asserted realizable by the local rank model. They
only demonstrate why degree lower bounds plus a small surplus ratio do
not replace a geometric/moment argument about actual supports.

The sorting/diagonal-compression arguments in the existing audit optimize
unweighted benefit minus rank. No proof has been supplied that they
preserve or improve this graded signed first moment. Applying them as
though they did would be a gap. The possible new route is a weighted
compression or near-extremizer stability theorem, followed by an exact
finite-length reduction. The new grouped positive-sorting theorem now supplies the reduction to
`ORDER_IDEAL_FOURTH_POWER.md`, closing this gap for all Y0-downward
full-prefix monomial supports.

## Scope and source

The conclusion concerns Eq63 graded row counts, not every alternative
column-only test or arbitrary global kernel exploitation. It does not
assert a finite-length nonmonomial theorem beyond the existing audit.
Current reconstruction formulas: ePrint2026/2056, Eq54--58, pages45--48;
graded Eq63, page50. Cached authoritative PDF checksum:
b67c188ec477b6063caf9c1c06b214c71e358ff09b9517adcdb1db212ea2700a.
The order-ideal extension is separately proved in the linked note; no
formal verification or independent human referee is claimed.

The companion also proves a filtered-row-test corollary for translation-stable jet spaces of maximum total degree d≤D. Its ranks are target-image filtration increments, and its test is derived directly from primary Lemma 3.12; it agrees with Eq63 on homogeneous sources. This does not claim that Proposition 5.10 itself states a nonmonomial theorem. Exact finite coefficient-prefix preservation and an independent audit are in FILTERED_NONMONOMIAL_SCOPE.md and FILTERED_NONMONOMIAL_INDEPENDENT_AUDIT.md under research/current_graded_method_costs/.
