# OR tensor amplification: an exact fixed-gap obstruction

This tests a nonlinear amplification distinct from inherited pullback and disjoint-block CRT localization: form products of discrepancies, so a tuple agrees whenever **any** component agrees. It supplies a quantitative obstruction, not a new construction or an upper bound for arbitrary correlated families.

## Incidence theorem (no formula or coordinate assumptions)

For block i=1,...,B let Ω_i have n_i elements. Every label s in a set of at least two labels specifies an agreement subset S_(i,s) of size A_i. Put a_i=A_i/n_i. On the Cartesian domain Ω=∏Ω_i, a tuple s has prescribed OR agreement set

    U_s={x: x_i∈S_(i,s_i) for at least one i}.

Its size is N a, where N=∏n_i and a=1−∏(1−a_i). Suppose all tuples are represented by DISTINCT univariate polynomials of degree≤D on any N distinct field nodes, with one received word, respecting these labeled agreements. This permits arbitrary embeddings of the product domain, moving nodes and word values, and nonlinear coefficient formulas.

Two tuples differing only in coordinate i share at least all matches in the other coordinates. Therefore their nonzero polynomial difference has at least

    N[1−∏_(j≠i)(1−a_j)]

roots. Writing ρ=D/N gives

    a−ρ ≤ min_i a_i∏_(j≠i)(1−a_j).                 (1)

If there are two labels in coordinate i whose support intersection has size C_i, choose those labels instead. The sharper inequality is

    a−ρ ≤ min_i (a_i−C_i/n_i)∏_(j≠i)(1−a_j).      (2)

These bounds apply to the carried OR threshold. Additional newly created matches outside U_s are not bounded by this argument.

## Sharp universal optimization of (1)

If some a_i=1, the bound is zero for B≥2. Otherwise put t_i=a_i/(1−a_i) and t=min_i t_i. The right side of (1) is

    min_i t_i /∏(1+t_j) ≤ t/(1+t)^B.

The latter function is maximized at t=1/(B−1), with value

    (1/B)(1−1/B)^(B−1) < 1/B.                    (3)

Thus even allowing the seed agreement fractions to vary with B, a full Cartesian OR construction cannot retain a fixed positive agreement gap above the effective degree rate. The dimension rate (D+1)/N only strengthens the obstruction. A fixed positive margin above the DKT first-order curve is also impossible, since that curve exceeds capacity. For a fixed q-label seed the list size is q^B, so (3) is O(1/log L). The constant 1/e is the asymptotic optimum of this incidence-only bound.

The extremizer a_i=1/B is not claimed algebraically realizable. It proves that tuning progressively sparser inner agreements does not rescue the OR operation.

## Application to the actual rational cubic banks

All three current exact banks have7 agreements per candidate and cubic pair differences. They contain the original eight candidates, two of which share3 old coordinates; therefore C_i=3 is available, and no pair can share more than3 distinct coordinates. For B repeated copies, (2) gives:

| seed | Cartesian list | carried OR fraction | upper bound on a−D/N |
|---|---:|---:|---:|
| eight on16 | 8^B | 1−(9/16)^B | (1/4)(9/16)^(B−1) |
| ten on18 | 10^B | 1−(11/18)^B | (2/9)(11/18)^(B−1) |
| eleven on19 | 11^B | 1−(12/19)^B | (4/19)(12/19)^(B−1) |

Thus their strongest possible carried OR margin vanishes exponentially in the number of factors. Common-zero insertion preserves A−D while increasing length; unramified polynomial pullback scales all three quantities equally; no-match padding only worsens the margin. These subsequent operations cannot repair the decay. Arbitrary puncturing or new matches require separate analysis.

## Correlated tuples: fixed-density amplification is also excluded

The full Cartesian hypothesis is unnecessary when the product failure probability tends to zero. Let C be ANY selected tuple family containing at least two distinct realized polynomials. Assume, as above, that every label at coordinate i has the same support size A_i, and put F=∏_i(1−a_i). Every carried OR support has size N(1−F). For two tuples s,t, define

    c_i(s,t)=|S_(i,s_i)∩S_(i,t_i)|/n_i.

