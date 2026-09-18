# Correlated low-density CRT products: exact unreduced degree obstruction

**Update:** FULL_WRAPPED_CRT_BARRIER.md now proves the general wrapped result, including every zero-constant chart, with agreement gap at most2 max_i(h_i/n_i). The limitations below describe the intermediate proof, not the final scope.
This closes the explicit multiplicative-CRT product formula even for correlated tuple banks in the diluted regime. It does not close arbitrary univariate realizations of those incidence patterns, or unrestricted reduction modulo the domain locator.

## Hypotheses and exact identity

Let n_1,...,n_B>1 be pairwise coprime, N=∏n_i, and work over a field containing μ_N with characteristic not dividing N. Set X_i=X^(N/n_i). In coordinate i fix a received polynomial W_i of degree h_i<n_i, and candidate polynomials P_(i,s) of degree strictly less than h_i. For ANY selected tuple set C consider

    F_s(X)=H(X)−∏_i[W_i(X_i)−P_(i,s_i)(X_i)],

where H is common to the whole bank. Require at least two distinct tuples differing as polynomial factors; no Cartesian closure or coordinate-neighbor assumption is made.

For s≠t, let I be the coordinates where P_(i,s_i)≠P_(i,t_i), and let d_i be the degree of their difference. Then

    deg(F_s−F_t)=Σ_j h_j N/n_j − min_(i∈I)(h_i−d_i)N/n_i.    (1)

Proof: telescope the difference of the two products in any coordinate order. The term indexed by a changed coordinate i contains its nonzero factor difference and unchanged-degree factors in all other coordinates, hence has exactly the degree displayed for that i. All those degrees are distinct. Indeed equality for i≠j would imply

    (h_i−d_i)n_j=(h_j−d_j)n_i.

Coprimality implies n_i divides h_i−d_i, impossible because0<h_i−d_i<n_i. Therefore the maximum-degree telescoping term is unique and cannot cancel. This argument works in every allowed characteristic; the common polynomial H cancels from the difference. In particular no correlated leading-coefficient or moment constraints among the tuple labels can change (1).

## Degree and agreement ledger

Suppose each label in coordinate i has A_i agreements with W_i on μ_(n_i), put a_i=A_i/n_i, σ=Σh_i/n_i, and ε=max_i h_i/n_i. Since W_i−P_(i,s) is nonzero, A_i≤h_i. The CRT map μ_N→∏μ_(n_i) is a bijection, so every tuple has EXACT agreement fraction with the word H

    a=1−∏_i(1−a_i).

Every common degree cap D for at least two F_s satisfies, by (1),

    D/N ≥ σ−ε.

Since a≤Σa_i≤σ,

    a−D/N ≤ ε.                                             (2)

Thus if h_i/n_i tends uniformly to zero, explicit correlated CRT discrepancy products cannot have a fixed positive carried gap above capacity. This conclusion is independent of the outer-code cardinality, rate, and distance.

If max a_i→0 and Σa_i→λ with0<λ<∞, then a→1−e^(−λ), while liminf D/N≥λ provided ε→0. The limiting gap is at most

    1−e^(−λ)−λ < 0.                                       (3)

So the common low-density proposal a_i≈λ/B is strictly below capacity in this explicit model. Fixed-degree seeds diluted by adding unused inner coordinates have ε=O(1/B) when n_i are all Ω(B). Pairwise coprimality of the chosen inner lengths must still be enforced; it is not free for repeated identical domains.

For this explicit formula and received word H, there are no additional coincidences outside the OR supports: over a field the discrepancy product vanishes if and only if at least one factor vanishes. Therefore (2)–(3) bound the actual agreement, not merely a chosen subset of matches. Changing the received word away from H is a different mechanism.

## Modulo the domain locator: exact caveat

If σ<1, every product already has degree<N. Reducing modulo X^N−1 changes nothing, and the theorem also applies to the reduced realization. More generally it applies to a particular pair whenever its exact degree in (1) is<N.

Without that condition, reduction can lower the degree. Although all multivariate monomials ∏X_i^(e_i),0≤e_i≤h_i<n_i, have DISTINCT exponent residues modulo N, their numerical ordering changes on wrapping around N. Injectivity of residues prevents coefficient cancellation but does not preserve the highest degree.

Explicit example over Q: n=(3,5,7), h=(2,4,6), N=105. Compare products

    (X^70−1)(X^84−1)(X^90−1)
    (X^70−2)(X^84−2)(X^90−2).

Their difference is

    X^174+X^160+X^154−3X^90−3X^84−3X^70+7,

of degree174, exactly as (1) predicts. Modulo X^105−1 it becomes

    −3X^90−3X^84−3X^70+X^69+X^55+X^49+7,

of degree90. Thus applying (1) to an arbitrary reduced polynomial would be false. This example is not a high-agreement construction; it isolates the precise logical gap.

A modularly reduced CRT product with σ≥1 remains a separate possible algebraic mechanism. The abstract incidence inequalities of OR_TENSOR_BARRIER.md continue to apply, including the fixed-density correlated obstruction, but do not settle diluted correlated products after wrapping.
