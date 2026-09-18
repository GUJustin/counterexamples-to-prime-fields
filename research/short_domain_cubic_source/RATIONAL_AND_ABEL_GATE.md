# Constructive short-domain attempts with genuine first-order identities

## Outcome and priorities

No short-domain fixed-gap growing source is constructed here. The two most explicit characteristic-zero replacements for the Frobenius Dickson identity can be built as actual polynomial differential-equation banks, but their agreement geometry forbids the required growing list. These are exact family-specific gates, not a universal nonexistence claim.

Mechanisms considered, in order:

1. Polynomial specializations of rational first-integral pencils. This gives an explicit Riccati identity and arbitrarily large polynomial banks; the obstruction below concerns their common-word agreements rather than existence of solutions.
2. Reciprocal solutions of nonintegrable Abel equations. This is genuinely distinct from the Riccati pencil and has a polynomial divisor formulation. An exact uniqueness argument again bounds fixed-gap lists.
3. Equations with a quadratic value-dependent derivative coefficient, analogous to the successful Dickson cubic. These permit two moving singular value branches and escape both gates. The missing positive step is to realize such branches in a characteristic-zero or short-domain polynomial bank without reintroducing the original Frobenius relation p=4k+1.

The small-exponent scaled Dickson family already studied via the Corvaja–Zannier common-core obstruction is not repeated here.

## 1. Actual Riccati bank from a rational pencil

Choose polynomials B,R,h over a field and distinct constants a in a set C of size L. Suppose each h−a divides R. Then

    P_a=B+R/(h−a)

is polynomial and satisfies the common equation

    R(P_a′−B′)−R′(P_a−B)+h′(P_a−B)²=0.           (1)

This has derivative degree one and total jet degree two. For instance R=product_{a in C}(h−a) gives arbitrarily many polynomial solutions in characteristic zero, and specialization to sufficiently large primes preserves them. Thus existence of a large actual solution bank is not the issue.

Let every P_a have degree≤D and let a word on n distinct coordinates agree with every selected candidate on at least A coordinates. At a coordinate where R(x)≠0, the values are injective in a. At R(x)=0, all values except possibly the one parameter a=h(x) equal B(x); polynomial evaluation at that exceptional denominator is understood by cancellation. Any other bucket is a singleton.

Let S be the coordinates where R(x)=0 and the word equals B(x). Each coordinate of S belongs to at least L−1 candidate supports. Outside S there is at most one candidate agreement. Pairwise root counting therefore gives, for L>2,

    |S| binom(L−1,2) ≤ D binom(L,2),
    LA ≤ L|S|+n,

and hence

    A−D ≤ 2D/(L−2)+n/L.                          (2)

At A−D≥eta n and D≤rho n, (2) forces L=O_rho(1/eta). This gate permits an arbitrary high-degree B and therefore accounts for cancellation of common leading coefficients.

The subsequent direct incidence argument sharpens this to `L(A−D)≤n`, even with the arbitrary offset. Let h_x count candidates matching the received value, and b_x count all agreeing candidate pairs at x. The bucket description gives h_x in {0,1,L−1,L}, so `(h_x−1)(L−1)≤2b_x`. Summing and using `sum_x b_x≤D binom(L,2)` gives the sharper bound. The previous note's warning that this stronger statement was unjustified is superseded by this proof; a bound on the degree of B is not needed.

The same calculation is independent of characteristic and of the size of the ambient field. Rational reparametrization or taking much larger splitting primes does not alter this collision pattern.

## 2. A distinct reciprocal-Abel construction and its exact gate

The reciprocal transformation y=1/P in y′=A_0(X)y³+B_0(X)y² gives a polynomial equation of the form

    P P′−B P+A_0=0.                             (3)

Equivalently, nonzero solutions are polynomial divisors of A_0 satisfying

    P′+A_0/P=B.

This offers a concrete algebraic generation problem beyond rational Riccati pencils. Related polynomial-divisor formulations are studied in Bravo–Calderón–Fernández–Ojeda, *Rational Solutions of Abel Differential Equations*, Proposition 2.1, https://arxiv.org/html/2109.07853v1. The agreement conclusion below is a direct argument, not a cited classification.

Assume characteristic zero or p>D. For distinct degree≤D solutions P,Q, subtract (3) after dividing in the rational function field:

    (P−Q)′=A_0(P−Q)/(PQ).                        (4)

If P(x)=Q(x)≠0, the right side has vanishing order at least ord_x(P−Q), whereas the left has order exactly one less. The latter assertion follows because that positive order is at most D<p (or characteristic is zero). This is impossible. Thus distinct solutions can share a value only when that value is zero.

For any received word, each nonzero candidate has at most D agreements at zero-valued coordinates. At all nonzero-valued coordinates there is at most one agreement across the bank. Consequently

    L(A−D)≤n                                    (5)

for any list of L nonzero polynomial solutions with A>D agreements each. An identically zero solution, possible only if A_0=0, contributes at most one additional list member. In particular no fixed-gap growing list exists in this family, even if the polynomial divisor problem yields many actual solutions.

## Remaining constructive target

The successful Dickson equation has derivative coefficient 4X(2G²−1−X^(2k)), rather than a coefficient linear in the value. Distinct solution graphs can meet on two moving nonzero value branches, which is exactly what (3) lacks. Replacing its Frobenius identity by a characteristic-zero polynomial identity is still the unresolved step.

A useful new source must therefore do more than supply many polynomial sections of a Riccati pencil or many reciprocal Abel solutions. It needs multiple shared value branches whose common word can have more than D+eta n agreements per candidate, with a bank size tending to infinity and p/n tending to infinity. No such identity is established in this bounded attempt; no random scan or new lower-bound claim is made.
