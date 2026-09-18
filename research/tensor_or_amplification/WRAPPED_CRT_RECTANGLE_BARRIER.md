# Wrapped CRT products: coefficient-rectangle rigidity

**Update:** FULL_WRAPPED_CRT_BARRIER.md now proves the general wrapped result, including every zero-constant chart, with agreement gap at most2 max_i(h_i/n_i). The limitations below describe the intermediate proof, not the final scope.
This closes the modular-wrapping escape for factors with nonzero constant coefficients, even for arbitrary correlated tuple families. It extends the unreduced theorem and explicitly isolates the remaining zero-constant chart.

## Setup

Let n_i>1 be pairwise coprime, N=∏n_i, 1≤h_i<n_i, w_i=h_i/n_i, σ=Σw_i, and ε=max w_i. Work over a field of characteristic not dividing N. For coordinate i and label s let f_(i,s)(Z) have degree exactly h_i and a NONZERO leading coefficient independent of s. Initially assume every f_(i,s)(0) is nonzero.

For any selected set of tuples define reduced polynomials

    P_s(X) = H(X) − ∏_i f_(i,s_i)(X^(N/n_i))  mod (X^N−1),

with the unique representative of degree<N. H is common. Suppose all P_s have degree≤D, put ρ=D/N, and require at least two tuples with different factor vectors. The tuple family need not contain any coordinate-neighbor pair.

Then

    ρ ≥ min(σ−ε, 1−2ε).                                (1)

## Unique CRT coefficient locations

For multiindices 0≤e_i≤h_i, the exponents Σe_i N/n_i are distinct MODULO N. If two residues agree, reducing their difference modulo n_i and using gcd(N/n_i,n_i)=1 gives e_i=e'_i modulo n_i; their ranges force equality. Therefore reduction modulo X^N−1 does not sum distinct multivariate coefficients: it only permutes their locations.

For two tuples s,t, all product coefficients at residue exponents>D agree, since both reduced P_s and P_t have degree≤D and H cancels.

## Greedy high-frequency rectangle

Suppose contrary to (1) that ρ<σ−ε and ρ<1−2ε. Fix coordinate i. The sum of the other weights is σ−w_i>ρ. Greedily add other coordinates until their weight sum u first exceeds ρ. Then

    ρ<u≤ρ+ε,       u+w_i<1.

Let S be the resulting subset. In all coordinates j≠i, choose exponent h_j if j∈S and exponent0 otherwise. Let the i-th exponent vary through0,...,h_i. Every resulting exponent, divided by N, is u+e_i/n_i, strictly betweenρ and1. Thus the entire coefficient line lies above D without wrapping.

Its coefficients for tuple s are K_s times the coefficient vector of f_(i,s_i), where K_s is a product of leading or constant coefficients from other coordinates. K_s and K_t are nonzero. Equality of the high coefficients at e_i=h_i, whose leading coefficient is fixed and nonzero, gives K_s=K_t. Equality of the remaining coefficients then gives f_(i,s_i)=f_(i,t_i). This holds for every i, contradicting the two distinct factor vectors. This proves (1).

For the simple proposed factors f_(i,s)=Z^h_i−a_(i,s), with nonzero labels a_(i,s), it suffices to compare the two coefficients at e_i=0,h_i: their ratio is −a_(i,s). The full rectangle proof shows that constant candidates are not essential.

## Agreement consequence

On μ_N the received word is H. The product vanishes exactly when one factor vanishes. If each coordinate factor has A_i roots in μ_(n_i), with a_i=A_i/n_i, the exact agreement fraction is

    a=1−∏(1−a_i) ≤ min(Σa_i,1) ≤ min(σ,1).

Combining with (1),

    a−ρ ≤ 2ε.                                         (2)

Hence diluted factors with max h_i/n_i→0 cannot give a fixed positive capacity gap, even AFTER reduction modulo X^N−1, for any correlated tuple family. Actual dimension rate only strengthens the conclusion. If root counts vary with the label, each tuple still has agreement≤min(σ,1), so the same bound holds for every candidate and every common threshold.

When max a_i→0, Σa_i→λ>0, and ε→0, the stronger asymptotic bound is

    limsup(a−ρ) ≤ 1−e^(−λ)−min(λ,1) < 0.

No unproved cancellation or degree-order preservation after wrapping is used: the high rectangle is deliberately chosen in an interval with no wrap, and residue injectivity identifies its coefficients exactly.

## Exceptional zero constants: a quantitative partial extension

Do not simply discard labels with zero constant term. For a particular pair of tuples define

    Z={j: f_(j,s_j)(0) f_(j,t_j)(0)=0},  τ=Σ_(j∈Z)w_j.

If τ+ε<1, the same conclusion holds. For coordinate i initialize S with Z\{i}, so every other-coordinate exponent0 coefficient used by either tuple is nonzero. If its initial sum already exceedsρ, keep it; otherwise greedily add coordinates until the sum exceedsρ. Since σ−w_i>ρ this is possible. The final sum u satisfies

    ρ<u≤max(Σ_(Z\{i})w_j, ρ+ε),

and u+w_i<1 follows from τ+ε<1 and ρ+2ε<1. The previous coefficient-line proof therefore applies.

Consequently ANY pair of different factor vectors yielding degree≤D must satisfy at least one of

    ρ ≥ min(σ−ε,1−2ε),    or    τ ≥ 1−ε.             (3)

Thus the only remaining zero-constant escape at low degree has substantial total CRT weight: the union of coordinates with a zero constant must carry weight at least1−ε for every exceptional pair. No exclusion of that remaining chart is claimed. Changing the received word away from H or abandoning the product factorization is also outside this theorem.
