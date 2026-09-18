# Moment-cancelled translated-coset trees: a bounded transfer test

2026-09-18. Read-only extraction from the binary repository's AGENTS.md, current-status/strategy, and `sections/constructions/additive-support-trees.tex`; also checked the existing `LOCATORS_TREES_NORMS_TRANSFER.md`. No binary-repository edits. This note tests joint cancellation across translated leaves, which is stronger than requiring each translated leaf to retain its own gap.

## What actually creates the binary population

At fixed height h, the binary construction has t=2^(h−1) disjoint affine-flat leaves. Each leaf has a large translation-stable locator gap. The product therefore has a common high-degree part. Essential dual spaces and recovery of branching functionals certify that the Θ(N^(2^h−1)) counted templates are DISTINCT SUPPORTS, not merely recursive descriptions. Exterior-pole averaging converts those supports into distinct labels, with a separate field-size collision cost. Copying the locator-gap identity without this support population does not transfer the theorem.

Consider a concrete prime-field replacement: permit the t leaves to be arbitrary translated multiplicative cosets, and permit their centers to vary JOINTLY so that moments cancel across branches. A leaf has monic locator

    (X−c)^m−a,   a≠0,

where m|(p−1). Its full m roots must belong to one fixed evaluation domain D⊂F_p. Leaves in a support are disjoint. We count actual supports of size T=tm, not parameter descriptions.

## Low-dimensional rigidity lemma

Assume p>tm+t, m>t+K, and a family of such supports has locators L_S satisfying

    deg(L_S−L_S')≤K

for every pair. Then either the family has only one support, or all leaves have one common center and the family has at most floor(|D|/(tm)) distinct supports.

In particular K=3 and m>t+3 cannot give a growing overlapping-support population through this mechanism. It also excludes logarithmically many leaves when m≫log|D|. This is a statement about this specific equal-leaf-size translated-coset model, not all prime-field support trees.

### 1. The joint leading coefficients recover every center

Put C_S(X)=∏_(leaves i)(X−c_i), counting repeated centers. Expanding the leaf product shows

    L_S(X)=C_S(X)^m + terms of degree≤tm−m.

Because m>t, the first t nonleading coefficients are those of C_S^m. They are common throughout the family, since tm−t>K. The map from the first t coefficients of monic C_S to those of C_S^m is triangular, with diagonal coefficient m≠0. Thus C_S itself is fixed: the entire multiset of leaf centers, including multiplicities, is recovered. Joint moment cancellation does not leave a changing center tree.

### 2. Distinct fixed centers cannot retain hidden radius freedom

Let the distinct centers be c_1,...,c_q with multiplicities t_1,...,t_q, Σt_i=t. Group the radii at each center:

    L_S=∏_i [Σ_(j=0)^(t_i) (−1)^j e_(i,j)(S)(X−c_i)^(m(t_i−j))],
    e_(i,0)=1.

Here e_(i,j) is the j-th elementary symmetric function of the leaf radii at c_i. Compare two locators and induct on j. Suppose all e_(i,l) agree for l<j. At total removed-leaf level j the only possibly changing terms are the individual e_(i,j). If

    P0=∏_i (X−c_i)^(mt_i),

their contribution is

    (−1)^j P0 Σ_(i:t_i≥j) δe_(i,j)/(X−c_i)^(jm).

All remaining differences have degree at most T−(j+1)m. Let q_j be the number of active centers. The first q_j coefficients of this displayed contribution must vanish whenever T−jm−(q_j−1)>K. Dividing formally by the common monic P0 reduces these equations to the first q_j terms of

    Σ_i δe_(i,j) X^(−jm)(1−c_i/X)^(−jm).

Their coefficient matrix is a Vandermonde matrix in the distinct c_i, with row factors binom(jm+l−1,l), 0≤l<q_j. Those factors are nonzero because p>tm+t. Hence every δe_(i,j)=0.

If q≥2, then j≤max t_i≤t−1, so T−jm≥m and q_j≤t. Our assumption m>t+K guarantees the required inequality at EVERY level. The induction fixes all radii as multisets, hence the full locator and support. This proves the one-support conclusion for multiple centers.

### 3. One center permits only disjoint supports

If q=1, every locator is a polynomial in (X−c)^m. Since K<m, their differences can only be constants. Distinct such locators have no common root, so their supports are pairwise disjoint subsets of D. There are at most floor(|D|/T) of them. This counts supports directly and does not rely on an injective tree description.

## Fixed-rate, fixed-height version

A simpler consequence applies without the low-dimensional assumption. Suppose t is fixed, m=Theta(|D|), and the common locator gap g satisfies g>t and m>t, meaning deg differences≤tm−g. The center-recovery argument still fixes all centers. For each fixed center, at most floor(|D|/m) complete translated μ_m cosets lie in D, since these cosets are disjoint. Consequently the number of actual supports is at most

    (floor(|D|/m))^t=O_t(1).

Thus even jointly moment-cancelled translated leaves cannot reproduce the fixed-height binary polynomial support population at a fixed fractional gap. This extends the old individual-translation objection: the centers are recovered from the COMMON prefix even when no individual leaf is assumed to preserve its gap.

## Implication for the requested construction

In a direct pole compiler with locator corrections of degree≤K, each distinct support supplies at most one label. The lemma therefore prevents this proposed prime-field replacement from yielding n log n labels at dimension3 and agreement T=Theta(sqrt n): its only nontrivial surviving family has at most n/T=O(sqrt n) supports. Multiplying by a fixed core locator only increases the correction degree and does not evade the bound when the same degree budget is retained.

A successful binary-inspired transfer needs leaves other than equal-size translated multiplicative cosets, or cancellations not represented by a common low-degree locator correction, or a different received-line compiler. This audit establishes no universal impossibility and proposes no new computation. The decisive missing positive ingredient remains a large family of genuinely different overlapping split locators with a common long prefix; fixed-height translated-coset trees do not supply it even after allowing collective moment cancellation.