Inclusion–exclusion on the product domain gives the exact intersection fraction

    |U_s∩U_t|/N = 1−2F+∏_i[1−2a_i+c_i(s,t)].

The bracket is the proportion outside both component supports, so it is nonnegative. The pair root bound therefore gives

    a−D/N ≤ F−∏_i[1−2a_i+c_i(s,t)] ≤ F.          (5)

In particular, no positive-distance or positive-rate outer code repairs the fixed-seed OR construction: for repeated eight-, ten-, or eleven-cubic seeds, ANY bank of at least two distinct polynomials has carried gap at most (9/16)^B, (11/18)^B, or (12/19)^B, respectively. This includes arbitrary correlated tuple selection and requires neither coordinate-neighbor pairs nor an explicit product formula. The simpler inequality |U_s∩U_t|≥2|U_s|−N proves the same final bound.

More generally (5) tends to zero whenever Σ_i a_i tends to infinity, since F≤exp(−Σ_i a_i). Supports and received values may move arbitrarily provided the final domain retains the product-incidence labeling and all candidates match one common word on the asserted OR supports. This is an exact distinct-node result, independent of characteristic.

If support sizes vary with the label, use each tuple's actual OR support size. Whenever every selected tuple has failure fraction at most ε_B→0, any two share at least (1−2ε_B)N coordinates. Thus a common carried threshold at most N has agreement-minus-degree fraction at most 2ε_B. Equal support sizes yield the sharper bound (5).

## Explicit polynomial CRT realization has an additional degree cost

For pairwise coprime n_i and N=∏n_i, the map μ_N→∏μ_(n_i), x↦(x^(N/n_i)), is a bijection. Suppose block i has a received polynomial W_i of degree h_i strictly larger than its candidate degrees, and maximum degree d_i of a difference between its candidates. Consider

    F_s(X)=H(X)−∏_i[W_i(X^(N/n_i))−P_(i,s_i)(X^(N/n_i))].

It matches H on U_s. The common polynomial H may cancel any common high-degree terms. Nonetheless, changing only label i gives an exact polynomial difference of degree

    Σ_(j≠i) h_j N/n_j + d_i N/n_i.

Hence every degree cap satisfies

    D/N ≥ max_i [Σ_(j≠i)h_j/n_j + d_i/n_i].       (4)

No common subtraction, normalization, or cancellation of the shared leading product can improve (4): it is the degree of an actual pair difference. Also h_i≥A_i by the root bound for W_i−P_(i,s_i). This explicit realization is therefore at least as constrained as the incidence theorem, typically much more so. Degree reduction modulo X^N−1 is a different realization, but still obeys (1)–(3) whenever the resulting polynomials remain distinct and retain the OR supports.

## Exact remaining escape

A correlated outer code remains a possible escape only when the component agreement densities are diluted enough that ∏(1−a_i) does not tend to zero, for example a_i≈1/B. In that regime the coordinate-neighbor argument (1) need not apply, while (5) alone need not vanish. The original fixed-density eight-, ten-, and eleven-cubic seeds do NOT have this escape. Creating additional agreements outside the OR supports is a separate possible mechanism, but when the carried supports already approach full density the pairwise degree lower bound still forces D/N→1 and therefore forbids any fixed positive normalized gap, even if the actual agreement threshold is larger.

No correlated sparse construction or new-match mechanism is supplied here. A prospective scalable family must specify both the coupling and its polynomial realization; outer-code distance alone does not provide the missing algebraic dependencies.

This result is separate from the already archived disjoint-block support obstruction in ../dickson_domain_deformation/GLUING_SUPPORT_GATE.md. It addresses overlapping OR cylinders on a Cartesian domain, whose agreement fraction increases toward1, rather than the sum of agreements on disjoint blocks.
